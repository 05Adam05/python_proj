import telebot
import datetime
v_1.0

TOKEN = "455886429:AAEZs-Yt1PCPx1tlYAc2WWpi_JxhacJ5dnM"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(regexp="Новости")
def answer(message):
	bot.send_message(message.chat.id, "Все новсти в Махачкале вы можете узнать сдесь https://news.yandex.ru/Makhachkala")

# @bot.message_handler(regexp="Событие")
# def answer(message):
# 	if datetime.date.today == 2017-12-18:
# 		bot.send_message(message.chat.id, "Урааааааааааааа")

@bot.message_handler(commands=["start"])
def start_kb(message):
	b_kb = telebot.types.ReplyKeyboardMarkup()
	b_kb.row("Новости")
	b_kb.row("Событие")
	bot.send_message(message.chat.id, "Введи оператор", reply_markup=b_kb)
	bot.send_message(message.chat.id, "Первое слово пиши с большой буквы")
	bot.send_message(message.chat.id, datetime.date.today())

@bot.message_handler(regexp="Адам")
def cheker(message):
	bot.send_message(message.chat.id, "Адам мой создатель")

@bot.message_handler(regexp="Привет")
def answer(message):
	bot.send_message(message.chat.id, "Салам Алейкум")

@bot.message_handler(regexp="Дратути")
def answer(message):
	bot.send_message(message.chat.id, "Салам Алейкум")

@bot.message_handler(regexp="Здрасте")
def answer(message):
	bot.send_message(message.chat.id, "Салам Алейкум")

@bot.message_handler(regexp="Здравствуйте")
def answer(message):
	bot.send_message(message.chat.id, "Салам Алейкум")

@bot.message_handler(regexp="Салют")
def answer(message):
	bot.send_message(message.chat.id, "Салам Алейкум")

@bot.message_handler(regexp="Как тебя зовут")
def answer(message):
	bot.send_message(message.chat.id, "Меня создал Адам, а меня зовут Проэкт")

@bot.message_handler(regexp="Ты кто")
def answer(message):
	bot.send_message(message.chat.id, "Я бот")

@bot.message_handler(regexp="Как дела")
def answer(message):
	bot.send_message(message.chat.id, "Отлично, а утебя")

@bot.message_handler(regexp="Отлично")
def answer(message):
	bot.send_message(message.chat.id, "Взаимно")

@bot.message_handler(regexp="Хорошо")
def answer(message):
	bot.send_message(message.chat.id, "Это хорошо что у тебя хорошо")

@bot.message_handler(regexp="Плохо")
def answer(message):
	bot.send_message(message.chat.id, "Сочувствую")

@bot.message_handler(regexp="Пока")
def answer(message):
	bot.send_message(message.chat.id, "Не уходи мне будет скучно")

@bot.message_handler(regexp="Так себе")
def answer(message):
	bot.send_message(message.chat.id, "Нормально значит")

@bot.message_handler(regexp="Норм")
def answer(message):
	bot.send_message(message.chat.id, "Норм так нор")

@bot.message_handler(regexp="Нормально")
def answer(message):
	bot.send_message(message.chat.id, "Красавчик!")


@bot.message_handler(func=lambda message:True)
def say_smth(message):
	if message.text:
		bot.send_message(message.chat.id, "Я пока это непонимаю")
	elif message.text == "Салам Алейкум":
		bot.reply_to(message, "Ва Алейкум Ассалам варахматуллахи")

if __name__=="__main__":
	bot.polling()  