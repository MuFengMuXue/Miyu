# Redshift

From the Redshift project web page:

:Redshift adjusts the color temperature of your screen according to your surroundings. This may help your eyes hurt less if you are working in front of the screen at night. This program is inspired by the closed-source application f.lux.

## Installation
Install the  package. Alternatively, install the  package, for a version with minimal dependencies.

## Front ends
The redshift-gtk command comes with the  package and provides a system tray icon for controlling Redshift. See optional dependencies.

Alternatives are  or .

## Usage
Redshift will at least need your location to start (unless  is used), meaning the latitude and longitude of your location. Redshift employs several routines for obtaining your location. If none of them works (e.g. none of the used helper programs is installed), you need to enter your location manually.

## Quick start
To just get it up and running with a basic setup, issue:

 $ redshift -l LATITUDE:LONGITUDE

where  is the latitude and  is the longitude of your location.

To instantly adjust the color temperature of your screen use:

 $ redshift -P -O TEMPERATURE

where  is the desired color temperature (between  and ).

## Autostart
There are several options to have Redshift automatically started:

* By right-clicking the system tray icon and selecting Autostart when redshift-gtk or plasma5-applets-redshift-control is already launched.
* By placing a Redshift desktop entry in  or by adding  to your window manager or desktop environment's autostarting method.
* By using the user units provided:  and . Activate only one of them depending on whether or not you want the system tray icon.

## Toggle
Redshift will continously update the color temperature at regular intervals. One shot mode can be selected if you only want to do one adjustment. The color adjustments done by Redshift can be temporarily toggled on and off by sending it the USR1 signal:

 $ pkill -USR1 redshift

## Configuration
Redshift reads the configuration file  if it exists. However, Redshift does not create that configuration file, so you may want to create it manually. See [https://raw.githubusercontent.com/jonls/redshift/master/redshift.conf.sample redshift.conf.sample.

## Specify location manually
Redshift calculates the sunrise and sunset times based on geographic coordinates. It can be specified manually by using the  location-provider, e.g. for Paris:

## Automatic location based on GeoClue
Redshift uses the  location-provider by default. It needs a GeoClue agent running in the background. It is supposed to work without further configuration, but if you experience problems, see #Unable to connect to GeoClue.

## Automatic location based on GPSD
You can also use  to automatically determine your GPS location and use it as an input for Redshift. Create the following script and pass  and  to :

 #!/bin/bash
 date
 #gpsdata=$( gpspipe -w -n 10 |   grep -m 1 lon )
 gpsdata=$( gpspipe -w | grep -m 1 TPV )
 lat=$( echo "$gpsdata"  | jsawk 'return this.lat' )
 lon=$( echo "$gpsdata"  | jsawk 'return this.lon' )
 alt=$( echo "$gpsdata"  | jsawk 'return this.alt' )
 dt=$( echo "$gpsdata" | jsawk 'return this.time' )
 echo "$dt"
 echo "You are here: $lat, $lon at $alt"

For more information, see this forums thread.

## Use real screen brightness
Redshift has a brightness adjustment setting, but it does not work the way most people might expect. In fact it is a fake brightness adjustment obtained by manipulating the gamma ramps, which means that it does not reduce the backlight of the screen. Changing screen backlight is possible with redshift hooks and , but there are some limitations and you may have to find another method of controlling the backlight depending on your hardware.

You need to create a file in  and make it executable. You can use and edit the following example:

{{hc|~/.config/redshift/hooks/brightness.sh|output=
#!/bin/sh
# Set brightness via xbrightness when redshift status changes

# Set brightness values for each status.
# Range from 1 to 100 is valid
brightness_day=85
brightness_transition=50
brightness_night=30
# Set fps for smoooooth transition
fps=1000
# Adjust this grep to filter only the backlights you want to adjust
backlights=($(xbacklight -list  grep ddcci*))

set_brightness() {
	for backlight in "${backlights[@}"
	do
		xbacklight -set $1 -fps $fps -ctrl $backlight &
	done
}

if [ "$1" = period-changed ]; then
	case $3 in
		night)
			set_brightness $brightness_night
			;;
		transition)
			set_brightness $brightness_transition
			;;
		daytime)
			set_brightness $brightness_day
			;;
	esac
fi
}}

Make it executable and restart the  to apply changes.

Check the service status as it should not contain the following message:

 redshiftNo outputs have backlight property

## Troubleshooting
## Unable to connect to GeoClue
If running  and you are getting:
 Unable to obtain GeoClue client path: Timeout was reached.

Then make sure that a GeoClue agent is running. GNOME Shell [https://gitlab.gnome.org/GNOME/gnome-shell/-/blob/main/js/ui/status/location.js provides an agent itself. For other desktop environments, a demo agent () is autostarted. You can check if GeoClue works properly by checking the output of the  command.

If you are using a desktop environment that does not support XDG Autostart, then you have to start the demo agent manually, or you can create a systemd unit file with the following config:

Then start/enable the  user unit.

## Screen 1 could not be found
Locate configuration-file "redshift.conf" in your distribution and change "screen 1" to "screen 0".

## Left/right clicking the tray icon does not work
Install . See redshift issue 363 and .

## Redshift makes the screen quickly flicker between the set color value of the screen and the default color value
Make sure there are not multiple instances of redshift running.

## Redshift works fine when invoked as a command but fails when run as a systemd service
The systemd unit has a line in the  file that makes the service wait until the  unit is started by a display manager before the unit will invoke . If you do not use a display manager, edit the  user service and delete the  line. Run a daemon-reload and the service should initialize properly.

## Redshift-gtk service causes core-dumping
Refer to the previous problem and to === Redshift does not appear in system tray ===

If running the  command does not start in the system tray, but instead you get the following output

you will need to install .

## Redshift turns the screen green when resolution is over 1080p while using Nvidia drivers
This is a bug with the nvidia drivers. A fix for this is to make the following edit:

For more information, see [https://github.com/jonls/redshift/issues/587 redshift issue 587 and redshift issue 720.

## Redshift does not support hotkey for toggling
A workaround is to create a custom hotkey in your desktop environment calling the command .

For more information, see == See also ==

* [https://web.archive.org/web/20250123081224/https://jonls.dk/redshift Redshift website
* Redshift on GitHub
* Wikipedia:Redshift (software)
* Similar software: ,
