import requests
import re
import time
import datetime

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "prop": "revisions",
    "titles": "2022 Russian invasion of Ukraine",
    "rvlimit": "10",
    "rvprop": "ids|size|timestamp|user|comment|content",
    "rvslots": "main",
    "formatversion": "2",
    "format": "json"
}

regex = r"(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})Z" # regex for latest date eg. 2020-01-01T00:00:00Z

current_revid = 0
newest_revid = 0
page_size = 0
fetches = 0

def get_info():

    global current_revid
    global newest_revid
    global page_size
    global fetches

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGE = DATA["query"]["pages"][0]

    for revision in PAGE["revisions"]:

        timestamp = revision["timestamp"]
        matches = re.search(regex, timestamp)
        unix_timestamp = datetime.datetime(*tuple([int(i) for i in matches.groups()])).timestamp()

        user = revision["user"]
        comment = revision["comment"]
        revid = revision["revid"]
        size = revision["size"]

        if fetches == 0: # first fetch

            current_revid = revid - 1
            page_size = size

        if revid > newest_revid: # update newest revid

            newest_revid = revid

        if revid > current_revid: # new revisions since last fetch

            # print(unix_timestamp)
            # print(revid)
            
            if fetches == 0:

                print(f"Article Size: {size} bytes")
            
            else:

                print(f"{size - page_size} bytes diff")

            print("{} ({})".format(timestamp, user))

            if comment == "":

                print("(no comment)")

            else:

                print(comment)

            # print('\n')

        fetches += 1
        
    current_revid = newest_revid # update current fetched revid

while True:
    get_info()
    time.sleep(5)