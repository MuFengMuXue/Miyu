# Acpid

acpid2 is a flexible and extensible daemon for delivering ACPI events. When an event occurs, it executes programs to handle the event. These events are triggered by certain actions, such as:

* Pressing special keys, including the Power/Sleep/Suspend button
* Closing a notebook lid
* (Un)Plugging an AC power adapter from a notebook
* (Un)Plugging phone jack etc.

## Installation
Install the  package. Then start/enable .

## Configuration
 comes with a number of predefined actions for triggered events, such as what should happen when you press the Power button on your machine. By default, these actions are defined in , which is executed after any ACPI events are detected (as determined by ).

## Determine the event
Unfortunately, not every computer labels ACPI events in the same way.  For example, the Sleep button may be identified on one machine as SLPB and on another as SBTN.

To determine how your buttons or  shortcuts are recognized, run the following command:

 # journalctl -f

Now press the Power button and/or Sleep button (e.g. ) on your machine. The result should look something this:

 logger: ACPI action undefined: PBTN
 logger: ACPI action undefined: SBTN

If that does not work, run:

 # acpi_listen

or with :

 $ netcat -U /var/run/acpid.socket

Then press the power button and you will see something like this:

 button/power PBTN 00000000 00000b31

The output of  is sent to  as $1, $2 , $3 & $4 parameters.
Example:

 $1 button/power
 $2 PBTN
 $3 00000000
 $4 00000b31

## Define event action
The following is a brief example of one such action. In this case, when the Sleep button is pressed, acpid runs the command  which should place the computer into a sleep (suspend) state:

 button/sleep)
     case "$2" in
         SLPB) echo -n mem >/sys/power/state ;;
         *)    logger "ACPI action undefined: $2" ;;
     esac
     ;;

The event may be different on different machines. For example if Sleep button is actually recognized as SBTN, rather than the SLPB label specified in the default . In order for Sleep function to work properly on this machine, we would need to replace SLPB) with SBTN).

Using this information as a base, you can easily customize the  file to execute a variety of commands depending on which event is triggered.  See the #Tips and tricks section below for other commonly used commands.

## Alternative configuration
By default, all ACPI events are passed through the  script. This is due to the ruleset outlined in :

 # Pass all events to our one handler script
 event=.*
 action=/etc/acpi/handler.sh %e

While this works just fine as it is, some users may prefer to define event rules and actions in their own self-contained scripts. The following is an example of how to use an individual event file and corresponding action script:

As root, create the following files:

Make the script executable, and reload the  to get acpid to recognize the changes to these files.

Using this method, it is easy to create any number of individual event/action scripts.

## Tips and tricks
## Example events
The following are examples of events that can be used in the  script. These examples should be modified so that they apply to your specific environment e.g. changing the event variable names interpreted by .

To set the laptop screen brightness when plugged in power or not (the numbers might need to be adjusted, see ):

 ac_adapter)
     case "$2" in
         AC*|AD*)
             case "$4" in
                 00000000)
                     echo -n 50 > /sys/class/backlight/acpi_video0/brightness
                     ;;
                 00000001)
                     echo -n 100 > /sys/class/backlight/acpi_video0/brightness
                     ;;
             esac

## Enabling volume control
Find out the acpi identity of the volume buttons (see above) and substitute it for the acpi events in the files below.

See also === Enabling backlight control ===

Similar to volume control, acpid enables control of your screen's backlight; to achieve this, write a handler, like this:

The event in acpi_listen should be something like:

 video/brightnessdown BRTDN 00000087 00000000
 video/brightnessup BRTUP 00000086 00000000

Connect them to ACPI events:

## Enabling Wi-Fi toggle
You can also create a simple wireless-power switch by pressing the WLAN button. Here's an example:

and its handler:

## Disabling ordinary key events
Since [https://sourceforge.net/p/acpid2/code/ci/b336c96e32c959ed3df15eaf5669f47ea589d977/ b336c96 acpid generates events for some ordinary key presses, such as arrow keys. This results in event/handler spam, visible in system logs or top. Events for these buttons can be dropped in the configuration file:

## Getting user name of the current display
To run commands depending on Xorg, defining the X display as well as the MIT magic cookie file (via XAUTHORITY) is required. The latter is a security credential providing read and write access to the X server, display, and any input devices (see ).

See for an example function when using xinitrc.

## Connect to acpid socket
In addition to rule files, acpid accepts connections on a UNIX domain socket, by default . User applications may connect to this socket.

Where  can be a script similar to .

## Disable keyboard and touchpad while laptop lid is closed under Wayland
This example uses [https://www.phoronix.com/news/Linux-5.11-Inhibited-Input inhibited property of input device drivers as a replacement for xinput which does not work under Wayland.
