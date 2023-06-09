import asyncio
import logging
import sys

from bot.handlers import admin_handlers
from bot.handlers import common_handlers
from bot.dependencies import dp, bot
from bot.utils.misc import check_eventloop_policy

check_eventloop_policy()


async def main():
    dp.include_router(admin_handlers.admin_router)
    dp.include_router(common_handlers.form_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
