import argparse

from commands.article import article, summary
from commands.revision import revision_feed
from commands.search import search


def main():
    
    parser = argparse.ArgumentParser(
        description="Wikipedia CLI",
        epilog="'wiki <command> -h' for help on specific commands",
        prog="wiki")

    subparsers = parser.add_subparsers(
        dest="command",
        required=True)

    # article subcommand
    article_parser = subparsers.add_parser(
        'article',
        help="get article")

    article_flags = article_parser.add_mutually_exclusive_group()

    article_flags.add_argument(
        '-s', '--summary',
        help="get short summary instead of entire page",
        action='store_true',
        default=False)

    article_flags.add_argument(
        '-r', '--revision',
        help="get live revision feed of article",
        action='store_true',
        default=False)
    
    article_parser.add_argument(
        '-w', '--width',
        help="set maximum width of output (default: no limit)",
        type=int,
        default=0) # redundant with fill_width but keep for consistency

    article_parser.add_argument(
        'title',
        help="title of article")

    # search subcommand
    search_parser = subparsers.add_parser(
        'search',
        help="search for relevant articles")

    search_flags = search_parser.add_mutually_exclusive_group()
    search_flags.add_argument(
        '-n', '--results',
        help="number of results to return (default: 10)",
        metavar='NUM',
        type=int,
        default=10) # redundant but keep for consistency


    search_parser.add_argument(
        'title',
        help="title of article")

    args = parser.parse_args()

    # print(args)

    if args.command == 'article':

        if args.summary:

            summary(args.title, args.width)

        elif args.revision:

            revision_feed(args.title)

        else:

            article(args.title, args.width)

    elif args.command == 'search':

        search(args.title, args.results)

main()
