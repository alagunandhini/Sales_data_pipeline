import pandas as pd
import os
from extract import extract_data

def save_silver(customers, products, orders):

    os.makedirs("silver", exist_ok=True)

    customers.to_csv(
        "silver/customers_clean.csv",
        index=False
    )

    products.to_csv(
        "silver/products_clean.csv",
        index=False
    )

    orders.to_csv(
        "silver/orders_clean.csv",
        index=False
    )

    print("Silver data saved successfully.")


def transform_data(customers, products, orders):

    # Remove duplicate customers
    customers = customers.drop_duplicates()

    # Handle missing customer emails
    customers["email"] = customers["email"].fillna("unknown")

    # Clean customer names
    customers["name"] = customers["name"].str.strip().str.title()

    # Clean product categories
    products["category"] = products["category"].str.strip()

    # Convert order date
    orders["order_date"] = pd.to_datetime(orders["order_date"])

    # Add product price to orders
    orders = orders.merge(
        products[["product_id", "price"]],
        on="product_id",
        how="left"
    )

    # Calculate total amount
    orders["total_amount"] = (
        orders["quantity"] * orders["price"]
    )

    return customers, products, orders


if __name__ == "__main__":

    customers, products, orders = extract_data()
    print(customers)

    customers, products, orders = transform_data(
        customers,
        products,
        orders
    )
    save_silver(
        customers,
        products,
        orders
    )


    print("========== CLEAN CUSTOMERS ==========")
    print(customers)

    print("\n========== CLEAN PRODUCTS ==========")
    print(products)

    print("\n========== TRANSFORMED ORDERS ==========")
    print(orders)

    print("\nTotal Revenue:")
    print(orders["total_amount"].sum())