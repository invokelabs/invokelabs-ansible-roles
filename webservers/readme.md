# Webserver Role

The webserver role encompasses two main areas of functionality:

 * Installation and configuration of Apache 2.2 or Apache 2.4
 * Installation and configuration of PHP 5.3 or PHP 5.5
 
Your best guide on how it works and what its configuration requirements are is to look at the defaults/main.yml file, which contains default values for all configuration variables. You should also probably read the tasks involved, they are fairly simple.

Currently you can mix the different versions of Apache and PHP, so for example you do not have to use Apache 2.4 just to run PHP 5.5 and you don't need Apache 2.2 to run PHP 5.3.  However, you cannot have both versions of Apache or both versions of PHP currently installed at the same time. Attempting to configure the system in that way will result in an error.

The default configuration is to use Apache 2.2 and PHP 5.3.

### Notable Parameters

As above, understanding what is parameterisable is best achieved by looking at the default variables for the role in ``defaults/main.yml`` but one useful parameter is ``additional_vhost_config`` that you can specify as a string of ``\n`` separated Apache configuration directives.