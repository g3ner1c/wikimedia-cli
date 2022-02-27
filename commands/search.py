import requests

def search(query, results=10, suggestion=False):

    S = requests.Session()

    URL = "https://en.wikipedia.org/w/api.php"

    PARAMS = {
        'action': 'query',
        'list': 'search',
        'srlimit': results,
        'srsearch': query,
        'format': 'json'
    }

    if suggestion:
        PARAMS['srinfo'] = 'suggestion'

    R = S.get(url=URL, params=PARAMS)
    DATA = R.json()
    
    for article in DATA['query']['search']:
        print(article['title'])