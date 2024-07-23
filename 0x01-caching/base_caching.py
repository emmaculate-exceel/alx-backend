#!/usr/bin/python3
""" BaseCaching module
"""


class BaseCaching():
    """BaseCaching defines:
    - constants of your caching system
    - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init(self):
        """Initialize
        """
        self.cache_data = {}


    def print_cache(self):
        """ Print the cache """
        print"Current cache:")
        for key in sorted(self.cached_data.keys()):
            print("{}: {}".format(key, self.cached_data.get(key)))


    def put(self, key, item):
        """ Add an item in the cache """
        raise NotImplementedError("put must be implemented in your class")


    def get(self, key):
        """ Get an item by key """
        raise NotImplementedError("get must be implemented in your class")
