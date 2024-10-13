# This is the Python script for your project

def eh_tabuleiro(tab): # Verifica se o argumento introduzido corresponde a um tabuleiro.

    """

    A função eh_tabuleiro recebe um argumento tab e devolve True caso o argumento seja um tabuleiro e False caso contrário.
    Um tabuleiro corresponde a uma sequência de tuplos, onde cada tuplo corresponde a uma linha do tabuleiro. 
    Cada linha do tabuleiro é uma sequência de inteiros.
    Inteiro -1 --> peça do jogador O (peças brancas); 
    Inteiro 1 --> peça do jogador X (bolas pretas);
    Inteiro 0 --> casa vazia do tabuleiro.  

    """

    if not (2 <= len(tab) <= 100): # Verifica se o tabuleiro tem entre 2 a 100 linhas.
        return False
    
    expected_num_col = len(tab[0]) # Número de colunas expectável do tabuleiro.
    for linha in tab: 
        for elemento in linha:
            if elemento not in [-1, 0, 1]: # Verificar elementos das colunas
                return False
        if len(linha) != expected_num_col: # Verificar se o número de colunas é igual em todas as linhas.
            return False
    return True


def eh_posicao(num_p):
        
    """

    A função eh_posicao recebe um argumento num_p e devolve True caso o argumento seja uma posição válida e False caso contrário.
    Para que essa posição seja válida, o argumento tem de ser um inteiro entre 1 e 100*100.
    O máximo de posições possíveis é 100*100, uma vez que o tabuleiro tem de ter entre 2 a 100 linhas e entre 2 a 100 colunas.

    """
    return isinstance(num_p, int) and 1 <= num_p <= 100 * 100 


def obtem_dimensao(tab): 
    
    """

    A função obtem_dimensao recebe um argumento tab e devolve um tuplo com dois elementos:
    - O primeiro elemento corresponde ao número de linhas do tabuleiro. 
    - O segundo elemento corresponde ao número de colunas do tabuleiro.

    """
    return (len(tab), len(tab[0])) 


def obtem_valor(tab, pos):

    """
    
    A função obtem_valor recebe dois argumentos: (tab e pos) e devolve o valor da posição (pos) do tabuleiro (tab).
    Para chegarmos ao índice da linha e da coluna da posição (pos) no tabuleiro, utilizamos a seguinte fórmula:
    - linha = (pos - 1) // len(tab[0])
    - coluna = (pos - 1) % len(tab[0])
    
    """

    tamanho_linha = len(tab[0])
    linha = (pos - 1) // tamanho_linha
    coluna = (pos - 1) % tamanho_linha
    return tab[linha][coluna]


def obtem_coluna(tab,pos):

    """
    
    A função obtem_coluna recebe dois argumentos: (tab e pos).
    Devolve um tuplo com as posições da coluna onde se encontra a posição (pos).

    """

    tamanho_linha = len(tab[0])
    tuplo_col = ()
    coluna = (pos - 1) % tamanho_linha 
    posicao_inicial = coluna + 1
    posicao_max = len(tab) * tamanho_linha

    posicao_atual = posicao_inicial

    while posicao_atual <= posicao_max:

        tuplo_col += (posicao_atual,)
        posicao_atual += tamanho_linha

    return tuplo_col


def obtem_linha(tab,pos):

    """

    A função obtem_linha recebe dois argumentos: (tab e pos).
    Devolve um tuplo com as posições da linha onde se encontra a posição (pos).

    """
    tuplo_linha = ()
    tamanho_linha = len(tab[0])
    linha = (pos - 1) // tamanho_linha
    posicao_inicial = (linha * tamanho_linha) + 1
    posicao_max = posicao_inicial + tamanho_linha - 1

    posicao_atual = posicao_inicial

    while posicao_atual <= posicao_max: # Começamos pelo primeiro elemento da linha de pos e vamos até ao último elemento da linha.

        tuplo_linha += (posicao_atual,)
        posicao_atual += 1

    return tuplo_linha


