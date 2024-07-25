#!/usr/bin/env python3
""" a class for the caching system """


BaseCaching = __import__('base_caching').BaseCaching
# from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache """
    
    def __init__(self):
        super().__init__()
        self.cache_data[key] = item

    def put(self, key, item):
        """ put method """
        if key is not None or item is not None:
            value = self.cache_data.get(key)
            return value

    def get(self, key):
        """ get method """
        if key is None or key is not in self.cache_data.get(item):
            return None
