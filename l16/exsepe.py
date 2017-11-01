class MyError(Exception):
	pass
	class Calt:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def summ(self):
		return self.x + self.y

	def minus(self):
		return self.x - self.y

	def delit(self):
		return self.x / self.y

	def ymnoj(self):
		return self.x * self.y

try:
	my_list = [1,2,3]
	x = int(input("Число"))
	y = int(input("Число"))
	if x == 13 or y ==13:
		raise MyError
	number = Calt(x,y)
	print(number.delit())
	print("Я могу работать")
except ZeroDivisionError as wrd:
	print("Возникла ошибка", wrd)
except IndexError as wrd:
	print("Возникла ошибка", wrd)
except ValueError as wrd:
	print("Возникла ошибка", wrd)
except MyError:
	print("Неизвестная ошибка, в коде!")
except: 
	print("Неизвестная ошибка")


