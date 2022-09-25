import curses
import prints

MENU = [
    'Get organization\'s members\n',
    'Get organization\'s repositories\n',
    # 'Documentation\n'
    'EXIT\n'
]
MENU_LENGTH = len(MENU)


def print_menu(stdscr, current_row_idx):
    stdscr.clear()

    for idx, row in enumerate(MENU):

        if idx == current_row_idx:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(f' {chr(int("25B6", 16))} {row}')
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(row)

    stdscr.refresh()


def print_introduction(stdscr):
    prints.print_input(stdscr)
