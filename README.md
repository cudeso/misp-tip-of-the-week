# MISP Tip of the Week

A collection of tips for using [MISP](https://www.misp-project.org/). Published via [BelgoMISP](https://twitter.com/belgomisp) (*todo*) and this repository. Available in MD and [JSON](https://raw.githubusercontent.com/cudeso/misp-tip-of-the-week/main/misp-tip-of-the-week.json). 

Do you want to **contribute**? [Suggest a tip](https://github.com/cudeso/misp-tip-of-the-week/issues/new/choose) via a Github issue or do a PR to the JSON file.


# Tips of the Week


20221014 **Administration** *security* *hardening* *audit* 

>The MISP diagnostics page contains useful security audit recommendations. Visit Administration > Diagnostics and scroll down to 'Security Audit' to check which settings require a review.

![](https://user-images.githubusercontent.com/256028/195662623-79cad086-1d85-4bc9-84b9-12af9269a61f.png) 



*** 


20221007 **Threatintel** *indicators* *attriobutes* *search* 

>You can search for multiple (substring) MISP attributes at the same time with a '%VALUE%' string per newline. Further refine your search with for example tags and the first seen or last seen of the attributes/values.

![](https://user-images.githubusercontent.com/256028/193765295-666d02c4-3f01-4316-a6f6-66833187f46b.png) 



*** 


20220930 **Threatintel** *enrichment* *modules* 

>The MISP modules can also be used outside MISP. Query the module server for its enabled modules or immediately start using a MISP module with one simple request.

![](https://user-images.githubusercontent.com/256028/192039631-fc60fdb0-f276-4398-be26-e7ef6d3b07f9.png)![](https://user-images.githubusercontent.com/256028/192039637-7f4fb3b8-0a2c-418b-a127-738e0e2cdb97.png) 

[https://github.com/cudeso/misp-tip-of-the-week/blob/main/originals/misp_modules.ipynb](https://github.com/cudeso/misp-tip-of-the-week/blob/main/originals/misp_modules.ipynb) 


*** 


20220923 **Threatintel** *contextualisation* *taxonomy* 

>Use a private taxonomy to describe internal sources, (risk) classifications or workflows. Taxonomies are simple JSON files in 'app/files/taxonomies/<taxonomy>/machinetag.json'. Then 'Update taxonomies' and enable the required tags.

![](https://user-images.githubusercontent.com/256028/191695060-9d93acf9-6343-485c-a8a4-de9404c6a9be.png)![](https://user-images.githubusercontent.com/256028/191697121-c496bea3-b656-4d32-b134-a05c284182f6.png)![](https://user-images.githubusercontent.com/256028/191698588-59194109-8e43-4ca6-ae21-fe841415d83e.png)![](https://user-images.githubusercontent.com/256028/191698789-4ede81d3-952c-422e-9945-d99eb7786943.png) 

[https://www.circl.lu/doc/misp/taxonomy/#adding-a-private-taxonomy](https://www.circl.lu/doc/misp/taxonomy/#adding-a-private-taxonomy) 


*** 


20220916 **Administration** *security* *privacy* 

>Enhance the security of your MISP platform by enabling Content Security Policy (CSP) support and then further configure the policy via the Security.csp setting.

![](https://user-images.githubusercontent.com/256028/190467762-102d26b9-7036-436b-b9ad-d11353232a49.png)![](https://user-images.githubusercontent.com/256028/190468001-5a0d2bf1-9189-491b-85d5-2b90468c3ebc.png)![](https://user-images.githubusercontent.com/256028/190469261-04a31280-0cea-4501-ad91-627181b8d582.png) 

[https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) 


*** 


20220909 **Administration** *workers* *monitoring* 

>Monitor the status of background workers via 'app/Console/cake Admin getWorkers' or an API request to 'servers/getWorkers'. Use Cacti (https://www.misp-project.org/2020/08/22/MISP-Monitoring-with-Cacti.html/) to track the number of jobs in the worker queues.

![](https://user-images.githubusercontent.com/256028/185498557-3fdc0b5d-98de-42c5-8749-540ab1fbdd6a.png)![](https://user-images.githubusercontent.com/256028/176754729-ce2444e4-0536-4b4a-802b-c9cee91b4112.jpg) 

[https://www.misp-project.org/2020/08/22/MISP-Monitoring-with-Cacti.html/](https://www.misp-project.org/2020/08/22/MISP-Monitoring-with-Cacti.html/) 


*** 


20220902 **Administration** *notification* *template* 

>You can change the event notification e-mail template by dropping a custom 'alert.ctp' in 'app/View/Emails/text/Custom'. Use the default template as inspiration.

![](https://user-images.githubusercontent.com/256028/185491172-97a7818a-3cff-4049-956d-d4110cb9f803.png)![](https://user-images.githubusercontent.com/256028/185491176-4a04d5bc-7743-4e4b-9002-eaeec5941085.png) 



*** 


20220826 **Threatintel** *pivoting* *context* 

>The 'Event Graph' helps analysts in understanding details of an event by visually representing attributes in a grouped tree. Make sure to apply filters for events with a lot of attributes.

![](https://user-images.githubusercontent.com/256028/185485314-7063afb9-581d-4215-a859-175e45e849e8.png)![](https://user-images.githubusercontent.com/256028/185485328-bb87f405-dc50-4141-b3cf-42f2e56c9632.png) 



*** 


20220819 **Threatintel** *correlations* *context* 

>Use correlation exclusions (Administration > Top correlations) to avoid unnecessary or irrelevant threat data correlations. Have a look at the Jupyter notebook for an example API usage.

![](https://user-images.githubusercontent.com/256028/185342291-0e00de8d-f440-4bfb-bd17-c5e8e52ea61f.png)![](https://user-images.githubusercontent.com/256028/185340370-fb9541b8-58a3-4a25-8bbb-ce79995f55b7.png)![](https://user-images.githubusercontent.com/256028/185340390-73d2e1fd-d6e0-4b05-8992-2af76e5797c0.png)![](https://user-images.githubusercontent.com/256028/185340393-864b5b3c-7635-47fd-87fa-67d47ff4fca6.png) 

[https://github.com/cudeso/misp-tip-of-the-week/blob/main/originals/misp_add_correlation_exclusion.ipynb](https://github.com/cudeso/misp-tip-of-the-week/blob/main/originals/misp_add_correlation_exclusion.ipynb) 


*** 


20220812 **Administration** *authentication* *usermanagement* *password* 

>You can set the minimum password length 'Security.password_policy_length' (default 12) and complexity 'Security.password_policy_complexity' (https://regexr.com/6oren) via Server Settings & Maintenance>Security Settings.

![](https://user-images.githubusercontent.com/256028/176716402-dfcd81da-d40c-4a41-9ed0-92435033a454.jpg) 

[https://regexr.com/6oren](https://regexr.com/6oren) 


*** 


20220805 **Administration** *samples* *malware* *php* 

>If you store (large) malware samples in MISP and run into '500: Internal Server Error' then it's time to increase the file upload limits in PHP. Change upload_max_filesize and post_max_size and restart Apache.

![](https://user-images.githubusercontent.com/256028/175075817-44f8bef7-0c4f-45de-8c6c-b25b06ab16ec.jpg) 

[]() 


*** 


20220729 **Misc** *web* *usage* *customisation* 

>Bored with the looks and feel of the MISP interface? You can customise it easily with a bootstrap theme from https://bootswatch.com/2/ (or build your own). Copy the CSS to 'app/webroot/css/' and set MISP.custom_css. Share your art-work!

![](https://user-images.githubusercontent.com/256028/180954083-54f5802d-7927-4235-b2fa-08720a6d94bf.jpg) 

[]() 


*** 


20220722 **Administration** *workers* *backgroundjobs* 

>If you have not already done so, now is a good time to migrate the MISP background jobs backend to supervisord (CakeResque is no longer maintained). Use the migration guide and some of the tips to get started.

![](https://user-images.githubusercontent.com/256028/180070173-72af9081-09d2-48a9-b2ae-e8f9ae860dbb.jpg)![](https://user-images.githubusercontent.com/256028/180070182-90de5c9b-d216-40fa-8f5c-54890ea08540.jpg)![](https://user-images.githubusercontent.com/256028/180070157-b3fec255-33e2-4d39-b626-97d730b27487.jpg)![](https://user-images.githubusercontent.com/256028/180072428-965f1d6c-6321-471d-849e-ffe3b6cd8729.jpg) 

[https://github.com/cudeso/misp-tip-of-the-week/blob/main/originals/MISP-background-jobs-tips.md](https://github.com/cudeso/misp-tip-of-the-week/blob/main/originals/MISP-background-jobs-tips.md) 
[https://github.com/MISP/MISP/blob/2.4/docs/background-jobs-migration-guide.md](https://github.com/MISP/MISP/blob/2.4/docs/background-jobs-migration-guide.md) 


*** 


20220715 **Threatintel** *quality* *indicators* *attributes* 

>Quality is more important than quantity in threat intelligence. MISP warns you if you add redundant or similar information to threat events. This works for both objects and attributes.

![](https://user-images.githubusercontent.com/256028/178993140-ffaad442-b928-4147-856f-48dbeae529be.jpg)![](https://user-images.githubusercontent.com/256028/178993281-fc316a34-c071-4da7-b60b-9ba5121b31e5.jpg)![](https://user-images.githubusercontent.com/256028/178993286-152957d9-188e-478a-b95b-e9a08622f103.jpg) 



*** 


20220708 **Administration** *optimisation* *usermanagement* 

>It's a good idea to assign additional MISP system resources to scripts that collect large sets of data (or for users that do a lot of data crunching). Create a dedicated user role and set the memory limit and execution time.

![](https://user-images.githubusercontent.com/256028/175073724-25b93e43-96bb-40c7-98e2-187726a7eb0e.jpg) 



*** 


20220701 **Administration** *stix* *taxii* *conversion* 

>You can use the STIX 2 MISP conversion script (app/files/scripts/stix2misp.py or https://github.com/MISP/MISP/blob/2.4/app/files/scripts/stix2misp.py) outside the MISP web UI to manually convert STIX files to (MISP) JSON format. Output files are written in the tmp directory.

![](https://user-images.githubusercontent.com/256028/176549080-f822d0dc-22aa-48fa-a694-d6aaec005105.jpg) 



*** 


20220624 **Threatintel** *contextualisation* *taxonomy* *tags* 

>Instead of global tags use local tags from a private taxonomy to contextualise events with the specifics of your company environment. These local tags are stripped from events when shared (synced) with external communities.

![](https://user-images.githubusercontent.com/256028/175109726-e257efad-6156-48d3-8c5a-4dbb7af17b25.jpg) 



*** 


20220617 **Administration** *backups* *bcp* 

>Backups are important! Use the built-in MISP backup script (tools/misp-backup/misp-backup.sh) to create backups (or snapshots). Backups include data and config and can be restored over an existing MISP install.

![](https://user-images.githubusercontent.com/256028/166995861-7bb25fe8-8966-42af-98ec-3be2d2dd159e.jpg)![](https://user-images.githubusercontent.com/256028/166995886-f1f18267-17b5-49b3-86bf-d2be1cfe0df3.jpg) 



*** 


20220610 **Threatintel** *automation* *pymisp* *procedures* 

>Document your CTI operational procedures with Jupyter notebooks and PyMISP. Use the examples at https://github.com/cudeso/misp-tip-of-the-week/tree/main/originals and https://github.com/MISP/PyMISP/tree/main/docs/tutorial to get started.

![](https://user-images.githubusercontent.com/256028/172591533-14aa943d-ea95-4417-b6c8-3b7a3f70975b.jpg)![](https://user-images.githubusercontent.com/256028/172591539-260069a0-4308-4330-9ba2-f949c3c74efb.jpg)![](https://user-images.githubusercontent.com/256028/172591544-290f472b-2ece-49ad-af12-2009e5074145.jpg)![](https://user-images.githubusercontent.com/256028/172591550-e184b186-308b-42f8-9e88-532de7e4fd53.jpg) 



*** 


20220603 **Administration** *usermanagement* *organisations* 

>You can combine ('merge') an organisation with another and basically transfer all the users and data from one organisation to another. First edit the organisation, and then choose Merge in the left menu.

![](https://user-images.githubusercontent.com/256028/171633007-e786e755-cb54-4dba-ad44-0fc43b8d06e2.jpg)![](https://user-images.githubusercontent.com/256028/171632946-63c9cab6-498c-46ab-8fad-3507c3001089.jpg) 



*** 


20220527 **Administration** *logging* *auditing* 

>The API /admin/logs supports different models that can be used for audit reports. Track the latest changes on events, attributes, authentication actions and password resets and alert on unusual behaviour. Supported models include Attribute, Event, Role, Server, Taxonomy, User and many more.

![](https://user-images.githubusercontent.com/256028/166974608-2045a847-f752-4b42-bc4c-e0503719386e.jpg)![](https://user-images.githubusercontent.com/256028/170514624-b93c74d1-31ec-4b0c-a787-133d3ac64910.jpg)![](https://user-images.githubusercontent.com/256028/170516230-8f6ddd70-b438-4f60-afc9-2708314eb09f.jpg) 



*** 


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

