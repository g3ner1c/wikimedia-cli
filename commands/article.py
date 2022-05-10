from textwrap import wrap

import requests

from .util import *


def fill(text, width=70, **kwargs):
    return '\n'.join([line for para in text.splitlines() for line in wrap(para, width, **kwargs) or ['']])
    #* ^^ newlines resets line width, textwrap.fill doesn't do that
    #* ^^ source: https://github.com/python/cpython/issues/46167#issuecomment-1093406764


def article(title, fill_width=80, lang="en"):
    
    # returns article in plain text

    PARAMS = {
        'prop': 'extracts',
        'titles': title,
        'explaintext': ''
    }

    article = request(PARAMS, lang)['query']['pages'][0]['extract']

    if fill_width:
        print(fill(article, fill_width, replace_whitespace=False))
    else:
        print(article)


def summary(title, fill_width=80, lang="en"):

    # returns article summary in plain text

    PARAMS = {
        'prop': 'extracts',
        'exintro': '',
        'titles': title,
        'explaintext': ''
    }

    summary = request(PARAMS, lang)['query']['pages'][0]['extract']

    if fill_width:
        print(fill(summary, fill_width, replace_whitespace=False))
    else:
        print(summary)
