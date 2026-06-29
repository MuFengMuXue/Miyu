# Naemon

Naemon is the new monitoring suite that aims to be faster and more stable, while giving you a clearer view of the state of your network.

## Installation
Install .

Copy  to  if you want some example hosts and services to start with.

Install the plugins from  as well as .

## Web interface
Install , then uncomment:

Thruk is a fast, modern GUI. A demo is available at http://thruk.org/demo.html.

## Apache configuration
Add the http user to the naemon group:

 # usermod -aG naemon http

Load modules and include naemon-thruk.conf:

Set the thruk_user and thruk_group to naemon:

Restart  and navigate to http://localhost/thruk/

The default username and password is .
