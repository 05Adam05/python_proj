import telebot

TOKEN = "181530422:AAGTPK6IUBqWraxxKyf8a-PzjSCSCfodUWw"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(regexp="Привет")
def answer(message):
	bot.send_message(message.chat.id, "Валейкумассалам")

# @bot.message_handler(func=lambda message:True)
# def say_smth(message):
# 	if:
# 		pass
# 		bot.send_message(message.chat.id, "Не понимаю")
# 	elif message.text == "Саламуалейкум":
# 		bot.reply_to(message, "Оооооо, братуха")

# @bot.message_handler(regexp="Адам")
# def cheker(message):
# 	bot.send_message(message.chat.id, "STFU")



@bot.message_handler(regexp="Новости")
def answer(message):
	bot.send_message(message.chat.id, "Все новсти в Махачкале вы можете узнать сдесь https://news.yandex.ru/Makhachkala")
@bot.message_handler(commands=["start"])
def start_kb(message):
	our_kb2 = telebot.types.ReplyKeyboardMarkup()
	our_kb2.row("События")
	our_kb2.row("Новости")
	bot.send_message(message.chat.id, "Введи оператор", reply_markup=our_kb2)


if __name__=="__main__":
	bot.polling()