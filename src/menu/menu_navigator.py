import curses
from src.menu.actions import print_documentation, print_exit_text, print_input, print_menu_description, print_command_documentation

MENU = [
    'Get organization\'s members\n',
    'Get organization\'s member by username\n',
    'Get repository\'s collaborators\n',
    'Get repository\'s collaborator by username\n\n',
    'Create a pull request\n',
    'Update a pull request\n',
    'Merge a pull request\n\n',
    'Create a repository\n',
    'Delete a repository\n\n',
    'Documentation\n',
    'Exit\n'
]
MENU_LENGTH = len(MENU)


def print_menu(stdscr, current_row_idx):
    stdscr.clear()

    print_menu_description(stdscr)
    for idx, row in enumerate(MENU):

        if idx == current_row_idx:
            if row == 'Exit\n':
                stdscr.addstr(f' > {row}', curses.color_pair(3))
            else:
                stdscr.addstr(f' > {row}', curses.color_pair(1))
        else:
            if row == 'Exit\n':
                stdscr.addstr(row, curses.color_pair(3))
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
            if MENU[current_row_idx] == 'Exit\n':
                print_exit_text(stdscr)
            elif MENU[current_row_idx] == 'Documentation\n':
                print_documentation(stdscr)
            else:
                print_command_documentation(stdscr, MENU[current_row_idx].split('\n')[0])

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()


def print_introduction(stdscr):
    print_input(stdscr)
