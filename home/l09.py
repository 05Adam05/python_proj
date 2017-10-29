import random
def my_cook(*args, major = "мазик"):
	for product in args:
	 	making_food(product)
	print("Обильно польем " + major)
	print("ваше блюдо - " + food_name(args) + " - готово!!!Ешь(на смерть)")

def making_food(ingridients):
	print(random.choice(cook_variants) + " " + ingridients)

def food_name(ingridients):
	name = ""
	for ing in ingridients:
		name += ing[2]
	return name



cook_variants = ["Пожарим", "Сварим", \
"Разгоним", "Похороним", "Съедим"]

my_cook("яйца", "молоко", "роцессор",\
 "труп кошки", "корм кошки", "тухлая колбаска") 