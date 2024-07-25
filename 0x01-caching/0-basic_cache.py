#!/usr/bin/env python3
""" a class for the caching system """


BaseCaching = __import__('base_caching').BaseCaching
# from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basic cache """

    def __init__(self):
        self.cache_data = {}

    def put(self, key, item):
        """ put method """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ get method """
        if key is None or key is in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
