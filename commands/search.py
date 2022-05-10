import requests

from .util import *

def search(query, results=10, suggestion=False, lang="en"):

    PARAMS = {
        'list': 'search',
        'srsearch': query,
        'srlimit': results
    }
    if suggestion:
        PARAMS['srinfo'] = 'suggestion'

    DATA = request(PARAMS, lang)
    
    for article in DATA['query']['search']:
        print(article['title'])