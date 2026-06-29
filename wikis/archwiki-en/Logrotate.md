# Logrotate

From https://github.com/logrotate/logrotate:

:The logrotate utility is designed to simplify the administration of log files on a system which generates a lot of log files. Logrotate allows for the automatic rotation compression, removal and mailing of log files. Logrotate can be set to handle a log file daily, weekly, monthly or when the log file gets to a certain size.

By default, logrotate's rotation consists of renaming existing log files with a numerical suffix, then recreating the original empty log file. For example,  is renamed . If  already exists from a previous rotation, it is first renamed . (The number of backlogs to keep can be configured.)

## Installation
Logrotate can be installed with the  package.

By default, logrotate runs daily using a systemd timer: .

## Configuration
The primary configuration file for logrotate which sets default parameters is ; additional application-specific configuration files are included from the  directory. Values set in application-specific configuration files override those same parameters in the primary configuration file. See  for configuration examples and a reference of available directives.

To verify if logrotate works correctly, run it in debug mode, in this mode it does nothing except producing debug output:

 $ logrotate --debug /etc/logrotate.conf

## Compressing logs
Logrotate can compress logs with a custom command like .

See  and  for more details.

## Usage
logrotate is usually run through the systemd service: .

To run logrotate manually:

 # logrotate /etc/logrotate.conf

To rotate a single log file:

 # logrotate /etc/logrotate.d/mylog

To simulate running your configuration file (dry run):

 # logrotate --debug /etc/logrotate.d/mylog

To force running rotations even when conditions are not met, run:

 # logrotate -vf /etc/logrotate.d/mylog

See  for more details.

## Troubleshooting
## exim log not rotated
If you have set the  variable in , you will get a message such as:

To fix this, add the user  to the group . Then change the group of the , usually , to  instead of the default .

## Check logrotate status
Logrotate rotations are usually logged to  (the  option allows you to specify another state file):

## Skipping log because parent directory has insecure permission
Configure which user and which group has to job  to be run with:

{{bc|
file-to-be-rotated {
    su user group
    rotate 4
}
}}
