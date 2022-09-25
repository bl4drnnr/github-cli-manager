import curses

from curses import wrapper

import menu


BASE_URL = 'https://api.github.com/'


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    current_row_idx = 0

    menu.print_menu(stdscr, current_row_idx)

    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < menu.MENU_LENGTH - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            stdscr.clear()
            stdscr.addstr(f'You pressed {menu.MENU[current_row_idx]}')
            stdscr.refresh()
            stdscr.getch()
            if current_row_idx == menu.MENU_LENGTH - 1:
                exit()

        menu.print_menu(stdscr, current_row_idx)
        stdscr.refresh()


if __name__ == '__main__':
    wrapper(main)
