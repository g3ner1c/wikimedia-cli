# `t http`

```text
wiki t http [-h] [-j] [-l <lang>] [<params> ...]
```

Request HTTP GET requests to the Wiktionary API.

## Options and arguments

### `<params>`

Parameters to pass to the Wiktionary API.  
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
$ wiki t http format=json action=query prop=info titles=quizzacious | jq
{
  "batchcomplete": "",
  "query": {
    "pages": {
      "4987614": {
        "pageid": 4987614,
        "ns": 0,
        "title": "quizzacious",
        "contentmodel": "wikitext",
        "pagelanguage": "en",
        "pagelanguagehtmlcode": "en",
        "pagelanguagedir": "ltr",
        "touched": "2022-05-23T09:18:18Z",
        "lastrevid": 60294187,
        "length": 484
      }
    }
  }
}
```

```json
$ wiki t http -j '{"format":"json","action":"query","prop":"pageviews","titles":"NFT","pvipdays":14}' | jq
{
  "batchcomplete": "",
  "query": {
    "pages": {
      "7990038": {
        "pageid": 7990038,
        "ns": 0,
        "title": "NFT",
        "pageviews": {
          "2022-05-09": 4,
          "2022-05-10": 8,
          "2022-05-11": 7,
          "2022-05-12": 5,
          "2022-05-13": 8,
          "2022-05-14": 4,
          "2022-05-15": 6,
          "2022-05-16": 5,
          "2022-05-17": 7,
          "2022-05-18": 6,
          "2022-05-19": 22,
          "2022-05-20": 22,
          "2022-05-21": 11,
          "2022-05-22": 8
        }
      }
    }
  }
}
```
