# NIS

Network Information Service (NIS) is a protocol developed by Sun to allow one to defer user authentication to a server. The server software is in the  package, and the client software is in the  package.  is also available, which is a multi threaded version of the client daemon.

## NIS Server
## Install Packages
Install the , , and  packages.

## Configuration
## /etc/hosts
Add your server's external (not 127.0.0.1) IP address to the hosts file. Make sure it is the first non-commented line in the file, yes, even above the localhost line, like so:

This is due to a peculiarity in ypinit (maybe it is a bug, maybe it is a feature), which will always add the first line in  to the list of ypservers.

## /etc/nisdomainname
Add the domain name:

## /etc/ypserv.conf
Add rules to  for your your nis clients of this form:

For example:

For more information see .

## /var/yp/Makefile
Add or remove files you would like NIS to use to  under the "all" rule.

Default:

 # all:  passwd group hosts rpc services netid protocols netgrp \
 #         shadow # publickey networks ethers bootparams printcap mail \
 #         # amd.home auto.master auto.home auto.local passwd.adjunct \
 #         # timezone locale netmasks

After that you have to build your NIS database:

 # cd /var/yp
 # make

Or you can do it in a more automated fashion:

 # /usr/lib/yp/ypinit -m

If you use this way you may skip manually adding lines to .

## /var/yp/securenets
Add rules to  to restrict access:

Be sure to comment out this line, as it gives access to anyone.

## /var/yp/ypservers
Add your server to :

## Set your domain name
 # ypdomainname EXAMPLE.COM

Now edit the  file and add your ypserver or nis server.

## Start NIS Daemons
Start/enable the following systemd units:
*
*
*
*  (to allow clients to change their password with )

## NIS Client
## Install Packages
The first step is to install the tools that you need. This provides the configuration files and general tools needed to use NIS. Install  .

## Configuration
## Set your domain name
 # ypdomainname EXAMPLE.COM

You can apply this permanently by editing  and adding:
 # NISDOMAINNAME="EXAMPLE.COM"

Now edit the  file and add your ypserver or nis server.
 ypserver nis_server

## /etc/hosts
It may be a good idea to add your NIS server to
 192.168.1.10   nis_server.domain.com   nis_server

## Start NIS Daemons
Start/enable the  and  systemd units.

## Early testing
To test the setup so far you can run the command yptest:
 # yptest

If it works you will, among other things, see the contents of the NIS user database (which is printed in the same format as ).

## /etc/nsswitch.conf
To actually use NIS to log in you have to edit .  Modify the lines for passwd, group and shadow to read:
 passwd: files nis
 group: files nis
 shadow: files nis

And then do not forget to restart .

## /etc/pam.d/passwd
To allow a user on a client machine to change their password on the server, be sure that  is started/enabled on the server.

Edit  on the client to add the  parameter to :
 password     required     pam_unix.so sha512 shadow nullok nis

See section 7 of The Linux NIS HOWTO for further information on configuring NIS clients.

## Connections after Systemd V235
Due to sandboxing on , any IP connections from and to the  service are now denied. This will cause failures to log in, even though  works as expected, and can also cause  to crash outright. The basic problem is that the default  file that ships with  specifies , and this prevents it from communicating with the NIS server at login. Moreover, since V239, that file also specifies , dropping  from the list.

The solution is to whitelist the address or address range of your NIS server.

Another systemd sandboxing element related to namespace management ("ProtectHostname") may prevent proper operation.  The following snippet turns that off too.

Use a drop-in unit file for , with these lines (the following allows connections , edit as appropriate):

## systemd-userdbd.service
After updating nis clients to systemd 245-1, the  can be affected by a similar issue as the  which can cause 25 second login delays.

Use a drop-in unit file for  containing your NIS server IP address to correct the issue.

(Alternately, the same drop-in file used for systemd-logind.service could be used.)

## More resources
*The Linux NIS HOWTO,very helpful and generally applicable to Arch Linux.
*YoLinux NIS tutorial
*Quick HOWTO, Configuring NIS
