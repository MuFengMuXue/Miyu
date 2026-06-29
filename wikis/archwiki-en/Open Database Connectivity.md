# Open Database Connectivity

Open Database Connectivity, commonly ODBC, is an open specification for providing application developers with a predictable API with which to access Data Sources.
An ODBC engine needs drivers to be able to interact with databases.

## ODBC engines
You have two options to chose from: unixODBC and iODBC. Apparently unixODBC is more widely supported. This document shows how to set up unixODBC. First to access your database on your localhost and then extends the steps to configure MySQL to allow remote access through ODBC.

Additionally you can choose from various Devart ODBC drivers for SQL Server, Oracle, MySQL, SQLite, Firebird, PostgreSQL, Interbase.

## Installation
Install the  package.

## Configuration
Driver are declared in , and connections in . More instruction at each driver section.

## Drivers
## FreeTDS
FreeTDS is a set of libraries for Unix and Linux that allows your programs to natively talk to Microsoft SQL Server and Sybase databases. Technically speaking, FreeTDS is an open source implementation of the TDS (Tabular Data Stream) protocol used by these databases for their own clients.

## Installation
Install the  package.

## Configuration
The configuration file of FreeTDS itself is .

## Myodbc
Myodbc is ODBC driver/connector for mariadb.

## Installation
Install the  package.

## Configuration
Starting with , which lists all installed drivers.

## SQLite
sqliteodbc is ODBC driver/connector for sqlite.

## Installation
Install the  package.

## Configuration
Starting with , which lists all installed drivers.

## PostgreSQL
psqlodbc is ODBC driver/connector for PostgreSQL.

## Installation
Install the  package.

## Configuration
Starting with , which lists all installed drivers.

## Databases
## Microsoft SQL Server 2000
SQL Server ODBC driver connection strings and configuration guide

## Mariadb
Set up your data sources in  (system wide) or  (current user). If a data source is defined in both of these files, the one in your home directory take precedence.

MariaDB ODBC driver connection strings and configuration guide

## Create a test database
Create a new database "test". You can use one of the MySQL front-ends such as , or the command-line mysqladmin command:
 $ mysqladmin -h localhost -u root -p create test

## Testing the ODBC
To test the ODBC connection
 $ isql MySQL-test

If the connection is established, you will see
 +---------------------------------------+
 | Connected!                            |
 |                                       |
 | sql-statement                         |
 | help tablename                      |
 | quit                                  |
 |                                       |
 +---------------------------------------+
 SQL>

If you have a problem connecting then check the error message by running
 $ isql MySQL-test -v

## A couple useful websites
https://www.unixodbc.org/doc/OOoMySQL.pdf

This website got me going on ODBC with MySQL but left out some things that were necessary for me
to get isql up and running. However this might be a good reference for the OpenOffice part.

http://mail.easysoft.com/pipermail/unixodbc-support/2004-August/000111.html

To work around error messages this URL proved helpful so here it is as well.

## Postgresql
Set up your data sources in  (system wide) or  (current user). If a data source is defined in both of these files, the one in your home directory take precedence.

## Virtuoso / SPARQL
Opening a connection using the default credentials (username: "dba", password: "dba"):
 $ isql VOS dba dba

## SQLite
Setup  by assign the sqlite file location.
