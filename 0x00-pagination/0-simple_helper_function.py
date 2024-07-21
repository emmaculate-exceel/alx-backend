#!/usr/bin/env python3
""" indexing page and the page size """
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indexing page """
    start = (page - 1) * page_size
    end = page * page_size 
    return (start, end)
