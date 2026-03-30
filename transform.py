import pandas as pd

def transform_data(raw_data):
    df = pd.DataFrame(raw_data)

    # Only required columns
    df = df[[
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "total_volume",
        "high_24h",
        "low_24h",
        "last_updated"
    ]]

    # Convert last_updated to datetime
    df["last_updated"] = pd.to_datetime(df["last_updated"])

    return df


if __name__ == "__main__":
    # Sample testing
    sample_data = [
        {
            "id": "bitcoin",
            "symbol": "btc",
            "name": "Bitcoin",
            "current_price": 5000000,
            "market_cap": 100000000,
            "total_volume": 200000,
            "high_24h": 5100000,
            "low_24h": 4900000,
            "last_updated": "2026-03-30T10:00:00Z"
        }
    ]

    df = transform_data(sample_data)
    print(df)