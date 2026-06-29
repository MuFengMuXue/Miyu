# Logwatch

Logwatch is a powerful and versatile log parser and analyzer. Logwatch is designed to give a unified report of all activity on a server, which can be delivered through the command line or email.

## Installation
Install .

In addition to the logwatch binaries, scripts and configuration files, the package used to include a cron job that was installed as . You need to start/enable  to generate regular logwatch reports.

## Configuration
Logwatch has a tiered configuration approach. There are several locations where configuration details can be specified, with each one superseding the previous one:

*
*
*
* The script / command line arguments

Logwatch will parse all these location when called.

Within these directories, there are several areas of configuration. The  files are where most of the high-level settings are, which allow you to set where your reports are sent, how they are formatted, etc. The configuration file at  contains all the default settings and comments on what they do. It is recommended to leave the default configuration alone and instead re-define a setting variable you want to change in .

Within the  directory of any locations are configuration files detailing specific log files. By default, most of the common log files found in a Linux system are already accounted for. If you have some esoteric application that does not have a log file configuration already, copy an existing one from the  directory and customize it for your application.

The  folder contains similar definitions, but these one define the various services reported by logwatch. This is necessary because often multiple services will report to the same log (e.g. messages, dmesg, boot, etc.). For more information, examine some of the default  files.

Note that if you want logwatch messages delivered by email, you need to install a package that provides a sendmail frontend. Postfix is a good choice.

There is a helpful document supplied with the package to give further information on configuration. It is located at .
