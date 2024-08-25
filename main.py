import asyncio
import logging
from aiogram.filters import CommandStart
from aiogram.types import Message
from confir import TOKEN

from aiogram import Bot, Dispatcher, types
from asyncio import sleep
from handlers import router

import keyboard as kb

bot = Bot(TOKEN)
dp = Dispatcher()
dp.include_router(router)
#markup = kb.main_markup

       

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(dp.start_polling(bot))
    except (KeyboardInterrupt, SystemExit):
        print('Bye!')