import pandas as pd

def transform_data(data):
    if not data:
        print("No data to transform")
        return None

    df = pd.DataFrame(data)

    # seleccionar columnas importantes
    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume"
    ]]

    print("Data transformed successfully!")
    return df
