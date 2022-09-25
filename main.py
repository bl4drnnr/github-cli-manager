from curses import wrapper

import menu_options
import init_curses

BASE_URL = 'https://api.github.com/'


def main(stdscr):
    init_curses.init_curses_settings()

    current_row_idx = 0

    menu_options.print_introduction(stdscr)
    menu_options.print_menu(stdscr, current_row_idx)
    menu_options.navigate_menu(stdscr, current_row_idx)


if __name__ == '__main__':
    wrapper(main)
