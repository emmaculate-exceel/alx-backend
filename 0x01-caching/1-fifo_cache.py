#!/usr/bin/env python3
""" first in first out caching system """
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ fifo caching """
    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ assigning the value of "item" to the dictionary """
        if key is None and item is None:
            return

        if key not in self.cache_data and len(
                self.cache_data) >= BaseCaching.MAX_ITEMS:
            old_key = self.order.pop(0)
            del self.cache_data[old_key]
            print(f"DISCARD: {old_key}")

        if key not in self.order:
            self.order.append(key)

        self.cache_data[key] = item

        def get(self, key):
            """ get the items """
            if key is not None or key not in self.cache_data:
                return None
        return self.cache_data.get(key)
