# Logstash

### Description

This role installs several features of a logstash service.

First, it installs rsyslogd with server services turned on, so the host on which this role is installed becomes an rsyslog server to which other hosts should send their syslog data.

Second, it installs elasticsearch from the elasticsearch role to index the log data.

Thirdly it installs Apache 2.4 from the webserver role, in order to host the kibana web dashboard for logstash and elasticsearch.

One important thing to be aware of is that the Kibana installation is protected by an HTTP Basic Auth rule, with the htpasswd file containing the credentials located in ``/home/logstash/kibana/.htpasswd`. By default the first time you run the playbook on a host, this file will be created but it will be empty. It is your responsibility in your own project's playbooks to create the users that you need in that file, otherwise you won't be able to log in.

Since the webservers role is used to create the Kibana vhost, you will need to specify a ``domainname`` parameter for the vhost.

Also don't forget that this role requires that port 514 be open to the public, both UDP and TCP due to the rsyslog server.

### Parsing Logs

Your best bet for understanding what is currently configured is to look at the requisite configuration files in the role. If you spend some time customising things for your own project but your customisations might be useful, please contribute them back to the role. You can parameterize their inclusion if necessary.