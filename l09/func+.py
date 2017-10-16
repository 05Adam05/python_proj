# def my_fanc(name):
# 	print("Здрасти " + name)

# # my_fanc("Адам")

# def my_sum(a, b):
# 	print(a + b)
# 	return a + b

# ab_sum = my_sum(25, 50)

# number1 = int(input("Веди первое число"))
# number2 = int(input("Веди второе число"))
# print(my_sum(number1, number2))

# def my_divide(n, m, l, k, p, o):
# 	res = n / m +p* o + k /l
# 	return res

# print(my_divide(n = 15, m = 5, o = 15, k = 20, p = 40, l = 18))

# def group(name1 = "Саид", name2 = "Султан", name3 = "Руслан"):
# 	group_list  = "В нашей группе есть " + name1 + name2 + name3
# 	return group_list

# group("Гаджи", "Аслан", "Ахмед", "Залик")
# print(group("Гаджи", "Аслан"))

def human_list(*args,**kwargs):
	for human in args:
		print(human + "-оглы")
	print(kwargs)


human_list("Адам", "Ева","Кайн", "Авель", godfather = "Отец", hogfather = "Лукман")