import pandas as pd

def clean_data(df):

    df = df.copy()

    print("Original Rows:", len(df))

    # Remove duplicate records
    df = df.drop_duplicates()

    # Separate invalid records
    invalid_quantity = df[df["quantity"] <= 0]

    missing_price = df[df["price"].isnull()]

    rejected = pd.concat([
        invalid_quantity,
        missing_price
    ]).drop_duplicates()

    # Keep valid records
    clean_df = df[
        (df["quantity"] > 0) &
        (df["price"].notnull())
    ].copy()

    print("\nRejected Records:")
    print(rejected)

    print("\nCleaned Records:")
    print(clean_df)

    print("\nFinal Rows:", len(clean_df))

    return clean_df