from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.inline.callback_datas import buy_callback, cancel_callback, description_callback

small = InlineKeyboardMarkup(row_width=1,
                             inline_keyboard=[
                                 [
                                     InlineKeyboardButton(
                                         text='Пакет минимальный',
                                         callback_data=buy_callback.new(item_name='mP1')
                                     )
                                 ],
                                 [
                                     InlineKeyboardButton(
                                         text='Пакет стандарт',
                                         callback_data='buy:mP2'
                                     )
                                 ],
                                 [
                                     InlineKeyboardButton(
                                         text='Пакет полный',
                                         callback_data='buy:mP3'
                                     )
                                 ],
                                 [
                                     InlineKeyboardButton(
                                         text='Отмена',
                                         callback_data=cancel_callback.new(cancel='cancel')
                                     )
                                 ]
                             ])

minimum_keyboard = InlineKeyboardMarkup(row_width=1,
                                        inline_keyboard=[
                                            [
                                                InlineKeyboardButton(
                                                    text='Оплата',
                                                    callback_data='buy:transfer'
                                                )
                                            ],
                                            [
                                                InlineKeyboardButton(
                                                    text='Отмена',
                                                    callback_data='cancel:mCancel'
                                                )
                                            ]
                                        ])
