# wikimedia-cli

[![Documentation status](https://readthedocs.org/projects/wikimedia-cli/badge/?version=latest)](https://wikimedia-cli.readthedocs.io/en/latest/?badge=latest)
[![Build status](https://img.shields.io/github/workflow/status/g3ner1c/wikimedia-cli/Test%20package)](https://www.codefactor.io/repository/github/g3ner1c/wikimedia-cli)
[![CodeFactor](https://www.codefactor.io/repository/github/g3ner1c/wikimedia-cli/badge)](https://www.codefactor.io/repository/github/g3ner1c/wikimedia-cli)
[![Open issues](https://img.shields.io/github/issues/g3ner1c/wikimedia-cli)](https://github.com/g3ner1c/wikimedia-cli/issues)
[![Open PRs](https://img.shields.io/github/issues-pr/g3ner1c/wikimedia-cli)](https://github.com/g3ner1c/wikimedia-cli/pulls)
[![Repo stars](https://img.shields.io/github/stars/g3ner1c/wikimedia-cli?style=social)](https://github.com/g3ner1c/wikimedia-cli/stargazers)

[![Supported Python versions](https://img.shields.io/pypi/pyversions/wikimedia-cli)](https://pypi.org/project/tetris/)
[![PyPI version](https://img.shields.io/pypi/v/wikimedia-cli)](https://pypi.org/project/tetris/)

A minimally dependent Wikimedia CLI written in Python

[In early developement](#ideas-and-todo)

## Currently supported Wikimedia projects

- [Wikipedia](https://www.wikipedia.org/) - The free encyclopedia
- [Wiktionary](https://www.wiktionary.org/) - The free dictionary

## Documentation

Documentation is available on **[ReadTheDocs](https://wikimedia-cli.readthedocs.io/en/latest/)**

- [Installation](https://wikimedia-cli.readthedocs.io/en/latest/installation.html)

To build the documentation locally, make sure you are in the root project directory and run:

```bash
pip install Sphinx furo myst-parser
cd docs
make html
```

Documentation will be built in the `docs/_build/html` directory

## Ideas and TODO

- Wiktionary and Wikipedia article formatting (e.g. bold, italics, colors, links, images, etc.)
- Wiktionary Improvements
  - Summary
  - Breakdown of phrase properties (e.g. definition, usage, synonyms, entomology, etc.)
- Other wikimedia wikis
  - Wikimedia commons
  - Wikidata
  - Wikinews
  - Wikibooks
- Revision history
- Main page and ITN/Ongoing
- Packaging
  - AUR
