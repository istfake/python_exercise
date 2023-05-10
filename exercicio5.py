def formatar_dinheiro():
    dinheiro = float(input("Quanto dinheiro você tem: "))
    return "R${:,.2f}".format(dinheiro).replace(".", ",")


resultado = formatar_dinheiro()
print(f"resultado deu {resultado}")
