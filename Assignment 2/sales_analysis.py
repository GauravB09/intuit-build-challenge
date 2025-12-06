import csv
from collections import namedtuple
from stream_util import Stream

# Using namedtuple to keep the data immutable and cleaner than a dict
Sale = namedtuple('Sale', ['date', 'product', 'category', 'quantity', 'unit_price', 'region'])

class SalesAnalyzer:
    def __init__(self, filepath, data=None):
        # Allow passing data directly for testing purposes
        if data is not None:
            self.data = data
        else:
            self.data = self._load_data(filepath)

    def _load_data(self, filepath):
        """Reads CSV and parses fields into Sale objects"""
        sales = []
        try:
            with open(filepath, mode='r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    sales.append(Sale(
                        row['Date'],
                        row['Product'],
                        row['Category'],
                        int(row['Quantity']),
                        float(row['UnitPrice']),
                        row['Region']
                    ))
        except FileNotFoundError:
            print(f"Error: {filepath} not found.")
        return sales

    def get_total_revenue(self):
        """Calculates total revenue (Price * Qty) across all sales."""
        return Stream.of(self.data) \
            .map(lambda s: s.quantity * s.unit_price) \
            .reduce(lambda acc, val: acc + val, 0.0)

    def get_sales_count_by_category(self, category):
        """Counts how many sales records exist for a specific category."""
        return Stream.of(self.data) \
            .filter(lambda s: s.category.lower() == category.lower()) \
            .reduce(lambda count, _: count + 1, 0)

    def get_average_price_per_region(self):
        """Returns dict: {Region: Average Unit Price}."""
        grouped = Stream.of(self.data).group_by(lambda s: s.region)

        result = {}
        for region, items in grouped.items():
            total_price = Stream.of(items).map(lambda s: s.unit_price).reduce(lambda a, b: a + b, 0.0)
            count = len(items)
            result[region] = round(total_price / count, 2)
        return result

    def get_top_product_by_quantity(self):
        """Finds the product with the highest total quantity sold."""
        grouped = Stream.of(self.data).group_by(lambda s: s.product)

        product_totals = []
        for prod, items in grouped.items():
            total_qty = Stream.of(items).map(lambda s: s.quantity).reduce(lambda a, b: a + b, 0)
            product_totals.append((prod, total_qty))

        if not product_totals:
            return None

        # sort descending to put the winner at index 0
        sorted_products = Stream.of(product_totals) \
            .sorted(key=lambda x: x[1], reverse=True) \
            .collect()

        return sorted_products[0]

    def get_monthly_revenue(self):
        """Aggregates revenue by month (YYYY-MM)."""
        grouped = Stream.of(self.data).group_by(lambda s: s.date[:7])

        monthly_stats = {}
        for month, items in grouped.items():
            revenue = Stream.of(items) \
                .map(lambda s: s.quantity * s.unit_price) \
                .reduce(lambda a, b: a + b, 0.0)
            monthly_stats[month] = revenue

        return monthly_stats

    def get_high_value_transactions(self, threshold):
        """Returns sales where total value > threshold."""
        return Stream.of(self.data) \
            .filter(lambda s: (s.quantity * s.unit_price) > threshold) \
            .collect()

if __name__ == "__main__":
    app = SalesAnalyzer("sales_data.csv")

    print("--- Sales Data Analysis ---")
    print(f"Total Revenue: ${app.get_total_revenue():,.2f}")

    print("\n--- Sales Count by Category ---")
    for cat in ["Electronics", "Furniture", "Stationery"]:
        print(f"{cat}: {app.get_sales_count_by_category(cat)}")

    print("\n--- Average Price by Region ---")
    avgs = app.get_average_price_per_region()
    for reg, price in avgs.items():
        print(f"{reg}: ${price}")

    print("\n--- Top Selling Product ---")
    top = app.get_top_product_by_quantity()
    if top:
        print(f"Product: {top[0]}, Total Quantity: {top[1]}")

    print("\n--- Monthly Revenue ---")
    months = app.get_monthly_revenue()
    for m in sorted(months.keys()):
        print(f"{m}: ${months[m]:,.2f}")