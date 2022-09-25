import curses


def print_flags_error(stdscr):
    stdscr.addstr('ERROR!ERROR!ERROR!ERROR!ERROR!\n', curses.color_pair(3))
    stdscr.addstr('Wrong flag has been provided, please, see -h or --help in order to see manual with documentation.\n', curses.color_pair(3))
    stdscr.addstr('ERROR!ERROR!ERROR!ERROR!ERROR!\n\n', curses.color_pair(3))

    stdscr.addstr('Print any key to exit...')

    stdscr.getch()
    stdscr.clear()
    exit()
