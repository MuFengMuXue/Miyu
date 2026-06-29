# FreeRADIUS

The FreeRADIUS server is a daemon for Unix and Unix-like operating systems which allows one to set up a RADIUS protocol server.

## Installation
Install .

Create your keys using:

 # /etc/raddb/certs/bootstrap

You may want to investigate the , , and  files to customize properties of
the generated certs, or simply create your own certs and keys if you want to sign them with a different CA - by default the bootstrap script generates a new CA to sign the keys.

## Basic usage
Start .

## Configuration
The configuration files can be found under .
