from sqlalchemy import create_engine

def load_to_db(df):
    # SQLite database file will be created automatically
    engine = create_engine("sqlite:///data.db")

    # Insert data into table
    df.to_sql("crypto_prices", con=engine, if_exists="append", index=False)

    print("Data loaded successfully into database (data.db)")


if __name__ == "__main__":
    print("Run pipeline.py to load real API data into database")