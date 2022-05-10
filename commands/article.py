from textwrap import wrap

from .search import search
from .util import *


def fill(text, width: int = 70, **kwargs):
    return '\n'.join([line for para in text.splitlines() for line in wrap(para, width, **kwargs) or ['']])
    #* ^^ newlines resets line width, textwrap.fill doesn't do that
    #* ^^ source: https://github.com/python/cpython/issues/46167#issuecomment-1093406764


def article(title, fill_width: int = 80, summary: bool = False, lang: str = "en"):

    #* returns article in plain text

    PARAMS = {
        'prop': 'extracts',
        'titles': title,
        'explaintext': ''
    }

    if summary:
        PARAMS['exintro'] = ''

    article = request(PARAMS, lang)['query']['pages'][0]['extract']

    if fill_width:
        print(fill(article, fill_width, replace_whitespace=False))
    else:
        print(article)
