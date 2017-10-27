class Guns:
	def __init__(self, name, shot_range, calibre, holder, hammer):
		self.name = name
		self.shot_range = shot_range
		self.calibre = calibre
		self.holder = holder
		self.hidden_hammer = hammer

	# def show_hammer(self):
	# 	# return "Это секретная инфа, забудь!!"
	# 	return self.hidden_hammer

	# def change_hammer(self, value):
	# 	# print("Лошара ахаха, руки прочь")
	# 	self.hidden_hammer = value

	# hammer = property(show_hammer, change_hammer)

	@property
	def my_calibre(self):
		return "Мой калибр " + self.calibre 

	@my_calibre.setter
	def my_calibre(self, value):
		self.calibre = value + " Навальный"


railgun = Guns("Рельсотрон", 200000, "100*200", 1, "USA")
# print(railgun.hammer)
# railgun.hammer = "MatherRussia"

print(railgun.my_calibre)
railgun.my_calibre = "200*400"
print(railgun.my_calibre) 
