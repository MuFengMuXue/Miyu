# SLiM

SLiM is an acronym for Simple Login Manager. Lightweight and easily configurable, SLiM requires minimal dependencies, and none from  the GNOME or KDE desktop environments. It therefore contributes towards a lightweight system for users that also like to use lightweight desktops such as Xfce, Openbox, and Fluxbox.

## Installation
Install the  package.

Follow Display manager#Loading the display manager to start SLiM at boot.

## Configuration
SLiM can automatically detect installed desktop environments and window managers through the use of  in . Those upgrading from a version before 1.3.6-2 must amend  and xinitrc, accordingly. See below.

## Enabling SLiM
Enable the SLiM service . This assumes a previously enabled display manager was disabled first. Otherwise, change the default target.

## Environments
To configure SLiM 1.3.6-2 (or later) to load an environment, edit both  and .

First, edit :
If you only use a single environment, you can hash out . This will disable automatic detection of installed environments:

 # Set directory that contains the xsessions.
 # slim reads xsession from this directory, and be able to select.
 # sessiondir            /usr/share/xsessions/

If you wish to automatically detect installed desktop environments, leave the line un-commented.

Second, edit xinitrc:

## Set default username
SLiM can be configured to automatically set a desired username, which will therefore already be completed. The password field will also already be focused by default. Change the following line in :

 # default_user        simone

Uncomment this line, and change "simone" to the username of choice:

 default_user        your username

## Enable Autologin
Edit  to uncomment the  command and replace   with :

 auto_login          yes

## Theming
Install the  package. The  packages contains several different themes (slimthemes.png). Look in the directory of  to see the themes available. Enter the theme name on the  line in :

 #current_theme       default
 current_theme       archlinux-simplyblack

You can preview a theme while Xorg is running with:

 $ slim -p /usr/share/slim/themes/''''

To close, type "exit" in the Login line and press Enter.

Additional theme packages can be found in the AUR. See the theme documentation for how to customize your theme or make your own. SLiM does not support alternative theme directories, so it is recommended to create a package for your custom theme so that pacman is aware of it.

## Custom background
SLiM is hard-coded to load  or  (in that order) from your theme directory. Simply overwrite the appropriate file

 # cp /path/to/new_background.jpg /usr/share/slim/themes/''''/background.jpg

## Dual screen setup
You can customize the slim theme in  to turn these percents values. The box itself is 450 pixels by 250 pixels:

 input_panel_x           50%
 input_panel_y           50%

into pixels values:

 # These settings set the "archlinux-simplyblack" panel in the center of a 1440x900 screen
 input_panel_x           495
 input_panel_y           325

 # These settings set the "archlinux-retro" panel in the center of a 1680x1050 screen
 input_panel_x           615
 input_panel_y           400

If your theme has a background picture, you should use the background_style setting (stretch, tile, center or color) to get it correctly displayed.

## Tips and tricks
## Changing the cursor
After installing, edit  and uncomment the line:

 cursor   left_ptr

This will give you a normal arrow instead. This setting is forwarded to . You can look up the possible cursor names or in .

To change the cursor theme being used at the login screen, see Cursor themes#The default cursor theme.

## Match SLiM and Desktop Wallpaper
To share a wallpaper between SLiM and your desktop, rename the used theme background, then create a link from your desktop wallpaper file to the default SLiM theme:

 # mv /usr/share/slim/themes/default/background.jpg{,.bck}
 # ln -s /path/to/mywallpaper.jpg /usr/share/slim/themes/default/background.jpg

## Shutdown, reboot, suspend, exit, launch terminal from SLiM
You may shutdown, reboot, suspend, exit or even launch a terminal from the SLiM login screen. To do so, use the values in the username field, and the root password in the password field:

* To launch a terminal, enter console as the username (defaults to xterm which must be installed separately... edit  to change terminal preference)
* For shutdown, enter halt as the username
* For reboot, enter reboot as the username
* To exit to bash, enter exit as the username
* For suspend, enter suspend as the username. Suspend is disabled by default, edit  as root to uncomment the  line and, if necessary, modify the suspend command itself (by e.g. changing  to ).

## Power-off error with Splashy
If you use Splashy and SLiM, sometimes you cannot power-off or reboot from menu in GNOME, Xfce, LXDE or others. Check your  and ; set the  same as .

