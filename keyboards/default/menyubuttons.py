from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menyu_bir = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Setlar(8)')
        ],
        [
            KeyboardButton(text='Lavash(9)'),
            KeyboardButton(text='Shaurma(4)')
        ],
        [
            KeyboardButton(text='Burger(4)'),
            KeyboardButton(text='Hot-Dog(8)')
        ],
        [
            KeyboardButton("Ichimliklar(11)")
        ],
        [
            KeyboardButton('Shirinlik va disertlar(4)')
        ],
        [
            KeyboardButton('Garnirlar(10)')
        ],
        [
            KeyboardButton('Orqaga🔙')
        ]
    ],
    resize_keyboard=True
)
setlar_menyu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Combo Plus Isituvchan (Qora choy)"),
            KeyboardButton("FitCombo")
        ],
        [
            KeyboardButton("Iftar kofte grill mol go'shtidan"),
            KeyboardButton("Donar boks  mol go'shtidan")
        ],
        [
            KeyboardButton("Donar boks tovuq go'shtidan"),
            KeyboardButton("COMBO+")
        ],
        [
            KeyboardButton("Iftar strips tovuq go'shtidan"),
            KeyboardButton("Kids COMBO")
        ],
        [
            KeyboardButton("🔙 Ortga qaytish"),
        ],
    ]
)
