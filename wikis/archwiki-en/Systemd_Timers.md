# Systemd/Timers

Timers are systemd unit files whose name ends in .timer that control .service files or events. Timers can be used as an alternative to cron (read #As a cron replacement). Timers have built-in support for calendar time events, monotonic time events, and can be run asynchronously.

## Timer units
Timers are systemd unit files with a suffix of .timer. Timers are like other unit configuration files and are loaded from the same paths but include a  section which defines when and how the timer activates. Timers are defined as one of two types:

* Realtime timers (a.k.a. wallclock timers) activate on a calendar event, the same way that cronjobs do. The option  is used to define them.
* Monotonic timers activate after a time span relative to a varying starting point. They stop if the computer is temporarily suspended or shut down. There are number of different monotonic timers but all have the form: . Common monotonic timers include  and .

For a full explanation of timer options, see the . The argument syntax for calendar events and time spans is defined in .

## Service units
For each .timer file, a matching .service file exists (e.g.  and ). The .timer file activates and controls the .service file. The .service does not require an  section as it is the timer units that are enabled. If necessary, it is possible to control a differently-named unit using the  option in the timer's  section.

## Management
To use a timer unit enable and start it like any other unit (remember to add the .timer suffix). To view all started timers, run:

## Examples
A service unit file can be scheduled with a timer out-of-the-box. The following examples schedule  to be run with a corresponding timer called .

## Monotonic timer
A timer which will start 15 minutes after boot and again every week while the system is running.

## Realtime timer
A timer which starts once a week (at 12:00am on Monday). When activated, it triggers the service immediately if it missed the last start time (option ), for example due to the system being powered off:

When more specific dates and times are required,  events uses the following format:

 DayOfWeek Year-Month-Day Hour:Minute:Second

An asterisk may be used to specify any value and commas may be used to list possible values. Two values separated by  indicate a contiguous range.

In the below example the service is run the first four days of each month at 12:00 PM, but only if that day is a Monday or a Tuesday.

 OnCalendar=Mon,Tue *-*-01..04 12:00:00

To run a service on the first Saturday of every month, use:

 OnCalendar=Sat *-*-1..7 18:00:00

When using the  part, at least one weekday has to be specified. If you want something to run every day at 4am, use:

 OnCalendar=*-*-* 4:00:00

To run a service at different times,  may be specified more than once. In the example below, the service runs at 22:30 on weekdays and at 20:00 on weekends.

 OnCalendar=Mon..Fri 22:30
 OnCalendar=Sat,Sun 20:00

You can also specify a timezone at the end of the directive (use  to list accepted values)

 OnCalendar=*-*-* 02:00:00 Europe/Paris

More information is available in .

## Transient timer units
One can use  to create transient .timer units. That is, one can set a command to run at a specified time without having a service file. For example the following command touches a file after 30 seconds:

 # systemd-run --on-active=30 /bin/touch /tmp/foo

One can also specify a pre-existing service file that does not have a timer file. For example, the following starts the systemd unit named  after 12.5 hours have elapsed:

 # systemd-run --on-active="12h 30m" --unit someunit.service

See  for more information and examples.

## As a cron replacement
Although cron is arguably the most well-known job scheduler, systemd timers can be an alternative.

## Benefits
The main benefits of using timers come from each job having its own systemd service. Some of these benefits are:

* Jobs can be easily started independently of their timers. This simplifies debugging.
* Each job can be configured to run in a specific environment (see ).
* Jobs can be attached to cgroups.
* Jobs can be set up to depend on other systemd units.
* Jobs are logged in the systemd journal for easy debugging.

## Caveats
Some things that are easy to do with cron are difficult to do with timer units alone:

* Creation: to set up a timed job with systemd you need to create two files and run  commands, compared to adding a single line to a crontab.
* Emails: there is no built-in equivalent to cron's  for sending emails on job failure. See systemd#Notifying with e-mail for an example of setting up a similar functionality using .

Also note that user timer units will only run during an active user login session by default. However, lingering can enable services to run at boot even when the user has no active login session.

## Using a crontab
Several of the caveats can be worked around by installing a package that parses a traditional crontab to configure the timers.  and  are two such packages. These can provide the missing  feature.

Also, like with crontabs, a unified view of all scheduled jobs can be obtained with . See #Management.

## Manually
Outside of migrating from an existing crontab, using the same periodicity as cron can be desired. To avoid the tedious task of creating a timer for each service to start periodically, use a template unit, for example:

Then one only needs to enable/start .

## Tips and tricks
## Handling "time to live"
Some software will track the time elapsed since they last ran, for example blocking the update of a database if the last download ended less than 24 hours ago.

By default, timers do not track when the task they launched has ended. To work around this, we can use :

## Desktop notifications
The  provides an automatic desktop notification that helps you notice when a systemd service is triggered by a timer and is running. The notification will automatically close when the service finishes.

This can be helpful for understanding why CPU usage is high or for preventing a shutdown when a backup service hasn't finished.

For more details and configuration options, visit https://gitlab.com/Zesko/systemd-timer-notify
