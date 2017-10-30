class laze:
	def __init__(self, level, long_sleep,):
		self.__level  = level
		self.__long_sleep = long_sleep

	def sleep(self):
		print(self.long_sleep * "zzzzzzzZZZZZZ")


	@property 
	def level(self):
		return self.__level / 2

	@level.setter
	def level(self, value):
		print("СПИ НО НЕ ПРОСПИ!")
		print(self.__level + value)
		return self.__level + value


	@property
	def show_long(self):
		return "Сколько хочу, столько сплю"


	@show_long.setter
	def show_long(self, value):
		print('Не буди меня')


	

kamil = laze(80, 10)
# kamil.sleep()
# print(kamil.long_sleep) 
# kamil.long_sleep = 12
# print(kamil.long_sleep)
print(kamil.level)
kamil.level = 10


