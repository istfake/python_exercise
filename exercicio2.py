a = input("numero do primeiro lado: ")
b = input("numero do segundo lado: ")
c = input("numero do terceiro lado: ")


def classe_triangulo(a, b, c):
    if a == b and b == c:
        return "equilatero"

    elif a == b or b == c or a == c:
        return "Isóceles"

    else:
        return "escaleno"


print(classe_triangulo(a, b, c))
