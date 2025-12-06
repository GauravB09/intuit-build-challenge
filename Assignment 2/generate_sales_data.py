import csv
import random
from datetime import datetime, timedelta

def create_sales_data(filename="sales_data.csv", rows=100):
    products = [
        ("Laptop", "Electronics", 1200.00),
        ("Smartphone", "Electronics", 800.00),
        ("Headphones", "Electronics", 150.00),
        ("Chair", "Furniture", 150.00),
        ("Desk", "Furniture", 300.00),
        ("Sofa", "Furniture", 700.00),
        ("Pen", "Stationery", 2.50),
        ("Notebook", "Stationery", 5.00)
    ]
    regions = ["North", "South", "East", "West"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Product", "Category", "Quantity", "UnitPrice", "Region"])

        for _ in range(rows):
            date = (datetime(2023, 1, 1) + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d")
            prod, cat, price = random.choice(products)
            qty = random.randint(1, 10)
            region = random.choice(regions)
            writer.writerow([date, prod, cat, qty, price, region])

    print(f"Generated {filename} with {rows} sales records.")

if __name__ == "__main__":
    create_sales_data()