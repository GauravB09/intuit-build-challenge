import functools
import itertools

class Stream:
    """
    Simple wrapper class to chain functional operations like filter, map, reduce.
    """
    def __init__(self, iterable):
        self._iterator = iter(iterable)

    @staticmethod
    def of(iterable):
        return Stream(iterable)

    def filter(self, predicate):
        self._iterator = filter(predicate, self._iterator)
        return self

    def map(self, mapper):
        self._iterator = map(mapper, self._iterator)
        return self

    def sorted(self, key=None, reverse=False):
        self._iterator = iter(sorted(self._iterator, key=key, reverse=reverse))
        return self

    def collect(self):
        # Consume the iterator and return a list
        return list(self._iterator)

    def reduce(self, accumulator, initial):
        return functools.reduce(accumulator, self._iterator, initial)

    def group_by(self, key_func):
        # itertools.groupby needs the data to be sorted by the key first
        sorted_items = sorted(self._iterator, key=key_func)
        result = {}
        for key, group in itertools.groupby(sorted_items, key=key_func):
            result[key] = list(group)
        return result