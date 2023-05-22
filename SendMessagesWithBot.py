from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = ''

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

import requests
while 1:
    chat_id = ""
    message = input()
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)