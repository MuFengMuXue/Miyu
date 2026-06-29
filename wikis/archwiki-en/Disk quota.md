# Disk quota

From Wikipedia:
:"A disk quota is a limit set by a system administrator that restricts certain aspects of file system usage on modern operating systems. The function of setting quotas to disks is to allocate limited disk-space in a reasonable way."
This article covers the installation and setup of disk quota.

## Installation
Install the  package.

## Configuration
## Set up the filesystem
Edit fstab to enable the quota mount option(s) on selected file systems, e.g.:

To additionally enable the group quota mount option:

If supported by the kernel and file system it is recommended to use journaled quota instead:

Append  to enable group quota.

Remount the partition to apply the change:

 # mount -vo remount /home

## Create quota index
To create the quota index for :

 # quotacheck -cum /home

Append the  parameter to also create a group index.

To enable disk quotas for the desired file system:

 # quotaon -v /home

To disable disk quotas for the file system:

 # quotaoff -v /home

## Usage
## Enable quota for user/group
Quotas are configured using  (as the root user) that will be opened in the default configured text editor:

;blocks: Indicates number of 1k blocks currently used by the user/group.
;soft: Indicates max number of blocks for the user/group before a warning is issued and grace period countdown begins. If set to "0" (zero) then no limit is enforced.
;hard: Indicates max number of blocks for the user/group can use. If maximum amount has been reached, no further disk space can be used. If set to "0" (zero) then no limit is enforced.
;inodes: Indicates the current inodes amount used by the user/group.
;soft: Indicates the soft inode limit for the user/group.
;hard: Indicates the hard inode limit for the user/group.

Consider the following configuration for ftpuser1:

In this case if ftpuser1 uses over 976MB of space a warning will be issued. If the hard limit of 1GB has been reached the user will be unable to write any more data.

See #Specify a grace period to give users a specific amount of time to reduce storage usage when they hit their soft limit.

## Specify a grace period
To give current users some time to reduce their file usage, a grace period can be configured. This specifies the allowed time a user/group can exceed their soft limit and while under their hard limit:

The grace period can be set in seconds, minutes, hours, days, weeks or months.

## Reports
Shows all configured quotas:

 # repquota -a

Shows quotas on a specific partition:

 # repquota /home

Show quotas that apply to a user/user group:

 # quota -u user

 # quota -g group

## Copy quota settings
## To one or several users
To copy quota settings from  to :

 # edquota -p user1 user2

To copy quota settings to several other users, append   ...

## To groups
To copy quota settings from  to :

 # edquota -g -p group1 group2

## To all users
The idea is to modify the quota settings for one user and copy the setting to all other users. Set the quota for  and apply the quota to users with a UID greater than 999:

 # edquota -p user1 $(awk -F: '$3 > 999 {print $1}' /etc/passwd)

## Tips and tricks
## Quota warnings
The command  can be used to warn the users about their quota. Configuration is available in .

## Stats
The command  can be used to give more information about the current quota usage:
