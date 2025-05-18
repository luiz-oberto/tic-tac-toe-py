
'''
Functions for the tic-tac-toe game.
- need to implement the player turn (troca de jogadores de uma jogada para outra)
- need to implement the verifier of game over
'''
from game_screen import screen

# update the game screen
def update_screen():
    for i in range(1, len(screen)+1):
        print(screen[f"linha_{i}"])

# transform the line into a list to change the values
def line_transformer(line, player_option):
    line_copy = screen[f"linha_{line}"]
    line_split = line_copy.split()
    separador = '  '

    for i in range(0, len(line_split)+6, 2):
        line_split.insert(i, separador)

    return line_split

# do the mark of the player in the square selected (X or O)
def mark_one(line_number, line: list, player_option): # parametro: player
    if line_number == 2:
        for i in line:
            match player_option:
                case '1':
                    line[1] = "X"

                case '2':
                    line[5] = "X"

                case '3':
                    line[9] = "X"

    elif line_number == 5:
        for i in line:
            match player_option:
                case '4':
                    line[1] = "X"

                case '5':
                    line[5] = "X"

                case '6':
                    line[9] = "X"

    elif line_number == 8:
        for i in line:
            match player_option:
                case '7':
                    line[1] = "X"

                case '8':
                    line[5] = "X"

                case '9':
                    line[9] = "X"

    return line

# update the game with the line changed
def update_linha(line_to_update: list, line_number):
    update_line = ''
    for i in line_to_update:
        update_line += i
    screen[f"linha_{line_number}"] = update_line
