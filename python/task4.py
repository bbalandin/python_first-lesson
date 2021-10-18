from dotenv import dotenv_values
from random import uniform, randint

def foo(string, number):
	list_words = string.split()
	list_main = list()
	# list_main - массив в который мы кладём конечный результат
	for items in list_words:
		chance = uniform(0, 1)
		# снизу мы добавляем слова-паразиты в list_main
		# с определённой вероятностью
		if chance < number:
			list_main.append(items)
			list_main.append(', блин ')
		elif chance < number:
			list_main.append(items)
			list_main.append(', короче ')
		else:
			list_main.append(items)
			list_main.append(', ну ')

	return ''.join(list_main)

config = dotenv_values('.env')
string = config['string']
number = float(config['number'])

print(foo(string, number))