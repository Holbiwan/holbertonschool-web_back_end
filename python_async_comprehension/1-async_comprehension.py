#!/usr/bin/env python3
"""Coroutine called async_comprehension that takes no arguments"""

from typing import List
from random import uniform
from asyncio import gather
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehension"""
    return [i async for i in async_generator()]
