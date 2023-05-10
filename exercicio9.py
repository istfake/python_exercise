def notas():
    nota = float(input("Digite sua nota: "))
    if nota < 38:
        print("Aluno reprovado")

    else:
        diferenca = 5 - (nota % 5)
        if diferenca < 3:
            arredondada = nota + diferenca

        else:
            arredondada = nota

        if arredondada >= 40:
            print(f"aluno aprovado com a nota {arredondada}")

        else:
            print("Aluno reprovado")


resultado = notas()
print(resultado)
