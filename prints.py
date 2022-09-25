import curses


def print_input(stdscr):
    stdscr.addstr('-------------------------------------------------------------------------\n')
    stdscr.addstr('  _________________ ____  _____      __  ______   _  _____  ____________ \n')
    stdscr.addstr(' / ___/  _/_  __/ // / / / / _ )____/  |/  / _ | / |/ / _ |/ ___/ __/ _ \\\n')
    stdscr.addstr('/ (_ // /  / / / _  / /_/ / _  /___/ /|_/ / __ |/    / __ / (_ / _// , _/\n')
    stdscr.addstr('\___/___/ /_/ /_//_/\____/____/   /_/  /_/_/ |_/_/|_/_/ |_\___/___/_/|_| \n')
    stdscr.addstr('-------------------------------------------------------------------------\n\n')

    stdscr.addstr('GITHUB-MANAGER - is the simple Python terminal-based interactive application \n')
    stdscr.addstr('that allows you use GitHub REST API in order to ')
    stdscr.addstr('read/write/update users/repositories\n', curses.A_UNDERLINE)
    stdscr.addstr('of your private or organization GitHub account.\n\n')

    stdscr.addstr('In order to see manual with documentation start program with --help or -h flag.\n')
    stdscr.addstr('The other way to do that is chose documentation menu after start.\n\n')

    stdscr.addstr('Press any key to start...')
    stdscr.getch()
    stdscr.clear()


def print_documentation():
    pass
