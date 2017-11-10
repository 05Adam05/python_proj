import random
class Human:
	def __init__(self, name, heath, damage):
		self.name = name
		self.heath = heath
		self.damage = damage
	def attack(self, target):
		target.heath -= self.damage
		print(self.name,"Нанес урон", self.damage)
class Player(Human):
	def __init__(self, name, heath, damage, count_kit):
		super().__init__(name, heath, damage)
		self.count_kit = count_kit
	def heal(self):
		if self.count_kit > 0:
			self.count_kit -= 1
			self.heath += 10
			print("+ 10 HP ваше здоровье:", self.heath)
		else:
			print("Сорян, аптечик нет")
class Zombie(Human):
	def death(self):
		print("УААУААУаааааау")
def game():
	count_kill = 0
	sidor = Player("Сидор", 85,random.randint(18,22), 3)
	zombie = Zombie("Тварь", 30,random.randint(4,7))
	while True:		
		sidor.attack(zombie)
		input()
		zombie.attack(sidor)
		input()
		if zombie.heath <= 0:
			zombie.death()
			zombie = Zombie("Тварь", 30, random.randint(4,7))
			count_kill += 1
		print("Ваш уровень здоровья", sidor.heath,
			"Вы хотите апечку?")
		i = int(input("1 - Да" + " 2 - нет"))
		if i == 1:
			sidor.heal()

		if sidor.heath <= 0:
			print("Сидоровияч умудрился замочить", count_kill,
				"и пал смертью храбырых, теперь сталкером некому нести хабар")
			break
game()