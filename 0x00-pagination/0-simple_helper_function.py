#!/usr/bin/env python3
""" indexing page and the page size """


def index_range(page, page_size):
    """ indexing page """
    start = (page - 1) * page_size
    end = page + page_size
    return (start, end)
