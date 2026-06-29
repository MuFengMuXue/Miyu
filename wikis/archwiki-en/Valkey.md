# Valkey

From Wikipedia:Valkey:
:Valkey is an open-source in-memory key–value database, used as a distributed cache and message broker, with optional durability.

## Installation
Install the  package.

Start/enable .

## Client-side software
* Python:
* PHP:
* C:

## Configuration
The Valkey configuration file is well-documented and located at .

* Accept connections on the specified port (default is 6379), specify  to disable listening on TCP:
 port 6379

## Listen on socket
Using Valkey over a Unix socket may give a performance increase, compared to TCP/IP https://valkey.io/topics/benchmark/.

The following changes should be made in  to enable use of the unix socket:

* Enable and update the Valkey socket path:
 unixsocket /run/valkey/valkey.sock

* Set permission to the socket to all members of the  user group:
 unixsocketperm 770

* Add users (e.g. "git", "http") to the  user group so they can access and use the socket.

Finally restart the .

## Troubleshooting
## Warning about Transparent Huge Pages (THP)
To solve warning messages as "you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Valkey", you may want to permanently disable this feature:

## Warning about TCP backlog
To solve warning messages as "The TCP backlog setting of 511 cannot be enforced because /proc/sys/net/core/somaxconn is set to the lower value of 128", increase the current value:

## Warning about overcommit_memory is set to 0
To solve warning messages as "overcommit_memory is set to 0! Background save may fail under low memory condition":

## Tips and tricks
## Enabling tab autocompletion
## Zsh
You can leverage  completion script from . To map  completion script to , put the following line to :
