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
#faz jogada
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 'X'
    else:
        tabuleiro[linha][coluna] = '-'
    return tabuleiro
#posiciona frota 
def posiciona_frota(frota):
    grid = [[0 for _ in range(10)] for _ in range(10)]

    for tipo_navio, lista_posicoes in frota.items():
        for posicoes in lista_posicoes:
            for linha, coluna in posicoes:
                grid[linha][coluna] = 1

    return grid
# embarcações afundadas?
def afundados(frota, tabuleiro):
    afundados = 0
    for tipo, navios in frota.items():
        for navio in navios:
            if all(tabuleiro[x][y] == 'X' for x, y in navio):
                afundados += 1
    return afundados