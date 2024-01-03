#!/usr/bin/env python3
"""
Async 'wait_n': int 'n', int 'max_delay' -> List[float]
Spawns wait_random n times, returns delays in ascending order
"""

from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns list of delays in ascending order."""
    delays = [await wait_random(max_delay) for _ in range(n)]
    return sorted(delays)
