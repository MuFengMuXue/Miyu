# NZBGet

NZBGet is an Usenet-client written in C++ and designed with performance in mind to achieve maximum download speed by using very little system resources.

## Installation
Install the  package.

## Configuring NZBGet
Copy the template configuration file to a custom directory:
 # cp /usr/share/nzbget/nzbget.conf /var/lib/nzbget/.nzbget

Update the configuration before starting NZBGet:

Make sure the permissions are set correctly:
 # chown -R nzbget:nzbget /var/lib/nzbget
 # chmod -R 750 /var/lib/nzbget

## Starting NZBGet
You can start/enable the , or start it manually:

* Running as root in console-mode:
* Running as root in daemon-mode:

NZBGet should now be accessible on http://localhost:6789.

## Running NZBGet under a different user
See system user for an example and reasons why it may be useful.

After adding a system user, update the main configuration file using the webinterface or by manually editing :

Create and set permissions for the desired directories:
 # mkdir /home/myuser/Downloads/NZBGet
 # chown -R nzbget:nzbget /home/myuser/Downloads/NZBGet
 # chmod 775 /home/myuser/Downloads/NZBGet

The  will be accessible for the user  and for the  group. Making the target directory world read/writable is highly discouraged (i.e. do not chmod the directory to 777). Instead, give individual users/groups appropriate permissions to the appropriate directories (e.g. by adding 'yourself' to the  user group).

Starting NZBGet as user  in daemon-mode:

 /usr/bin/nzbget -c /var/lib/nzbget/.nzbget -D

Or start the  instead.

## Troubleshooting
## Default NZBGet credentials
The default credentials for NZBGet are  as user and  as password. For security reasons it is recommended to change the default credentials.

## NZBGet crashes on start
This may happen when the user edited the NZBGet configuration by the Web-interface (located at http://localhost:6789), corrupting the configuration-file. Clean-up the configuration-file and restart the server/daemon again.

## Alternative systemd service
The following  provides an alternative solution for (re)starting NZBGet when using systemd:

## Unable to extract archives
Verify if , ,  and  have been installed.
