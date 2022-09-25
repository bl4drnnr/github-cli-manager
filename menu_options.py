import curses
import prints

MENU = [
    'Get organization\'s members\n',
    'Get organization\'s repositories\n',
    'EXIT\n'
]
MENU_LENGTH = len(MENU)
FIRST_OPEN = True


def print_menu(stdscr, current_row_idx):
    global FIRST_OPEN
    stdscr.clear()

    if FIRST_OPEN:
        prints.print_input(stdscr)
        FIRST_OPEN = False

    for idx, row in enumerate(MENU):

        if idx == current_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(row)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(row)

    stdscr.refresh()
