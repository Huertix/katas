def my_map(callback, list):
	new_list = []

	for item in list:
		new_list.append(callback(item))

	return new_list

items = [1, 2, 3]

print map(lambda x: x*3, items)

print my_map(lambda x: x*3, items)


def m2(lista):
	new_list = []

	for item in list:
		new_list.append(item * 2)

	return new_list

def m3(lista):
	new_list = []

	for item in list:
		new_list.append(item * 3)

	return new_list


def ma2(lista):
	return my_map(por2, lista)	

def ma3(lista):
	return my_map(lambda x: x*3, lista)	

def por2(x):
	return x*2 

