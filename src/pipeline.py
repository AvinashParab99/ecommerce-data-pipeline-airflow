
import logging
from pathlib import Path

from src.extract import extract_data
from src.clean import clean_data
from src.transform import transform_data
from src.validate import validate_data
from src.load import load_data

# Logging configuration
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


def run_pipeline():

    try:
        logging.info("Pipeline started")

        # 1. Extract
        raw_data = extract_data()
        logging.info(f"Extracted {len(raw_data)} records")

        # 2. Clean
        clean_df = clean_data(raw_data)
        logging.info(f"Cleaned records: {len(clean_df)}")

        # 3. Transform
        transformed_df = transform_data(clean_df)
        logging.info("Transformation completed")

        # 4. Validate
        validated_df = validate_data(transformed_df)
        logging.info("Validation completed")

        # 5. Load
        load_data(validated_df)
        logging.info("Data loaded successfully")

        logging.info("Pipeline completed successfully")

    except Exception:
        logging.exception("Pipeline failed")
        raise


if __name__ == "__main__":
    run_pipeline()
