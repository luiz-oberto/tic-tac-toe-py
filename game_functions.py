'''
Functions for the tic-tac-toe game.
- need to implement the verifier of game over(end game) 
'''
from game_screen import screen
from time import sleep
import random
import os


players = [{"player": "1", "mark": "X"}, {"player": "2", "mark": "O"}]

# random choice between the players to decide who will begin the game
def first_player():
    os.system('clear')
    
    for i in range(3):
        os.system('clear')
        print('escolhendo o primeiro a jogar.')
        sleep(0.3)
        os.system('clear')        
        print('escolhendo o primeiro a jogar..')
        sleep(0.3)
        os.system('clear')
        print('escolhendo o primeiro a jogar...')
        sleep(0.3)
        os.system('clear')
        print('escolhendo o primeiro a jogar....')
        sleep(0.3)
        os.system('clear')
        print('escolhendo o primeiro a jogar.....')
        sleep(0.3)
        os.system('clear')

    first = random.choice(players)
    
    return first


# change the player each turn
def change_player(player):
    try:
    
        if player["player"] == "1":
            next_to_play = players[1]
            
        elif player["player"] == "2":
            next_to_play = players[0]
            
        return next_to_play

    except valueError as e:
        raise e 


# transform the line into a list to change the values
def line_to_list(line, player_option):
    line_copy = screen[f"linha_{line}"]
    line_split = line_copy.split()
    separador = '  '

    for i in range(0, len(line_split)+6, 2):
        line_split.insert(i, separador)

    return line_split

# do the mark of the player in the square selected (X or O)
def mark_one(line_number, line, player_option, player): # parametro: player = "X" ou "O"    
    if line_number == 2:
        for i in line:
            match player_option:
                case '1':
                    line[1] = player["mark"]

                case '2':
                    line[5] = player["mark"]

                case '3':
                    line[9] = player["mark"]

    elif line_number == 5:
        for i in line:
            match player_option:
                case '4':
                    line[1] = player["mark"]

                case '5':
                    line[5] = player["mark"]

                case '6':
                    line[9] = player["mark"]

    elif line_number == 8:
        for i in line:
            match player_option:
                case '7':
                    line[1] = player["mark"]

                case '8':
                    line[5] = player["mark"]

                case '9':
                    line[9] = player["mark"]

    return line

# update the game with the line changed
def update_linha(line_to_update: list, line_number):
    update_line = ''
    for i in line_to_update:
        update_line += i
    screen[f"linha_{line_number}"] = update_line

# update the game screen
def update_screen():
    for i in range(1, len(screen)+1):
        print(screen[f"linha_{i}"])
