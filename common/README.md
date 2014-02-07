# Common

This role contains all setup tasks that should be common to a node. This should be considered the first role that one should run when setting up a brand new node.

The installed programs differ depending on the value of isproduction.

Here is the list of common packages installed:

    - monit
    - munin-node
    - git
    - ntp
    - curl
    - make
    - python-software-properties
    - pwgen
    - rsyslog


If the variable ``isproduction`` is set to ``False``, the following additional packages are installed:

    - wget
    - zip
    - postfix
    - libpcre3-dev
    - build-essential

If the variable ``ec2_nat`` is set to ``True``, then this host will become a NAT-aware instance when run inside Amazon AWS EC2.
    
As well there are a couple more variables about which you should be aware:

	rsyslog_server_host: [IP/hostname]
		Specifies the host name or IP address of a node configured as an rsyslog server. When this is set, the node being configured will send its syslog 
	information to the host specified by this value.

	graphite_host: [IP/hostname]
		Specifies the host name or IP address of a node configured with the carbon listener for graphite. When this is set, the node will be configured to send all diamond data to the carbon server on the host specified by this value.
		
This common role will also install [diamond](https://github.com/BrightcoveOS/Diamond/wiki) to each node. As above, if ``graphite_host`` is specified, then diamond will send all statistics to that host, however if ``graphite_host`` is not specified then diamond will still be installed and gather statistics, but they will be stored locally on the node in files and deleted after 7 days.

Some non-default Diamond collectors are enabled in this play, you can look in the  ``files/collectors_config/`` directory to see which ones.