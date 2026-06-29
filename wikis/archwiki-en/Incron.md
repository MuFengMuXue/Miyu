# Incron

incron is an "inotify cron" system. It consists of a daemon and a table manipulator. You can use it a similar way as the regular cron. The difference is that the inotify cron handles filesystem events rather than time periods.

## Installation
Install the  package.

## Activation and autostart
After installation, the daemon will not be enabled by default.  You can enable .

## Configuration
Incrontabs should never be edited directly; instead, users should use the incrontab program to work with their incrontabs.

## Using incrontab
To view their incrontabs, users should issue the command:

 $ incrontab -l

To edit their incrontabs, they should use:

 $ incrontab -e

To remove their incrontabs, they may use:

 $ incrontab -r

To reload incrond, use:

 $ incrontab -d

To edit another user's incrontab, isue the following command:

 # incrontab -u user -e

## Incrontab format
Each row in an incrontab file is a table that the dameon runs when an event happens to a certain directory or file.

The basic format for an incrontab is:

 path mask command

;path: the directory or file that incrond will monitor for changes.
;mask: the type of filesystem event that incrond will monitor for. This paramter can be seperated by commas.
;command: the command to be run after the specified filesystem event(s) occur.

## Mask types
incrontab uses mask types to specify which file system event to monitor for. For more options see

To trigger a command if a file is accessed or read:

 IN_ACCESS

To trigger a command if metadata of a file change (e.g. timestamps,  permissons):

 IN_ATTRIB

To trigger a command  if a file opened for writing is closed:

 IN_CLOSE_WRITE

To trigger a command if a file or directory not opened for writing is closed:

 IN_CLOSE_NOWRITE

To trigger a command if a file or directory is created in a watched directory:

 IN_CREATE

To trigger a command if a file or directory is deleted from a watched directory:

 IN_DELETE

To trigger a command if a watched file or directory is deleted (or moved to a different filesystem):

 IN_DELETE_SELF

To trigger a command if a file was modified:

 IN_MODIFY

To trigger a command if a watched file or directory is moved within the filesystem:

 IN_MOVE_SELF

To trigger a command if a file or directory is moved out of the watched directory:

 IN_MOVED_FROM

To trigger a command if a file or directory is moved to the watched directory:

 IN_MOVED_TO

To trigger a command if a watched file or directory is opened:

 IN_OPEN

## Custom Mask Types
Incrond provides additional custom event types to modify its monitoring behavior.

For instance, to pause monitoring an event until the current one is completely handled, add loopable=true to the event list, eg:

 IN_CLOSE,loopable=true

An event with the loopable event enabled will not fire again until the associated command exits.

See  for the complete list of custom mask types.
