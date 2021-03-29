from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Небольшие сливы'),
            KeyboardButton(text='Большие сливы')
        ],
        [
            KeyboardButton(text='Слитые курсы'),
        ],
        [
            KeyboardButton(text='Вернуться')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
