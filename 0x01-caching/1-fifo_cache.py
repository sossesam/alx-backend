#!/usr/bin/python3
""" 0-main is working"""

BaseCaching = __import__('base_caching').BaseCaching

class FIFOCache(BaseCaching):
    """ 0-main is working"""
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.memlist = []

    def put(self, key, item):

        if key is None or item is None:
            return
        
            
        if len(self.memlist) >= BaseCaching.MAX_ITEMS:
            removed_key = self.memlist.pop(0)
            del self.cache_data[removed_key]
            self.memlist.append(key)
            self.cache_data[key] = item

            print(f"DISCARD: {removed_key}")
            
        else:
            self.memlist.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ 0-main is working"""
        if self.cache_data.get(key) is None or key is None:
            return None
        else:
            return self.cache_data[key]