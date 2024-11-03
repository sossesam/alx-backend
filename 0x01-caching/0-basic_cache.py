#!/usr/bin/python3
""" 0-main is working"""

BasicCaching = __import__('base_caching').BaseCaching

class BasicCache(BasicCaching):
    """ 0-main is working"""
    def __init__(self):
        """ 0-main is working"""
        super().__init__()

    def put(self, key, item):
        """ 0-main is working"""
        if key == None or item == None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ 0-main is working"""
        if self.cache_data.get(key) == None or key == None:
            return None
        else:
            return self.cache_data[key]
