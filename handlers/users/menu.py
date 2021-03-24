import logging

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, CallbackQuery

from keyboards.default import menu
from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.maloletki_buttons import maloletki, kate_keyboard, roma_keyboard
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Выберите категорю товара', reply_markup=menu)


@dp.message_handler(text='малолетние'.capitalize())
async def get_maloletki(message: types.Message):
    await message.answer('Вы выбрали категорию малолетки', reply_markup=maloletki)


@dp.callback_query_handler(buy_callback.filter(item_name='mKate'))
async def buying_kate(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=30)
    logging.info(f'callback_data = {call.data}')
    logging.info(f'callback_data dict = {callback_data}')
    await call.message.answer('Вы выбрали Катю', reply_markup=kate_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='mRoma'))
async def buying_roma(call: CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.answer('Вы выбрали Рому', reply_markup=roma_keyboard)


@dp.callback_query_handler(buy_callback.filter(item_name='mCancel'))
async def cancel(call: CallbackQuery):
    await call.answer('Вы отменили действие ', show_alert=True)
    await call.message.edit_reply_markup()


@dp.message_handler(text='большие сливы'.capitalize())
async def get_big_sliv(message: types.Message):
    await message.answer('Вы выбрали категорию большие сливы')
    await message.answer_photo(
        'https://sun9-39.userapi.com/impg/P2xu9611ddPsDx4gK5C8d8UhP2dR_qmpiu__VQ/TGYfa1nlpS8.jpg?size=850x482&quality=96&sign=37cabfe8a2264b2020060b4ddab3b1fc&type=album')


@dp.message_handler(text='SMM')
async def get_smm(message: types.Message):
    await message.answer('Вы выбрали категорию smm')


@dp.message_handler(text='Програмирование'.capitalize())
async def get_programming(message: types.Message):
    await message.answer('Вы выбрали категорию програмирование')


@dp.message_handler(text='Буряточка')
async def get_roma(message: types.Message):
    await message.answer('Цена договорная \n'
                         'по вопросам сюда -> \n'
                         r'https://vk.com/explodingpies')


@dp.message_handler(text='Вернуться')
async def get_remove(message: types.Message):
    await message.answer(text='ок', reply_markup=ReplyKeyboardRemove())
