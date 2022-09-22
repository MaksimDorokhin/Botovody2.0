from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


commands_default_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='/start'),
            KeyboardButton(text='/item')
        ],
        [
            KeyboardButton(text='/help')
        ],
        [
            KeyboardButton(text='Поделиться контактом',
                           request_contact=True),
            KeyboardButton(text='Передать геолокацию',
                           request_location=True),
        ]
    ],
    resize_keyboard=True
)

commands_info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О нас'),
            KeyboardButton(text='Контакты')
        ],
        [
            KeyboardButton(text='График работы')
        ],
        [
            KeyboardButton(text='О боте'),
            KeyboardButton(text='Меню'),
        ]
    ],
    resize_keyboard=True
)