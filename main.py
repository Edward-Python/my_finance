import asyncio
import logging
import time

from aiogram import Bot, Dispatcher

from config.config import settings


async def main():
    bot = Bot(token=settings.token.get_secret_value())
    dp = Dispatcher()
    # dp.include_router()
    await dp.start_polling(bot)


def times():
    time_local = time.localtime(time.time())
    format_time = time.strftime("%m-%d | %H:%M", time_local)
    return format_time


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        print(f"Бот запущен в {times()}")
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"Бот выключен в {times()}")