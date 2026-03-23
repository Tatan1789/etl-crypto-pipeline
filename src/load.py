import os

def load_data(df):
    if df is None:
        print("No data to load")
        return

    output_path = "data/crypto_data.csv"

    # crear carpeta si no existe
    os.makedirs("data", exist_ok=True)

    df.to_csv(output_path, index=False)

    print(f"Data saved to {output_path}")
