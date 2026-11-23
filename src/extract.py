import pandas as pd


def extract_data():

    file_path = "C:/Users/ADMIN/PycharmProjects/ecome data pipe line engin/data/raw/orders.csv"

    df = pd.read_csv(file_path)

    print("Data extracted successfully!")
    print(df)
    print("\nTotal Rows:", len(df))

    print("\nColumns:", df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 3 Records:")
    print(df.head(3))
    

    return df


if __name__ == "__main__":
    from src.clean import clean_data
 

    raw_data = extract_data()

    clean_data(raw_data)