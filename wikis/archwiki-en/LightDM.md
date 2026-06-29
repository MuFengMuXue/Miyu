# LightDM

LightDM is a cross-desktop display manager. Its key features are:

* Cross-desktop - supports different desktop technologies.
* Supports different display technologies (X, Mir, Wayland ...).
* Lightweight - low memory usage and high performance.
* Supports guest sessions.
* Supports remote login (incoming - XDMCP, VNC, outgoing - XDMCP, PAM).
* Comprehensive test suite.
* Low code complexity.

More details about LightDM's design can be found here.

## Installation
Install the  package.

Follow Display manager#Loading the display manager to start LightDM at boot.

## Greeter
You will probably want to install a greeter. A greeter is a GUI that prompts the user for credentials, lets the user select a session, and so on. It is possible to use LightDM without a greeter, but only if an automatic login is configured; otherwise you will need to install  and one of the greeter packages below.

GTK-based greeters:

*
*
*
*
*
*

Qt-based greeters:

*
*

Other greeters:

*
*

Themes for :

*
*

Themes for  and :

*

You can set the default greeter by changing the  section of the LightDM configuration file, like so:

One way to check which greeters are available is to list the files in the  directory; each  .desktop file represents an available greeter. In this example, the  and  greeters are available:

## Enabling LightDM
Make sure to enable  so LightDM will be started at boot; see also Display manager#Loading the display manager.

## Command line tool
LightDM offers a command line tool, , which can be used to lock the current seat, switch sessions, etc, which is useful with 'minimalist' window managers and for testing. To see a list of available commands, execute:

 $ dm-tool --help

## User switching
LightDM's dm-tool command can be used to allow multiple users to be logged in on separate ttys. The following will send a signal requesting that the current session be locked and then will initiate a switch to LightDM's greeter, allowing a new user to log in to the system.

 $ dm-tool switch-to-greeter

## Testing
First, install .

Then, run LightDM as an X application:

 $ lightdm --test-mode --debug

## Optional configuration and tweaks
LightDM can be configured by modifying its configuration file, .

Some greeters have their own configuration files. For example:

:  (or you can use the  gui).

:

## X session wrapper
If you are migrating from xinit, you will notice that the display is not launched by your shell. This is because, as opposed to your shell starting the display (and the display inheriting the environment of your shell), LightDM starts your display and does not source your shell. LightDM launches the display by running a wrapper script and that finally exec's your graphic environment. By default,  is run.

## Environment variables
The script checks and sources , ,   and  , in that order. If you are using a shell that does not source any of these files, you can create an   to do so. (In this example, the login shell is zsh)

If you have shell variables that are important for your display (such as Gtk or QT themes, GNUPG location, configuration overrides, etc.) this will let your graphic environment have access to your environment without having to be launched by your login shell.

## Keymap
The script runs Xkbmap with arguments provided in files , . If those files are not found, it runs xmodmap with , . If using xkbmap, the files are parsed using cat. The following example works

Otherwise, the session inherits the system default mapping of X11. This mapping can be defined in the xorg configuration files, either manually or with . See Xorg/Keyboard configuration#Setting keyboard layout.

## Multiple keyboard layouts in lightdm-gtk-greeter
To enable users switch between pre-defined keyboard layouts on the log-in screen enable the drop-down menu and configure the layouts. Either use the  gui or edit the configuration file directly:

Use localectl to set multiple layouts, e.g. de and its “variant” neo with the latter as primary:

 # localectl --no-convert set-x11-keymap de,de pc105 neo,

Note the trailing comma which implies a blank variant for the second de.

## Changing background images/colors
You can set the background to a hex color or an image. Some greeters offer more robust background options like background selection from the login screen, random backgrounds, etc.

## GTK greeter
You can use the  gui.

Users wishing to customize the wallpaper on the greeter screen need to edit  and define the  variable under the  section. For example:

GTK3 themes can be specified with the  variable in the  section. The icon and cursor theme can be set in the same way, as shown in the following example:

## HiDPI or 4K configuration
Using lightdm-gtk-greeter out of the box in a HiDPI or 4K monitor, will render very small text and dialog boxes, it is possible to force a DPI setting like this:

In this case "192" means twice the 96 DPI setting of the screen, which is equivalent to the 2X Scale setting in other graphic environments. The value can be obtained with  in Xorg, for example.

## Webkit2 greeter
The  allows you to choose a background image directly on the login screen. It also offers an option to display a random image each time it starts if you use the Material theme. By default, images are sourced from . You can change the background images directory by editing . For example:

## Slick Greeter
Use the  GUI

