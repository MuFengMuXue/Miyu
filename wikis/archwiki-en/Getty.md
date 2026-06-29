# Getty

A getty is the generic name for a program which manages a terminal line and its connected terminal.  Its purpose is to protect the system from unauthorized access.  Generally, each getty process is started by systemd and manages a single terminal line.

## Installation
agetty is the default getty in Arch Linux, as part of the  package.

An alternative is .

## Tips and tricks
## Staircase effect
agetty modifies the TTY settings while waiting for a login so that the newlines are not translated to CR-LFs. This tends to cause a "staircase effect" for messages printed to the console.

It is entirely harmless, but in the event it persists once logged, you can fix this behavior with:

 $ stty onlcr

See this forums discussion on the subject.

## Add additional virtual consoles
Agetty manages virtual consoles and six of these virtual consoles are provided by default in Arch Linux. They are usually accessible by pressing  through .

Open the file  and set the option  to the number of virtual terminals that you want at boot.

If needed, it is possible to temporarily start a  service directly.

## Automatic login to virtual console
Configuration relies on systemd unit drop-in files to override the default parameters passed to agetty.

Configuration differs for virtual versus serial consoles. In most cases, you want to set up automatic login on a virtual console, (whose device name is , where  is a number). The configuration of automatic login for serial consoles will be slightly different. Device names of the serial consoles look like , where  is a number.

## Virtual console
Create a drop-in file for  with the following contents:

{{hc|/etc/systemd/system/getty@tty1.service.d/autologin.conf|2=
ExecStart=
ExecStart=-/sbin/agetty --noreset --noclear --autologin username - ${TERM}
}}

If you do not want full automatic login, but also do not want to type your username, see #Prompt only the password for a default user in virtual console login.

If you want to use a tty other than tty1, see systemd/FAQ#How do I change the default number of gettys?.

## Serial console
Create a drop-in file:

{{hc|/etc/systemd/system/serial-getty@ttyS0.service.d/autologin.conf|2=
[Service
ExecStart=
ExecStart=-/usr/bin/agetty --noreset --noclear --autologin username --keep-baud 115200,57600,38400,9600 - ${TERM}
}}

## Nspawn console
To configure auto-login for a systemd-nspawn container, override  by creating a drop-in file:

{{hc|/etc/systemd/system/console-getty.service.d/autologin.conf|2=
ExecStart=
ExecStart=-/usr/bin/agetty --noreset --noclear --autologin username --keep-baud 115200,57600,38400,9600 - ${TERM}
}}

If  method is used to access the container, also adjust the  template that manages  pseudo ttys:

{{hc|/etc/systemd/system/container-getty@.service.d/autologin.conf|2=
[Service
ExecStart=
ExecStart=-/usr/bin/agetty --noreset --noclear --autologin username - ${TERM}
}}

## Prompt only the password for a default user in virtual console login
Getty can be used to login from a virtual console with a default user, typing the password but without needing to insert the username. For instance, to prompt the password for  on :

{{hc|/etc/systemd/system/getty@tty1.service.d/skip-username.conf|2=
ExecStart=
ExecStart=-/usr/bin/agetty -o '-- username --skip-login --noreset --noclear - ${TERM}
}}

## Have boot messages stay on tty1
By default, Arch has the  service enabled. The service file already passes , which stops agetty from clearing the screen. However systemd clears the screen before starting it. To disable this behavior, create a drop-in file:

## Turn off display after timeout
When the system is used as a server but has a display connected, the display will be turned on forever. To turn off display after 5 minutes create a drop-in file. On any key press, display will turn back on.
