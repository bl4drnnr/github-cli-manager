import sys

from curses import wrapper

import menu_options
import init_curses
import args

BASE_URL = 'https://api.github.com/'


def main(stdscr):
    init_curses.init_curses_settings()

    current_row_idx = 0

    menu_options.print_introduction(stdscr)
    menu_options.print_menu(stdscr, current_row_idx)
    menu_options.navigate_menu(stdscr, current_row_idx)


if __name__ == '__main__':
    if len(sys.argv[1:]) == 0:
        wrapper(main)
    else:
        wrapper(args.get_input_args)
