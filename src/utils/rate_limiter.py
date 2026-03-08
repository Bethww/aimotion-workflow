"""Async rate limiter for API calls."""
from __future__ import annotations
import asyncio
import time

class RateLimiter:
    def __init__(self, requests_per_minute: int = 30) -> None:
        self.rpm = requests_per_minute
        self.interval = 60.0 / requests_per_minute
        self._last_request: float = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        async with self._lock:
            now = time.monotonic()
            wait = self.interval - (now - self._last_request)
            if wait > 0:
                await asyncio.sleep(wait)
            self._last_request = time.monotonic()
