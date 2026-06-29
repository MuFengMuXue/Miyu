# RethinkDB

RethinkDB is a document-oriented database similar to MongoDB but aims to overcome scalability and practical limitation of the latter. [https://www.rethinkdb.com/blog/mongodb-biased-comparison/ RethinkDB is built to store JSON documents, and scale to multiple machines with very little effort. It has a pleasant query language that supports queries such as table joins and group by. It is easy to setup and learn.

## Installation
Install  from the official repositories.

Create and set user rights for RethinkDB folder:

 # mkdir /var/lib/rethinkdb/default
 # chown -R rethinkdb:rethinkdb /var/lib/rethinkdb/

Now you can start  from the command-line:

 # rethinkdb

Alternatively, start and enable .

RethinkDB's admin UI is now available on port 8080.

## Configuration
RethinkDB has multi-instance support, which means you can run several independent database instances on the same machine. The systemd service also supports multi-instance configuration.

To create a new RethinkDB instance, create its configuration file:

 # cd /etc/rethinkdb
 # cp instances.d/default.conf instances.d/Name.conf

where Name represents the configuration you will be using later. Change the configuration options in the new file. Then start/enable .

The 'default' instance is created at installation time for your convenience. Its data is stored in .
