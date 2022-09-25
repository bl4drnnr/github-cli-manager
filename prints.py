import curses

INTRO_LOGO = [
    '-------------------------------------------------------------------------\n',
    '  _________________ ____  _____      __  ______   _  _____  ____________ \n',
    ' / ___/  _/_  __/ // / / / / _ )____/  |/  / _ | / |/ / _ |/ ___/ __/ _ \\\n',
    '/ (_ // /  / / / _  / /_/ / _  /___/ /|_/ / __ |/    / __ / (_ / _// , _/\n',
    '\___/___/ /_/ /_//_/\____/____/   /_/  /_/_/ |_/_/|_/_/ |_\___/___/_/|_| \n',
    '-------------------------------------------------------------------------\n\n'
]


def print_input(stdscr):
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(INTRO_LOGO):
        x = w//2 - len(row)//2
        stdscr.addstr(idx, x, row, curses.color_pair(2))

    stdscr.addstr('GITHUB-MANAGER - is the simple Python terminal-based interactive application \n')
    stdscr.addstr('that allows you use GitHub REST API in order to ')
    stdscr.addstr('read/write/update users/repositories\n', curses.A_UNDERLINE)
    stdscr.addstr('of your private or organization GitHub account.\n\n')

    stdscr.addstr('In order to see manual with documentation start program with --help or -h flag.\n')
    stdscr.addstr('The other way to do that is chose documentation menu after start.\n\n')

    stdscr.addstr('Press any key to start...')
    stdscr.getch()
    stdscr.clear()


def print_exit_text(stdscr):
    stdscr.addstr('It seems you it is enough for now.\n')
    stdscr.addstr('Well, hope you liked it and hope we will see again\n\n')

    stdscr.addstr('It case of any issues, feel free to contact me - ')
    stdscr.addstr('mikhail.bahdashych@protonmail.com\n\n', curses.color_pair(1))

    stdscr.addstr('Print any key to exit...')

    stdscr.getch()
    stdscr.clear()
    exit()


def print_documentation():
    pass
