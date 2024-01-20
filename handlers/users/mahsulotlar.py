from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from loader import dp
from aiogram import types
from loader import bot
from keyboards.inline.mahsulotlar_inline import setlar_1, setlar_2, setlar_3, setlar_4, setlar_5, setlar_6, setlar_7, \
    setlar_8, \
    lavash_1, lavash_2, lavash_3, lavash_4, lavash_5, lavash_6, lavash_7, \
    shaurma_1, shaurma_2, shaurma_3, shaurma_4, \
    burger_1, burger_2, burger_3, burger_4, \
    hot_dog_1, hot_dog_2, hot_dog_3, hot_dog_4, hot_dog_5, hot_dog_6, hot_dog_7, hot_dog_8, \
    ichimliklar_1, ichimliklar_2, ichimliklar_3, ichimliklar_4, ichimliklar_5, ichimliklar_6, ichimliklar_7, \
    ichimliklar_8, ichimliklar_9, ichimliklar_10, ichimliklar_11, \
    shirinliklar_1, shirinliklar_2, shirinliklar_3, shirinliklar_4, \
    garnirlar_1, garnirlar_2, garnirlar_3, garnirlar_4, garnirlar_5, garnirlar_6, garnirlar_7, garnirlar_8, garnirlar_9, \
    garnirlar_10

from aiogram.dispatcher.storage import FSMContext
from .editable_buttons import userlar

@dp.message_handler(text='Combo Plus Isituvchan (Qora choy)')
async def setlar1(message: types.Message, state: FSMContext):
    userlar[message.from_user.id] = 1

    # await message.delete()
    # btn = setlar_1['inline_keyboard'][0][1]
    # state_data = await state.get_data()
    # btn['text'] = state_data.get('combo1', 1)
    await message.answer_photo('AgACAgIAAxkBAAIGKWWfuHfPdQ52hyOY8bo_HCWk0BVdAAJz0jEbKnT4SFmH0C4R5RoCAQADAgADcwADNAQ',
                               reply_markup=setlar_1, caption=" Narxi: 16 000 so'm")


@dp.message_handler(text="FitCombo")
async def setlar2(message: types.Message):
    userlar[message.from_user.id] = 1

    await message.answer_photo('AgACAgIAAxkBAAIGN2WfvgQx73bkHVY3wxAa2f0J3qqpAAL8xDEbj7LASZsZmVlRGVCHAQADAgADcwADNAQ',
                               reply_markup=setlar_2, caption=" Narxi: 30 000 so'm")


@dp.message_handler(text="Iftar kofte grill mol go'shtidan")
async def setlar3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGTWWhB8L1D-KkzzAz-srlT75MZqjDAAIq0zEbPAABCUkznULuKWZRIQEAAwIAA3MAAzQE',
                               reply_markup=setlar_3,
                               caption=f"""Muborak RAMAZON oyi munosabati bilan maxsus taklif! Mol go'shtli 5 dona shirali gril-kotletlari, guruch, limon sharbati bilan boyitilgan qizil karamli salat, pomidorlar va yong'oqlardan tayyorlangan maxsus quyuq RAMAZON sousi. Iftorlik vaqtingiz uchun ideal yechim!
Narxi: 35 000 so'm""")


@dp.message_handler(text="Donar boks  mol go'shtidan")
async def setlar4(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGe2WhC1UB_qjaxu4mXw6e_JVWaK6aAAI00zEbPAABCUkWOC2jpgbrZQEAAwIAA3MAAzQE',
                               reply_markup=setlar_4,
                               caption=f"""YANGILIK! Oq kunjut sousi ostidagi shirali grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, qizil karamdan tayyorlangan barra salatdan tashkil topgan qatlamlarning to'yimli uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 34 000 so'm""")


