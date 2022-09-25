from curses import wrapper

from modules.menu_options import print_introduction, print_menu, navigate_menu
from modules.init_curses import init_curses_settings

BASE_URL = 'https://api.github.com/'


def main(stdscr):
    init_curses_settings()

    current_row_idx = 0

    print_introduction(stdscr)
    print_menu(stdscr, current_row_idx)
    navigate_menu(stdscr, current_row_idx)


if __name__ == '__main__':
    wrapper(main)
