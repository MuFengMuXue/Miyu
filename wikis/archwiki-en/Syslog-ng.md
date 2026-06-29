# Syslog-ng

syslog-ng is a syslog implementation which can take log messages from sources and forward them to destinations, based on powerful filter directives. Although its origins are syslog, it is a pretty generic log management tool, being able to consume structured and unstructured log messages, parsing and transforming them if necessary.

## Overview
syslog-ng takes incoming log messages from defined 'sources' and forwards them to the appropriate destinations, based on powerful filter directives. In a typical simple set-up, syslog-ng will read messages from three sources:

# the default  device, where most logs are sent
# syslog-ng "internal" log messages
#  kernel messages

Sources are defined using the "source" directive. These incoming messages are then filtered according to defined filters ("filter" keyword), i.e. according to originating program or log level, and sent to the appropriate "destination".

Destinations include log files (e.g. ), printing messages on a console and remote servers.

The pivotal function is log. This function defines which filters should be applied to a certain source, and where the resulting messages should be sent to.

Apart from local sources, as explained above, syslog-ng is also able to work with various sources over the network.  To work with these, you will have to create a  or  or  source as explained below.

## Installation
Install the  package.

To use syslog-ng, start/enable .

## systemd/journald integration
syslog-ng pulls in the messages from the systemd journal by default. Keeping  in  is recommended in order to avoid the overhead associated with the socket and to avoid needless error messages in the log. If on the other hand you do not want to store your logs twice and turn journalds , you will need , as syslog-ng tries to follow the 'journald' journal file.

See #syslog-ng and systemd journal for more details.

## Sources
syslog-ng receives log messages from a source. To define a source you should follow the following syntax:

 source  { source-driver(params); source-driver(params); ... };

In the simplest case, you will just need a single  driver.

 source src { system(); };

This will automatically detect the best way to collect local logs and will make sure kernel, application and internal logs from syslog-ng are all collected.

You can look at the identifiers and source-drivers in the alternative syslog-ng manuals (as the ones on syslog-ng.com were unreachable).

The  driver is actually a higher-level construct that expands to various sources as needed for the local system. But you can acquire more control by removing the  source and use the lower level drivers directly.

The  source-driver opens the given AF_UNIX socket and starts listening on it for messages.

The  source-driver "receives" messages generated internally, by syslog-ng itself.

Therefore, the following means:  gets messages from the  socket and syslog-ng.

 source src { unix-stream("/dev/log"); internal(); };

The kernel sends log messages to  and the  driver reads log messages from files. Therefore, the following means kernsrc gets messages from file :

 source kernsrc { file("/proc/kmsg"); };

To open a port to read data from a remote server a source must be defined with this syntax:

 source s_net { network(transport(tcp)); };

for UDP or

 source s_net { network(transport(udp)); };

to receive log messages via TCP. Both listen on port 514, unless overridden with the  parameter.

## syslog-ng and systemd journal
Starting with syslog-ng version 3.6.1 the default  source on Linux systems using systemd uses journald as its standard  source.

If you wish to use both the journald and syslog-ng, ensure the following settings are in effect. For systemd-journald, in the  file,  either set to  or unset (which defaults to auto) and  set to . For , you need the following  stanza:

{{hc|/etc/syslog-ng/syslog-ng.conf|
source src {
  system();
};
}}

If, on the other hand, you wish not to retain the journald logs, but only syslog-ng's text logs, set  in . This will store journald in ram. As of syslog-ng 3.6.3, syslog-ng is using journald as the system(); source so if you set , the systemd journal will drop all messages and not forward them to syslog-ng.

After the change restart the  and  daemons.

## Destinations
In syslog-ng, log messages are sent to files. The syntax is very similar to sources:

 destination  {destination-driver(params); destination-driver(params); ... };

You will be normally logging to a file, but you could log to a different destination-driver: pipe, Unix socket, TCP-UDP ports, terminals or to specific programs. Simply declaring a destination will not cause messages to be delivered to that destination: that will only happen as soon as you connect sources and destinations using log statements. Log statements can also include filters, thereby implementing a flexible log routing functionality.

