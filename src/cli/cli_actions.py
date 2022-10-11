import sys

from src.cli.exceptions import NoToken, WrongOption, WrongAttributes
from src.api.docs import docs_description
from src.api.fetch_data import send_request


def isSubArray(A, B, n, m):
    i = 0
    j = 0

    while i < n and j < m:
        if A[i] == B[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            i = i - j + 1
            j = 0

    return False


def cli_execute(operation, options):
    try:
        if 'token' not in options:
            raise NoToken
    except NoToken:
        print('No GitHub developer token set.')
        sys.exit()

    body = {}
    updated_options = {}
    required_options = []
    used_options = []
    query = ''

    for option in options:
        if option != 'token':
            used_options.append(option)
        if option == 'query':
            query = options[option]
        if option == 'pull-number':
            used_options.append('pull_number')

    try:
        if operation == 'gom':
            required_options = ['org']
            selected_operation = docs_description['Get organization\'s members']
        elif operation == 'gomu':
            required_options = ['org', 'username']
            selected_operation = docs_description['Get organization\'s member by username']
        elif operation == 'grc':
            required_options = ['owner', 'repo']
            selected_operation = docs_description['Get repository\'s collaborators']
        elif operation == 'grcu':
            required_options = ['owner', 'repo', 'username']
            selected_operation = docs_description['Get repository\'s collaborator by username']
        elif operation == 'cpr':
            required_options = ['owner', 'repo', 'head', 'base']
            selected_operation = docs_description['Create a pull request']
            body['head'] = options['head']
            body['base'] = options['base']
            del options['head']
            del options['base']
        elif operation == 'upr':
            required_options = ['owner', 'repo', 'pull_number']
            selected_operation = docs_description['Update a pull request']
        elif operation == 'mpr':
            required_options = ['owner', 'repo', 'pull_number']
            selected_operation = docs_description['Merge a pull request']
        elif operation == 'cr':
            required_options = ['name']
            selected_operation = docs_description['Create a repository']
            body['name'] = options['name']
            del options['name']
        elif operation == 'dr':
            required_options = ['owner', 'repo']
            selected_operation = docs_description['Delete a repository']
        elif operation == 'gagt':
            selected_operation = docs_description['Get all gitignore templates']
        elif operation == 'gagtn':
            required_options = ['name']
            selected_operation = docs_description['Get a gitignore template']
        elif operation == 'lrfu':
            required_options = ['username']
            selected_operation = docs_description['List repositories for a user']
        elif operation == 'lor':
            required_options = ['org']
            selected_operation = docs_description['List organization repositories']
        elif operation == 'lofu':
            required_options = ['username']
            selected_operation = docs_description['List organizations for a user']
        else:
            raise WrongOption
        if len(required_options) > 0:
            if not isSubArray(used_options, required_options, len(used_options), len(required_options)):
                raise WrongAttributes

        endpoint = selected_operation['endpoint']
        method = selected_operation['method']
    except WrongOption:
        print('Wrong option.')
        sys.exit()
    except WrongAttributes:
        print('Wrong attributes.')
        print('List of required attributes:', required_options)
        sys.exit()

    for key, option in options.items():
        updated_options['{' + key + '}'] = option

    response = send_request(endpoint, updated_options, method, options['token'], body, query, None)
    print(str(response))
