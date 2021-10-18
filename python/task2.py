from dotenv import dotenv_values


def square(number):
	for i in range(number):
		print('*' * number)

config = dotenv_values('.env')
number = int(config['number'])
print(square(number))