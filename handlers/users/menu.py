from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message

from keyboards.default import menu, home
from keyboards.inline.callback_datas import cancel_callback
from keyboards.inline.small_sliv import small
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Выберите категорю товара', reply_markup=menu)


@dp.callback_query_handler(cancel_callback.filter(cancel='mCancel'))
async def get_cancel(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer(text='Небольшие сливы', reply_markup=small)


@dp.callback_query_handler(cancel_callback.filter(cancel='cancel'))
async def get_back(call: CallbackQuery):
    await call.message.delete()
    await call.message.answer('Возврат в меню', reply_markup=menu)


@dp.message_handler(text='Вернуться')
async def get_remove(message: types.Message):
    await message.answer(text='Главная', reply_markup=home)


@dp.message_handler(text='Меню')
async def get_menu(message: Message):
    await show_menu(message)
