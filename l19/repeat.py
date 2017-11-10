f = open("Grait.txt", "r")
my_list = f.read().split(", ")
i = 5
for n in my_list:
	print(i, n)
	i -= 1