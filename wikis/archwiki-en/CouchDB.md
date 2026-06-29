# CouchDB

"Apache CouchDB is a document-oriented database that can be queried and indexed in a MapReduce fashion using JavaScript." ― CouchDB homepage

## Installation
Install the  package.

## Usage
Before you start the application, you need to create admin account as follows After starting CouchDB for the first time,  will be replaced with the hashed version.

Next, start/enable the  daemon.

Test to see if the service is running by running . Note that in order to access this instance of CouchDB from another system, you will need to configure it (see below).

## Using Fauxton admin interface
You can now access the Fauxton admin interface by going to [http://localhost:5984/_utils http://localhost:5984/_utils.

## Configuration
You can do this through Fauxton or using command line.

To setup the database and create an admin account through Fauxton, visit http://127.0.0.1:5984/_utils/#setup.

To setup a single node from the command line (where  and  are to be replaced).

 $ curl -X POST -H "Content-Type: application/json" http://127.0.0.1:5984/_cluster_setup -d '{"action": "enable_single_node", "bind_address":"127.0.0.1", "username": "", "password": ""}'

Also, you might want to take a look at #Single node setup & Security.

Note that you can also do all this as well as changing the default port, bind address, log-level and other useful nuggets in .

If you want to run CouchDB on port 80 you will have to run the daemon as root, use a reverse proxy or set an iptables rule such as:

 $ iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-ports 5984

## Creating a self-signed certificate
If you would like to use ssl with a self-signed certificate you can create one like this:

 # cd /etc/couchdb
 # openssl req -new -x509 -nodes -newkey rsa:4096 -keyout server.key -out server.crt

Then uncomment httpsd and update the paths in  and  sections:

{{hc|/etc/couchdb/local.ini|2=
httpsd = {couch_httpd, start_link, [https}

cert_file = /etc/couchdb/server.crt
key_file = /etc/couchdb/server.key
}}

Fauxton can then be accessed over SSL on port 6984 via [https://localhost:6984/_utils/ https://localhost:6984/_utils/.

## Single node setup & Security
If you run CouchDB in a single node setup, you might want to increase security by not binding unnecessarily on public network interfaces. Two process are actually doing so:  and . The first one is quite easy to work around, you can simply add the following systemd drop-in addition to :

The second one needs an edit in
{{hc|/etc/couchdb/vm.args|2=
-kernel inet_dist_use_interface {127,0,0,1}
}}
