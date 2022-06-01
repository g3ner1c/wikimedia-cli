from ..util import *
from .search import t_search


def t_phrase(phrase: str, fill_width: int = 80, summary: bool = False, lang: str = "en", recurse: bool = True) -> (str):

    #* returns phrase as (phrase, plain text)

    phrase = t_search(phrase, 1, lang)[0] # fuzzy search, exact match evaluates to itself

    PARAMS = {
        'prop': 'extracts',
        'titles': phrase,
        'explaintext': ''
    }

    if summary: # currently doesn't work at the moment remain for future use
        pass
        # PARAMS['exintro'] = ''

    try:

        definition = request_wiktionary(PARAMS, lang)['query']['pages'][0]['extract']

        if not definition:

            raise KeyError

    except KeyError: # phrase not found

        if recurse:

            # recurse in case 1st search doesn't match
            return t_phrase(t_search(phrase, 1, lang)[0], fill_width, summary, lang, recurse=False)

        return "", "Phrase not found"

    if fill_width:

        phrase = fill(phrase, fill_width, replace_whitespace=False)
        definition = fill(definition, fill_width, replace_whitespace=False)

    return phrase, definition