## Changing your avatar
First, make sure the  package is installed, then set it up as follows, replacing  with the desired user's login name.

* Create the file  using a 96x96 PNG image file. Different image file formats are possible too, e.g., JPEG.
* Alternatively, create the image file as  and skip the next step if the defaults already point to the user home directory path
* Edit or create the account settings file , and add the lines

 Icon=/var/lib/AccountsService/icons/username.png

The filename here should point to the icon created in the first step, so adjust the filename extension if necessary.

## Sources of Arch-centric 64x64 icons
The  package contains some nice examples that install to  and that can be copied to  as follows:

 # find /usr/share/archlinux/icons -name "*64*" -exec cp {} /usr/share/icons/hicolor/64x64/devices \;

After copying, the  package can be removed.

## Enabling autologin
Edit the LightDM configuration file and ensure these lines are uncommented and correctly configured:

You must be part of the  group to be able to login automatically without entering your password:

 # groupadd -r autologin
 # gpasswd -a username autologin

LightDM logs in using the session specified in the  of the user getting logged in automatically. To override this file, specify  in :

The list of valid session names can be found by listing  for X's sessions and  for Wayland's.

## Enabling interactive passwordless login
LightDM goes through PAM so you must configure the lightdm configuration of PAM:

You must then also be part of the  group and the  group to be able to login interactively without entering your password:

 # groupadd -r nopasswdlogin
 # groupadd -r autologin
 # gpasswd -a username nopasswdlogin
 # gpasswd -a username autologin

To create a new user account that logs in automatically and additionally able to login again without a password the user can be created with supplementary membership of both groups, e.g.:

 # useradd -mG autologin,nopasswdlogin username

## Enabling guest sessions
To enable guest sessions in LightDM (without changing your system configuration) you need at least two things:

# a guest-account-script: defaults to  and accepts two commands:
#* add (to create a temporary guest system account and returns the user name of the created account)
#* remove account name(to delete the corresponding account)
# an autologin group to which the created guest account must be added (cf. )

There are two AUR packages that enable guest sessions in lightdm:

*  which provides the (largely unmodified) upstream guest-session script as well as  itself.
*  which provides only a minimal version of the script.

## Hiding system and services users
To prevent system users from showing-up in the login, install the optional dependency , or add the user names to  under . The first option has the advantage of not needing to update the list when more users are added or removed.

## Migrating from SLiM
Move the contents of xinitrc to xprofile, removing the call to start the window manager or desktop environment.

## Login using ~/.xinitrc
See Display manager#Run ~/.xinitrc as a session.

## NumLock on by default
Install the  package and then edit :

## Default session
Lightdm, like other DMs, stores the last-selected xsession in . See Display manager#Session configuration for more info.

## Adjusting the login window's position
## GTK greeter
Users need to edit  and enter a value for the  variable. It accepts  and  values, either absolute (in pixels) or relative (in percent). Each value can also have an additional anchor location for the window, ,  and  separated from the value by a comma.

Example:

 position=200,start 50%,center

## VNC Server
Lightdm can also be used to connect to via VNC. Make sure to install  on the server side and optionally as your VNC client on the client PC.

Setup an authentication password on the server as root:

 # vncpasswd /etc/vncpasswd

Edit the LightDM configuration file as shown below. Note that  configures the VNC to only listen to connections from localhost. This is used to only allow connections via SSH and port forwarding. On the SSH client, make sure that you use  for the tunnel destination; using  or  is not reliable on dual stack network connections. If you want to allow insecure connections you can disable this setting.

Now open an SSH tunnel and connect to localhost as described in TigerVNC#On the client.

## Lock the screen using light-locker
 is a simple screen locker using LightDM to authenticate the user. Once installed and running, you can lock your session via:

 $ light-locker-command -l

This requires  to be started at the beginning of your session. By default, this is enabled through XDG Autostart. See Autostarting for more options.

## Multiple-monitor setup
Sometimes LightDM does not set the monitor resolution correctly on a multiple-monitor setup. The following Xorg configuration works with two monitors: a large primary screen on the left side, and a secondary smaller screen to its right. The order can be reversed and tweaked.

This makes the  tweaks from  redundant.

## Troubleshooting
## Autologin does not work
Ensure  in  contain the correct values. Trailing whitespace will cause errors.

If autologin fails with a blank screen or if the login screen immediately returns, you may need to set .

You can also install  for this special purpose.

## Viewing current configuration
To view effective configuration, run:

 $ lightdm --show-config

This will show current settings, with the configuration files these settings were read from.

