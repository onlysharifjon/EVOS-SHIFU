from loader import dp
from aiogram.types import Message
from keyboards.default.userbuttons import sozlama
@dp.message_handler(text = "⚙️ Sozlamalar")
async def sozlamar_func(message: Message):
    await message.answer('⚙️ Sozlamalar bo`limi ⚙️',reply_markup=sozlama)
from aiogram.types import ReplyKeyboardRemove
import sqlite3
connect_evos = sqlite3.connect('evos_.database.db')
cursor_evos = connect_evos.cursor()

connect_user = sqlite3.connect("userlar_malumotlari.db")
cursor_user = connect_user.cursor()
from .start import odamlar_test
@dp.message_handler(text = "Ma`lumotlarni O`chirish")
async def delete_func(message: Message):
    cursor_evos.execute(f"DELETE FROM korzinka WHERE user_id={message.from_user.id}")
    cursor_evos.execute(f"DELETE FROM buyurtma_tarixi WHERE buyurtmachi_id={message.from_user.id}")
    connect_evos.commit()

    cursor_user.execute(f"DELETE FROM userlar WHERE user_id={message.from_user.id}")
    connect_user.commit()
    odamlar_test.clear()
    await message.answer('Sizning Ma`lumotlaringiz muvaffaqiyatli o`chirildi 👋',reply_markup=ReplyKeyboardRemove())




