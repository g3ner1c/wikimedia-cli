from ..util import request_wikipedia


def p_search(query: str, results: int = 10, lang: str = "en") -> list[str]:

    # * returns list of articles close to query

    PARAMS = {"list": "search", "srsearch": query, "srlimit": results}

    DATA = request_wikipedia(PARAMS, lang)

    if DATA["query"]["searchinfo"]["totalhits"] == 0:

        if "suggestion" in DATA["query"]["searchinfo"]:
            return p_search(DATA["query"]["searchinfo"]["suggestion"], results, lang)
            # recurse to search with suggestion

        return ["No results found"]

    else:
        return [article["title"] for article in DATA["query"]["search"]]