This declaration instructs syslog-ng to send messages to :

 destination authlog { file("/var/log/auth.log"); };

If the user is logged in,  sends messages to the terminal of the specified user. If you want to send console messages to root's terminal if it is logged in:

 destination console { usertty("root"); };

Messages can be sent to a pipe with . The following sends xconsole messages to the pipe .
This needs some more configuration, so you could look at the sub-section xconsole below.

 destination xconsole { pipe("/dev/xconsole"); };

To send messages on the network, use . The following will send your log data out to another server.

 destination remote_server { udp("10.0.0.2" port(514)); };

You can also use the newer  driver syntax for the same:

 destination remote_server { network("10.0.0.2" port(514) transport(udp)); };

## Creating filters for messages
The syntax for the filter statement is:

 filter  { expression; };

Functions can be used in the expression, such as the function  which selects messages based on the syslog facility codes (kern, mail, auth, etc).
Apart from facility codes, each log message is associated with a severity value; where debug is the most verbose,
and panic only shows serious errors. You can find the facilities, log levels and priority names in  or in RFC 3164.
To filter those messages coming from authorization, like  use the following:

 filter f_auth { facility(auth); };

The facility expression can use the boolean operators , , and , so the following filter
selects those messages not coming from authorization, network news or mail:

 filter f_debug { not facility(auth, authpriv, news, mail); };

The function  selects messages based on its severity level, so if you want to select informational levels:

 filter f_info { severity(info); };

Functions and boolean operators can be combined in more complex expressions. The following line filters messages with a priority level from informational to warning not coming from auth, authpriv, mail and news facilities:

 filter f_messages { severity(info..warn) and not facility(auth, authpriv, mail, news); };

Messages can also be selected by matching a regular expression in the message with the function . For example this would match the main part of the message against the regexp "failed":

 filter f_failed { match("failed" value("MESSAGE")); };

In filter expressions, you can use both pre-defined and user defined macros. These are also called "hard" and "soft" macros respectively.

A list and documentation of all macros can be found in the syslog-ng documentation:

  "AMPM", "BSDTAG", "DATE, C_DATE, R_DATE, S_DATE", "DAY, C_DAY, R_DAY, S_DAY", "FACILITY", "FACILITY_NUM", "FULLDATE, C_FULLDATE, R_FULLDATE, S_FULLDATE", "FULLHOST", "FULLHOST_FROM", "HOUR, C_HOUR, R_HOUR, S_HOUR", "HOUR12, C_HOUR12, R_HOUR12, S_HOUR12", "HOST", "HOST_FROM", "ISODATE, C_ISODATE, R_ISODATE, S_ISODATE", "LEVEL_NUM", "LOGHOST", "MIN, C_MIN, R_MIN, S_MIN", "MONTH, C_MONTH, R_MONTH, S_MONTH", "MONTH_ABBREV, C_MONTH_ABBREV, R_MONTH_ABBREV, S_MONTH_ABBREV", "MONTH_NAME, C_MONTH_NAME, R_MONTH_NAME, S_MONTH_NAME", "MONTH_WEEK, C_MONTH_WEEK, R_MONTH_WEEK, S_MONTH_WEEK", "MSEC, C_MSEC, R_MSEC, S_MSEC", "MSG or MESSAGE", "MSGHDR", "MSGID", "MSGONLY", "PID", "PRI", "PRIORITY or LEVEL", "PROGRAM", "SDATA, .SDATA.SDID.SDNAME", "SEC, C_SEC, R_SEC, S_SEC", "SOURCEIP", "SEQNUM", "STAMP, R_STAMP, S_STAMP", "SYSUPTIME", "TAG", "TAGS", "TZ, C_TZ, R_TZ, S_TZ", "TZOFFSET, C_TZOFFSET, R_TZOFFSET, S_TZOFFSET", "UNIXTIME, C_UNIXTIME, R_UNIXTIME, S_UNIXTIME", "USEC, C_USEC, R_USEC, S_USEC", "YEAR, C_YEAR, R_YEAR, S_YEAR", "WEEK, C_WEEK, R_WEEK, S_WEEK", "WEEK_ABBREV, C_WEEK_ABBREV, R_WEEK_ABBREV, S_WEEK_ABBREV", "WEEK_DAY, C_WEEK_DAY, R_WEEK_DAY, S_WEEK_DAY", "WEEKDAY, C_WEEKDAY, R_WEEKDAY, S_WEEKDAY", "WEEK_DAY_NAME, C_WEEK_DAY_NAME, R_WEEK_DAY_NAME, S_WEEK_DAY_NAME".

