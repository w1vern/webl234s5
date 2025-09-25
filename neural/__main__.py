

import asyncio

from neural.rabbit import app


async def main() -> None:
    try:
        await app.run()
    finally:
        await app.stop()


if __name__ == "__main__":
    asyncio.run(main())
