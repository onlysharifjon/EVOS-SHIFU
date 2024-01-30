from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.userbuttons import start_button, telefon

from loader import dp
from handlers.users.editable_buttons import userlar

odamlar = []

import sqlite3

connect = sqlite3.connect('userlar_malumotlari.db')
cursor = connect.cursor()


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    cursor.execute("CREATE TABLE IF NOT EXISTS userlar(user_id INTEGER)")
    odamlar = cursor.execute("SELECT user_id from userlar").fetchall()
    fake_data = odamlar.copy()
    odamlar.clear()
    for i in fake_data:
        odamlar.append(i[0])
    print(odamlar)
    userlar[message.from_user.id] = 1
    if message.from_user.id not in odamlar:
        cursor.execute(f'INSERT INTO userlar VALUES({int(message.from_user.id)})')
        connect.commit()
        odamlar.append(message.from_user.id)
        await message.answer("<b>EVOS |</b> Доставка botiga xush kelibsiz!", reply_markup=telefon)
    else:
        await message.answer('<b>EVOS |</b> Доставка botiga xush kelibsiz!', reply_markup=start_button)