@dp.message_handler(text="Donar boks tovuq go'shtidan")
async def setlar5(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGfmWhDDm-Drc3GclIkpzWl3Ns6JLhAAI70zEbPAABCUl8j8tRW3JjpQEAAwIAA3MAAzQE',
                               reply_markup=setlar_5,
                               caption=f"""YANGILIK!  Yangi, maxsus tayyorlangan teriyaki sousi, grill tovuq go'shti, qarsildoq kartoshka-fri, donador guruch, limon sharbati bilan to'yintirilgan qizil karamdan tayyorlangan barra salatning noodatiy mazali uyg'unlashuvi. Qulay, ixcham, ammo to'yimli qadoq!
Narxi: 32 000 so'm""")


@dp.message_handler(text="COMBO+")
async def setlar6(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGf2WhDLvv4SweUj1Ebt5KR6LLplrIAAI-0zEbPAABCUmP8HDiCaOlIgEAAwIAA3MAAzQE',
                               reply_markup=setlar_6,
                               caption=f"""Yangi yaxshi taklif! Issiq qarsildoq qovurilgan kartoshka va bir stakan Pepsi"
Narxi: 16 000 so'm""")


@dp.message_handler(text="Iftar strips tovuq go'shtidan")
async def setlar7(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGgGWhDV0M7YqWZTxDv2ax_H_0_0ndAAIq0zEbPAABCUkznULuKWZRIQEAAwIAA3MAAzQE',
                               reply_markup=setlar_7,
                               caption=f"""Muborak RAMAZON oyi munosabati bilan maxsus taklif! Tovuqli 5 dona shirali gril-kotletlari, guruch, limon sharbati bilan boyitilgan qizil karamli salat, pomidorlar va yong'oqlardan tayyorlangan maxsus quyuq RAMAZON sousi. Iftorlik vaqtingiz uchun ideal yechim!
Narxi: 30 000 so'm""")


@dp.message_handler(text="Kids COMBO")
async def setlar8ci(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGgWWhDjAjtyMokbEbrD-5885J30pyAAJM0zEbPAABCUnXqwABvGQE6XwBAAMCAANzAAM0BA',
                               reply_markup=setlar_8, caption=" Narxi: 16 000 so'm")


@dp.message_handler(text="Mol goʼshtidan qalampir lavash")
async def lavash1(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGrGWhEZgikiERkCZ1mgdXe7fX48LjAAJi0zEbPAABCUkg_hzH19Y1DQEAAwIAA3MAAzQE',
                               reply_markup=lavash_1,
                               caption=f"""Qarsildoq chipslar, yangi bodring va pomidorlar bilan lavashga oʼralgan yumshoq mol goʼshti, bizning taʼmi oʼtkir qayla bilan
Narxi: 26 000 so'm""")


@dp.message_handler(text="Tovuq goʼshtli qalampir lavash")
async def lavash2(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGtGWhEkXE4sDn4DRiKGzU6xdKbVoHAAJs0zEbPAABCUnDAyjI7zeJiAEAAwIAA3MAAzQE',
                               reply_markup=lavash_2,
                               caption="""Yangi bodring va pomidorlar, qarsildoq chipslar bilan lavashga oʼralgan qovurilgan tovuq filesi, bizning taʼmi oʼtkir maxsus qayla bilan
Narxi:24 000 so'm""")


@dp.message_handler(text="Mol go'shtidan pishloqli lavash Standard")
async def lavash3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGtWWhEvn_LfqNl1onqoDsdnig6ODPAAJz0zEbPAABCUn9O3aEBWanygEAAwIAA3MAAzQE',
                               reply_markup=lavash_3,
                               caption="Tanlang:")


@dp.message_handler(text="Lavash cheese tovuq go'sht Standart")
async def lavash4(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGtmWhE9fIQHJa_jmx_hrBWYf3PypyAAJ00zEbPAABCUme0TjsJfELKAEAAwIAA3MAAzQE',
                               reply_markup=lavash_4,
                               caption="Tanlang:")


