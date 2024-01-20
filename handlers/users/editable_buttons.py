from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp, bot
from aiogram import types

userlar = {}


@dp.callback_query_handler(text='Combo_Plus_Isituvchan_(Qora choy)_minus')
async def combo_choy_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1

        setlar_99 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data='Combo_Plus_Isituvchan_(Qora choy)_minus'),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data='Combo_Plus_Isituvchan_(Qora choy)_pilus')
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish",
                                         callback_data='save_Combo_Plus_Isituvchan_(Qora choy)')
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_99)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text='Combo_Plus_Isituvchan_(Qora choy)_pilus')
async def combo_choy_plus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_99 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data='Combo_Plus_Isituvchan_(Qora choy)_minus'),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data='Combo_Plus_Isituvchan_(Qora choy)_pilus')
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data='save_Combo_Plus_Isituvchan_(Qora choy)')
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_99)


@dp.callback_query_handler(text='fit_combo_minus')
async def fit_combo_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1

        setlar_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data='fit_combo_minus'),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data='fit_combo_pilus')
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data='save_fitcombo')
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_2)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text='fit_combo_pilus')
async def fit_combo_plus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data='fit_combo_minus'),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data='fit_combo_pilus')
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data='save_fitcombo')
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_2)


@dp.callback_query_handler(text="Iftar_kofte_grill_mol_go'shtidan_minus")
async def Iftar_kofte_grill_mol_goshtidan_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1

        setlar_3 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Iftar_kofte_grill_mol_go'shtidan_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Iftar_kofte_grill_mol_go'shtidan_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish",
                                         callback_data="save_Iftar_kofte_grill_mol_go'shtidan")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_3)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Iftar_kofte_grill_mol_go'shtidan_pilus")
async def Iftar_kofte_grill_mol_goshtidano_plus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Iftar_kofte_grill_mol_go'shtidan_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Iftar_kofte_grill_mol_go'shtidan_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish",
                                     callback_data="save_Iftar_kofte_grill_mol_go'shtidan")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_3)


@dp.callback_query_handler(text="Donar_boks_mol_go'shtidan_minus")
async def Donar_boks_mol_goshtidan_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1

        setlar_4 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Donar_boks_mol_go'shtidan_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Donar_boks_mol_go'shtidan_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donar_boks_mol_go'shtidan")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_4)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Donar_boks_mol_go'shtidan_pilus")
async def Donar_boks_mol_goshtidan_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Donar_boks_mol_go'shtidan_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Donar_boks_mol_go'shtidan_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donar_boks_mol_go'shtidan")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_4)


@dp.callback_query_handler(text="Donar_boks_tovuq_go'shtidan_minus")
async def Donar_boks_tovuq_goshtidan_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        setlar_5 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Donar_boks_tovuq_go'shtidan_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Donar_boks_tovuq_go'shtidan_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donar_boks_tovuq_go'shtidan")
                ]
            ]
        )

        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_5)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Donar_boks_tovuq_go'shtidan_pilus")
async def Donar_boks_tovuq_goshtidan_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_5 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Donar_boks_tovuq_go'shtidan_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Donar_boks_tovuq_go'shtidan_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donar_boks_tovuq_go'shtidan")
            ]
        ]
    )

    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_5)


@dp.callback_query_handler(text="COMBO+_minus")
async def COMBO_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        setlar_6 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="COMBO+_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="COMBO+_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_COMBO+")
                ]
            ]
        )

        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_6)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="COMBO+_pilus")
async def COMBO_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_6 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="COMBO+_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="COMBO+_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_COMBO+")
            ]
        ]
    )

    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_6)


@dp.callback_query_handler(text="Iftar_strips_tovuq_go'shtidan_minus")
async def Iftar_strips_tovuq_goshtidan_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        setlar_7 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Iftar_strips_tovuq_go'shtidan_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Iftar_strips_tovuq_go'shtidan_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Iftar_strips_tovuq_go'shtidan")
                ]
            ]
        )

        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_7)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Iftar_strips_tovuq_go'shtidan_pilus")
