import unittest
from stream_util import Stream

class StreamUtilTest(unittest.TestCase):
    def test_filter_and_collect(self):
        data = [1, 2, 3, 4, 5]
        result = Stream.of(data).filter(lambda x: x > 3).collect()
        self.assertEqual(result, [4, 5])

    def test_map_and_reduce(self):
        data = [1, 2, 3]
        # Map: double it (2, 4, 6) -> Reduce: sum (12)
        result = Stream.of(data)\
            .map(lambda x: x * 2)\
            .reduce(lambda a, b: a + b, 0)
        self.assertEqual(result, 12)

    def test_group_by(self):
        data = [("A", 10), ("B", 20), ("A", 30)]
        # Group by first element of tuple
        grouped = Stream.of(data).group_by(lambda x: x[0])

        self.assertEqual(len(grouped), 2) # A and B
        self.assertEqual(len(grouped["A"]), 2) # Two items for A
        self.assertEqual(grouped["B"][0][1], 20)

    def test_sorted(self):
        data = [3, 1, 4, 2]
        result = Stream.of(data).sorted().collect()
        self.assertEqual(result, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()