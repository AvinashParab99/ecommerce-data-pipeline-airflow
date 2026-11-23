from sqlalchemy import create_engine, text
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

def load_api_data(df):

    DB_URL = os.getenv("DB_URL")

    engine = create_engine(DB_URL)

    insert_query = text("""
        INSERT INTO api_posts (id, user_id, title, body)
        VALUES (:id, :userId, :title, :body)
        ON CONFLICT (id) DO NOTHING
    """)

    records = df.to_dict("records")

    with engine.begin() as connection:
        connection.execute(insert_query, records)

    engine.dispose()

    print("API data loaded successfully!")


def extract_incremental_data():

    url = "https://jsonplaceholder.typicode.com/posts"

    last_id = get_last_processed_id()

    print("Last Processed ID:", last_id)

    all_data = []
    start = last_id
    limit = 10

    while True:

        params = {
            "_start": start,
            "_limit": limit
        }

        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        if not data:
            break

        all_data.extend(data)

        print("Fetched:", len(data))

        start += len(data)

    return pd.DataFrame(all_data)

def extract_paginated_data():

    url = "https://jsonplaceholder.typicode.com/posts"

    all_data = []
    page = 1
    limit = 10

    while True:

        params = {
            "_page": page,
            "_limit": limit
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            break

        all_data.extend(data)

        print(f"Page {page}: {len(data)} records fetched")

        page += 1

    df = pd.DataFrame(all_data)

    print("\nTotal Records:", len(df))
    print("Shape:", df.shape)

    return df


def get_last_processed_id():

    engine = create_engine(
        "postgresql+psycopg2://postgres:Avinash@localhost:5432/ecommerce_db"
    )

    query = text("SELECT COALESCE(MAX(id), 0) FROM api_posts")

    with engine.connect() as connection:
        last_id = connection.execute(query).scalar()

    engine.dispose()

    return last_id



def extract_api_data():
    url = "https://jsonplaceholder.typicode.com/posts"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    data = response.json()

    # JSON to DataFrame
    df = pd.DataFrame(data)

    print("Total Records:", len(df))
    print("\nFirst 5 Records:")
    print(df.head())

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:", df.shape)


    #Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

# Check duplicate records
    print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicates
    df = df.drop_duplicates()

# Remove records with missing important fields
    df = df.dropna(subset=["id", "title", "body"])

    print("\nAfter Cleaning:")
    print("Shape:", df.shape)


    return df



# if __name__ == "__main__":

#     df = extract_paginated_data()

#     df = df.drop_duplicates()
#     df = df.dropna(subset=["id", "title", "body"])

#     print("\nFinal Records:", len(df))

#     load_api_data(df)

if __name__ == "__main__":

    df = extract_incremental_data()

    print("New Records:", len(df))

    if not df.empty:
        load_api_data(df)
    else:
        print("No new records found.")