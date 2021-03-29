from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.small_sliv import small, minimum_keyboard
from loader import dp


@dp.message_handler(text='Небольшие сливы')
async def get_smallSliv(message: types.Message):
    await message.answer('Небольшие сливы', reply_markup=small)


@dp.callback_query_handler(buy_callback.filter(item_name='mP1'))
async def get_pack1(call: CallbackQuery):
    await call.message.answer(text='Пакет минимальный', reply_markup=minimum_keyboard)
    await call.message.delete()


@dp.callback_query_handler(buy_callback.filter(item_name='mP2'))
async def get_pack2(call: CallbackQuery):
    await call.message.answer(text='Пакет стандартный', reply_markup=minimum_keyboard)
    await call.message.delete()


@dp.callback_query_handler(buy_callback.filter(item_name='mP3'))
async def get_pack3(call: CallbackQuery):
    await call.message.answer(text='Пакет полный', reply_markup=minimum_keyboard)
    await call.message.delete()
