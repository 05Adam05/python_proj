class Player:
	def __init__(self, name, hands, legs, eyes, money):
		self.name = name
		self.hands = hands
		self.legs = legs
		self.eyes = eyes
		self.money = money

	def show_money(self):
		return "Это секретная инфа, забудь!!"
		# return self.money

	def change_money(self, value):
		print(" руки прочь")
		# self.hidden_hammer = value

	money = property(show_money, change_money)

	# @property
	# def my_calibre(self):
	# 	return "Мой калибр " + self.calibre 

	# @my_calibre.setter
	# def my_calibre(self, value):s
	# 	self.calibre = value + " Навальный"


player = Player("Чел", 2, 2, 1, "100")
print(player.money)
player.money = "1000"
print(player.money)

# print(railgun.my_calibre)
# railgun.my_calibre = "200*400"
# print(railgun.my_calibre) 