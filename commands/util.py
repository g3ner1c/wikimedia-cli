import requests

def request(params: dict, lang: str = "en") -> dict:

    params['format'] = "json"
    params['formatversion'] = "2"
    if 'action' not in params:
        params['action'] = 'query' # defaults to query

    S = requests.Session()

    URL = f"https://{lang}.wikipedia.org/w/api.php"

    R = S.get(url=URL, params=params)

    return R.json()
