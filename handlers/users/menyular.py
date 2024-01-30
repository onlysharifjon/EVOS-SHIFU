from aiogram import types
from loader import dp
from aiogram.types import Message
from keyboards.default.menyubuttons import menyu_bir, setlar_menyu, lavashlar_buttons, shaurmalar_buttons, \
    burgerlar_buttons, \
    hot_doglar_buttons, ichimliklar_buttons, shirinliklar_buttons, garnirlar_buttons
from keyboards.default.userbuttons import start_button

#
@dp.message_handler(text="🍴 Menyu")
async def birinchi_menyu(message: types.Message):
    await message.answer("Tanlang:", reply_markup=menyu_bir)


@dp.message_handler(text='Setlar (8)')
async def setlar8(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIGI2Wft2OarG6k791GGzKBu1AOYIxPAAJs0jEbKnT4SBDLVcPvJZVCAQADAgADcwADNAQ',
                               reply_markup=setlar_menyu)


@dp.message_handler(text='Lavash (9)')
async def Lavash9(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIGnmWhENdG-XtsjnvkFJxkqMKRqPbVAAJe0zEbPAABCUkYLpcxOXN68gEAAwIAA3MAAzQE',
                               reply_markup=lavashlar_buttons)


@dp.message_handler(text='Shaurma (4)')
async def Shaurma4(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIG2WWhGVgvtYx7pV8bH-CxvmiQMBkHAAKx0zEbPAABCUkuL-xfS6MVOQEAAwIAA3MAAzQE',
                               reply_markup=shaurmalar_buttons)


@dp.message_handler(text='Burger (4)')
async def Burger4(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIHAWWhHT12G9105qicqEAWJT_pkQpoAALX0zEbPAABCUkNQ5ono2v4awEAAwIAA3MAAzQE',
                               reply_markup=burgerlar_buttons)


@dp.message_handler(text='Hot-Dog (8)')
async def Hot_dog8(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIHImWhU5W_V2h8D7Okr1V1hrA4dKYGAAJP1TEbPAABCUnDq9Jah-MAAcYBAAMCAANzAAM0BA',
                               reply_markup=hot_doglar_buttons)


@dp.message_handler(text='Ichimliklar (11)')
async def ichimliklar11(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIHUWWhXDnJKydytUe_IUC2o2nOS3AoAAKH1TEbPAABCUlp4pmJ7tTLUQEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_buttons)


@dp.message_handler(text='Garnirlar (10)')
async def garnirlar10(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIHy2WhZ9Mi3jgAAU8hhKAiK4eFmOOOrQAC5dUxGzwAAQlJQHBEKGu_M9EBAAMCAANzAAM0BA',
                               reply_markup=garnirlar_buttons)


@dp.message_handler(text='Shirinlik va disertlar (4)')
async def shirinliklar4(message: Message):
    await message.answer_photo('AgACAgIAAxkBAAIHgmWhY7lytfkU3oA6yGBivFhRROJdAALI1TEbPAABCUkRKW24s9U3qQEAAwIAA3MAAzQE',
                               reply_markup=shirinliklar_buttons)


@dp.message_handler(text='🔙 Ortga qaytish')
async def ortga(message: Message):
    await message.answer('Tanlang:', reply_markup=menyu_bir)


@dp.message_handler(text="🔙 Orqaga qaytish")
async def birinchi_menyu(message: types.Message):
    await message.answer('🛒 Asosiy Menyu', reply_markup=start_button)


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def photo(message: Message):
    file_id = message.photo
    print(file_id[0]['file_id'])
