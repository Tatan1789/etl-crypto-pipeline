from extract import extract_data
from transform import transform_data
from load import load_data


def main():
    print("Starting ETL pipeline...")

    data = extract_data()

    if data:
        print(f"Extracted {len(data)} records")

        df = transform_data(data)

        if df is not None:
            load_data(df)


if __name__ == "__main__":
    main()
