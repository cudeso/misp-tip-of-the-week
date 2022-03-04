# MISP Tip of the Week

A collection of tips for using [MISP](https://www.misp-project.org/). Published via [BelgoMISP](https://twitter.com/belgomisp) (*todo*) and this repository. Available in MD and [JSON](https://raw.githubusercontent.com/cudeso/misp-tip-of-the-week/main/misp-tip-of-the-week.json). 

Do you want to **contribute**? [Suggest a tip](https://github.com/cudeso/misp-tip-of-the-week/issues/new/choose) via a Github issue or do a PR to the JSON file.


# Tips of the Week


20220302 **Administration** *workers* *jobs* 

>You can get the number of pending jobs in the MISP workers via {misp_url}/servers/getWorkers .

 

[https://www.misp-project.org/2020/08/22/MISP-Monitoring-with-Cacti.html/](https://www.misp-project.org/2020/08/22/MISP-Monitoring-with-Cacti.html/)

*** 


20220302 **Administration** *usermanagement* 

>Reset the password of a user via the CLI /var/www/MISP/app/Console/cake Password user@domain.cti Password1234

 



*** 


20220302 **Administration** *correlations* *performance* 

>Correlations aren’t cached, this means that they are requested (counted) every time when accessing the event index page. You can get a huge performance increase on the event index page by disabling MISP.showCorrelationsOnIndex.

 

[https://www.vanimpe.eu/2021/03/25/staying-in-control-of-misp-correlations/](https://www.vanimpe.eu/2021/03/25/staying-in-control-of-misp-correlations/)

*** 



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

