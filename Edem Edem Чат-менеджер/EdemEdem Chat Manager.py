import asyncio
from aiogram import Bot, Dispatcher, types, Router, F
import sqlite3
from datetime import datetime
from random import randint
conn = sqlite3.connect('ПУТЬ ДО БД')
cursor = conn.cursor()
DanilID = 1886347358
botversion = "0.8.1"

bot = Bot(token='ТОКЕН')
dp = Dispatcher()
rt = Router()

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

@dp.message(F.new_chat_members)
async def new_member(message: types.Message):
    if "[User(id=6682084938, is_bot=True, first_name='Edem Edem | Чат-менеджер" in str(message.new_chat_members):
        pass
    else:
        for user in message.new_chat_members:
            await message.reply(f"Тарофчек, {user.full_name}")
            cursor.execute(f"SELECT banlist FROM actions WHERE banlist = {int(user.id)} AND chat_id = {message.chat.id}")
            if cursor.fetchone() is None:
                pass
            else:
                await bot.send_message(message.chat.id, "Пользователь в бане")
                await bot.ban_chat_member(message.chat.id, user.id)

@dp.message(F.left_chat_member)
async def new_member(message: types.Message):
    await message.reply(f"Покя, {message.left_chat_member.full_name}")

@dp.message(F.text)
async def sms(msg: types.Message):
    chat_id = msg.chat.id
    if msg.text == " " or msg.text != " ":
        cursor.execute(f"SELECT * FROM users WHERE user_id = {int(msg.from_user.id)}")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO users(user_id,user_name,user_description,user_sex,user_partner,user_partner_temp,user_partner_date,user_coins,user_partner_points,user_education,job) VALUES('{msg.from_user.id}', '{msg.from_user.full_name}', 'Описание отсутствует', 'Нубик', '-', '-', '-', '0', '0', '0', '0');")
            conn.commit()
        cursor.execute(f"SELECT * FROM chats WHERE chat_id = {int(chat_id)}")
        if cursor.fetchone() is None:
            cursor.execute(f"INSERT INTO chats(chat_id,chat_name,chat_creator_id) VALUES('{chat_id}', '{msg.chat.full_name}', '');")
            conn.commit()
    if msg.text.lower() == "check":
        if "ChatMemberStatus.CREATOR: 'creator'" in str(await bot.get_chat_member(chat_id, msg.from_user.id)):
            await bot.send_message(chat_id, "Создатель установлен")
            cursor.execute(f"UPDATE chats SET chat_creator_id = {msg.from_user.id} WHERE chat_id = {chat_id};")
            conn.commit()
        if "user=User(id=6682084938, is_bot=True, first_name='Edem Edem | Чат-менеджер" in str(await bot.get_chat_administrators(chat_id)):
            await bot.send_message(chat_id, "В случае расследования какой-либо федеральной структуры или подобного, я не имею никакого отношения к этой группе или к людям в ней, я не знаю, как я здесь оказался, возможно, добавлен третьей стороной, я не поддерживаю никаких действий членов этой группы. Все, что я здесь разместил, является чистой сатирой и будет рассматриваться как таковое в суде. Я не совершал никаких преступлений и являюсь невинным свидетелем.")
        else:
            await bot.send_message(chat_id, "Что-то пошло не так")
    elif msg.text.lower() == "кто создатель":
        cursor.execute(f"SELECT chat_creator_id FROM chats WHERE chat_id = '{chat_id}';")
        ownerid = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{ownerid}';")
        ownername = cursor.fetchone()[0]
        await bot.send_message(chat_id, f'<a href=\"tg://user?id=ownerid\">{ownername}</a> является создателем', parse_mode='html')
    elif msg.text.lower() == "+админ":
        cursor.execute(f"SELECT chat_creator_id FROM chats WHERE chat_id = '{chat_id}';")
        ownerid = cursor.fetchone()[0]
        if ownerid != msg.from_user.id:
            await bot.send_message(chat_id, "Только создатель может назначать администраторов")
        else:
            cursor.execute(f"SELECT adminlist FROM actions WHERE adminlist = {int(msg.reply_to_message.from_user.id)} AND chat_id = {chat_id}")
            if cursor.fetchone() is None:
                cursor.execute(f"INSERT INTO actions VALUES({chat_id}, {msg.reply_to_message.from_user.id}, \"-\", \"-\");")
                conn.commit()
                await bot.send_message(chat_id, "Админ назначен")
            else:
                await bot.send_message(chat_id, "Этот пользователь уже есть в списке администраторов")
    elif msg.text.lower() == "-админ":
        cursor.execute(f"SELECT chat_creator_id FROM chats WHERE chat_id = '{chat_id}';")
        ownerid = cursor.fetchone()[0]
        if ownerid != msg.from_user.id:
            await bot.send_message(chat_id, "Только создатель может разжаловать администраторов")
        else:
            cursor.execute(f"SELECT adminlist FROM actions WHERE adminlist = {int(msg.reply_to_message.from_user.id)} AND chat_id = {chat_id}")
            if cursor.fetchone() is None:
                await bot.send_message(chat_id, "Пользователь не является администратором")
            else:
                cursor.execute(f"DELETE FROM actions WHERE chat_id = {chat_id} AND adminlist={msg.reply_to_message.from_user.id}")
                conn.commit()
                await bot.send_message(chat_id, "Администратор разжалован")
    elif msg.text.lower()[:11] == "отпердолить":
        if "." in msg.text or "/" in msg.text:
            await bot.send_message(chat_id, "Нельзя использовать точки и слэш")
        else:
            cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.from_user.id}';")
            oneid = msg.from_user.id
            twoid = msg.reply_to_message.from_user.id
            oneuser = cursor.fetchone()[0]
            try:
                cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                twouser = cursor.fetchone()[0]
            except:
                twouser = msg.reply_to_message.from_user.id
            if len(msg.text) < 13:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> отпердолил <a href=\"tg://user?id={twoid}\">{twouser}</a>", parse_mode='html')
            else:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> отпердолил <a href=\"tg://user?id={twoid}\">{twouser}</a> со словами: \"{msg.text[12:]}\"", parse_mode='html')
    elif msg.text.lower()[:6] == "геншин":
        if "." in msg.text or "/" in msg.text:
            await bot.send_message(chat_id, "Нельзя использовать точки и слэш")
        else:
            cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.from_user.id}';")
            oneid = msg.from_user.id
            twoid = msg.reply_to_message.from_user.id
            oneuser = cursor.fetchone()[0]
            try:
                cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                twouser = cursor.fetchone()[0]
            except:
                twouser = msg.reply_to_message.from_user.id
            if len(msg.text) < 8:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> заставил играть в Genshin Impact <a href=\"tg://user?id={twoid}\">{twouser}</a>", parse_mode='html')
            else:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> заставил играть в Genshin Impact <a href=\"tg://user?id={twoid}\">{twouser}</a> со словами: \"{msg.text[7:]}\"", parse_mode='html')
    elif msg.text.lower()[:4] == "ник ":
        if len(msg.text.lower()) > 53:
            await bot.send_message(chat_id, "Ник ограничен 50 символами")
        else:
            if "." in msg.text or "/" in msg.text or ">" in msg.text or "<" in msg.text:
                await bot.send_message(chat_id, "В указании ника нельзя использовать некоторые символы")
            else:
                cursor.execute(f"UPDATE users SET user_name='{msg.text[4:]}' WHERE user_id='{msg.from_user.id}';")
                conn.commit()
                await bot.send_message(chat_id, "Ник обновлён")
    elif msg.text.lower() == "профиль":
        user_id = msg.from_user.id
        cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.from_user.id}';")
        nickname = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_description FROM users WHERE user_id = '{msg.from_user.id}';")
        description = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_sex FROM users WHERE user_id = '{msg.from_user.id}';")
        sex = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_partner FROM users WHERE user_id = '{msg.from_user.id}';")
        marriage_check = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_coins FROM users WHERE user_id = '{msg.from_user.id}';")
        coins = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_education FROM users WHERE user_id={msg.from_user.id}")
        education = cursor.fetchone()[0]
        if education == 0:
            education = "Школьник"
        elif education == 1:
            education = "Бакалавр"
        elif education == 2:
            education = "Кандидат наук"
        elif education == 3:
            education = "Доктор наук"
        cursor.execute(f"SELECT job FROM users WHERE user_id={msg.from_user.id}")
        job = cursor.fetchone()[0]
        if job == 0:
            job = "Безработный РНН-господин"
        elif job == 1:
            job = "Помощник говночиста"
        elif job == 2:
            job = "Говночист"
        elif job == 3:
            job = "Скибиди туалет"
        elif job == 4:
            job = "Король туалета"
        if marriage_check == "-":
            await bot.send_message(chat_id, f"<b>Профиль пользователя <a href='tg://user?id={user_id}'>{nickname}</a></b>\n<b>Описание: </b> {description}\n<b>Пол: </b> {sex}\n<b>Уровень образования: </b>{education}\n<b>Работа: </b>{job}\n<b>Брак: </b>отсутствует\n<b>Едемкоины:</b> {coins}", parse_mode='html')
        else:
            cursor.execute(f"SELECT user_partner FROM users WHERE user_id = '{msg.from_user.id}';")
            partner = cursor.fetchone()[0]
            cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{partner}';")
            partner_nickname = cursor.fetchone()[0]
            cursor.execute(f"SELECT user_partner_date FROM users WHERE user_id = '{msg.from_user.id}';")
            partner_date = cursor.fetchone()[0]
            cursor.execute(f"SELECT user_partner_points FROM users WHERE user_id = '{msg.from_user.id}';")
            partner_points = int(cursor.fetchone()[0])
            partner_status = "Отсутствует"
            if partner_points < 100:
                partner_status = "Любовь в чате [1/5]"
            elif 100 < partner_points <= 1000:
                partner_status = "Любовники [2/5]"
            elif partner_points > 1000 >= partner_points:
                partner_status = "Парочка [3/5]"
            elif 1000 < partner_points <= 10000:
                partner_status = "Каблуки [4/5]"
            elif partner_points > 10000:
                partner_status = "Любовь навсегда [5/5]"
            datecalc = datetime.today() - datetime.strptime(partner_date, "%Y-%m-%d %H:%M:%S.%f")
            await bot.send_message(chat_id, f"<b>Профиль пользователя <a href='tg://user?id={user_id}'>{nickname}</a></b>\n<b>Описание: </b> {description}\n<b>Пол: </b> {sex}\n<b>Уровень образования: </b>{education}\n<b>Работа: </b>{job}\n<b>Брак: </b><a href='tg://user?id={partner}'>{partner_nickname}</a>\n<b>Количество дней в браке: </b>{datecalc.days} \n<b>Едемкоины:</b> {coins}\n<b>Уровень брака:</b> {partner_status}\n<b>Очки брака:</b> {partner_points}", parse_mode='html')
    elif msg.text.lower()[:4] == "пол ":
        if len(msg.text.lower()) > 33:
            await bot.send_message(chat_id, "Пол ограничен 30 символами")
        else:
            if "." in msg.text or "/" in msg.text or ">" in msg.text or "<" in msg.text:
                await bot.send_message(chat_id, "В указании пола нельзя использовать некоторые символы")
            else:
                cursor.execute(f"UPDATE users SET user_sex='{msg.text[4:]}' WHERE user_id='{msg.from_user.id}';")
                conn.commit()
                await bot.send_message(chat_id, "Пол обновлён")
    elif msg.text.lower()[:9] == "описание ":
        if len(msg.text.lower()) > 208:
            await bot.send_message(chat_id, "Описание ограничено 200 символами")
        else:
            if "." in msg.text or "/" in msg.text or ">" in msg.text or "<" in msg.text:
                await bot.send_message(chat_id, "В описании нельзя использовать некоторые символы")
            else:
                cursor.execute(f"UPDATE users SET user_description='{msg.text[9:]}' WHERE user_id='{msg.from_user.id}';")
                conn.commit()
                await bot.send_message(chat_id, "Описание обновлено")
    elif msg.text.lower() == "version":
        await bot.send_message(chat_id, botversion)
    elif msg.text.lower() == "id":
        await bot.send_message(chat_id, str(msg.reply_to_message.from_user.id))
    elif msg.text.lower() == "myid":
        await bot.send_message(chat_id, str(msg.from_user.id))
    elif msg.text.lower()[:7] == "связать":
        if "." in msg.text or "/" in msg.text:
            await bot.send_message(chat_id, "Нельзя использовать точки и слэш")
        else:
            cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.from_user.id}';")
            oneid = msg.from_user.id
            twoid = msg.reply_to_message.from_user.id
            oneuser = cursor.fetchone()[0]
            try:
                cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                twouser = cursor.fetchone()[0]
            except:
                twouser = msg.reply_to_message.from_user.id
            if len(msg.text) < 9:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> связал <a href=\"tg://user?id={twoid}\">{twouser}</a>", parse_mode='html')
            else:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> связал <a href=\"tg://user?id={twoid}\">{twouser}</a> со словами: \"{msg.text[8:]}\"", parse_mode='html')
    elif msg.text.lower() == "брак запрос":
        if msg.reply_to_message.from_user.id == msg.from_user.id:
            await bot.send_message(chat_id, "Нельзя предложить брак самому себе, хиккан")
        else:
            try:
                if msg.reply_to_message.from_user.id is None:
                    pass
            except:
                await bot.send_message(chat_id, "Для отправки запроса нужно ответить на сообщение")
            else:
                cursor.execute(f"SELECT user_partner FROM users WHERE user_id = '{msg.from_user.id}';")
                marriage = cursor.fetchone()[0]
                if marriage != "-":
                    await bot.send_message(chat_id, "Вы уже состоите в браке")
                else:
                    cursor.execute(f"SELECT user_partner FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                    marriage = cursor.fetchone()[0]
                    if marriage != "-":
                        await bot.send_message(chat_id, "Пользователь уже состоит в браке")
                    else:
                        cursor.execute(f"SELECT user_partner_temp FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                        marriage = cursor.fetchone()[0]
                        if marriage != "-":
                            await bot.send_message(chat_id, f"Пользователю уже предложил брак <a href=\"tg://user?id={marriage}\">пользователь</a>", parse_mode='html')
                        else:
                            cursor.execute(f"UPDATE users SET user_partner_temp='{msg.from_user.id}' WHERE user_id='{msg.reply_to_message.from_user.id}';")
                            conn.commit()
                            await bot.send_message(chat_id, f"Вы предложили брак <a href=\"tg://user?id={msg.reply_to_message.from_user.id}\">пользователю</a>", parse_mode='html')
    elif msg.text.lower() == "брак принять":
        cursor.execute(f"SELECT user_partner_temp FROM users WHERE user_id = '{msg.from_user.id}';")
        marriage = cursor.fetchone()[0]
        if marriage == "-":
            await bot.send_message(chat_id, "У вас нет активных предложений брака")
        else:
            cursor.execute(f"SELECT user_partner FROM users WHERE user_id = '{marriage}';")
            marriage1 = cursor.fetchone()[0]
            if marriage1 != "-":
                await bot.send_message(chat_id, "Пользователь уже состоит в браке")
                cursor.execute(f"UPDATE users SET user_partner_temp='-' WHERE user_id='{msg.from_user.id}'")
                conn.commit()
            else:
                cursor.execute(f"UPDATE users SET user_partner='{marriage}' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_partner_temp='-' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_partner='{msg.from_user.id}' WHERE user_id='{marriage}'")
                cursor.execute(f"UPDATE users SET user_partner_date='{datetime.today()}' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_partner_date='{datetime.today()}' WHERE user_id='{marriage}'")
                conn.commit()
                await bot.send_message(chat_id, "Вы приняли брак")
    elif msg.text.lower() == "брак отказать":
        cursor.execute(f"SELECT user_partner_temp FROM users WHERE user_id = '{msg.from_user.id}';")
        marriage = cursor.fetchone()[0]
        if marriage == "-":
            await bot.send_message(chat_id, "У вас нет активных предложений брака")
        else:
            cursor.execute(f"UPDATE users SET user_partner_temp='-' WHERE user_id='{msg.from_user.id}';")
            conn.commit()
            await bot.send_message(chat_id, "Вы отказались от брака")
    elif msg.text.lower()[:11] == "брак развод":
        cursor.execute(f"SELECT user_partner FROM users WHERE user_id = '{msg.from_user.id}';")
        partner_check = cursor.fetchone()[0]
        if partner_check != "-":
            if msg.text.lower() != "брак развод тнн":
                await bot.send_message(chat_id, "Для подтверждения развода напишите \"брак развод тнн\"")
            elif msg.text.lower() == "брак развод тнн":
                cursor.execute(f"SELECT user_partner FROM users WHERE user_id = '{msg.from_user.id}';")
                partner = cursor.fetchone()[0]
                cursor.execute(f"UPDATE users SET user_partner='-' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_partner='-' WHERE user_id='{partner}'")
                cursor.execute(f"UPDATE users SET user_partner_date='-' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_partner_date='-' WHERE user_id='{partner}'")
                cursor.execute(f"UPDATE users SET user_partner_points='0' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_partner_points='0' WHERE user_id='{partner}'")
                conn.commit()
                await bot.send_message(chat_id, "Вы развелись, поздравляю")
        else:
            await bot.send_message(chat_id, "Вы не состоите в браке")
    elif msg.text.lower()[:10] == "поцеловать":
        if "." in msg.text or "/" in msg.text:
            await bot.send_message(chat_id, "Нельзя использовать точки и слэш")
        else:
            cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.from_user.id}';")
            oneid = msg.from_user.id
            twoid = msg.reply_to_message.from_user.id
            oneuser = cursor.fetchone()[0]
            try:
                cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                twouser = cursor.fetchone()[0]
            except:
                twouser = msg.reply_to_message.from_user.id
            if len(msg.text) < 12:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> поцеловал <a href=\"tg://user?id={twoid}\">{twouser}</a>", parse_mode='html')
            else:
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> поцеловал <a href=\"tg://user?id={twoid}\">{twouser}</a> со словами: \"{msg.text[11:]}\"", parse_mode='html')
    elif msg.text.lower()[:2] == "рп":
        if "." in msg.text or "/" in msg.text:
            await bot.send_message(chat_id, "Нельзя использовать точки и слэш")
        else:
            try:
                cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.from_user.id}';")
                oneid = msg.from_user.id
                twoid = msg.reply_to_message.from_user.id
                oneuser = cursor.fetchone()[0]
                try:
                    cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                    twouser = cursor.fetchone()[0]
                except:
                    twouser = msg.reply_to_message.from_user.id
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> {msg.text[3:]} <a href=\"tg://user?id={twoid}\">{twouser}</a>", parse_mode='html')
            except:
                cursor.execute(f"SELECT user_name FROM users WHERE user_id = '{msg.from_user.id}';")
                oneid = msg.from_user.id
                oneuser = cursor.fetchone()[0]
                await bot.send_message(chat_id, f"<a href=\"tg://user?id={oneid}\">{oneuser}</a> {msg.text[3:]}", parse_mode='html')
    elif msg.text.lower()[:6] == "report":
        report = f"Сообщение: {msg.text}\nID пользователя: {msg.from_user.id}\nНик пользователя: {msg.from_user.full_name}"
        await bot.send_message(chat_id, "Сообщение разработчику отправлено")
        await bot.send_message(DanilID, report)
    elif msg.text.lower()[:6] == "казино":
        if msg.text.lower() == "казино":
            await bot.send_message(chat_id, "Нужно ввести ставку")
        elif msg.text.lower() == "казино все" or msg.text.lower() == "казино всё":
            cursor.execute(f"SELECT user_coins FROM users WHERE user_id = '{msg.from_user.id}';")
            coins = int(cursor.fetchone()[0])
            if coins == 0:
                await bot.send_message(chat_id, "Нельзя играть при нулевом балансе")
            else:
                number = randint(1, 100)
                if number < 70:
                    await bot.send_message(chat_id, f"Вы проиграли {coins} едемкоинов")
                    coins = 0
                    cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                    conn.commit()
                elif number > 69 and number != 100:
                    coins *= 3
                    await bot.send_message(chat_id, f"Вы выиграли {coins} едемкоинов")
                    cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                    conn.commit()
                elif number == 100:
                    coins *= 10
                    await bot.send_message(chat_id, f"У вас джекпот. Вы выиграли {coins} едемкоинов")
                    cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                    conn.commit()
        else:
            cursor.execute(f"SELECT user_coins FROM users WHERE user_id = '{msg.from_user.id}';")
            coins = int(cursor.fetchone()[0])
            bet = msg.text[7:]
            check = "1"
            try:
                bet = int(bet)
            except:
                await bot.send_message(chat_id, "Введённая ставка не является числом")
                check = "0"
            if check == "1":
                if bet > coins:
                    await bot.send_message(chat_id, "Недостаточно едемкоинов")
                if bet <= coins:
                    number = randint(1, 100)
                    if number < 70:
                        await bot.send_message(chat_id, f"Вы проиграли {bet} едемкоинов")
                        coins -= bet
                        cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                        conn.commit()
                    elif number > 69 and number != 100:
                        bet *= 3
                        await bot.send_message(chat_id, f"Вы выиграли {bet} едемкоинов")
                        coins += bet
                        cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                        conn.commit()
                    elif number == 100:
                        bet *= 10
                        await bot.send_message(chat_id, f"У вас джекпот. Вы выиграли {bet} едемкоинов")
                        coins += bet
                        cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                        conn.commit()
    elif msg.text.lower()[:6] == "!коины":
        if msg.from_user.id == DanilID:
            coins = msg.text[7:]
            cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.reply_to_message.from_user.id}'")
            conn.commit()
            await bot.send_message(chat_id, "Количество монет установлено")
        else:
            pass
    elif msg.text.lower() == "едемкоины":
        cursor.execute(f"SELECT user_coins FROM users WHERE user_id = '{msg.from_user.id}';")
        coins = cursor.fetchone()[0]
        await bot.send_message(chat_id, f"Количество ваших едемкоинов: {coins}")
    elif msg.text.lower()[:18] == "едемкоины передать":
        give = msg.text[19:]
        check = "1"
        try:
            give = int(give)
        except:
            check = "0"
        if check == "1":
            cursor.execute(f"SELECT user_coins FROM users WHERE user_id = '{msg.from_user.id}';")
            coins = int(cursor.fetchone()[0])
            if give > coins:
                await bot.send_message(chat_id, "Недостаточно едемкоинов")
            elif give <= coins:
                try:
                    cursor.execute(f"SELECT user_coins FROM users WHERE user_id = '{msg.reply_to_message.from_user.id}';")
                    coins2 = int(cursor.fetchone()[0])
                    coins2 += give
                    coins -= give
                    cursor.execute(f"UPDATE users SET user_coins='{coins2}' WHERE user_id='{msg.reply_to_message.from_user.id}'")
                    cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                    conn.commit()
                    await bot.send_message(chat_id, f"Вы успешно передали {give} едемкоинов")
                except:
                    await bot.send_message(chat_id, "Нужно переслать сообщение пользователя для передачи едемкоинов")
        else:
            await bot.send_message(chat_id, "Введённое количество не является числом")
    elif msg.text.lower()[:9] == "!рассылка":
        if msg.from_user.id == DanilID:
            text = msg.text[10:]
            cursor.execute(f"SELECT chat_id FROM chats;")
            chatids = str(cursor.fetchall())
            chatids = chatids.replace('(', '')
            chatids = chatids.replace(')', '')
            chatids = chatids.replace('\'', '')
            chatids = chatids.replace('[', '')
            chatids = chatids.replace(']', '')
            chatids = chatids.replace(',', '')
            chatids = list(chatids.split(' '))
            for i in chatids:
                await bot.send_message(i, text)
    elif msg.text.lower()[:5] == "!фото":
        if msg.from_user.id == DanilID:
            link = msg.text[6:]
            cursor.execute(f"SELECT chat_id FROM chats;")
            chatids = str(cursor.fetchall())
            chatids = chatids.replace('(', '')
            chatids = chatids.replace(')', '')
            chatids = chatids.replace('\'', '')
            chatids = chatids.replace('[', '')
            chatids = chatids.replace(']', '')
            chatids = chatids.replace(',', '')
            chatids = list(chatids.split(' '))
            for i in chatids:
                await bot.send_photo(i, photo=f"{link}")
    elif msg.text.lower() == "бот":
        await bot.send_message(chat_id, "Я тутачки")
    elif msg.text.lower() == "кубик":
        await msg.answer_dice(emoji="🎲")
    elif msg.text.lower() == "баскетбол":
        await msg.answer_dice(emoji="🏀")
    elif msg.text.lower() == "777":
        await msg.answer_dice(emoji="🎰")
    elif msg.text.lower() == "футбол":
        await msg.answer_dice(emoji="⚽️")
    elif msg.text.lower() == "дартс":
        await msg.answer_dice(emoji="🎯")
    elif msg.text.lower() == "боулинг":
        await msg.answer_dice(emoji="🎳")
    elif msg.text.lower() == "кик":
        admincheck = 1
        ownercheck = 1
        isadmin = 1
        cursor.execute(f"SELECT adminlist FROM actions WHERE adminlist = {int(msg.reply_to_message.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            isadmin = 0
        cursor.execute(f"SELECT adminlist FROM actions WHERE adminlist = {int(msg.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            admincheck = 0
        cursor.execute(f"SELECT chat_creator_id FROM chats WHERE chat_creator_id = {int(msg.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            ownercheck = 0
        if ownercheck == 0 and admincheck == 0:
            await bot.send_message(chat_id, "Кикать может только администратор либо создатель")
        elif isadmin == 1:
            await bot.send_message(chat_id, "Нельзя исключать администраторов")
        elif ownercheck == 1 or admincheck == 1:
            try:
                await bot.ban_chat_member(chat_id, msg.reply_to_message.from_user.id)
                await bot.send_message(chat_id, "Пользователь кикнут")
            except:
                await bot.send_message(chat_id, "Не удалось исключить пользователя")
    elif msg.text.lower() == "бан":
        admincheck = 1
        ownercheck = 1
        isadmin = 1
        isban = 1
        cursor.execute(f"SELECT adminlist FROM actions WHERE adminlist = {int(msg.reply_to_message.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            isadmin = 0
        cursor.execute(f"SELECT adminlist FROM actions WHERE adminlist = {int(msg.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            admincheck = 0
        cursor.execute(f"SELECT chat_creator_id FROM chats WHERE chat_creator_id = {int(msg.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            ownercheck = 0
        cursor.execute(f"SELECT banlist FROM actions WHERE banlist = {int(msg.reply_to_message.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            isban = 0
        if ownercheck == 0 and admincheck == 0:
            await bot.send_message(chat_id, "Банить может только администратор либо создатель")
        elif isban == 1:
            await bot.send_message(chat_id, "Пользователь уже в бане")
        elif isadmin == 1:
            await bot.send_message(chat_id, "Нельзя банить администраторов")
        elif ownercheck == 1 or admincheck == 1:
            try:
                cursor.execute(f"INSERT INTO actions(chat_id,banlist,adminlist,mutelist) VALUES({chat_id}, {msg.reply_to_message.from_user.id}, \"-\", \"-\");")
                conn.commit()
                await bot.ban_chat_member(chat_id, msg.reply_to_message.from_user.id)
                await bot.send_message(chat_id, "Пользователь забанен")
            except:
                await bot.send_message(chat_id, "Не удалось исключить пользователя")
    elif msg.text.lower() == "разбан":
        admincheck = 1
        ownercheck = 1
        isban = 1
        cursor.execute(f"SELECT adminlist FROM actions WHERE adminlist = {int(msg.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            admincheck = 0
        cursor.execute(f"SELECT chat_creator_id FROM chats WHERE chat_creator_id = {int(msg.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            ownercheck = 0
        cursor.execute(f"SELECT banlist FROM actions WHERE banlist = {int(msg.reply_to_message.from_user.id)} AND chat_id = {chat_id}")
        if cursor.fetchone() is None:
            isban = 0
        if admincheck == 0 and ownercheck == 0:
            await bot.send_message(chat_id, "Банить может только администратор либо создатель")
        elif isban == 0:
            await bot.send_message(chat_id, "Пользователь не в бане")
        elif ownercheck == 1 or admincheck == 1:
            cursor.execute(f"DELETE FROM actions WHERE chat_id = {chat_id} AND banlist={msg.reply_to_message.from_user.id}")
            conn.commit()
            await bot.send_message(chat_id, "Пользователь разбанен")
    elif msg.text.lower() == "список админов":
        admincheck = 1
        cursor.execute(f"SELECT chat_creator_id FROM chats WHERE chat_id={chat_id}")
        owner = cursor.fetchone()[0]
        cursor.execute(f"SELECT adminlist FROM actions WHERE chat_id = {chat_id} and adminlist != '-';")
        if cursor.fetchone() is None:
            await bot.send_message(chat_id, f"<a href=\"tg://user?id={owner}\">Создатель</a>", parse_mode='html')
            admincheck = 0
        if admincheck != 0:
            cursor.execute(f"SELECT adminlist FROM actions WHERE chat_id = {chat_id} and adminlist != '-';")
            adminlist = str(cursor.fetchall())
            adminmsg = f"<a href=\"tg://user?id={owner}\">Создатель</a>\n"
            adminlist = adminlist.replace('(', '')
            adminlist = adminlist.replace(')', '')
            adminlist = adminlist.replace('\'', '')
            adminlist = adminlist.replace('[', '')
            adminlist = adminlist.replace(']', '')
            adminlist = adminlist.replace(',', '')
            adminlist = list(adminlist.split(' '))
            for i in adminlist:
                adminmsg += f"<a href=\"tg://user?id={i}\">Администратор</a>\n"
            await bot.send_message(chat_id, adminmsg, parse_mode='html')
    elif msg.text.lower() == "едемкоины топ":
        cursor.execute(f"SELECT user_id,user_name,user_coins FROM users ORDER BY user_coins * 1 DESC LIMIT 5")
        top = cursor.fetchall()
        await bot.send_message(chat_id, f"<b>Топ пять обладателей едемкоинов:</b>\n1. {top[0][1]} - {top[0][2]} едемкоинов\n2. {top[1][1]} - {top[1][2]} едемкоинов\n3. {top[2][1]} - {top[2][2]} едемкоинов\n4. {top[3][1]} - {top[3][2]} едемкоинов\n5. {top[4][1]} - {top[4][2]} едемкоинов", parse_mode='html')
    elif " или нет" in msg.text.lower():
        check = randint(1,2)
        if check == 1:
            await bot.send_message(chat_id, "Да", reply_to_message_id=msg.message_id)
        if check == 2:
            await bot.send_message(chat_id, "Нет", reply_to_message_id=msg.message_id)
    elif msg.text.lower() == "помощь" or msg.text.lower() == "help":
        await bot.send_message(chat_id, "Полный список команд расположен в описании профиля бота")
    elif msg.text.lower()[:4] == "!смс":
        if msg.from_user.id == DanilID:
            sms = msg.text[5:]
            sms = sms.split(",")
            await bot.send_message(chat_id=sms[0], text=sms[1])
    elif msg.text.lower() == "образование":
        cursor.execute(f"SELECT user_education FROM users WHERE user_id={msg.from_user.id}")
        education = cursor.fetchone()[0]
        if education == 0:
            await bot.send_message(chat_id, "Уровень образования: Школьник")
        if education == 1:
            await bot.send_message(chat_id, "Уровень образования: Бакалавр")
        if education == 2:
            await bot.send_message(chat_id, "Уровень образования: Кандидат наук")
        if education == 3:
            await bot.send_message(chat_id, "Уровень образования: Доктор наук")
    elif msg.text.lower() == "образование+":
        cursor.execute(f"SELECT user_education FROM users WHERE user_id={msg.from_user.id}")
        education = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_coins FROM users WHERE user_id={msg.from_user.id}")
        coins = int(cursor.fetchone()[0])
        if education == 0:
            cursor.execute(f"UPDATE users SET user_education='1' WHERE user_id='{msg.from_user.id}'")
            conn.commit()
            await bot.send_message(chat_id, "Уровень образования повышен")
        elif education == 1:
            if coins >= 10000:
                coins -= 10000
                cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_education='2' WHERE user_id='{msg.from_user.id}'")
                conn.commit()
                await bot.send_message(chat_id, "Вы повысили уровень образования за 10000 едемкоинов")
            elif coins < 10000:
                await bot.send_message(chat_id, "Для повышения уровня образования нужно 10000 едемкоинов")
        elif education == 2:
            if coins >= 50000:
                coins -= 50000
                cursor.execute(f"UPDATE users SET user_coins='{coins}' WHERE user_id='{msg.from_user.id}'")
                cursor.execute(f"UPDATE users SET user_education='3' WHERE user_id='{msg.from_user.id}'")
                conn.commit()
                await bot.send_message(chat_id, "Вы повысили уровень образования за 50000 едемкоинов")
            elif coins < 50000:
                await bot.send_message(chat_id, "Для повышения уровня образования нужно 50000 едемкоинов")
        elif education == 3:
            await bot.send_message(chat_id, "Вы достигли максимального уровня образования")
    elif msg.text.lower() == "работа":
        cursor.execute(f"SELECT job FROM users WHERE user_id={msg.from_user.id}")
        job = cursor.fetchone()[0]
        if job == 0:
            await bot.send_message(chat_id, "Вы безработный РНН-господин")
        elif job == 1:
            await bot.send_message(chat_id, "Вы помощник говночиста")
        elif job == 2:
            await bot.send_message(chat_id, "Вы говночист")
        elif job == 3:
            await bot.send_message(chat_id, "Вы скибиди туалет")
        elif job == 4:
            await bot.send_message(chat_id, "Вы король туалета")
    elif msg.text.lower() == "работа+":
        cursor.execute(f"SELECT job FROM users WHERE user_id={msg.from_user.id}")
        job = cursor.fetchone()[0]
        cursor.execute(f"SELECT user_education FROM users WHERE user_id={msg.from_user.id}")
        education = cursor.fetchone()[0]
        if job == 0:
            await bot.send_message(chat_id, "Вы устроились на работу")
            cursor.execute(f"UPDATE users SET job='1' WHERE user_id='{msg.from_user.id}'")
            conn.commit()
        if job == 1:
            if education >= 1:
                await bot.send_message(chat_id, "Вы повышены")
                cursor.execute(f"UPDATE users SET job='2' WHERE user_id='{msg.from_user.id}'")
                conn.commit()
            else:
                await bot.send_message(chat_id, "Недостаточный уровень образования")
        if job == 2:
            if education >= 2:
                await bot.send_message(chat_id, "Вы повышены")
                cursor.execute(f"UPDATE users SET job='3' WHERE user_id='{msg.from_user.id}'")
                conn.commit()
            else:
                await bot.send_message(chat_id, "Недостаточный уровень образования")
        if job == 3:
            if education == 3:
                await bot.send_message(chat_id, "Вы повышены")
                cursor.execute(f"UPDATE users SET job='4' WHERE user_id='{msg.from_user.id}'")
                conn.commit()
            else:
                await bot.send_message(chat_id, "Недостаточный уровень образования")
        if job == 4:
            await bot.send_message(chat_id, "Достигнут максимальный уровень работы")
    elif msg.text.lower() == "работать" or msg.text.lower() == "завод":
        cursor.execute(f"SELECT job FROM users WHERE user_id={msg.from_user.id}")
        job = cursor.fetchone()[0]
        jobtimenone = 0
        jobtimegood = 0
        pay = randint(1, 50)
        constanta = 1
        if job == 0:
            await bot.send_message(chat_id, "Вы безработный")
        else:
            cursor.execute(f"SELECT job_time FROM users WHERE user_id='{msg.from_user.id}'")
            if cursor.fetchone() is None:
                jobtimenone = 1
            else:
                try:
                    cursor.execute(f"SELECT job_time FROM users WHERE user_id={msg.from_user.id}")
                    job_time = cursor.fetchone()[0]
                    datecalc = datetime.today() - datetime.strptime(job_time, "%Y-%m-%d %H:%M:%S.%f")
                    if datecalc.seconds > 18000:
                        jobtimegood = 1
                except:
                    jobtimenone = 1
            if jobtimenone == 1 or jobtimegood == 1:
                if job == 1:
                    constanta = 1
                elif job == 2:
                    constanta = 3
                elif job == 3:
                    constanta = 5
                elif job == 4:
                    constanta = 7
                pay = pay * constanta
                await bot.send_message(chat_id, f"Вы заработали {pay} едемкоинов")
                cursor.execute(f"SELECT user_coins FROM users WHERE user_id={msg.from_user.id}")
                coins = int(cursor.fetchone()[0])
                coins += pay
                cursor.execute(f"UPDATE users SET user_coins={coins} WHERE user_id='{msg.from_user.id}'")
                conn.commit()
                jobtime = datetime.today()
                cursor.execute(f"UPDATE users SET job_time='{jobtime}' WHERE user_id='{msg.from_user.id}'")
                conn.commit()
            elif jobtimegood == 0 and jobtimenone == 0:
                alltime = 18000 - datecalc.seconds
                hours = int(alltime / 3600)
                minutes = int((alltime - hours*3600)/60)
                seconds = alltime - hours*3600 - minutes*60
                await bot.send_message(chat_id, f"Работать можно один раз в 5 часов. Осталось {hours} часов, {minutes} минут и {seconds} секунд.")


if __name__ == '__main__':
    asyncio.run(main())