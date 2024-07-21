#!/usr/bin/env python3
""" indexing page and the page size """
import unittest
import csv
import math
from typing import Tuple, List


class Server:
    """
    Server class to paginate a database of popular names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for rows in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ ensuring the dataset returns an integer """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        if page is >= len(dataset):
            return []

        return self.dataset()


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ indexing page """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