async def Iftar_strips_tovuq_goshtidan_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_7 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Iftar_strips_tovuq_go'shtidan_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Iftar_strips_tovuq_go'shtidan_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Iftar_strips_tovuq_go'shtidan")
            ]
        ]
    )

    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_7)


@dp.callback_query_handler(text="Kids_COMBO_minus")
async def Kids_COMBO_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        setlar_8 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Kids_COMBO_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Kids_COMBO_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Kids_COMBO")
                ]
            ]
        )

        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=setlar_8)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Kids_COMBO_pilus")
async def Kids_COMBO_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    setlar_8 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Kids_COMBO_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Kids_COMBO_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Kids_COMBO")
            ]
        ]
    )

    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=setlar_8)


@dp.callback_query_handler(text="Mol_goʼshtidan_qalampir_lavash_minus")
async def Mol_goshtidan_qalampir_lavash_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        lavash_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Mol_goʼshtidan_qalampir_lavash_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Mol_goʼshtidan_qalampir_lavash_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Mol_goʼshtidan_qalampir_lavash")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=lavash_1)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Mol_goʼshtidan_qalampir_lavash_pilus")
async def Mol_goshtidan_qalampir_lavash_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    lavash_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Mol_goʼshtidan_qalampir_lavash_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Mol_goʼshtidan_qalampir_lavash_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Mol_goʼshtidan_qalampir_lavash")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=lavash_1)


@dp.callback_query_handler(text="Tovuq_goʼshtli_qalampir_lavash_minus")
async def Tovuq_goshtli_qalampir_lavash_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        lavash_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Tovuq_goʼshtli_qalampir_lavash_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Tovuq_goʼshtli_qalampir_lavash_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Tovuq_goʼshtli_qalampir_lavash")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=lavash_2)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Tovuq_goʼshtli_qalampir_lavash_pilus")
async def Tovuq_goshtli_qalampir_lavash_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    lavash_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Tovuq_goʼshtli_qalampir_lavash_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Tovuq_goʼshtli_qalampir_lavash_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Tovuq_goʼshtli_qalampir_lavash")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=lavash_2)


@dp.callback_query_handler(text="FITTER_minus")
async def FITTER_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        lavash_5 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="FITTER_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="FITTER_pilus'")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_FITTER")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=lavash_5)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="FITTER_pilus")
async def FITTER_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    lavash_5 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="FITTER_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="FITTER_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_FITTER")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=lavash_5)


@dp.callback_query_handler(text="Gamburger_minus")
async def Gamburger_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        burger_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Gamburger_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Gamburger_pilus'")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Gamburger")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=burger_1)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Gamburger_pilus")
async def Gamburger_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    burger_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Gamburger_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Gamburger_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Gamburger")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=burger_1)


@dp.callback_query_handler(text="Double_burger_minus")
async def Double_burger_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        burger_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Double_burger_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Double_burger_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Double_burger")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=burger_2)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Double_burger_pilus")
async def Double_burger_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    burger_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Double_burger_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Double_burger_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Double_burger")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=burger_2)


@dp.callback_query_handler(text="Cheese_burger_minus")
async def Cheese_burger_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        burger_3 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Cheese_burger_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Cheese_burger_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Cheese_burger")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=burger_3)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Cheese_burger_pilus")
async def Cheese_burger_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    burger_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Cheese_burger_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Cheese_burger_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Cheese_burger")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=burger_3)


@dp.callback_query_handler(text="Double_cheese_minus")
async def Double_cheese_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        burger_4 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Double_cheese_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Double_cheese_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Double_cheese")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=burger_4)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Double_cheese_pilus")
async def Double_cheese_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    burger_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Double_cheese_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Double_cheese_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Double_cheese")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=burger_4)


@dp.callback_query_handler(text="Hot_dog_baguette_minus")
async def Hot_dog_baguette_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Hot_dog_baguette_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Hot_dog_baguette_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_baguette")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_1)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Hot_dog_baguette_pilus")
async def Hot_dog_baguette_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Hot_dog_baguette_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Hot_dog_baguette_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_baguette")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_1)


