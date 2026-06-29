# FHEM

FHEM (TM) is a GPL'd perl server for house automation. It is used to automate some common tasks in the household like switching lamps / shutters / heating / etc. and to log events like temperature / humidity / power consumption.

## Installation
Install the  package.

## Configuration
Since version 5.7, the FHEM package uses a different directory layout for its files:

*  Perl modules and static content
*  logs and state files, changing content
*  main configuration file

If you have a legacy configuration, please adjust your paths by putting these lines into

If you like to edit the configuration from the web frontend, make sure the user  has write access to .

Please visit the FHEM reference documentation for further information.

## Startup
Just start/enable .
