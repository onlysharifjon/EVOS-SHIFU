from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, bot
from aiogram import types

userlar = {}


@dp.callback_query_handler(text='combo1_minus')
async def combo_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        print(True)
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        print(userlar[call.message.chat.id])
        setlar_99 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data='combo1_minus'),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data='combo1_pilus')
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data='save_combo_plus')
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_99)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text='combo1_pilus')
async def combo_minus(call: types.CallbackQuery):
    print(True)
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1
    print(userlar[call.message.chat.id])
    setlar_99 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data='combo1_minus'),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data='combo1_pilus')
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data='save_combo_plus')
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_99)
