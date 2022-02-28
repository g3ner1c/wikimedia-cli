import requests

def article(title):
    
    # returns article in plain text

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        'action': 'query',
        'prop': 'extracts',
        'titles': title,
        'explaintext': '',
        'exsectionformat': 'plain',
        'formatversion': '2',
        'format': 'json',
        'rvcontentformat': 'text/plain'
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGE = DATA['query']['pages'][0]
    article = PAGE['extract']

    print(article)

def summary(title):

    # returns article summary in plain text

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        'action': 'query',
        'prop': 'extracts',
        'exintro': '',
        'titles': title,
        'explaintext': '',
        'exsectionformat': 'plain',
        'formatversion': '2',
        'format': 'json',
        'rvcontentformat': 'text/plain'
    }

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()

    PAGE = DATA['query']['pages'][0]
    summary = PAGE['extract']

    print(summary)