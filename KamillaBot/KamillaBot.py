from aiogram import Bot, Dispatcher, executor, types

bot = Bot(token='ТОКЕН')
DanilID = 1886347358
dp = Dispatcher(bot)
banlist = []
gbl = []
mutelist = []
adminlist = []

@dp.message_handler()
async def sms(msg: types.Message):
    chat_id = msg.chat.id
    if " " in msg.text or " " not in msg.text:
        checkID = chat_id, msg.from_user.id
        if checkID in mutelist:
            await bot.delete_message(chat_id, msg.message_id)
        elif msg.from_user.id in gbl:
            pass
        else:
            if "еда" == msg.text.lower() or " еда " in msg.text.lower():
                from random import randint
                checker = randint(1, 10)
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
                if checker == 9:
                    await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
                    await bot.send_photo(chat_id, photo="https://sun9-65.userapi.com/impg/09dXFn6vy4yz-HjqnfQv1QmQDdwxM53RKUVr0w/o35lgUGC27c.jpg?size=960x1280&quality=96&sign=f1590041d411540d2c0cc2a0baa8a976&type=album")
                if checker == 10:
                    await bot.send_message(chat_id, "Мой обед. Ваш в коммы?")
                    await bot.send_photo(chat_id, photo="https://sun9-60.userapi.com/impg/9wGIhhxL2ZrrncLAjo32Hf6NlJyU3_W9IZu7TA/50JDRHWp300.jpg?size=960x1280&quality=96&sign=1511e6181af080c2d6224e8fc7979a93&type=album")
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
            elif "бот" == msg.text.lower() or " бот " in msg.text.lower():
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
            elif "test" == msg.text.lower():
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
            elif "пока " in msg.text.lower() or msg.text.lower() == "пока" or " пока " in msg.text.lower() or " пока" in msg.text.lower():
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
                checker = randint(1, 4)
                if checker == 1:
                    await bot.send_message(chat_id, "Я КАМИЛЛА А НЕ КАМОМА")
                if checker == 2:
                    await bot.send_message(chat_id, "Ещё раз назовёшь Камомой и я тя забаню")
                if checker == 3:
                    await bot.send_message(chat_id, "Лучше зови меня королевой Камиллой")
                if checker == 4:
                    await bot.send_message(chat_id, "Иди в ананас")
            elif "cmd" in msg.text.lower():
                await bot.send_message(chat_id, f"<b>Список команд:</b> еда, донат, кубик, баскетбол, казино, футбол, дартс, myid, бот, test, хинкали, или нет, привет, пока, камилла, камома, cmd, секс, оценку, боулинг, getid, !репорт, грустно, взлом жопы, энергетик, !версия \n<b>Команды для админов:</b> kick, ban, unban", parse_mode='html')
            elif "секс" in msg.text.lower():
                if msg.from_user.id == DanilID:
                    await bot.send_sticker(chat_id, sticker="CAACAgIAAxkBAAEJHdxkcOriqn5V8g2mgEO789WyyX11TwACzgEAAmqXWxUbfUs_BJsa3i8E")
                    await bot.send_message(chat_id, "Конечно, папочка")
                else:
                    from random import randint
                    checker = randint(1, 2)
                    if checker == 1:
                        await bot.send_message(chat_id, "Харам")
                    if checker == 2:
                        await bot.send_message(chat_id, "Никогда не стала бы заниматься сексом")
            elif "оценку" in msg.text.lower():
                from random import randint
                checker = randint(1, 8)
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
                    await bot.send_message(chat_id, "Топова рибят")
                if checker == 8:
                    await bot.send_message(chat_id, "Апупенна")
            elif "лю" in msg.text.lower():
                if msg.from_user.id == DanilID:
                    await bot.send_message(chat_id, "Я типя тожи лю мой хинкалик")
            elif "няша" in msg.text.lower():
                if msg.from_user.id == DanilID:
                    await bot.send_message(chat_id, "Ти")
            elif "kick" in msg.text.lower():
                if msg.from_user.id == DanilID:
                    await bot.kick_chat_member(chat_id, msg.reply_to_message.from_user.id)
            elif "getid" in msg.text.lower():
                await bot.send_message(chat_id, msg.reply_to_message.from_user.id)
            elif "ban" == msg.text.lower() or "бан" == msg.text.lower():
                if msg.from_user.id == DanilID:
                    tempbanID = msg.reply_to_message.from_user.id
                    banID = chat_id, msg.reply_to_message.from_user.id
                    banlist.append(banID)
                    while banID in banlist:
                        await bot.ban_chat_member(chat_id, tempbanID)
            elif "unban" == msg.text.lower() or "разбан" == msg.text.lower():
                if msg.from_user.id == DanilID:
                    banID = chat_id, msg.reply_to_message.from_user.id
                    banlist.remove(banID)
            elif "!репорт" in msg.text.lower():
                await bot.send_message(chat_id, "Сообщение отправлено")
                await bot.send_message(DanilID, ("Имя: " + str(msg.from_user.first_name) + "\nID: " + str(msg.from_user.id) + "\nСообщение: " + str(msg.text)))
            elif msg.text.lower() == "взлом жопы":
                await bot.send_message(chat_id, "В случае расследования какой-либо федеральной структуры или подобного, я не имею никакого отношения к этой группе или к людям в ней, я не знаю, как я здесь оказался, возможно, добавлен третьей стороной, я не поддерживаю никаких действий членов этой группы. Все, что я здесь разместил, является чистой сатирой и будет рассматриваться как таковое в суде. Я не совершал никаких преступлений и являюсь невинным свидетелем.")
            elif "грустно" in msg.text.lower():
                await bot.send_message(chat_id, "не грусти попа не будит расти")
            elif msg.text.lower() == "энергетик" or " энергетик " in msg.text.lower():
                from random import randint
                checker = randint(1, 8)
                if checker == 1:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-31.userapi.com/impg/YOJkLF7mgw4fZ9215YQvawKDu6A8PD9Htn9gEQ/4Wfi2w6Bbmo.jpg?size=960x1280&quality=96&sign=cc4d4f2021ff59fabc1dfd057facc607&type=album")
                if checker == 2:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-30.userapi.com/impg/_Kv_p-dG2hNsOF7vUCLl9O7-vFtRBzFEI-DQkA/4M8yU8TW3OQ.jpg?size=960x1280&quality=96&sign=f9822b59246b7e6e79a4064adca58a30&type=album")
                if checker == 3:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-55.userapi.com/impg/8mlM-WEkJrquNRx3bE8IA_-Ku33iBGladCTXNA/3uhzbnnxbz4.jpg?size=960x1280&quality=96&sign=943c42ba174628c563cc20fdba9ea892&type=album")
                if checker == 4:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-45.userapi.com/impg/YCE2rVmxJlAoCs9hMuyRXoiyzra3_lOjgfGpUA/dmUgAlLhbaQ.jpg?size=960x1280&quality=96&sign=d0c6bce427e58112848f1f36e2da6e3b&type=album")
                if checker == 5:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-12.userapi.com/impg/8a_m_BhlVFpprdgNFBE4PLx6ygHfJ4LNlFiDlg/LxNoICVDNBQ.jpg?size=960x1280&quality=96&sign=81ecfb2dd3606ec8dc8bc41c143520a7&type=album")
                if checker == 6:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-55.userapi.com/impg/kz9oX-dowhsBfITPFRbh2eoc5AlVB4oRcTaOOA/dnrZ5XEncAQ.jpg?size=960x1280&quality=96&sign=2633e4dac2fc5dbb84dbf2eeaa794507&type=album")
                if checker == 7:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-60.userapi.com/impg/AuauINxkBK5YFVHiOC5PH5cSfW6_KwLiAd5T8A/zw6NtLxq2Fk.jpg?size=960x1280&quality=96&sign=2945eb0ca760d2e539c1670b83f95ed5&type=album")
                if checker == 8:
                    await bot.send_message(chat_id, "Пью энергетек как настоящая альтушка а вы что делаити")
                    await bot.send_photo(chat_id, photo="https://sun9-58.userapi.com/impg/OL6E5NRRJUA3oWuvzu9jjeXhu5TetILIiZxzNA/cwaWgzxDgIg.jpg?size=960x1280&quality=96&sign=f4f3b326fb43539ca39d569138875e6f&type=album")
            if "!версия" in msg.text.lower():
                await bot.send_message(chat_id, "Версия 0.7")
            elif "gbladd" in msg.text.lower():
                if msg.from_user.id == DanilID:
                    gbl.append(int(msg.text[7:]))
                    await bot.send_message(chat_id, "Пользователь " + msg.text[7:] + " попадает в ад")
            elif "gbldel" in msg.text.lower():
                if msg.from_user.id == DanilID:
                    gbl.remove(int(msg.text[7:]))
                    await bot.send_message(chat_id, "Пользователь " + msg.text[7:] + " вытащен из ада")
            elif "mute" == msg.text.lower() or "мут" == msg.text.lower():
                if msg.from_user.id == DanilID:
                    muteID = chat_id, msg.reply_to_message.from_user.id
                    mutelist.append(muteID)
            elif "unmute" == msg.text.lower() or "размут" == msg.text.lower():
                if msg.from_user.id == DanilID:
                    muteID = chat_id, msg.reply_to_message.from_user.id
                    mutelist.remove(muteID)
            elif "проверить создателя" == msg.text.lower():
                check = "\"status\": \"creator\""
                owners = str(await bot.get_chat_member(chat_id, msg.from_user.id))
                if check in owners:
                    owner = msg.from_user.id
                    ownerADD = chat_id, msg.from_user.id
                    adminlist.append(ownerADD)
                    await bot.send_message(chat_id, "Создатель установлен: " + owner)
            elif msg.text.lower() == "добавить админа":
                if msg.from_user.id == DanilID:
                    adminaddID = chat_id, msg.reply_to_message.from_user.id
                    adminlist.append(adminaddID)
                    await bot.send_message(chat_id, "Администратор добавлен: " + str(msg.reply_to_message.from_user.id))
            elif msg.text.lower() == "убрать админа":
                if msg.from_user.id == DanilID:
                    admindelID = chat_id, msg.reply_to_message.from_user.id
                    adminlist.remove(admindelID)
                    await bot.send_message(chat_id, "Администратор удалён: " + str(msg.reply_to_message.from_user.id))
            elif msg.text.lower() == "список админов":
                chat_admins = await bot.get_chat_administrators(chat_id)
                await bot.send_message(chat_id, chat_admins)
            else:
                pass

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)