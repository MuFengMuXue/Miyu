# Autofs

AutoFS provides automounting of removable media or network shares when they are inserted or accessed.

## Installation
Install the  package.

## Configuration
AutoFS uses template files for configuration which are located in  The main template is called , which can point to one or more other templates for specific media types.

Open the file  with your favorite editor, you will see something similar to this:

The first value on each line determines the base directory under which all the media in a template are mounted, the second value is which template to use. The default base path is , but you can change this to any other location you prefer. For instance:

The base directory will be created if it does not exist on your system. The base directory will be mounted on to load the dynamically loaded media, which means any content in the base directory will not be accessible while autofs is on. This procedure is however non-destructive, so if you accidentally automount into a live directory you can just change the location in  and restart AutoFS to regain the original contents.

If you still want to automount to a target non-empty directory and want to have the original files available even after the dynamically loaded directories are mounted, you can use autofs to mount them to another directory (e.g. ) and create soft links.

 # ln -s /var/autofs/net/share_name /media/share_name

Alternatively, you can have autofs mount your media to a specific folder, rather than inside a common folder.

Open the file  and add an entry for automount:

 automount: files

When you are done configuring your templates (see below), launch the AutoFS daemon as root by enabling and starting the .

Devices are now automatically mounted when they are accessed, they will remain mounted as long as you access them.

## Removable media
Removable devices are assigned block device locations according to the next available spot, e.g. if {{ic|/dev/sd{a,b,c} }} are already occupied, the next removable media will be given block .  Instead of assigning a mount point based on an unreliable block device path, a more robust approach is to use the UUID or PARTUUID of the removable media as the location in the map file.

For example, to mount a specific USB drive to the path , configure the template file and map file:

Use  to find the UUID of the partition to mount, then generate the map file:

 # _ID=$( blkid --output value --match-tag PARTUUID /dev/sdXY )
 # printf "%s %s\n" "black -fstype=auto :PARTUUID=" "${_ID}" >/etc/autofs/auto.mnt

## NFS network mounts
AutoFS provides automatically discovering and mounting NFS-shares on remote servers (the AutoFS network template in  has been removed in autofs5). To enable automatic discovery and mounting of network shares from all accessible servers without any further configuration, you will need to add the following to the  file:

 /net -hosts --timeout=60

For instance, if you have a remote server fileserver (the name of the directory is the hostname of the server) with an NFS share named , you can just access the share by typing:

 # cd /net/fileserver/home/share

The  option uses a similar mechanism as the  command to detect remote shares. You can see the exported shares by typing:

 # showmount servername -e

## Manual NFS configuration
To mount a NFS share for file_server on  at location , add a new configuration, e.g. :

## Samba
## Single shares
Add the following to :

 /media//etc/autofs/auto.[my_server --timeout 60 --browse

where  defines how many seconds to wait before the file system is unmounted. The  option creates empty folders for each mount-point in the file in order to prevent timeouts, if a network share cannot be contacted.

Next create a file

 -fstype=cifs,[other_options ://You can specify a user name and password to use with the share in the  section:

 [any_name -fstype=cifs,username=://[remote_server/==== Multiple shares ====

You may be specify multiple shares in the , for instance:

 [any_name -fstype=cifs,/photos ://[remote_server/photos /music :///video ://[remote_server/video

## Auto discovery
See the comments in .

## FTP and SSH (with FUSE)
Remote FTP and SSH servers can be accessed seamlessly with AutoFS using FUSE, a virtual file system layer.

## Remote FTP
First, install the  package.

Load the fuse module:

 # modprobe fuse

Create a  file containg  to load it on each system boot.

Next, add a new entry for FTP servers in :

 /media/ftp        /etc/autofs/auto.ftp    --timeout=60

Create the file  and add a server using the  format:

 servername -fstype=curl,rw,allow_other,nodev,nonempty,noatime    :ftp\://myuser\:mypassword\@remoteserver

If you want slightly more security you can create the file  and add the passwords there.
Passwords are still plain text, but you can have mode 600, and  command will not show them (mounted or not).
This method is also less sensitive to special characters (that else must be escaped) in the passwords. The format is:

 machine remoteserver
 login myuser
 password mypassword

The line in  looks like this without user and password:

 servername -fstype=curl,allow_other    :ftp\://remoteserver

Create the file  with this code:

Create the file  with this code:

Set the permissions for both files:

 # chmod 755 /sbin/mount.curl
 # chmod 755 /sbin/umount.curl

After a restart your new FTP server should be accessible through .

## MTP
Media Transfer Protocol (MTP) is used in some Android devices.

Install the  package.

Create a new entry for MTP Device in :

 android -fstype=fuse,allow_other,umask=000     :mtpfs

## Troubleshooting and tweaks
This section contains a few solutions for common issues with AutoFS.

## Using NIS
Version 5.0.5 of AutoFS has more advanced support for NIS. To use AutoFS together with NIS, add  in front of the template names in :

 /home   yp:auto_home    --timeout=60
 /sbtn   yp:auto_sbtn    --timeout=60
 +auto.master

On earlier versions of NIS (before 5.0.4), you should add  to :

 automount: files nis

## Optional parameters
You can set parameters like  systemwide for all AutoFS media in :

* Open the  file and edit the  line:
* To enable logging (default is no logging at all), uncomment and add  to the  line in  e.g.:

After restarting the  daemon, verbose output is visible in the unit status or in the journal.

## Identify multiple devices
If you use multiple USB drives/sticks and want to easily tell them apart, you can use AutoFS to set up the mount points and Udev to create distinct names for your USB drives. See udev#Setting static device names for instructions on setting up Udev rules.

## AutoFS permissions
If AutoFS is not working for you, make sure that the permissions of the templates files are correct, otherwise AutoFS will not start. This may happen if you backed up your configuration files in a manner which did not preserve file modes. Here are what the modes should be on the configuration files:

* —
* —
* —
* —

In general, scripts (like previous ) should have executable bits set and lists of mounts should not.

If you are getting errors in  similar to this, you have a permissions problem:

 May  7 19:44:16 peterix automountlookup(program): lookup for petr failed
 May  7 19:44:16 peterix automount[15218: failed to mount /media/cifs/petr

## fusermount problems
With certain versions of , you may not be able to unmount a fuse file system drive mounted by autofs, even if you use the  option. See the discussion on the mailing list.

## Debugging auto mount issues
For better debugging, try running automount in the foreground.

Stop , then run:

 # automount -f -v

Or if you want more debug info then try:

 # automount -f --debug

## Alternatives to AutoFS
* systemd can automount filesystems upon demand; see fstab#Automount with systemd for the description and the article on sshfs for an example.
* Thunar Volume Manager is an automount system for users of the Thunar file manager.
* PCManFM is a lightweight file manager with built-in support for accessing remote shares
* Udisks is a minimalistic automatic disk mounting service
