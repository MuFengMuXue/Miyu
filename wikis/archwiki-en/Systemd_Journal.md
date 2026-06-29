# Systemd/Journal

systemd has its own logging system called the journal; running a separate logging daemon is not required.

systemd journal classifies messages by Priority level and Facility. Logging classification corresponds to classic Syslog protocol (RFC 5424).

## Accessing the journal
The journal is read using , typically in one of two ways: inspecting previous logs, or watching new entries as they are logged.
For the former, the / option is typically useful; the latter is enabled by the / option.

## Filtering output
journalctl allows its output to be filtered in many ways.
This is useful to make logs easier to sift through,  because journalctl can struggle displaying logs in real-time if there are too many of them...

Non-option arguments enable filtering by journal fields (e.g. , see ), executable path, or kernel device, as described in .
See Lennart Poettering's blog post for some examples.

A full list of additional options, and the short form of the following, is available at , but here are the most common ones:

* Show all messages matching :
: This should be preferred over , as it avoids journalctl performing more work only for it to be discarded.
* Include explanations of log messages from the message catalog where available:  Note that this feature should not be used when attaching logs to bug reports and support threads, as to limit extraneous output. You can list all known catalog entries by running .
* Show all messages from a given time onwards ():
* Show all messages from the current boot:
* Show all messages by a specific identifier:
* Show all messages by a specific unit: (the  suffix can be omitted)
: Note that user services require the use of  instead:
* Show only error, critical and alert priority messages:  You can use numeric log level too, like . If single number/log level is used, , then all higher priority log levels are also included (i.e. 0 to 3 in this case).
* If the journal directory (by default located under ) contains a large amount of log data then  can take several minutes to filter output. It can be sped up significantly by using  option to force  to look only into most recent journal:

## Specify a different journal to view
There may be a need to check the logs of another system that is dead in the water, like booting from a live system to recover a production system. In such case, one can mount the disk in e.g. , and specify the journal path via /, like so:

 # journalctl -D /mnt/var/log/journal -e

## Examining journal without
While the journal is stored in a binary format, the content of stored messages is not modified.
This means it is viewable with , for example for recovery in an environment which does not have systemd installed, e.g.:

## Priority level
A syslog severity code (in systemd called priority) is used to mark the importance of a message RFC 5424 6.2.1.

{| class="wikitable"
|-
! Value !! Severity !! Keyword  !! Description !! Examples
|-
| 0 || Emergency || emerg || System is unusable || Severe Kernel BUG, systemd dumped core.This level should not be used by applications.
|-
| 1 || Alert || alert || Should be corrected immediately || Vital subsystem goes out of work. Data loss. .
|-
| 2 || Critical || crit || Critical conditions || Crashes, coredumps. Like familiar flash:Failure in the system primary application, like X11.
|-
| 3 || Error || err || Error conditions || Non-fatal error reported:,,
|-
| 4 || Warning || warning || May indicate that an error will occur if action is not taken || A non-root file system has only 1GB free.
|-
| 5 || Notice || notice || Events that are unusual, but not error conditions || ,
|-
| 6 || Informational || info ||  Normal operational messages that require no action ||
|-
| 7 || Debug || debug || Messages which may need to be enabled first, only useful for debugging ||
|}

These rules are recommendations, and the priority level of a given error is at the application developer's discretion. It is always possible that the error will be at a higher or lower level than expected.

## Facility
A syslog facility code is used to specify the type of program that is logging the message RFC 5424 6.2.1.

{| class="wikitable"
! Facility code !! Keyword !! Description !! Info
|-
| 0 || kern || Kernel messages
|-
| 1 || user || User-level messages
|-
| 2 || mail || Mail system || Archaic POSIX still supported and sometimes used (for more )
|-
| 3 || daemon || System daemons || All daemons, including systemd and its subsystems
|-
| 4 || auth || Security/authorization messages || Also watch for different facility 10
|-
| 5 || syslog || Messages generated internally by syslogd || For syslogd implementations (not used by systemd, see facility 3)
|-
| 6 || lpr || Line printer subsystem (archaic subsystem)
|-
| 7 || news || Network news subsystem (archaic subsystem)
|-
| 8 || uucp || UUCP subsystem (archaic subsystem)
|-
| 9 || || Clock daemon || systemd-timesyncd
|-
| 10 || authpriv || Security/authorization messages || Also watch for different facility 4
|-
| 11 || ftp || FTP daemon
|-
| 12 || - || NTP subsystem
|-
| 13 || - || Log audit
|-
| 14 || - || Log alert
|-
| 15 || cron || Scheduling daemon
|-
| 16 || local0 || Local use 0  (local0)
|-
| 17 || local1 || Local use 1  (local1)
|-
| 18 || local2 || Local use 2  (local2)
|-
| 19 || local3 || Local use 3  (local3)
|-
| 20 || local4 || Local use 4  (local4)
|-
| 21 || local5 || Local use 5  (local5)
|-
| 22 || local6 || Local use 6  (local6)
|-
| 23 || local7 || Local use 7  (local7)
|}

