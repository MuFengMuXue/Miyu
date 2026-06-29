# Sftpman

You can use sftpman (an SSHFS helper) to mount a remote system - accessible via SSH - to a local folder.

sftpman offers both a command-line tool (sftpman) and an iced-based frontend (sftpman-iced, see screenshot), each packaged separately.

With sftpman, you first setup (define) your remote filesystems and then you mount/unmount them easily (with one command or click).

## Installation
There are 2 packages you may wish to install.

*  - provides the command-line application sftpman and is also used internally (as a library) by the GUI frontend.

*  - provides the sftpman-iced application, an iced-based GUI frontend to sftpman.

## Defining filesystems
Each filesystem managed by sftpman needs to have a unique name/id which will be used when managing the system and also in its mount path.
A system with an id of my-machine will be mounted locally to /mnt/sshfs/my-machine.

Authentication with the remote filesystem during mounting can be performed using passwords, SSH keys or by delegating it to an authentication-agent.

To define a new remote filesystem with password-based authentication using the command-line tool, do:
 $ sftpman create \
 --id "my-machine" \
 --host "HOSTNAME_OR_IP" \
 --user "USERNAME" \
 --auth_type=password \
 --remote_path "/REMOTE_PATH"

Or the equivalent in case you want to authenticate with SSH Keys (recommended):
 $ sftpman create \
 --id "my-machine" \
 --host "HOSTNAME_OR_IP" \
 --user "USERNAME" \
 --auth_type=publickey \
 --ssh_key "/PATH/TO/PRIVATE_KEY" \
 --mount_point "/REMOTE_PATH"

The above setup is the minimum for defining a new filesystem that sftpman can mount.
Depending on your environment, you may need to configure additional options (like --port, which defaults to 22). To see a full list of available options do:
 $ sftpman create --help

You can also use the GUI application to define new filesystems more easily.

## Mounting/Unmounting
Once you have defined several filesystems, you can mount them by using their ids.

To mount:
 $ sftpman mount my-machine
which mounts the filesystem to /mnt/sshfs/my-machine

To unmount:
 $ sftpman umount my-machine

## Removing defined filesystems
To remove a defined filesystem from sftpman's list do:
 $ sftpman rm machine-id

## Learning more
To see a list of more commands and options that sftpman supports, consult the help:
 $ sftpman help

## Troubleshooting
sftpman can perform some basic checks on the environment, which may catch some potential problems:
 $ sftpman preflight_check

If the GUI application does not ask you for a password while mounting (when using password-based authentication or for password-protected ssh keys), you will need to install an ssh askpass tool, see #Mounting/Unmounting.

When doing authentication using keys, start small and make sure SSH-ing actually works by trying it manually, before trying to use sshfs and a helper around sshfs (like sftpman). Some common problems can be solved by consulting Using SSH Keys#Troubleshooting.

Also see SSHFS#Troubleshooting.
