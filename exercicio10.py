def numero():
    numero = float(input("digite um numero: "))

    if numero % 3 == 0:
        return True

    else:
        return False


resultado = numero()
print(resultado)
