
import pandas as pd
from pathlib import Path


def extract_data():

    # Project root directory
    project_dir = Path(__file__).resolve().parent.parent

    # CSV file path
    file_path = project_dir / "data" / "raw" / "orders.csv"

    df = pd.read_csv(file_path)

    print("Data extracted successfully!")
    print("Total Rows:", len(df))
    print("Columns:", df.columns.tolist())

    return df


if __name__ == "__main__":
    raw_data = extract_data()
    print(raw_data.head())
