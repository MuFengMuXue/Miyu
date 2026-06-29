# SFTP chroot

OpenSSH 4.9+ includes a built-in chroot for SFTP, but requires a few tweaks to the normal install.

## Installation
Install and configure OpenSSH. Once running, make sure  has been set correctly:

Access files with sftp or SSHFS. Many standard FTP clients should work as well.

## Configuration
## Setup the filesystem
Bind mount the live filesystem to be shared to this directory. In this example,  is to be used, owned by user  and has octal permissions of :

 # chown root:root /mnt/data/share
 # chmod 755 /mnt/data/share
 # mkdir -p /srv/ssh/jail
 # mount -o bind /mnt/data/share /srv/ssh/jail

Add entries to fstab to make the bind mount survive on a reboot:

## Create an unprivileged user
Create the  user group:

 # groupadd sftponly

Create a user who is a member of the sftponly group and has shell login access denied:

 # useradd -G sftponly -s /usr/bin/nologin -d /srv/ssh/jail username

Set a (complex) password to prevent  error (may appear even with key authentication):

 # passwd username

## Configure OpenSSH
Restart  to confirm the changes.

## Fixing path for authorized_keys
With the standard path of AuthorizedKeysFile, the SSH keys authentication will fail for chrooted-users. To fix this, append a root-owned directory on AuthorizedKeysFile to  e.g. , as example:

Create authorized_keys folder, generate a SSH-key on the client, copy the contents of the key to  (or any other preferred method) of the server and set correct permissions:

 # mkdir /etc/ssh/authorized_keys
 # chown root:root /etc/ssh/authorized_keys
 # chmod 755 /etc/ssh/authorized_keys
 # echo 'ssh-rsa  ' >> /etc/ssh/authorized_keys/username
 # chmod 644 /etc/ssh/authorized_keys/username

Restart .

## Tips and tricks
## Write permissions
The bind path needs to be fully owned by , however files and/or subdirectories do not have to be.
In the following example the user www-demo uses  as the jail-directory:
 # mkdir /srv/ssh/www/demo/public_html
 # chown www-demo:sftponly /srv/ssh/www/demo/public_html
 # chmod 755 /srv/ssh/www/demo/public_html

The user should now be able to create files/subdirectories inside this directory. See File permissions and attributes for more information.

## Allow upload only
To allow only uploading files via sftp and deny downloading files, change the  line:

## Logging
The user will not be able to access . This can be seen by running  on the process once the user connects and attempts to download a file.

## Create sub directory
Create the sub-directory  in the , for example:
 # mkdir /usr/local/chroot/user/dev
 # chmod 755 /usr/local/chroot/user/dev

Now you should create socket at  which will be used by openssh. You may directly bind this socket to  (or  in case you are using journald) or create using /.

## Bind to journald
 # touch /usr/local/chroot/user/dev/log
 # mount --bind /run/systemd/journal/dev-log /usr/local/chroot/user/dev/log

To make it permanent, add an entry to fstab:

## Syslog-ng configuration
Add to  a new source for the log and add the configuration, for example change the section:
{{bc|source src {
  unix-dgram("/dev/log");
  internal();
  file("/proc/kmsg");
};
}}

to:
{{bc|source src {
  unix-dgram("/dev/log");
  internal();
  file("/proc/kmsg");
  unix-dgram("/usr/local/chroot/theuser/dev/log");
};
}}

and append:
{{bc|#sftp configuration
destination sftp { file("/var/log/sftp.log"); };
filter f_sftp { program("internal-sftp"); };
log { source(src); filter(f_sftp); destination(sftp); };
}}

(Optional) If you would like to similarly log SSH messages to its own file:

{{bc|#sshd configuration
destination ssh { file("/var/log/ssh.log"); };
filter f_ssh { program("sshd"); };
log { source(src); filter(f_ssh); destination(ssh); };
}}
(From Syslog-ng#Move log to another file)

## OpenSSH configuration
Edit  to replace all instances of  with .

## Restart service
Restart service  and .

 should now exist.

## Alternatives to SFTP
## Secure copy protocol (SCP)
Installing  provides the scp command to transfer files. SCP may be faster than using SFTP Install  or  as alternative shell solutions.

## Scponly
install .

For existing users, simply set the user's shell to scponly:

 # usermod -s /usr/bin/scponly username

See [https://github.com/scponly/scponly/wiki the Scponly Wiki for more details.

## Adding a chroot jail
The package comes with a script to create a chroot. To use it, run:

 # /usr/share/doc/scponly/setup_chroot.sh
* Provide answers.
* Check that  has  owner and  for others.
* Change the shell for selected user to .
* sftp-server may require some libnss modules such as libnss_files. Copy them to chroot's  path.
