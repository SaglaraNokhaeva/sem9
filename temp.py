import math


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
quadratic_equation(-68.0, -54.0, 29.0)

# -1.1613403800109576 0.36722273295213426