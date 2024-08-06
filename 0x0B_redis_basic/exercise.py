#!/usr/bin/env python3
""" Module to handle datastore with redis """

import redis
import uuid
from typing import Union, Callable, Optional

class Cache:
    """ Cache class for redis datastore """
    def __init__(self):
        """ Constructor for initializing redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float]:
        """ Get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Get string data from redis """
        return self.get(key, fn=lambda d: d.decode("utf-8"))
    
    def get_int(self, key: str) -> int:
        """ Get int data from redis """
        return self.get(key, fn=int)
    
