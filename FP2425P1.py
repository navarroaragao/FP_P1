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
    print(iniciais_diagonais)

    iniciais_antidiagonais = tuple(range(max, max - tamanho_linha, -1))
    for i in range(0,tamanho_coluna - 1):
        iniciais_antidiagonais += (i * tamanho_linha + 1,)
    print(iniciais_antidiagonais)
    tuplo_diagonais = ()
    tuplo_antidiagonais = ()
    for inicio in iniciais_diagonais:
        if pos in tuple(range(inicio, max, tamanho_linha + 1)):
            tuplo_diagonais = tuple(range(inicio, max, tamanho_linha + 1))
    for inicio in iniciais_antidiagonais:
        if pos in tuple(range(inicio, 0, - tamanho_linha + 1)):
            tuplo_antidiagonais = tuple(range(inicio, 0, - tamanho_linha + 1))
    return (tuplo_diagonais, tuplo_antidiagonais)
        
#rint(obtem_diagonal(((1,0,0,1),(-1,1,0,1), (-1,0,0,-1)), 6))




def tabuleiro_str(tab): 

    representacao = ''

    for m in tab:
        representacao_linha = '' #'X---+---+\n| | |\nO---X---+\n| | |\nO---+---+'
        for n in m:
            if n == 1:
                n = 'O'
            elif n == -1:
                n = 'X'
            else:
                n = '+'
    representacao += representacao_linha + '\n'
        
    return representacao

def eh_posicao_valida(tab, pos): 
    if isinstance(tab, tuple) and isinstance(pos, int):
        if 1 <= pos <= 100 * 100:
            return True
    else:
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    
def eh_posicao_livre(tab, pos):

    if isinstance(tab, tuple) and isinstance(pos, int):
        if pos < 0 or pos >= len(tab[0]):
           return False
        
    for m in tab:
        if m[pos] == 0:
            return True
    else:
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    
def obtem_posicoes_livres(tab): # A função não está corretamente, tenho que voltar a fazer...
    posicoes_livres = ()
    for m in tab:
        for i in range(len(m)):
            if  m[i] == 0:
                posicoes_livres += (i + 1,)
    return posicoes_livres

def obtem_posicoes_jogadores(tab, int):
    posicoes_jogadores = ()
    if int != 1 or int != -1 or int != 0:
        raise ValueError('obtem_posicoes_jogadores: argumentos invalidos')
    for m in tab:
        for i in range(len(m)):
            if m[i] == int:
                posicoes_jogadores += (i + 1,)
    posicoes_jogadores_ord = list(sorted(posicoes_jogadores))
    return tuple(posicoes_jogadores_ord)