from game_screen import screen
import game_functions as func
import os

next_to_play = func.first_player()
print(next_to_play)


while True:
    print(f'Vez de: {next_to_play["mark"]}')
    func.update_screen()
    option = input('Selecione um número de 1 a 9 para marcar: ')
    print(option)

    if option == '':
        print('Insira um valor válido!')
        continue

    elif option in screen["linha_2"]:
        option_in_line = 2
        linha = func.line_to_list(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option, next_to_play)
        func.update_linha(modified_line, option_in_line)
                
    elif option in screen["linha_5"]:
        option_in_line = 5
        linha = func.line_to_list(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option, next_to_play)
        func.update_linha(modified_line, option_in_line)

    elif option in screen["linha_8"]:
        option_in_line = 8
        linha = func.line_to_list(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option, next_to_play)
        func.update_linha(modified_line, option_in_line)
        
    else:
        os.system('clear')
        print('Insira um valor válido!')
        continue

    next_to_play = func.change_player(next_to_play)
    os.system('clear')
