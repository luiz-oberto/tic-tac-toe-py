import curses

menu = ["Iniciar Jogo", "Opções", "Sair"]

def draw_menu(stdscr, selected):
    stdscr.clear()
    h, w = stdscr.getmaxyx()

    for idx, item in enumerate(menu):
        x = w//2 - len(item)//2
        y = h//2 - len(menu)//2 + idx
        if idx == selected:
            stdscr.addstr(y, x, item, curses.A_REVERSE)
        else:
            stdscr.addstr(y, x, item)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    current_row = 0

    draw_menu(stdscr, current_row)

    while True:
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == ord('\n'):  # Enter
            stdscr.addstr(0, 0, f"Selecionado: {menu[current_row]}")
            stdscr.refresh()
            stdscr.getch()
            if menu[current_row] == "Sair":
                break

        draw_menu(stdscr, current_row)

curses.wrapper(main)


    
'''
    while True:
        stdscr.clear()

        # Desenhar o tabuleiro
        for i in range(3):
            for j in range(3):
                if (i, j) == (y, x):
                    stdscr.addstr(i*2, j*4, "[ ]", curses.A_REVERSE)
                else:
                    stdscr.addstr(i*2, j*4, "[ ]")

        key = stdscr.getch()

        # Sair com a tecla 'q'
        if key == ord('q'):
            break
        elif key == curses.KEY_UP and y > 0:
            y -= 1
        elif key == curses.KEY_DOWN and y < 2:
            y += 1
        elif key == curses.KEY_LEFT and x > 0:
            x -= 1
        elif key == curses.KEY_RIGHT and x < 2:
            x += 1
        elif key == ord(' '):  # espaço para marcar
            # aqui você pode marcar o tabuleiro, ex: board[y][x] = "X"
            pass
'''

