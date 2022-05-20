# wikimedia-cli

A lightweight, minimally dependent, Wikimedia CLI written in Python

[Still in early developement](#ideas-and-todo)

## Contents

- [wikimedia-cli](#wikimedia-cli)
  - [Contents](#contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Wikipedia](#wikipedia)
      - [Search for an article](#search-for-an-article)
      - [Read an article](#read-an-article)
        - [Pipe into less for easier reading](#pipe-into-less-for-easier-reading)
      - [Article summary](#article-summary)
      - [Live revision feed](#live-revision-feed)
      - [Localization](#localization)
  - [Ideas and TODO](#ideas-and-todo)
  - [Thanks to](#thanks-to)

## Installation

```txt
git clone https://github.com/g3ner1c/wikipedia-cli.git
cd wikipedia-cli
echo "alias wiki='$(pwd)/main.py'" >> <shell-profile-path>
wiki -h
```

## Usage

```txt
$ wiki -h
usage: wiki [-h] {pedia} ...

Wikimedia CLI

positional arguments:
  {pedia}
    pedia     get articles from wikipedia

options:
  -h, --help  show this help message and exit

'wiki <command> -h' for help on specific commands
```

Use `-h` with a command or subcommand for more info

```txt
$ wiki pedia -h
usage: wiki pedia [-h] {article,search,revision} ...

get information from wikipedia

positional arguments:
  {article,search,revision}
    article             get articles
    search              search for articles
    revision            view revision history and live revisions of articles

options:
  -h, --help            show this help message and exit

'wiki pedia <subcommand> -h' for help on specific subcommands
```

```txt
$ wiki pedia article -h
usage: wiki pedia article [-h] [-l LANG] [-s] [-w WIDTH] [-u] [--no-title] title

get articles

positional arguments:
  title                 title of article

options:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  ISO 639-1 language code of Wikipedia to use (default: en)
  -s, --summary         get short summary instead of entire page, sets --no-title
  -w WIDTH, --width WIDTH
                        set maximum width of output (default: 80)
  -u, --url             print url to article after output
  --no-title            don't print title
```

### Wikipedia

#### Search for an article

```txt
$ wiki pedia search "ukraine invasion"
 (1) 2022 Russian invasion of Ukraine
 (2) Russo-Ukrainian War
 (3) Timeline of the 2022 Russian invasion of Ukraine
 (4) Government and intergovernmental reactions to the 2022 Russian invasion of Ukraine
 (5) List of invasions and occupations of Ukraine
 (6) Legality of the 2022 Russian invasion of Ukraine
 (7) Prelude to the 2022 Russian invasion of Ukraine
 (8) List of Russian generals killed during the 2022 invasion of Ukraine
 (9) Ukrainian–Soviet War
(10) Protests against the 2022 Russian invasion of Ukraine

Enter article index
> 6

Legality of the 2022 Russian invasion of Ukraine
--------------------------------------------------------------------------------

The 2022 Russian invasion of Ukraine violated international law (including the
Charter of the United Nations), and constitutes a crime of aggression in
international criminal law. The invasion has also been called unlawful under
some countries' domestic criminal codes — including those of Ukraine and Russia—
although procedural obstacles exist to prosecutions under these laws. ...
```

#### Read an article

```txt
$ wiki pedia article "ukraine invasion"

2022 Russian invasion of Ukraine
--------------------------------------------------------------------------------

On 24 February 2022, Russia invaded Ukraine, marking a steep escalation of the
Russo-Ukrainian War, which had begun in 2014. The invasion has caused Europe's
largest refugee crisis since World War II, with more than 6.2 million Ukrainians
fleeing the country and a third of the population displaced. ...
```

##### Pipe into less for easier reading

```txt
wiki pedia article "ukraine invasion" | less
```

#### Article summary

Use the `-s` flag with `article` to get a summary instead of the full article

```txt
$ wiki pedia article "ukraine invasion" | wc
   1373   14231   93024
$ wiki pedia article -s "ukraine invasion" | wc
     57     662    4427
```

#### Live revision feed

New revisions will automatically print to terminal as the command is left running

Exact title of article is required, case-insensitive *(fuzzy searching in the works)*

```txt
$ wiki pedia revision -f "2022 Russian invasion of Ukraine"
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

#### Localization

Use the ISO 639-1 language code with `-f` to access a different language wiki

```txt
$ wiki pedia article -l fr "invasion de l'ukraine"

Invasion de l'Ukraine par la Russie en 2022
--------------------------------------------------------------------------------

L'invasion de l'Ukraine par la Russie en 2022, aussi appelée guerre d'Ukraine ou
guerre russo-ukrainienne de 2022, est une campagne militaire déclenchée le 24
février 2022 sur ordre du président russe Vladimir Poutine.
Elle intervient à la suite de la crise ukrainienne, née du mouvement Euromaïdan
de 2013-2014 qui avait été suivi de la guerre du Donbass à partir de 2014. ...
```

## Ideas and TODO

- **Full Documentation - Important**
- Other wikimedia wikis
  - Wikitionary
  - Wikimedia commons
  - Wikidata
  - Wikinews
- Revision history
- Main page and ITN/Ongoing
- Packaging
  - PyPI
  - AUR?

## Thanks to

[The awesome Wikipedia wrapper API which I ~~stole code~~ took inspiration from](https://github.com/goldsmith/Wikipedia)
