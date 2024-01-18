from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.userbuttons import start_button, telefon

from loader import dp
from handlers.users.mahsulotlar import userlar
odamlar = []


@dp.message_handler(commands='start')
async def starter(message: types.Message):
    userlar[message.from_user.id] = 1
    if message.from_user.id not in odamlar:
        odamlar.append(message.from_user.id)
        await message.answer("<b>EVOS |</b> Доставка botiga xush kelibsiz!", reply_markup=telefon)
    else:
        await message.answer('<b>EVOS |</b> Доставка botiga xush kelibsiz!', reply_markup=start_button)
