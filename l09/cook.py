import random
def my_cook(*args, major = "мазик"):
	for product in args:
	 	making_food(product)
	print("Обильно польем " + major)
	print("наше блюдо - " + food_name(args) + " - готово!!!"

def making_food(ingridients):
	print(random.choice(cook_variants) + " " + ingridients)

def food_name(ingridients):
	name = ""
	for ing in ingridients:
		name += ing[1]
	return name



cook_variants = ["Пожарим", "Сварим", \
"Разгоним", "Похороним", "Съедим"]

my_cook("яйца", "молоко", "роцессор",\
 "труп кошки", "корм кошки", "Тухлая колбаска")