# Talkd and the talk command

The "talk" command allows you to talk to other users on the same system. This was historically useful on UNIX systems, before the popularization of IRC and more recent instant messaging software. It can still be useful for some cases e.g. when multiple users log in via SSH to the same system.

## Installation
The simplest form of talking to other users only requires installing , which contains talk and talkd.

Then, start/enable  (the  will automatically be started at the first use of talk).

Alternatively, the talk daemon can be handled by , you would then start .

## Configuration
Allow write access in your terminal if needed:

 $ mesg y

If you use the xinetd service, configure the entry by editing  and setting .

Now reload .

## Usage
To test by talking to yourself, you might need to start a GNU Screen session to make yourself show up with w and who—you need to show up there or talk will not work.

To talk to someone the command is just

 $ talk username

Of course, you can talk to users on another system as well, and optionally specify to which tty you want to talk to:

 $ talk username@hostname tty

"tty" is of the form "ttyXX", or "pts/X".

If the message
 for invitation on caller's machine
keeps showing up when you are trying to "talk" on your local machine, "talkd" might not be running correctly.
Try manually start/enable  and .