Useful facilities to watch: 0, 1, 3, 4, 9, 10, 15.

## Journal storage
In Arch Linux, the directory  is a part of the  package. Since the default mode for the journal is , the journal will write to , and the directory will be created if it is not present. If the mode is manually configured to , systemd will instead write its logs to  in a non-persistent way.

## Journal size limit
The default size limit for persistent journals (the default mode) corresponds to 10% of the size of the underlying file system, but has a soft-cap at 4 GiB. For example, with  located on a 20 GiB partition, journal data may take up to 2 GiB. On a 50 GiB partition, it would at max. at 4 GiB. To confirm the current limits on your system, review  unit logs:

 # journalctl -b -u systemd-journald

The maximum size of the persistent journal can be controlled by uncommenting and changing the following:

It is also possible to use the drop-in snippets configuration override mechanism rather than editing the global configuration file. In this case, place the overrides under the  header:

Restart the  after changing this setting to apply the new limit.

See  for more info.

## Clean journal files manually
Journal files can be globally removed from  using e.g. , or can be trimmed according to various criteria using . For example:

* Remove archived journal files until the disk space they use falls below 100M:
* Make all journal files contain no data older than 2 weeks.

Journal files must have been rotated out and made inactive before they can be trimmed by vacuum commands. Rotation of journal files can be done by running . The  argument can also be provided alongside one or more vacuum criteria arguments to perform rotation and then trim files in a single command.

See  for more info.

## Tips and tricks
## Per unit size limit by a journal namespace
Edit the unit file for the service you wish to configure (for example sshd) and add  in the  section.

Then create  by copying . After that, edit  and adjust  to your liking.

Restarting the service should automatically start the new journal service . The logs from the namespaced service can be viewed with .

See  for details about journal namespaces.

## Journald in conjunction with syslog
Compatibility with a classic, non-journald aware syslog implementation can be provided by letting systemd forward all messages via the socket . To make the syslog daemon work with the journal, it has to bind to this socket instead of  (official announcement).

The default  for forwarding to the socket is  to avoid system overhead, because rsyslog or syslog-ng pull the messages from the journal by itself.

See Syslog-ng#Overview and Syslog-ng#syslog-ng and systemd journal, or rsyslog respectively, for details on configuration.

## Forward journald to /dev/tty12
Create a drop-in directory  and create a  file in it:

Then restart .

## Journal access as user
By default, a regular user only has access to their own per-user journal. To grant read access for the system journal as a regular user, you can add that user to the  user group. Members of the  and  groups are also given read access.

See  and Users and groups#User groups for more information.

## Desktop notifications
Desktop notifications can help you quickly notice error messages, improving awareness compared to manually checking logs or not noticing them at all.

The  package provides an automatic desktop notification for each error message logged by any process.
For more details and configuration options, visit the GitLab project page.

## Hiding the hostname
By default,  shows the hostname of the machine which generated the logs, which is pertinent if you are viewing the logs of multiple machines at once (possibly on different terminals).
But, in other cases, the / option can help make lines shorter.

## Wrap journal lines instead of truncating them
By default, journalctl truncates lines longer than screen width, but in some cases, it may be better to enable wrapping instead of truncating.
This can be controlled by the  environment variable, which contains options passed to less (the default pager) and defaults to  (see  and  for details).

By omitting the  option, the output will be wrapped instead of truncated. For example, start journalctl as follows:

To set this behaviour as default, add this as an environment variable.

## Printing kernel messages only
journalctl can be used as a  alternative:

 # journalctl --dmesg
