import os
import pandas as pd
import logging

logger = logging.getLogger(__name__)

OUTPUT_PATH = "data/crypto_data.csv"

def load_data(df: pd.DataFrame) -> bool:
    """
    Save transformed DataFrame to a CSV file.

    Args:
        df: Cleaned DataFrame to persist.

    Returns:
        True if the file was saved successfully, False otherwise.
    """
    if df is None or df.empty:
        logger.warning("No data to load. Skipping file write.")
        return False

    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        df.to_csv(OUTPUT_PATH, index=False)
        logger.info(f"{len(df)} records saved to '{OUTPUT_PATH}'.")
        return True

    except PermissionError:
        logger.error(f"Permission denied when writing to '{OUTPUT_PATH}'.")
    except Exception as e:
        logger.error(f"Unexpected error during load: {e}")

    return False
