import asyncio
import time

import aiohttp
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/todos"
IDS = range(1, 11)


def fetch_sync() -> float:
    start = time.perf_counter()
    for i in IDS:
        response = requests.get(f"{BASE_URL}/{i}")
        response.raise_for_status()
        data = response.json()
    elapsed = time.perf_counter() - start
    print(f"Synchronous version: {elapsed:.2f} seconds")
    return elapsed


async def fetch_one(session: aiohttp.ClientSession, todo_id: int) -> dict:
    async with session.get(f"{BASE_URL}/{todo_id}") as response:
        response.raise_for_status()
        return await response.json()


async def fetch_async() -> float:
    start = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_one(session, i) for i in IDS]
        results = await asyncio.gather(*tasks)
    elapsed = time.perf_counter() - start
    print(f"Asynchronous version: {elapsed:.2f} seconds")
    return elapsed


def main() -> None:
    sync_time = fetch_sync()
    async_time = asyncio.run(fetch_async())
    diff = sync_time - async_time
    print(f"The asynchronous version {diff:.2f} It worked a split second faster!")


if __name__ == "__main__":
    main()