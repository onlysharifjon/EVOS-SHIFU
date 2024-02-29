from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from keyboards.default.userbuttons import start_button
from loader import dp
from states.state_aiogram import Bolimlar
from aiogram import types
import sqlite3
from keyboards.inline.mahsulotlar_inline import mahsulot_inline

from keyboards.default.menyubuttons import menyu_bir


@dp.message_handler(text="🔙 Ortga qaytish", state="*")
async def mahsulotlar(message: types.Message):
    await message.answer('Orqaga qaytildi', reply_markup=menyu_bir)


@dp.message_handler(text="🔙 Orqaga qaytish", state="*")
async def mahsulotlar(message: types.Message):
    await message.answer('Orqaga qaytildi', reply_markup=start_button)


@dp.message_handler(state=Bolimlar.setlar)
async def setlar_funksiyasi(message: types.Message):
    connect = sqlite3.connect('evos_.database.db')
    cursor = connect.cursor()
    mahsulot_nomi = message.text
    mahsulot_malumotlari = cursor.execute(f"SELECT * FROM mahsulotlar WHERE name=?", (message.text,)).fetchall()
    txt = f'''
😋Mahsulot nomi: {mahsulot_malumotlari[0][0]}
💸Mahsulot narxi: {mahsulot_malumotlari[0][1]}
📃Mahsulot kategoriyasi: {mahsulot_malumotlari[0][3]}
    '''
    await message.answer_photo(open(f'images/product_image/{mahsulot_malumotlari[0][2]}', 'rb'), caption=txt,
                               reply_markup=mahsulot_inline)

    @dp.callback_query_handler(text="pilus", state="*")
    async def minus_update(call: types.CallbackQuery):
        connect_ = sqlite3.connect('evos_.database.db')
        cursor_ = connect_.cursor()
        filter_korzinka = cursor_.execute('SELECT * FROM korzinka where mahsulot=? AND status=? AND user_id=?',
                                          (mahsulot_nomi, 0, call.message.chat.id)).fetchone()

        if filter_korzinka is None:
            cursor_.execute('INSERT INTO korzinka (user_id, mahsulot, soni, status) VALUES (?,?,?,?)',
                            (call.message.chat.id, mahsulot_nomi, 1, 0))
            connect_.commit()
            ozgargan_inline = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text='-', callback_data="minus"),
                        InlineKeyboardButton(text=f'1', callback_data='0'),
                        InlineKeyboardButton(text='+', callback_data="pilus")
                    ],
                    [
                        InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save")
                    ]
                ]
            )
            await call.message.edit_reply_markup(reply_markup=ozgargan_inline)














        elif filter_korzinka[0]:
            print(filter_korzinka)
            updater = filter_korzinka[3] + 1

            cursor_.execute("UPDATE korzinka SET soni=? WHERE user_id=? AND mahsulot=? AND status= ?",
                            (updater, call.message.chat.id, mahsulot_nomi, 0))
            connect_.commit()

            ozgargan_inline = InlineKeyboardMarkup(
                inline_keyboard=[
                    [
                        InlineKeyboardButton(text='-', callback_data="minus"),
                        InlineKeyboardButton(text=f'{updater}', callback_data='0'),
                        InlineKeyboardButton(text='+', callback_data="pilus")
                    ],
                    [
                        InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save")
                    ]
                ]
            )
            await call.message.edit_reply_markup(reply_markup=ozgargan_inline)

    @dp.callback_query_handler(text='minus', state="*")
    async def minus(call: CallbackQuery):
        connect_ = sqlite3.connect('evos_.database.db')
        cursor_ = connect_.cursor()
        filter_korzinka = cursor_.execute('SELECT * FROM korzinka where mahsulot=? AND status=? AND user_id=?',
                                          (mahsulot_nomi, 0, call.message.chat.id)).fetchone()

        if filter_korzinka is None:
            print(True)
            cursor_.execute("DELETE FROM korzinka WHERE soni=0")
            connect_.commit()
            await call.answer('Buyurtma Berilmagan Mahsulot ?')
        elif filter_korzinka[0]:
            print(filter_korzinka)

            updater = filter_korzinka[-2] - 1
            if updater >= 0:

                cursor_.execute("UPDATE korzinka SET soni=? WHERE user_id=? AND mahsulot=? AND status= ?",
                                (updater, call.message.chat.id, mahsulot_nomi, 0))
                connect_.commit()
                cursor_.execute("DELETE FROM korzinka WHERE soni=0")
                connect_.commit()
                ozgargan_inline = InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            InlineKeyboardButton(text='-', callback_data="minus"),
                            InlineKeyboardButton(text=f'{updater}', callback_data='0'),
                            InlineKeyboardButton(text='+', callback_data="pilus")
                        ],
                        [
                            InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save")
                        ]
                    ]
                )

                await call.message.edit_reply_markup(reply_markup=ozgargan_inline)
            else:
                cursor_.execute("DELETE FROM korzinka WHERE soni=0")
                connect_.commit()
                print(True)
                await call.answer('Buyurtma Berilmagan Mahsulot !')

    @dp.callback_query_handler(text="save", state="*")
    async def state_save_korzinka(call: CallbackQuery):
        user_id = call.message.chat.id
        status = 0
        connect_ = sqlite3.connect('evos_.database.db')
        cursor_ = connect_.cursor()

        kozinka = cursor_.execute('SELECT * FROM korzinka WHERE user_id=? AND status=? AND mahsulot=?',
                                  (user_id, status, mahsulot_nomi)).fetchone()
        print(kozinka)
        cursor_.execute("UPDATE korzinka SET status=? WHERE user_id=? AND mahsulot=?", (1, kozinka[2], kozinka[1]))
        connect_.commit()
        await call.message.delete()
        await call.message.answer(f'Savatchaga <b>{kozinka[1]}</b> {kozinka[3]} ta qo`shildi', parse_mode='HTML')
