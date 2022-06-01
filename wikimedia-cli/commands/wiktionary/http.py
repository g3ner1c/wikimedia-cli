from json import loads

import requests


def t_get(params: list, json: bool = False, lang: str = "en") -> dict:

    S = requests.Session()

    URL = f"https://{lang}.wiktionary.org/w/api.php"


    if json:

        params = loads(params[0])

    else:

        params = { p[0]:(p[1] if len(p) == 2 else '') for p in [param.split('=') for param in params] }

    R = S.get(url=URL, params=params)

    return R.text
