# Задача 1

from dotenv import dotenv_values


def get_rectangle_square(width, height):
    return width * height

config = dotenv_values('.env')
width = int(config['width'])
height = int(config['height'])
print('Площадь прямоугольника:', get_rectangle_square(width, height))