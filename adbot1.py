import telebot
import datetime


TOKEN = "455886429:AAEZs-Yt1PCPx1tlYAc2WWpi_JxhacJ5dnM"

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=["start"])
def start_kb(message):
  b_kb = telebot.types.ReplyKeyboardMarkup()
  b_kb.row("Анекдот")
  b_kb.row("Событие")
  b_kb.row("Новости")
  b_kb.row("Погода")
  bot.send_message(message.chat.id, "Введи оператор", reply_markup=b_kb)

@bot.message_handler(regexp="Новости")
def answer(message):
  bot.send_message(message.chat.id, "«Газпром» ответил на заявление «Нафтогаза» о победе в суде Стокгольма\n\
Подробнее https://news.yandex.ru/yandsearch?cl4url=iz.ru/686771/2017-12-22/gazprom-otvetil-na-zaiavlenie-naftogaza-o-pobede-v-sude-stokgolma&lang=ru&from=main_portal&stid=tJ9HJo48CGWu9zcPuPQY&t=1513970601&lr=28&msid=1513970982.68399.22889.10998&mlid=1513970601.glob_225.8660bcfd\n\
Пленум ЦК КПРФ рекомендовал выдвинуть в президенты Грудинина\n\
Подробнее https://news.yandex.ru/yandsearch?cl4url=russian.rt.com/russia/news/463385-kprf-rekomendaciya-kandidat-grudinin&lang=ru&from=main_portal&stid=pSSsrWNbNMfVSx0-CKVZ&t=1513970759&lr=28&msid=1513971118.51232.22879.22626&mlid=1513970759.glob_225.15fb5518\n\
Бориса Джонсона отправили из России домой сытым\n\
Подробнее https://news.yandex.ru/yandsearch?cl4url=www.gazeta.ru/politics/news/2017/12/22/n_10969190.shtml&lang=ru&from=main_portal&stid=y1PG6O9cL7DqIoYG9NDk&t=1513970759&lr=28&msid=1513971163.60245.22877.14087&mlid=1513970759.glob_225.ebaf1429\n\
США ввели санкции против 10 граждан бывшего СССР\n\https://news.yandex.ru/yandsearch?cl4url=www.gazeta.ru/social/2017/12/22/11517392.shtml&lang=ru&from=main_portal&stid=1jx2kBDnF5h8mdZs1Qsd&t=1513970914&lr=28&msid=1513971364.8613.22880.19081&mlid=1513970914.glob_225.21d6442d\n\
Порошенко и Тиллерсон скоординировали позиции по миссии ООН в Донбассе\n\
https://news.yandex.ru/yandsearch?cl4url=ria.ru/world/20171222/1511555888.html&lang=ru&from=main_portal&stid=-aOPkrg_7XBeDSxmeAGO&t=1513971093&lr=28&msid=1513971512.31724.22887.25737&mlid=1513971093.glob_225.cd4c0118\n\
USD ЦБ58,32−0,24-0,24EUR ЦБ69,13−0,39-0,39НЕФТЬ65,11+0,56%+0,56%")
# @bot.message_handler(regexp="Событие")
# def answer(message):
#   data = datetime.date.today()
#   bot.send_message(message.chat.id, data)
#   if str(data) == "2017-12-20":
#     bot.send_message(message.chat.id, "Ураа")
#   else:
#     bot.send_message(message.chat.id, "Событий нет")


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
    bot.send_message(message.chat.id, "Ежегодно 23 декабря в Египте\n\
отмечают годовщину вывода из страны войск Великобритании,\n\
Франции и Израиля в 1956 году. \n\
Этот день стал одним из национальных праздников\n\
и получил название Национального дня освобождения Порт-Саида\n\
(Port Said's National Day), которое напоминает о городе,\n\
в котором развернулись самые масштабные военные действия \n\
https://www.pando4ka.com/events/1848/")
  elif str(data) == "2017-12-24":
    bot.send_message(message.chat.id, "Днепровско-Карпатская операция – стратегическая\n\
наступательная операция советской армии \n\
в годы Великой Отечественной войны, проведенная \n\
в период с 24 декабря 1943 года по 17 апреля 1944 года \n\
против немецко-румынских войск с целью освобождения Правобережной Украины.\n\
Развернувшись на фронте около 1400 км, операция явилась \n\
одной из крупнейших в ходе всей войны. \n\
Подробнее можете узнать сдесь http://www.calend.ru/event/7386/")
  elif str(data):
    bot.send_message(message.chat.id, "Пока данных о событиях нет")



@bot.message_handler(regexp="Мем")
def answer(message):
  bot.send_message(message.chat.id,  )



@bot.message_handler(regexp="Погода")
def answer(message):
  data = datetime.date.today()
  bot.send_message(message.chat.id, data)
  if str(data) == '2017-12-22':
    bot.send_message(message.chat.id, "Днем +6°\n\
Ночью +1°\n\
Пасмурно")
  elif str(data) == "2017-12-23":
    bot.send_message(message.chat.id, "Днем +4°\n\
Ночью +2°\n\
Небльшой дождь")
  elif str(data) == "2017-12-24":
    bot.send_message(message.chat.id, "Днем +3°\n\
Ночью 0\n\
Снеш")
  elif str(data) == "2017-12-25":
    bot.send_message(message.chat.id, "Днем +11°\n\
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
Ночью 0°\n\
Снег")
  elif str(data) == "2017-12-24":
    bot.send_message(message.chat.id, "Днем +11°\n\
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