from extract import extract_data
from transform import transform_data


def validate_customers(customers):

    print("========== CUSTOMER DATA QUALITY ==========")

    print("\nMissing values:")
    print(customers.isnull().sum())

    duplicate_ids = customers["customer_id"].duplicated().sum()

    print("\nDuplicate customer IDs:", duplicate_ids)


def validate_products(products):

    print("\n========== PRODUCT DATA QUALITY ==========")

    print("\nMissing values:")
    print(products.isnull().sum())

    duplicate_ids = products["product_id"].duplicated().sum()

    print("\nDuplicate product IDs:", duplicate_ids)

    invalid_prices = (products["price"] <= 0).sum()

    print("Invalid prices:", invalid_prices)


def validate_orders(orders):

    print("\n========== ORDER DATA QUALITY ==========")

    print("\nMissing values:")
    print(orders.isnull().sum())

    duplicate_ids = orders["order_id"].duplicated().sum()

    print("\nDuplicate order IDs:", duplicate_ids)

    invalid_quantity = (orders["quantity"] <= 0).sum()

    print("Invalid quantities:", invalid_quantity)


def validate_customer_references(customers, orders):

    valid_customer_ids = set(customers["customer_id"])

    invalid_orders = orders[
        ~orders["customer_id"].isin(valid_customer_ids)
    ]

    print("\n========== CUSTOMER REFERENCE CHECK ==========")

    print(
        "Orders with invalid customer IDs:",
        len(invalid_orders)
    )


def validate_product_references(products, orders):

    valid_product_ids = set(products["product_id"])

    invalid_orders = orders[
        ~orders["product_id"].isin(valid_product_ids)
    ]

    print("\n========== PRODUCT REFERENCE CHECK ==========")

    print(
        "Orders with invalid product IDs:",
        len(invalid_orders)
    )


if __name__ == "__main__":

    customers, products, orders = extract_data()

    customers, products, orders = transform_data(
        customers,
        products,
        orders
    )

    validate_customers(customers)

    validate_products(products)

    validate_orders(orders)

    validate_customer_references(
        customers,
        orders
    )

    validate_product_references(
        products,
        orders
    )