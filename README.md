# MISP Tip of the Week

A collection of tips for using [MISP](https://www.misp-project.org/). Published via [BelgoMISP](https://twitter.com/belgomisp) (*todo*) and this repository. Available in MD and [JSON](https://raw.githubusercontent.com/cudeso/misp-tip-of-the-week/main/misp-tip-of-the-week.json). 

Do you want to **contribute**? [Suggest a tip](https://github.com/cudeso/misp-tip-of-the-week/issues/new/choose) via a Github issue or do a PR to the JSON file.


# Tips of the Week


20220520 **Administration** *sharing* *distribution* *usermanagement* 

>Use sharing groups to setup re-usable distribution lists for sharing threat events with different communities ('multi-tenancy'-ish). Watch a video https://vimeo.com/710012285 on basic usage of sharing groups.

 

[https://vimeo.com/710012285](https://vimeo.com/710012285)

*** 


20220512 **Administration** *correlation* *database* *performance* 

>Regularly remove orphaned attributes or correlations via the diagnostics page or remove orphaned correlations via the CLI 'cake admin removeOrphanedCorrelations'. And don't forget to run 'optimize table correlations' in the mysql console.

![](https://user-images.githubusercontent.com/256028/167998212-37a57623-66c2-4803-8f46-013860bf41e8.jpg)![](https://user-images.githubusercontent.com/256028/167999051-7f0e1f7b-82e3-49d0-a51b-5b290cda33d9.jpg) 

[https://www.vanimpe.eu/2021/03/25/staying-in-control-of-misp-correlations/](https://www.vanimpe.eu/2021/03/25/staying-in-control-of-misp-correlations/)

*** 


20220505 **Threatintel** *feeds* 

>You can use MISP feeds without having to import the events in your instance. Use them as 'lookup' to check if there is OSINT on an indicator. BONUS: create a custom feed from your ticketing system and lookup incident data/occurrences.

![](https://user-images.githubusercontent.com/256028/166990384-35e28137-f70a-461e-9fd2-fd40cf35b5ef.jpg) 



*** 


20220429 **Threatintel** *scraping* *reports* 

>Did you know you can use MISP as a simple web scraper? Automatically convert HTML from a remote website into Markdown and extract useful threat tactics, techniques and indicators. Enable module 'html_to_markdown' and create MISP reports from a URL. Or do it via the API (see pseudo-code).

![](https://user-images.githubusercontent.com/256028/165084117-4d2ed631-6e1c-430c-ba1b-64e262387cd5.jpg) 



*** 


20220422 **Threatintel** *taxonomy* *tlp* *classification* 

>Make it mandatory for MISP event publishers to add a TLP designation to their events. Set the 'Required' checkbox under the TLP taxonomy in taxonomies/index.

![](https://user-images.githubusercontent.com/256028/162378880-a747cd9f-85a0-40ee-b94e-276a96b9c0ed.jpg) 



*** 


20220415 **Threatintel** *opsec* 

>Use the MISP Event Delegation feature to have events published by another organisations. This way you can guarantee the anonymity of the threat event author. First put the distribution of the event as "your organisation only" and then choose Delegate Publishing.

![](https://user-images.githubusercontent.com/256028/163488531-0e7bba7d-712d-40d1-86f2-ae94bacd2ffd.jpg) 



*** 


20220408 **Administration** *usermanagement* 

>You got an API key but forgot the associated user account? Access 'users/view/me.json' with the API key to get your user details.  curl -k -H "Authorization: API_KEY" https://misp/users/view/me.json

![](https://user-images.githubusercontent.com/256028/162270894-a1f84058-b354-43c1-a1d0-892b25fe5eb4.jpg) 



*** 


20220401 **Misc** *web* *usage* 

>You can change the list of columns in the event overview for cleaner output. For example, remove the 'clusters' and 'creator user' to get additional space to display the event details that are important to you. The changes are automatically stored in your user profile under "event_index_hide_columns".

![](https://user-images.githubusercontent.com/256028/161009689-e348da15-85a9-4091-ade5-fc379d424504.jpg) 



*** 


20220302 **Administration** *workers* *jobs* 

>You can get the number of pending jobs in the MISP workers via {misp_url}/servers/getWorkers .

 

[https://www.misp-project.org/2020/08/22/MISP-Monitoring-with-Cacti.html/](https://www.misp-project.org/2020/08/22/MISP-Monitoring-with-Cacti.html/)

*** 


20220302 **Administration** *usermanagement* 

>Reset the password of a user via the CLI /var/www/MISP/app/Console/cake Password user@domain.cti Password1234

 



*** 


20220302 **Administration** *correlations* *performance* 

>Correlations aren't cached, this means that they are requested (counted) every time when accessing the event index page. You can get a huge performance increase on the event index page by disabling MISP.showCorrelationsOnIndex.

 

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

