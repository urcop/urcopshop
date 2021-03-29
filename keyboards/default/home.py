from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

home = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О нас'),
            KeyboardButton(text='Помощь')
        ],
        [
            KeyboardButton(text='Меню'),
        ],
        [
            KeyboardButton(text='Личный кабиент')
        ]
    ],
    resize_keyboard=True
)
