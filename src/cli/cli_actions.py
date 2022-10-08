import sys

from src.cli.exceptions import NoToken, WrongOption


def cli_execute(operation, options):
    try:
        if 'token' not in options:
            raise NoToken
    except NoToken:
        print('No GitHub developer token set.')
        sys.exit()

    try:
        if operation == 'gom':
            pass
        elif operation == 'gomu':
            pass
        elif operation == 'grc':
            pass
        elif operation == 'grcu':
            pass
        elif operation == 'cpr':
            pass
        elif operation == 'upr':
            pass
        elif operation == 'mpr':
            pass
        elif operation == 'cr':
            pass
        elif operation == 'dr':
            pass
        else:
            raise WrongOption
    except WrongOption:
        print('Wrong option.')
        sys.exit()
