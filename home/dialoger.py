import os , random
from datetime import datetime

def cleaning():
    os.system("cls")
    print("====================================================")
    print("======================DIALOGER======================")
os.system("title DIALOGER v.0.4")
cleaning()
print("Чтобы разговаривать пишите в поле ввода короткие фразы.")
name = "None"
while True:
    frase = input("»>")
    if (frase.lower().find("привет") != -1):
        cleaning()
        ans = random.randint(0,2)
        if ans == 0:
            print("Здравствуйте , могу ли я вам чем-то помочь?")
        elif ans == 1:
            print("Приветствую , вам помочь?")
        elif ans == 2:
            print("Привет , чем могу помочь?")
    elif (frase.lower().find("дела") != -1) and (frase.lower().find("как") != -1):
        cleaning()
        ans = random.randint(0,2)
        if ans == 0:
            print("У меня все хорошо , а у вас?")
        elif ans == 1:
            print("Отлично!")
        elif ans == 2:
            print("Все нормально.")
    elif (frase.lower().find("калькулятор") != -1):
        cleaning()
        print("Калькулятор открыт.")
        os.system("calc")
    elif (name == "None") and (frase.lower().find("как") != -1) and (frase.lower().find("тебя") != -1)and(frase.lower().find("зовут") != -1):
        cleaning()
        ans = random.randint(0,2)
        if ans == 0:
            print("Вы ещё не дали мне имя. Можете дать его сейчас.")
            name = input("Имя :")
            cleaning()
            print("Теперь меня зовут",name)
        elif ans == 1:
            print("У меня нет имени. Как вы хотите меня звать?")
            name = input("Имя :")
            cleaning()
            print("Теперь меня зовут",name)
        elif ans == 2:
            print("Назовите меня так , как вам угодно.")
            name = input("Имя :")
            cleaning()
            print("Теперь меня зовут",name)
    elif (name != "None") and (frase.lower().find("как") != -1) and (frase.lower().find("тебя") != -1)and(frase.lower().find("зовут") != -1):
        cleaning()
        print("Моё имя -",name)
    elif (frase.lower() == "это хорошо") or (frase.lower() == "это хорошо!") or (frase.lower() == "хорошо")or(frase.lower() == "хорошо!")or(frase.lower() == "ага")or(frase.lower() == "да"):
        cleaning()
        print("Да.")
    elif (frase.lower().find(name) != -1):
        cleaning()
        ans = random.randint(0,2)
        if ans == 0:
            print("Вам что-то нужно?")
        elif ans == 1:
            print("Что вам угодно?")
        elif ans == 2:
            print("Чем могу быть полезен?")
    elif (frase.lower().find("благодарю") != -1) or (frase.lower().find("спасибо") != -1):
        cleaning()
        ans = random.randint(0,2)
        if ans == 0:
            print("Не за что.")
        elif ans == 1:
            print("Моя работа , помогать вам.")
        elif ans == 2:
            print("Обращайтесь!")
    elif (frase.lower().find("какая") != -1) and (frase.lower().find("дата") != -1):
        cleaning()
        print(datetime.now())
    elif (frase.lower().find("какое") != -1) and (frase.lower().find("число") != -1):
        cleaning()
        print(datetime.now())
    elif (frase.lower().find("который") != -1) and (frase.lower().find("час") != -1):
        cleaning()
        print(datetime.now())
    elif (frase.lower().find("какое") != -1) and (frase.lower().find("время") != -1):
        cleaning()
        print(datetime.now())
    elif (frase.lower().find("скажи") != -1) and (frase.lower().find("время") != -1):
        cleaning()
        print(datetime.now())
    elif (frase.lower().find("пока") != -1) or (frase.lower().find("прощай") != -1) or (frase.lower().find("досвидания") != -1)or(frase.lower() == "до свидания"):
        cleaning()
        print("Выход завершен.")
        break
    else:
        cleaning()
        print("Э-э-э . Я вас не понимаю...")