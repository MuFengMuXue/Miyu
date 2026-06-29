# Cron

From Wikipedia:

:cron is the time-based job scheduler in Unix-like computer operating systems. cron enables users to schedule jobs (commands or shell scripts) to run periodically at certain times, dates or intervals. It is commonly used to automate system maintenance or administration.

## Installation
There are many cron implementations, but none of them are installed by default as the base system uses systemd timers instead.

Packages available:

*
*
*
*

See Gentoo:Cron, which offers comparisons.

## Configuration
The cron daemon parses a configuration file called a . Each user on the system can maintain a separate crontab file to schedule commands individually. The root user's crontab is used to schedule system-wide tasks (though users may opt to use  or the  directory, depending on which cron implementation they choose).

## Activation and autostart
After installation, the daemon will not be enabled by default. The installed package likely provides a service, which can be controlled by systemctl. For example, cronie uses .

Check  and similar directories to see which jobs are present. Activating a cron service will trigger all of them.

## Basic commands
Crontabs should never be edited directly; instead, you should use the  program to work with your crontabs.

To view your crontabs:

 $ crontab -l

To edit your crontabs:

 $ crontab -e

To remove all of your crontabs:

 $ crontab -r

If you have a saved crontab and would like to completely overwrite your old crontab:

 $ crontab saved_crontab_filename

To overwrite a crontab from the command line (Wikipedia:stdin):

 $ crontab -

To edit somebody else's crontab:

 # crontab -u username -e

This same format (appending  to a command) works for listing and deleting crontabs as well.

## Crontab format
The basic format for a crontab is a set of 6 space-separated values, in the following order:

* minute from 0 to 59.
* hour from 0 to 23.
* day_of_month from 1 to 31.
* month from 1 to 12.
* day_of_week from 0 to 6, with 0 denoting Sunday.
* command is the process to run.

To fine-tune your schedule you may also use one of the following symbols:

{| class="wikitable"
! Symbol !! Description
|-
|  || Wildcard, specifies every possible time interval
|-
|  || List multiple values separated by a comma.
|-
|  || Specify a range between two numbers, separated by a hyphen
|-
|  || Specify a periodicity/frequency using a slash
|-
|}

For example, the line:

 */5 9-16 * 1-5,9-12 1-5 ~/bin/i_love_cron.sh

will execute the script  at five minute intervals from 9 AM to 4:55 PM on weekdays except during the months of June, July, and August.

In addition, crontab has some special keywords:

{| class="wikitable"
! Keyword !! Description
|-
|  || at startup
|-
|  || once a year
|-
|  || identical to
|-
|  || once a month
|-
|  || once a week
|-
|  || once a day
|-
|  || identical to
|-
|  || once an hour
|-
|}

For example:

 @reboot ~/bin/i_love_cron.sh

will execute the script  at startup.

## Cronie
The  file includes the list of users not allowed to use crontab, without this file, only users listed in  can use it.

{{Note|
* Cronie uses  to carry out scripts in the different directories. The filenames should not include any dot (.) since  in its default mode will silently ignore them (see ). The names must consist only of upper and lower-case letters, digits, underscores and minus-hyphens. If you want to be absolutely sure what scripts are being run you can test and validate using e.g. .
* The output of  might show a message such as . However, this can be safely ignored since cronie does not require one.
* Cronie is particular about the permissions for . None of the tasks in {{ic|/etc/cron.d/{hourly,weekly,daily} ... etc}} will be run (including the anacron launcher) if  is damaged or has improper permissions.  can show if you have any such issues.
}}

## Dcron
Dcron follows the common crontab format, but allows adding the  and  tags.

See  for further information and configuration examples.

## Fcron
When replacing  with fcron be aware the spool directory is  and the  command is used instead of crontab to edit the user crontabs. These crontabs are stored in a binary format with the text version next to them as foo.orig in the spool directory. Any scripts which manually edit user crontabs may need to be adjusted due to this difference in behavior.

A quick scriptlet which may aide in converting traditional user crontabs to fcron format:

{{bc|
cd /var/spool/cron && (
 for ctab in *; do
  fcrontab ${ctab} -u ${ctab}
 done
)
}}

See also the forum thread.

## Examples
The entry:

 01 * * * * /bin/echo "Hello, world!"

runs the command  on the first minute of every hour of every day of every month (i.e. at 12:01, 1:01, 2:01, etc.).

Similarly:

 */5 * * jan mon-fri /bin/echo "Hello, world!"

runs the same job every five minutes on weekdays during the month of January (i.e. at 12:00, 12:05, 12:10, etc.).

The line:

 */5 9-16 * 1-5,9-12 1-5 /home/user/bin/i_love_cron.sh

will execute the script  at five minute intervals from 9 AM to 5 PM (excluding 5 PM itself) every weekday (Mon-Fri) of every month except during the summer (June, July, and August).

Here are some self-documenting examples of cron tasks:

## Tips and tricks
## Default editor
To use an alternate default editor, define the  environment variable in a shell initialization script as described in Environment variables.

As a regular user,  will need to be used instead of  for the environment variable to be pulled correctly:

 $ su -c "crontab -e"

To have an alias to this  is required to carry the arbitrary string because  launches in a new shell:

 alias scron="su -c $(printf "%q " "crontab -e")"

