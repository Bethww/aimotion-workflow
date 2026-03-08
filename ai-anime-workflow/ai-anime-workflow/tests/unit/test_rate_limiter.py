import asyncio, time, pytest
from src.utils.rate_limiter import RateLimiter

@pytest.mark.asyncio
async def test_rate_limiter_throttles():
    limiter = RateLimiter(requests_per_minute=600)
    start = time.monotonic()
    for _ in range(3):
        await limiter.acquire()
    elapsed = time.monotonic() - start
    assert elapsed >= 0.18
