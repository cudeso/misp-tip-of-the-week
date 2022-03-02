# MISP Tip of the Week

A collection of tips for using [MISP](https://www.misp-project.org/). Published via [BelgoMISP](https://twitter.com/belgomisp) and this repository. Available in MD and [JSON](https://raw.githubusercontent.com/cudeso/misp-tip-of-the-week/misp-tip-of-the-week.json). **(still testing, launch for 202204)**

# Tips of the Week


20220302 **Administration** *workers* *jobs* 

>You can get the number of pending jobs in the MISP workers via {misp_url}/servers/getWorkers .

*** 


20220302 **Administration** *correlations* *performance* 

>Correlations aren’t cached, this means that they are requested (counted) every time when accessing the event index page. You can get a huge performance increase on the event index page by disabling MISP.showCorrelationsOnIndex.

*** 



# JSON format

Each tip as an entry. Most recent entry is the first in the list.
* Timestamp: date in YYYYMMDD
* Category: Administration, Threatintel, Misc
* Tags: list of tags
* Entry: text

