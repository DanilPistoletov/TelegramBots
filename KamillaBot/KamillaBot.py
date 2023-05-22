from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='')
dp = Dispatcher(bot)

@dp.message_handler()
async def sms(msg: types.Message):
    chat_id = msg.chat.id
    if "еда" in msg.text.lower():
        from random import randint
        checker = randint(1, 8)
        if checker == 1:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun9-4.userapi.com/impg/FF8OmtFL2F5cSdbZmALb_e7jvaj8Q0_i8k1iRw/WgS1d9Oi9eg.jpg?size=958x1238&quality=96&sign=e2057389dadf9075ae8321333dbff5de&type=album")
        if checker == 2:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun9-26.userapi.com/impg/V9l4oUb2-Cs590qGpa84dBNAV7ZmO36ZpXJ84g/UUiQRvBh0ZA.jpg?size=960x1280&quality=96&sign=ad9682c77faae99bdc83e51ce0d8f6f9&type=album")
        if checker == 3:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun9-55.userapi.com/impg/rU1LGaZnBJ0z0CfmlNL3JWEiPXEebXfKTJoqLw/yXb4-wJD8AY.jpg?size=1280x960&quality=96&sign=aa960c2fab0f9c687fbd16cbe31411d9&type=album")
        if checker == 4:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun9-74.userapi.com/impg/IqR7olIqWOJFw6zB_pn2DEjlynU7qb-9onWyXQ/e8O9gPfoc0s.jpg?size=957x1002&quality=96&sign=c34e6720d7e3d3e2d4ed3353c2f72a39&type=album")
        if checker == 5:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun58-1.userapi.com/impg/UEPmnxLvg7jefu8vNy_KbaxasKrZIXmf8M6b3w/4NJ3Ww6gLCQ.jpg?size=936x898&quality=96&sign=6e39b4a1541e811b03dcc2126323fddc&type=album")
        if checker == 6:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun9-1.userapi.com/impg/l9wbkphkHPHeDw03K45Si7d6AvZb_lVOh6KxHg/wMJrn4zOu3Q.jpg?size=960x1280&quality=96&sign=6129661ce3555bd89c81d7a96d8b7092&type=album")
        if checker == 7:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun9-79.userapi.com/impg/19yzpIGZzNzBd6QbjET4Gs3vJ8eR59fYI8_4Gg/ZZZWh6_CvA8.jpg?size=960x1280&quality=96&sign=38a106d18a87ff18147db52bc6d247fd&type=album")
        if checker == 8:
            await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
            await bot.send_photo(chat_id, photo="https://sun9-31.userapi.com/impg/1jkxuk6plL5QLPJF-nI39M4F7kyc8kbPfAfL6w/61rp1Lrlgw8.jpg?size=960x1280&quality=96&sign=50f67bbb8e323cd802f5f084117b0cc3&type=album")
    elif "донат" in msg.text.lower() or "деньги" in msg.text.lower() or "бабло" in msg.text.lower():
        from random import randint
        checker = randint (1, 3)
        if checker == 1:
            await bot.send_message(chat_id, "Рибят я уже тыщу лет веду паблик и если кто-то хочет мне задонатить то давайте")
        if checker == 2:
            await bot.send_message(chat_id, "Если у вас есть деньги можете задонатить мне :з")
        if checker == 3:
            await bot.send_message(chat_id, "Жду донат")
    elif "кубик" in msg.text.lower():
        await msg.answer_dice(emoji="🎲")
    elif "баскетбол" in msg.text.lower():
        await msg.answer_dice(emoji="🏀")
    elif "казино" in msg.text.lower():
        await msg.answer_dice(emoji="🎰")
    elif "футбол" in msg.text.lower():
        await msg.answer_dice(emoji="⚽️")
    elif "дартс" in msg.text.lower():
        await msg.answer_dice(emoji="🎯")
    elif "боулинг" in msg.text.lower():
        await msg.answer_dice(emoji="🎳")
    elif "myid" in msg.text.lower():
        await msg.answer(f"Твой ID: {msg.from_user.id}")
    elif "бот" in msg.text.lower():
        from random import randint
        checker = randint(1, 5)
        if checker == 1:
            await bot.send_message(chat_id, "Сам ты бот")
        if checker == 2:
            await bot.send_message(chat_id, "За бота сейчас бан получишь")
        if checker == 3:
            await bot.send_message(chat_id, "Кто бот?")
        if checker == 4:
            await bot.send_message(chat_id, "Че кукарекаешь ботяра")
        if checker == 5:
            await bot.send_message(chat_id, "Тише железяка")
    elif "test" in msg.text.lower():
        await bot.send_message(chat_id, "Всё нормально")
    elif "хинкали" in msg.text.lower():
        await bot.send_message(chat_id, "ОБОЖАЮ ХИНКАЛИ😍😍😍")
    elif "или нет" in msg.text.lower():
        from random import randint
        checker = randint(0, 1)
        if checker == 0:
            await bot.send_message(chat_id, "Да")
        if checker == 1:
            await bot.send_message(chat_id, "Нет")
    elif "привет" in msg.text.lower():
        await bot.send_message(chat_id, "Дратути")
    elif "пока" in msg.text.lower():
        await bot.send_message(chat_id, "Покеда")
    elif "камила" in msg.text.lower() or "камилла" in msg.text.lower() or "камиля" in msg.text.lower():
        from random import randint
        checker = randint(1, 3)
        if checker == 1:
            await bot.send_message(chat_id, "Камилла это я")
        if checker == 2:
            await bot.send_message(chat_id, "Кто мя звал?")
        if checker == 3:
            await bot.send_message(chat_id, "I am Kamilla Fortuna")
    elif "камома" in msg.text.lower() or "камом" in msg.text.lower():
        from random import randint
        checker = randint(1, 3)
        if checker == 1:
            await bot.send_message(chat_id, "Я КАМИЛЛА А НЕ КАМОМА")
        if checker == 2:
            await bot.send_message(chat_id, "Ещё раз назовёшь Камомой и я тя забаню")
        if checker == 3:
            await bot.send_message(chat_id, "Лучше зови меня королевой Камиллой")
    elif "cmd" in msg.text.lower():
        await bot.send_message(chat_id, f"<b>Список команд:</b> еда, донат, кубик, баскетбол, казино, футбол, дартс, myid, бот, test, хинкали, или нет, привет, пока, камилла, камома, cmd, секс, оценку, боулинг", parse_mode='html')
    elif "секс" in msg.text.lower():
        from random import randint
        checker = randint(1, 2)
        if checker == 1:
            await bot.send_message(chat_id, "Харам")
        if checker == 2:
            await bot.send_message(chat_id, "Никогда не стала бы заниматься сексом")
    elif "оценку" in msg.text.lower():
        from random import randint
        checker = randint(1, 7)
        if checker == 1:
            await bot.send_message(chat_id, "Оценка говно")
        if checker == 2:
            await bot.send_message(chat_id, "Хрень")
        if checker == 3:
            await bot.send_message(chat_id, "Не очень")
        if checker == 4:
            await bot.send_message(chat_id, "Ну хз")
        if checker == 5:
            await bot.send_message(chat_id, "Сойдёт")
        if checker == 6:
            await bot.send_message(chat_id, "Нормально")
        if checker == 7:
            await bot.send_message(chat_id, "Ахуенна рибят")
    else:
        pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)