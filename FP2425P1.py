# This is the Python script for your project

# tab - tabuleiro
# num_p - número de posições
# pos - posição
# m - tuplos que representam linhas
# n - elementos que representam colunas

def eh_tabuleiro(tab): # Verifica se o argumento introduzido corresponde a um tabuleiro.

    if not (2 <= len(tab) <= 100): # Verifica se o tabuleiro tem entre 2 ou 100 linhas.
        return False
    
    expected_num_col = len(tab[0]) # Verificar se o número de colunas é igual em todas as linhas.
    for line in tab: # Verificar colunas
        for element in line:
            if element not in [-1, 0, 1]:
                return False
        if len(line) != expected_num_col: # Verificar se o número de colunas é igual em todas as linhas.
            return False
    return True

def eh_posicao(num_p):
        return isinstance(num_p, int) and 1 <= num_p <= 100 * 100 # Verificar se a posição existe o mínimo é 1 e o máximo é 100 * 100,

def obtem_dimensao(tab):
    return (len(tab), len(tab[0]))  

def obtem_valor(tab, pos):
    tamanho_line = len(tab[0])
    line = (pos - 1) // tamanho_line
    column = (pos - 1) % tamanho_line
    return tab[line][column]


def obtem_coluna(tab,pos):
    tamanho_line = len(tab[0])
    tuple_col = ()
    column = (pos - 1) % tamanho_line # column é o indice
    posicao_inicial = column + 1
    posicao_max = len(tab) * tamanho_line

    posicao_atual = posicao_inicial

    while posicao_atual <= posicao_max:

        tuple_col += (posicao_atual,)
        posicao_atual += tamanho_line

    return tuple_col

def obtem_linha(tab,pos):
    tuple_line = ()
    tamanho_line = len(tab[0])
    line = (pos - 1) // tamanho_line
    posicao_inicial = (line * tamanho_line) + 1
    posicao_max = posicao_inicial + tamanho_line - 1

    posicao_atual = posicao_inicial

    while posicao_atual <= posicao_max:

        tuple_line += (posicao_atual,)
        posicao_atual += 1

    return tuple_line

def obtem_diagonais(tab, pos):

    tamanho_linha = len(tab[0])
    tamanho_coluna = len(tab)
    max = tamanho_coluna * tamanho_linha

    iniciais_diagonais = (tuple(range(1, tamanho_linha +1)))
    for i in range(1, tamanho_coluna):
        iniciais_diagonais += (i * tamanho_linha + 1,)

    iniciais_antidiagonais = tuple(range(max, max - tamanho_linha, -1))
    for i in range(0,tamanho_coluna - 1):
        iniciais_antidiagonais += (i * tamanho_linha + 1,)

    tuplo_diagonais = ()
    tuplo_antidiagonais = ()
    for inicio in iniciais_diagonais:
        if pos in tuple(range(inicio, max, tamanho_linha + 1)):
            tuplo_diagonais = tuple(range(inicio, max, tamanho_linha + 1))

    for inicio in iniciais_antidiagonais:
        if pos in tuple(range(inicio, 0, - tamanho_linha + 1)):
            tuplo_antidiagonais = tuple(range(inicio, 0, - tamanho_linha + 1))
    return (tuplo_diagonais, tuplo_antidiagonais)

def tabuleiro_para_str(tab): 
    representacao_tab = ''

    for i_linha in range(len(tab)):
        linha = tab[i_linha]
        for i_col in range(len(linha)):
            col = linha[i_col]
            if col == 1:
                representacao_tab += 'X'
            elif col == -1:
                representacao_tab += 'O'
            else:
                representacao_tab += '+'
            
            if i_col < len(linha) - 1:
                representacao_tab += '---'
    
        if i_linha < len(tab) - 1:
            representacao_tab += '\n'
            for col in range(len(tab[0])):
                representacao_tab += '|'
                if col < len(linha) - 1:
                    representacao_tab += '   '
            representacao_tab += '\n'

    return representacao_tab

