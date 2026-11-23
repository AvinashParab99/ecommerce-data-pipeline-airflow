
def validate_data(df):

    required_columns = [
        "order_id",
        "customer_id",
        "product",
        "quantity",
        "price",
        "status",
        "revenue",
        "order_category"
    ]

    # Check required columns
    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    # Check empty data
    if df.empty:
        raise ValueError("No data available")

    # Check duplicate order IDs
    if df["order_id"].duplicated().any():
        raise ValueError("Duplicate order IDs found")

    # Check invalid quantity
    if (df["quantity"] <= 0).any():
        raise ValueError("Invalid quantity found")

    # Check missing values
    if df[required_columns].isnull().any().any():
        raise ValueError("Missing values found")

    print("Data quality validation passed!")

    return df
