import game_functions as func
import os

next_to_play = func.first_player()
print(next_to_play)


while True:
    print(f'Vez de: {next_to_play["mark"]}')
    func.update_screen()
    option = input('Selecione um número de 1 a 9 para marcar: ')

    if option == '1' or option == '2' or option == '3':
        option_in_line = 2
        linha = func.line_transformer(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option, next_to_play)
        func.update_linha(modified_line, option_in_line)
                
    elif option == '4' or option == '5' or option == '6':
        option_in_line = 5
        linha = func.line_transformer(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option, next_to_play)
        func.update_linha(modified_line, option_in_line)

    elif option == '7' or option == '8' or option == '9':
        option_in_line = 8
        linha = func.line_transformer(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option, next_to_play)
        func.update_linha(modified_line, option_in_line)
        
    else:
        os.system('clear')
        print('Insira um valor válido!')
        continue

    next_to_play = func.change_player(next_to_play)
    os.system('clear')
