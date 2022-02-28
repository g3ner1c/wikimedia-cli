import argparse
from commands.article import article
from commands.revision import revision_feed
from commands.search import search

def main():
    
    parser = argparse.ArgumentParser(description="Wikipedia CLI", prog="wiki")
    commands = parser.add_mutually_exclusive_group()
    
    commands.add_argument('-A', '--article', help="get article", action="store_true")
    commands.add_argument('-R', '--revision', help="get live revision feed", action="store_true")
    commands.add_argument('-S', '--search', help="search for articles", action="store_true")
    parser.add_argument('title', help="Title of article")

    args = parser.parse_args()

    if args.article:

        article(args.title)

    elif args.revision:

        revision_feed(args.title)

    elif args.search:

        search(args.title)

main()