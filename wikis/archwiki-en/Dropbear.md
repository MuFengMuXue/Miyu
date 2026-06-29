# Dropbear

Dropbear is lightweight SSH server that is commonly run on routers and other low memory devices. It is also often configured to run during the boot process.

## Installation
Install the  package.

## Configuration
Dropbear server does not have any configuration file. It is configured with command line options.

Enable/start .

## Disable password and root logins
Edit the . This creates a new drop-in file. Adding content to it will override corresponding sections in main configuration.

Override the command to start Dropbear:

 Service
 ExecStart=
 ExecStart=/usr/bin/dropbear -F -P /run/dropbear.pid -R -w -s

: Is used to generate hostkeys automatically.

: Is used to forbid forking into background.

: Is used to disallow root logins.

: Is used to disable password logins.

## Set SSH key from GitLab
Change GitLab URL to your own.

 $ mkdir -p ~/.ssh -m 0700
 $ curl -sSLf https://gitlab.com/example.keys >> ~/.ssh/authorized_keys
