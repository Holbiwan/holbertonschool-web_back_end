#!/usr/bin/env python3
"""Measure the runtime for four parallel comprehensions"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function to count"""
    start = time.perf_counter()

    async def run_comprehension():
        """Async function to run async_comprehension"""
        await async_comprehension()

    async def measure_runtime() -> float:
        """Function to count"""
        start = time.perf_counter()

        await asyncio.gather(
            run_comprehension(),
            run_comprehension(),
            run_comprehension(),
            run_comprehension(),
        )

        end = time.perf_counter()
        return end - start
