# Borg backup

BorgBackup (short: Borg) is a deduplicating backup program. Optionally, it supports compression and authenticated encryption.

The main goal of Borg is to provide an efficient and secure way to backup data. The data deduplication technique used makes Borg suitable for daily backups since only changes are stored. The authenticated encryption technique makes it suitable for backups to not fully trusted targets.

## Installation
Install the  package. The next major release, version 2, is available as beta with .

For additional features, install the following packages:

; : for mounting archives
; : for connecting to remote hosts
; : a set of wrapper scripts to control Borg via YAML files instead of terminal commands (borgmatic, (Website)
; : borgbackup without bash scripts - similar to borgmatic with a slightly different feature set (borgctl)
; : a libadwaita/GTK4 based GUI for Borg
; : a Qt-based GUI for Borg
; : A TUI and CLI for regularly scheduled backups

If you wish to backup to a different machine than the one where data is sourced, this other machine (the "server") also requires borg to be installed. In order to facilitate creation and management of backups, server administrators can take advantage of:

; : a WebUI for a Borg's central repository server, comparable to the paid-service offered by https://www.borgbase.com/.
; : Get a report on repositories with statistics, warnings and error messages (optionally per email) and export OpenMetrics.

## Documentation
The official documentation includes a  quickstart guide. Local documentation can be found in  and .

Additionally, guidance can be found through the command, either generally:

 $ borg help

or for specific commands:

 $ borg help command

## Usage
The main concept behind Borg is de-duplication: rather than accumulating files as in traditional TAR archiving, de-duplication verifies the identity of files, regardless of their names, by hashing them so that they are only copied once. This means that even without compression, it takes up minimal space for repeated incremental backups.

File compression is optional and supports multiple algorithms (zstd is recommended) and intensities.

Archives created with Borg can be mounted as FUSE filesystems for browsing and restoring individual files.

Archives can be created locally, or on remote systems using SSHFS, NFS, Samba, or similar mounting solutions. Transfer over SSH is supported, but the remote host must have Borg available.

## Creating repositories
Borg repositories can be encrypted or made tamper-evident. For more information on modes and options, consult the official documentation on setting up a repository.

To create a Borg repository without encryption or authentication:

 $ borg init --encryption=none /path/to/repo

## Creating archives
Individual archive instances can be created within the repository with the  command. Each archive must be given a unique name. Borg includes a list of placeholders to make adding strings such at dates, times, usernames, and hostnames easier.

To create an archive of the  directory with the hostname of the source machine and the current date:

 $ borg create /path/to/repo::{hostname}-{now:%Y-%m-%d} archivable-dir

Borg supports extensive inclusion and exclusion options. To exclude  files from the archive:

 $ borg create ... --exclude '*.pyc' /path/to/repo::archive-name

More information can be found on the  documentation page.

## Pruning archives
The removal of old archives is not performed automatically, but can be performed manually with the  command. The number of archives to keep must be specified, and can be limited by the time the archive was created.

To keep only the last 7 daily archives, the last four weekly archives, and the last three monthly archives:

 $ borg prune --keep-daily=7 --keep-weekly=4 --keep-monthly=3 /path/to/repo

To keep only the last 10 archives, regardless of when they were created:

 $ borg prune --keep-last=10 /path/to/repo

To keep all archives from the past 30 days, regardless of how many archives that includes:

 $ borg prune --keep-within=30d /path/to/repo

More information can be found on the  documentation page.

## Restoring from an archive
To restore from an archive:

 $ borg extract /path/to/repo::archive-name path/to/restore

Alternatively, a repository can be mounted for interactive restoration:

 $ borg mount /path/to/repo::archive-name

## Tips and tricks
## Cache exclusion
Archives' size can be reduced by excluding cache directories. Directories that adhere to the Cache Directory Archiving Standard can be automatically excluded by appending  to the archive creation command:

 $ borg create ... --exclude-caches /path/to/repo::archive-name

## Listing affected files
Many operations in Borg support the  flag to list affected files or archives. If paired with , the user can verify the effects of a given command.
