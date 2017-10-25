class Sheros:
	def __init__(self, name, superpower, archemy):
		self.name = name
		self.superpower = superpower
		self.archemy = archemy

	def superpuch(self):
		print(self.name + " нанес стрфшнейший " + self.superpower + 
		"по" + ", сделал фраг")


class Wotermelon:
	def __init__(self, name, weight, diametr):
		self.name = name
		self.weight = weight
		self.diametr = diametr

	def superpunch(self):
		print(self.name + " накатился всеми своими " +
			str(self.weight) + "килограммами и весь мир взныл")




tor = Sheros("Тор-баузер", "пробив молотом блок Роскомнадзора", "ФСБ")

aquaman = Sheros("Аква-мем", "смехотворный удар, призвал Кото-\
	пса Дратути, вытащил рисунок суперспособности", "суперспособности, Дружко")


arboozman = Wotermelon("Петрович", 32000, 1)



def syrike(arboozman):
	arboozman.superpuch()

# syrike(tor)
# syrike(aquaman)
syrike(arboozman)