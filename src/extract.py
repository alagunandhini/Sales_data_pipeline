import pandas as pd
import os


def extract_data():

    customers = pd.read_csv("data/customers.csv")
    products = pd.read_csv("data/products.csv")
    orders = pd.read_csv("data/orders.csv")

    return customers, products, orders


def save_bronze(customers, products, orders):

    os.makedirs("bronze", exist_ok=True)

    customers.to_csv("bronze/customers.csv", index=False)
    products.to_csv("bronze/products.csv", index=False)
    orders.to_csv("bronze/orders.csv", index=False)

    print("Bronze data saved successfully.")


if __name__ == "__main__":

    customers, products, orders = extract_data()

    save_bronze(
        customers,
        products,
        orders
    )