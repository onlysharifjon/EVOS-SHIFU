from loader import dp
from aiogram import types
from keyboards.default.userbuttons import joylashuv, start_button
from .start import cursor, connect


@dp.message_handler(content_types=types.ContentTypes.CONTACT)
async def contact_ga_javob_ber(message: types.Message):
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS contact_table(phone_number TEXT,last_name TEXT,user_id INTEGER,username TEXT)')
    a = message.contact
    nomeri = a['phone_number']
    ismi = a['first_name']
    id_odam = a['user_id']
    username = message.from_user.username
    print(username)
    cursor.execute('INSERT INTO contact_table VALUES(?,?,?,?)', (nomeri, ismi, message.from_user.id, username))
    connect.commit()
    await message.answer('Manzilingizni jo`nating', reply_markup=joylashuv)


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def locator(message: types.Message):
    text = message.location
    print(text)
    await message.answer("Locatsiya qabul qilindi", reply_markup=start_button)
