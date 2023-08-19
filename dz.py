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
import json
import math
import csv
import random
from random import randint

def main(func):
    # ○ Декоратор, запускающий функцию нахождения корней квадратного
    # уравнения с каждой тройкой чисел из csv файла.
    def generation_csv_file(count):
        with open('my_csv_file.csv', 'w', newline='', encoding='utf-8') as f_write:
            csv.write = csv.writer(f_write, dialect='excel')
            for i in range(count):
                csv.write.writerow([random.uniform(-100, 100), randint(-100, 100), randint(-100, 100)])

    generation_csv_file(randint(10, 20))
    def inner():
        with open('my_csv_file.csv', 'r', newline='') as f:
            csv_file = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for line in csv_file:
                print(line)
                result = func(*line)
                print(result)
        return result

    return inner


def main2(func):
    # ○ Декоратор, сохраняющий переданные параметры и результаты работы
    # функции в json файл.
    my_dict = {}
    def iner2():
        with (open('my_csv_file.csv', 'r', newline='') as f, open('my_csv_file.json', 'w', encoding='utf-8') as file):
            csv_file = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
            for line in csv_file:
                key = str(line)
                value = tuple(func(*line))
                my_dict[key] = value

                # result = func(*line)
                # print(result)


                # temp_dict = {}
                # print(line)
                # for _ in result:
                #     my_dict{line:result}
                # print(type(result))
                # for _  in enumerate(result):
                #     dict.update({line: _})
                # temp_dict = dict(zip(line, result))
                # print(temp_dict)
                # dict.update(line=[*result])
                # my_dict[line] = [*result]
                # line.append(result)

            print(my_dict)
            json.dump(my_dict, file, indent=2, ensure_ascii=False)
        return my_dict

    return iner2


# @main2
@main2
def quadratic_equation(a, b, c):
    answer = []
    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        answer.append(x1)
        answer.append(x2)
    elif discr == 0:
        x = -b / (2 * a)
        answer.append(x)
    else:
        answer.append("Корней нет")
    return answer


# print(quadratic_equation(1, 4, 1))


quadratic_equation()
