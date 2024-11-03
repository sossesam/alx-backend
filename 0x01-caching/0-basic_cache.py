#!/usr/bin/python3
""" 0-main """
BasicCaching = __import__('base_caching').BaseCaching

class BasicCache(BasicCaching):
    """ 0-main """
    def __init__(self):
        """ 0-main """
        super().__init__()

    def put(self, key, item):
        """ 0-main """
        if key == None or item == None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """ 0-main """
        if self.cache_data.get(key) == None or key == None:
            return None
        else:
            return self.cache_data[key]
