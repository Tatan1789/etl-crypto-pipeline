import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

API_URL = "https://api.coingecko.com/api/v3/coins/markets"

def extract_data(vs_currency: str = "usd", top_n: int = 10) -> list | None:
    """
    Fetch top N cryptocurrencies by market cap from CoinGecko API.

    Args:
        vs_currency: Target currency for prices (default: 'usd').
        top_n: Number of coins to retrieve (default: 10).

    Returns:
        List of coin data dicts, or None if the request fails.
    """
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": top_n,
        "page": 1,
    }

    try:
        response = requests.get(API_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info(f"Successfully extracted {len(data)} records from CoinGecko.")
        return data

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error: {e}")
    except requests.exceptions.ConnectionError:
        logger.error("Connection error. Check your internet connection.")
    except requests.exceptions.Timeout:
        logger.error("Request timed out after 10 seconds.")
    except Exception as e:
        logger.error(f"Unexpected error during extraction: {e}")

    return None