To filter messages received from a particular remote host (as declared in the incoming message itself and not by its IP address), the  function must be used:

 filter f_host { host( "192.168.1.1" ); };

If you would rather filter on sending IP address, you can use the  filter:

 filter f_ipaddr { netmask( "192.168.1.1/32" ); };

## Log paths
syslog-ng connects sources, filters and destinations with log statements. The syntax is:

 log {source(s1); source(s2); ...
 filter(f1); filter(f2); ...
 destination(d1); destination(d2); ...
 flags(flag1flag2...); };

The following for example sends messages from  source to  destination filtered by  filter:

 log { source(src); filter(f_mail); filter(f_info); destination(mailinfo); };

A log statement describes a pipeline: it tells syslog-ng to take messages from a source (or multiple sources) and deliver them to a destination (or multiple destinations) assuming the associated filters are matching.

If you have multiple log statements that take messages from the same source, messages will be duplicated along with all of those pipelines. Of course, you can apply a different set of filters and therefore route messages selectively to multiple destinations.

Apart from filtering, syslog-ng can apply parsing or rewriting of messages. Parsing means the extraction of information from the message text, whereas rewriting a message means that syslog-ng can change/reformat messages as needed.

The  statement has a lot more to offer:

# You can stop processing subsequent log paths after the current one matches using flags(final).
# You can tell a log statement to grab messages that none of the other log statements captured using flags(fallback)
# You can create an arbitrary graph out of log pipelines by using embedded log statements and junctions, which help you to construct complex processing pipelines.

You can read more about  statements in a chapter of the syslog-ng documentation.

## Tips and tricks
After understanding the logic behind syslog-ng, many possible and complex configuration are possible. Here there are some examples.

## Have syslog-ng reload the configuration file
You can make syslog-ng re-evaluate the configuration file. You can do so manually by sending a  to the process, or reload .

## Failover Logging to Remote Host
This setup shows how to send the default unencrypted syslog packets across both TCP and UDP protocols, using the standard port (514) and an alternate port. This is sending the same output to the same machine 4 different ways to try and make sure packets make it. Mostly useful if you are debugging a remote server that fails to reboot. The different ports and protocols are to make it past any firewall filters or other network problems. Also useful for port-forwarding and using tunnels. Something like this setup is ideal to tunnel across an ssh connection that the prone-to-failover host initiates through a reverse connection.

{{bc|#sending to a remote syslog server on TCP and UDP ports (not encrypted)
destination askapache_failover_loghost {
    tcp("208.86.158.195" port(25214));
    udp("208.86.158.195" port(25214));
    udp("mysyslog1.dyndns.org" port(514));
};
log {
    source(src);
    destination(askapache_failover_loghost);
};
}}

And then on the loghost receiving these logs:

{{bc|#a USB redirected console for flexible viewing
destination debugging_console {
    file("/dev/ttyU1");
};

# listens on IP addresses and ports, sets the incoming settings
source prone_to_failover_host {
    tcp(ip(208.86.158.195),port(25214));
    udp(ip(208.86.158.195) port(25214));

    udp(default-facility(syslog) default-priority(emerg));
    tcp(default-facility(syslog) default-priority(emerg));
}

# log it
log {
    source(prone_to_failover_host);
    destination(debugging_console);
};
}}

## Move log to another file
In order to move some log from  to another file.

{{bc|#sshd configuration
destination ssh { file("/var/log/ssh.log"); };
filter f_ssh { program("sshd"); };
log { source(src); filter(f_ssh); destination(ssh); flags(final); };
}}

