# MongoDB Role

### Description

This role installs MongoDB to a server. It's currently basic in features, although it does support basic replica set configuration, you need to manually add or remove nodes from the replica set.

### TODO:

1. Add support for parameterising replica set configuration so that replicasets can be built easily from a single playbook, specifying the hosts that a node should join in the replicaset.