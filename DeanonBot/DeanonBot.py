from aiogram import Bot, Dispatcher, executor, types
import sqlite3
conn = sqlite3.connect('ПУТЬ К БАЗЕ ЛИБО ЕЁ НАЗВАНИЕ')
cursor = conn.cursor()

bot = Bot(token='ТОКЕН')
dp = Dispatcher(bot)

@dp.message_handler()
async def sms(msg: types.Message):
    chat_id = msg.chat.id
    if msg.from_user.id == 1886347358:
        if msg.text.isalpha() == 0 and len(msg.text) == 11 and msg.text[0] == "7":
            cursor.execute(f"SELECT * FROM phone WHERE number={msg.text}")
            row = cursor.fetchone()
            sex = str(row[4])
            namesurname = str(row[1])
            number = str(row[0])
            nickname = str(row[2])
            city = str(row[3])
            await bot.send_message(chat_id, "Номер телефона: " + number + "\nФИО: " + namesurname + "\nНикнейм: " + nickname + "\nЛокация: " + city + "\nПол: " + sex)
        else:
            await bot.send_message(chat_id, "Введите номер в формате 79XXXXXXXXX")
    else:
        await bot.send_message(chat_id, "Нет доступа к боту")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)