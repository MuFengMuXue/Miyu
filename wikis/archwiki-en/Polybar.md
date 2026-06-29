# Polybar

polybar is a fast and easy-to-use tool for creating status bars. It aims to be easily customizable, utilising many modules which enable a wide range of (editable) functionality, such as displaying workspaces, the date, or system volume. Polybar is especially useful for window managers that have a limited or non-existent status bar, such as awesome or i3. Polybar can also be used with desktop environments like Plasma.

## Installation
Install the  package.

## Configuration
Copy the configuration example from  to . By default, polybar will load the config file from , , or  depending on which it finds first.

## Running Polybar
See  for a list of options to run it manually. However, you will probably want to run Polybar with your window manager's bootstrap routine. See #Running with a window manager.

## Sample configuration
A very basic polybar configuration may look like this:

It defines a bar named  with a module called .

Polybar will also install the default configuration with many preconfigured modules in .

## Running with a window manager
Create an executable file containing the startup logic, for example :

This script will mean that restarting your window manager will also restart Polybar.

To execute this script by your window manager on startup, see Autostarting#On window manager startup.

## Multiple monitors
If you wish to have your bar duplicated across multiple monitors, you need to launch multiple bars.

Add something like this to your startup script:

Then configure Polybar to read the monitor from the environment:
{{hc|config.ini|2=
monitor = ${env:MONITOR:}
[..
}}

## Troubleshooting
## ThinkPad battery display
On Lenovo ThinkPad X200 and related models, the battery level display frequently stops after having resumed from system suspension (such as re-opening the lid), due to a weird firmware on the models.Restarting polybar allows it to pick up on the battery again. This can be automated by a systemd unit that runs  when resuming from suspension.

Ensure polybar is configured to use :

Enable the  unit.
