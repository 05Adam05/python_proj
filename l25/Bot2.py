import telebot

TOKEN = "412526464:AAGPBU6liOdo8CsMmWJssFR08KPPZpJZaWg"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(regexp="Адам")
def cheker(message):
	bot.send_message(message.chat.id, "STFU")

@bot.message_handler(commands=["start"])
def start_kb(message):
	our_kb = telebot.types.ReplyKeyboardMarkup()
	our_kb.row("+","-")
	our_kb.row("Привет","Здрасте","Пока")


@bot.message_handler(commands=["start"])
def stsrt_kb(message):
	bot.send_message(massage.chat.id, "Введи оператор", reply_markup=our_kb)


if __name__=="__main__":
	bot.polling()