def eh_posicao_valida(tab, pos): 

    if eh_tabuleiro(tab) and isinstance(pos, int):
        if 1 <= pos <= len(tab) * len(tab[0]):
            return True
    else:
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    
def eh_posicao_livre(tab, pos):

    if isinstance(tab, tuple) and isinstance(pos, int):
        if pos < 0 or pos >= len(tab[0]):
           return False
        
    for linha in tab:
        if linha[pos] == 0:
            return True
    else:
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    
def obtem_posicoes_livres(tab): 
    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    else:
        posicoes_livres = ()

        for linha in range(len(tab)):
            for col in range(len(tab[linha])):
                if  tab[linha][col] == 0:
                    posicoes_livres += (linha * len(tab[0]) + col + 1,)
        return posicoes_livres

def obtem_posicoes_jogador(tab, jog):
    if not eh_tabuleiro(tab) or not (jog in [-1, 0, 1]):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    else: # É preciso?
        tuplo_posicoes = ()  
        for linha in range(len(tab)): # 
            for col in range(len(tab[linha])):
                if  tab[linha][col] == jog:
                    tuplo_posicoes += (linha * len(tab[0]) + col + 1,)
        return tuplo_posicoes
    
def obtem_posicoes_adjacentes(tab, pos):
    dimensoes = obtem_dimensao(tab)
    max_posicao = dimensoes[0] * dimensoes[1]
    if not (eh_tabuleiro(tab) and isinstance(pos, int) and (1 <= pos <= max_posicao)):
        raise ValueError('obtem_posicoes_adjacentes: argumentos invalidos')
    else:
        tuplo_adjacentes = ()
        tamanho_linha = len(tab[0])

        index_linha_pos = (pos -1) // tamanho_linha
        index_coluna_pos = (pos -1) % tamanho_linha

        for index_linha in range(index_linha_pos - 1, index_linha_pos + 2):
            for index_coluna in range(index_coluna_pos - 1, index_coluna_pos + 2):
                posicao_adjacente = index_linha * tamanho_linha + index_coluna + 1

                condicao_linha_esperada = index_linha == ((posicao_adjacente - 1) // tamanho_linha)
                condicao_pertencer_tabuleiro = 1 <= posicao_adjacente <= max_posicao

                if condicao_linha_esperada and condicao_pertencer_tabuleiro and posicao_adjacente != pos:
                    tuplo_adjacentes += (posicao_adjacente,)

        return tuplo_adjacentes
    

def ordena_posicoes_tabuleiro(tab, tup):
    if not (eh_tabuleiro(tab) and isinstance(tup, tuple)):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    else:
        dimensao = obtem_dimensao(tab)
        m = dimensao[0]
        n = dimensao[1]

        posicao_central = (m // 2) * n + (n // 2) + 1
        
        def distancia(pos1, pos2):
            
            linha1 = (pos1 - 1) // n
            coluna1 = (pos1 - 1) % n

            linha2 = (pos2 - 1) // n
            coluna2 = (pos2 - 1) % n

            return max(abs(linha2 - linha1), abs(coluna2 - coluna1))
        
        tuplo_distancias = ()
        for elemento in tup:
            distancia_central = distancia(posicao_central, elemento)
            tuplo_elemento_distancia = (elemento, distancia_central)
            tuplo_distancias += (tuplo_elemento_distancia,)

        tuplo_distancias = sorted(tuplo_distancias, key = lambda x: (x[1], x[0])) # 1 é a distancia e 0 é a posição

        tuplo_final = ()
        for elemento in tuplo_distancias:
            tuplo_final += (elemento[0],)

    return tuplo_final

def marca_posicao(tab, pos, jog):
    condicao_validacao_tab = eh_tabuleiro(tab) and eh_posicao_valida(tab, pos) and (jog in (-1, 1))
    if not condicao_validacao_tab:
        raise ValueError('marca_posicao: argumentos invalidos')

    else:
        dimensoes = obtem_dimensao(tab)
        tamanho_linha = dimensoes[1]

        index_linha_pos = (pos - 1) // tamanho_linha
        index_coluna_pos = (pos - 1) % tamanho_linha

        tabuleiro_marcado = ()
        for index_linha in range(len(tab)):
            tuplo_aux = ()
            for index_coluna in range(len(tab[index_linha])):
                if index_coluna == index_coluna_pos and index_linha == index_linha_pos:
                    tuplo_aux += (jog,)
                    continue
                tuplo_aux += (tab[index_linha][index_coluna],)
            tabuleiro_marcado += (tuplo_aux,)

    return tabuleiro_marcado


