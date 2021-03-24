from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import buy_callback

maloletki = InlineKeyboardMarkup(row_width=1,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text='Катя 300р',
                                             callback_data=buy_callback.new(item_name='mKate')
                                         )
                                     ],
                                     [
                                         InlineKeyboardButton(
                                             text='Ксюша 300р',
                                             callback_data=buy_callback.new(item_name='mKsenia')
                                         )
                                     ],
                                     [
                                         InlineKeyboardButton(
                                             text='Рома 150р \n по скидке',
                                             callback_data=buy_callback.new(item_name='mRoma')
                                         )
                                     ],
                                     [
                                         InlineKeyboardButton(
                                             text='Отмена',
                                             callback_data=buy_callback.new(item_name='mCancel')
                                         )
                                     ]
                                 ])

kate_keyboard = InlineKeyboardMarkup()
KATE_LINK = 'https://vk.com/pp__kk__pp'
kate_link = InlineKeyboardButton(text='Катя', url=KATE_LINK)
kate_keyboard.insert(kate_link)

roma_keyboard = InlineKeyboardMarkup()
ROMA_LINK = 'https://vk.com/explodingpies'
roma_link = InlineKeyboardButton(text='Купить тут', url=ROMA_LINK)
roma_keyboard.insert(roma_link)
