import curses

INTRO_LOGO = [
    '+-------------------------------------------------------------------------+\n',
    '|  _________________ ____  _____      __  ______   _  _____  ____________ |\n',
    '| / ___/  _/_  __/ // / / / / _ )____/  |/  / _ | / |/ / _ |/ ___/ __/ _ \\|\n',
    '|/ (_ // /  / / / _  / /_/ / _  /___/ /|_/ / __ |/    / __ / (_ / _// , _/|\n',
    '|\___/___/ /_/ /_//_/\____/____/   /_/  /_/_/ |_/_/|_/_/ |_\___/___/_/|_| |\n',
    '+-------------------------------------------------------------------------+\n\n'
]


def print_logo(stdscr, color_pair_id):
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(INTRO_LOGO):
        x = w // 2 - len(row) // 2
        stdscr.addstr(idx, x, row, curses.color_pair(color_pair_id))


def print_input(stdscr):
    print_logo(stdscr, 2)

    stdscr.addstr('GITHUB-MANAGER - is the simple Python terminal-based interactive application \n')
    stdscr.addstr('that allows you use GitHub REST API in order to ')
    stdscr.addstr('read/write/update users/repositories\n', curses.A_UNDERLINE)
    stdscr.addstr('of your private or organization GitHub account.\n\n')

    stdscr.addstr('In order to see manual with documentation choose Documentation menu after start.\n\n')

    stdscr.addstr('Press any key to start...')

    stdscr.getch()
    stdscr.clear()


def print_exit_text(stdscr):
    print_logo(stdscr, 4)

    stdscr.addstr('It seems you it is enough for now.\n', curses.color_pair(4))
    stdscr.addstr('Well, hope you liked it and hope we will see again\n\n', curses.color_pair(4))

    stdscr.addstr('It case of any issues, feel free to contact me - ', curses.color_pair(4))
    stdscr.addstr('mikhail.bahdashych@protonmail.com\n\n', curses.color_pair(1))

    stdscr.addstr('Press any key to exit...', curses.color_pair(4))

    stdscr.getch()
    stdscr.clear()
    exit()


def print_menu_description(stdscr):
    print_logo(stdscr, 2)
    stdscr.addstr('So, what are we gonna do now?\n\n\n', curses.color_pair(1))


def print_documentation(stdscr):
    print_logo(stdscr, 5)

    stdscr.addstr('DOCUMENTATION\n\n', curses.A_BOLD)
    stdscr.addstr('GitHub manager - being Python written terminal-based interactive application - provides users with\n', curses.A_BOLD)
    stdscr.addstr('very simple opportunity to manage GitHub REST API using interactive shell\n\n', curses.A_BOLD)

    stdscr.addstr('Below will be listed description to every possible menu option (basically, just GitHub REST API endpoint) of application.\n\n')

    stdscr.addstr('Get organization\'s members', curses.color_pair(2))
    stdscr.addstr(' - GET /orgs/{org}/members - List organization members\n', curses.A_BOLD)
    stdscr.addstr('List all users who are members of an organization. If the authenticated user is also a member of this organization\n')
    stdscr.addstr('then both concealed and public members will be returned.\n\n')

    stdscr.addstr('Get organization\'s member', curses.color_pair(2))
    stdscr.addstr(' - GET /orgs/{org}/members/{username} - Check organization membership for a user\n', curses.A_BOLD)
    stdscr.addstr('Check if a user is, publicly or privately, a member of the organization.\n\n')

    stdscr.addstr('Get repository\'s collaborators', curses.color_pair(2))
    stdscr.addstr(' - GET /repos/{owner}/{repo}/collaborators - List repository collaborators\n', curses.A_BOLD)
    stdscr.addstr('For organization-owned repositories, the list of collaborators includes outside\n')
    stdscr.addstr('collaborators, organization members that are direct collaborators, organization\n')
    stdscr.addstr('members with access through team memberships, organization members with\n')
    stdscr.addstr('access through default organization permissions, and organization owners.\n\n')

    stdscr.addstr('Get repository\'s collaborator by username', curses.color_pair(2))
    stdscr.addstr(' - GET /repos/{owner}/{repo}/collaborators/{username} - Check if a user is a repository collaborator\n', curses.A_BOLD)
    stdscr.addstr('For organization-owned repositories, the list of collaborators includes outside\n')
    stdscr.addstr('collaborators, organization members that are direct collaborators, organization\n')
    stdscr.addstr('members with access through team memberships, organization members with\n')
    stdscr.addstr('access through default organization permissions, and organization owners.\n\n')

    stdscr.addstr('\nReference: https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps', curses.color_pair(1))

    stdscr.addstr('\n\nPress any key to continue...')

    stdscr.getch()
    stdscr.clear()
