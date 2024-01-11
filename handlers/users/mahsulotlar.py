from loader import dp
from aiogram import types

from keyboards.inline.mahsulotlar_inline import combo_plus_inline


@dp.message_handler(text="Combo Plus Isituvchan (Qora choy)")
async def combo_plush(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGKWWfuHfPdQ52hyOY8bo_HCWk0BVdAAJz0jEbKnT4SFmH0C4R5RoCAQADAgADcwADNAQ',
                               reply_markup=combo_plus_inline, caption='Narxi: 16 000 so`m')
