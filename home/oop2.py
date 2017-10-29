class Player:
	def __init__(self, name, hands, legs, eyes, money):
		self.name = name
		self.hands = hands
		self.legs = legs
		self.eyes = eyes
		self.hidden_money = money

	def show_money(self):
		return "Это секрет"

	def change_money(self):
		print("фигушки")

	money = property(show_money, change_money)

player = Player("Человек", 2, 2, 4,"100")
print(player.money)
player.money = "1000"
print(player.money)