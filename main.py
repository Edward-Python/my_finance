import asyncio
import logging
import time

from aiogram import Bot, Dispatcher

from config.config import settings
from handlers.handler import router
from fsm_mashine.name_category import category_router


async def main():
    bot = Bot(token=settings.token.get_secret_value())
    dp = Dispatcher()
    dp.include_routers(router, category_router)
    # dp.include_router(router=category_router)
    await bot.delete_webhook(drop_pending_updates=True)
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