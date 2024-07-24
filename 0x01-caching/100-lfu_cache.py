#!/usr/bin/env python3
""" Using a least frequent usage caching system """


class LFUCache(BaseCaching):
    """ least frequent class """
    def __init__(self):
        super().__init__()
        self.frequency = {}
        self.lfu_count = {}

    def _update_frequency(self, key):
        """ update the refrequency """
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

    def _remove_least_frequent(self):
        """ delete least frequent """
        if self.cache_data:
            min_freq = min(self.frequency.values())
            items_with_min_freq = [key for key,  freq in self.frequency.items() if freq == min_freq]
            if len(items_with_min_freq) > 1:
                lru_key = min(items_with_min_freq, key=lambda k: self.lfu_count.get(k, 0))
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print(f"DISCARD: {lru_key}")
            else:
                lfu_key = items_with_min_freq[0]
                del self.cache_data[lfu_key]
                del self.frequency[lfu_key]
                print(f"DISCARD: {lfu_key"})

    def put(sel, key, item):
        """ put value and keys """
        if key is None or item is None:
            return

        if len(self, cache_data) >= self.MAX_ITEMS:
            self._remove_least_frequent()

        self.cache_data[key] = item
        self._update_frequency(key)
        self._lfu_count[key] = len(self.cache_data)


    def get(self, key):
        """ get keys """
        if key is None or key not in self.cache_data:
            return None


        self._update_frequency(key)
        return self.cache_data[key]
