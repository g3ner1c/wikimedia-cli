import argparse

from commands.article import article, title_print
from commands.revision import revision_feed
from commands.search import search
from commands.util import *


def main():

    parser = argparse.ArgumentParser(
        description="Wikimedia CLI",
        epilog="'wiki <command> -h' for help on specific commands",
        prog="wiki")

    subparsers = parser.add_subparsers(
        dest="command",
        required=True)

    wikipedia = subparsers.add_parser(
        'pedia',
        help="get articles from wikipedia",
        description="get articles from wikipedia",
        epilog="'wiki pedia <command> -h' for help on specific commands").add_subparsers(
        dest="subcommand",
        required=True)

    #* === wikipedia common arguments ===
    pedia_common_args = argparse.ArgumentParser(add_help=False)
    pedia_common_args.add_argument(
        'title',
        help="title of article",
        type=str)

    pedia_common_args.add_argument(
        '-l', '--lang',
        help="ISO 639-1 language code of Wikipedia to use (default: en)",
        type=str,
        default="en") #* change this to set default language


    #* === article command ===
    article_parser = wikipedia.add_parser(
        'article',
        help="get articles",
        description="get articles",
        parents=[pedia_common_args])

    article_parser.add_argument(
        '-s', '--summary',
        help="get short summary instead of entire page, sets --no-title",
        action='store_true',
        default=False)

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

    article_parser.add_argument(
        '--no-title',
        help="don't print title",
        action='store_true',
        default=False)


    #* === search command ===
    search_parser = wikipedia.add_parser(
        'search',
        help="search for articles",
        description="search for articles",
        parents=[pedia_common_args])

    search_parser.add_argument(
        '-n', '--results',
        help="number of results to return (default: 10)",
        metavar='NUM',
        type=int,
        default=10) # redundant but keep for consistency

    search_parser.add_argument(
        '--no-index',
        help="don't index results, sets --no-article",
        action='store_true',
        default=False)

    search_parser.add_argument(
        '--no-article',
        help="don't ask for an article query",
        action='store_true',
        default=False)


    #* === revision command ===
    revision_parser = wikipedia.add_parser(
        'revision',
        help="view revision history and live revisions of articles",
        description="view revision history and live revisions of articles",
        parents=[pedia_common_args])

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

    if args.command == 'pedia':

        if args.subcommand == 'article':

            ARTICLE = article(args.title, args.width, args.summary, args.lang)

            if args.summary:
                args.no_title = True

            if args.no_title:
                print(ARTICLE[1])

            else:
                title_print(*ARTICLE, width=args.width)

            if args.url:

                print("\n{}".format(
                    request({
                        'prop': 'info',
                        'inprop': 'url',
                        'titles': ARTICLE[0],
                    }, args.lang)['query']['pages'][0]['fullurl']
                ))

        elif args.subcommand == 'search':

            SEARCH = search(args.title, args.results, args.lang)

            if args.no_index:
                for title in SEARCH:
                    print(title)
                    args.no_article = True
            else:
                for index, title in enumerate(SEARCH, 1):
                    # fancy right-justified index
                    print(" " * (len(str(args.results)) - len(str(index))) + f"({index}) {title}")

            if not args.no_article:

                article_index = input("\nEnter article index\n> ")
                title_print(*article(SEARCH[int(article_index) - 1], lang=args.lang))

        elif args.subcommand == 'revision':

            if args.feed:

                revision_feed(args.title)

main()
