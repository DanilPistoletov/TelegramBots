DanilID = 1886347358
banlist = {}

elif "ban" == msg.text.lower():
	if msg.from_user.id == DanilID:
		tempchatID = chat_id
		banID = msg.reply_to_message.from_user.id
		tempbanID = banID
		banlist[tempchatID] = {tempchatID: tempbanID}
		await bot.send_message(chat_id, banlist[tempchatID][tempchatID])
		while tempbanID == banlist[tempchatID][tempchatID]:
                	await bot.ban_chat_member(chat_id, banID)
elif "unban" == msg.text.lower():
	if msg.from_user.id == DanilID:
		tempchatID = chat_id
		del banlist[tempchatID][tempchatID]