def obtem_diagonais(tab, pos):

    """
    
    A função obtem_diagonais recebe dois argumentos: (tab e pos).
    Devolve dois tuplos: O primeiro tuplo contém todos os elementos da diagonal onde se encontra a posição (pos);
    O segundo tuplo contém todos os elementos da antidiagonal onde se encontra a posição (pos).
    
    """

    tamanho_linha = len(tab[0])
    tamanho_coluna = len(tab)
    max = tamanho_coluna * tamanho_linha

    iniciais_diagonais = (tuple(range(1, tamanho_linha + 1))) # tuplo que contém todas as posições onde as diagonais começam.
    for i in range(1, tamanho_coluna):
        iniciais_diagonais += (i * tamanho_linha + 1,)

    iniciais_antidiagonais = tuple(range(max, max - tamanho_linha, -1)) # tuplo que contém todas as posições onde as diagonais começam.
    for i in range(0, tamanho_coluna - 1):
        iniciais_antidiagonais += (i * tamanho_linha + 1,)

    tuplo_diagonais = ()
    tuplo_antidiagonais = ()
    for inicio in iniciais_diagonais: # Percorrer todas as diagonais para encontrar a posição pos.
        if pos in tuple(range(inicio, max + 1, tamanho_linha + 1)): # Verificamos se a posição está na diagonal.
            tuplo_diagonais = tuple(range(inicio, max + 1, tamanho_linha + 1))

    for inicio in iniciais_antidiagonais: # Percorrer todas as antidiagonais para encontrar a posição pos.
        if pos in tuple(range(inicio, 0, - tamanho_linha + 1)): # Verificamos se a posição está na antidiagonal.
            tuplo_antidiagonais = tuple(range(inicio, 0, - tamanho_linha + 1))
    return (tuplo_diagonais, tuplo_antidiagonais)


def tabuleiro_para_str(tab): 

    """

    A função tabuleiro_para_str recebe um argumento tab e devolve uma string que representa o tabuleiro.
    A representação do tabuleiro é feita da seguinte forma:
    - Cada espaço livre é representada por '+';
    - Cada peça do jogador 1 é representada por 'X';
    - Cada peça do jogador -1 é representada por 'O';
    
    """

    representacao_tab = ''

    for i_linha in range(len(tab)):
        linha = tab[i_linha]
        for i_col in range(len(linha)): # Substituição dos número pela respetiva representação.
            col = linha[i_col]
            if col == 1:
                representacao_tab += 'X'
            elif col == -1:
                representacao_tab += 'O'
            else:
                representacao_tab += '+'
            
            if i_col < len(linha) - 1:
                representacao_tab += '---'
    
        if i_linha < len(tab) - 1: # Adição de linhas horizontais e espaços
            representacao_tab += '\n'
            for col in range(len(tab[0])):
                representacao_tab += '|'
                if col < len(linha) - 1:
                    representacao_tab += '   '
            representacao_tab += '\n'

    return representacao_tab


def eh_posicao_valida(tab, pos): 

    """
    
    A função eh_posicao_valida recebe dois argumentos: (tab e pos).
    Devolve True caso a posição corresponda a uma posição do tabuleiro e False caso contrário.
    Os argumentos têm que ser validados antes de serem utilizados na função.
    
    """

    if eh_tabuleiro(tab) and isinstance(pos, int):
        if 1 <= pos <= len(tab) * len(tab[0]): # Verifica se a posição está dentro dos limites do tabuleiro.
            return True
    else:
        raise ValueError('eh_posicao_valida: argumentos invalidos')
    
    
def eh_posicao_livre(tab, pos):

    """

    A função eh_posicao_livre recebe dois argumentos: (tab e pos).
    Se a posição (pos) não estiver ocupada por nenhuma peça, a função devolve True. Caso contrário, devolve False.
    Os argumentos têm que ser validados antes de serem utilizados na função.

    """
    if not eh_tabuleiro(tab) or not eh_posicao_valida(tab, pos):
        raise ValueError('eh_posicao_livre: argumentos invalidos')
    
    dimensoes = obtem_dimensao(tab)
    tamanho_linha = dimensoes[1]
    index_linha = (pos - 1) // tamanho_linha
    index_coluna = (pos - 1) % tamanho_linha

    return tab[index_linha][index_coluna] == 0

    
