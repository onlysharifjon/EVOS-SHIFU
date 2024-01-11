from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

combo_plus_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-', callback_data='combo_minus'),
            InlineKeyboardButton(text='1', callback_data='0'),
            InlineKeyboardButton(text='+', callback_data='combo+pilus')
        ],
        [
            InlineKeyboardButton(text='📥Savatga qo`shish', callback_data='save_combo_plus')
        ]
    ]
)