## Power-off tray icon fails
If your power off tray icon fails, it could be due to not having root privileges. To start a tray icon with root privileges, be sure to have SLiM start the program. Edit  as follows:

 sessionstart_cmd 	/path/to/tray/icon/program &

## Login information with SLiM
By default, SLiM fails to log logins to utmp and wtmp which causes who, last, etc. to misreport login information. To fix this edit your  as follows:

 sessionstart_cmd    /usr/bin/sessreg -a -l $DISPLAY %user
 sessionstop_cmd     /usr/bin/sessreg -d -l $DISPLAY %user

## Custom SLiM Login Commands
You can also use the sessionstart_cmd/sessionstop_cmd in  to log specific infomation, such as the session, user, or theme used by slim:

 sessionstop_cmd /usr/bin/logger -i -t ASKAPACHE "(sessionstop_cmd: u:%user s:%session t:%theme)"
 sessionstart_cmd /usr/bin/logger -i -t ASKAPACHE "(sessionstart_cmd: u:%user s:%session t:%theme)"

Or if you want to play a song when slim loads (and you have the beep program installed)

 sessionstart_cmd /usr/bin/beep -f 659 -l 460 -n -f 784 -l 340 -n -f 659 -l 230 -n -f 659 -l 110

## GNOME Keyring
See GNOME/Keyring#Using the keyring to use GNOME Keyring in a custom session.

## Setting DPI with SLiM
The Xorg server generally picks up the DPI but if it does not you can specify it to SLiM. If you set the DPI with the argument  in  it will not work with SLiM. To fix this change your  from:

 xserver_arguments   -nolisten tcp vt07

to

 xserver_arguments   -nolisten tcp vt07 -dpi 96

## Use a random theme
Use the  variable as a comma separated list to specify a set from which to choose. Selection is random.

## Move the whole session to another VT
If tty terminals 3-6 are not used and commented out (You may use screen and therefore only need one terminal), change  to move the X server:

 xserver_arguments -nolisten tcp vt07

Simply change the vt07 to for example vt03 as no agetty is started there.

## Automatically mount your encrypted /home on login
To automatically mount an encrypted partition on user login with SLiM, configure pam_mount as follows:

## Change Keyboard Layout
Edit , find the following section, add the two bolded lines, and replace dvorak with your preferred keymap:

 Section  "InputClass"
           Identifier "evdev keyboard catchall"
           MatchIsKeyboard "on"
           MatchDevicePath "/dev/input/event*"
           Driver "evdev"

           # Keyboard layouts
           Option "XkbLayout" "dvorak"
 EndSection

## Screen Lock
Slim includes slimlock, a screen lock feature. To use it, just run slimlock.

Slimlock reads some configuration from  and its own configuration file .

To prevent VT switching whilst locked, set tty_lock to 1 in . This also requires that that you have write access to  and that slimlock has the  capability. One way to achieve this is set slimlock to suid root:

 # chmod +4000 /usr/bin/slimlock
 # chown root: /usr/bin/slimlock

An alternative is to setcap and permit your uid to write to .

 # setcap cap_sys_tty_config+ep /usr/bin/slimlock
 # chmod o+rw /dev/console

You can use  to lock the screen automatically:

 $ xss-lock -- /usr/bin/slimlock &

## Known issues
## Shutdown or Reboot Stalled
There is a bug or known issue with the combination of SLiM, Xfce and systemd that does not let the system to properly shutdown and systemd waits for the SLiM service to end, but eventually is terminated.

To accelerate the shutdown process these lines might help when editing :

 ExecStart=/usr/bin/slim -nodaemon
 Restart=on-failure
 TimeoutStopSec=5s
 IgnoreSIGPIPE=no
 ExecStop=/bin/kill -TERM -${MAINPID}

See .

## Identification problem
If your password contains non-ASCII characters (é, è, ç, à, etc.) and the locale of your system is in Unicode ( for example), you will not be able to log in to your session with the package from the official repository (bugs found on Debian, [https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=532060 bug#532060 and on NixOS, bug#29802).

A fixed version available on AUR brings Unicode support and solves this problem: .

## Crashes with 30-bit-colour X
When the Screen section of  contains , Slim immediately crashes in _XPutPixel32() libX11 function called from Image::createPixmap().
