from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp

@dp.message_handler(Command('link'))
async def get_link(message: types.Message):
    link = 't.me/urcopshop_bot?start='+f'{message.from_user.id}'
    await message.answer('Ваша реферальная ссылка: \n'
                         f'{link}')