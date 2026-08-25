import time

import pandas as pd
from sqlalchemy import create_engine, text


DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "db"
DB_PORT = "5432"
DB_NAME = "ny_taxi"

GREEN_TRIPS_FILE = "data/green_tripdata_2025-11.parquet"
ZONES_FILE = "data/taxi_zone_lookup.csv"


def get_engine():
    connection_url = (
        f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    return create_engine(connection_url)


def wait_for_postgres(engine, retries=10, delay=2):
    for attempt in range(1, retries + 1):
        try:
            with engine.connect() as connection:
                connection.execute(text("SELECT 1"))

            print("Connected to PostgreSQL")
            return

        except Exception as error:
            print(
                f"PostgreSQL is not ready "
                f"(attempt {attempt}/{retries}): {error}"
            )
            time.sleep(delay)

    raise RuntimeError("Could not connect to PostgreSQL")


def main():
    engine = get_engine()
    wait_for_postgres(engine)

    print("Reading green taxi trips...")
    trips_df = pd.read_parquet(GREEN_TRIPS_FILE)

    print(f"Loaded {len(trips_df)} trip records")

    print("Loading trips into PostgreSQL...")
    trips_df.to_sql(
        name="green_taxi_trips",
        con=engine,
        if_exists="replace",
        index=False,
    )

    print("Reading taxi zones...")
    zones_df = pd.read_csv(ZONES_FILE)

    print(f"Loaded {len(zones_df)} zone records")

    print("Loading zones into PostgreSQL...")
    zones_df.to_sql(
        name="taxi_zones",
        con=engine,
        if_exists="replace",
        index=False,
    )

    print("Ingestion completed successfully")


if __name__ == "__main__":
    main()