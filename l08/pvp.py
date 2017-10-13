import random

def creat_player():
	player = {"HP" : 100, "Урон" : 10}
	player["имя"] = input("Веди имя боец: ")
	choose = input("1 - увеличить HP, 2 - увеличить урон ")
	if choose == "1":
		player["HP"] += 30
	else:
		player["Урон"] += 3 
	return player

def show_health(player):
	print("Количество жизней игрока: ",player["имя"], player["HP"])
def attack(attacker, victim):
	damage = random.randint(attacker["Урон"] - 3, attacker["Урон"] + 3)
	print(attacker["имя"], "нанес", damage, "единиц урона")
	victim["HP"] -= damage


player1 = creat_player()
player2 = creat_player()

while True:
	attack(player1, player2)
	attack(player2, player1)

	show_health(player1)
	show_health(player2)

	input()

	if player1["HP"] <= 0:
		print(player2["имя"], "выйграл")
		break

	if player2["HP"] <= 0:
		print(player1["имя"], "выйграл")
		break

