#!/usr/bin/env python3
"""
Asynchronous coroutine 'wait_random' takes in an integer argument 'max_delay'
and returns a random float delay between 0 and max_delay
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns delay between 0 and max_delay"""
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
