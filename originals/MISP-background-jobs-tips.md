# MISP Background Jobs

Tips when setting up the new MISP background jobs backend. Also see the [Background jobs migration guide](https://github.com/MISP/MISP/blob/2.4/docs/background-jobs-migration-guide.md).


### "Your requirements could not be resolved to an installable set of package"
This occurs when installing the required PHP packages (despite using the '--with-all-dependencies' option) and not all package upgrades are done automatically.
> From the `/var/www/MISP/app` directory, first manually upgrade the composer packages with `sudo -u www-data php composer.phar update`. Then continue with the installation procedure `sudo -u www-data php composer.phar require --with-all-dependencies ...`

### "An Internal Error Has Occurred." when accessing the diagnostics page

Along with this message, the log `/var/www/MISP/app/tmp/logs/debug.log` contains 
```
Notice: Notice (8): Undefined index: supervisor_host in [/var/www/MISP/app/Lib/Tools/BackgroundJobsTool.php, line 630]
```
(the message can be different, and also refer to redis_host, redis_namespace or other configuration settings). This is because not all configuration settings are already stored in the MISP config file. 
> Edit `/var/www/MISP/app/Config/config.php`, add the configuration settings for the background jobs, save and retry again.
```
  'SimpleBackgroundJobs' =>
  array (
    'enabled' => true,
    'supervisor_password' => 'PWD_CHANGE_ME',
    'redis_host' => '127.0.0.1',
    'redis_port' => 6379,
    'redis_namespace' => 'background_jobs',
    'redis_database' => 1,
    'redis_password' => 'PWD_REDIS_CHANGE_ME',
    'supervisor_host' => '127.0.0.1',
    'supervisor_port' => 9001,
    'supervisor_user' => 'supervisor',
    'max_job_history_ttl' => 86400,
  ),
```

### "Warning: MISP cannot connect to the Supervisord API

A message when accessing the workers page, along with the alert `check the following settings are correct: [supervisor_host, supervisor_port, supervisor_user, supervisor_password] and restart the service. For details check the MISP error logs."`. In the MISP error logs you will find `An error occured when getting the workers statuses via Supervisor API: Connection refused for URI http://127.0.0.1:9001/RPC2`.

This occurs because the inet_http_server configuration setting is not added to supervisord, or that you have used a wrong password.

> Edit `/etc/supervisor/supervisord.conf` and add 
```
[inet_http_server]
port=127.0.0.1:9001
username=supervisor
password=PWD_CHANGE_ME
```

### Supervisord processes exit immediately

When you restart supervisord you can see the helper scripts spawning and exiting immidiately. This can be seen in the syslog.

```
2022-07-20 18:38:51,738 INFO spawned: 'update_00' with pid 50387
2022-07-20 18:38:51,760 INFO exited: default_01 (exit status 1; not expected)
```

This is because the new background jobs backend in MISP has not yet been enabled.

> Enable the new backend in `servers/serverSettings/SimpleBackgroundJobs`
