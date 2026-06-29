# TeamSpeak

From Wikipedia:TeamSpeak:

:TeamSpeak is proprietary Voice over IP software that allows computer users to speak on a chat channel with fellow computer users, much like a telephone conference call.

## Installation
## Client
Install the  package.

## Server
Install the  package.

## Server configuration and startup
## Configuration
* You can configure the TeamSpeak server. If you are using systemd, please check  for all available command line parameters.

* If you possess a license file please copy it to .

## First startup
With the first startup TeamSpeak creates the SQLite database at  and starts logging its standard output in files in: . Teamspeak also creates the first ServerQuery administration account (the superuser) and the first virtual server including a privilege key for the server administrator of this virtual server. The privilege key is only displayed once on standard output.

* Start and enable .

* To find the privilege key check the unit status.

* Scan the output for the privilege key:

* The privilege key is what token is equal to.

* Alternatively, you can navigate to the logs directory for teamspeak3-server and read the output log directly. (This is a persistent file and will still have the first startup output here even if you have restarted the server):

 # cd /var/log/teamspeak3-server
 # cat ts3server_*.log

Open up a Teamspeak 3 client, connect to the server and copy and paste the privilege key into the client popup.

## Re-Initialising Teamspeak
If you have used the initial privilege key and have lost server permissions (e.g. your teamspeak 3 client with superadmin rights was uninstalled) you will have to start from scratch.

* Stop .

* Remove :

* Clear :

* Now follow the same instructions for a first time setup.

## Starting Teamspeak with disabled IPv6 stack
When booting your system with the  kernel parameter to disable the IPv6 stack, Teamspeak will not be able to start with the default configuration. Edit  to change the listening IPs.
