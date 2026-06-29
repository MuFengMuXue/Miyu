# Davfs2

davfs2 is a Linux file system driver that allows to mount a WebDAV resource. WebDAV is an extension to HTTP/1.1 that allows remote collaborative authoring of Web resources.

## Installing davfs2
Install the  package.

## Mount WebDAV-resource
## Configuration and mount options
There is a system wide configuration file  and a user configuration file . The latter is read in addition to the system configuration when invoked by an ordinary user and takes precedence. There are general, WebDAV related, cache related and debugging options. All the available options and their syntax can be found in .

There are also mount options used to define if needed the path of the configuration file, the owner and group of the filesystem and some other options related to file access. The list of recognised options can be obtained with the following command:

 $ mount.davfs -h

Also see  for description and options.

## Using command-line
To mount a WebDAV-resource use , not  directly.

 # mount -t davfs http(s)://address:/path /mount/point

## Using systemd
To use systemd mounting:

You can create a systemd automount unit to set a timeout

See Fstab#Automount with systemd for more tips and tricks when using systemd mount units.

## Using fstab
To define how the webdav resource should be mounted into the filesystem, append an fstab entry under the following format:

where username is the owner of the mounted file system. It may be a numeric ID or a user name and only root can mount a uid different from the mounting user.  mount option could be used to automount network drives.

## Tips and tricks
## Storing credentials
Create a secrets file to store credentials for a WebDAV-service using  for user, and  for root:

Make sure the secrets file contains the correct permissions, for root mounting:

 # chmod 600 /etc/davfs2/secrets
 # chown root:root /etc/davfs2/secrets

And for user mounting:

 $ chmod 600 ~/.davfs2/secrets

## Troubleshooting
## Creating/copying files not possible and/or freezes
If creating/copying files is not possible and/or freezes occur, edit the configuration and mount options to use  as option.
Default for this parameter is  which locks files on the server when they are opened for writing.

## Password in secrets file
Be careful for special characters in passwords such as  and . Escape them with .

## Network is online but domain lookup fails
Sometimes  is reached but the domain of your WebDAV server still cannot be found: you can wait until the name lookup succeeds manually.

First, you need to set up using fstab. Then, for 15 seconds we test if we can reach the server with ping and only try to mount once successful:

{{hc|/etc/systemd/system/mnt-webdav-service.service|2=
Description=Mount WebDAV Service
After=network-online.target
Wants=network-online.target

[Service
Type=oneshot
ExecStart=bash -c 'for i in {1..15}; do if ping -c 1 mywebdav.server.url; then mount /path/to/mountpoint; break; else sleep 1; fi; done'
ExecStop=umount /path/to/mountpoint
RemainAfterExit=true

Install
WantedBy=default.target
}}

This is better used as user unit.

## Error 'different mount options in /etc/fstab' when mounting a webdav resource
This happens when:

# the webdav resource and a mountpoint for it has been set in /etc/fstab
# the mountpoint has been passed as an argument to 'mount' command (even if the mountpoint is the same as in /etc/fstab)

Fix: do not pass a mountpoint when mounting, so that the value specified in /etc/fstab is used. For example:

 $ mount -t davfs https://mywebdav mymountpoint # incorrect
 different mount options in /etc/fstab
 $ mount -t davfs https://mywebdav # correct
