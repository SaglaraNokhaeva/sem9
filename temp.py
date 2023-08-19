import math


def quadratic_equation(a, b, c):
    answer = []
    discr = b ** 2 - 4 * a * c
    if a==0:
        x = -c/b
        answer.append(x)
    else:
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
print(quadratic_equation(0,-2,1))
# -2.309372391483992, 1.434372391483992