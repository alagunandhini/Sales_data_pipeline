import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()

# PostgreSQL connection
def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="sales_db",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )

    return connection


# Load customers
def load_customers(connection):

    df = pd.read_csv("silver/customers_clean.csv")

    cursor = connection.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO customers
            (customer_id, name, email, city)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (customer_id) DO NOTHING
            """,
            (
                int(row["customer_id"]),
                row["name"],
                row["email"],
                row["city"]
            )
        )

    connection.commit()

    cursor.close()

    print("Customers loaded successfully.")


# Load products
def load_products(connection):

    df = pd.read_csv("silver/products_clean.csv")

    cursor = connection.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO products
            (product_id, product_name, category, price)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (product_id) DO NOTHING
            """,
            (
                row["product_id"],
                row["product_name"],
                row["category"],
                float(row["price"])
            )
        )

    connection.commit()

    cursor.close()

    print("Products loaded successfully.")


# Load orders
def load_orders(connection):

    df = pd.read_csv("silver/orders_clean.csv")

    cursor = connection.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            """
            INSERT INTO orders
            (order_id, customer_id, product_id,
             quantity, order_date, price, total_amount)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (order_id) DO NOTHING
            """,
            (
                row["order_id"],
                int(row["customer_id"]),
                row["product_id"],
                int(row["quantity"]),
                row["order_date"],
                float(row["price"]),
                float(row["total_amount"])
            )
        )

    connection.commit()

    cursor.close()

    print("Orders loaded successfully.")


if __name__ == "__main__":

    connection = get_connection()

    try:

        load_customers(connection)
        load_products(connection)
        load_orders(connection)

        print("\nAll data loaded successfully!")

    finally:

        connection.close()