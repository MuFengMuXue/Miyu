# Rsnapshot

Rsnapshot is an open source utility that provides incremental back ups.

## Installation
Install the  package.

## Configuration
In the install process, the configuration file is created. It is recommended you make a back up of this file in case you need to reconfigure the file again.

 # cp /etc/rsnapshot.conf /etc/rsnapshot.conf.default

The  file is well commented and much of it should be fairly self-explanatory. For a full reference of all the various options, please consult .

## Root Directory
Choose the directory where you want to store the file system back ups, in this case I will store the back ups in

## External program dependencies
Uncomment the lines referring to the UNIX commands , ,  (if you want to do remote back ups) and , etc. This section of the file should look like this:

## Retain Previous Backups
Rsnapshot allows named backup levels that retain a given number of previous backups.

When configuring these, note that the first in the list will be the only one that actually backs up files from the file system AND rotates its own previous backups. The rest will ONLY rotate previous backups, creating its newest backup from the oldest backup created by the previous item on the list. So, the order these are listed in the configuration file are very important.

Replace the default "BACKUP LEVELS / INTERVALS" section in the rsnapshot configuration file:

* When  is called, a new backup will be created from the file system, and saved in /hourly.0/. The rest of the retained backups will continue to get incremented each time the command is run. So eventually, what was /hourly.0, will become /hourly.23/. Then the next time the command is run, this will be deleted.

* When  is called, it will create /daily.0/ from the /hourly.23/ backup if it exists. Otherwise, rotation works the same way.

* Likewise, when  is called, it will create /weekly.0/ from the /daily.6/ backup if it exists. The pattern follows the same for each additional retain level that is configured.

Using the above config, you could call:

 every hour

 every day

 every week

 every month

This would give you a robust 12 months of backups while minimizing the space taken up by older snapshots.

If you just wanted to run this same config, but only backup daily, you would need to comment out the hourly backup level. Otherwise calling  would never actually backup any files since it is not the first on the list.

## Back up
This is the section where you tell rsnapshot which files you actually want to back up. You put a  parameter first, followed by the full path to the directory or network path you are backing up. The third column is the relative path you want to back up to inside the snapshot root.

In this example, backup tells us it is a backup point.  is the full path to the directory we want to take snapshots of, and  is a directory inside the  we are going to put them in. Using the word localhost as the destination directory is just a convention. You might also choose to use the server's fully qualified domain name instead of localhost. If you are taking snapshots of several machines on one dedicated backup server, it is a good idea to use their various hostnames as directories to keep track of which files came from which server.

## Remote Systems
In addition to full paths on the local filesystem, you can also backup remote systems using rsync over ssh. If you have ssh installed and enabled - via the  parameter - you can specify a path like:

This behaves fundamentally the same way, but you must take a few extra things into account:

*The ssh daemon must be running on example.com

*You must have access to the account you specify the remote machine, in this case the root user on example.com.

*You must have key-based logins enabled for the root user at example.com, without passphrases. If you wanted to perform backups as another user, you could specify the other user instead of root for the source (i.e. user@domain.com). Please note that allowing remote logins with no passphrase is a security risk that may or may not be acceptable in your situation. Make sure you guard access to the backup server very carefully! For more information on how to set this up, please consult the ssh man page, or a tutorial on using ssh public and private keys. You will find that the key based logins are better in many ways, not just for rsnapshot but for convenience and security in general. One thing you can do to mitigate the potential damage from a backup server breach is to create alternate users on the client machines with uid and gid set to 0, but with a more restrictive shell such as scponly.

*This backup occurs over the network, so it may be slower. Since this uses rsync, this is most noticeable during the first backup. Depending on how much your data changes, subsequent backups should go much, much faster since rsync only sends the differences between files.

## Extra Scripts
There is an extra  line. With this parameter, the second column is the full path to an executable backup script, and the third column is the local path you want to store it in (just like with the  parameter). For example:

In this example, rsnapshot will run the script  in a temp directory, then sync the results into the  directory under the snapshot root.

Your backup script simply needs to dump out the contents of whatever it does into its current working directory. It can create as many files and/or directories as necessary, but it should not put its files in any pre-determined path. The reason for this is that rsnapshot creates a temp directory, changes to that directory, runs the backup script, and then syncs the contents of the temp directory to the local path you specified in the third column. A typical backup script would be one that archives the contents of a database. It might look like this:

## Testing the configuration
When you have made all your changes, you should verify that the configuration file is syntactically valid, and that all the supporting programs are where you think they are. To do this, run rsnapshot with the configtest argument:

 # rsnapshot configtest

If all is well, it should say Syntax OK. If there is a problem, it should tell you exactly what it is. Make sure your configuration file is using tabs and not spaces, etc.

