import argparse


def setup_option_parser(argv):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help',
                        action='help',
                        help='Display this message.')
    parser.add_argument('-t', '--token',
                        metavar='',
                        help='GitHub developer token.')
    parser.add_argument('-gom',
                        metavar='',
                        help='List organization members.')
    parser.add_argument('-gomu',
                        metavar='',
                        help='Check organization membership for a user.')
    parser.add_argument('-grc',
                        metavar='',
                        help='List repository collaborators.')
    parser.add_argument('-grcu',
                        metavar='',
                        help='Check if a user is a repository collaborator.')
    parser.add_argument('-cpr',
                        metavar='',
                        help='Draft pull requests are available in public repositories.')
    parser.add_argument('-upr',
                        metavar='',
                        help='Draft pull requests are available in public repositories.')
    parser.add_argument('-mpr',
                        metavar='',
                        help='Merge a pull request.')
    parser.add_argument('-crepo',
                        metavar='',
                        help='Create a new repository for the authenticated user.')
    parser.add_argument('-drepo',
                        metavar='',
                        help='Deleting a repository')
    return parser.parse_args(argv)
