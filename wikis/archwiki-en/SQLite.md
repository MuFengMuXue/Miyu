# SQLite

From the project home page:
:SQLite is a software library that implements a self-contained, serverless, zero-configuration, transactional SQL database engine. SQLite is the most widely deployed SQL database engine in the world. The source code for SQLite is in the public domain.

## Installation
Install the  package.

Related packages are:

*  – most of the static HTML files that comprise this website, including all of the SQL Syntax and the C/C++ interface specs and other miscellaneous documentation *  –  is a command-line utility program that measures and displays how much and how efficiently space is used by individual tables and indexes with an SQLite database file [https://www.sqlite.org/sqlanalyze.html
*  – the Tcl interface to the SQLite library *  – sqlite3 module for PHP (do not forget to enable it in )
*  – Ruby bindings for the SQLite3 embedded database
*  – Gambas3 Sqlite3 database access component

## Using sqlite3 command line shell
The SQLite library includes a simple command-line utility named sqlite3 that allows the user to manually enter and execute SQL commands against an SQLite database.

## Create a database
 $ sqlite3 databasename

## Create table
 sqlite> create table tblone(one varchar(10), two smallint);

## Insert data
 sqlite> insert into tblone values('helloworld',20);
 sqlite> insert into tblone values('archlinux', 30);

## Search database
See the [https://www.sqlite.org/docs.html sqlite docs.

## Software
*
*
*

For tools supporting multiple DBMSs, see List of applications/Documents#Database tools.

## Using sqlite in shell script
See forum post.
