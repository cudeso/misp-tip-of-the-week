'''
Python script to create the README.md file. Warning: this will overwrite the existing file.

- Reads JSON file
- Converts to a human readable format

Koen Van Impe - cudeso.be
'''

import sys
import json

jsonfile = "misp-tip-of-the-week.json"
mdfile = "README.md"

prenote= """# MISP Tip of the Week

A collection of tips for using [MISP](https://www.misp-project.org/). Published via [BelgoMISP](https://twitter.com/belgomisp) (*todo*) and this repository. Available in MD and [JSON](https://raw.githubusercontent.com/cudeso/misp-tip-of-the-week/main/misp-tip-of-the-week.json). 

Do you want to **contribute**? [Suggest a tip](https://github.com/cudeso/misp-tip-of-the-week/issues/new/choose) via a Github issue or do a PR to the JSON file.


# Tips of the Week

"""

postnote = """

# JSON format

```
    {
        "timestamp": "20220302",
        "category": "Administration",
        "tags": ["correlations", "performance"],
        "refs": [ "https://www.misp-project.org/" ],
        "screenshots": [ "https://raw.githubusercontent.com/MISP/misp-website/new/assets/assets/images/misp-small.png"],
        "value": "tip"
    }
```

Each tip as an entry. Most recent entry is the first in the list.
* Timestamp: date in YYYYMMDD
* Category: Administration, Threatintel, Misc
* Tags: list of tags
* Refs: list of external references
* Screenshots: list of screenshots (put the files on Github)
* Entry: text

"""

try:

    f = open(jsonfile)
    data = json.load(f)

    f_md = open(mdfile, "w")
    f_md.write(prenote)

    for el in data["entry"]:
        ts = el["timestamp"]
        category = el["category"]
        entry = el["value"]
        refs = ""
        for t in el["refs"]:
            refs = refs + "[{}]({}) \n".format(t, t)
        screenshots = ""
        for t in el["screenshots"]:
            screenshots = screenshots + "![]({}) \n".format(t, t)            
        tags = ""
        for t in el["tags"]:
            tags = tags + "*{}* ".format(t)

        note = """
{} **{}** {}

>{}

{} 

{}

*** 

""".format(ts, category, tags, entry, screenshots, refs)
        f_md.write(note)

    f_md.write(postnote)

    f_md.close()

        
except Exception as ex:
    print("could not open or parse json input file. Reason: %s" %str(ex))
    sys.exit(-2)