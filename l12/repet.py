# class Human():
# 	bipedalism = True
# 	intellect = 999
# 	def speech(self):
# 		print("Я человек")
# firstman = Human()
# print("Уровень интелекта -",firstman.intellect)
# firstman.speech()

# secondman = Human()
# print(secondman.intellect)
# firstman.speech()

class Cat():
	def __init__(self, jump, tail_lenght, mind):
		self.jump = jump
		self.tail_lenght = tail_lenght
		self.mind = mind

	def Meow(self):
		print("Мяуууууууууууууууууууууууууууууууууууууууууууу!")

tom = Cat(100, 1, 500)
print(tom.jump)

barseek = Cat(20, 50, 0)
print(barseek.jump)

if tom.mind > barseek.mind:
	print("Том мудр!")
else:
	print("Том мудр, но Барсик мудрее")







