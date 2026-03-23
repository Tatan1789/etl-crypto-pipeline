import pandas as pd
import logging
from datetime import datetime, timezone

logger = logging.getLogger(__name__)

COLUMNS = ["id", "symbol", "name", "current_price", "market_cap", "total_volume"]

def transform_data(data: list) -> pd.DataFrame | None:
    """
    Transform raw API response into a clean, structured DataFrame.

    Args:
        data: Raw list of coin dicts from the CoinGecko API.

    Returns:
        Cleaned pandas DataFrame, or None if transformation fails.
    """
    if not data:
        logger.warning("No data received for transformation.")
        return None

    try:
        df = pd.DataFrame(data)

        # Select and reorder relevant columns
        df = df[COLUMNS].copy()

        # Add extraction timestamp (UTC)
        df["extracted_at"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

        # Validate: drop rows with nulls in critical numeric columns
        critical_cols = ["current_price", "market_cap", "total_volume"]
        before = len(df)
        df.dropna(subset=critical_cols, inplace=True)
        dropped = before - len(df)
        if dropped > 0:
            logger.warning(f"Dropped {dropped} row(s) with missing critical values.")

        # Normalize symbol to uppercase
        df["symbol"] = df["symbol"].str.upper()

        logger.info(f"Transformation complete. {len(df)} records ready to load.")
        return df

    except KeyError as e:
        logger.error(f"Missing expected column in data: {e}")
    except Exception as e:
        logger.error(f"Unexpected error during transformation: {e}")

    return None
