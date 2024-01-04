#!/usr/bin/env python3
"""Coroutine called async_comprehension that takes no arguments"""

from asyncio import sleep
from random import uniform
from typing import List


async def async_generator() -> Generator[float, None, None]:
    """Async Generator"""
    for _ in range(10):
        await sleep(1)
        yield uniform(0, 10)


async def async_comprehension() -> List[float]:
    """Async Comprehension"""
    return [i async for i in async_generator()]
