import curses

from src.api.docs import docs_description
from src.api.fetch_data import send_request

INTRO_LOGO = [
    '+-------------------------------------------------------------------------+\n',
    '|  _________________ ____  _____      __  ______   _  _____  ____________ |\n',
    '| / ___/  _/_  __/ // / / / / _ )____/  |/  / _ | / |/ / _ |/ ___/ __/ _ \\|\n',
    '|/ (_ // /  / / / _  / /_/ / _  /___/ /|_/ / __ |/    / __ / (_ / _// , _/|\n',
    '|\___/___/ /_/ /_//_/\____/____/   /_/  /_/_/ |_/_/|_/_/ |_\___/___/_/|_| |\n',
    '+-------------------------------------------------------------------------+\n\n'
]

PAD_HEIGHT = 32767


def pad_refresh(pad, pad_pos, height, width):
    pad.refresh(pad_pos, 0, 0, 0, height - 1, width)


def movement_control(pad, pad_pos, height, width):
    pad_refresh(pad, pad_pos, height, width)

    key_up, key_down = 'AB'
    y = 0

    for c in iter(pad.getkey, 'q'):
        if c in '\x1b\x5b':
            continue
        y -= (c == key_up)
        y += (c == key_down)
        pad_refresh(pad, y, height, width)


def print_raw_input(stdscr, prompt_string):
    curses.echo()
    stdscr.addstr(prompt_string, curses.A_BOLD)
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
    pad_pos = 0
    pad = curses.newpad(PAD_HEIGHT, width)

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

    pad.addstr('\nReference: https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps\n\n', curses.color_pair(1))

    pad.addstr('In case of any issues fell free to ask any questions - ')
    pad.addstr('mikhail.bahdashych@prontonmail.com', curses.color_pair(1))

    pad.addstr('\n\nPress Q to get back...')
    movement_control(pad, pad_pos, height, width)


def print_command_documentation(stdscr, command):
    print_logo(stdscr, 2)

    selected_command = docs_description[command]
    additional_options = {}

    for idx, item in enumerate(selected_command['description']):
        if idx == 0:
            stdscr.addstr(item, curses.color_pair(2) | curses.A_BOLD)
        else:
            stdscr.addstr(item)

    stdscr.addstr('TIP: ', curses.A_BOLD)
    stdscr.addstr('Check Developer Setting at your GitHub account, in order to check, if your token has access to resource.\n')
    stdscr.addstr('If something, you want to get, is private, but you have access, please, provide developer token.\n')
    stdscr.addstr('If you want to access public entity, fill the input empty.\n\n')

    token = print_raw_input(stdscr, "Token: ")

    if '{org}' in selected_command['endpoint']:
        additional_options['{org}'] = print_raw_input(stdscr, 'Provide organization\'s name: ')
    if '{username}' in selected_command['endpoint']:
        additional_options['{username}'] = print_raw_input(stdscr, 'Provide username: ')
    if '{owner}' in selected_command['endpoint']:
        additional_options['{owner}'] = print_raw_input(stdscr, 'Provide repository owner: ')
    if '{repo}' in selected_command['endpoint']:
        additional_options['{repo}'] = print_raw_input(stdscr, 'Provide repository name: ')

    response = send_request(stdscr, token.strip(), selected_command['endpoint'], additional_options)

    if response is not None:

        stdscr.addstr('\nSUCCESS!', curses.color_pair(2) | curses.A_BOLD)
        save_to_file = print_raw_input(stdscr, '\nSeems like we have data. Wanna save to file (otherwise data just will be printed)? [Y/N]: ')
        save_to_file = save_to_file.strip()

        if save_to_file == 'y' or save_to_file == 'Y':
            stdscr.addstr('\nDon\'t provide file format, only, it will be provided automatically as .txt.\n')
            file_name = print_raw_input(stdscr, 'Provide file name: ')
            f = open(f'{file_name.strip()}.txt', 'w')
            f.write(str(response))
            f.close()
            stdscr.addstr('\nDone! Data has been written successfully!', curses.color_pair(2))
        else:
            height, width = stdscr.getmaxyx()
            pad_pos = 0
            pad = curses.newpad(PAD_HEIGHT, width)

            print_logo(pad, 5)

            stdscr.addstr(str(response))

            movement_control(pad, pad_pos, height, width)

    stdscr.addstr('\n\nPress any key to get back to menu...\n', curses.color_pair(4))
    stdscr.getch()
