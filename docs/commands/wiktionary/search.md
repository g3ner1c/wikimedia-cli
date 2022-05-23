# `t search`

```text
wiki t search [-h] [-l <lang>] [-n <num>] [--no-index] [--no-query] <title>
```

Search for phrases on Wiktionary.

## Options and arguments

### **`-n`**, `--results <num>`

Set the number of results to return.  
Defaults to 10.

### **`--no-index`**

Don't index results  
Sets `--no-query`.

### **`--no-query`**

Don't ask for a phrase query.

## Inherited options and arguments

### **`-l`**, `--lang <lang>`

ISO 639-1 language code of localized Wiktionary to use.  
Defaults to `en`.

### **`<title>`**

Name of phrase to interact with.

## Examples

```text
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
```
