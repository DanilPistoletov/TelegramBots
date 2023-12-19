import asyncio
from aiogram import Bot, Dispatcher, F, types
AdminID = СЮДАВАШАЙДИ
banlist = []

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

bot = Bot(token='СЮДАТОКЕНБОТА')
dp = Dispatcher()

@dp.message(F.text)
async def sms(msg: types.Message):
    chat_id = msg.chat.id
    if msg.from_user.id in banlist:
        pass
    elif msg != "" and msg.from_user.id != AdminID:
        report = f"Сообщение: {msg.text}\nID пользователя: {msg.from_user.id}\nНик пользователя: {msg.from_user.full_name}"
        await bot.send_message(chat_id, "Сообщение отправлено")
        await bot.send_message(AdminID, report)
    elif msg.text[:5] == "!ban " and msg.from_user.id == AdminID:
        banlist.append(int(msg.text[5:]))
        await bot.send_message(chat_id, f"Пользователь {msg.text[5:]} заблокирован")
    elif msg.text[:8] == "!banlist" and msg.from_user.id == AdminID:
        await bot.send_message(chat_id, f"Список заблокированных ID: {banlist}")
    elif msg.text[:9] == "!ответить" and msg.from_user.id == AdminID:
        sms = msg.text[10:]
        sms = sms.split(" ")
        await bot.send_message(chat_id=sms[0], text=sms[1])


if __name__ == '__main__':
    asyncio.run(main())