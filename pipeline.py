from extract import fetch_crypto_data
from transform import transform_data
from load import load_to_db

def run_pipeline():
    print("Starting API to Database Pipeline...")

    # Extract
    raw_data = fetch_crypto_data()
    if raw_data is None:
        print("Failed to fetch data from API")
        return

    print("Data extracted successfully")

    # Transform
    df = transform_data(raw_data)
    print("Data transformed successfully")
    print(df.head())

    # Load
    load_to_db(df)
    print("Pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()