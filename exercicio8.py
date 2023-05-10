def pontuacoes_jogador(pontuacoes: str) -> list:
    pontuacoes = list(map(int, pontuacoes.split()))
    recordes = [pontuacoes[0]]
    recorde_atual = pontuacoes[0]
    pior_jogo = 0
    for i in range(1, len(pontuacoes)):
        if pontuacoes[i] > recorde_atual:
            recorde_atual = pontuacoes[i]
            recordes.append(pontuacoes[i])
        else:
            recordes.append(recorde_atual)
        if pontuacoes[i] < pontuacoes[pior_jogo]:
            pior_jogo = i
    num_recordes = sum(1 for i in range(1, len(recordes))
                       if recordes[i] > recordes[i-1])
    return [num_recordes, pior_jogo+1]


pontuacoes = input("Digite as pontuações separadas por espaço: ")
resultados = pontuacoes_jogador(pontuacoes)
print(
    f"O jogador bateu o recorde {resultados[0]} vezes e o pior jogo foi o número {resultados[1]}.")
