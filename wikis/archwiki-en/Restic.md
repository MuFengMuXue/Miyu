# Restic

This page discusses the restic backup tool, provides a 'quick start' guide, and suggests best practices in the context of Arch Linux.

Restic's main features and benefits are:

* encrypted backups
* remote backups
* built-in support for compression
* efficient storage (chunk-based increments, data is not duplicated)
* gives flexibility to use a custom scheduler like cron or systemd
* written in Go, providing stand-alone binaries

## Installation
Install , then initialise a repository in an empty directory (for local backups) with:

 $ restic init --repo /path/to/backup/directory/

See the official tutorial.

## Security
Restic stipulates threat-model assumptions for usage.

It uses symmetric encryption for repositories. This introduces some issues with scheduled backupsas the key would generally have to be stored in plain text for an automated process to be able to create the backup. Ideally there would be asymmetric encryption that allows to create snapshots with a public key (used in an automated script by restic) yet only decrypt the snapshot with a private key, but this is not supported.

As an advantage of restic's symmetric encryption, it features  commands to manage multiple keys for a repository. Hence, it is possible to add a primary key and secondary keys. Further, the  option can be used to fetch a key from a vault. In combination it is possible to safeguard a primary key and use a secondary key:
* for an append-only backup repository,
* securing it via a vault like systemd-creds, or with a second-factor token.

The above methods can be configured both for a system (root) and a regular user, limiting the risk associated with plaintext password credentials for the backup repository.

