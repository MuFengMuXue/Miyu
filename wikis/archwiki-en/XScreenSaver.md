# XScreenSaver

XScreenSaver is a screen saver and screen locker with graphical effects. The X Window System has functional screen-saving (in the power management sense) by default.

## Installation
Install the  package.

For an Arch Linux branded experience, install the  package.

## Configuration
Most options are configured on a user-by-user basis by running xscreensaver-settings. xscreensaver-settings writes the chosen configuration to , discarding any manual modifications to the file. Global options are defined in .

Since at least XScreenSaver 5.22, there is another way to edit XScreenSaver's user configuration, using X resources.

## Theming
Starting from version 6.0, XScreenSaver comes with several pre-installed themes. You can select a theme using xscreensaver-settings or by changing the  option ( in  or using X resources: ).

You can customize themes using X resources. The example below demonstrates changing some colors and fonts. If you are using a non-default theme, replace  with the name of your chosen theme in lower case, or use question mark () to affect all themes:

You can view a list of the available X resources in .

Do not forget to reload the resource file after changes.

## DPMS and blanking settings
XScreenSaver manages screen blanking and display energy saving (DPMS) independently of X itself and overrides it. To configure the timings for blanking, standby, display poweroff and such, use xscreensaver-demo or edit the configuration file manually, e.g. :

DPMS and screen blanking can be disabled by starting xscreensaver-demo and, for the Mode setting, choosing Disable Screen Saver.

## Usage
In the LXDE and LXQt environments, XScreenSaver is autostarted automatically if it is available - no further action is required.

For other environments, see Autostarting.

In KDE Plasma, screen saver and locker features are handled by ksmserver, which conflicts with XScreenSaver. To disable it, edit the  user unit:

Also open KDE System Settings and disable Power Management > Turn off screen.

Then logout and login again, and XScreenSaver should work properly now. See  for more information.

To immediately trigger xscreensaver, if it is running, and lock the screen, execute the following command:

 $ xscreensaver-command -lock

## Lock on suspend
XScreenSaver ships with a small utility named xscreensaver-systemd, which handles signals from systemd using D-Bus and automatically locks the screen on suspend and hibernate. It is started automatically with xscreensaver, no further action required. See  for more information.

## User switching from the lock screen
By default, XScreenSaver's New Login button in the lock screen will call  to switch users. Display managers other than GDM that support user switching require a different command.

As modifications in  are discarded by xscreensaver-settings,  is used in this section.

## LXDM
To use LXDM's switching mode:

 xscreensaver-auth.default.*.newLoginCommand: lxdm -c USER_SWITCH

## LightDM
To use LightDM's switching mode:

 xscreensaver-auth.default.*.newLoginCommand: dm-tool switch-to-greeter

## SDDM
SDDM does not support user switching. You can try to call the  method [https://github.com/sddm/sddm/issues/824 using dbus-send, but it may not work properly.

## Tips and tricks
## Disable during media playback
Starting from version 5.45, the xscreensaver-systemd utility implements the D-Bus ScreenSaver interface. It is started automatically with xscreensaver, so most applications should properly disable the screensaver without additional configuration. However, some applications do not support D-Bus or use another interfaces.

## mpv
By default mpv uses the X11 Screen Saver extension (XSS). It turns off the screensaver at startup and turns it on again on exit. The screensaver is always re-enabled when the player is paused. The option can be controlled in mpvs configuration file located in :

 stop-screensaver = "yes"

This is not supported on all video outputs or platforms. If you face some issues you might use a Lua script to manually disable the screensaver. Create a file at  with the following contents:

 local utils = require 'mp.utils'
 mp.add_periodic_timer(30, function()
     utils.subprocess({args={"xscreensaver-command", "-deactivate"}})
 end)

The above script will call  every 30 seconds.

## mplayer
Add the following to :

 heartbeat-cmd="xscreensaver-command -deactivate >&- 2>&- &"

## Kodi
Kodi has no native support to disable XScreenSaver (it uses its own screensaver). Install the  package as a workaround or try Kodi extension from https://sourceforge.net/projects/osscreensavermanager/.

## Browser HTML5 video
Most browsers (Chromium and Chromium-based spin-offs, Firefox, GNOME Web, Otter Browser etc.) support the D-Bus ScreenSaver interface and should disable the screensaver during HTML5 video playback.

## Other applications
If you are using applications that do not disable the screensaver, you can try a script named lightsonplus, which disables the screensaver when a fullscreen video is detected. Some applications (such as , Steam and others) are supported out of the box, you just need to enable their detection in the  script. If your application is unsupported but has a permanent window name, you can set it in the  variable.

## Animated wallpaper
One can run  in the background, just like a wallpaper. First, kill any process that is controlling the background (the root window).

Then, locate the desired XScreenSaver executable (typically in ) and run it with the  flag, for example:

 $ /usr/lib/xscreensaver/glslideshow -root &

## Troubleshooting
To log verbose debugging information, start xscreensaver with the  command line option. You can also add  to the  file to make it persistent.

To save the log to a file, you can set the path using the  option. Using this option also implies verbose output. (There is no equivalent option in  or X resources).

## "Authentication failed" when unlocking the screen
XScreenSaver relies on PAM for authentication when unlocking the screen. XScreenSaver might fail to authenticate when its PAM drop-in is misconfigured. As a potential fix, create  if it does not exist and replace the file content with the following:

or possible, if you have faillock configured. compare to /etc/pam.d/login

Kill and restart the  daemon for the changes to take effect.
