#!/usr/bin/env python3
"""Returns the start and end indices for a specific page and page size"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns the start and end indices for a page

    Args:
        page: The specific page required
        page_size: The number of elements in a page

    Returns:
        A tuple of size two containing the start index and the end index
    """
    start = (page - 1) * page_size
    return (start, start + page_size)
