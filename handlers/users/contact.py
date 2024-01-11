from loader import dp
from aiogram import types
from keyboards.default.userbuttons import joylashuv, start_button


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_ga_javob_ber(message: types.Message):
    a = message.contact
    nomeri = a['phone_number']
    ismi = a['first_name']
    id_odam = a['user_id']
    print(a)
    await message.answer('Mnazilingizni jo`nating', reply_markup=joylashuv)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def locator(message: types.Message):
    text = message.location
    print("Ibrohim uchun", text)
    await message.answer("Locatsiya qabul qilindi", reply_markup=start_button)
