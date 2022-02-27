import requests

def article(title):

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