@dp.message_handler(text="FITTER")
async def lavash5(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGt2WhFDmBGpxJVB93lf4ntaETCkTgAAJ90zEbPAABCUmfQAic3HP31QEAAwIAA3MAAzQE',
                               reply_markup=lavash_5,
                               caption="""Tovuq goʼshti, qarsildoq muztogʼ salati, yangi bodring va pomidorlar, fetaksa va bizning maxsus qaylamiz - barchasi yashil lavashga oʼralgan
Narxi: 22 000 so'm""")


@dp.message_handler(text="Lavash tovuq go'sht")
async def lavash6(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGuGWhFNX8650ZE15UT0Me-rxlmixRAAKC0zEbPAABCUnQRN8VWIEU3wEAAwIAA3MAAzQE',
                               reply_markup=lavash_6,
                               caption="Tanlang:")


@dp.message_handler(text="Lavash mol go'sht")
async def lavash7(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIGuWWhFYQNZ1c-bsUxSI_C3u-kFQvrAAKJ0zEbPAABCUm3O8m3EwwlNgEAAwIAA3MAAzQE',
                               reply_markup=lavash_7,
                               caption="Tanlang:")


@dp.message_handler(text="Shaurma qalampir mol go'sht")
async def shaurma1(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIG32WhGbJWaYBPRhWIbEMLSRN2YpNSAAK00zEbPAABCUnVy1Xxp8GMkgEAAwIAA3MAAzQE',
                               reply_markup=shaurma_1,
                               caption="")


@dp.message_handler(text="Shaurma tovuq go'sht")
async def shaurma2(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIG52WhGri072cspA_lK1cc4UvtsL_IAALE0zEbPAABCUlZXcI4dQZDswEAAwIAA3MAAzQE',
                               reply_markup=shaurma_2,
                               caption="")


@dp.message_handler(text="Shaurma qalampir tovuq go'sht")
async def shaurma3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIG6GWhG1OEAAEC21Hw1VJ9aWfzJIb4EAACxNMxGzwAAQlJWV3COHUGQ7MBAAMCAANzAAM0BA',
                               reply_markup=shaurma_3,
                               caption="")


@dp.message_handler(text="Shaurma mol go'sht")
async def shaurma4(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIG6WWhG7iftylJkNDLLEWyNM9LQ7mqAALL0zEbPAABCUkJXxikBol6WwEAAwIAA3MAAzQE',
                               reply_markup=shaurma_4,
                               caption="")


@dp.message_handler(text="Gamburger")
async def burger1(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHB2WhHgfLUJJobhgesG9m_p_j9YCcAALb0zEbPAABCUkBvQ0HnwW4YAEAAwIAA3MAAzQE',
                               reply_markup=burger_1,
                               caption=f"""Tabiiy mol go'shtidan shirali kotlet, yangi yetilib pishgan pomidor va marinadlangan bodringning dumaloq bo'lakchalari, Aysberg salat bargi, yumshoq, dumaloq bulochkadagi qaymoqli-tomatli sous ostida shirin, qizil piyoz halqasi
Narxi: 22 000 so'm""")


@dp.message_handler(text="Double burger")
async def burger2(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHCGWhHtGmlrTGrm17YUcOd_Z_jOVQAALd0zEbPAABCUmN3EJ7UzxkVgEAAwIAA3MAAzQE',
                               reply_markup=burger_2,
                               caption=f"""Tabiiy mol go'shtidan ikkita shirali kotlet, yangi yetilib pishgan pomidor va marinadlangan bodringning dumaloq bo'lakchalari, Aysberg salat bargi, yumshoq bulochkadagi qaymoqli-tomatli sous ostida shirin, qizil piyoz halqasi
Narxi: 33 000 so'm""")


