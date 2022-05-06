# json2text

`json2text` is a simple tool to convert json object to plain texts.

From 
```json
{
  "about": {
    "Balance": "Balance",
    "Owner": "Owner",
    "Contracts": "Contracts",
    "Venture": "Venture",
    "panel": "Venture panel",
    "Quitting": "Quitting",
    "resign": "Resign Moderator",
    "resignMember": "Resign Moderator"
  }
}
```

to the key-value pairs
```json
[("about.Balance", "Balance"), ("about.Owner", "Owner"), ("about.Contracts", "Contracts"), ("about.Venture", "Venture"), ("about.panel", "Venture panel"), ("about.Quitting", "Quitting"), ("about.resign", "Resign Moderator"), ("about.resignMember", "Resign Moderator")]
```


Also can convert from

```json
[("about.Balance", "Balance"), ("about.Owner", "Owner"), ("about.Contracts", "Contracts"), ("about.Venture", "Venture"), ("about.panel", "Venture panel"), ("about.Quitting", "Quitting"), ("about.resign", "Resign Moderator"), ("about.resignMember", "Resign Moderator")]
```

to 

```json
{
  "about": {
    "Balance": "Balance",
    "Owner": "Owner",
    "Contracts": "Contracts",
    "Venture": "Venture",
    "panel": "Venture panel",
    "Quitting": "Quitting",
    "resign": "Resign Moderator",
    "resignMember": "Resign Moderator"
  }
}
```

## Install

Install from code.
```bash
python setup.py install
```

Install with pip
```bash
pip install json2text
```

## Usage

```python
import json
from json2text import JSON2Text, Text2JSON

with open('test.json', 'r') as f:
    jsonObj = json.load(f)
    texts = JSON2Text(jsonObj)
    print(texts)

    jsonObj = Text2JSON(texts)
    print(jsonObj)
```