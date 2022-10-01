import curses

from src.api.docs import docs_description
from src.api.fetch_data import send_request

from src.menu.common import INTRO_LOGO, PAD_HEIGHT, PARAM_DICTIONARY


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
    body = {}

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

    parameters_parsed_url = selected_command['endpoint'].split('/')
    for param in parameters_parsed_url:
        if '{' in param:
            for parameter, description in PARAM_DICTIONARY.items():
                if parameter == param:
                    additional_options[param] = print_raw_input(stdscr, description)

    method = selected_command['method']

    set_params = []
    if 'payload' in selected_command:
        for key, value in selected_command['payload'].items():
            set_params.append(key)

    for kind_of_params in set_params:
        if kind_of_params == 'required':
            stdscr.addstr('\nPlease, set all required body parameters in order to continue.\n', curses.A_BOLD)
        elif kind_of_params == 'optional':
            stdscr.addstr('\nSet optional parameters, if you want.\n', curses.A_BOLD)

        for param_to_set in selected_command['payload'][kind_of_params]:
            for param_key, param_value in PARAM_DICTIONARY.items():
                if param_to_set == param_key:
                    body[param_to_set] = print_raw_input(stdscr, param_value)

    response = send_request(stdscr, selected_command['endpoint'], additional_options, method, token.strip(), body)

    if response is not None:

        stdscr.addstr('\nSUCCESS!', curses.color_pair(2) | curses.A_BOLD)
        save_to_file = print_raw_input(stdscr, '\nSeems like we did it. Wanna save result to file (otherwise data just will be printed)? [Y/N]: ')
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