## Handling errors of jobs
cron registers the output from stdout and stderr and attempts to send it as email to the user's spools via the  command. Cronie disables mail output if  is not found. In order for mail to be written to a user's spool, there must be an smtp daemon running on the system, e.g. . Otherwise, you can install a package that provides the sendmail command, and configure it to send mail to a remote mail exchanger. You can also log the messages by using the  option and writing a custom script.

# Edit the  unit.
# Install , msmtp, , sSMTP, or write a custom script.

## Example with sSMTP
sSMTP is a send-only sendmail emulator which delivers email from a local computer to an smtp server.  While there are currently no active maintainers, it is still by far the simplest way to transfer mail to a configured mailhub.  There are no daemons to run, and configuration can be as simple as editing 3 lines in a single configuration file (if your host is trusted to relay unauthenticated email through your mailhub).  sSMTP does not receive mail, expand aliases, or manage a queue.

Install , which creates a symbolic link from  to . You must then edit .  See sSMTP for details.  Creating a symbolic link to  insures that programs like S-nail (or any package which provides ) will just work without modification.

Restart  to insure that it detects that you now have a  installed.

## Example with msmtp
Install , which creates a symbolic link from  to . Restart  to make sure it detects the new  command. You must then provide a way for  to convert your username into an email address.

Add  line to your crontab:

 MAILFROM=your@email.com

Then either add  line to your crontab, like so:

 MAILTO=your@email.com

or create  and append this line:

 aliases /etc/aliases

and create :

 your_username: your@email.com
 # Optional:
 default: your@email.com

Then modify the configuration of cronie daemon by replacing the  command with:

 ExecStart=/usr/bin/crond -n -m '/usr/bin/msmtp -t'

## Example with esmtp
Install  and .

After installation configure the routing:

Procmail needs root privileges to work in delivery mode but it is not an issue if you are running the cronjobs as root anyway.

To test that everything works correctly, create a file  with  in it.

From the same directory run:

 $ sendmail user_name
 match for local action "local"

You can proceed to test it. First start . Then do:

 $ echo test | sendmail user

user can check their mail in with any reader able to handle mbox format, or just have a look at the file . If everything goes as expected, you can enable opensmtpd for future boots.

This approach has the advantage of not sending local cron notifications to a remote server. On the downside, you need a new daemon running.

## Long cron job
Suppose this program is invoked by cron :

 #!/bin/sh
 echo "I had a recoverable error!"
 sleep 1h

What happens is this:

# Cron runs the script.
# As soon as cron sees some output, it runs your MTA, and provides it with the headers. It leaves the pipe open, because the job has not finished and there might be more output.
# The MTA opens the connection to postfix and leaves that connection open while it waits for the rest of the body.
# Postfix closes the idle connection after less than an hour and you get an error like this :

To solve this problem you can use the command chronic or sponge from . From their respective man page:

; : chronic runs a command, and arranges for its standard out and standard error to only be displayed if the command fails (exits nonzero or crashes). If the command succeeds, any extraneous output will be hidden.
; : sponge reads standard input and writes it out to the specified file. Unlike a shell redirect, sponge soaks up all its input before opening the output file… If no output file is specified, sponge outputs to stdout.

Chronic too buffers the command output before opening its standard output.

## Running X.org server-based applications
Cron does not run under the Xorg server therefore it cannot know the environmental variable necessary to be able to start an X.org server application so they will have to be defined. One can use a program like  to do it:

 17 02 * ... /usr/bin/xuserrun /usr/bin/xclock

Or they can be defined manually ( will give the current DISPLAY value):

 17 02 * ... env DISPLAY=:0 /usr/bin/xclock

If running notify-send for desktop notifications in cron, notify-send is sending values to dbus. So it needs to tell dbus to connect to the right bus.
The address can be found by examining DBUS_SESSION_BUS_ADDRESS environment variable and setting it to the same value. Therefore:

 17 02 * ... env DBUS_SESSION_BUS_ADDRESS=your-address notify-send 'Foo bar'

If done through say SSH, permission will need be given:

 # xhost +si:localuser:$(whoami)

## Asynchronous job processing
If you regularly turn off your computer but do not want to miss jobs, there are some solutions.

## Cronie
 comes with anacron included. The configuration file is . Information on the format can be found in the . Running  will test  for validity.

## Dcron
Vanilla  supports asynchronous job processing. Just put it with @hourly, @daily, @weekly or @monthly with a jobname, like this:

 @hourly         ID=greatest_ever_job      echo "This job is very useful."

## Cronwhip
 is a script to automatically run missed cron jobs; it works with the former default cron implementation, dcron. See also the forum thread.

## Fcron
Like anacron,  assumes the computer is not always running and, unlike anacron, it can schedule events at intervals shorter than a single day which may be useful for systems which suspend/hibernate regularly (such as a laptop). Like cronwhip, fcron can run jobs that should have been run during the computer's downtime.

## Ensuring exclusivity
If you run potentially long-running jobs (e.g., a backup might all of a sudden run for a long time, because of many changes or a particular slow network connection), then flock (from ) can ensure that the cron job will not start a second time:

 5,35 * * * * /usr/bin/flock -n /tmp/lock.backup /root/make-backup.sh
