# snowflake_ingest.py

import logging
import snowflake.connector
from config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)

def connect_to_snowflake(user, password, account, warehouse, database, schema):
    try:
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
        )
        logging.info("Connected to Snowflake.")
        return conn
    except Exception as e:
        logging.error(f"Snowflake connection failed: {e}")
        return None

def insert_logs(conn, table_name, df):
    if df.empty:
        logging.warning("No data to insert into Snowflake.")
        return

    cursor = conn.cursor()
    try:
        for _, row in df.iterrows():
            values = tuple(row.values)
            placeholders = ','.join(['%s'] * len(values))
            query = f"INSERT INTO {table_name} VALUES ({placeholders})"
            cursor.execute(query, values)
        logging.info(f"Inserted {len(df)} rows into {table_name}.")
    except Exception as e:
        logging.error(f"Failed to insert logs: {e}")
    finally:
        cursor.close()
