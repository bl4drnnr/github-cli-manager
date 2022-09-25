import getopt
import sys

import prints
import errors
import init_curses


def get_input_args(stdscr):
    init_curses.init_curses_settings()

    flags = sys.argv[1:]
    short_flags = 'h'
    long_flags = ['help']

    try:
        opts, args = getopt.getopt(flags, short_flags, long_flags)
        for o, a in opts:
            if o in ('-h', '--help'):
                prints.print_documentation()
            else:
                errors.print_flags_error(stdscr)
    except getopt.GetoptError:
        errors.print_flags_error(stdscr)
