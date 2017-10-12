import random

player = {"Счет" : 1000} 

player["Имя"] = input("Веди свое имя")

while True:
	player["Ставка"] = int(input("Крутить за: "))

	player["Крутим"] = random.randit(1, 36)
	print(player)

	if player["Крутим"] == player["Ставка"]:
		print(player["Имя"]) + ("Выйграл 1000")
		player["Счет"] += player["Ставка"]

	if player["Ставка"] == 0:
		print["Нельзя ставить 0"]
	if player["Ставка"] >= player["Счет"]:
		print["НЕлбзя больше счета"]
