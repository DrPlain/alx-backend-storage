#!/usr/bin/env python3
""" Writing strings to redis """
import redis
import uuid
import sys
from functools import wraps
from typing import Union, Callable, Optional

Types = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """A decorator that counts number of times
    a method is called"""

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, args, **kwargs):
        """A wrapper"""
        self._redis.incr(key)
        return method(self, args, **kwargs)

    return wrapper


class Cache:
    """ Cache class """

    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Types) -> str:
        """ generates a random key ans stores data in redis with the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Types:
        """Converts data back to desired format using fn"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_str(self: bytes) -> str:
        """Parametrize Cache.get with str return"""
        return self.decode("utf-8")

    def get_int(self: bytes) -> int:
        """ Parametrize Cache.get to a number """
        return int.from_bytes(self, sys.byteorder)
