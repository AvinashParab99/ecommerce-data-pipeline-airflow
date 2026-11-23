
import pandas as pd
from sqlalchemy import create_engine, text

import os
from dotenv import load_dotenv
load_dotenv()



def load_data(df):

    

    DB_URL = os.getenv("DB_URL")


    engine = create_engine(DB_URL)

    # Convert DataFrame into records
    records = (
        df.astype(object)
        .where(pd.notna(df), None)
        .to_dict("records")
    )

    insert_query = text("""
        INSERT INTO orders (
            order_id,
            customer_id,
            product,
            quantity,
            price,
            status,
            revenue,
            order_category
        )
        VALUES (
            :order_id,
            :customer_id,
            :product,
            :quantity,
            :price,
            :status,
            :revenue,
            :order_category
        )
        ON CONFLICT (order_id) DO NOTHING
    """)

    try:
        with engine.begin() as connection:
            result = connection.execute(
                insert_query,
                records
            )

        print("New records inserted:", result.rowcount)

    finally:
        engine.dispose()
