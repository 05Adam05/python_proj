import telebot

TOKEN = "412526464:AAGPBU6liOdo8CsMmWJssFR08KPPZpJZaWg"

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["Привет"])
def answer(message):
	bot.send_message(message.chat.id, "Привет")

@bot.message_handler(commands=["Как тебя зовут"])
def answer(message):
	bot.send_message(message.chat.id, "Мой создателб Адам и меня зовут Черт")


@bot.message_handler(func=lambda message:True)
def say_smth(message):
	if message.text == "Здрасте":
		bot.send_message(message.chat.id, "Животное, пошел вон!")
	elif message.text == "Здровеньке булы":
		bot.reply_to(message, "Оооооо, братуха")

@bot.message_handler(regexp="Адам")
def cheker(message):
	bot.send_message(message.chat.id, "STFU")





if __name__=="__main__":
	bot.polling()