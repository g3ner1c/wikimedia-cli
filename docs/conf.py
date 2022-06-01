project = "wikimedia-cli"
author = 'Sky "g3ner1c" H.'
copyright = '2022 Sky "g3ner1c" H.'

extensions = ["myst_parser"]  #! this is so that you can write docs in markdown instead of rst

master_doc = "index"
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"

html_static_path = ["_static"]

pygments_style = "sphinx"
pygments_dark_style = "one-dark"
