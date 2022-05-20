from textwrap import wrap

from .search import search
from ..util import *


def fill(text, width: int = 70, **kwargs):
    return '\n'.join([line for para in text.splitlines() for line in wrap(para, width, **kwargs) or ['']])
    #* ^^ newlines resets line width, textwrap.fill doesn't do that
    #* ^^ source: https://github.com/python/cpython/issues/46167#issuecomment-1093406764

def title_print(title: str, text: str, width: int = 80): #* prints article with title
    print(f'\n{title}\n{"-"*80}\n\n{text}')


def article(title: str, fill_width: int = 80, summary: bool = False, lang: str = "en", recurse: bool = True) -> (str):

    #* returns article as (title, plain text)

    title = search(title, 1, lang)[0] # fuzzy search, exact match evaluates to itself

    PARAMS = {
        'prop': 'extracts',
        'titles': title,
        'explaintext': ''
    }

    if summary:
        PARAMS['exintro'] = ''

    try:

        article_text = request(PARAMS, lang)['query']['pages'][0]['extract']

        if not article_text:

            raise KeyError

    except KeyError: # article not found

        if recurse:

            # recurse in case 1st search doesn't match
            return article(search(title, 1, lang)[0], fill_width, summary, lang, recurse=False)

        return "", "Article not found"

    if fill_width:

        title = fill(title, fill_width, replace_whitespace=False)
        article_text = fill(article_text, fill_width, replace_whitespace=False)

    return title, article_text
