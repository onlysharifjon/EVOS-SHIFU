from loader import dp
from states.state_aiogram import Bolimlar
from aiogram import types
import sqlite3

connect = sqlite3.connect('evos_database.db')
cursor = connect.cursor()


@dp.message_handler(state=Bolimlar.setlar)
async def setlar_funksiyasi(message: types.Message):
    cursor.execute("CREATE TABLE IF NOT EXISTS mahsulotlar(name TEXT,price INTEGR,image TEXT,category TEXT)")
    print(message.text)
