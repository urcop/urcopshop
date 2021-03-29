from aiogram import types

from loader import dp


@dp.message_handler(text='Большие сливы')
async def get_bigSliv(message: types.Message):
    await message.answer('Вы выбрали категорию большие сливы')

