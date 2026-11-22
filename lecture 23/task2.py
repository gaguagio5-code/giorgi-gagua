import asyncio

import aiohttp

URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_posts(session: aiohttp.ClientSession) -> list[dict]:
    async with session.get(URL) as response:
        response.raise_for_status()
        return await response.json()

async def main() -> None:
    async with aiohttp.ClientSession() as session:
        posts = await fetch_posts(session)

    first_20 = posts[:20]
    selected = [post for post in first_20 if post["userId"] == 1]

    print(f"Titles of posts by user 1 (from the first 20 posts): {len(selected)} found\n")
    for number, post in enumerate(selected, start=1):
        print(f"{number}. {post['title']}")

if __name__ == "__main__":
    asyncio.run(main())