import curses
from screen import screen

# print(screen)
def desenha_tabuleiro(stdscr, screen_dict):
    stdscr.clear()
    y = 0
    for linha in screen_dict.values():
        print(linha)
        stdscr.addstr(y, 0, linha)
        y += 1

    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)
    desenha_tabuleiro(stdscr, screen)
    stdscr.getch()


curses.wrapper(main)
