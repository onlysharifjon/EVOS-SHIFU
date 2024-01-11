from aiogram import types
from loader import dp
from aiogram.types import Message
from keyboards.default.menyubuttons import menyu_bir, setlar_menyu

from keyboards.default.userbuttons import start_button


@dp.message_handler(text="🍴 Menyu")
async def birinchi_menyu(message: types.Message):
    await message.answer("Tanlang:", reply_markup=menyu_bir)


@dp.message_handler(text="Orqaga🔙")
async def birinchi_menyu(message: types.Message):
    await message.answer('🛒 Asosiy Menyu', reply_markup=start_button)


@dp.message_handler(text='Setlar(8)')
async def setlar8(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIGI2Wft2OarG6k791GGzKBu1AOYIxPAAJs0jEbKnT4SBDLVcPvJZVCAQADAgADcwADNAQ',
                               reply_markup=setlar_menyu)


@dp.message_handler(text='🔙 Ortga qaytish')
async def setlar8(message: Message):
    await message.answer('Tanlang:', reply_markup=menyu_bir)

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo(message: Message):
    file_id = message.photo
    print(file_id[0]['file_id'])
