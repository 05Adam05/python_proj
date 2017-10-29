class Player:
	def __init__(self, name, hands, legs, eyes, money):
		self.name = name
		self.hands = hands
		self.legs = legs
		self.eyes = eyes
		self.money = money

	@property
	def my_money(self):
		return "Мои деньги " + self.money

	@my_money.setter
	def my_money(self, value):
		self.money = value + "фиг"

player = Player("Человек", 2, 3, 4, "100")

print(player.my_money)
player.my_money = "1000"
print(player.my_money)