@dp.callback_query_handler(text="Sub_tovuq_cheese_minus")
async def Sub_tovuq_cheese_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Sub_tovuq_cheese_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Sub_tovuq_cheese_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_tovuq_cheese")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_2)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Sub_tovuq_cheese_pilus")
async def Sub_tovuq_cheese_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Sub_tovuq_cheese_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Sub_tovuq_cheese_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_tovuq_cheese")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_2)


@dp.callback_query_handler(text="Sub_tovuq_minus")
async def Sub_tovuq_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_3 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Sub_tovuq_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Sub_tovuq_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_tovuq")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_3)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Sub_tovuq_pilus")
async def Sub_tovuq_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Sub_tovuq_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Sub_tovuq_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_tovuq")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_3)


@dp.callback_query_handler(text="Hot_dog_baguette_double_minus")
async def Hot_dog_baguette_double_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_4 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Hot_dog_baguette_double_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Hot_dog_baguette_double_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_baguette_double")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_4)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Hot_dog_baguette_double_pilus")
async def Hot_dog_baguette_double_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Hot_dog_baguette_double_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Hot_dog_baguette_double_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_baguette_double")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_4)


@dp.callback_query_handler(text="Hot_dog_kids_minus")
async def Hot_dog_kids_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_5 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Hot_dog_kids_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Hot_dog_kids_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_kids")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_5)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Hot_dog_kids_pilus")
async def Hot_dog_kids_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_5 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Hot_dog_kids_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Hot_dog_kids_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_kids")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_5)


@dp.callback_query_handler(text="Sub_go'sht_cheese_minus")
async def Sub_gosht_cheese_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_6 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Sub_go'sht_cheese_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Sub_go'sht_cheese_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_go'sht_cheese")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_6)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Sub_go'sht_cheese_pilus")
async def Sub_gosht_cheese_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_6 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Sub_go'sht_cheese_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Sub_go'sht_cheese_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_go'sht_cheese")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_6)


@dp.callback_query_handler(text="Hot_dog_classic_minus")
async def Hot_dog_classic_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_7 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Hot_dog_classic_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Hot_dog_classic_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_classic")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_7)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Hot_dog_classic_pilus")
async def Hot_dog_classic_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_7 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Hot_dog_classic_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Hot_dog_classic_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Hot_dog_classic")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_7)


@dp.callback_query_handler(text="Sub_go'sht_minus")
async def Sub_gosht_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        hot_dog_8 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Sub_go'sht_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Sub_go'sht_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_go'sht")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=hot_dog_8)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Sub_go'sht_pilus")
async def Sub_gosht_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    hot_dog_8 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Sub_go'sht_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Sub_go'sht_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sub_go'sht")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=hot_dog_8)


@dp.callback_query_handler(text="Sok_dena_0,33l_minus")
async def Sok_dena_0_33l_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Sok_dena_0,33l_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Sok_dena_0,33l_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sok_dena_0,33l")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_1)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Sok_dena_0,33l_pilus")
async def Sok_dena_0_33l_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Sok_dena_0,33l_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Sok_dena_0,33l_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Sok_dena_0,33l")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_1)


@dp.callback_query_handler(text="Suv_0,5_minus")
async def Suv_0_5_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Suv_0,5_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Suv_0,5_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Suv_0,5")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_2)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Suv_0,5_pilus")
async def Suv_0_5_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Suv_0,5_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Suv_0,5_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Suv_0,5")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_2)


@dp.callback_query_handler(text="Pepsi_0,5_minus")
async def Pepsi_0_5_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_3 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Pepsi_0,5_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Pepsi_0,5_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Pepsi_0,5")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_3)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Pepsi_0,5_pilus")
async def Pepsi_0_5_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Pepsi_0,5_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Pepsi_0,5_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Pepsi_0,5")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_3)


@dp.callback_query_handler(text="Pepsi_1,5_minus")
async def Pepsi_1_5_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_4 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Pepsi_1,5_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Pepsi_1,5_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Pepsi_1,5")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_4)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Pepsi_1,5_pilus")
async def Pepsi_1_5_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Pepsi_1,5_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Pepsi_1,5_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Pepsi_1,5")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_4)


