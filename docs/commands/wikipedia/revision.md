# `p revision`

```text
wiki p revision [-h] [-l <lang>] [-f] <title>
```

View revision history and live revisions of articles.

## Options and arguments

### **`-f`**, `--feed`

View live revision feed  
New revisions will automatically print to terminal as the command is left running  
Exact title of article is required, case-insensitive *(fuzzy searching in the works)*

## Inherited options and arguments

### **`-l`**, `--lang <lang>`

ISO 639-1 language code of localized Wikipedia to use.  
Defaults to `en`.

### **`<title>`**

Title of article to interact with.

## Examples

```text
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
