# 🪙 ETL Crypto Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)
![API](https://img.shields.io/badge/API-CoinGecko-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

End-to-end ETL pipeline that extracts cryptocurrency market data from the CoinGecko public API, transforms it into a clean structured format, and loads it into a CSV file ready for analysis.

---

## 📋 Overview

| Step | Description | Module |
|------|-------------|--------|
| **Extract** | Fetch top 10 cryptos by market cap from CoinGecko | `src/extract.py` |
| **Transform** | Clean data, add timestamp, validate nulls | `src/transform.py` |
| **Load** | Save processed data to CSV | `src/load.py` |
```
CoinGecko API → extract.py → transform.py → load.py → data/crypto_data.csv
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.10+** | Core language |
| **Pandas** | Data transformation |
| **Requests** | HTTP calls to CoinGecko API |
| **CSV** | Lightweight data storage |

---

## 📁 Project Structure
```
etl-crypto-pipeline/
├── data/
│   └── .gitkeep          # Output folder (CSV files excluded via .gitignore)
├── notebook/
│   └── etl_crypto_pipeline.ipynb   # Full pipeline walkthrough
├── src/
│   ├── extract.py        # API extraction logic
│   ├── transform.py      # Data cleaning and validation
│   ├── load.py           # CSV persistence
│   └── main.py           # Pipeline orchestrator
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/Tatan1789/etl-crypto-pipeline.git
cd etl-crypto-pipeline
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the pipeline**
```bash
python src/main.py
```

**4. Check the output**
```bash
cat data/crypto_data.csv
```

---

## 📊 Output Sample

| id | symbol | name | current_price | market_cap | total_volume | extracted_at |
|---|---|---|---|---|---|---|
| bitcoin | BTC | Bitcoin | 70781.0 | 1415687998467 | 46286462924 | 2024-01-01 12:00:00 UTC |
| ethereum | ETH | Ethereum | 2147.16 | 259199755766 | 22446729989 | 2024-01-01 12:00:00 UTC |

---

## 🔭 Potential Extensions

- **Database storage** → PostgreSQL or BigQuery instead of CSV
- **Scheduling** → Apache Airflow or Prefect DAGs
- **Cloud deployment** → AWS Lambda / GCP Cloud Functions
- **Data quality** → Great Expectations or Pandera
- **Dashboard** → Metabase or Looker Studio

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
