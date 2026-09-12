import pandas as pd
import os


def create_gold_data():

    # Read Silver data
    customers = pd.read_csv(
        "silver/customers_clean.csv"
    )

    products = pd.read_csv(
        "silver/products_clean.csv"
    )

    orders = pd.read_csv(
        "silver/orders_clean.csv"
    )

    # Create Gold folder
    os.makedirs("gold", exist_ok=True)

    # ==========================================
    # 1. PRODUCT SALES
    # ==========================================

    product_sales = (
        orders
        .groupby("product_id")["total_amount"]
        .sum()
        .reset_index()
    )

    product_sales = product_sales.merge(
        products[
            ["product_id", "product_name", "category"]
        ],
        on="product_id",
        how="left"
    )

    product_sales = product_sales[
        [
            "product_id",
            "product_name",
            "category",
            "total_amount"
        ]
    ]

    product_sales.to_csv(
        "gold/product_sales.csv",
        index=False
    )

    # ==========================================
    # 2. CUSTOMER SALES
    # ==========================================

    customer_sales = (
        orders
        .groupby("customer_id")["total_amount"]
        .sum()
        .reset_index()
    )

    customer_sales = customer_sales.merge(
        customers[
            ["customer_id", "name", "city"]
        ],
        on="customer_id",
        how="left"
    )

    customer_sales = customer_sales[
        [
            "customer_id",
            "name",
            "city",
            "total_amount"
        ]
    ]

    customer_sales.to_csv(
        "gold/customer_sales.csv",
        index=False
    )

    # ==========================================
    # 3. DAILY SALES
    # ==========================================

    daily_sales = (
        orders
        .groupby("order_date")["total_amount"]
        .sum()
        .reset_index()
    )

    daily_sales.to_csv(
        "gold/daily_sales.csv",
        index=False
    )

    print("Gold data created successfully.")


if __name__ == "__main__":
    create_gold_data()