class Car:
	def __init__(self, wheels, door, speed):
		self.wheels = wheels
		self.door = door
		self.speed = speed

	def go(self, name):
		print("Вуууххухху" + name)
		print("Я хочу разогнаться до " + str(self.speed))

firari = Car(4, 2, 350)
print("Фирари разгоняется до " + str(firari.speed))
firari.go("Адам")


class Aircraft(Car):
	def __init__(self,  wheels, door, speed, wings):
		self.wheels = wheels
		self.door = door
		self.speed = speed
		self.wings = wings

	
	def fly(self, name):
		print(name + "в небо " * self.speed)

boibg = Aircraft(3, 5, 1000, 2)
boibg.fly("Хочу в ")




