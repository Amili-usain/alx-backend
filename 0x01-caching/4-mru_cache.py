#!/usr/bin/env python3
"""Most Recently Used (MRU) caching module."""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Caching system that stores and retrieves items using MRU
       (Most Recently Used) policy."""

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
                most_recent_key = next(reversed(self.cache_data))
                del self.cache_data[most_recent_key]
                print("DISCARD:", most_recent_key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key."""
        if key in self.cache_data:
            value = self.cache_data[key]
            del self.cache_data[key]
            self.cache_data[key] = value
            return value
        return None
