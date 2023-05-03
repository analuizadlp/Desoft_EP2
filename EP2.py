# definindo posições
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    for i in range(tamanho):
        if orientacao == "horizontal":
            posicoes.append([linha, coluna+i])
        else:
            posicoes.append([linha+i, coluna])
    return posicoes
# preenche frotas
def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio in frota:
        frota[nome_navio].append(posicoes)
    else:
        frota[nome_navio] = [posicoes]
    return frota
# embarcações afundadas?
def afundados(frota, tabuleiro):
    afundados = 0
    for tipo, navios in frota.items():
        for navio in navios:
            if all(tabuleiro[x][y] == 'X' for x, y in navio):
                afundados += 1
    return afundados