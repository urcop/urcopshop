import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart(deep_link=re.compile(r'^[0-9]{3,15}$')))
async def bot_start_deeplink(message: types.Message):
    deep_link_args = message.get_args()
    await message.answer(f'Привет, {message.from_user.full_name}! \n'
                         f'Ваш рефер - id{deep_link_args}')


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!")
