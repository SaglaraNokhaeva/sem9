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
quadratic_equation(-16.0, -14.0, 53.0)

# -2.309372391483992, 1.434372391483992