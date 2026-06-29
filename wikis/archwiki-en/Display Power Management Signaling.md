# Display Power Management Signaling

VESA Display Power Management Signaling (DPMS) enables power saving behaviour of monitors when the computer is not in use. The time of inactivity before the monitor enters into a given saving power level—standby, suspend or off—can be set as described in .

## Linux console
To alter the terminal, use the setterm command. Its syntax (where 0 disables):

 $ setterm --blank $ setterm --powersave [on|vsync|hsync|powerdown|off
 $ setterm --powerdown Some commands just write the terminal sequences to the current terminal device, whether that be in screen, a remote ssh terminal, console mode, serial consoles, etc.

To see the escape codes used, pipe the output as follows:

 $ setterm --powerdown 2>&1 | exec cat -v 2>&1 | sed "s/\\^\\[/\\\\033/g"

To modify a specific terminal, redirect the escape codes to it (with write permission):

 $ setterm --powerdown 0 >> /dev/tty3

## Xorg
## Configuration
To fully disable DPMS and screen blanking on the X Window System, create configuration files:

If you simply want to adjust the delays, change the duration (in minutes):

## Runtime settings
It is possible to turn off your monitor with the xset command which is provided by the  package.

Examples:

{| class="wikitable"
! Command
! Description
|-
|
| Disable screen saver blanking
|-
|
| Change blank time to 1 hour
|-
|
| Turn off DPMS
|-
|
| Disable DPMS and prevent screen from blanking
|-
|
| Turn off screen immediately
|-
|
| Standby screen
|-
|
| Suspend screen
|}

To query the current settings:

See  for all available commands.
