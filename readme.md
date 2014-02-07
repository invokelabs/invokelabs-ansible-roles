# Invoke Common Ansible Plays

[TOC]

## Description

These are Ansible plays for particular server roles. The directory structure follow the recommended Ansible directory structure.
Ansible uses the directory structure to auto-locate various needed files during the playbook run. The Ansible documentation outlines
the details of how this structure is used. Please see  [this URL](http://www.ansibleworks.com/docs/playbooks.html#roles "Ansible role directory structure link.") for more information.

Each role mentioned below should also have its own Readme file that you can view for more details.

## Current Roles

1. Webservers
2. MongoDB
3. MySQL
4. Gearman
5. Elasticsearch
6. RabbitMQ
7. Common
8. Stats
9. Logstash
10. Jenkins (OS X Only)

### Webservers

The webserver role will install apache and PHP-FPM.  Apache will be installed with the event MPM, which means that it will handle requests differently than what you may be used to dealing with.  Unlike the standard Apache prefork MPM, the event MPM uses an asynchronous, event-driven I/O model to handle HTTP requests. It is much more predictable in terms of its memory usage.

Apache will also install the modfastgci module if you select the Apache 2.2 option, or use mod_proxy_fcgi if you choose the 2.4 option, through which it will communicate with the backend PHP-FPM processes running on the machine.

PHP-FPM is the PHP FastCGI Process manager. It is the recommended way of running PHP programs for web servers today.

You have the option of using PHP 5.3 or PHP 5.5.

### MongoDB

The MongoDB role will install the latest version of 10gen's MongoDB from the 10gen APT repository. You have the option of initializing a replica set if you include the replicaset.yml play.

### MySQL

The MySQL role encompasses several features, all configurable by parameterization. You can select to install MySQL server, the client libraries, or both.

### Gearman

This role will install the Gearman PPA from the gearman project for Ubuntu, and will install the latest stable version of Gearman Job Server as provided by them for precise pangolin. This is needed because the default version of the Gearman Job Server as provided by ubuntu is buggy and won't work properly. This role is mostly deprecated and not recommended. If you do choose this role, and are using PHP, you should choose a pure-PHP implementation of the client protocol, the C PECL extension is highly unstable.

### Elasticsearch

This role will create a local elasticsearch user and install Elasticsearch version 0.20.6 or 0.90.7 into that user's home directory. It will ensure that the elasticsearch process only runs as that user. It will also install an initd script to ensure that the elasticsearch server can be started like a normal service on the system. You can now run multiple versions of elasticsearch on a single server if necessary.

### RabbitMQ

This role installs the rabbitmq-server package, which allows the server to act as a rabbitmq broker.

### Common

The common role installs several important features.  It ensure that git, monit, rsyslog, diamond, and a few others are installed.  This is where there is still some work to be done, as I'd like to add some simple user account management to the common role.

### Stats

The stats role installs Graphite and statsD. Graphite is a collection of programs that provide several services:

 * Carbon, a daemon that listens on a socket for data, speaking a particular protocol.
 * Whisper, an RRD-style database system that stores time-series data received from Carbon. Like RRD, in order to save space on disk, whisper will average the time-series data according to the schedule you choose.
 * Carbon-UI, a Django and ExtJS-based web front end for interacting with the data stored in whisper-- it allows you to dynamically create graphs by mixing and matching the data in whisper. You can also run computations and analyses on the data from the web UI. You can also set up various dashboards to show the data in interesting ways.
 * StatsD is a program that collects and aggregates data received from other services, and sends them to Carbon for storage in Whisper. The main features of statsD is that it is very easy to integrate with applications, it's very fast, and it does its own data aggregation before sending data to Carbon, which means that together they can handle a very large volume of metrics.
 
In fact the greatest advantage that statsD + Graphite have over any other charting mechanism is that they are extremely fast, space efficient, and scalable even on a single server. It's not uncommon to have a single server storing tens of thousands of metrics per second in near real time, around 15 seconds currently configured.

The webservers role is a dependency.

### Logstash

The logstash role encompasses multiple services just like the stats role, and there is some overlap between the two.

The main feature of the role is that it installs a central syslog server, so that any other nodes in your system can send their syslog output to the logstash role and have the contents of those logs indexed in elasticsearch for later searching, via web front end called Kibana.

The main area of overlap with the stats role is that Kibana can also display charts or graphs of events, however this role is more for log content than application metrics. Additionaly logstash and elasticsearch requires a lot more system resources than graphite and statsD, so you'll need significant investment in instance capacity in order to get scalable performance out of logstash and elasticsearch.

The role installs rsyslog, logstash, and kibana,  and has two role dependencies, webservers and elasticsearch.

### Jenkins

The Jenkins role current installs Jenkins on Mac OS X for the main purpose of providing Continuous Integration services for iOS projects, although in theory there is no reason that a web application couldn't be integrated on OS X as well.

The role is suitable to play against a newly installed version of OS X, with or without Server.app installed.  The role will install several dependencies needed, including Apple's Java for Mac OS X, and the Xcode command line tools. It will also configure local e-mail services so that e-mail can be sent out from localhost. However, you will need to download the Apple Java .pkg file and the Xcode command line tools .pkg file yourself due to licensing restrictions that prevent us from bundling these files with our roles.

The role configures Jenkins for SSL support by default, and can provide a self-signed certificate if you don't have a CA-signed one handy.  It also creates a default jenkins user, and installs the Xcode, CocoaPods, and Testflight plugins.

## Future Roles

Future roles to add:

1. Management Server
2. Memcached Service
3. Redis Service
4. Varnish Service
5. LDAP Service

