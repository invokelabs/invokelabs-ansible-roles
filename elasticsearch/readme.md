# Elasticsearch Role

### Description

The elasticsearch role installs an elasticsearch service to a node.

### Features

The features of the role are primarily that it allows more than one version of elasticsearch to run on the same node, and that it ensures that elasticsearch runs as an unprivileged user in its own home directory.

### Versions

The role comes packaged with two versions of elasticsearch, ``0.20.6`` and ``0.90.7``.  The former was simply the latest stable version when the role was first created, and the latter is the stable version at the time the role was updated.

### Default Variables

Please view the ``defaults/main.yml`` file for a list of the configuration variables available.