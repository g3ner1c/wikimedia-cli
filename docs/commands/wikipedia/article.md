# `p article`

```text
wiki p article [-h] [-l <lang>] [-s] [-w <width>] [-u] [--no-title] <title>
```

Read articles from Wikipedia.

## Options

### **`-s`**, `--summary`

Print a short summary of the article instead of the entire page.  
Sets `--no-title`.

### **`-w`**, `--width <width>`

Set the maximum width of text wrapping.  
0 for no wrapping.  
Defaults to 80.

### **`-u`**, `--url`

Print the URL of the article after the text.

### **`--no-title`**

Don't print the title heading of the article.

## Inherited options

### **`-l`**, `--lang <lang>`

ISO 639-1 language code of localized Wikipedia to use.  
Defaults to `en`.

### **`<title>`**

Title of article to interact with.

## Examples

```text
$ wiki p article "ukraine invasion"

2022 Russian invasion of Ukraine
--------------------------------------------------------------------------------

On 24 February 2022, Russia invaded Ukraine, marking a steep escalation of the
Russo-Ukrainian War, which had begun in 2014. The invasion has caused Europe's
largest refugee crisis since World War II, with more than 6.2 million Ukrainians
fleeing the country and a third of the population displaced. ...
```

```text
$ wiki p article "ukraine invasion" | wc
   1373   14231   93024
$ wiki p article -s "ukraine invasion" | wc
     57     662    4427
```

```text
$ wiki p article -l fr "invasion de l'ukraine"

Invasion de l'Ukraine par la Russie en 2022
--------------------------------------------------------------------------------

L'invasion de l'Ukraine par la Russie en 2022, aussi appelée guerre d'Ukraine ou
guerre russo-ukrainienne de 2022, est une campagne militaire déclenchée le 24
février 2022 sur ordre du président russe Vladimir Poutine.
Elle intervient à la suite de la crise ukrainienne, née du mouvement Euromaïdan
de 2013-2014 qui avait été suivi de la guerre du Donbass à partir de 2014. ...
```
