from .search import p_search
from ..util import *


def p_article(title: str, fill_width: int = 80, summary: bool = False, lang: str = "en", recurse: bool = True) -> (str):

    #* returns article as (title, plain text)

    title = p_search(title, 1, lang)[0] # fuzzy search, exact match evaluates to itself

    PARAMS = {
        'prop': 'extracts',
        'titles': title,
        'explaintext': ''
    }

    if summary:
        PARAMS['exintro'] = ''

    try:

        article_text = request_wikipedia(PARAMS, lang)['query']['pages'][0]['extract']

        if not article_text:

            raise KeyError

    except KeyError: # article not found

        if recurse:

            # recurse in case 1st search doesn't match
            return p_article(p_search(title, 1, lang)[0], fill_width, summary, lang, recurse=False)

        return "", "Article not found"

    if fill_width:

        title = fill(title, fill_width, replace_whitespace=False)
        article_text = fill(article_text, fill_width, replace_whitespace=False)

    return title, article_text
