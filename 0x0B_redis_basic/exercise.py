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
        key = method.__qualname__
        self._redis.incr(key)  # Increment method call count
        return method(self, *args, **kwargs)
    return wrapper

def call_history(method: Callable) -> Callable:
    """Decorator to store history of inputs and outputs."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"
        self._redis.rpush(inputs_key, str(args))  # Store inputs in list
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))  # Store outputs in list
        return result
    return wrapper

class Cache:
    """ Cache class for redis datastore """
    def __init__(self):
        """ Constructor for initializing redis """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

def replay(method: Callable):
    """Function to show the history of calls of a function."""
    instance = Cache()  # Assumes Cache instance is required
    method_name = method.__qualname__
    count_key = method_name
    inputs_key = f"{method_name}:inputs"
    outputs_key = f"{method_name}:outputs"

    call_count = instance._redis.get(count_key) or 0
    inputs = instance._redis.lrange(inputs_key, 0, -1)
    outputs = instance._redis.lrange(outputs_key, 0, -1)

    print(f"{method.__name__} was called {call_count.decode()} times:")
    for inp, out in zip(inputs, outputs):
        print(f"{method.__name__}{inp.decode()} -> {out.decode()}")

# Example usage
if __name__ == "__main__":
    cache = Cache()
    cache.store("foo")
    cache.store("bar")
    cache.store(42)
    replay(cache.store)
