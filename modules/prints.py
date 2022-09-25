import curses

from modules.docs import docs_description
from modules.send_requests import send_request

INTRO_LOGO = [
    '+-------------------------------------------------------------------------+\n',
    '|  _________________ ____  _____      __  ______   _  _____  ____________ |\n',
    '| / ___/  _/_  __/ // / / / / _ )____/  |/  / _ | / |/ / _ |/ ___/ __/ _ \\|\n',
    '|/ (_ // /  / / / _  / /_/ / _  /___/ /|_/ / __ |/    / __ / (_ / _// , _/|\n',
    '|\___/___/ /_/ /_//_/\____/____/   /_/  /_/_/ |_/_/|_/_/ |_\___/___/_/|_| |\n',
    '+-------------------------------------------------------------------------+\n\n'
]

PAD_CONTENT = []


def print_raw_input(stdscr, prompt_string):
    curses.echo()
    stdscr.addstr(prompt_string)
    stdscr.refresh()
    user_input = stdscr.getstr()
    return user_input.decode('utf-8')


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

        for item, value in docs_description.items():
            pad.addstr(item, curses.color_pair(2))
            for idx, st in enumerate(value['description']):
                if idx == 0:
                    pad.addstr(st, curses.A_BOLD)
                else:
                    pad.addstr(st)

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


def print_command_documentation(stdscr, command):
    print_logo(stdscr, 2)

    selected_command = docs_description[command]
    additional_options = {}

    for item in selected_command['description']:
        stdscr.addstr(item)

    ask_for_token = "TIP: Check Developer Setting at your GitHub account, in order to check, if your token has access to resource\n" \
                    "If something, you want to get, is private, but you have access, please, provide developer token.\n" \
                    "If you want to access public entity, fill the input empty.\n\n" \
                    "Token: "

    token = print_raw_input(stdscr, ask_for_token).lower()

    if '{org}' in selected_command['endpoint']:
        additional_options['{org}'] = print_raw_input(stdscr, 'Provide organization\'s name: ')
    elif '{username}' in selected_command['endpoint']:
        additional_options['{username}'] = print_raw_input(stdscr, 'Provide username: ')
    elif '{owner}' in selected_command['endpoint']:
        additional_options['{owner}'] = print_raw_input(stdscr, 'Provide repository owner: ')
    elif '{repo}' in selected_command['endpoint']:
        additional_options['{repo}'] = print_raw_input(stdscr, 'Provide repository name: ')

    response = send_request(stdscr, token.strip(), selected_command['endpoint'], additional_options)

    stdscr.addstr(str(response))
    stdscr.getch()
