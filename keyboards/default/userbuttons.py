from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

start_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🍴 Menyu'),
        ],
        [
            KeyboardButton('📋 Mening buyurtmalarim'),
        ],
        [KeyboardButton('📥 Savat'),
         KeyboardButton('📞 Aloqa')
         ],
        [
            KeyboardButton('📨 Xabar yuborish'),
            KeyboardButton('⚙️ Sozlamalar')
        ],
        [
            KeyboardButton('Biz haqimizda ℹ️')
        ]
    ],
    resize_keyboard=True,
    # one_time_keyboard=True,
)

telefon = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Aloqa📞', request_contact=True)
        ]
    ],
    resize_keyboard=True
)

joylashuv = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Joylashuv📍', request_location=True)
        ]
    ],
    resize_keyboard=True
)

menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton('Setlar (8)')],
        [KeyboardButton('Lavash (9)'), KeyboardButton('Shaurma (4)')],
        [KeyboardButton('Burger (4)'), KeyboardButton('Hot-Dog (8)')],
        [KeyboardButton('Ichimliklar (11)')],
        [KeyboardButton('Shirinlik va disertlar (4)')],
        [KeyboardButton('Garnirlar (10)')],
    ],
    resize_keyboard=True,
)