Make sure you add this block above your usual log statements. Due to  in the log statement, anything that matches the "sshd" filter would only be sent to  and processing of the message would stop at that point.

## Configuring as a loghost
Configuring your system to be a loghost is quite simple. Drop the following into your configuration, and create the needed directory.
With this simple configuration, log filenames will be based on the FQDN of the remote host,
and located in . After creating the remote directory, reload your syslog-ng configuration.

{{bc|source net { udp(); };
destination remote { file("/var/log/remote/${FULLHOST}-log"); };
log { source(net); destination(remote); };
}}

You could also consider the  source that will open multiple ports, accepting messages over multiple different syslog protocols that are usually deployed in the field.

## Improve performance
syslog-ng's performance can be improved in different ways:

## Write every so often
It seems that the old  option is called  now, where the writing to the file is buffered for  lines. Default is 100.

## Increase source batching limits
syslog-ng is doing message processing in parallel, as streams of messages are received using the many different source mechanisms. To avoid starving one source connection over the other, syslog-ng both uses threading and imposes limits on how much messages would it process from a single source connection at a time.

This means that even though a source application might have sent 1000 messages in a tight loop, syslog-ng would process it 100 pieces at a time (the exact limit is specified by ) and after every 100, it would re-check if other connections are also in need of processing. This has some overhead, and syslog-ng performance can be increased significantly by increasing

The other mechanism that can use tuning based on a specific use-case is the window size setting used for backpressure propagation. This is the  parameter that controls how many messages can be in-flight before a destination acknowledges them. By increasing the  you can let it work on more messages before it would stop to allow destinations to consume messages.

By increasing  your memory/disk buffer use will increase, as syslog-ng will have to put the messages somewhere.

## Avoid redundant processing and disk space
A single log message can be sent to different log files several times. For example, in the initial configuration file, we have the following definitions:

{{bc|
destination cron { file("/var/log/cron.log"); };
destination messages { file("/var/log/messages"); };
filter f_cron { facility(cron); };
filter f_messages { level(info..warn)
       and not facility(auth, authpriv, mail, news); };
log { source(src); filter(f_cron); destination(cron); };
log { source(src); filter(f_messages); destination(messages); };
}}

The same message from the  facility will end up in both the  and  files. To change this behavior we can use the  flag, ending up further processing with the message. Therefore, in this example, if we want messages from the  facility not ending up in the messages file, we should change the cron's log sentence by:

 log { source(src); filter(f_cron); destination(cron); flags(final); };

another way is to exclude the  facility from  filter:

 filter f_messages { level(info..warn) and not facility(cron, auth, authpriv, mail, news); };

## PostgreSQL Destination
This section will use two roles:  and .  will be the administrator of the database  and  will only be able to add records to the  table.

No longer needed to create table for logs. syslog-ng will create automatically.
 psql -U postgres

 postgres=# CREATE ROLE syslog WITH LOGIN;
 postgres=# \password syslog    # Using the \password function is secure because
 postgres=# CREATE ROLE logwriter WITH LOGIN;
 postgres=# \password logwriter # the password is not saved in history.
 postgres=# CREATE DATABASE syslog OWNER syslog;
 postgres=# \q # You are done here for the moment

Edit  to allow  and  to establish a connection to PostgreSQL.

Then reload .

Edit  so that it knows where and how to write to PostgreSQL. syslog-ng will utilize the  role.

{{bc|...
#
# SQL logging support
#

destination d_pgsql {
  sql(type(pgsql)
  host("127.0.0.1") username("logwriter") password("password")
  database("syslog")
  table("logs_${HOST}_${R_YEAR}${R_MONTH}${R_DAY}") #or whatever you want, example ${HOST}" for hosts, ${LEVEL}" for levels.. etc
  columns("datetime timestamp with time zone", "host varchar(32)", "program varchar(16)", "pid varchar(16)", "message varchar(200)")
  values("$R_ISODATE", "$HOST", "$PROGRAM", "$PID", "$MSG")
  indexes("datetime", "host", "program", "pid", "message"));
};

log { source(src); destination(d_pgsql); };
}}

