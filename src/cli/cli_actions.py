import sys

from src.cli.exceptions import NoToken, WrongOption, WrongAttributes
from src.api.docs import docs_description
from src.api.fetch_data import send_request


def cli_execute(operation, options):
    try:
        if 'token' not in options:
            raise NoToken
    except NoToken:
        print('No GitHub developer token set.')
        sys.exit()

    body = {}

    try:
        if operation == 'gom':
            if 'org' not in options:
                raise WrongAttributes
            selected_operation = docs_description['Get organization\'s members']
        elif operation == 'gomu':
            if 'org' not in options and 'username' not in options:
                raise WrongAttributes
            selected_operation = docs_description['Get organization\'s member by username']['endpoint']
        elif operation == 'grc':
            if 'owner' not in options and 'repo' not in options:
                raise WrongAttributes
            selected_operation = docs_description['Get repository\'s collaborators']['endpoint']
        elif operation == 'grcu':
            if 'owner' not in options and 'repo' not in options and 'username' not in options:
                raise WrongAttributes
            selected_operation = docs_description['Get repository\'s collaborator by username']['endpoint']
        elif operation == 'cpr':
            if 'owner' not in options and 'repo' not in options:
                raise WrongAttributes
            selected_operation = docs_description['Create a pull request']['endpoint']
        elif operation == 'upr':
            if 'owner' not in options and 'repo' not in options and 'pull-number' not in options:
                raise WrongAttributes
            selected_operation = docs_description['Update a pull request']['endpoint']
        elif operation == 'mpr':
            if 'owner' not in options and 'repo' not in options and 'pull-number' not in options:
                raise WrongAttributes
            selected_operation = docs_description['Merge a pull request']['endpoint']
        elif operation == 'cr':
            selected_operation = docs_description['Create a repository']['endpoint']
        elif operation == 'dr':
            selected_operation = docs_description['Delete a repository']['endpoint']
        else:
            raise WrongOption
        endpoint = selected_operation['endpoint']
        method = selected_operation['method']
    except WrongOption:
        print('Wrong option.')
        sys.exit()
    except WrongAttributes:
        print('Wrong attributes.')
        sys.exit()

    response = send_request(endpoint, options, method, options['token'], body, None)
    print(str(response))
