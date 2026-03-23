from extract import extract_data


def main():
    print("Starting ETL pipeline...")

    data = extract_data()

    if data:
        print(f"Extracted {len(data)} records")
        print(data[0])  # muestra un ejemplo


if __name__ == "__main__":
    main()
