# guests = input("Веди список готей: ")
# print(guests)
# list_of_guests = guests.split(", ")
# print(list_of_guests[1])

# final_guest = " + ".join(list_of_guests)
# print(final_guest)

# numbers = input("Веди числа ")
# numbers_list = numbers.split(" ")

# print(numbers_list)


# for i in numbers_list:
# 	n = 0 
# 	numbers_list[0] = int(i)
# 	n += 1

# print(numbers_list)

# print(len(numbers_list))
# print(min(numbers_list))
# print(max(numbers_list))

numbers2 = [20,21,15,29]

guess = int(input("отгадай чичло"))

print(guess in numbers2)
	
numbers3 = {5,10,15,20}
if guess in numbers3:
	print("ура")