## LightDM not starting and screen flashing
If you encounter consistent screen flashing and ultimately no LightDM on boot, ensure that you have defined the greeter correctly in LightDM's configuration file. And if you have correctly defined the GTK greeter, make sure the  (default: ) exists and contains at least one .desktop file.

The same error can happen on lightdm startup if the last used session is not available anymore (eg. you last used gnome and then removed the gnome-session package): the easiest workaround is to temporarily restore the removed package. Another solution might be:

 # dbus-send --system --type=method_call --print-reply --dest=org.freedesktop.Accounts /org/freedesktop/Accounts/User1000 org.freedesktop.Accounts.User.SetXSession string:xfce

This example sets the session "xfce" as default for the user 1000.

## Wrong locale displayed
In case of your locale not being displayed correctly in Lightdm add your locale to :

 LANG=pt_PT.utf8

Alternatively if you want LightDM and its greeters to be in a language other than your set system locale, you can use the  option in a drop-in file.

## Missing icons with GTK greeter
If you are using  as a greeter and it shows placeholder images as icons, make sure valid icon themes and themes are installed and configured. Check the following file:

## LightDM freezes on login attempt
You may find that after entering the correct username and password and attempting to log in, LightDM freezes and you are unable to continue to the desktop. To fix the issue, reinstall the  package. See [https://bbs.archlinux.org/viewtopic.php?id=179031 this forum thread.

## LightDM displaying in wrong monitor
If you are using multiple monitors, LightDM may display in the wrong one (e.g. if your primary monitor is on the right). To force the LightDM login screen to display on a specific monitor, edit  and change the display-setup-script parameter like this:

Replace HDMI-1 with your real monitor ID, which you can find from xrandr command output.

Alternatively, if you are using the GTK greeter, you can edit  and add the active-monitor parameter like this:

Replace 0 with the desired display number.

## LightDM does not appear or monitor only displays TTY output
It may happen that your system boots so fast that LightDM service is started before your graphics drivers are properly loaded. If this is your case, you will want to add the following to your  file:

This setting will tell LightDM to wait until graphics devices are ready before spawning greeters/autostarting sessions on them.

With newer versions of LightDM, this is now the default setting.  As a consequence, on some hardware, your graphics drivers may not be properly detected and LightDM may never attempt to launch a greeter--even after the system has stabilized after boot.  If this occurs, setting this to false will disable the check and force LightDM to launch a greeter regardless.

## LightDM is running with low FPS on Intel Graphics
See Intel graphics#AccelMethod.

## PulseAudio not starting automatically
See PulseAudio#Running.

## Long pause before LightDM shows up when home is encrypted
Some LightDM themes try to access the user avatar located in HOME. If your HOME is encrypted, LightDM cannot access it and hangs. To prevent this from happening, you can either:

* Set your avatar as explained in #Changing your avatar
* for  only:  in

## Boot hangs on "[  OK  ] Reached target Graphical Interface."
There is a possibility that user and group lookups fail if you modified . That happens when  group: includes  without setting  in

## Wayland session not working with duplicate GNOME entries in greeter
Some greeters ( for example) do not support two sessions with the same name To check for duplicate entries:

 $ ls -1 /usr/share/wayland-sessions /usr/share/xsessions

Rename the duplicate entry in . For example:

 # mv /usr/share/xsessions/gnome.desktop /usr/share/xsessions/gnome.desktop.disabled

## Login always segfaults on first attempt
Set a hostname as described in Network configuration#Set the hostname. See also .

## Infinite login loop
If you get stuck in loop in which you type your correct username and password but the screen goes black and then you return to the login prompt after every attempt, running  (or the stuck user's problematic ) may fix the issue.

Another reason for this may be that you tried to recreate your "lightdm.conf" from scratch and your version is missing this line:

 session-wrapper=/etc/lightdm/Xsession

In that case, lightdm tries to use "lightdm-session" as the session-wrapper which does not exist on Arch Linux.

If your lightdm.conf file contains the intended session-wrapper but the lightdm logs indicate that the default session wrapper is being used instead, ensure that your lightdm.conf file is available during startup. For example, you may have created a symlink to a file in your home directory, but your home directory is not being mounted before the LightDM service started. In such cases LightDM will fall back to the default session wrapper.

## Input devices do not work in Wayland sessions
When starting a Wayland session, input devices may sometimes not work unless disconnecting and reconnecting the physical connection. See [https://github.com/canonical/lightdm/issues/63 LightDM issue 63.

A workaround is to delay the startup of Wayland compositors by adding  to . See archlinux/packaging/packages/lightdm!4 for a proposed workaround for the Arch package.
