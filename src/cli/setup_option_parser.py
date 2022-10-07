import argparse


def setup_option_parser(argv):
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help',
                        action='help',
                        help='Display this message.')
    return parser.parse_args(argv)
