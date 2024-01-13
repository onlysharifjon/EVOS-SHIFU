from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menyu_bir = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Setlar (8)')
        ],
        [
            KeyboardButton(text='Lavash (9)'),
            KeyboardButton(text='Shaurma (4)')
        ],
        [
            KeyboardButton(text='Burger (4)'),
            KeyboardButton(text='Hot-Dog (8)')
        ],
        [
            KeyboardButton("Ichimliklar (11)")
        ],
        [
            KeyboardButton('Shirinlik va disertlar (4)')
        ],
        [
            KeyboardButton('Garnirlar (10)')
        ],
        [
            KeyboardButton('🔙 Orqaga qaytish')
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
    ],
    resize_keyboard=True
)

lavashlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Mol goʼshtidan qalampir lavash'),
            KeyboardButton('Tovuq goʼshtli qalampir lavash')
        ],
        [
            KeyboardButton("Mol go'shtidan pishloqli lavash Standard"),
            KeyboardButton("Lavash cheese tovuq go'sht Standart")
        ],
        [
            KeyboardButton('FITTER'),
            KeyboardButton("Lavash tovuq go'sht")
        ],
        [
            KeyboardButton("Lavash mol go'sht")
        ],
        [
            KeyboardButton('🔙 Ortga qaytish')
        ],
    ],

    resize_keyboard=True,
)

shaurmalar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Shaurma qalampir mol go'sht"),
            KeyboardButton("Shaurma tovuq go'sht")
        ],
        [
            KeyboardButton("Shaurma qalampir tovuq go'sht"),
            KeyboardButton("Shaurma mol go'sht")
        ],
        [
            KeyboardButton('🔙 Ortga qaytish')
        ],
    ],

    resize_keyboard=True,
)

burgerlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Gamburger"),
            KeyboardButton("Double burger")
        ],
        [
            KeyboardButton("Cheese burger"),
            KeyboardButton("Double cheese")
        ],
        [
            KeyboardButton('🔙 Ortga qaytish')
        ],
    ],

    resize_keyboard=True,
)

hot_doglar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Hot-dog baguette"),
            KeyboardButton("Sub tovuq cheese")
        ],
        [
            KeyboardButton("Sub tovuq"),
            KeyboardButton("Hot-dog baguette double")
        ],
        [
            KeyboardButton("Hot-dog kids"),
            KeyboardButton("Sub go'sht cheese")
        ],
        [
            KeyboardButton("Hot-dog classic"),
            KeyboardButton("Sub go'sht")
        ],
        [
            KeyboardButton('🔙 Ortga qaytish')
        ],
    ],

    resize_keyboard=True,
)

ichimliklar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Sok dena 0,33l"),
            KeyboardButton("Suv 0,5")
        ],
        [
            KeyboardButton("Pepsi 0,5"),
            KeyboardButton("Pepsi 1,5")
        ],
        [
            KeyboardButton("Quyib beriladigan Pepsi"),
            KeyboardButton("Bliss sharbati")
        ],
        [
            KeyboardButton("Amerikano"),
            KeyboardButton("Latte")
        ],
        [
            KeyboardButton("Ko'k choy"),
            KeyboardButton("Qora choy")
        ],
        [
            KeyboardButton("Limonli ko'k choy")
        ],
        [
            KeyboardButton('🔙 Ortga qaytish')
        ],
    ],

    resize_keyboard=True,
)

shirinliklar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Medovik Asalim"),
            KeyboardButton("Chizkeyk")
        ],
        [
            KeyboardButton("Donut karameli"),
            KeyboardButton("Donut mevali")
        ],
        [
            KeyboardButton('🔙 Ortga qaytish')
        ],
    ],

    resize_keyboard=True,
)

garnirlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton("Ketchup"),
            KeyboardButton("Pishloqli sous")
        ],
        [
            KeyboardButton("Chisnokli sous"),
            KeyboardButton("Chili sous")
        ],
        [
            KeyboardButton("Barbekyu sousi"),
            KeyboardButton("Guruch")
        ],
        [
            KeyboardButton("Salat"),
            KeyboardButton("Non")
        ],
        [
            KeyboardButton("Tovuq Strips"),
            KeyboardButton("Fri")
        ],

        [
            KeyboardButton('🔙 Ortga qaytish')
        ],
    ],

    resize_keyboard=True,
)
