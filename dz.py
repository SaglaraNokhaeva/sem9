# Задание
# Решить задачи, которые не успели решить на семинаре.
# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# ○ Декоратор, запускающий функцию нахождения корней квадратного
# уравнения с каждой тройкой чисел из csv файла.
# ○ Декоратор, сохраняющий переданные параметры и результаты работы
# функции в json файл.
# Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса

import math
import csv
from random import randint
def generation_csv_file(count):
    with open('my_csv_file.csv', 'w', newline='', encoding='utf-8') as f_write:
        csv.write = csv.writer(f_write, dialect='excel')
        for i in range(count):
            csv.write.writerow([randint(-100, 100), randint(-100, 100), randint(-100, 100)])
# generation_csv_file(100)


def main(func):
    def inner():
        with open('my_csv_file.csv', 'r', newline='') as f:
            csv_file = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for line in csv_file:
                print(line)
                result = func(*line)
        return result
    return inner

@main
def quadratic_equation(a, b, c):
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print(x1, x2)
        return x1, x2
    elif discr == 0:
        x = -b / (2 * a)
        print(x)
        return x
    else:
        print("Корней нет")
        return "Корней нет"
# print(quadratic_equation(1, 4, 1))

quadratic_equation()