def obtem_posicoes_livres(tab): 

    """
    
    A função obtem_posicoes_livres recebe um argumento tab e devolve um tuplo com todas as posições livres do tabuleiro.
    Os argumentos têm que ser validados antes de serem utilizados na função.
    
    """
    if not eh_tabuleiro(tab):
        raise ValueError('obtem_posicoes_livres: argumento invalido')
    else:
        posicoes_livres = ()

        for linha in range(len(tab)):
            for col in range(len(tab[linha])):
                if  tab[linha][col] == 0:
                    posicoes_livres += (linha * len(tab[0]) + col + 1,) # Conversão do índice da linha e da coluna para a posição.

        return posicoes_livres


def obtem_posicoes_jogador(tab, jog):

    """
    
    A função obtem_posicoes_jogador recebe dois argumentos: (tab e jog).
    Devolve um tuplo com todas as posições onde se encontra uma peça do jogador (jog).
    Os argumentos têm que ser validados antes de serem utilizados na função.
    
    """

    if not eh_tabuleiro(tab) or not (jog in [-1, 0, 1]):
        raise ValueError('obtem_posicoes_jogador: argumentos invalidos')
    else:
        tuplo_posicoes = ()  
        for linha in range(len(tab)):  
            for col in range(len(tab[linha])):
                if  tab[linha][col] == jog: # Verifica se a posição contém a peça do jogador (jog).
                    tuplo_posicoes += (linha * len(tab[0]) + col + 1,) # Conversão do índice da linha e da coluna para a posição.

        return tuplo_posicoes
    
    