## Scheduling
## systemd timers
Unlike other tools like timeshift[https://github.com/teejee2008/timeshift, restic does not include a scheduling capability. You are expected to either use cron or systemd timers.

You can use a ready project like restic-automatic-backup-scheduler or follow this example that creates local (full) system backups and should be run as the root user.

The example assumes there is an existing directory where an existing restic repository has been initialised (see #Installation).

## Create separate volume
This step is optional, but it is a good idea to mount a separate volume there to prevent the automated backup process from potentially consuming all space available to the OS.

The first restic backup will have to clone the entire OS, so the minimum amount of space required is equal to the space taken up by the OS (subject to path exclusions described below) or any other directory that you decide to backup.

Of course, you need space for any additional incremental changes in the future so it is a good idea to create a volume with 2 or even 3 times the size of the data being backed up. E.g. if  takes up  then you can create  with .

## systemd service
You will need a service unit. Create one:

To run the service with minimal required privileges while still allowing read access to all user files, run the service as a restricted user with AmbientCapabilities=CAP_DAC_READ_SEARCH

## Configuring resource constraints
Using systemd gives you the option to put resource constraints on the backup process. E.g. you can limit the amount of memory and / or CPU. This is something you would configure in the systemd service unit. See .

Another way to constrain the resources used by restic is to use the  environment variable as described in the official documentation.

## systemd timer
You will also need a timer unit (this one runs every 15 min):

## Backup script
You will also want to create a small shell script to pass in all the required options, for example:

{{hc|/usr/local/bin/restic-backup|
#!/bin/bash

if pgrep -f 'restic backup' > /dev/null; then
  echo 'restic is already running...' 1>&2
  exit 0
fi

set -e
set -v

export RESTIC_REPOSITORY='/mnt/restic'
export RESTIC_PASSWORD_COMMAND='/usr/local/bin/get-restic-password'
export RESTIC_COMPRESSION='off'
export RESTIC_CACHE_DIR=~/.cache/restic

mkdir -p "${RESTIC_CACHE_DIR}"

restic unlock
restic backup / --exclude-file=/etc/restic/excludes.txt --tag scheduled
restic check --with-cache --read-data-subset=5G
restic forget --prune --keep-hourly 24 --keep-daily 30 --keep-monthly 6 --keep-weekly 4 --keep-yearly 3
}}

 # chmod 744 /usr/local/bin/restic-backup
 # chmod 700 /usr/local/bin/get-restic-password

## Compression
You might want to consider enabling compression in restic to save space if you are backing up data that is not already compressed (like large text files).

## Snapshot retention
Adjust the  values in the script above if wanted.

## Configuring niceness
You may also wish to tweak niceness of the backup process. If you are running backups often you will likely want to reduce the resource usage to prevent it from affecting interactive use. However, you should check how long the backups are taking and make sure they are not overlapping (i.e. a new backup being started when the previous one has not finished).

You can do that with . You may want to adjust the backup script by adding nice to the beginning of the resource intensive commands e.g.:

 # nice -n 19 restic backup ...
 # nice -n 19 restic check ...

Alternatively if you are using  you may want to ensure that the niceness is configured in its configuration file(s) under .

{{hc|/etc/ananicy.d/00-types.types|
{"type":"file-sync","nice":19,"ionice":7}
}}

{{hc|/etc/ananicy.d/99-custom/file-sync/restic.rules|
{"name": "restic", "type": "file-sync"}
}}

Refer to the restic FAQ for more information.

## Excludes list
Add the excludes file under  e.g.:

## Enable
Do not forget to enable the .

## Remote append-only backup repository
As with most backup solutions, restic backups can usually be modified by the user that executes the backup. This makes the backup data vulnerable to manipulation and threats like ransomware. While the above example runs the backup as root and thereby prevents trivial modification by local unprivileged users, a compromise of the system will allow malware to delete/overwrite the backup data as well, even if that data is in a remote repository (since the local user authenticates to the remote repository). In order to setup a secure backup solution that cannot be modified, restic can be used in combination with  to make use of its append-only feature run on a restricted remote system.

## Setup restricted 'rclone serve' over ssh
The following will restrict the user to the specified command, effectively allowing only the addition of new data to the path  while preventing the modification of existing files.

## Run restic through rclone
Initialize the backup repository on the remote ssh server:
 restic -o rclone.program='ssh myuser@backup.tld' -r rclone: init

Execute restic backup with rclone as transport:
 restic -o rclone.program='ssh myuser@backup.tld' -r rclone: backup /home/myuser/importantData

## Append-only script
Note that it is no longer possible to use the prune option in order to delete old backups since no data on the remote repository can be modified now. The user can only write-append new files and read existing backup data to restore.

{{hc|/usr/local/bin/restic-backup|
#!/bin/bash

if pgrep -f 'restic backup' > /dev/null; then
  echo 'restic is already running...' 1>&2
  exit 0
fi

set -e
set -v

export RESTIC_REPOSITORY="rclone:"
export RESTIC_PASSWORD_COMMAND='/usr/local/bin/get-restic-password'
export RESTIC_COMPRESSION='off'
export RESTIC_CACHE_DIR=~/.cache/restic

RCLONE_EXEC="rclone.program=ssh myuser@backup.tld forced-command"
DATA_PATH="/home/myuser/importantData"

mkdir -p "${RESTIC_CACHE_DIR}"

restic -o "${RCLONE_EXEC}" unlock
restic -o "${RCLONE_EXEC}" backup ${DATA_PATH} --exclude-file="$HOME/.local/scripts/excludes" --tag scheduled
restic -o "${RCLONE_EXEC}" check --with-cache --read-data-subset=5G
}}

## Restoring backup data
 restic -o rclone.program='ssh myuser@backup.tld forced-command' -r rclone: restore latest --target /tmp/restoredData

## Tips and tricks
## Password with token as second factor
The following employs a Universal 2nd Factor token, a YubiKey in this example, to derive a password used to unlock a restic repository with its  option. A prerequisite is an already set up challenge-response slot, since it can be used for multiple purposes.

First, a random user key is generated and fed into the token's challenge-response function to obtain its token-unique hash:

 $ dd if=/dev/urandom of=/home/username/resticblob bs=512 count=1
 $ chmod 400 /home/username/resticblob
 $ ykchalresp -2 -i/home/username/resticblob
 71832e30cf9d5adb8672154d7a83fa1684f544d3

Second, the hash is copy-pasted to be added as a user access key to the restic repository.

 $ restic -r /home/username/restic/ key add
 enter password for repository:
 repository 045a06ef opened (version 2, compression level auto)
 enter new password:
 enter password again:
 saved new key with ID 1991e876106f203c245e45a401b59dedec4aae6656f89152b66eca180385c1b

Now, the token can be used to access the repository transparently:

 $ restic -r /home/username/restic unlock --password-command "ykchalresp -2 -i/home/username/resticblob"
 repository 045a06ef opened (version 2, compression level auto)

Note for the non-interactive use this method requires a token configuration without user-presence (touch) verification for the challenge-response method and some tokens do not allow to configure the feature. The same restriction applies for other methods, unless the  option is used to execute a shell script to prepare its output accordingly. Also possible is to use the  option, see for example.
