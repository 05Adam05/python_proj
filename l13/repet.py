class Car:
	def __init__(self, color, firm):
		self.color = color
		self.firm = firm

	def signal(self):
		print("бибиииииииппипи")

volga = Car("Красный", "Газ")
volga.signal()
print(volga)


class Cargo_car(Car):
	def __init__(self, color, firm, carrying):
		super().__init__(color, firm)
		self.carrying = carrying

	def signal(self):
		print("ТА_ДААААААААМ")

belaz = Cargo_car("Желтый", "Белаз", 450000)
belaz.signal()