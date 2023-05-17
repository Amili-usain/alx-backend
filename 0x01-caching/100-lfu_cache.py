#!/usr/bin/env python3
"""Least Frequently Used (LFU) caching module."""
from collections import defaultdict, OrderedDict

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Caching system that stores and retrieves items using LFU
       (Least Frequently Used) policy."""

    def __init__(self):
        """Initialize the cache."""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = defaultdict(int)

    def put(self, key, item):
        """Add an item to the cache."""
        if key is None or item is None:
            return
        if key not in self.cache_data and \
                len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            self._evict_least_frequent()
        self.cache_data[key] = item
        self.frequency[key] += 1

    def get(self, key):
        """Retrieve an item by key."""
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None

    def _evict_least_frequent(self):
        """Evict the least frequently used item from the cache."""
        min_freq = min(self.frequency.values())
        candidates = [k for k, v in self.frequency.items() if v == min_freq]
        least_recent_key = next(iter(candidates))
        del self.cache_data[least_recent_key]
        del self.frequency[least_recent_key]
        print("DISCARD:", least_recent_key)
