from textwrap import wrap

import requests


def fill(text, width=70, **kwargs):
    return '\n'.join([line for para in text.splitlines() for line in wrap(para, width, **kwargs) or ['']])
    #* ^^ newlines resets line width, textwrap.fill doesn't work
    #* ^^ source: https://github.com/python/cpython/issues/46167#issuecomment-1093406764

def article(title, fill_width=0):
    
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

    if fill_width:

        print(fill(article, fill_width, replace_whitespace=False))

    else:

        print(article)

def summary(title, fill_width=0):

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

    if fill_width:
    
        print(fill(summary, fill_width, replace_whitespace=False))
    
    else:
        
        print(summary)
