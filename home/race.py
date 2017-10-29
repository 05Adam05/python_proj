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
	"name": "firari",
	"speed": 2,
	"fule": 25,
	"spend": 2,
	"nitro": 8,
	"distance": 0

}

car2 = {
	"name": "LAMBARGINI",
	"speed":3,
	"fule": 30,
	"spend": 3,
	"nitro": 10,
	"distance": 0

}

car3 = {
	"name": "BUGATI",
	"speed": 5,
	"fule": 35,
	"spend": 5,
	"nitro": 11,
	"distance": 0

}

track = 40

while True:
	race_step(car1)
	race_step(car3)

	input()

	if car1["fule"] <= 0:
		print(car2, "выйграл")
		break

	if car2["fule"] <= 0:
		print(car1, "выйграл")
		break

	
