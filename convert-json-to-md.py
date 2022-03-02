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

A collection of tips for using [MISP](https://www.misp-project.org/). Published via [BelgoMISP](https://twitter.com/belgomisp) and this repository. Available in MD and [JSON](https://raw.githubusercontent.com/cudeso/misp-tip-of-the-week/misp-tip-of-the-week.json). **(still testing, launch for 202204)**

# Tips of the Week

"""

postnote = """

# JSON format

Each tip as an entry. Most recent entry is the first in the list.
* Timestamp: date in YYYYMMDD
* Category: Administration, Threatintel, Misc
* Tags: list of tags
* Entry: text

"""

if True: #try:

    f = open(jsonfile)
    data = json.load(f)

    f_md = open(mdfile, "w")
    f_md.write(prenote)

    for el in data["entry"]:
        ts = el["timestamp"]
        category = el["category"]
        entry = el["value"]
        tags = ""
        for t in el["tags"]:
            tags = tags + "*{}* ".format(t)

        note = """
{} **{}** {}

>{}

*** 

""".format(ts, category, tags, entry)
        f_md.write(note)

    f_md.write(postnote)

    f_md.close()

        
#except Exception as ex:
#    print("could not open or parse json input file. Reason: %s" %str(ex))
#    sys.exit(-2)