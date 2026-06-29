# OpenVAS

OpenVAS stands for Open Vulnerability Assessment System and is a network security scanner with associated tools like a graphical user front-end. The core component is a server with a set of network vulnerability tests (NVTs) to detect security problems in remote systems and applications.

## Pre-install
## PostgreSQL
Set up PostgreSQL before you continue.

## Redis
Configure Redis as prescribed by the OpenVAS redis configuration. In summary, amend the following to your :

 port 0
 unixsocket /run/redis/redis.sock
 unixsocketperm 770
 timeout 0
 databases 128

Finally restart .

## Installation
Install the following packages to get a full OpenVAS setup, including manager, web frontend, scanner, and so on: , , , , .  needs to be installed for the scanner to deliver proper results and  is needed for PDF report feature to work.

## Initial setup
Setup the PostgreSQL DB for gvm:

 createuser gvm
 [postgres$ createdb -O gvm gvmd

Grant this user DBA roles:

 psql gvmd
 # create role dba with superuser noinherit;
 # grant dba to gvm;
 # create extension "uuid-ossp";
 # \q

Make sure to have the following sysctl configurations:

 # echo "net.core.somaxconn = 1024" >> /etc/sysctl.d/90-openvas.conf
 # echo "vm.overcommit_memory = 1" >> /etc/sysctl.d/90-openvas.conf
 # sysctl -p /etc/sysctl.d/90-openvas.conf

Before doing this check the values of somaxconn (normally this is 4096 for Arch Linux and does not need to be adjusted:

 # sysctl -a | grep somaxconn

If this is the case just skip the first echo line.

Grant the gvm user access to the redis socket:

 # usermod -aG redis gvm
 # echo "db_address = /run/redis/redis.sock" > /etc/openvas/openvas.conf
 # chown gvm:gvm /etc/openvas/openvas.conf

Update NVTs:

 # chown -R gvm:gvm /var/lib/openvas
 [gvm$ greenbone-nvt-sync && openvas --update-vt-info

Update feeds:

 greenbone-feed-sync --type GVMD_DATA
 [gvm$ greenbone-scapdata-sync --rsync
 greenbone-certdata-sync --rsync

You can enable the following timers to update these data on a frequently basis: , , , .

Create certificates for the server and clients, default values were used:

 [gvm$ gvm-manage-certs -a

Add an administrator user account, be sure to copy the password:

 gvmd --create-user=admin --role=Admin

You can also change the password of the user later on

 [gvm$ gvmd --user=admin --new-password=

## Getting started
Start ,  and .

Create the Scanner:

 gvmd --get-scanners

Copy the id of the OpenVAS Default scanner and run:

 [gvm$ gvmd --modify-scanner=id-of-scanner --scanner-host=/run/gvm/ospd.sock
 gvmd --verify-scanner=id-of-scanner

Set the feed import user:

 [gvm$ gvmd --get-users --verbose

Copy the id of the admin user and run:

 gvmd --modify-setting 78eceaec-3385-11ea-b237-28d24461215b --value id-of-admin

Point your web browser to http://127.0.0.1 and login with your admin credentials.
