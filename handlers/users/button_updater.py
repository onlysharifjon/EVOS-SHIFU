from loader import dp
from aiogram import types

import sqlite3

connect = sqlite3.connect('C:/Users/momin/PycharmProjects/EVOS-SHIFU/evos_.database.db')
cursor = connect.cursor()


@dp.callback_query_handler(text="minus", state="*")
async def minus_update(call: types.CallbackQuery):
    print("Ishladi")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS korzinka(id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, mahsulot TEXT, soni INTEGER, status BOOLEAN)")
    connect.commit()

    # await call.message.edit_reply_markup()


@dp.callback_query_handler(text="pilus")
async def pilus_update(call: types.CallbackQuery):
    pass
