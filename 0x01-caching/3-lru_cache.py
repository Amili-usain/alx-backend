#!/usr/bin/env python3
"""Least Recently Used (LRU) caching module."""
from collections import OrderedDict

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Caching system that stores and retrieves items using LRU
       (Least Recently Used) policy."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)
        else:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key."""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
