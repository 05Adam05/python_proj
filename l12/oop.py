# class Animal:
# 	def __init__(self, hands, areal, feed):
# 		self.hands = hands
# 		self.areal = areal
# 		self.feed = feed

# 	def scream(self, name):
# 		print("Ааааааа! Где мой " + name + "????")
# 		print("Я хочу есть " + self.feed)

# 	def attack(self, victim):
# 		print("Набросился на соперника всеми " + self.hands + "мя лапами")


# # revun = Animal(4, "Россия Матушка", "нытье")
# # print("Ревун обитает в " + revun.areal)
# # revun.scream("Лукман")

# class Fish(Animal):
# 	def swim(self, speed):
# 		print("Вжух-вжух" * speed)

# # arkadi = Fish(0, "Ак-гёль", "мусор")
# # arkadi.scream("ДИМОНННН!")
# # arkadi.swim(5)

# class Birds(Animal):
# 	def __init__(self, wings, areal, feed, highs):
# 		self.wings = wings
# 		self.areal = areal
# 		self.feed = feed
# 		self.highs = highs

# 	def scream(self):
# 		print("Супер-КААР")

# 	def attack(self):
# 		print("Начал колотить своими " + str(self.wings) + "мя крыльями")

# # kar_karich = Birds(3, "Чернобыль", "Сталкеры", -10)
# # kar_karich.scream()

# class EvilBirds(Birds):
# 	def __init__(self, wings, areal, feed, highs, fangs):
# 		super().__init__(wings, areal, feed, highs)
# 		self.fangs = fangs

# 		def scream(self):
# 			super().scream()
# 			print("Я убью тебя ыыыыыы")


# ruslan = Fish(0, "средиземье", "букашки")
# red = EvilBirds(2, "Повсюду", "Мясо", 1000000, 1)
# # print(red.fangs)
# # red.scream()
# red.attack()
# ruslan.attack()

class Car:
	def __init__(self, wheels, door, speed):
		self.wheels = wheels
		self.door = door
		self.speed = speed

	def go(self, name):
		print("Вуууххухху" + name)		
irari = Car(4, 2, 350)
print("Фирари разгоняется до " + str(firari.speed))
firari.go("Поехали")


# class Aircraft(Car):
# 	def __init__(self,  wheels, door, speed, wings):
# 		self.wheels = wheels
# 		self.door = door
# 		self.speed = speed
# 		self.wings = wings

	
# 	def fly(self, name):
# 		print(name + "в небо " * self.speed)

# boibg = Aircraft(3, 5, 1000, 2)
# boibg.fly("Хочу в ")