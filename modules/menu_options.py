import curses
from modules.prints import print_documentation, print_exit_text, print_input, print_menu_description

MENU = [
    'Get organization\'s members\n',
    'Get organization\'s member by username\n',
    'Get repository\'s collaborators\n',
    'Get repository\'s collaborator by username\n\n',
    'Documentation\n',
    'Exit\n'
]
AVAILABLE_ENDPOINTS = []
MENU_LENGTH = len(MENU)


def print_menu(stdscr, current_row_idx):
    stdscr.clear()

    print_menu_description(stdscr)
    for idx, row in enumerate(MENU):

        if idx == current_row_idx:
            stdscr.addstr(f' > {row}', curses.color_pair(1))
        else:
            stdscr.addstr(row)

    stdscr.refresh()


def navigate_menu(stdscr, current_row_idx):
    while True:
        key = stdscr.getch()
        stdscr.clear()

        if key == curses.KEY_UP and current_row_idx > 0:
            current_row_idx -= 1
        elif key == curses.KEY_DOWN and current_row_idx < MENU_LENGTH - 1:
            current_row_idx += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if MENU[current_row_idx] == 'Get organization\'s members\n':
                pass
            elif MENU[current_row_idx] == 'Get organization\'s repositories\n':
                pass
            elif MENU[current_row_idx] == 'Documentation\n':
                print_documentation(stdscr)
            elif MENU[current_row_idx] == 'EXIT\n':
                print_exit_text(stdscr)
            else:
                print_exit_text(stdscr)

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()


def print_introduction(stdscr):
    print_input(stdscr)
