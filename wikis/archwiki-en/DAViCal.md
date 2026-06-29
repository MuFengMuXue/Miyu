# DAViCal

DAViCal is a server implementing the CalDAV and CardDAV protocol. It is solely a server, with minimal direct user interaction, instead relying on using CalDav clients, such as Apple's iCal.app, iOS (iPhone, iPad, iPod), Thunderbird with Sunbird, or Evolution.

## Installation
## Installing pre-requisites
DAViCal is written in PHP and uses the PostgreSQL database as its backend to store the calendar information. Currently it only supports PostgreSQL, but there is work to support other databases as well.

Install , , , and .

The installation directories are defined by Web application package guidelines and are slightly different than upstream documentation ( and ).

DAViCal is a web application, and therefore you need a web server set up as well. Here Nginx will be assumed, but DAViCal can run on nearly any web server (some may stop processing requests when they see the CalDAV HTTP headers, and therefore DAViCal will not be able to see them).

## Preparing PostgreSQL
First of all, you should set up PostgreSQL so it can start up by following PostgreSQL#Installation.

DAViCal requires two independent accounts to be set up, one for accessing the database from the web application, which will be limited in power, and another that will be used for administrating the DAViCal related tables.

In order to do so, you will need to edit :

Add the following lines:

    local   davical         davical_app                             trust
    local   davical         davical_dba                             trust

Make sure that you have a 'root' role in your database. If you do not, create it by becoming the postgres user as described on PostgreSQL page and execute the following:
 $ createuser -s -U postgres --interactive
 $ Enter name of role to add: root

Prepare database by running create-database.sh script as root:

 # /usr/share/webapps/davical/dba/create-database.sh

Then run createdb as root:

 # createdb

If your PostgreSQL server is on a remote host, use DAViCal PostgreSQL_Config instead of the instructions above.
