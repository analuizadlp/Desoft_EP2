import random
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
        [[3, 6], [3, 7]]],   
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}
tamanho_frota= {
    "porta-aviões":4,
    "navio-tanque":3,
    "contratorpedeiro":2,
    "submarino":1,
    }
for nome in frota.keys():
    n = 0
    if nome == 'porta-aviões':
        i = 1
    elif nome == 'navio-tanque':
        i = 2
    elif nome == 'contratorpedeiro':
        i = 3
    elif nome == 'submarino':
        i = 4
    while n < i:
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho_frota[nome]}')
        linha = int(input('Qual a linha?'))
        coluna = int(input('Qual a coluna?'))
        if nome !='submarino':
            direcao = input('[1] Vertical [2] Horizontal')
        if nome == 'submarino':
            orie = 'vertical'
        if direcao == '1':
            orie = 'vertical'
        elif direcao =='2':
            orie ='horizontal'
        if posicao_valida(frota, linha, coluna, orie, tamanho_frota[nome]) == False:
            print('Esta posição não está válida!')
        else:
            preenche_frota(frota, nome, linha, coluna, orie, tamanho_frota[nome])
            n += 1
# print(frota)
# Jogadas do jogador 
tabuleiro_oponente = posiciona_frota(frota_oponente)


def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '___________      ___________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto
grid_frota = posiciona_frota(frota)
grid_oponente = posiciona_frota(frota_oponente)
old_ataque = []
old_att_oponente = []
jogando = True
while jogando == True:
    grid=monta_tabuleiros(grid_frota, grid_oponente)
    print(grid)
    repete = True
    while repete == True:
        lin = True
        col = True
        while lin == True:
            linha_ataque = int(input('Jogador, qual linha deseja atacar?'))
            if linha_ataque < 0 or linha_ataque > 9:
                print('Linha inválida')
            else:
                lin = False
        while col == True:
            coluna_ataque = int(input('Jogador, qual coluna deseja atacar?'))
            if coluna_ataque < 0 or coluna_ataque > 9:
                print('Coluna inválida!')
            else:
                col = False
        new_ataque = [linha_ataque, coluna_ataque]
        if new_ataque in old_ataque:
            print(f'A posição linha {linha_ataque} e coluna {coluna_ataque} já foi informada anteriormente')
        else:
            repete = False
    old_ataque.append(new_ataque)
    grid_oponente = faz_jogada(grid_oponente, linha_ataque, coluna_ataque)
    emb_afundadas = afundados(frota_oponente, grid_oponente)
    if emb_afundadas == 10:
        jogando = False
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
# Jogadas do oponente
    else:
        turno2 = True
        while turno2:
            r1 = random.randint(0, 9)
            r2 = random.randint(0, 9)
            att_oponente = [r1, r2]
            if att_oponente not in old_att_oponente:
                print(f'Seu oponente está atacando na linha {r1} e coluna {r2}')
                old_att_oponente.append(att_oponente)
                grid_frota = faz_jogada(grid_frota, r1, r2)
                turno2 = False
        if afundados(frota, grid_frota) == 10:
            jogando = False
            print('Xi! O oponente derrubou toda a sua frota =(')