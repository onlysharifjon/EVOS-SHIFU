from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mahsulot_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-', callback_data="minus"),
            InlineKeyboardButton(text='0', callback_data='0'),
            InlineKeyboardButton(text='+', callback_data="pilus")
        ],
        [
            InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save")
        ]
    ]
)
