import os
import game_functions as func

os.system('clear')

while True:
    func.update_screen()
    option = input('Selecione um número de 1 a 9 para jogar. ')

    if option == '1' or option == '2' or option == '3':
        option_in_line = 2
        linha = func.line_transformer(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option)
        func.update_linha(modified_line, option_in_line)
        
        os.system('clear')
        
    elif option == '4' or option == '5' or option == '6':
        option_in_line = 5
        linha = func.line_transformer(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option)
        func.update_linha(modified_line, option_in_line)
        
        os.system('clear')

    elif option == '7' or option == '8' or option == '9':
        option_in_line = 8
        linha = func.line_transformer(option_in_line, option)
        modified_line = func.mark_one(option_in_line, linha, option)
        func.update_linha(modified_line, option_in_line)
        
        os.system('clear')
        
    else:
        os.system('clear')        
        print('Insira um valor válido!')
    

