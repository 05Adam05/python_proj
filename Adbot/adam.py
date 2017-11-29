import telebot

TOKEN = "455886429:AAEZs-Yt1PCPx1tlYAc2WWpi_JxhacJ5dnM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(regexp="Привет")
def answer(message):
	bot.send_message(message.chat.id, "Валейкумассалам")

@bot.message_handler(func=lambda message:True)
	print("Я не понял тебя")
def say_smth(message):
	if message.text == "Здрасте":
		bot.send_message(message.chat.id, "Животное, пошел вон!")
	elif message.text == "Саламуалейкум":
		bot.reply_to(message, "Оооооо, братуха")

@bot.message_handler(regexp="Как тебя зовут")
def info(message):
	bot.send_message(message.chat.id, "Меня создал Адам, а зовут меня Черт")

@bot.message_handler(regexp="Пока")
def ans(message):
	bot.send_message(message.chat.id, "Не уходи")



@bot.message_handler(regexp="Адам")
def cheker(message):
	bot.send_message(message.chat.id, "STFU")

@bot.message_handler(commands=["start"])
def start_kb(message):
	b_kb = telebot.types.ReplyKeyboardMarkup()
	b_kb.row("Адам","Как тебя зовут")
	b_kb.row("Привет","Здрасте","Пока")
	bot.send_message(message.chat.id, "Введи оператор", reply_markup=b_kb)


if __name__=="__main__":
	bot.polling() 