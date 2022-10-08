import argparse


def setup_option_parser(argv):
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument('token', help='GitHub developer token.')

    parser.add_argument('-o', '--org',
                        metavar='',
                        help='Organization name.')
    parser.add_argument('-u', '--username',
                        metavar='',
                        help='Username.')
    parser.add_argument('-own', '--owner',
                        metavar='',
                        help='Owner.')
    parser.add_argument('-r', '--repo',
                        metavar='',
                        help='Repository.')
    parser.add_argument('-p', '--pull-number',
                        metavar='',
                        help='Pull number.')
    parser.add_argument('-h', '--help',
                        action='help',
                        help='Display this message.')
    parser.add_argument('--gom',
                        metavar='',
                        help='Get organization\'s members.')
    parser.add_argument('--gomu',
                        metavar='',
                        help='Get organization\'s member by username.')
    parser.add_argument('--grc',
                        metavar='',
                        help='Get repository\'s collaborators.')
    parser.add_argument('--grcu',
                        metavar='',
                        help='CheckGet repository\'s collaborator by username.')
    parser.add_argument('--cpr',
                        metavar='',
                        help='Create a pull request.')
    parser.add_argument('--upr',
                        metavar='',
                        help='Update a pull request.')
    parser.add_argument('--mpr',
                        metavar='',
                        help='Merge a pull request.')
    parser.add_argument('--cr',
                        metavar='',
                        help='Create a repository.')
    parser.add_argument('--dr',
                        metavar='',
                        help='Deleting a repository')
    return parser.parse_args(argv)
