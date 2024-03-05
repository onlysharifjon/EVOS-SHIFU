from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.types import Message
from keyboards.default.menyubuttons import menyu_bir, setlar_menyu, lavashlar_buttons, shaurmalar_buttons, \
    burgerlar_buttons, \
    hot_doglar_buttons, ichimliklar_buttons, shirinliklar_buttons, garnirlar_buttons
from keyboards.default.userbuttons import start_button

from states.state_aiogram import Bolimlar


#
@dp.message_handler(text="🍴 Menyu", state='*')
async def birinchi_menyu(message: types.Message):
    await message.answer("Tanlang:", reply_markup=menyu_bir)
    await Bolimlar.barcha_menyular.set()


@dp.message_handler(text='Setlar (8)', state=Bolimlar.barcha_menyular)
async def setlar8(message: Message):
    await message.answer_photo(
        open("images/category_image/setlar(8).jpg", "rb"),
        reply_markup=setlar_menyu)
    await Bolimlar.setlar.set()


#

@dp.message_handler(text='Lavash (9)', state=Bolimlar.barcha_menyular)
async def Lavash9(message: Message):
    await message.answer_photo(
        open("images/category_image/lavash(9).jpg", "rb"),
        reply_markup=lavashlar_buttons)
    await Bolimlar.setlar.set()


@dp.message_handler(text='Shaurma (4)', state=Bolimlar.barcha_menyular)
async def Shaurma4(message: Message):

    await message.answer_photo(
        open("images/category_image/shaurma(4).jpg", "rb"),
        reply_markup=shaurmalar_buttons)
    await Bolimlar.setlar.set()


@dp.message_handler(text='Burger (4)', state=Bolimlar.barcha_menyular)
async def Burger4(message: Message):

    await message.answer_photo(open("images/category_image/burger(4).jpg", "rb"),
                               reply_markup=burgerlar_buttons)
    await Bolimlar.setlar.set()


##
@dp.message_handler(text='Hot-Dog (8)', state=Bolimlar.barcha_menyular)
async def Hot_dog8(message: Message):

    await message.answer_photo(open("images/category_image/Hot-Dog(8).jpg", "rb"),
                               reply_markup=hot_doglar_buttons)
    await Bolimlar.setlar.set()


@dp.message_handler(text='Ichimliklar (11)', state=Bolimlar.barcha_menyular)
async def ichimliklar11(message: Message):

    await message.answer_photo(open("images/category_image/ichimliklar(11).jpg", "rb"),
                               reply_markup=ichimliklar_buttons)
    await Bolimlar.setlar.set()


@dp.message_handler(text='Garnirlar (10)', state=Bolimlar.barcha_menyular)
async def garnirlar10(message: Message):
    await message.answer_photo(open("images/category_image/garnirlar(10).jpg", "rb"),
                               reply_markup=garnirlar_buttons)
    await Bolimlar.setlar.set()


@dp.message_handler(text='Shirinlik va disertlar (4)', state=Bolimlar.barcha_menyular)
async def shirinliklar4(message: Message):
    await Bolimlar.setlar.set()
    await message.answer_photo(open("images/category_image/shirinlik_va_disertlar(4).jpg", "rb"),
                               reply_markup=shirinliklar_buttons)


@dp.message_handler(text='🔙 Ortga qaytish',state="*")
async def ortga(message: Message):
    await message.answer('Tanlang:', reply_markup=menyu_bir)
    await Bolimlar.barcha_menyular.set()


@dp.message_handler(text="🔙 Orqaga qaytish",state="*")
async def birinchi_menyu(message: types.Message, state: FSMContext):
    await message.answer('🛒 Asosiy Menyu', reply_markup=start_button)
    await state.finish()
