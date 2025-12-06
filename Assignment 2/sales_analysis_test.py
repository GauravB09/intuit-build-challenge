import unittest
from sales_analysis import SalesAnalyzer, Sale

class SalesAnalyzerTest(unittest.TestCase):

    def setUp(self):
        # Small dataset to verify calculations
        self.mock_data = [
            Sale("2023-01-15", "Laptop", "Electronics", 1, 1000.0, "North"),
            Sale("2023-01-15", "Sofa", "Furniture", 1, 500.0, "North"),
            Sale("2023-01-20", "Mouse", "Electronics", 2, 50.0, "South"),
            Sale("2023-02-10", "Desk", "Furniture", 1, 500.0, "East"),
            Sale("2023-02-15", "Chair", "Furniture", 2, 100.0, "West")
        ]
        self.app = SalesAnalyzer("test", data=self.mock_data)

    def test_total_revenue(self):
        # expected: 1000 * 1 + 500 * 1 + 50 * 2 + 500 * 1 + 100 * 2 = 2300
        self.assertEqual(self.app.get_total_revenue(), 2300.0)

    def test_sales_count_by_category(self):
        self.assertEqual(self.app.get_sales_count_by_category("Electronics"), 2)
        self.assertEqual(self.app.get_sales_count_by_category("Furniture"), 3)

    def test_average_price_per_region(self):
        # North has 1000 and 500, avg should be 750
        avgs = self.app.get_average_price_per_region()
        self.assertEqual(avgs["North"], 750.0)

    def test_top_product(self):
        # Mouse (2) and Chair (2) are tied for highest quantity
        top = self.app.get_top_product_by_quantity()
        self.assertIn(top[0], ["Mouse", "Chair"])
        self.assertEqual(top[1], 2)

    def test_monthly_revenue(self):
        stats = self.app.get_monthly_revenue()
        # Jan: 1000 + 100 = 1100
        self.assertEqual(stats["2023-01"], 1600.0)
        # Feb: 500 + 200 = 700
        self.assertEqual(stats["2023-02"], 700.0)

    def test_high_value_transactions(self):
        # only Laptop (1000) and Sofa/Desk (500) are > 400
        high_rollers = self.app.get_high_value_transactions(400)
        self.assertEqual(len(high_rollers), 3)
        self.assertEqual(high_rollers[0].product, "Laptop")
        self.assertEqual(high_rollers[1].product, "Sofa")
        self.assertEqual(high_rollers[2].product, "Desk")

    def test_empty_data(self):
        empty_app = SalesAnalyzer("test", data=[])
        self.assertEqual(empty_app.get_total_revenue(), 0.0)
        self.assertEqual(empty_app.get_monthly_revenue(), {})

if __name__ == '__main__':
    unittest.main()