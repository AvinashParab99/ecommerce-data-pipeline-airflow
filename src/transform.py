
import pandas as pd

def transform_data(df):

    df = df.copy()

    # 1. Calculate Revenue
    df["revenue"] = df["quantity"] * df["price"]

    # 2. Convert product names to uppercase
    df["product"] = df["product"].str.upper()

    # 3. Create order category
    df["order_category"] = df["status"].apply(
        lambda x: "Completed" if x == "Delivered" else "In Progress"
    )

    print("\nTransformed Data:")
    print(df)

    # 4. Calculate total revenue
    total_revenue = df["revenue"].sum()

    print("\nTotal Revenue:", total_revenue)

    return df


if __name__ == "__main__":
    from src.extract import extract_data
    from src.clean import clean_data

    raw_data = extract_data()
    clean_df = clean_data(raw_data)
    transformed_df = transform_data(clean_df)
