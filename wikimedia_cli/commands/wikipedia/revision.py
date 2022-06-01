import re
import time

import requests

from ..util import request_wikipedia

REGEX = r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})Z"  # regex for latest date eg. 2020-01-01T00:00:00Z
H_REGEX = r"/\* (.*) \*/\s?"  # regex for heading eg. /* heading */


def p_revision_feed(title: str, interval: int = 5, lang: str = "en"):

    current_revid = 0
    newest_revid = 0
    page_size = 0
    fetches = 0

    PARAMS = {
        "prop": "revisions",
        "titles": title,
        "rvlimit": "10",
        "rvprop": "ids|size|timestamp|user|comment",
        "rvslots": "main",
    }

    S = requests.Session()

    while True:

        DATA = request_wikipedia(PARAMS, lang, S)

        PAGE = DATA["query"]["pages"][0]

        for revision in PAGE["revisions"]:

            timestamp = revision["timestamp"]
            # matches = re.search(REGEX, timestamp)
            # unix_timestamp = datetime.datetime(*tuple([int(i) for i in matches.groups()])).timestamp()

            user = revision["user"]
            comment = revision["comment"]
            revid = revision["revid"]
            size = revision["size"]

            if fetches == 0:  # first fetch

                current_revid = revid - 1
                page_size = size

            if revid > newest_revid:  # update newest revid

                newest_revid = revid

            if revid > current_revid:  # new revisions since last fetch

                # print(unix_timestamp)
                print(f"#{revid}")

                if fetches == 0:

                    print(f"Article Size: {size} bytes")

                else:

                    diff = size - page_size

                    if diff > 0:

                        print(f"\033[92m{f'+{size - page_size} bytes diff'}\033[00m")  # green text

                    else:

                        print(f"\033[91m{f'{size - page_size} bytes diff'}\033[00m")  # red text

                print(f"by \033[94m{user}\033[00m at \033[94m{timestamp}\033[00m")  # cyan text

                if comment == "":

                    print("\033[3m\033[95mno comment\033[00m\033[0m")  # magenta italic text

                else:

                    try:

                        comment_heading = re.search(H_REGEX, comment).groups()[0]
                        print(
                            "\033[95mSection: \033[00m" + f"\033[4m\033[95m{comment_heading}\033[00m\033[0m"
                        )  # magenta underlined heading

                    except AttributeError:

                        pass

                    comment_body = re.sub(H_REGEX, "", comment, 0, re.MULTILINE)  # remove heading from comment
                    if not comment_body.isspace():  # check if not whitespace

                        print(f"\033[95m{comment_body}\033[00m")  # magenta text

                print("\n")

            fetches += 1
            page_size = size  # update page size

        current_revid = newest_revid  # update current fetched revid
        time.sleep(interval)
