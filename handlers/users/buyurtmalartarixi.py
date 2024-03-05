from loader import dp
from aiogram import types
import sqlite3

connect = sqlite3.connect('evos_.database.db')

cursor = connect.cursor()


async def filtlab_ber(odam_id):
    k = cursor.execute('SELECT * FROM korzinka WHERE user_id = ? AND status=?', (odam_id, 1)).fetchall()
    return k


@dp.callback_query_handler(text="rozi-boldim")
async def tasdiqlash(call: types.CallbackQuery):
    odam_id = call.message.chat.id
    listda_olamiz = await filtlab_ber(odam_id)
    print(listda_olamiz)

    for i in listda_olamiz:
        cursor.execute("INSERT INTO buyurtma_tarixi (buyurtma, buyurtmachi_id) VALUES (?,?)", (f"{i[1]} {i[3]}", i[2]))
        print(i)
    connect.commit()
    cursor.execute("DELETE FROM korzinka WHERE user_id=? AND status=?", (odam_id, 1))
    connect.commit()
    from .savat import dict_
    if listda_olamiz == []:
        await call.message.answer('🛒 Savat bo`sh')
    else:
        await call.message.answer_photo(open('images/payment/img.png','rb'), caption=f'<a href="https://my.click.uz/clickp2p/43B4B7321486FB8289B75368B5B371D00F077290C586F1FA7BC9F0E742B5B176">*880*3*998905122180*{dict_[odam_id]}#</a>', parse_mode='HTML')

        await call.message.answer(
            '<i>Sizning buyurtmangiz qabul qilindi!😋</i>\n\n 📞<code>+998 97 777 77 77</code>\n💵To`lov Amalga oshirilganda🏃<i>Kuryermiz siz bilan yaqin orada aloqaga chiqadi</i>')


@dp.message_handler(text='📋 Mening buyurtmalarim', state='*')
async def buyurtmalarim(message: types.Message):
    print(True)

    # await message.reply('')
