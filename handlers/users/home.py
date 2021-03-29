from aiogram.types import Message

from handlers.users import bot_help
from loader import dp

@dp.message_handler(text='Помощь')
async def get_help(message: Message):
    await bot_help(message)
