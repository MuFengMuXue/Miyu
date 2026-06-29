# UW IMAP

From Wikipedia:
:UW IMAP is the reference server implementation of the IMAP protocol, developed at the University of Washington.
Although it has not been actively developed in many years, it still works well as a basic IMAPS server. (For other IMAP servers, see Mail server#Software.)

## Installation
Install . It does not use a configuration file.

## Configuration
Although it was originally designed to be used with inetd, on modern Arch systems a better solution is to use a systemd socket file:

Also, a corresponding .service file needs to be created:

UW-IMAPD uses PAM, so a PAM authorization file will also need to be created. This example will provide authentication using standard system passwords:

Enable and start  and test.

## SSL
A generic SSL certificate and key will be created at  if it does not yet exist. This can be replaced with a signed certificate for the specific server.
