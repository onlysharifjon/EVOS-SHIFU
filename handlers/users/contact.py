from loader import dp
from aiogram import types


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_ga_javob_ber(message: types.Message):
    a = message.contact
    nomeri = a['phone_number']
    ismi = a['first_name']
    id_odam = a['user_id']
