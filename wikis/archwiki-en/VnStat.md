# VnStat

vnStat is a lightweight (command line) network traffic monitor. It monitors selectable interfaces and stores network traffic logs in a database for later analysis.

## Installation
Install the  package.

## Configuration
Start/enable the  daemon.

Pick a preferred network interface and edit the  variable in the  accordingly. To list all interfaces available to vnstat, use .

To start monitoring a particular interface that was not referred to in the configuration file when the daemon was started, you must initialize a database first. Each interface needs its own database. The command to initialize one for the  interface is:
 # vnstat --add -i eth0

Remember to restart the  daemon after you have added a new interface.

## Usage
Query the network traffic:
 # vnstat --query

Viewing live network traffic usage:
 # vnstat --live

To find more options, use:
 # vnstat --help
or to see all options use:
 # vnstat --longhelp

Eye candy presentation of the data can also be achieved by , which is part of the  package.
