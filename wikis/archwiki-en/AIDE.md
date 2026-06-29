# AIDE

Advanced Intrusion Detection Environment (AIDE) is a host-based intrusion detection system (HIDS) for checking the integrity of files. It does this by creating a baseline database of files on an initial run, and then checks this database against the system on subsequent runs. File properties that can be checked against include inode, permissions, modification time, file contents, etc.

AIDE only does file integrity checks. It does not check for rootkits or parse logfiles for suspicious activity, like some other HIDS (such as OSSEC) do. For these features, you can use an additional HIDS (see for a possibly biased comparison), or use standalone rootkit scanners (rkhunter, chkrootkit) and log monitoring solutions (logwatch, logcheck).

## Installation
You can install the  package, or you can instead install  if you want to use it in a system with SELinux and Audit framework enabled.

## Configuration
The default configuration file at  has defaults based on Fedora and is heavily commented. If you want to change the rules, see  and the [https://aide.github.io/doc/ AIDE Manual for further documentation.

## Usage
To check your configuration, use .

To initialize the database, use  or . Depending on your configuration and system, this command can take a while to complete.

You can check the system against the baseline database using , or update the baseline db using .

For more info, see .

## Cron
AIDE can be run manually if desired, but you may want to run it automatically instead. How you set this up will depend on your cron daemon and MUA (if email notification is desired).

If cron is set up to automatically mail all job output, it can be as simple as

For examples of more complicated cron scripts see or [https://rfxn.com/downloads/cron.aide.

## Security
Since the database is stored on the root filesystem, attackers can easily modify it to cover their tracks if they compromise your system. You may want to copy the database to offline, read-only media and perform checks against this copy periodically.