@dp.callback_query_handler(text="Quyib_beriladigan_Pepsi_minus")
async def Quyib_beriladigan_Pepsi_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_5 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Quyib_beriladigan_Pepsi_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Quyib_beriladigan_Pepsi_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Quyib_beriladigan_Pepsi")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_5)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Quyib_beriladigan_Pepsi_pilus")
async def Quyib_beriladigan_Pepsi_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_5 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Quyib_beriladigan_Pepsi_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Quyib_beriladigan_Pepsi_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Quyib_beriladigan_Pepsi")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_5)


@dp.callback_query_handler(text="Bliss_sharbati_minus")
async def Bliss_sharbati_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_6 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Bliss_sharbati_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Bliss_sharbati_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Bliss_sharbati")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_6)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Bliss_sharbati_pilus")
async def Bliss_sharbati_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_6 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Bliss_sharbati_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Bliss_sharbati_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Bliss_sharbati")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_6)


@dp.callback_query_handler(text="Amerikano_minus")
async def Amerikano_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_7 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Amerikano_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Amerikano_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Amerikano")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_7)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Amerikano_pilus")
async def Amerikano_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_7 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Amerikano_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Amerikano_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Amerikano")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_7)


@dp.callback_query_handler(text="Latte_minus")
async def Latte_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_8 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Latte_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Latte_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Latte")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_8)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Latte_pilus")
async def Latte_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_8 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Latte_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Latte_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Latte")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_8)


@dp.callback_query_handler(text="Ko'k_choy_minus")
async def Kok_choy_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_9 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Ko'k_choy_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Ko'k_choy_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Ko'k_choy")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_9)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Ko'k_choy_pilus")
async def Kok_choy_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_9 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Ko'k_choy_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Ko'k_choy_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Ko'k_choy")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_9)


@dp.callback_query_handler(text="Qora_choy_minus")
async def Qora_choy_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_10 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Qora_choy_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Qora_choy_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Qora_choy")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_10)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Qora_choy_pilus")
async def Qora_choy_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_10 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Qora_choy_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Qora_choy_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Qora_choy")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_10)


@dp.callback_query_handler(text="Limonli_ko'k_choy_minus")
async def Limonli_kok_choy_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        ichimliklar_11 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Limonli_ko'k_choy_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Limonli_ko'k_choy_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Limonli_ko'k_choy")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=ichimliklar_11)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Limonli_ko'k_choy_pilus")
async def Limonli_kok_choy_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    ichimliklar_11 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Limonli_ko'k_choy_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Limonli_ko'k_choy_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Limonli_ko'k_choy")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=ichimliklar_11)


@dp.callback_query_handler(text="Medovik_Asalim_minus")
async def Medovik_Asalim_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        shirinliklar_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Medovik_Asalim_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Medovik_Asalim_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Medovik_Asalim")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=shirinliklar_1)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Medovik_Asalim_pilus")
async def Medovik_Asalim_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    shirinliklar_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Medovik_Asalim_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Medovik_Asalim_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Medovik_Asalim")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=shirinliklar_1)


@dp.callback_query_handler(text="Chizkeyk_minus")
async def Chizkeyk_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        shirinliklar_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Chizkeyk_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Chizkeyk_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Chizkeyk")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=shirinliklar_2)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Chizkeyk_pilus")
async def Chizkeyk_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    shirinliklar_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Chizkeyk_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Chizkeyk_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Chizkeyk")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=shirinliklar_2)


@dp.callback_query_handler(text="Donut_karameli_minus")
async def Donut_karameli_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        shirinliklar_3 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Donut_karameli_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Donut_karameli_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donut_karameli")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=shirinliklar_3)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Donut_karameli_pilus")
async def Donut_karameli_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    shirinliklar_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Donut_karameli_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Donut_karameli_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donut_karameli")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=shirinliklar_3)


@dp.callback_query_handler(text="Donut_mevali_minus")
async def Donut_mevali_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        shirinliklar_4 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Donut_mevali_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Donut_mevali_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donut_mevali")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=shirinliklar_4)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Donut_mevali_pilus")
async def Donut_mevali_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    shirinliklar_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Donut_mevali_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Donut_mevali_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Donut_mevali")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=shirinliklar_4)