@dp.message_handler(text="Cheese burger")
async def burger3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHCWWhH11vHpIXNAMQTCO3XkbY2wnsAALe0zEbPAABCUnsEJgS5KxW1wEAAwIAA3MAAzQE',
                               reply_markup=burger_3,
                               caption=f"""Tabiiy mol go'shtidan shirali kotlet, yangi yetilib pishgan pomidor va marinadlangan bodringning dumaloq bo'lakchalari, Aysberg salat bargi, yumshoq, dumaloq bulochkadagi qaymoqli-tomatli sous ostida Chedder pishlog'i bo'lagi
Narxi: 24 000 so'm""")


@dp.message_handler(text="Double cheese")
async def burger4ci(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHCmWhH-mQ9pMooNsMd4BQ-uMg1BwfAALh0zEbPAABCUkQ36moiloD0gEAAwIAA3MAAzQE',
                               reply_markup=burger_4,
                               caption=f"""Tabiiy mol go'shtidan ikkita shirali kotlet, yangi yetilib pishgan pomidor va marinadlangan bodringning dumaloq bo'lakchalari, Aysberg salat bargi, yumshoq, dumaloq bulochkadagi qaymoqli-tomatli sous ostida ikki bo'lak Chedder pishlog'i
Narxi: 37 000 so'm""")


@dp.message_handler(text="Hot-dog baguette")
async def Hot_dog1(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHL2WhVO3EtuxSB-qg1A19ygrv2NdqAAJY1TEbPAABCUk7_Rdd8FSvpwEAAwIAA3MAAzQE',
                               reply_markup=hot_dog_1,
                               caption=f"""Narx: 14 000 so'm""")


@dp.message_handler(text="Sub tovuq cheese")
async def Hot_dog2(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHMGWhVj6iEspXIxXdCU7HPR_X6SoKAAJc1TEbPAABCUmAYZfd2voN-gEAAwIAA3MAAzQE',
                               reply_markup=hot_dog_2,
                               caption=f"""Narx: 19 000 so'm""")


@dp.message_handler(text="Sub tovuq")
async def Hot_dog3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHMWWhVsR6wOOI1ukvYrcoIw0xKn1IAAJf1TEbPAABCUknE3gH5uyaWgEAAwIAA3MAAzQE',
                               reply_markup=hot_dog_3,
                               caption=f"""Narx: 17 000 so'm""")


@dp.message_handler(text="Hot-dog baguette double")
async def Hot_dog4(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHMmWhV6E8jRikeaIvy8A1-3Hd2APSAAJi1TEbPAABCUnqWrViEKAhpwEAAwIAA3MAAzQE',
                               reply_markup=hot_dog_4,
                               caption=f"""Narx: 21 000 so'm""")


@dp.message_handler(text="Hot-dog kids")
async def Hot_dog5(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHM2WhWBHf8qmcQcjlBsgwXraTnrCfAAJk1TEbPAABCUmR4jPvbBw_PwEAAwIAA3MAAzQE',
                               reply_markup=hot_dog_5,
                               caption=f"""Narx: 8 000 so'm""")


@dp.message_handler(text="Sub go'sht cheese")
async def Hot_dog6(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHNGWhWI9dtfm0zHPxK48lmRIgNjS2AAJn1TEbPAABCUlpu8_k75YAAS8BAAMCAANzAAM0BA',
                               reply_markup=hot_dog_6,
                               caption=f"""Narx: 21 000 so'm""")


@dp.message_handler(text="Hot-dog classic")
async def Hot_dog7(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHNWWhWQ4jzdaal1yMv9ZVPmMW-p6kAAJY1TEbPAABCUk7_Rdd8FSvpwEAAwIAA3MAAzQE',
                               reply_markup=hot_dog_7,
                               caption=f"""Narx: 8 000 so'm""")


@dp.message_handler(text="Sub go'sht")
async def Hot_dog8ci(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHNmWhWYPqWpJUZNDTqtYnHxS-2jsCAAJq1TEbPAABCUma6GnS2HarywEAAwIAA3MAAzQE',
                               reply_markup=hot_dog_8,
                               caption=f"""Narx: 19 000 so'm""")


