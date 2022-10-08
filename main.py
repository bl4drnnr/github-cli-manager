import sys

from curses import wrapper

from src.menu.menu_navigator import print_introduction, print_menu, navigate_menu
from src.curses_settings.init_curses import init_curses

from src.cli.setup_option_parser import setup_option_parser
from src.cli.exceptions import SingleArgument
from src.cli.cli_actions import cli_execute

_AVAILABLE_OPTIONS = ['gom', 'gomu', 'grc', 'grcu', 'cpr', 'upr', 'mpr', 'cr', 'dr']


def cli(argv):
    options = setup_option_parser(argv)
    operation = []
    set_options = {}

    for i in options.__dict__:
        if options.__dict__[i] is not None:
            if i in _AVAILABLE_OPTIONS:
                operation.append(i)
            else:
                set_options[i] = options.__dict__[i]

    try:
        if len(operation) != 1:
            raise SingleArgument
    except SingleArgument:
        print('One operation argument is expected.')
        sys.exit()

    cli_execute(operation[0], set_options)


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
