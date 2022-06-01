from textwrap import wrap

import requests


def fill(text, width: int = 70, **kwargs):
    return "\n".join([line for para in text.splitlines() for line in wrap(para, width, **kwargs) or [""]])
    # * ^^ newlines resets line width, textwrap.fill doesn't do that
    # * ^^ source: https://github.com/python/cpython/issues/46167#issuecomment-1093406764


def title_print(title: str, text: str, width: int = 80):  # * prints article with title
    print(f'\n{title}\n{"-"*80}\n\n{text}')


def request_wikipedia(params: dict, lang: str = "en", reuse_session: requests.sessions.Session = None) -> dict:

    params["format"] = "json"
    params["formatversion"] = "2"
    if "action" not in params:
        params["action"] = "query"  # defaults to query

    if reuse_session:
        S = reuse_session
    else:
        S = requests.Session()

    URL = f"https://{lang}.wikipedia.org/w/api.php"

    R = S.get(url=URL, params=params)

    return R.json()


def request_wiktionary(params: dict, lang: str = "en", reuse_session: requests.sessions.Session = None) -> dict:

    params["format"] = "json"
    params["formatversion"] = "2"
    if "action" not in params:
        params["action"] = "query"  # defaults to query

    if reuse_session:
        S = reuse_session
    else:
        S = requests.Session()

    URL = f"https://{lang}.wiktionary.org/w/api.php"

    R = S.get(url=URL, params=params)

    return R.json()
