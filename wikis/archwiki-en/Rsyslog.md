# Rsyslog

rsyslog is a syslog implementation that offers many benefits over syslog-ng. It can be configured to receive log entries from systemd's journal in order to process or filter them before quickly writing them to disk or sending them over network.

## Installation
Install the  package.

## Enabling and starting service
After installation, enable  and start it afterwards.

Starting the  unit first would likely fail, because enabling the service creates a symlink for  which would be missing otherwise;  would raise the error:

## Configure hostname
Rsyslog uses the  routine  or  to determine the hostname of the local machine. The  or  routine check the contents of  for the fully qualified domain name (FQDN) if you are not using BIND or NIS.

You can check what the local machine's currently configured FQDN is by running . The output of  will be used by rsyslog when writing log messages. If you want to have full hostnames in logs, you need to add  to the beginning of the file (before using any directive that write to files). This is because, rsyslog reads its configuration file and applies it on-the-go and then reads the later lines.

The  file contains a number of lines that map FQDNs to IP addresses and that map aliases to FQDNs. See the example  file below:

 is the first item following the IP address, so  function will return localhost.localdomain as the local machine's FQDN. Then  file will use localhost as hostname.

To use somehost as the hostname. Move somehost.localdomain to the first item:

## Configuration
rsyslog is configured in . See the official documentation for more information on the available configuration options.

By default, all syslog messages are handled by systemd's journal. In order to gather system logs in rsyslog, you either have to turn on #journald's syslog-forward feature or use the #imjournal module of rsyslog to gather the logs by importing it from the systemd journald.

## imjournal
If you want rsyslog to pull messages from systemd, load the imjournal module:

See the documentation on the imjournal input module for more information.

## journald's syslog-forward feature
Log output can be fine tuned in . The daemon uses Facility levels (see below) to determine what gets put where. For example:

States that all messages falling under the authpriv facility are logged to .

Another example, which would be similar to the behaviour of syslog-ng for the old :

See Systemd/Journal#Journald in conjunction with syslog for more information.

## Facility levels
{| class="wikitable"
|-
! Facility Number !! Keyword !! Facility Description
|-
| 0 || kern || kernel messages
|-
| 1 || user || user-level messages
|-
| 2 || mail || mail system
|-
| 3 || daemon || system daemons
|-
| 4 || auth || security/authorization messages
|-
| 5 || syslog || messages generated internally by syslogd
|-
| 6 || lpr || line printer subsystem
|-
| 7 || news ||  network news subsystem
|-
| 8 || uucp || UUCP subsystem
|-
| 9 || || clock daemon
|-
| 10 || authpriv || security/authorization messages
|-
| 11 || ftp || FTP daemon
|-
| 12 || - || NTP subsystem
|-
| 13 || - || log audit
|-
| 14 || - || log alert
|-
| 15 || cron || clock daemon
|-
| 16 || local0 || local use 0  (local0)
|-
| 17 || local1 || local use 1  (local1)
|-
| 18 || local2 || local use 2  (local2)
|-
| 19 || local3 || local use 3  (local3)
|-
| 20 || local4 || local use 4  (local4)
|-
| 21 || local5 || local use 5  (local5)
|-
| 22 || local6 || local use 6  (local6)
|-
| 23 || local7 || local use 7  (local7)
|}

## Severity levels
As defined in RFC 5424, there are eight severity levels:

{| class="wikitable"
|-
! Code !! Severity !! Keyword !! Description !! General Description
|-
| 0 || Emergency || emerg (panic) || System is unusable. || A "panic" condition usually affecting multiple apps/servers/sites. At this level it  would usually notify all tech staff on call.
|-
| 1 || Alert || alert || Action must be taken immediately. || Should be corrected immediately, therefore notify staff who can fix the problem. An example would be the loss of a primary ISP connection.
|-
| 2 || Critical || crit || Critical conditions. || Should be corrected immediately, but indicates failure in a primary system, an example is a loss of a backup ISP connection.
|-
| 3 || Error || err (error) || Error conditions. || Non-urgent failures, these should be relayed to developers or admins; each item must be resolved within a given time.
|-
| 4 || Warning || warning (warn) || Warning conditions. || Warning messages, not an error, but indication that an error will occur if action is not taken, e.g. file system 85% full - each item must be resolved within a given time.
|-
| 5 || Notice || notice || Normal but significant condition. || Events that are unusual but not error conditions - might be summarized in an email to developers or admins to spot potential problems - no immediate action required.
|-
| 6 || Informational || info || Informational messages. || Normal operational messages - may be harvested for reporting, measuring throughput, etc. - no action required.
|-
| 7 || Debug || debug || Debug-level messages. || Info useful to developers for debugging the application, not useful during operations.
|}

## Examples
## journald with rsyslog for kernel messages
Since the syslog component of systemd, journald, does not flush its logs to disk during normal operation, these logs will be gone when the machine is shut down abnormally (power loss, kernel lock-ups, ...). In the case of kernel lock-ups, it can be important to have some kernel logs for debugging. Until journald gains a configuration option for flushing kernel logs, rsyslog can be used in conjunction with journald.

Summary of requirements:

* journald must still get all log messages.
* rsyslog must only log kernel messages, all other logs are handled by journald.
* Kernel logs must be logged separatedly to .
* Use systemd to start the service.

Installation and configuration steps:

# Install .
# Edit  and add  to the list of logs. Without this modification, the kernel log would grow indefinitely.
# Edit  and comment everything except for . If a heart-beat (repeated confirmation that the log is alive) is preferred,  should remain uncommented as well.
# Add the next line to the same configuration file:
#:
#:The  part catches all messages originating from the kernel.  is used here to use a less verbose date format. By default, a date format like  is used. Since the kernel log contains a precision already (printk time) and the actual log time is irrelevant, a format like  might be preferred.
# Since rsyslog should operate completely separated from systemd, remove the option that shares a socket with systemd:
#:
# Next, make rsyslog start on boot and start it for this session by starting and enabling .
