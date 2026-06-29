# PhpVirtualBox

phpVirtualBox is an open source, AJAX implementation of the VirtualBox user interface written in PHP. As a modern web interface, it allows you to access and control remote VirtualBox instances. Much of its verbage and some of its code is based on the (inactive) vboxweb project. phpVirtualBox was designed to allow users to administer VirtualBox in a headless environment - mirroring the VirtualBox GUI through its web interface.

## Installation
To remotely control virtual machine you need two components: VirtualBox web service, running in the same OS with virtual machine, and web interface, written in PHP and therefore dependent on PHP-capable web server. Communication between them, based on SOAP protocol is currently unencrypted, so it is recommended to install both on the same machine if you do not want your username and password to be send via network as clear text.

## VirtualBox web service
To use the web console, you must install the  package.

## VirtualBox web interface (phpvirtualbox)
Install the  package. You will also need a PHP-capable web server of your choice (Apache HTTP Server is suitable choice).

## Configuration
From here on out, it is assumed that you have a web server (with root at ) and php functioning properly.

## Web service
In the virtual machine settings, enable the remote desktop access and specify a port different with other virtual machines.

Every time you need to make machine remotely available execute something like this:

 vboxwebsrv -b --logfile path/to/log/file --pidfile /run/vbox/vboxwebsrv.pid --host 127.0.0.1

As user whose account you want the service to be running from ( option is not necessary if you enabled association with localhost in the ).

 provides the  for systemd.

To start  from non-root user you must:

#Create or add a user in the group  (for example, )
#Edit  like this:
#Create tmpfile rule for your
#Create manually  directory for first start  or just reboot your system for automatically create.
#Start/enable

## Web interface
Edit , uncomment the following line:
 extension=soap

Edit the example configuration file  appropriately (it is well-commented and does not need explanations). Copy that file into  and symlink to .

Then, edit , find  and append the configuration path  at the end. It will look like the follows:

 open_basedir = /srv/http/:/home/:/tmp/:/usr/share/pear/:/usr/share/webapps/:/etc/webapps/

If you are running Apache as webserver, you can copy  into . If you are running Apache 2.4, due to the syntax of ACL changes, edit that file to replace the follows

 Order allow,deny
 Allow from all

to:

 Require all granted

Next, add following line into :

 Include conf/extra/phpvirtualbox.conf

Edit  and remove the following line.

 deny from all

Do not forget to restart the webserver (e.g. for Apache, restart ).

## Running
If everything works fine, visit http://YourVboxWebInterfaceHost/phpvirtualbox and it should show a login box. The initial username and password are both "admin", after login change them from the web interface (File -> change password). If you set  in the web interface , you should immediately see the phpvirtualbox web interface.

## Debugging
If you encounter a login problem, and you have upgraded virtualbox from 3.2.x to 4.0.x, you should run the following command to update you websrvauthlibrary in you virtualbox configuration file which has been changed from  to .

 VBoxManage setproperty vrdeauthlibrary default
 VBoxManage setproperty websrvauthlibrary default

If you encounter a login problem with an error message that contains

 => Could not connect to host (http://127.0.0.1:18083/)

Then you may want to edit  variable location to use  rather than . See [https://sourceforge.net/p/phpvirtualbox/discussion/help/thread/cbc7fa4b/ this forum post for further information.

If you are still unable to login into the interface, you can try to disable webauth by

 VBoxManage setproperty websrvauthlibrary null

on virtualization server and set username and password to empty strings and set $noAuth=true in  on web server. By doing this, you should immediatelly access the web interface without login process. And then, maybe you can try some apache access control.
