# Сщздать класс Human подклассы player и зомбиэ
# Игрок и зомби деруться.Умирает зомби - появляетмся зомби
# умир тгрок - игра окончена
class Human:
	def __init__(self, heath, damage):
		self.heath = heath
		self.damage = =damage


	def attack(self, target):
		target.heath -= self.damage
		print("Нанес урон", self.damage)

class Player(Human):
	def __init__(self, heath, damage, count_kit):
		super().__init__(heath,damage)
		self.count_kit = count_kit

	def heal(self):
		if self.count_kit > 0:
			self.count_kit -= 1
			self.heath += 10
			print("+ 10 HP ваше здоровье")
		else:
			print("Сорян, аптечик нет")

class Zombie(Human):
	def death(self):
		print("УААУААУаааааау")

def game():
	count_kill = 0
	sidor = Player(125, 20, 3)
	zombie = Zombie(10, 5)
	while True:		
		sidor.attack(zombie)
		input()
		zombie.attack(sidor)
		input()
		if zombie.heath <= 0:
			zombie.death()
			zombie = Zombie(30, 5)
			count_kill += 1
		print("Ваш уровень здоровья", sidor.heath,
			"Вы хотите апечку?")
		i = int(input("1 - Да" + " 2 - нет"))
		if i == 1:
			sidor.heal()

		if sidor.heath <= 0:
			print("Некому нести хаабар")
			break









