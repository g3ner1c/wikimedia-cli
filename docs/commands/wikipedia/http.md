# `p http`

```text
wiki p http [-h] [-j] [-l <lang>] [<params> ...]
```

Request HTTP GET requests to the Wikipedia API.

## Options and arguments

### `<params>`

Parameters to pass to the Wikipedia API.  
Parameters take the form of `key=value` and are sperated by spaces to pass as individual arugments.

If `--json` is set, `<params>` will take one argument as a JSON.

### **`-j`**, `--json`

Take `<params>` as JSON.

## Inherited options and arguments

### **`-l`**, `--lang <lang>`

ISO 639-1 language code of localized Wikipedia to use  
Defaults to `en`.

## Examples

```json
$ wiki p http format=json action=query prop=info titles=bread | jq
{
  "batchcomplete": "",
  "query": {
    "normalized": [
      {
        "from": "bread",
        "to": "Bread"
      }
    ],
    "pages": {
      "36969": {
        "pageid": 36969,
        "ns": 0,
        "title": "Bread",
        "contentmodel": "wikitext",
        "pagelanguage": "en",
        "pagelanguagehtmlcode": "en",
        "pagelanguagedir": "ltr",
        "touched": "2022-05-22T17:50:39Z",
        "lastrevid": 1079133817,
        "length": 50871
      }
    }
  }
}
```

```json
$ wiki p http -j '{"format":"json","action":"query","prop":"pageviews","titles":"NATO","pvipdays":14}' | jq
{
  "batchcomplete": "",
  "query": {
    "pages": {
      "21133": {
        "pageid": 21133,
        "ns": 0,
        "title": "NATO",
        "pageviews": {
          "2022-05-09": 15024,
          "2022-05-10": 15483,
          "2022-05-11": 19099,
          "2022-05-12": 53220,
          "2022-05-13": 44733,
          "2022-05-14": 34677,
          "2022-05-15": 61166,
          "2022-05-16": 72129,
          "2022-05-17": 51661,
          "2022-05-18": 51762,
          "2022-05-19": 38754,
          "2022-05-20": 26217,
          "2022-05-21": 18488,
          "2022-05-22": null
        }
      }
    }
  }
}
```
