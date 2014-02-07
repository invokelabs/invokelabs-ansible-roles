# Stats Role

### Description

The stats role encompasses two main areas of functionality:

* Installation of the statsD NodeJS program.
* Installation and configuration of the graphite database and graphite web front end.

The installation of the two programs is controlled with an ansible variable, ``stats_backend``. When the backend variable is true, then graphite and its dependencies will be installed, as well as nodeJS and statsD.

The backend portion includes a dependency on the webservers role, so even if you don't explicitly install the webservers role, if you specify ``stats_backend=true`` then it will be installed and configured with mod_proxy_uwsgi, and the graphite Django-based backend will be run via uwsgi. Furthermore the backend portion also installs the carbon daemon, which listens on a network socket (currently both UDP and TCP).

Your best bet is to read the playbook and corresponding documentation for graphite, carbon, and whisper, on the respective web sites.

### How Stats are Generated

The main thing to be aware of with this role is that you need to think about the information that you are going to feed it. In particular you should be aware that the common role will allow any node to dump its system-level statistics to graphite. See the readme for common role to see what you need to configure there, it is just one variable that specifies the hostname or IP address for the system that is running this role.

Currently these system level statistics get published via the diamond program, and you have the option of creating your own diamond plugins if you require custom system-level information that wouldn't normally be logged via syslog.

For application-level statistics, it is your responsibility to load a StatsD library of some kind into your application and configure it to send its metrics to the hostname or IP address of the node running this role.

### Django Dashboard

Graphite's web-based UI is written in Django, so you'll need to know a tiny bit about django in order to get the best results from it. The main thing to be aware of is that Django has user authentication built in, but in order to use it you must first create an adminstrative user in django. This is not done by default for you. Secondly if you want to restrict access to the graphs on the UI, you will need to change the configuration to require authentication after you have created at least one administrative user.