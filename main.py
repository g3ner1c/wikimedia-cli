import argparse

from commands.util import *
from commands.wikipedia.article import p_article
from commands.wikipedia.http import p_get
from commands.wikipedia.revision import p_revision_feed
from commands.wikipedia.search import p_search
from commands.wiktionary.phrase import t_phrase
from commands.wiktionary.http import t_get
from commands.wiktionary.revision import t_revision_feed
from commands.wiktionary.search import t_search


def main():

    parser = argparse.ArgumentParser(
        description="Wikimedia CLI",
        epilog="'wiki <command> -h' for help on specific commands",
        prog="wiki")

    subparsers = parser.add_subparsers(
        dest="command",
        required=True)

    
    #* === wikipedia command ===

    wikipedia = subparsers.add_parser(
        'p',
        help="wikipedia",
        description="wikipedia commands",
        epilog="'wiki p <subcommand> -h' for help on specific subcommands").add_subparsers(
        dest="subcommand",
        required=True)

    #* === wikipedia common arguments ===
    pedia_common_args = argparse.ArgumentParser(add_help=False)
    pedia_common_args.add_argument(
        'title',
        help="title of article",
        metavar='<title>',
        type=str)

    pedia_common_args.add_argument(
        '-l', '--lang',
        help="ISO 639-1 language code of Wikipedia to use (default: en)",
        type=str,
        metavar='<lang>',
        default="en") #* change this to set default language


    ##* == article subcommand ==
    p_article_parser = wikipedia.add_parser(
        'article',
        help="get articles",
        description="get articles",
        parents=[pedia_common_args])

    p_article_parser.add_argument(
        '-s', '--summary',
        help="get short summary instead of entire page, sets --no-title",
        action='store_true',
        default=False)

    p_article_parser.add_argument(
        '-w', '--width',
        help="set maximum width of output (default: 80)",
        type=int,
        metavar='<width>',
        default=80) # redundant with fill_width but keep for consistency

    p_article_parser.add_argument(
        '-u', '--url',
        help="print url after output",
        action='store_true',
        default=False)

    p_article_parser.add_argument(
        '--no-title',
        help="don't print title",
        action='store_true',
        default=False)


    ##* == search subcommand ==
    p_search_parser = wikipedia.add_parser(
        'search',
        help="search for articles",
        description="search for articles",
        parents=[pedia_common_args])

    p_search_parser.add_argument(
        '-n', '--results',
        help="number of results to return (default: 10)",
        metavar='<num>',
        type=int,
        default=10) # redundant but keep for consistency

    p_search_parser.add_argument(
        '--no-index',
        help="don't index results, sets --no-query",
        action='store_true',
        default=False)

    p_search_parser.add_argument(
        '--no-query',
        help="don't ask for an article query",
        action='store_true',
        default=False)


    ##* == revision subcommand ==
    p_revision_parser = wikipedia.add_parser(
        'revision',
        help="view revision history and live revisions of articles",
        description="view revision history and live revisions of articles",
        parents=[pedia_common_args])

    ### == revision subcommand modes ==
    p_revision_flags = p_revision_parser.add_mutually_exclusive_group()
    p_revision_flags.add_argument(
        '-f', '--feed',
        help="view live revision feed",
        action='store_true',
        default=False)
    ### ===============================

    ##* == http subcommand ==
    p_http_parser = wikipedia.add_parser(
        'http',
        help="request HTTP GET methods to the Wikipedia API",
        description="request HTTP GET methods to the Wikipedia API")

    p_http_parser.add_argument(
        'params',
        help="parameters to pass to the Wikipedia API",
        type=str,
        nargs='*')
    
    p_http_parser.add_argument(
        '-j', '--json',
        help="take input as JSON",
        action='store_true',
        default=False)
    
    p_http_parser.add_argument(
        '-l', '--lang',
        help="ISO 639-1 language code of Wikipedia to use (default: en)",
        type=str,
        metavar='<lang>',
        default="en")
        

    #* === wiktionary command ===

    wiktionary = subparsers.add_parser(
        't',
        help="wiktionary",
        description="wiktionary commands",  
        epilog="'wiki t <subcommand> -h' for help on specific subcommands").add_subparsers(
        dest="subcommand",
        required=True)

    #* === wiktionary common arguments ===
    tionary_common_args = argparse.ArgumentParser(add_help=False)
    tionary_common_args.add_argument(
        'phrase',
        help="name of phrase",
        metavar='<phrase>',
        type=str)

    tionary_common_args.add_argument(
        '-l', '--lang',
        help="ISO 639-1 language code of Wikipedia to use (default: en)",
        type=str,
        metavar='<lang>',
        default="en") #* change this to set default language

    
    ##* == phrase subcommand ==

    t_phrase_parser = wiktionary.add_parser(
        'phrase',
        help="get phrases",
        description="get phrases",
        parents=[tionary_common_args])

    t_phrase_parser.add_argument(
        '-s', '--summary',
        help="get short summary instead of entire page, sets --no-title",
        action='store_true',
        default=False)

    t_phrase_parser.add_argument(
        '-w', '--width',
        help="set maximum width of output (default: 80)",
        type=int,
        metavar='<width>',
        default=80) # redundant with fill_width but keep for consistency

    t_phrase_parser.add_argument(
        '-u', '--url',
        help="print url after output",
        action='store_true',
        default=False)

    t_phrase_parser.add_argument(
        '--no-title',
        help="don't print title",
        action='store_true',
        default=False)


    ##* == search subcommand ==
    t_search_parser = wiktionary.add_parser(
        'search',
        help="search for phrases",
        description="search for phrases",
        parents=[tionary_common_args])

    t_search_parser.add_argument(
        '-n', '--results',
        help="number of results to return (default: 10)",
        metavar='<num>',
        type=int,
        default=10) # redundant but keep for consistency

    t_search_parser.add_argument(
        '--no-index',
        help="don't index results, sets --no-query",
        action='store_true',
        default=False)

    t_search_parser.add_argument(
        '--no-query',
        help="don't ask for a phrase query",
        action='store_true',
        default=False)


    ##* == revision subcommand ==
    t_revision_parser = wiktionary.add_parser(
        'revision',
        help="view revision history and live revisions of phrases",
        description="view revision history and live revisions of phrases",
        parents=[tionary_common_args])

    ### == revision subcommand modes ==
    t_revision_flags = t_revision_parser.add_mutually_exclusive_group()
    t_revision_flags.add_argument(
        '-f', '--feed',
        help="view live revision feed",
        action='store_true',
        default=False)
    ### ===============================

    ##* == http subcommand ==
    t_http_parser = wiktionary.add_parser(
        'http',
        help="request HTTP GET methods to the Wiktionary API",
        description="request HTTP GET methods to the Wiktionary API")

    t_http_parser.add_argument(
        'params',
        help="parameters to pass to the Wiktionary API",
        type=str,
        metavar='<params>',
        nargs='*')
    
    t_http_parser.add_argument(
        '-j', '--json',
        help="take input as JSON",
        action='store_true',
        default=False)
    
    t_http_parser.add_argument(
        '-l', '--lang',
        help="ISO 639-1 language code of Wiktionary to use (default: en)",
        type=str,
        metavar='<lang>',
        default="en")


    args = parser.parse_args()

    # print(args)

    if args.command == 'p':

        if args.subcommand == 'article':

            ARTICLE = p_article(args.title, args.width, args.summary, args.lang)

            if args.summary:
                args.no_title = True

            if args.no_title:
                print(ARTICLE[1])

            else:
                title_print(*ARTICLE, width=args.width)

            if args.url:

                print("\n{}".format(
                    request_wikipedia({
                        'prop': 'info',
                        'inprop': 'url',
                        'titles': ARTICLE[0],
                    }, args.lang)['query']['pages'][0]['fullurl']
                ))

        elif args.subcommand == 'search':

            SEARCH = p_search(args.title, args.results, args.lang)

            if args.no_index:
                for title in SEARCH:
                    print(title)
                    args.no_query = True
            else:
                for index, title in enumerate(SEARCH, 1):
                    # fancy right-justified index
                    print(" " * (len(str(args.results)) - len(str(index))) + f"({index}) {title}")

            if not args.no_query:

                article_index = input("\nEnter article index\n> ")
                title_print(*p_article(SEARCH[int(article_index) - 1], lang=args.lang))

        elif args.subcommand == 'revision':

            if args.feed:

                p_revision_feed(args.title, lang=args.lang)

        elif args.subcommand == 'http':

            print(p_get(args.params, args.json, args.lang))
    
    elif args.command == 't':

        if args.subcommand == 'phrase':

            PHRASE = t_phrase(args.phrase, args.width, args.summary, args.lang)

            if args.summary:
                args.no_title = True

            if args.no_title:
                print(PHRASE[1])

            else:
                title_print(*PHRASE, width=args.width)

            if args.url:

                print("\n{}".format(
                    request_wiktionary({
                        'prop': 'info',
                        'inprop': 'url',
                        'titles': PHRASE[0],
                    }, args.lang)['query']['pages'][0]['fullurl']
                ))

        elif args.subcommand == 'search':

            SEARCH = t_search(args.phrase, args.results, args.lang)

            if args.no_index:
                for phrase in SEARCH:
                    print(phrase)
                    args.no_query = True
            else:
                for index, phrase in enumerate(SEARCH, 1):
                    print(" " * (len(str(args.results)) - len(str(index))) + f"({index}) {phrase}")

            if not args.no_query:

                article_index = input("\nEnter phrase index\n> ")
                title_print(*t_phrase(SEARCH[int(article_index) - 1], lang=args.lang))
        
        elif args.subcommand == 'revision':

            if args.feed:

                t_revision_feed(args.phrase, lang=args.lang)

        elif args.subcommand == 'http':

            print(t_get(args.params, args.json, args.lang))

main()
