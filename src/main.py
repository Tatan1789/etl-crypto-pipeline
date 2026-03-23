import logging
from extract import extract_data
from transform import transform_data
from load import load_data

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


def run_pipeline():
    """Orchestrate the full Extract -> Transform -> Load pipeline."""
    logger.info("=" * 40)
    logger.info("Starting ETL Crypto Pipeline...")
    logger.info("=" * 40)

    # Step 1: Extract
    raw_data = extract_data()
    if raw_data is None:
        logger.error("Pipeline aborted: extraction failed.")
        return

    logger.info(f"Extracted {len(raw_data)} raw records.")

    # Step 2: Transform
    df = transform_data(raw_data)
    if df is None:
        logger.error("Pipeline aborted: transformation failed.")
        return

    # Step 3: Load
    success = load_data(df)

    if success:
        logger.info("Pipeline completed successfully.")
    else:
        logger.error("Pipeline finished with errors during load.")


if __name__ == "__main__":
    run_pipeline()
