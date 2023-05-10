def divisão_expoente():
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))
    div = dividendo // divisor
    resto = dividendo % divisor
    return div, resto


resultado = divisão_expoente()
print(resultado)
