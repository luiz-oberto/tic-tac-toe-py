import random

marcadores = ["O", "X"]
tabuleiro = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
]

# teste do tabuleiro
def random_insert(marcador):
    # seleciona um elemento aleatório
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)

        if tabuleiro[linha][coluna] not in ["O", "X"]:
            tabuleiro[linha][coluna] = marcador
            return
    
    '''
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
    '''


# === VERIFICAÇÕES DE LINHAS, COLUNAS E DIAGONAIS ===
# FALTA VERIFICAR DIAGONAIS!!!
def verifica_linha(tab):
    ''' 
    verifica se uma linha possui 3 elementos iguais
    '''
    for linha in tab:
        if linha[0] == linha[1] == linha[2]:
            return True
    return False

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
    '''

    
def verifica_coluna(tab):
    '''
    Verifica se uma coluna possui os três elementos iguais
    '''
    for i in range(3):
        if tab[0][i] == tab[1][i] == tab[2][i]:
            return True
    return False

    '''
    i = 0
    coluna_linha = []
    
    while i <= 2:
        colunas = []
        # transforma as colunas em linhas
        for linha in tabuleiro:
            colunas.append(linha[i])
            
        coluna_linha.append(colunas)
        i+=1
    
    return verifica_linha(coluna_linha)
    '''

def main():
    turno = 0
    while turno < 9:
        jogador = marcadores[turno % 2]
        random_insert(jogador)

        # verificar se game_over
        if verifica_linha(tabuleiro):
            print("3 elementos iguais numa linha!")
            break
        
        elif verifica_coluna(tabuleiro):
            print("3 elementos iguais numa coluna!")
            break


        turno+=1    


    for linha in tabuleiro:
        print(linha)


main()
