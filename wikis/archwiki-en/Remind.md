# Remind

Remind is a sophisticated calendar and alarm program.

## Installation
Install the  package.

## Configuration
After installation, the user can define reminders in remind script files (.rem). A good place for these files could be .

Here are some example reminders that could be in the remind script:

The last particular day of a month is given by subtracting 7 days from the first day of the next month. The  symbol tells remind to start reminding that number of days ahead.

See also  man page for detailed information about configuring remind.

## Include
A reminder script can also include any number of external scripts. For example, a user might want to have a separate file for birthday reminders and a separate file for holidays. This can be done like so:

 include ~/.config/remind/birthdays.rem
 include ~/.config/remind/holidays.rem

## Usage
The simplest thing one can do with remind, is to check for reminders. Do this by passing a reminder file to remind:

 remind ~/.config/remind/reminders.rem

This will output a list of reminders that it is scheduled to tell the user about.

To output a text based calendar, use the  option:

 remind -c1 ~/.config/remind/reminders.rem

This will output a text calendar for the current month. To print months in advance, replace  with the number of months to print.

## Postscript/pdf calendars
It is also possible to create calendars in a postscript format.

 remind -c2 -p ~/.config/remind/reminders.rem | rem2ps > calendar.ps

The  option makes remind print output suitable for rem2ps. rem2ps by default prints the output to standard output, so it must be redirected to a file so it can be opened by a program like evince.

Postscript files can be converted with . Ps2pdf is provided by .
