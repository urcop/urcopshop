from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Малолетние'),
            KeyboardButton(text='Большие сливы')
        ],
        [
            KeyboardButton(text='SMM'),
            KeyboardButton(text='Програмирование')
        ],
        [
            KeyboardButton(text='Буряточка')
        ],
        [
            KeyboardButton(text='Вернуться')
        ]
    ],
    resize_keyboard=True
)
