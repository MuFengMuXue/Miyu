# Monit

Monit, not to be confused to M/Monit, is an AGPL3.0 licensed system and process monitoring tool.  Monit can automatically restart crashed services, display temperatures from standard hardware (through lm_sensors and hard drives from  for example).  Service alerts can be sent based on a wide criteria including a single occurrence or occurrences over a period of time.  It can be accessed directly through the command line or ran as a web app using its integrated HTTP(S) server.  This allows quick and streamlined snapshot of a given systems status.

## Installation
Install the  package and any software for optional testing such as  or . Once you have completed the configuration, be sure to enable and start .

## Configuration
Monit keeps a main configuration file as . You can choose to edit this file but if you wish to run scripts (such as to get hard drive temperatures or health status) you should uncomment the last directive of , save  and create .

## Configuration syntax
Monit utilizes a configuration syntax that makes it very easy to read; essentially  followed by  format. Any occurrence of , , , , , , , ,  in the configuration file is for human readability only and are completely ignored by Monit.

Checks are usually performed in . This is defined at the beginning of the configuration file, for example a 30second poll is defined with:

Checks with  would therefore happen every 2 minutes

## Configuration examples
## Mailserver declaration
## Email notification format
{{bc|set mail-format {
      from: Monit@MyServer
   subject: $SERVICE $EVENT at $DATE
   message: Monit $ACTION $SERVICE at $DATE on $HOST: $DESCRIPTION.
} }}

## CPU, memory and swap utilization
## Filesystem(s) usage
## Process monitoring
## Hard drive health and temperature using scripts
## Temperature
Create the file  as well as the  folder if necessary.

{{hc|/etc/monit.d/scripts/hdtemp.sh|
 #!/usr/bin/sh
 HDDTP=`/usr/bin/smartctl -A /dev/sd${1} | grep Temp.*Cels | awk -F " " '{printf "%d",$10}'`
 #echo $HDDTP # for debug only
 exit $HDDTP}}

In this example, the  script assumes your drive path is  where  is filled in by the letter at the end of the  declaration.  A similar method is used for the SMART health status in the next example.

## SMART health status
{{hc|/etc/monit.d/scripts/hdhealth.sh|
 #!/usr/bin/sh
 STATUS=`/usr/bin/smartctl -H /dev/sd${1} | grep overall-health | awk 'match($0,"result:"){print substr($0,RSTART+8,6)}'`
 if [ "$STATUS" = "PASSED" ]
 then
     # 1 implies PASSED
     TP=1
 else
     # 2 implies FAILED
     TP=2
 fi
 #echo $TP # for debug only
 exit $TP}}

## Alert recipients:  global or subsystem based
Alerts can be set globally, where a given user / email address is alerted for any  condition; or you can set an alert recipient for each type of check (eg network alerts go to recipient A; process alerts go to recipient B).  You can set as many global or subsystem recipients as you like, just make multiple declarations.

## Global alerts
Global alerts are set outside of any subsystem checks; for ease of reading they should be set in the same location as the mailserver declaration.
 SET ALERT email@domain

## Subsystem alerts
Subsystem alerts are set very similarly to global alerts except they lack the  flag.
 ALERT email@domain
