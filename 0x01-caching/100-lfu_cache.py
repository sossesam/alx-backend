#!/usr/bin/python3
""" 0-main is working"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """ 0-main is working"""
    def __init__(self, *args, **kwargs):
        """ 0-main is working"""
        super().__init__()
        self.memlist = {}

    def put(self, key, item):
        """ 0-main is working"""
        if key is None or item is None:
            return

        if len(self.memlist) == BaseCaching.MAX_ITEMS:
            if key in self.memlist.keys():
                self.memlist[key] = self.memlist[key] + 1
                self.cache_data[key] = item

            else:
                lfu = min(self.memlist, key=self.memlist.get)
                del self.cache_data[lfu]
                del self.memlist[lfu]
                self.memlist[key] = 0
                self.cache_data[key] = item
                print(f"DISCARD: {lfu}")

        else:
            self.memlist[key] = 0
            self.cache_data[key] = item

    def get(self, key):
        """ 0-main is working"""
        if self.cache_data.get(key) is None or key is None:
            return None
        else:
            self.memlist[key] = self.memlist[key] + 1
            return self.cache_data[key]