The final step to test your configuration is to run rsnapshot in test mode. This will print out a verbose list of the things it will do, without actually doing them. To do a test run, run this command:

 # rsnapshot -t hourly

This tells rsnapshot to simulate an "hourly" backup. It should print out the commands it will perform when it runs for real.

## Automation
Now that you have your configuration file set up, it is time to set up rsnapshot to be run automatically.

First create a service file:

Then create a timer unit for each interval you want the service to run (i.e. hourly, daily, weekly, montly):

You can verify your  entries are valid and do what you expect (especially if you want to change the above) with:

 # systemd-analyze calendar "Mon *-*-* 04:30:00"

Then finally, enable/start them and verify that the resulting unit status looks good, and that the timers are scheduled as expected:

 # systemctl list-timers rsnapshot*

Now you can wait for the first timer to trigger, or if you want to start one immediately you can do it manually.

## External Drives
If the destination drive is in an external enclosure connected via USB or eSATA, it may not have mounted during boot or may otherwise be unmounted at the time rsnapshot is scheduled to begin. If rsnapshot is configured to write to a path that always exists, e.g. , the data will be backed up on whichever hard drive is mounted as the root directory rather than the desired external drive.

To remedy this situation one must configure rsnapshot to depend upon the disk being mounted to the expected mount point. There are two actions required: alter  and .

Systemd will read the  file and create unit files for all of the mount points therein. For this setup we need to add one, optionally two, configuration options to the mount point. At the end of the options column for the desired mount point add  and, if you want the mount point to unmount after inactivity, . The value 10m can be changed to any value you wish. See  and  for additional details about the options available.

An example mount point:

After changing , run a daemon-reload so systemd picks up the changes made. Check that the mount and automount units look correct:

Finally, edit  and add the following line in the "section:

To ensure everything is configured properly check that the rsnapshot service units now require the mount point:

## How it works
We have a snapshot root under which all backups are stored. In this example, this is the directory . Within this directory, other directories are created for the various intervals that have been defined. In the beginning it will be empty, but once rsnapshot has been running for a week, it should look something like this:

 [root@localhost# ls -l /mnt/backups/
 drwxr-xr-x    7 root     root         4096 Dec 28 00:00 daily.0
 drwxr-xr-x    7 root     root         4096 Dec 27 00:00 daily.1
 drwxr-xr-x    7 root     root         4096 Dec 26 00:00 daily.2
 drwxr-xr-x    7 root     root         4096 Dec 25 00:00 daily.3
 drwxr-xr-x    7 root     root         4096 Dec 24 00:00 daily.4
 drwxr-xr-x    7 root     root         4096 Dec 23 00:00 daily.5
 drwxr-xr-x    7 root     root         4096 Dec 22 00:00 daily.6
 drwxr-xr-x    7 root     root         4096 Dec 29 00:00 hourly.0
 drwxr-xr-x    7 root     root         4096 Dec 28 20:00 hourly.1
 drwxr-xr-x    7 root     root         4096 Dec 28 16:00 hourly.2
 drwxr-xr-x    7 root     root         4096 Dec 28 12:00 hourly.3
 drwxr-xr-x    7 root     root         4096 Dec 28 08:00 hourly.4
 drwxr-xr-x    7 root     root         4096 Dec 28 04:00 hourly.5

Inside each of these directories is a full backup of that point in time. The destination directory paths you specified under the  and  parameters get stuck directly under these directories. In the example:

 backup          /etc/           localhost/

The  directory will initially get backed up into

Each subsequent time rsnapshot is run with the hourly command, it will rotate the hourly.X directories, and then copy the contents of the hourly.0 directory (using hard links) into hourly.1.

When rsnapshot daily is run, it will rotate all the daily.X directories, then copy the contents of hourly.5 into daily.0.

hourly.0 will always contain the most recent snapshot, and daily.6 will always contain a snapshot from a week ago. Unless the files change between snapshots, the full backups are really just multiple hard links to the same files. Thus, if your  file does not change in a week,  and  will literally be the same exact file. This is how rsnapshot can be so efficient on space. If the file changes at any point, the next backup will unlink the hard link in hourly.0, and replace it with a brand new file. This will now take double the disk space it did before, but it is still considerably less than it would be to have full unique copies of this file 13 times over.

Remember that if you are using different intervals than the ones in this example, the first interval listed is the one that gets updates directly from the main filesystem. All subsequently listed intervals pull from the previous intervals. For example, if you had weekly, monthly, and yearly intervals defined (in that order), the weekly ones would get updated directly from the filesystem, the monthly ones would get updated from weekly, and the yearly ones would get updated from monthly.
