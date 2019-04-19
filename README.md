# translit
Transliterator tool

## How to Build
```
pip install -r requirements.txt
python setup.py install
```

## Supported Languages
This package uses [transliterate](https://pypi.org/project/transliterate/). It supports the following ISO 639-1 language codes: 

```javascript
{
    // Armenian
    "hy" : { "name": "Armenian", "local":"Հայերեն", "1":"hy", "2":"hye", "2T":"hye", "2B":"arm", "3":"hye"},
    // Bulgarian (beta)
    "bg" :{"name":"Bulgarian", "local":"български език", "1":"bg", "2":"bul", "2T":"bul", "2B":"bul", "3":"bul"},
    // Georgian
    "ka" :{"name":"Georgian", "local":"ქართული", "1":"ka", "2":"kat", "2T":"kat", "2B":"geo", "3":"kat"},
    // Greek
    "el" :{"name":"Greek", "local":"ελληνικά", "1":"el", "2":"ell", "2T":"ell", "2B":"gre", "3":"ell"},
    // Macedonian (alpha)
    "mk" :{"name":"Macedonian", "local":"македонски јазик", "1":"mk", "2":"mkd", "2T":"mkd", "2B":"mac", "3":"mkd"},
    // Russian
    "ru" :{"name":"Russian", "local":"русский язык", "1":"ru", "2":"rus", "2T":"rus", "2B":"rus", "3":"rus"},
    // Serbian (alpha)
    "sr" :{"name":"Serbian", "local":"српски језик", "1":"sr", "2":"srp", "2T":"srp", "2B":"srp", "3":"srp"},
    // Ukrainian (beta)
    "uk" :{"name":"Ukrainian", "local":"українська мова", "1":"uk", "2":"ukr", "2T":"ukr", "2B":"ukr", "3":"ukr"}
}
```

## How to Use
Run the `translist` command line tool and pass a JSON object with `source` as source language, `target` as the target language and `text` as the text to transliterate.
```json
{ "source" : "ru", "target" : "en", "text": "до свидания" }
```

## Examples
```
$ translist
{ "source" : "ru", "target" : "en", "text": "до свидания" }
{"source": "ru", "trans": "do svidanija", "target": "en", "text": "до свидания"}
{ "source" : "en", "target": "ru", "text": "do svidanija" }
{"source": "en", "trans": "до свидания", "target": "ru", "text": "do svidanija"}
```
