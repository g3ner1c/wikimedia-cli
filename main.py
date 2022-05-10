import argparse

from commands.article import article
from commands.revision import revision_feed
from commands.search import search
from commands.util import *


def main():

    parser = argparse.ArgumentParser(
        description="Wikipedia CLI",
        epilog="'wiki <command> -h' for help on specific commands",
        prog="wiki")

    subparsers = parser.add_subparsers(
        dest="command",
        required=True)

    #* === common arguments ===
    common_args = argparse.ArgumentParser(add_help=False)
    common_args.add_argument(
        'title',
        help="title of article",
        type=str)

    common_args.add_argument(
        '-l', '--lang',
        help="ISO 639-1 language code of Wikipedia to use (default: en)",
        type=str,
        default="en") #* change this to set default language 
    # ==========================


    #* === article command ===
    article_parser = subparsers.add_parser(
        'article',
        help="get articles",
        parents=[common_args])

    # == article subcommand modes ==
    article_flags = article_parser.add_mutually_exclusive_group()
    article_flags.add_argument(
        '-s', '--summary',
        help="get short summary instead of entire page",
        action='store_true',
        default=False)
    # ==============================

    article_parser.add_argument(
        '-w', '--width',
        help="set maximum width of output (default: 80)",
        type=int,
        default=80) # redundant with fill_width but keep for consistency

    article_parser.add_argument(
        '-u', '--url',
        help="print url to article after output",
        action='store_true',
        default=False)


    #* === search command ===
    search_parser = subparsers.add_parser(
        'search',
        help="search for articles",
        parents=[common_args])

    search_parser.add_argument(
        '-n', '--results',
        help="number of results to return (default: 10)",
        metavar='NUM',
        type=int,
        default=10) # redundant but keep for consistency

    
    #* === revision command ===
    revision_parser = subparsers.add_parser(
        'revision',
        help="view revision history and live revisions of articles",
        parents=[common_args])

    # == revision subcommand modes ==
    revision_flags = revision_parser.add_mutually_exclusive_group()
    revision_flags.add_argument(
        '-f', '--feed',
        help="view live revision feed",
        action='store_true',
        default=False)
    # ===============================

    args = parser.parse_args()

    # print(args)

    if args.command == 'article':

        print(article(args.title, args.width, args.summary, args.lang))

        if args.url:

            print("\n{}".format(
                request({
                    'prop': 'info',
                    'inprop': 'url',
                    'titles': args.title,
                }, args.lang)['query']['pages'][0]['fullurl']
            ))

    elif args.command == 'search':

        for title in search(args.title, args.results, args.lang):
            print(title)

    elif args.command == 'revision':

        if args.feed:

            revision_feed(args.title)

main()
