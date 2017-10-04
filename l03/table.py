import random

print("Реши пример !!!")
number1 = int(input("ВЕди первое число: "))
number2 = random.randint(0,10)
answer = int(imput("Умножь " + str(number1) + " на " + str(number2) + " : "))

if (answer == number1 * number2): 
    print("МужиГ!!!")
else:
    print("Позор, стыд,растрел")