@dp.callback_query_handler(text="Ketchup_minus")
async def Ketchup_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_1 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Ketchup_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Ketchup_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Ketchup")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_1)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Ketchup_pilus")
async def Ketchup_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_1 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Ketchup_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Ketchup_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Ketchup")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_1)


@dp.callback_query_handler(text="Pishloqli_sous_minus")
async def Pishloqli_sous_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_2 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Pishloqli_sous_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Pishloqli_sous_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Pishloqli_sous")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_2)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Pishloqli_sous_pilus")
async def Pishloqli_sous_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_2 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Pishloqli_sous_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Pishloqli_sous_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Pishloqli_sous")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_2)


@dp.callback_query_handler(text="Chisnokli_sous_minus")
async def Chisnokli_sous_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_3 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Chisnokli_sous_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Chisnokli_sous_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Chisnokli_sous")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_3)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Chisnokli_sous_pilus")
async def Chisnokli_sous_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_3 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Chisnokli_sous_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Chisnokli_sous_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Chisnokli_sous")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_3)


@dp.callback_query_handler(text="Chili_sous_minus")
async def Chili_sous_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_4 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Chili_sous_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Chili_sous_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Chili_sous")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_4)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Chili_sous_pilus")
async def Chili_sous_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_4 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Chili_sous_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Chili_sous_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Chili_sous")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_4)


@dp.callback_query_handler(text="Barbekyu_sousi_minus")
async def Barbekyu_sousi_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_5 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Barbekyu_sousi_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Barbekyu_sousi_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Barbekyu_sousi")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_5)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Barbekyu_sousi_pilus")
async def Barbekyu_sousi_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_5 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Barbekyu_sousi_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Barbekyu_sousi_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Barbekyu_sousi")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_5)


@dp.callback_query_handler(text="Guruch_minus")
async def Guruch_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_6 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Guruch_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Guruch_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Guruch")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_6)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Guruch_pilus")
async def Guruch_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_6 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Guruch_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Guruch_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Guruch")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_6)


@dp.callback_query_handler(text="Salat_minus")
async def Salat_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_7 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Salat_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Salat_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Salat")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_7)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Salat_pilus")
async def Salat_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_7 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Salat_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Salat_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Salat")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_7)


@dp.callback_query_handler(text="Non_minus")
async def Non_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_8 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Non_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Non_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Non")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_8)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Non_pilus")
async def Non_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_8 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Non_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Non_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Non")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_8)


@dp.callback_query_handler(text="Tovuq_Strips_minus")
async def Tovuq_Strips_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_9 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Tovuq_Strips_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Tovuq_Strips_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Tovuq_Strips")
                ]
            ]
        )
        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_9)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Tovuq_Strips_pilus")
async def Tovuq_Strips_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_9 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Tovuq_Strips_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Tovuq_Strips_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Tovuq_Strips")
            ]
        ]
    )
    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_9)


@dp.callback_query_handler(text="Fri_minus")
async def Fri_minus(call: types.CallbackQuery):
    if userlar[call.message.chat.id] > 1:
        userlar[call.message.chat.id] = userlar[call.message.chat.id] - 1
        garnirlar_10 = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-', callback_data="Fri_minus"),
                    InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                    InlineKeyboardButton(text='+', callback_data="Fri_pilus")
                ],
                [
                    InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Fri")
                ]
            ]
        )

        await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                            reply_markup=garnirlar_10)
    else:
        await call.answer("Eng kam Mahsulot soni 1 ta")


@dp.callback_query_handler(text="Fri_pilus")
async def Fri_pilus(call: types.CallbackQuery):
    userlar[call.message.chat.id] = userlar[call.message.chat.id] + 1

    garnirlar_10 = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='-', callback_data="Fri_minus"),
                InlineKeyboardButton(text=f'{userlar[call.message.chat.id]}', callback_data=f'1'),
                InlineKeyboardButton(text='+', callback_data="Fri_pilus")
            ],
            [
                InlineKeyboardButton(text="📥 Savatga qo'shish", callback_data="save_Fri")
            ]
        ]
    )

    await bot.edit_message_reply_markup(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                        reply_markup=garnirlar_10)
