import logging
from pathlib import Path

from src.extract import extract_data
from src.clean import clean_data
from src.transform import transform_data
from src.load import load_data

# Create logs folder
Path("logs").mkdir(exist_ok=True)

# Logging configuration
logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)

def run_pipeline():

    try:
        logging.info("Pipeline started")

        # Extract
        raw_data = extract_data()
        logging.info(f"Extracted {len(raw_data)} records")

        # Clean
        clean_df = clean_data(raw_data)
        logging.info(f"Cleaned records: {len(clean_df)}")

        # Transform
        transformed_df = transform_data(clean_df)
        logging.info("Transformation completed")

        from src.validate import validate_data
        transformed_df = transform_data(clean_df)

        validated_df = validate_data(transformed_df)

        load_data(validated_df)

        # Load
        load_data(transformed_df)
        logging.info("Data loaded successfully")

        logging.info("Pipeline completed successfully")

    except Exception:
        logging.exception("Pipeline failed")
        raise

if __name__ == "__main__":
    run_pipeline()
