from loader import dp
from aiogram import types
import sqlite3

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

savat_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton("✅", callback_data='rozi-boldim'),
            InlineKeyboardButton("❌", callback_data="qarshiman"),

        ]
    ]
)

connect_ = sqlite3.connect('C:/Users/Sharifjon/PycharmProjects/EVOS-SHIFU/evos_.database.db')
cursor_ = connect_.cursor()


@dp.message_handler(text='📥 Savat', state="*")
async def svatcha(message: types.Message):
    filtrcha = cursor_.execute("SELECT * FROM korzinka WHERE user_id=? AND status=?",
                               (message.from_user.id, 1)).fetchall()
    txt = ""
    count = 0
    umumiy_narx = 0
    for i in filtrcha:
        narx_filtr = cursor_.execute('SELECT price FROM mahsulotlar WHERE name=?', (i[1],)).fetchone()
        print(narx_filtr)
        umumiy_narx += narx_filtr[0]
        count += 1
        txt += f"{count}) 😋<b>{i[1]}</b>\n"
    txt += f"\n\n🤑Umumiy narx: <code>{umumiy_narx}</code>"
    await message.answer(txt,reply_markup=savat_inline)
