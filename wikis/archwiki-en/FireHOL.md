# FireHOL

FireHOL is a language (and a program to run it) to build secure, stateful firewalls from easy to understand, human-readable configuration files. The configuration stays readable even for very complex setups. In the background it interfaces with iptables (IPv4/IPv6).

## Installation
Install the  package.

## Configuration
## Initial Auto Configuration
Firehol comes with its own firewall wizard. All traffic is allowed by default. Using the wizard is the first step to get a basic firewall configuration which automatically detects all open port and interfaces running on the system.

 # firehol wizard > /tmp/firehol.conf

The configuration is well documented. After finishing editing move it to . Then test run it with the command

 # firehol try

You have 30 seconds before those changes are undone and if everything works as expected, you can make it permanent by starting and enabling

A good way to start learning its scripting declarations is by copying an Firehol example configuration.

The configuration file is bash file and has 3 parts:

* helper
* interface
* router

## Usage
You can test the configuration file's correctness by issuing:

 # firehol try

or

 # firehol nofast try

If the configuration is working, start/enable the .
