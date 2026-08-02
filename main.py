import asyncio
import logging

from bot import run_telegram_bot

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


async def main():
    try:
        await run_telegram_bot()
    except KeyboardInterrupt:
        print("🛑 Bot Stopped")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())