import requests

from .util import *

def search(query, results=10, lang="en"):

    #* returns list of articles close to query

    PARAMS = {
        'list': 'search',
        'srsearch': query,
        'srlimit': results
    }

    DATA = request(PARAMS, lang)
    
    if DATA['query']['searchinfo']['totalhits'] == 0:

        if 'suggestion' in DATA['query']['searchinfo']:
            return search(DATA['query']['searchinfo']['suggestion'], results, lang)
            # recurse to search with suggestion

        else:
            return ["No results found"]

    else:
        return [article['title'] for article in DATA['query']['search']]
