import sys

from curses import wrapper

from src.menu.menu_navigator import print_introduction, print_menu, navigate_menu
from src.curses_settings.init_curses import init_curses

from src.cli.setup_option_parser import setup_option_parser


def cli(argv):
    options = setup_option_parser(argv)


def interactive_cli(stdscr):
    init_curses()

    current_row_idx = 0

    print_introduction(stdscr)
    print_menu(stdscr, current_row_idx)
    navigate_menu(stdscr, current_row_idx)


def main(argv):
    if len(argv) > 0:
        cli(argv)
    else:
        wrapper(interactive_cli)


if __name__ == '__main__':
    main(sys.argv[1:])
