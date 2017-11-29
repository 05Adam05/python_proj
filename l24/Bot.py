import telebot

TOKEN = "412526464:AAGPBU6liOdo8CsMmWJssFR08KPPZpJZaWg"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["Привет"])
def answer(message):
	bot.send_massage(message.chat.id, "Валейкум")

@bot.message_handler(func=lambda message:True)
def say_smth(message):
	if message.text == "Здрасте":
		bot.send_message(message.chat.id, "Животное, пошел вон!")
	elif message.text == "Здровеньке булы":
		bot.reply_to(message, "Оооооо, братуха")


if __name__=="__main__":
	bot.polling()