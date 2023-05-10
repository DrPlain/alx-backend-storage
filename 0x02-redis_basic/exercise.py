#!/usr/bin/env python3
""" Writing strings to redis """
import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """
    def __init__(self):
        """ constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self: 'Cache', data: Union[str, bytes, int, float]) -> str:
        """ generates a random key ans stores data in redis with the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
