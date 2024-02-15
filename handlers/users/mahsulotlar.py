from loader import dp
from states.state_aiogram import Bolimlar
from aiogram import types
import sqlite3
from keyboards.inline.mahsulotlar_inline import mahsulot_inline
connect = sqlite3.connect('C:/Users/momin/PycharmProjects/EVOS-SHIFU/evos_.database.db')
cursor = connect.cursor()


@dp.message_handler(state=Bolimlar.setlar)
async def setlar_funksiyasi(message: types.Message):
    print(type(message.text))
    mahsulot_malumotlari = cursor.execute(f"SELECT * FROM mahsulotlar WHERE name=?", (message.text,)).fetchall()
    print(mahsulot_malumotlari)
    # test ma`lumot [('FitCombo', 25000, 'Fit_Combo.jpg', 'setlar')]
    txt = f'''
😋Mahsulot nomi: {mahsulot_malumotlari[0][0]}
💸Mahsulot narxi: {mahsulot_malumotlari[0][1]}
📃Mahsulot kategoriyasi: {mahsulot_malumotlari[0][3]}
    '''
    await message.answer_photo(open(f'images/product_image/{mahsulot_malumotlari[0][2]}', 'rb'), caption=txt,reply_markup=mahsulot_inline)
