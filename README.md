# wikimedia-cli

[![Documentation Status](https://readthedocs.org/projects/wikimedia-cli/badge/?version=latest)](https://wikimedia-cli.readthedocs.io/en/latest/?badge=latest)
[![CodeFactor](https://www.codefactor.io/repository/github/g3ner1c/wikimedia-cli/badge)](https://www.codefactor.io/repository/github/g3ner1c/wikimedia-cli)
[![Open issues](https://img.shields.io/github/issues/g3ner1c/wikimedia-cli)](https://github.com/g3ner1c/wikimedia-cli/issues)
[![Open PRs](https://img.shields.io/github/issues-pr/g3ner1c/wikimedia-cli)](https://github.com/g3ner1c/wikimedia-cli/pulls)
[![License](https://img.shields.io/github/license/g3ner1c/wikimedia-cli)](./LICENSE)
[![Python 3.x](https://img.shields.io/badge/python-3.x-green.svg)](https://www.python.org/)
[![Repo stars](https://img.shields.io/github/stars/g3ner1c/wikimedia-cli?style=social)](https://github.com/g3ner1c/wikimedia-cli/stargazers)

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
cd docs
pip install sphinx sphinx_rtd_theme
pip install -r requirements.txt
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
  - PyPI
  - AUR?