@dp.message_handler(text="Sok dena 0,33l")
async def ichimliklar1(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHV2WhXMLzEtN3O0iaBiWuHkaQCG-dAAKL1TEbPAABCUmU42GiPANOqwEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_1,
                               caption=f"""Narx: 10 000 so'm""")


@dp.message_handler(text="Suv 0,5")
async def ichimliklar2(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHWGWhXWS3rWsU9tgbGWbZaEk5zLv7AAKO1TEbPAABCUmX8ReIbiZzlQEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_2,
                               caption=f"""Narx: 4 000 so'm""")


@dp.message_handler(text="Pepsi 0,5")
async def ichimliklar3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHWWWhXfbRaM3VPExU5j9M8htbJBbDAAKT1TEbPAABCUkN6_q7QjH0lQEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_3,
                               caption=f"""Narx: 9 000 so'm""")


@dp.message_handler(text="Pepsi 1,5")
async def ichimliklar4(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHW2WhXp3_Fw7HQqSHjr0IwwABKUwmHAACl9UxGzwAAQlJD2GM3v2IheABAAMCAANzAAM0BA',
                               reply_markup=ichimliklar_4,
                               caption=f"""Narx: 17 000 so'm""")


@dp.message_handler(text="Quyib beriladigan Pepsi")
async def ichimliklar5(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHXGWhXxwezGmWgP98Hzmd1t2aSS1gAAKb1TEbPAABCUm8V-yWQ-slSAEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_5,
                               caption=f"""Narx: 8 000 so'm""")


@dp.message_handler(text="Bliss sharbati")
async def ichimliklar6(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHXWWhX473oLlwGsLehqae9fwspLfoAAKe1TEbPAABCUl2hRTpsaqPIgEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_6,
                               caption=f"""Narx: 16 000 so'm""")


@dp.message_handler(text="Amerikano")
async def ichimliklar7(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHXmWhYAd3iEbMGwwH2cUKMOkKcw1sAAKq1TEbPAABCUlz8yugkHiagwEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_7,
                               caption=f"""Narx: 11 000 so'm""")


@dp.message_handler(text="Latte")
async def ichimliklar8(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHX2WhYILjIJeCviyB_dLDte3hJkmvAAKu1TEbPAABCUnitdUCHCWSrgEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_8,
                               caption=f"""Narx: 13 000 so'm""")


@dp.message_handler(text="Ko'k choy")
async def ichimliklar9(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHYGWhYO4VOeekxkUT_rMrJ8vMhHnJAAKx1TEbPAABCUm2WGTXfGMMWgEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_9,
                               caption=f"""Narx: 4 000 so'm""")


@dp.message_handler(text="Qora choy")
async def ichimliklar10(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHYWWhYWJWJwJSHPYvqwdjWII3xG3TAAK11TEbPAABCUmxs4_bFAvm9AEAAwIAA3MAAzQE',
                               reply_markup=ichimliklar_10,
                               caption=f"""Narx: 4 000 so'm""")


@dp.message_handler(text="Limonli ko'k choy")
async def ichimliklar11ci(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHYmWhYdKwoGdg9-V8BptRV-wTtHF3AAK91TEbPAABCUmLsDYyNs4DAAEBAAMCAANzAAM0BA',
                               reply_markup=ichimliklar_11,
                               caption=f"""Narx: 5 000 so'm""")


@dp.message_handler(text="Medovik Asalim")
async def shirinliklar1(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHhmWhZAEJu2uT7nlAsDsJBnuIqdd6AALL1TEbPAABCUniHOA_UlKJZQEAAwIAA3MAAzQE',
                               reply_markup=shirinliklar_1,
                               caption=f"""Narx: 16 000 so'm""")


@dp.message_handler(text="Chizkeyk")
async def shirinliklar2(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHh2WhZNyqj4FSeYYuNoHEc3z9-mXnAALO1TEbPAABCUlbtNWLb8SVkQEAAwIAA3MAAzQE',
                               reply_markup=shirinliklar_2,
                               caption=f"""Narx: 16 000 so'm""")


