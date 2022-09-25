import curses
import prints

MENU = [
    'Get organization\'s members\n',
    'Get organization\'s repositories\n',
    'Documentation\n',
    'EXIT\n'
]
AVAILABLE_ENDPOINTS = []
MENU_LENGTH = len(MENU)


def print_menu(stdscr, current_row_idx):
    stdscr.clear()

    for idx, row in enumerate(MENU):

        if idx == current_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(f' > {row}')
            stdscr.attroff(curses.color_pair(1))
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
            if current_row_idx == MENU_LENGTH - 1:
                prints.print_exit_text(stdscr)

            stdscr.clear()
            stdscr.addstr(f'You pressed {MENU[current_row_idx]}')
            stdscr.refresh()
            stdscr.getch()

        print_menu(stdscr, current_row_idx)
        stdscr.refresh()


def print_introduction(stdscr):
    prints.print_input(stdscr)