Finally, restart .

And check to see if things are being logged.
 psql -U logwriter -d syslog
 syslog=> SELECT * FROM  ORDER BY datetime DESC LIMIT 10;

## ISO 8601 timestamps
Before :
 #logger These timestamps are not optimal.
 #tail -n 1 /var/log/messages.log
 Feb 18 14:25:01 hostname logger: These timestamps are not optimal.
 #

Add  to  in the options section. Example:
 options {
   stats_freq (0);
   flush_lines (0);
   time_reopen (10);
   log_fifo_size (1000);
   long_hostnames(off);
   use_dns (no);
   use_fqdn (no);
   create_dirs (no);
   keep_hostname (yes);
   perm(0640);
   group("log");
   ts_format(iso);      #make ISO-8601 timestamps
   #frac-digits(3);     #optional time to nearest millisecond
 };

Then reload .

After :
 #logger Now THAT is a timestamp!
 #tail -n 2 /var/log/messages.log
 Feb 18 14:25:01 hostname logger: These timestamps are not optimal.
 2010-02-18T20:23:58-05:00 electron logger: Now THAT is a timestamp!
 #

## RFC 3339 timestamps
Same as above, except use  instead of  for

## Log Levels
Log levels are defined separately for each logged facility in syslog-ng config. Available log levels are listed in :

## Macros and Variables
Macros can be used in both templates, and in destination file names.  Macros of syslog-ng OSE.

The following code will write the log lines to  in the format of .

{{bc|template t_test { template("PROGRAM=$PROGRAM@PID=$PID@BSDTAG=$BSDTAG@TAG=$TAG@TAGS=$TAGS@FACILITY=$FACILITY@FACILITY_NUM=$FACILITY_NUM@LEVEL=$LEVEL@LEVEL_NUM=$LEVEL_NUM@PRI=$PRI@PRIORITY=$PRIORITY@FULLHOST=$FULLHOST@FULLHOST_FROM=$FULLHOST_FROM@HOST=$HOST@HOST_FROM=$HOST_FROM@LOGHOST=$LOGHOST@MSGHDR=$MSGHDR@MSGID=$MSGID@MSGONLY=$MSGONLY@MSG=$MSG@MESSAGE=$MESSAGE@SOURCE=$SOURCE@SOURCEIP=$SOURCEIP@SOURCE_IP=$SOURCE_IP@SEQNUM=$SEQNUM@UNIXTIME=$UNIXTIME@FULLDATE=$FULLDATE@ISODATE=$ISODATE@DATE=$DATE@STAMP=$STAMP@TZ=$TZ@TZOFFSET=$TZOFFSET@SEC=$SEC@MIN=$MIN@HOUR=$HOUR@HOUR12=$HOUR12@DAY=$DAY@WEEK=$WEEK@WEEK_DAY=$WEEK_DAY@WEEK_DAY_ABBREV=$WEEK_DAY_ABBREV@WEEK_DAY_NAME=$WEEK_DAY_NAME@MONTH=$MONTH@MONTH_ABBREV=$MONTH_ABBREV@MONTH_NAME=$MONTH_NAME@MONTH_WEEK=$MONTH_WEEK@YEAR=$YEAR@YEAR_DAY=$YEAR_DAY
\n"); template_escape(no); };

destination d_test { file("/var/log/test.log" template(t_test)); };

log { source(s_local); destination(d_test); flags(final); };
}}

You can create your own value list as below once syslog-ng is restarted with:

## Receive and parse common syslog messages
Starting from version 3.16 syslog-ng is capable to receive and parse messages on the most common ports with the most common parsers using the default-network-drivers() source driver.
* Default listening ports:
** 514, both TCP and UDP, for RFC3164 (BSD-syslog) formatted traffic
** 601 TCP, for RFC5424 (IETF-syslog) formatted traffic
** 6514 TCP, for TLS-encrypted traffic
* Automatic parsers:
** RFC3164 message parser
** RFC5424 message parser
** Cisco parser
** Structured EWMM parser
** Other application adapters (Splunk Common Information Model (CIM), iptables, or sudo)
