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
    parser.add_argument('-d', '--head',
                        metavar='',
                        help='Head branch.')
    parser.add_argument('-b', '--base',
                        metavar='',
                        help='Base branch.')
    parser.add_argument('-n', '--name',
                        metavar='',
                        help='Name of repository.')
    parser.add_argument('-q', '--query',
                        metavar='',
                        help='Query. (Example: --query=?type=all&sort=updated)')
    parser.add_argument('-h', '--help',
                        action='help',
                        help='Display this message.')
    parser.add_argument('--gom',
                        help='Get organization\'s members.',
                        action='store_true')
    parser.add_argument('--gomu',
                        help='Get organization\'s member by username.',
                        action='store_true')
    parser.add_argument('--grc',
                        help='Get repository\'s collaborators.',
                        action='store_true')
    parser.add_argument('--grcu',
                        help='Get repository\'s collaborator by username.',
                        action='store_true')
    parser.add_argument('--cpr',
                        help='Create a pull request.',
                        action='store_true')
    parser.add_argument('--upr',
                        help='Update a pull request.',
                        action='store_true')
    parser.add_argument('--mpr',
                        help='Merge a pull request.',
                        action='store_true')
    parser.add_argument('--cr',
                        help='Create a repository.',
                        action='store_true')
    parser.add_argument('--dr',
                        help='Deleting a repository.',
                        action='store_true')
    parser.add_argument('--gagt',
                        help='Get all gitignore templates.',
                        action='store_true')
    parser.add_argument('--gagtn',
                        help='Get a gitignore template.',
                        action='store_true')
    parser.add_argument('--lrfu',
                        help='Lists public repositories for the specified user.',
                        action='store_true')
    parser.add_argument('--lor',
                        help='Lists repositories for the specified organization.',
                        action='store_true')
    return parser.parse_args(argv)
