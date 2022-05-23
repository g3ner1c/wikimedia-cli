# `p search`

```text
wiki p search [-h] [-l <lang>] [-n <num>] [--no-index] [--no-query] <title>
```

Search for articles on Wikipedia.

## Options and arguments

### **`-n`**, `--results <num>`

Set the number of results to return.  
Defaults to 10.

### **`--no-index`**

Don't index results  
Sets `--no-query`.

### **`--no-query`**

Don't ask for an article query.

## Inherited options and arguments

### **`-l`**, `--lang <lang>`

ISO 639-1 language code of localized Wikipedia to use.  
Defaults to `en`.

### **`<title>`**

Title of article to interact with.

## Examples

```text
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
