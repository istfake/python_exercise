import math


def baskara():
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b**2 - 4*a*c
    if delta < 0:
        return ("Delta é negativo")

    elif delta == 0:
        x = -b / (2*a)
        return [x, x]

    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return [x1, x2]


resultado = baskara()
print(f"O resultado é de {resultado}")
