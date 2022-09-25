import curses

INTRO_LOGO = [
    '+-------------------------------------------------------------------------+\n',
    '|  _________________ ____  _____      __  ______   _  _____  ____________ |\n',
    '| / ___/  _/_  __/ // / / / / _ )____/  |/  / _ | / |/ / _ |/ ___/ __/ _ \\|\n',
    '|/ (_ // /  / / / _  / /_/ / _  /___/ /|_/ / __ |/    / __ / (_ / _// , _/|\n',
    '|\___/___/ /_/ /_//_/\____/____/   /_/  /_/_/ |_/_/|_/_/ |_\___/___/_/|_| |\n',
    '+-------------------------------------------------------------------------+\n\n'
]

PAD_CONTENT = []


def print_logo(stdscr, color_pair_id):
    h, w = stdscr.getmaxyx()

    for idx, row in enumerate(INTRO_LOGO):
        x = w // 2 - len(row) // 2
        stdscr.addstr(idx, x, row, curses.color_pair(color_pair_id))


def print_input(stdscr):
    print_logo(stdscr, 2)

    stdscr.addstr('GITHUB-MANAGER - is the simple Python terminal-based interactive application \n')
    stdscr.addstr('that allows you to use GitHub REST API in order to ')
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
    height, width = stdscr.getmaxyx()

    pad_height = 32767

    pad = curses.newpad(pad_height, width)
    pad.scrollok(True)
    pad_pos = 0
    pad_refresh = lambda: pad.refresh(pad_pos + 2, 0, 0, 0, height - 1, width)
    pad_refresh()

    try:
        print_logo(pad, 5)

        pad.addstr('DOCUMENTATION\n\n', curses.A_BOLD)
        pad.addstr('GitHub manager - being Python written terminal-based interactive application - provides users with\n', curses.A_BOLD)
        pad.addstr('very simple opportunity to manage GitHub REST API using interactive shell\n\n', curses.A_BOLD)

        pad.addstr('Below will be listed description to every possible menu option (basically, just GitHub REST API endpoint) of application.\n\n')

        pad.addstr('Get organization\'s members', curses.color_pair(2))
        pad.addstr(' - GET /orgs/{org}/members - List organization members\n', curses.A_BOLD)
        pad.addstr('List all users who are members of an organization. If the authenticated user is also a member of this organization\n')
        pad.addstr('then both concealed and public members will be returned.\n\n')

        pad.addstr('Get organization\'s member', curses.color_pair(2))
        pad.addstr(' - GET /orgs/{org}/members/{username} - Check organization membership for a user\n', curses.A_BOLD)
        pad.addstr('Check if a user is, publicly or privately, a member of the organization.\n\n')

        pad.addstr('Get repository\'s collaborators', curses.color_pair(2))
        pad.addstr(' - GET /repos/{owner}/{repo}/collaborators - List repository collaborators\n', curses.A_BOLD)
        pad.addstr('For organization-owned repositories, the list of collaborators includes outside\n')
        pad.addstr('collaborators, organization members that are direct collaborators, organization\n')
        pad.addstr('members with access through team memberships, organization members with\n')
        pad.addstr('access through default organization permissions, and organization owners.\n\n')

        pad.addstr('Get repository\'s collaborator by username', curses.color_pair(2))
        pad.addstr(' - GET /repos/{owner}/{repo}/collaborators/{username} - Check if a user is a repository collaborator\n', curses.A_BOLD)
        pad.addstr('For organization-owned repositories, the list of collaborators includes outside\n')
        pad.addstr('collaborators, organization members that are direct collaborators, organization\n')
        pad.addstr('members with access through team memberships, organization members with\n')
        pad.addstr('access through default organization permissions, and organization owners.\n\n')

        pad.addstr('\nReference: https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps', curses.color_pair(1))

        pad.addstr('\n\nPress ENTER to continue...')

        running = True
        while running:
            key = stdscr.getch()
            if key == curses.KEY_DOWN and pad_pos < pad.getyx()[0] - height - 1:
                pad_pos += 1
                pad_refresh()
            elif key == curses.KEY_UP and pad_pos > -2:
                pad_pos -= 1
                pad_refresh()
            elif key == curses.KEY_ENTER or key in [10, 13]:
                running = False
    except KeyboardInterrupt:
        pass

    for i in range(0, pad.getyx()[0]):
        PAD_CONTENT.append(pad.instr(i, 0))
