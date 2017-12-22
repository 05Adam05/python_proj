import telebot
import datetime


TOKEN = "455886429:AAEZs-Yt1PCPx1tlYAc2WWpi_JxhacJ5dnM"

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=["start"])
def start_kb(message):
	b_kb = telebot.types.ReplyKeyboardMarkup()
	b_kb.row("/start")
	b_kb.row("Событие")
	b_kb.row("Новости")
	b_kb.row("Погода")
	bot.send_message(message.chat.id, "Введи оператор", reply_markup=b_kb)

@bot.message_handler(regexp="Новости")
def answer(message):
	bot.send_message(message.chat.id, "Все новсти в Махачкале вы можете узнать сдесь https://news.yandex.ru/Makhachkala")

# @bot.message_handler(regexp="Событие")
# def answer(message):
# 	data = datetime.date.today()
# 	bot.send_message(message.chat.id, data)
# 	if str(data) == "2017-12-20":
# 		bot.send_message(message.chat.id, "Ураа")
# 	else:
# 		bot.send_message(message.chat.id, "Событий нет")


@bot.message_handler(regexp="Событие")
def answer(message):
	data = datetime.date.today()
	bot.send_message(message.chat.id, data)
	if str(data) == "2017-12-20":
		bot.send_message(message.chat.id, "Ураа")
	elif str(data) == "2017-12-22":
		bot.send_message(message.chat.id, "Бортеневская битва — сражение, произошедшее 22 декабря 1317 года у села Бортенево, в котором тверской князь Михаил Ярославич разбил объединённое войско московского князя Юрия Даниловича и темника Золотой Орды Кавгадыя, вторгшееся в пределы Тверского княжества. В этом сражении тверичи взяли в плен жену князя Юрия Даниловича,\
		 сестру ордынского хана Узбека Кончаку и брата князя Бориса.\n\
		 Можете подробнее узнать сдесь https://ru.wikipedia.org/wiki/%D0%91%D0%BE%D1%80%D1%82%D0%B5%D0%BD%D0%B5%D0%B2%D1%81%D0%BA%D0%B0%D1%8F_%D0%B1%D0%B8%D1%82%D0%B2%D0%B0")
	elif str(data) == "2017-12-23":
		bot.send_message(message.chat.id, "Ежегодно 23 декабря в Египте отмечают годовщину вывода из страны войск Великобритании, Франции и Израиля в 1956 году. Этот день стал одним из национальных праздников и получил название Национального дня освобождения Порт-Саида (Port Said's National Day), которое напоминает о городе, в котором развернулись самые масштабные военные действия \n\
			 Подробнее сдесь http://www.calend.ru/holidays/0/0/2358/")
	elif str(data) == "2017-12-24":
		bot.send_message(message.chat.id, "Днепровско-Карпатская операция – стратегическая наступательная операция \
			советской армии в годы Великой Отечественной войны, \
			проведенная в период с 24 декабря 1943 года по 17 апреля 1944 года \
			против немецко-румынских войск с целью освобождения Правобережной Украины.\
			 Развернувшись на фронте около 1400 км, операция явилась одной из крупнейших в ходе всей войны. \n\
			 Подробнее можете узнать сдесь http://www.calend.ru/event/7386/")
	elif str(data):
		bot.send_message(message.chat.id, "Пока данных о событиях нет")


@bot.message_handler(regexp="Погода")
def answer(message):
	data = datetime.date.today()
	bot.send_message(message.chat.id, data)
	if str(data) == '2017-12-22':
		bot.send_message(message.chat.id, "Днем +6°\n\
Ночью 0°с\n\
Пасмурно")
	elif str(data) == "2017-12-23":
		bot.send_message(message.chat.id, "Днем +4°\n\
Ночью +2°с\n\
Небльшой дождь")
	elif str(data) == "2017-12-24":
		bot.send_message(message.chat.id, "Днем +3°\n\
Ночью 1\n\
Снеш")
	elif str(data) == "2017-12-25":
		bot.send_message(message.chat.id, "Днем +9°\n\
Ночью +5°\n\
Пасмурно")
	elif str(data):
		bot.send_message(message.chat.id, "Данных о погоде нет ")

@bot.message_handler(regexp="На завтра")
def answer(message):
	data = datetime.date.today()
	bot.send_message(message.chat.id, data)
	if str(data) == '2017-12-22':
		bot.send_message(message.chat.id, "Днем +4°\n\
Ночью +2°с\n\
Небльшой дождь")
	elif str(data) == "2017-12-23":
		bot.send_message(message.chat.id, "Днем +3°\n\
Ночью +1°\n\
Снег")
	elif str(data) == "2017-12-24":
		bot.send_message(message.chat.id, "Днем +9°\n\
Ночью +5°с\n\
Пасмурно")
	elif str(data):
		bot.send_message(message.chat.id, "Данных о погоде нет ")

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

@bot.message_handler(regexp="Салам")
def answer(message):
	bot.send_message(message.chat.id, "Ва Алейкум Ассалам варахматуллахи")

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
	bot.send_message(message.chat.id, "Отлично, а у тебя")

@bot.message_handler(regexp="Отлично")
def answer(message):
	bot.send_message(message.chat.id, "Взаимно")

@bot.message_handler(regexp="Хорошо")
def answer(message):
	bot.send_message(message.chat.id, "Это хорошо что хорошо")

@bot.message_handler(regexp="Плохо")
def answer(message):
	bot.send_message(message.chat.id, "Сочувствую")

@bot.message_handler(regexp="Пока")
def answer(message):
	bot.send_message(message.chat.id, "Не уходи мне будет скучно")

@bot.message_handler(regexp="Так себе")
def answer(message):
	bot.send_message(message.chat.id, "Нормально значит")

@bot.message_handler(regexp="Нормально")
def answer(message):
	bot.send_message(message.chat.id, "Красавчик!")

@bot.message_handler(func=lambda message:True)
def say_smth(message):
	if message.text:
		bot.send_message(message.chat.id, "Я пока это непонимаю")
	elif message.text == "Салам":
		bot.reply_to(message, "Ва Алейкум Ассалам варахматуллахи")



if __name__=="__main__":
	bot.polling()  