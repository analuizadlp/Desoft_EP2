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
    grid = [0] * 10
    for i in range (len(grid)):
        grid[i] = [0] * 10 
    for p_embarcacao in frota.values():
        for t in p_embarcacao:
            for i in t:
                linha = i[0]
                coluna = i[1]
                grid[linha][coluna] = 1 
    return grid 

# embarcações afundadas?
def afundados(frota, tabuleiro):
    navios_afundados = 0
    for tipo, posicoes in frota.items():
        for posicao in posicoes:
            afundado = True
            for pos in posicao:
                if tabuleiro[pos[0]][pos[1]] != 'X':
                    afundado = False
                    break
            if afundado:
                navios_afundados += 1
    return navios_afundados

# posição válida 
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    navio_seguinte = define_posicoes(linha, coluna, orientacao, tamanho)
    for posicao in navio_seguinte:
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False
        for i in frota.values():
            for j in range(len(i)):
                if posicao in i[j]:
                    return False
    if frota == {}:
        return True 
    return True
# Posicionando Frota e adicionando frota oponente
frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]]}