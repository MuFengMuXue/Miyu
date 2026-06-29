# SDDM

The Simple Desktop Display Manager (SDDM) is a display manager. It is the recommended display manager for the LXQt desktop environment.

From Wikipedia:Simple Desktop Display Manager:

:Simple Desktop Display Manager (SDDM) is a display manager (a graphical login program and session manager) for the X11 and Wayland windowing systems. SDDM was written from scratch in C++11 and supports theming via QML.

## Installation
Install the  package. Optionally, install  for the KConfig Module and  for enabling Qt5 theme support.

Follow Display manager#Loading the display manager to start SDDM at boot.

## Configuration
The default configuration file for SDDM can be found at . For any changes, create configuration file(s) in . See  for all options.

The   package (included in the  group) provides a GUI to configure SDDM in Plasma's system settings. There is also a Qt-based  available.

Everything should work out of the box, since Arch Linux uses systemd and SDDM defaults to using  for session management.

## Autologin
SDDM supports automatic login through its configuration file, for example:

This configuration causes a KDE Plasma session to be started for user  when the system is booted. Available session types can be found in  for X and in  for Wayland.

To autologin into KDE Plasma while simultaneously locking the session (e.g. to allow autostarted apps to warm up), see KDE#Lock screen.

## Passwordless login
It is possible to configure SDDM to allow logging into some accounts without a password. This differs from automatic login in that the user still has to choose which account to log into, and it differs from simply setting the account password to the empty string in that it only allows interactive users to log in (and not, for example, remote users logged in via SSH).

SDDM goes through PAM so you must configure the SDDM configuration of PAM:

In order to also allow unlocking the KDE Plasma lock screen without a password, also add the same line at the top of :

You must then also be part of the  group to be able to login interactively without entering your password:

 # groupadd -r nopasswdlogin
 # gpasswd -a username nopasswdlogin

## Unlock KDE Wallet automatically on login
See KDE Wallet#Unlock KDE Wallet automatically on login.

## Theme settings
Theme settings can be changed in the  section. If you use Plasma's system settings, themes may show previews.

Set to  for the default Plasma theme.

Some themes are available in the AUR, for example .

## Current theme
Set the current theme through the  value, e.g. .

## Editing themes
The default SDDM theme directory is . You can add your custom made themes to that directory under a separate subdirectory. Note that SDDM requires these subdirectory names to be the same as the theme names. Study the files installed to modify or create your own theme.

## Customizing a theme
To override settings in the  configuration file, create a custom  file in the same directory. For example, to change the theme's background:

## Testing (previewing) a theme
You can preview an SDDM theme if needed. This is especially helpful if you are not sure how the theme would look if selected or just edited a theme and want to see how it would look without logging out. You can run something like this:

 $ sddm-greeter-qt6 --test-mode --theme /usr/share/sddm/themes/breeze

This should open a new window for every monitor you have connected and show a preview of the theme.

## Mouse cursor
To set the mouse cursor theme, set  to your preferred cursor theme.

Valid Plasma mouse cursor theme names are ,  and .

In case SDDM defaults to the Adwaita theme on KDE setups (GNOME mouse cursor), one should set the  variable to the desired value in  manually.

## User icon (avatar)
SDDM reads the user icon (a.k.a. "avatar") as a PNG image from either  for each user, or the common location for all users specified by  in an SDDM configuration file. The configuration setting can be placed in either  directly, or, better, a file under  such as .

To use the  location option, place a PNG image for each user named  at the location specified by the  key in the configuration file. The default location for  is . You can change the default  location to suit your needs. Here is an example:

The other option is to put a PNG image named  at the root of your home directory. In this case, no changes to any SDDM configuration file is required. However, you need to make sure that  user can read the PNG image file(s) for the user icon(s).

To set proper permissions run:

 $ setfacl -m u:sddm:x ~/
 $ setfacl -m u:sddm:r ~/.face.icon

You can check permissions with:

 $ getfacl ~/
 $ getfacl ~/.face.icon

See SDDM README: No User Icon.

