import argparse


def setup_option_parser(argv):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        action='help',
                        help='Display this message.')
    parser.add_argument('--token',
                        help='GitHub developer token.')
    parser.add_argument('--gom',
                        help='List organization members.')
    parser.add_argument('--gomu',
                        help='Check organization membership for a user.')
    parser.add_argument('--grc',
                        help='List repository collaborators.')
    parser.add_argument('--grcu',
                        help='Check if a user is a repository collaborator.')
    parser.add_argument('--cpr',
                        help='Draft pull requests are available in public repositories.')
    parser.add_argument('--upr',
                        help='Draft pull requests are available in public repositories.')
    parser.add_argument('--mpr',
                        help='Merge a pull request.')
    parser.add_argument('--crepo',
                        help='Create a new repository for the authenticated user.')
    parser.add_argument('--drepo',
                        help='Deleting a repository')
    return parser.parse_args(argv)
