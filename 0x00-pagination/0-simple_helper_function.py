#!/usr/bin/env python3
"""Task 0 module
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    """
    return ((page-1) * page_size, page_size * page)
