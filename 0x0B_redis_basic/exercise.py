#!/usr/bin/env python3
""" Module to handle datastore with redis """

import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps

def count_calls(method: Callable) -> Callable:
    """Decorator to count method calls."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__  # Use method's qualified name as key
        self._redis.incr(key)  # Increment method call count
        return method(self, *args, **kwargs)
    return wrapper

class Cache:
    """ Cache class for redis datastore """
    def __init__(self):
        """ Constructor for initializing redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis using a unique key. """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Callable[[bytes], Union[str, bytes, int, float]] = None
            ) -> Union[str, bytes, int, float]:
        """ Get data from redis with optional type conversion. """
        data = self._redis.get(key)
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """ Get string data from redis. """
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """ Get int data from redis. """
        return self.get(key, fn=int)