@dp.message_handler(text="Donut karameli")
async def shirinliklar3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHiGWhZV9qb6EH5TFjNehq7a_o-DlgAALS1TEbPAABCUnHuP61Lm3ZpwEAAwIAA3MAAzQE',
                               reply_markup=shirinliklar_3,
                               caption=f"""Narx: 15 000 so'm""")


@dp.message_handler(text="Donut mevali")
async def shirinliklar4(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHiWWhZdalbIm8Hbq0e1KqinGbfxfoAALU1TEbPAABCUm465d6AqF0mAEAAwIAA3MAAzQE',
                               reply_markup=shirinliklar_4,
                               caption=f"""Narx: 15 000 so'm""")


@dp.message_handler(text="Ketchup")
async def garnirlar1(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIHz2WhaCuZVS0q2OBRgPUF4TzXedrBAALm1TEbPAABCUlGyXdn4ZPVzAEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_1,
                               caption=f"""Narx: 2 000 so'm""")


@dp.message_handler(text="Pishloqli sous")
async def garnirlar2(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH0GWhaIYp08f3Ip3k6dFNNHOdmU7MAALq1TEbPAABCUn4clehVz9jCgEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_2,
                               caption=f"""Narx: 2 000 so'm""")


@dp.message_handler(text="Chisnokli sous")
async def garnirlar3(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH0WWhaPvfvkKH9KYCCrY84Gtlu2vfAALv1TEbPAABCUkHctNgzQbKGAEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_3,
                               caption=f"""Narx: 2 000 so'm""")


@dp.message_handler(text="Chili sous")
async def garnirlar4(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH0mWhaWhzAAGX6l9HpEoB22HAgtIhzQAC8tUxGzwAAQlJrW-krUi5fscBAAMCAANzAAM0BA',
                               reply_markup=garnirlar_4,
                               caption=f"""Narx: 2 000 so'm""")


@dp.message_handler(text="Barbekyu sousi")
async def garnirlar5(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH02Whadamp6P-6spkQ4_ugA7GndOMAALz1TEbPAABCUkwF7UCx7ZXTgEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_5,
                               caption=f"""Narx: 2 000 so'm""")


@dp.message_handler(text="Guruch")
async def garnirlar6(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH1GWhakLYy-css1oemhOFRXx_1yJUAAL31TEbPAABCUmWoNeE73AzpAEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_6,
                               caption=f"""Narx: 7 000 so'm""")


@dp.message_handler(text="Salat")
async def garnirlar7(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH1WWhapcBtWcdNdqYpVKcp5Ku-MfwAAL51TEbPAABCUkYIH_71xJzAQEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_7,
                               caption=f"""Narx: 7 000 so'm""")


@dp.message_handler(text="Non")
async def garnirlar8(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH1mWhawABpr75KUPD3QHBdEYgmbmc5AAC_dUxGzwAAQlJwT1p_02JZiwBAAMCAANzAAM0BA',
                               reply_markup=garnirlar_8,
                               caption=f"""Narx: 3 000 so'm""")


@dp.message_handler(text="Tovuq Strips")
async def garnirlar9(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH12Wha1vDOF_XhuMFxp67ym5KimssAAL-1TEbPAABCUlkCfzxK6cLlgEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_9,
                               caption=f"""Narx: 19 000 so'm""")


@dp.message_handler(text="Fri")
async def garnirlar10ci(message: types.Message):
    await message.answer_photo('AgACAgIAAxkBAAIH2GWha9WtF7_HVv3Sr5dRsRDAv7ysAAIC1jEbPAABCUmEmd8LJC9mYAEAAwIAA3MAAzQE',
                               reply_markup=garnirlar_10,
                               caption=f"""Narx: 14 000 so'm""")


# ----------------------------------------------------------------------------------------

