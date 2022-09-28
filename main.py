from curses import wrapper

from src.menu.menu_navigator import print_introduction, print_menu, navigate_menu
from src.curses_settings.init_curses import init_curses


def main(stdscr):
    init_curses()

    current_row_idx = 0

    print_introduction(stdscr)
    print_menu(stdscr, current_row_idx)
    navigate_menu(stdscr, current_row_idx)


if __name__ == '__main__':
    wrapper(main)
