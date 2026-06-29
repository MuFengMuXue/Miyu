# Galera

Galera is a synchronous multi-master cluster for MySQL/InnoDB databases.

## Installation
The two components Galera cluster comprised of are Galera plugin itself and a patched version of MySQL server which connect using wsrep API.

Install the  package. Also you will need  and  packages for rsync method.

Start/Enable the  daemon.

## Configuration
You need to configure the cluster.

On each node edit  and update the  variable so it contains the list of all nodes in the cluster:

Change the variables  and  to the IP address/hostname and name (this does not need to be unique) for each node, e.g.:

The  variable should contain the same name for all cluster nodes:

Also, set  to the desired state snapshot transfer method, the preferred one is rsync.

Make sure you also set the following options:

When you have finished with , bootstrap the mysqld service on the first node (ONLY on the first node):

 # galera_new_cluster

This will bootstrap the cluster. Use MySQL's command line tool to log in as root into your MySQL server:

 $ mysql -p -u root

Check the status of the cluster, this will show you wsrep-related status variables:

If you use the xtrabackup or mysqldump SST method, you will need to create a MySQL user for sst transfers.

Once you configured the first node, you should be able to start .
