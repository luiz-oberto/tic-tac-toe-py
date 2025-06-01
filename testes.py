import random

marcadores = ["O", "X"]
teste = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
]

# teste do tabuleiro
def random_insert(marcador):
    # seleciona um elemento aleatório
    escolher_linha = random.choice(teste)
    print(escolher_linha)
    escolher_elemento = random.choice(escolher_linha)
    print(escolher_elemento)

    if escolher_elemento == "X" or escolher_elemento == "O":
        print("procurando outra posição")
        random_insert(marcador)

    else:
        # mudar o elemento selecionado por um marcador
        linha = 0
        indice = 0
        
        while linha < len(teste):
            coluna = 0
            while coluna < len(teste[linha]):
                if teste[linha][coluna] == escolher_elemento:
                    print("colocando marcador")
                    teste[linha][coluna] = marcador
                    return
                    
                coluna += 1

            linha += 1



def verifica_linha(tabuleiro):
    ''' 
    verifica se uma linha possui 3 elementos iguais
    '''
    game_over = False

    # itera uma linha de cada vez
    for line in tabuleiro:
        first_mark = ''
        
        # verifica se todos os marcadores da linha são iguais
        for mark in line:
            if first_mark == '':
                first_mark = mark
            elif first_mark == mark:
                game_over = True 
            else:
                game_over = False
                break

        # para o jogo se uma linha for toda igual
        if game_over == True:
            break
            
    return game_over


    
def verifica_coluna():
    '''
    Verifica se uma coluna possui os três elementos iguais
    '''
    i = 0
    coluna_linha = []
    
    while i <= 2:
        colunas = []
        # transforma as colunas em linhas
        for linha in teste:
            colunas.append(linha[i])
            
        coluna_linha.append(colunas)
        i+=1
    
    return verifica_linha(coluna_linha)

#################################################################
i = 0
selecao = 0
while i < 9:
    objeto = marcadores[selecao]
    random_insert(objeto)

    # verificar se game_over
    if verifica_linha(teste):
        print("3 elementos iguais numa linha!")
        print("O jogo acabou")
        break
    
    elif verifica_coluna():
        print("3 elementos iguais numa coluna!")
        print("O jogo acabou")
        break
    

    if selecao == 0:
        selecao = 1
    elif selecao == 1:
        selecao = 0

    i+=1    


for linha in teste:
    print(linha)
