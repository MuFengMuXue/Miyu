# SCP and SFTP

The SSH file transfer protocol (SFTP) is a protocol to transfer files, relying on a secure shell back-end. The Secure copy (SCP) is an outdated protocol via a Secure Shell connection. Both protocols allow secure file transfers, encrypting passwords and transferred data. The modern SFTP protocol, however, features additional capabilities like, for example, resuming broken transfers or remote file manipulation like deletion.

## Secure file transfer protocol (SFTP)
Install and configure OpenSSH. Once running, SFTP is available by default.

Access files with the sftp program or SSHFS. Many standard FTP programs should work as well.

## Secure file transfer protocol (SFTP) with a chroot jail
Sysadmins can jail a subset of users to a chroot jail using  thus restricting their access to a particular directory tree.  This can be useful to simply share some files without granting full system access or shell access.  Users with this type of setup may use SFTP clients such as  to put/get files in the chroot jail.

## Setup the filesystem
Create a jail directory:

 # mkdir -p /var/lib/jail

Optionally, bind mount the filesystem to be shared to this directory. In this example,  is to be used.  It is owned by root and has octal permissions of 755.

 # mount -o bind /mnt/data/share /var/lib/jail

## Create an unprivileged user
Create the share user and setup a good password:

 # useradd -g sshusers -d /var/lib/jail foo
 # passwd foo

## Setup OpenSSH
Add the following to the end of  to enable the share and to enforce the restrictions:

Restart  to re-read the configuration file. See SFTP chroot to configure the keys correctly when using chroot or it will get permission denied.

Test that in fact, the restrictions are enforced by attempting an ssh connection via the shell. The ssh server should return a polite notice of the setup:

## Secure copy protocol (SCP)
Install, configure and start OpenSSH. It contains the scp utility to transfer files.

More features are available by installing additional packages, for example  or  described below.

## General Usage
## Linux to Linux
Copy file from a remote host to local host SCP example:

 $ scp username@from_host:file.txt /local/directory/

Copy file from local host to a remote host SCP example:

 $ scp file.txt username@to_host:/remote/directory/

Copy directory from a remote host to local host SCP example:

 $ scp -r username@from_host:/remote/directory/  /local/directory/

Copy directory from local host to a remote host SCP example:

 $ scp -r /local/directory/ username@to_host:/remote/directory/

Copy file from remote host to remote host SCP example:

 $ scp username@from_host:/remote/directory/file.txt username@to_host:/remote/directory/

## Linux to Windows
Use a Windows program such as WinSCP

## Scponly
Scponly is a limited shell for allowing users scp/sftp access and only scp/sftp access. Additionally, one can setup scponly to chroot the user into a particular directory increasing the level of security.

install .

For existing users, simply set the user's shell to scponly:

 # usermod -s /usr/bin/scponly username

## Adding a chroot jail
The package comes with a script to create a chroot. To use it, run:

 # /usr/share/doc/scponly/setup_chroot.sh

* Provide answers
* Check that  has  owner and  for others
* Change the shell for selected user to
* sftp-server may require some libnss modules such as libnss_files. Copy them to chroot's  path.

## Uploads to Chroot jail root dir
For security reasons the directory set as the chroot directory must be owned by root with only root having write access to it otherwise sftp/ssh connections will be denied. This of course means regular users cannot upload files to the root directory. In order to get around this while not compromising security you can create a folder inside the chroot directory which the regular user or group has write access to, e.g:

 # cd /var/lib/jail
 # mkdir uploads
 # chown :sshusers uploads
 # chmod 730 uploads

Some applications utilizing SFTP do not allow input of sub-directories when performing operations (e.g. uploading files), and will attempt to upload files to the chroot base directory (which will be denied). In order to force these applications to use a specific sub-directory you can append the following to the "ForceCommand" option:

Users on connect will then have their start directory change to the specified sub-directory (remember to restart the sshd server).
