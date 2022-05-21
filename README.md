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
      - [Article summary](#article-summary)
    - [Wiktionary](#wiktionary)
      - [Search for a phrase](#search-for-a-phrase)
      - [Get information on a phrase](#get-information-on-a-phrase)
    - [Pipe into less for easier reading](#pipe-into-less-for-easier-reading)
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
usage: wiki [-h] {p,t} ...

Wikimedia CLI

positional arguments:
  {p,t}
    p         wikipedia
    t         wiktionary

options:
  -h, --help  show this help message and exit

'wiki <command> -h' for help on specific commands
```

Use `-h` with a command or subcommand for more info

```txt
$ wiki pedia -h
usage: wiki p [-h] {article,search,revision} ...

wikipedia commands

positional arguments:
  {article,search,revision}
    article             get articles
    search              search for articles
    revision            view revision history and live revisions of articles

options:
  -h, --help            show this help message and exit

'wiki p <subcommand> -h' for help on specific subcommands
```

```txt
$ wiki pedia article -h
usage: wiki p article [-h] [-l LANG] [-s] [-w WIDTH] [-u] [--no-title] title

get articles

positional arguments:
  title                 title of article

options:
  -h, --help            show this help message and exit
  -l LANG, --lang LANG  ISO 639-1 language code of Wikipedia to use (default: en)
  -s, --summary         get short summary instead of entire page, sets --no-title
  -w WIDTH, --width WIDTH
                        set maximum width of output (default: 80)
  -u, --url             print url after output
  --no-title            don't print title
```

### Wikipedia

#### Search for an article

```txt
$ wiki p search "ukraine invasion"
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
$ wiki p article "ukraine invasion"

2022 Russian invasion of Ukraine
--------------------------------------------------------------------------------

On 24 February 2022, Russia invaded Ukraine, marking a steep escalation of the
Russo-Ukrainian War, which had begun in 2014. The invasion has caused Europe's
largest refugee crisis since World War II, with more than 6.2 million Ukrainians
fleeing the country and a third of the population displaced. ...
```

#### Article summary

Use the `-s` flag with `article` to get a summary instead of the full article

```txt
$ wiki p article "ukraine invasion" | wc
   1373   14231   93024
$ wiki p article -s "ukraine invasion" | wc
     57     662    4427
```

### Wiktionary

#### Search for a phrase

```txt
$ wiki t search "effect"
 (1) effect
 (2) to the effect
 (3) take effect
 (4) in effect
 (5) come into effect
 (6) adverse effect
 (7) Seebeck effect
 (8) domino effect
 (9) Peltier effect
(10) put into effect

Enter phrase index
> 8

domino effect
--------------------------------------------------------------------------------


== English ==


=== Etymology ===
An allusion to a row of dominoes in which the fall of one leads to a cascade of
falling pieces.


=== Noun ===
domino effect (plural domino effects)

The situation in which one event sets off a chain of additional events.
(politics, historical) The theory that, if South Vietnam fell to Communism, it
would be followed by Cambodia, Laos, additional Southeast Asian countries, other
Asian countries, and likely even elsewhere.
Synonym: domino theory
...
```

#### Get information on a phrase
  
```txt
$ wiki t phrase "cool"

cool
--------------------------------------------------------------------------------


== English ==


=== Alternative forms ===
(slang) c00l, coo, k00l, kewl, kool, qewl, qool


=== Pronunciation ===
enPR: ko͞ol, IPA(key): /kuːl/
Rhymes: -uːl


=== Etymology 1 ===
From Middle English cool, from Old English cōl (“cool, cold, tranquil, calm”),
from Proto-West Germanic *kōl(ī), from Proto-Germanic *kōlaz, *kōluz (“cool”),
from Proto-Indo-European *gel- (“cold”). Cognate with Saterland Frisian köil
(“cool”), West Frisian koel (“cool”), Dutch koel (“cool”), Limburgish kool
(“cool”), German Low German köhl (“cool”), German kühl (“cool”). Related to
cold.


==== Adjective ====
cool (comparative cooler, superlative coolest)

 Having a slightly low temperature; mildly or pleasantly cold.
Synonym: chilly
Antonyms: lukewarm, tepid, warm
Allowing or suggesting heat relief.
...
```

### Pipe into less for easier reading

```txt
wiki p article "ukraine invasion" | less
```

### Live revision feed

New revisions will automatically print to terminal as the command is left running

Exact title of article is required, case-insensitive *(fuzzy searching in the works)*

```txt
$ wiki p revision -f "2022 Russian invasion of Ukraine"
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

### Localization

Use the ISO 639-1 language code with `-f` to access a different language wiki

```txt
$ wiki p article -l fr "invasion de l'ukraine"

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
- Wiktionary and Wikipedia article formatting (e.g. bold, italics, colors, links, images, etc.)
- Other wikimedia wikis
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
