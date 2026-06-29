# MySQL

MySQL is a widely spread, multi-threaded, multi-user SQL database, developed by Oracle.

## Installation
Arch Linux favors MariaDB, a community-developed fork of MySQL, aiming for drop-in compatibility.

Oracle's MySQL was dropped to the AUR: .

Another fork aiming to be fully compatible is Percona Server, available as .

The InnoDB storage engine by Oracle was also forked by Percona as XtraDB. The fork is used by both MariaDB and Percona Server.

## Graphical tools
*
*

For tools supporting multiple DBMSs, see List of applications/Documents#Database tools.

## Console tools
*

## Programmatic access
* JDBC and MySQL
* PHP#MySQL/MariaDB
* Python
**
**
* C++
**
* Perl
**
* Ruby
**

## Docker
A docker image is available: https://hub.docker.com/_/mysql

## Troubleshooting
## Cannot connect to local MySQL server through socket
If running a new container fails to start, you may need to increase the ulimit. See GitHub issue for more information.
