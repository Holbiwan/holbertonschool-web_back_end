#!/usr/bin/env python3
"""Module to handle data storage and retrieval using Redis."""

import redis
from typing import Union, Optional, Callable
from uuid import uuid4
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a function is called.
    Increments a Redis counter each time the decorated function is called.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment count in Redis and call the original method."""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store history of method calls in Redis.
    Stores inputs and outputs of each call using Redis lists.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store inputs and outputs to Redis and return method output."""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))

        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))

        return result

    return wrapper


def replay(fn: Callable):
    """Displays historical calls of a function including inputs and outputs.
    Fetches the call history from Redis and prints each call detail.
    """
    r = redis.Redis()
    f_name = fn.__qualname__
    n_calls = r.get(f_name)
    try:
        n_calls = n_calls.decode('utf-8')
    except Exception:
        n_calls = 0

    print(f'{f_name} was called {n_calls} times:')
    ins = r.lrange(f_name + ":inputs", 0, -1)
    outs = r.lrange(f_name + ":outputs", 0, -1)

    for i, o in zip(ins, outs):
        try:
            i = i.decode('utf-8')
        except Exception:
            i = ""
        try:
            o = o.decode('utf-8')
        except Exception:
            o = ""
        print(f'{f_name}(*{i}) -> {o}')


class Cache:
    """Implements caching functionality using Redis."""

    def __init__(self):
        """Initializes Redis connection and flushes the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store input data in Redis using a random key and return the key."""
        random_key = str(uuid4())
        self._redis.set(random_key, data)
        return random_key

    def get(self, key: str,
            fn: Optional[Callable[[bytes], Union[str, bytes, int, float]]]
            = None) -> Union[str, bytes, int, float]:
        """Retrieves data from Redis & applies a conversion function."""
        value = self._redis.get(key)
        return fn(value) if fn and value else value

    def get_str(self, key: str) -> str:
        """Retrieves a string value from Redis."""
        value = self._redis.get(key)
        return value.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Retrieves an integer value from Redis."""
        value = self._redis.get(key)
        try:
            return int(value.decode("utf-8"))
        except Exception:
            return 0
