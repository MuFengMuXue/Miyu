# KiwiIRC

KiwiIRC is a hand-crafted IRC client that you can enjoy. Designed to be used easily and freely.

## Installation
Install either  or .

## Running
## Apache
Create the Apache configuration file:

And include it in :

After making changes to the Apache configuration file, restart .

## Lighttpd
Configuring Lighttpd, make sure  has been enabled.

Add the following alias for kiwiirc to the config:

 alias.url = ( "/kiwiirc" => "/usr/share/webapps/kiwiirc/")
