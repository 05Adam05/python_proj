def ride(car):
	car["distance"] += car["speed"]
	car["fule"] -= car["spend"]

def faster(car):
	car["speed"] += 2
	car["spend"] += 2

def nitro(car):
	car["distance"] += car["nitro"]
	car["fule"] -= car["spend"] * 3

def car_info(car):
	print("\n Текущие состояние: ",
		"Топливо: " + str(car["fule"]),
		"Скорость: " + str(car["speed"]),
		"Проехали: " + str(car["distance"]) + "/" + str(track)

		)

def race_step(car):
	choose = input("Твой ход, " + car["name"] + " Что будем делать?")

	if choose == "1":
		ride(car)
	elif choose == "2":
		faster(car)
	else:
		nitro(car)
	car_info(car)
	input()

car1 = {
	"name": "Чайка",
	"speed": 2,
	"fule": 25,
	"spend": 2,
	"nitro": 8,
	"distance": 0

}

car2 = {
	"name": "LAMBARGINI",
	"speed":3,
	"fule": 40,
	"spend": 3,
	"nitro": 11,
	"distance": 0

}

car3 = {
	"name": "BUGATI",
	"speed": 6,
	"fule": 35,
	"spend": 5,
	"nitro": 10,
	"distance": 0

}

track = 40

while True:
	race_step(car2)
	race_step(car3)

	if car2["fule"] <= 0:
		print(car3, "ВЫЙГРАЛ")
		break

	if car3["fule"] <= 0:
		print(car2, "ВЫЙГРАЛ")
		break

	if car2["distance"] >= 40:
		print(car3, "ВЫЙГРАЛ")
		break

	if car3["distance"] >= 40:
		print(car2, "ВЫЙГРАЛ")
		break