def obtem_posicoes_adjacentes(tab, pos):

    """

    A função obtem_posicoes_adjacentes recebe dois argumentos: (tab e pos).
    A função retorna um tuplo com as posições adjacentes à posição (pos) no tabuleiro.
    Posições que são adjacentes a uma posição (pos) são as posições que se encontram na mesma linha, coluna ou diagonal.
    O tuplo devolvido pela função tem de estar ordenado de menor a maior.
    Os argumentos têm que ser validados antes de serem utilizados na função.

    """

    dimensoes = obtem_dimensao(tab) # Obter as dimensões do tabuleiro, recorrendo à função obtem_dimensao.
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
                posicao_adjacente = index_linha * tamanho_linha + index_coluna + 1 # Conversão índices das linhas e colunas para posição. 

                condicao_linha_esperada = index_linha == ((posicao_adjacente - 1) // tamanho_linha)
                condicao_pertencer_tabuleiro = 1 <= posicao_adjacente <= max_posicao

                # Verificação das condições para que a posição adjacente seja válida.

                if condicao_linha_esperada and condicao_pertencer_tabuleiro and posicao_adjacente != pos: 
                    tuplo_adjacentes += (posicao_adjacente,)

        return tuplo_adjacentes
    

def ordena_posicoes_tabuleiro(tab, tup):

    """

    A função ordena_posicoes_tabuleiro recebe dois argumentos: (tab e tup).
    A função ordena as posições do tuplo (tup) de acordo com a distância à posição central do tabuleiro.
    A distância à posição central é calculada pelo valor máximo entre a diferença das linhas e a diferença das colunas.
    Os argumentos têm que ser validados antes de serem utilizados na função.

    """


    if not (eh_tabuleiro(tab) and isinstance(tup, tuple)):
        raise ValueError('ordena_posicoes_tabuleiro: argumentos invalidos')
    else:
        dimensao = obtem_dimensao(tab) # Obter as dimensões do tabuleiro, recorrendo à função obtem_dimensao.
        m = dimensao[0]
        n = dimensao[1]

        posicao_central = (m // 2) * n + (n // 2) + 1 # Cálculo da posição central do tabuleiro.
        
        def distancia(pos1, pos2):

            """
            
            A função distância é uma função auxiliar que recebe dois argumentos: (pos1 e pos2).
            A função devolve a distância entre as duas posições.
            
            """

            linha1 = (pos1 - 1) // n
            coluna1 = (pos1 - 1) % n

            linha2 = (pos2 - 1) // n
            coluna2 = (pos2 - 1) % n

            return max(abs(linha2 - linha1), abs(coluna2 - coluna1)) # Cálculo da distância máxima entre as duas posições.
        
        tuplo_distancias = ()

        for elemento in tup:

            # Recorrendo à função auxiliar calcula a distância entre a posição central e a posição. 
            distancia_central = distancia(posicao_central, elemento) 
            tuplo_elemento_distancia = (elemento, distancia_central) # Tuplo organizado com a posição e a respetiva distância à posição central.
            tuplo_distancias += (tuplo_elemento_distancia,)

        tuplo_distancias = sorted(tuplo_distancias, key = lambda x: (x[1], x[0])) # 1 corresponde à distância e 0 à posição.

        tuplo_final = ()
        for elemento in tuplo_distancias:
            tuplo_final += (elemento[0],) # Apenas colocamos as posições no tuplo final.

    return tuplo_final


def marca_posicao(tab, pos, jog):

    """
    
    A função marca_posicao recebe três argumentos: (tab, pos e jog).
    O argumento (pos) corresponde a uma posição livre do tabuleiro e (jog) identifica o jogador, pode ser 1 ou -1.
    A função devolve um novo tabuleiro com a posição (pos) marcada com a peça do jogador (jog).
    Só queremos alterar a posição inserida no tabuleiro, as restantes posições mantêm-se inalteradas.
    Os argumentos têm que ser validados antes de serem utilizados na função. 

    """
    condicao_validacao_tab = eh_tabuleiro(tab) and eh_posicao_livre(tab, pos) and (jog in (-1, 1))
    if not condicao_validacao_tab:
        raise ValueError('marca_posicao: argumentos invalidos')

    else:

        # Localização da posição introduzida pelo jogador:
        dimensoes = obtem_dimensao(tab)
        tamanho_linha = dimensoes[1]

        index_linha_pos = (pos - 1) // tamanho_linha
        index_coluna_pos = (pos - 1) % tamanho_linha

        tabuleiro_marcado = ()
        for index_linha in range(len(tab)): 
            tuplo_aux = ()
            for index_coluna in range(len(tab[index_linha])):
                # Verificamos se já chegamos à posição introduzida pelo jogador. 
                if index_coluna == index_coluna_pos and index_linha == index_linha_pos: 
                    tuplo_aux += (jog,) # Inserimos a peça do jogador na posição introduzida.
                    continue # Continue serve para não continuarmos à procura, já terminámos a procura.
                tuplo_aux += (tab[index_linha][index_coluna],) 

            tabuleiro_marcado += (tuplo_aux,) # Inserimos a nova linha no tabuleiro.

    return tabuleiro_marcado


def verifica_k_linhas(tab, pos, jog, k):

    """
    
    A função recebe um tabuleiro, uma posição do tabuleiro, um valor inteiro identificando um jogador e um valor inteiro positivo k.
    A função retorna True se existir uma linha (horizontal, vertical ou diagonal) com k ou mais peças do jogador (jog).
    Caso contrário, a função retorna False.
    Os argumentos têm que ser validados antes de serem utilizados na função.
    
    """

    if not (eh_tabuleiro(tab) and eh_posicao_valida(tab, pos) and (jog in (-1, 1)) and isinstance(k, int) and k > 0):
        raise ValueError('verifica_k_linhas: argumentos invalidos')
    
    else:
        linha_pos = obtem_linha(tab, pos)
        coluna_pos = obtem_coluna(tab, pos)
        diagonais_antidiagonais = obtem_diagonais(tab, pos)
        diagonal_pos = diagonais_antidiagonais[0]
        antidiagonal_pos = diagonais_antidiagonais[1]
        posicoes_jog = obtem_posicoes_jogador(tab, jog)

    def conta_pecas_consecutivas_aux(elementos):

        """
        
        A função conta_pecas_consecutivas é uma função auxiliar à função verifica_k_linhas que recebe um argumento (elementos).
        A função devolve True se existirem k ou mais peças consecutivas do jogador (jog) e False caso contrário.
        
        """

        contador = 0
        passou_posicao = False

        for posicao_atual in elementos: # Procurar no elemento se existem k ou mais peças do jogador.
            if posicao_atual == pos:
                passou_posicao = True

            if posicao_atual in posicoes_jog:
                contador += 1
            else:
                contador = 0
                posicao_atual = False

            if contador >= k and passou_posicao:
                return True
        return False
    
    # Chamar a função conta_pecas_consecutivas para as linhas, colunas, diagonais e antidiagonais.
    if conta_pecas_consecutivas_aux(linha_pos) or conta_pecas_consecutivas_aux(coluna_pos) or conta_pecas_consecutivas_aux(diagonal_pos) or conta_pecas_consecutivas_aux(antidiagonal_pos):
        return True
    else:
        return False


def eh_fim_jogo(tab, k):

    """
    
    A função recebe um tabuleiro (tab) e um valor inteiro positivo (k).
    A função retorna True se o jogo terminou e False caso contrário.
    Para que um jogo termine, é necessário que um dos jogadores tenha k ou mais peças consecutivas ou se não existirem posições livres.
    Os argumentos têm que ser validados antes de serem utilizados na função.
    
    """

    if not (eh_tabuleiro(tab) and isinstance(k, int) and k > 0):
        raise ValueError('eh_fim_jogo: argumentos invalidos')
    
    dimensoes = obtem_dimensao(tab)
    posicoes_livres = obtem_posicoes_livres(tab)

    if len(posicoes_livres) == 0:
        return True
    
    for posicao in range(1, dimensoes[0] * dimensoes[1] + 1):
        for jog in (-1, 1):
            ganhou = verifica_k_linhas(tab, posicao, jog, k)
            if ganhou:
                return True
    
    return False


def escolhe_posicao_manual(tab): 
 
    """
    
    A função escolhe_posicao_manual recebe um argumento tab e devolve a posição escolhida, manualmente, pelo jogador.
    A função deve apresentar uma mensagem ao jogador a solicitar a posição desejada.
    A mensagem aparece até que o jogador introduza uma posição livre.
    A função apresenta a posição escolhida pelo jogador.
    O argumento tem que ser validado antes de ser utilizado na função.
    
    """
    if not eh_tabuleiro(tab):
        raise ValueError('escolhe_posicao_manual: argumento invalido')
    
    else:
        dimensoes = obtem_dimensao(tab)
        maximo_posicoes = dimensoes[0] * dimensoes[1]

        posicao_valida = False
        while not posicao_valida:
            pos = int(input('Turno do jogador. Escolha uma posicao livre: '))
            if 0 < pos <= maximo_posicoes:
                posicao_valida = eh_posicao_livre(tab, pos)
                
    return pos


def escolhe_posicao_auto(tab, jog, k, lvl):

    """
    
    A função escolhe_posicao_auto recebe um tabuleiro (tab), um identificador do jogador (jog), um inteiro positivo (k) e uma cadeia de caracteres (lvl).
    A cadeia de caracteres (lvl) corresponde à estraégia utilizada pelo jogador automático.
    A função devolve a posição escolhida automaticamente, de acordo com a estratégia escolhida.
    Sempre que houver mais do que uma posição que cumpra um dos critérios das estratégias, deve escolher a posição mais próxima da posição central do tabuleiro.
    Os argumentos têm que ser validados antes de serem utilizados na função.
    
    """
    estrategias = ("facil", "normal", "dificil")
    condicao_validacao = eh_tabuleiro(tab) and (jog in (-1, 1)) and isinstance(k, int) and k > 0 and lvl in estrategias
    if not condicao_validacao:
        raise ValueError('escolhe_posicao_auto: argumentos invalidos')
    
    else:
        def estrategia_escolhida_facil():

            """
            
            A função escolhe_estratégia_aux é uma função auxiliar que define cada uma das três estratégias possíveis.
            Na estratégia fácil, o jogador escolhe uma posição livre adjacente à sua.
            Na estratégia normal, o jogador que tenha peças consecutivas (menores que k):
                - Escolhe uma posição livre adjacente à sua, que lhe permita ganhar;
                - Caso contrário, escolhe uma posição livre adjacente à do adversário.
            Na estratégia difícil, o jogador 
            
            """
            posicoes_jog = obtem_posicoes_jogador(tab, jog)
            tuplo_posicoes_adj_jog = ()
            for posicao_jog in posicoes_jog:
                posicoes_adj_jog = obtem_posicoes_adjacentes(tab, posicao_jog)
                for posicao_adj_jog in posicoes_adj_jog:
                    if eh_posicao_livre(tab, posicao_adj_jog):
                        tuplo_posicoes_adj_jog += (posicao_adj_jog,)
                    
            return tuplo_posicoes_adj_jog
    

        def estrategia_escolhida_normal():
            tuplo_posicoes_l = ()
            tuplo_posicoes_adv = ()
            posicoes_livres = obtem_posicoes_livres(tab)
            for l in range(k, 0, -1):
                for posicao_livre in posicoes_livres:

                    tabuleiro_hipotetico = marca_posicao(tab, posicao_livre, jog)
                    chegou_ao_l = verifica_k_linhas(tabuleiro_hipotetico, posicao_livre, jog, l) 
                    if chegou_ao_l:
                        tuplo_posicoes_l += (posicao_livre, )

                    tabuleiro_hipotetico_adv = marca_posicao(tab, posicao_livre, - jog)
                    chegou_ao_l_adv = verifica_k_linhas(tabuleiro_hipotetico_adv, posicao_livre, -jog, l)
                    if chegou_ao_l_adv:
                        tuplo_posicoes_adv += (posicao_livre, )

                if len(tuplo_posicoes_l) != 0: # Não retoirnar tuplo vazio
                    return tuplo_posicoes_l
                elif len(tuplo_posicoes_adv) != 0:
                    return tuplo_posicoes_adv

            return ()

        
        possibilidades = ()
        if lvl == "facil":
            possibilidades = estrategia_escolhida_facil()
        elif lvl == "normal":
            possibilidades = estrategia_escolhida_normal()
        
        return ordena_posicoes_tabuleiro(tab, possibilidades)[0]
    
    
    
def jogo_mnk(cfg, jog, lvl):

    """

    Esta é a função principal do jogo.
    A função jogo_mnk recebe três argumentos: (cfg, jog e lvl):
    - O argumento cfg é um tuplo com três elementos: (m, n, k).
        - m representa o número de linhas do tabuleiro;
        - n representa o número de colunas do tabuleiro;
        - k representa o número de peças consecutivas necessárias para ganhar o jogo.
    - O argumento jog é um inteiro que identifica o jogador humano. Pode ser 1 (pedras pretas) ou -1 (pedras brancas).
    - O argumento lvl é uma cadeia de caracteres que identifica a estratégia utilizada pela máquina (automático).
    O jogo começa sempre com o jogador das pedras pretas (jog = 1) a marcar uma posição livre no tabuleiro.
    O jogo termina quando um dos jogadores vence ou se não existirem posições livres no tabuleiro.
    A função devolve o resultado de jogo numa string e um inteiro que identifica o jogador vencedor ou 0 em caso de empate.
    Os argumentos têm que ser validados antes de serem utilizados na função.
    
    """

    condicao_esperada = isinstance(cfg, tuple) and len(cfg) == 3 and isinstance(jog, int) and (jog in (-1, 1)) and isinstance(lvl, str)

    if not condicao_esperada:
        raise ValueError('jogo_mnk: argumentos invalidos')
    
    else:
        pass
    pass
