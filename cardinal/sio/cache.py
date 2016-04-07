# -*- coding: utf-8 -*-

"""
This module provides a simple timer based cache.
"""


import time


class Cache(object):
    """
    A simple timer based cache.

    Provides a way to determine whether or not a value has expired.

    Keyword arguments:
    value -- the cached value (default None)
    ttl   -- the number of seconds the value is valid (default 900)
    """

    def __init__(self, value=None, ttl=900):
        self.__last_updated = time.time()
        self.__value = value
        self.ttl = ttl

    @property
    def expired(self):
        """
        Return whether or not the value is unset or has expired.
        """
        age = time.time() - self.__last_updated
        return not self.__value or age > self.ttl

    @property
    def value(self):
        """
        Return the cached value.
        """
        return self.__value

    @value.setter
    def value(self, value):
        """
        Set the cached value and update its timestamp.
        """
        self.__value = value
        self.__last_updated = time.time()
