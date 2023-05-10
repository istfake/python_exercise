def juros_simples(capital, taxa, tempo):
    juros = capital * (taxa/100) * tempo
    montante = capital + juros
    return montante


def juros_compostos(capital, taxa, tempo):
    montante = capital * ((1 + taxa/100) ** tempo)
    return montante


capital = float(input("Digite o valor do capital inicial: "))
taxa = float(input("Digite o valor da taxa de juros (%): "))
tempo = float(input("Digite o tempo de aplicação (em anos): "))

montante_simples = juros_simples(capital, taxa, tempo)
montante_compostos = juros_compostos(capital, taxa, tempo)

print("O montante sob juros simples é: R$", montante_simples)
print("O montante sob juros compostos é: R$", montante_compostos)
