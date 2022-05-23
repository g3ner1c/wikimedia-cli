# `t phrase`

```text
wiki t phrase [-h] [-l <lang>] [-s] [-w <width>] [-u] [--no-title] <title>
```

Define phrases from Wiktionary.

## Options

### **`-s`**, `--summary`

Print a short summary of the phrase instead of the entire page.  
Sets `--no-title`.

### **`-w`**, `--width <width>`

Set the maximum width of text wrapping.  
0 for no wrapping.  
Defaults to 80.

### **`-u`**, `--url`

Print the URL of the page after the text.

### **`--no-title`**

Don't print the title heading of the definition.

## Inherited options

### **`-l`**, `--lang <lang>`

ISO 639-1 language code of localized Wiktionary to use.  
Defaults to `en`.

### **`<title>`**

Name of phrase to interact with.

## Examples

```text
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
