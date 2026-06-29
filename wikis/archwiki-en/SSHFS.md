# SSHFS

SSHFS is a FUSE-based file system client for mounting remote directories over a Secure Shell connection.

## Installation
Install the  package.

## Usage
## Mounting
In order to be able to mount a directory the SSH user needs to be able to access it. Invoke sshfs to mount a remote directory:

 $ sshfs mountpoint [options

For example:

 $ sshfs myuser@mycomputer:/remote/path /local/path -C -p 9876

Here  specifies the port number and  enables compression. For more options see the #Options section.

When not specified, the remote path defaults to the remote user home directory. Default user names and options can be predefined on a host-by-host basis in  to simplify the sshfs usage. For more information see OpenSSH#Client usage.

SSH will ask for the password, if needed. If you do not want to type in the password multiple times a day, see SSH keys.

## Unmounting
To unmount the remote system:

 $ fusermount3 -u mountpoint

Example:

 $ fusermount3 -u /local/path

## Options
A complete list of options can be found in  and .

## User ID mapping
sshfs can automatically convert between local and remote user IDs. Use the  option to translate the UID of the connecting user to the remote user  (GID remains unchanged):

 $ sshfs myuser@mycomputer:/remote/path /local/path -o idmap=user

If you need more control over UID and GID translation, look at the options ,  and .

## allow_root or allow_other
 $ sshfs myuser@mycomputer:/remote/path /local/path -o allow_other,default_permissions,uid=1002,gid=1002

*  - Allow other users than the mounter (i.e. root) to access the share.
*  - Similar to allow_other but file access is limited to the user mounting the file system and root.
allow_root and allow_other are mutually exclusive. Additionally you want to edit  and uncomment the string  to enable all users to use these options.
*  - might be also used because fuse by default does not check file access permissions. i.e. use the actual permissions on the remote file system. This allows prohibiting access to everybody otherwise granted by allow_other.

## Change ownership of mountpoint
* ,  - set reported ownership of files to given values; uid is the numeric user ID of your user, gid is the numeric group ID of your user.

## Tips and tricks
## Chrooting
You may want to restrict a specific user to a specific directory on the remote system. This can be done by editing :

See also SFTP chroot. For more information check the  man page for ,  and .

## systemd
Similar to other file system mounts see  and possibly . Because of the FUSE system and its mechanics you should use user units. Setup SSH with public key authentication.

## As user unit
The example user unit mounts an sshfs filesystem in  with the following options:
*  is carried over from the system-wide config. May not be relevant when run as a regular user, but also doesn't harm anything.
*  causes sshfs to not attempt to connect to the server unless the directory is accessed (similar to a systemd automount unit).
*  makes sshfs attempt to re-establish a lost connection. This is useful when waking from sleep mode.
*  sends a TCP keep-alive packet to the server every 15 seconds. This helps with responsiveness.
*  enables sshfs directory caching. This also helps with responsiveness, particularly when used in a desktop environment.
*  maps the UID/GID of the remote user to UID/GID of the mounting user. See .
*  makes symlinks behave as expected (they can be followed, and absolute symlinks access files on the remote system).
*  enables SSH compression. Depending on the file types involved this can result in significant bandwidth savings.

{{hc|${XDG_CONFIG_HOME}/systemd/user/home-user-share-data.mount|Whatuser@remote:/mnt/data
Where%h/share/data
Typesshfs
Options_netdev,user,delay_connect,reconnect,ServerAliveInterval15,dir_cacheyes,idmapuser,follow_symlinks,transform_symlinks,compressionyes

[Install
WantedBydefault.target
}}

## Use ssh-key with passphrase
See SSH keys#Start ssh-agent with systemd user.

## Generate .mount and .automount files
Create an entry in /etc/fstab with at least _netdev, x-systemd.automount is only necessary if you need automount functionality.

All the generated files are after the daemon-reload command in /run/systemd/generator/. For user units you can copy the files you need and remove the fstab line and reload systemd

## Write .mount and .automount files
You will need to write two systemd units: a mount unit and an optional automount unit. Enabling the automount unit and keeping the mount unit itself disabled will not block startup and only mount once trying to access the file system. These files need to be named exactly like the mountpoint with "-" signs separating the folders within the path.

Mount unit, needs to be named exactly like the mountpoint (here,  becomes ):

The automount unit file also needs to be named exactly like the mountpoint:

## systemd root and multiple user
Automounting can happen on boot, or on demand (when accessing the directory). For both, the setup happens in the fstab.

## On demand
With systemd, on-demand mounting is possible using  entries.

Example:

 user@host:/remote/path /local/path  fuse.sshfs x-systemd.automount,_netdev,users,idmap=user,IdentityFile=/home/user/.ssh/id_rsa,allow_other,reconnect 0 0

The important mount options here are x-systemd.automount,_netdev.

* x-systemd.automount does the on-demand magic
* _netdev tells it that it is a network device, not a block device (without it, "No such device" errors might happen)

See also fstab#Automount with systemd.

## On boot
An example on how to use sshfs to mount a remote file system through

 user@host:/remote/path  /local/path  fuse.sshfs  _netdev  0  0

Take for example the fstab line

 llib@192.168.1.200:/home/llib/FAH  /media/FAH2  fuse.sshfs  _netdev  0  0

The above will work automatically if you are using an SSH key for the user that is not password-protected. See Using SSH Keys.

If you want to use sshfs with multiple users, add the following option:

 user@domain.org:/home/user  /media/user   fuse.sshfs    allow_other,_netdev    0  0

In order to ensure the network is available before trying to mount, it is not only important to set the  mount option, but also to add either  or a specific  to the appropriate wait-online service for your network manager.

## Secure user access
When automounting via fstab, the file system will generally be mounted by root. By default, this produces undesireable results if you wish access as an ordinary user and limit access to other users.

An example mountpoint configuration:

 user@host:/remote/path /local/path  fuse.sshfs noauto,x-systemd.automount,_netdev,user,idmap=user,follow_symlinks,identityfile=/home/user/.ssh/id_rsa,allow_other,default_permissions,uid=USER_ID_N,gid=USER_GID_N 0 0

See #allow_root or allow_other for the explanation of the options used.

## Troubleshooting
## Checklist
Read OpenSSH#Checklist first. Further issues to check are:

# Is your SSH login sending additional information from server's  file e.g.? This might confuse SSHFS. You should temporarily deactivate server's  file:
# Keep in mind that most SSH related troubleshooting articles you will find on the web are not systemd related. Often  definitions wrongly begin with  instead of using the syntax
# Check that the owner of server's source directory and content is owned by the server's user.
# The server's user ID can be different from the client's one. Obviously both user names have to be the same. You just have to care for the client's user IDs. SSHFS will translate the UID for you with the following mount options:
# Check that the client's target mount point (directory) is owned by the client user. This directory should have the same user ID as defined in SSHFS's mount options.
# Check that the client's mount point (directory) is empty. By default you cannot mount SSHFS directories to non-empty directories.

## Connection reset by peer
* If you are trying to access the remote system with a hostname, try using its IP address, as it can be a domain name resolving issue. Make sure you edit  with the server details.
* Make sure your user can log into the server (especially when using ).
* Make sure  is enabled in  on the remote system.
* If you are using a non-default key name and passing it as , this will not work. You have to use , with the full path to the key.
* If your  is a symlink, you will be getting this error as well. See this serverfault topic
* Adding the option  (as in ) can help in resolving the issue.
* If that does not reveal anything useful, you might also try adding the option .
* If you are trying to sshfs into a router running DD-WRT or the like, there is a solution here. (Note that the  option can be used to the sshfs command instead of patching dropbear).
* If you see this only on boot, it may be that systemd is attempting to mount prior to a network connection being available. Enabling the appropriate wait-online service for your network manager fixes this.
* Old Forum thread: sshfs: Connection reset by peer.

## Remote host has disconnected
If you receive this message directly after attempting to use sshfs:

* First make sure that the remote machine has sftp installed! It will not work, if not.
* Then, check that the path of the  in  on the remote machine is valid.

## fstab mounting issues
To get verbose debugging output, add the following to the mount options:

 ssh_command=ssh\040-vv,sshfs_debug,debug

To be able to run  and see the debug output, remove the following:
  noauto,x-systemd.automount

## Some directories are empty
sshfs by default does not support symlinks. If those directories happened to be symlinks, use:

 $ sshfs user@host:/remote/path /local/path -o follow_symlinks

## Files not refreshed
If you see old content on remote, consider using option :

 $ sshfs user@host:/remote/path /local/path -o dir_cache=no

## Limited transfer speed on fast network
If you observe transfer speed that is lower than your network capabilities and high CPU usage on the party where files are copied from, disable compression (remove  option or set ).