## Numlock
If you want to enforce numlock to be enabled, set  in the  section.

If SDDM is running under Wayland, the numlock setting currently does not work. You may need to change KWin settings to enable it, see this issue.

## Rotate display
See Xrandr#Configuration.

## DPI settings
Sometimes it is useful to set up the correct monitor's PPI settings on a "Display Manager" level.To do so you need to add to  the parameter  at the end of the string. For example:

## Enable HiDPI
Create the following file:

When using Wayland, the HiDPI scaling depends on the greeter used.[https://github.com/sddm/sddm/issues/1704 For instance, when using a Qt-based greeter such as Breeze, add the following configuration:

## Enable virtual keyboard
Install  (or another virtual keyboard).

Create the following file:

SDDM now displays a button in lower-left corner of login screen to open the virtual keyboard.

## Using a fingerprint reader
SDDM works with a fingerprint reader when using fprint. After installing fprint and adding fingerprint signatures, add the following to the top of :

In order to use either a password or a fingerprint, you can instead add the following to the top of the file:

Note that KWallet cannot be unlocked using a fingerprint reader (see KDE Wallet#Unlock KDE Wallet automatically on login), but the first line ensures that a password login will automatically unlock KWallet.

If you now press enter in the empty password field, the fingerprint reader should start working.

## Rootless
Traditionally, the X11 display server has been run with root privileges by default. This rootful mode allows X11 to have unrestricted access to system resources, which was necessary for its operation in environments where direct hardware access and management were common. However, with the increasing emphasis on security in modern computing environments, efforts have been made to transition to rootless modes, which is also why Wayland by default runs in rootless mode.

Starting unprivileged X11 (and Wayland) sessions has been supported since  0.20.0.To enable rootless mode: create a new configuration file under , name it something meaningful, and add the following to it, replacing  with  if necessary.

To confirm whether you are running in rootless mode check which user owns the compositor process (e.g. )

## Wayland
## KDE Plasma / KWin
Adding the following lines to your configuration file sets the Wayland compositor to KWin and enables the [https://wayland.app/protocols/wlr-layer-shell-unstable-v1 wlr_layer_shell Wayland protocol extension. This  requires  and  for SDDM themes using Qt6 and Qt5, respectively.

## Virtual keyboards
To enable virtual keyboard support (e.g. using  or ), append the  flag with the appropriate keyboard to the  command as shown below. Do not set the option  in the section , since this will cause the virtual keyboard to no longer be shown.

## Match Plasma display configuration
Changes to your display configuration made in a Plasma Wayland session (e.g. monitor layout, resolution, etc) will not persist to SDDM. To make them persist open Plasma's System Settings and navigate to Colors & Themes > Login Screen (SDDM) and click "Apply Plasma Settings...". You will need to have permission to perform this action.

The same can be achieved manually with the following:

To enable correct display & monitor handling in SDDM (scaling, monitor resolution, hz,...), you can copy or modify the appropriate configuration file from your home directory to the one of SDDM:

 # cp ~/.config/kwinoutputconfig.json /var/lib/sddm/.config/
 # chown sddm:sddm /var/lib/sddm/.config/kwinoutputconfig.json

To also enable correct input handling in SDDM (tap-to-click, touchscreen mapping,...), you can copy the appropriate configuration file from your home directory to the one of SDDM:

 # cp ~/.config/kcminputrc /var/lib/sddm/.config/
 # chown sddm:sddm /var/lib/sddm/.config/kcminputrc

## Troubleshooting
## Blank screen with cursor, but no greeter shows
Greeter crashes if there is no available disk space. Check your disk space with .

If disk space is not the issue, it may be due to a bug. Switch to another TTY, and then try  or to restart SDDM.

## Hangs after login
Try removing  and logging in again without rebooting. Rebooting without logging in creates the file again and the problem will persist.

## SDDM starts on tty1 instead of tty7
SDDM follows the systemd convention of starting the first graphical session on tty1.

Note that the config file still has the option  but is ignored since SDDM version 0.20: .

## One or more users do not show up on the greeter
By default, SDDM is configured to displays only users with a UID in the range of 1000 to 60513. If the UIDs of the desired users are outside this range then you will have to modify the range.

For example, for a UID of 501, set  and hide those with shells used by system users:

For users with a higher UIDs, set  to the appropriate value.

## User avatars do not show up on the greeter
User avatars are not shown on the greeter if the number of users exceeds  parameter or if avatars are not enabled at all as controlled by  parameter. To circumvent this add the following lines to your sddm configuration:

## SDDM loads only US keyboard layout
SDDM loads the keyboard layout specified in . You can generate this configuration file by  command. See Keyboard configuration in Xorg for more information.

An alternative way of setting the keyboard layout that will only set it in SDDM and not subsequent sessions is to invoke a setxkbmap command in the startup script of SDDM, located at . See Xorg/Keyboard configuration#Using setxkbmap for examples.

SDDM may also incorrectly display the layout as US but will immediately change to the correct layout after you start typing your password This seems to not be a bug in SDDM but in X server.[https://gitlab.freedesktop.org/xorg/xserver/-/issues/257

## Screen resolution is too low
Issue may be caused by HiDPI usage for monitors with corrupted EDID If you have enabled HiDPI, try to disable it.

If even the above fails, you can try setting your screen size in a Xorg configuration file:

## Long load time on autofs home directory
SDDM by default tries to display avatars of users by accessing  file. If your home directory is an autofs, for example if you use dm-crypt, this will make it wait for 60 seconds, until autofs reports that the directory cannot be mounted.

You can disable avatars by creating the following configuration file:

## X authority (aka MIT-MAGIC-COOKIE) file
SDDM uses a random fresh UUID for the auth file as described in details at [https://github.com/sddm/sddm/issues/622. So in order to find that file one may use a script:

 # find /var/run/sddm/ -type f

This may be needed if one needs to start x11vnc when there is no user logged in. For example:

 # x11vnc -display :0 -auth "$( find /var/run/sddm/ -type f )"

## Overlapping greeters on multiscreen setup
It happens that the X monitor layout is not setup correctly on multiscreen setup leading to overlapping greeters. To solve this add the following lines to order your sddm greeter layout from left to right:

## Login session appears on an unexpected display
It can happen that the SDDM login session appears on a different display than your primary display if multiple displays are connected. This problem can be annoying if the secondary display is rotated and the primary display is not. A simple fix to this problem is to use xrandr to configure the displays before the login session using Xsetup script. E.g. here xrandr reports that there are two connected displays where the secondary display (DP-2) is left of the primary display (DP-4).

 # xrandr | grep -w connected
 DP-2 connected 2160x3840+0+0 left (normal left inverted right x axis y axis) 597mm x 336mm
 DP-4 connected primary 3840x2160+2160+0 (normal left inverted right x axis y axis) 697mm x 392mm

The following Xsetup recreates the above setup for the login window:

## Black screen after logout with NVIDIA graphics card
One may encounter a complete black screen or with only cursor/display device logo on it after the logout of any user. This happens because  starts faster than the NVIDIA drivers. Consider using early KMS.

## Failing first password attempt results in text clearing itself after a few keystrokes on subsequent attempts
Use a different theme than the default.

## Screen out of sync on hybrid graphics with Wayland
If you set up SDDM with  compositor, one may encounter a screen out of sync when booting. If returning back to X11 works well, and you're using  drivers, chances are Wayland will work well by just replacing your current  drivers with . You can find more details about this issue at KDE Bug 483804.

## Some themes crash
Some SDDM themes do not specify  in  and SDDM starts with incompatible greeter (qt5 instead of qt6).

If you have set custom theme but on reboot there is default theme with error , you need to add  to .

## 12h or 24h clock
You could see an SDDM with a 12hr (am/pm) clock where you would expect a 24h clock. This is more likely for people who use a non-native language (like french people using US English) but still expecting units to be in their local format.

This behavior is not determined by SDDM settings, but in . Make sure you have an  set with the locale of choice. See Locale for details.
