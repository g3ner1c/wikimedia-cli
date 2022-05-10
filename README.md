# wikipedia-cli

A Wikipedia CLI written in Python

[Still in early developement](#ideas-and-todo)

## Contents

- [wikipedia-cli](#wikipedia-cli)
  - [Contents](#contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Search for an article](#search-for-an-article)
    - [Read an article](#read-an-article)
    - [Pipe into less for easier reading](#pipe-into-less-for-easier-reading)
    - [Read an article with fuzzy searching](#read-an-article-with-fuzzy-searching)
    - [Live revision feed](#live-revision-feed)
  - [Ideas and TODO](#ideas-and-todo)
  - [Thanks to](#thanks-to)

## Installation

```txt
git clone https://github.com/awesomeplaya211/wikipedia-cli.git
cd wikipedia-cli
python main.py -h
```

## Usage

```txt
$ python main.py -h
usage: wiki [-h] {article,search} ...

Wikipedia CLI

positional arguments:
  {article,search}
    article         get article
    search          search for relevant articles

optional arguments:
  -h, --help        show this help message and exit

'wiki <command> -h' for help on specific commands
```

Use `-h` with a command for more info

```txt
$ python main.py article -h
usage: wiki article [-h] [-s | -r] title

positional arguments:
  title           title of article

optional arguments:
  -h, --help      show this help message and exit
  -s, --summary   get short summary instead of entire page
  -r, --revision  get live revision feed of article
```

### Search for an article

```txt
$ python main.py search "ukraine invasion"
2022 Russian invasion of Ukraine
Russo-Ukrainian War
Protests against the 2022 Russian invasion of Ukraine
International reactions to the 2022 Russian invasion of Ukraine
Soviet–Ukrainian War
List of invasions and occupations of Ukraine
Timeline of the 2022 Russian invasion of Ukraine
Order of battle for the 2022 Russian invasion of Ukraine
War crimes during the 2022 Russian invasion of Ukraine
List of military engagements during the 2022 Russian invasion of Ukraine
```

### Read an article

```txt
$ python main.py article "2022 Russian invasion of Ukraine"
On 24 February 2022, Russia launched a large-scale invasion of Ukraine, its neighbour to the southwest, marking a dramatic escalation of the Russo-Ukrainian War that began in 2014. It is the largest conventional warfare operation in Europe since World War II.The invasion was preceded by a Russian military build-up that started in early...
```

### Pipe into less for easier reading

```txt
python main.py article "2022 Russian invasion of Ukraine" | less
```

### Read an article with fuzzy searching

```txt
python main.py article "$(python main.py search "ukraine invasion" -n 1)" -s
```

### Live revision feed

New revisions will automatically print to terminal as the command is left running

```txt
$ python main.py article -r "2022 Russian invasion of Ukraine"
#1074359973
Article Size: 348287 bytes
by Leaky.Solar at 2022-02-27T21:30:18Z
Section: Foreign military support to Ukraine
linked [[List of international military aid of Russo-Ukrainian War]] by see also template


#1074360822
+826 bytes diff
by Rfl0216 at 2022-02-27T21:36:52Z
Filled in 3 bare reference(s) with reFill 2


#1074360897
+1036 bytes diff
by Ingenuity at 2022-02-27T21:37:13Z
add azerbaijani citizens killed to infobox


#1074361141
+1954 bytes diff
by Leaky.Solar at 2022-02-27T21:39:15Z
Section: Reactions
attempted start of section for how crisis is seen through social media
```

## Ideas and TODO

- Redirect to closest article if no exact match is found
- Revision history
- Main page and ITN/Ongoing
- Support for localization
- Packaging
  - PyPI
  - AUR?

## Thanks to

[The awesome Wikipedia wrapper API which I ~~stole code~~ took inspiration from](https://github.com/goldsmith/Wikipedia)
