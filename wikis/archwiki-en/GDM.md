# GDM

From GDM - GNOME Display Manager: "The GNOME Display Manager (GDM) is a program that manages graphical display servers and handles graphical user logins."

Display managers provide X Window System and Wayland users with a graphical login prompt.

## Installation
GDM can be installed with the  package, and is installed as part of the  group.

Follow Display manager#Loading the display manager to start GDM at boot.

## Configuration
## Login screen background image
Firstly, you need to extract the existing GNOME Shell theme to a directory in your home directory. You can do this using the following script:

{{hc|extractgst.sh|2=
#!/bin/sh
gst=/usr/share/gnome-shell/gnome-shell-theme.gresource
workdir=${HOME}/shell-theme

for r in `gresource list $gst`; do
	r=${r#\/org\/gnome\/shell/}
	if [ ! -d $workdir/${r%/*} ]; then
	  mkdir -p $workdir/${r%/*}
	fi
done

for r in `gresource list $gst`; do
        gresource extract $gst $r >$workdir/${r#\/org\/gnome\/shell/}
done
}}

Navigate to the created directory. You should find that the theme files have been extracted to it (under a theme subfolder). Now copy your preferred background image to this directory.

Next, you need to create a file under the theme directory with the following content (the list below is for Gnome 47, just in case verify that the contents of the theme subfolder match the list here, including the background image):

Replace filename with the filename of your background image or remove the line to use a hex color value instead.

Now, open the  and  files and change the  definition as follows:

 #lockDialogGroup {
   background: url("filename");
   background-size: widthpx heightpx;
   background-repeat: no-repeat;
 }

Set  to the resolution that GDM uses; this might not necessarily be the resolution of the image. For a list of display resolutions, see Display resolution.

Again, set filename to be the name of the background image, filename should be within quotes in the CSS. background-size can also be set to auto if you want the image scaled to fill.

If using multiple monitors, the image ends up spanning across the monitors, so it might be better to use an SVG file for the background.

If you only want to change the background color, adjust the  definition as follows:

 #lockDialogGroup {
   background-color: #color;
 }

where color is the new hex-encoded background color.

Next, compile the theme using the following command:

 $ glib-compile-resources gnome-shell-theme.gresource.xml

Then, copy the resulting  file to the  directory (keep a backup of the original).

 # cp /usr/share/gnome-shell/gnome-shell-theme.gresource /usr/share/gnome-shell/gnome-shell-theme-original.gresource
 # cp ./gnome-shell-theme.gresource /usr/share/gnome-shell

Finally, logout and you should find that gdm is using your preferred background image (you might need to restart gdm if the changes are not applied immediately).

If a subsequent update resets the gnome-shell-theme.gresource file, simply repeat the above steps, verifying that the contents of the XML match the extracted file list.

For more information, please see the following forum thread. A shell script to automate the above steps is available on DimaZirix's github repository.

## dconf configuration
Some GDM settings are stored in a dconf database. They can be configured either by adding keyfiles to the  directory and then recompiling the GDM database by running  as root or by logging into the GDM user on the system and changing the setting directly using the gsettings command line tool. Note that for the former approach, a GDM profile file is required—this must be created manually as it is no longer shipped upstream, see below:

For the latter approach, you can log into the GDM user with the command below:

 # machinectl shell gdm@ /bin/bash

## Login screen logo
Create the following keyfile:

Then recompile the GDM database.

Alternatively, execute the following as the GDM user to change the logo:

 dbus-launch gsettings set org.gnome.login-screen logo /path/to/logo.png

To disable the logo, you can set the value to an empty string:

 [gdm$ dbus-launch gsettings set org.gnome.login-screen logo ''

## Changing the cursor theme
GDM disregards GNOME cursor theme settings and it also ignores the cursor theme set according to the XDG specification. To change the cursor theme used in GDM, create the following keyfile:

Then recompile the GDM database. Alternatively, execute the following as the GDM user temporarily and change the cursor theme:

 dbus-launch gsettings set org.gnome.desktop.interface cursor-theme theme-name

## Changing the icon theme
The same methods can be used to change the icon theme. Create the following keyfile:

Then, recompile the GDM database. Alternatively, execute the following as the GDM user temporarily and change the icon theme:

 [gdm$ dbus-launch gsettings set org.gnome.desktop.interface icon-theme theme-name

## Larger font for log-in screen
Click on the accessibility icon at the top right of the screen (a white circle with the silhouette of a person in the centre) and check the Large Text option.

To set a specific scaling factor, create the following keyfile:

Then recompile the GDM database. Alternatively, execute the following as the GDM user temporarily and change the font:

 dbus-launch gsettings set org.gnome.desktop.interface text-scaling-factor 1.25

## Turning off the sound
This tweak disables the audible feedback heard when the system volume is adjusted (via keyboard) on the login screen.

Create the following keyfile:

Then recompile the GDM database. Alternatively execute the following as the GDM user temporarily and turn off the sound:

 [gdm$ dbus-launch gsettings set org.gnome.desktop.sound event-sounds 'false'

## Configure power button behavior
Create the following keyfile:

Then recompile the GDM database. Alternatively, execute the following as the GDM user temporarily and configure the behavior:

 dbus-launch gsettings set org.gnome.settings-daemon.plugins.power power-button-action action

where action can be one of ,  or .

## Enabling tap-to-click
Tap-to-click is disabled in GDM (and GNOME) by default, but you can easily enable it with a dconf setting.

To enable tap-to-click, create the following keyfile:

Then recompile the GDM database. Alternatively, execute the following as the GDM user temporarily and enable the action:

 [gdm$ dbus-launch gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click 'true'

## Disable/Enable Accessibility Menu
To disable or enable the Accessibility Menu, create the following keyfile:

Then recompile the GDM database. Alternatively, execute the following as the GDM user temporarily and change the status:

 dbus-launch gsettings set org.gnome.desktop.interface toolkit-accessibility boolean

The menu is disabled when the key is , enabled when it is .

## Enable Night Light on GDM
To enable Night Light on GDM, run

## Keyboard layout
GDM requires the  parameter to be set in ; without it it defaults to a standard  (qwerty) layout, i.e it will not honor the value set in .

One generally applicable way to do so is to use : see Keyboard configuration in Xorg#Setting keyboard layout for details.

## Change the language
The system language will be applied to GDM. If a system has multiple users, it is possible to set a language for GDM different to the system language. In this case, firstly ensure that  is installed. Then, start gnome-control-center and choose Region & Language. In the header bar, check the Login Screen toggle button. Finally, click on Language and choose your language from the list. You will be prompted for your root password. Note that the Login Screen button will not be visible in the header bar unless multiple users are present on the system [https://bugzilla.gnome.org/show_bug.cgi?id=741500.

## Users and login
## Automatic login
To enable automatic login with GDM, add the following to  (replace  with your own):

or for an automatic login with a delay:

You can set the session used for automatic login (replace  with desired session):

## Passwordless login
If you want to bypass the password prompt in GDM then simply add the following line on the first line of :

 auth sufficient pam_succeed_if.so user ingroup nopasswdlogin

Then, add the group  to your system. See User group for group descriptions and group management commands.

Now, add your user to the  group and you will only have to click on your username to login.

## Disable fingerprint login
When using a fingerprint to login, it will not unlock the keychain, so you will still be prompted for the keychain password. You might want to disallow login and keep the fingerprint to unlock your session. To do this, just disable fingerprint for the GDM user.

Execute the following as the GDM user temporarily and change this setting:
 dbus-launch gsettings set org.gnome.login-screen enable-fingerprint-authentication false

## Passwordless shutdown for multiple sessions
GDM uses polkit and logind to gain permissions for shutdown. You can shutdown the system when multiple users are logged in by setting:

You can find all available logind options (e.g. reboot-multiple-sessions) in .

## Enable root login in GDM
It is not advised to login as root, but if necessary you can edit  and add the following line before the line :

The file should look something like this:

You should be able to login as root after restarting GDM.

## Hide user from login list
The users for the gdm user list are gathered by [https://www.freedesktop.org/wiki/Software/AccountsService/ AccountsService. It will automatically hide system users (UID  Remote Desktop > Remote Login'' in Gnome Settings app.

## Via CLI
To display current status and credentials, the following command can be used:

 # grdctl --system status --show-credentials

To set credentials:

 # grdctl --system rdp set-credentials rdp_login rdp_password

To generate new TLS key and certificate:

 # winpr-makecert3 -rdp -path /etc/gnome-remote-desktop -n rdp-tls

If  part is omitted, hostname will be used as the name instead.

To set TLS key and certificate:

 # grdctl --system rdp set-tls-key /etc/gnome-remote-desktop/rdp-tls.key
 # grdctl --system rdp set-tls-cert /etc/gnome-remote-desktop/rdp-tls.crt

Finally, to enable Remote Login:

 # grdctl --system rdp enable

## Setup default monitor settings
Some desktop environments store display settings in , based on which xrandr commands are generated. GDM has a file serving a similar purpose located at  (This is the global mutter configuration and will impact new GNOME session too).

If you have your monitors setup as you like (resolution, refresh rate, orientation, scaling, primary and so on) in  and want GDM to honor those settings:

 # cp /home/user/.config/monitors.xml /etc/xdg/monitors.xml

To automatically re-configure the monitor setup on each boot, use a drop-in file for :

The relevant parts of  for screen rotation and scaling are:

       ...
       2
       ...

         right
         no

       ...

Changes will take effect on logout. This is necessary because GDM does not respect .

## Configure X server access permission
You can use the  command to configure X server access permissions.

For instance, to grant GDM the right to access the X server, use the following command:

## Troubleshooting
## GDM greeter does not show user list after upgrade to GNOME 50
After upgrading to GDM 50, the greeter may fail to show the user selection list entirely, launching only as the  user with no option to select or switch to any regular user account. This can happen when  is empty or missing the required entries.

The file is not owned by any package ( returns ), so it will not be created or repaired automatically during updates.

Verify the file contains the following:
 user-db:user
 system-db:gdm
 file-db:/usr/share/gdm/greeter-dconf-defaults

If the file is empty or missing these entries, populate it and run:
 # dconf update

Then restart GDM. Without this profile, gnome-shell does not launch in greeter mode and fails to display the user list.

## Wayland and the proprietary NVIDIA driver
To use Wayland in GDM with the NVIDIA driver, you must fulfill the three following conditions:

* enable DRM KMS,
* configure Wayland,
* follow NVIDIA/Tips and tricks#Preserve video memory after suspend.

If, instead of GDM, a black screen appears, try disabling integrated graphics in your computer's BIOS settings.

In some cases, GNOME fails to start and transfers control back to GDM, which in turn causes the login screen to reappear. You may try setting the following environment variable as suggested in BBS#2126478:

## Failure on logout
If GDM starts up properly on boot, but fails after repeated attempts on logout, try adding this line to the daemon section of :

 GdmXserverTimeout=60

## Rootless Xorg
See Xorg#Rootless Xorg.

## Use Xorg backend
The Wayland backend is used by default, and the Xorg backend is used only if the Wayland backend cannot be started. You may wish to use the Xorg backend instead if, for example:

* GDM crashes

To use the Xorg backend by default, uncomment the following line in :

 #WaylandEnable=false

## Incomplete removal of gdm
After removing , systemd may report the following:

 user 'gdm': directory '/var/lib/gdm' does not exist

To remove this warning, login as root and delete the primary user  and then delete the group :

Verify that  is successfully removed via  and  with root privileges. To round it off, you may want to double-check no unowned files for gdm remain.

## GDM auto-suspend (GNOME 3.28)
GDM uses a separate dconf database to control power management. To apply your user's power settings, copy them to GDM's dconf database:

 $ IFS=$'\n'; for x in $(sudo -u username gsettings list-recursively org.gnome.settings-daemon.plugins.power); do eval "sudo -u gdm dbus-launch gsettings set $x"; done; unset IFS

where  is your username.

To only disable auto-suspend on AC, run:

 dbus-launch gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'

(To also disable auto-suspend on battery, run the command with  instead of .)

Restart GDM to activate your changes.

For newer versions of GNOME (Tested on 49.1):
 # Create following files and any directories if they do not exist.
 $ cat /etc/dconf/profile/gdm
 user-db:user
 system-db:gdm
 file-db:/usr/share/gdm/greeter-dconf-defaults

 $ cat /etc/dconf/db/gdm.d/00-disable-suspend
 [org/gnome/settings-daemon/plugins/power
 sleep-inactive-ac-type='nothing'
 sleep-inactive-ac-timeout=0

 $ sudo dconf update
 $ sudo reboot

Supplementary forum links:
# https://bbs.archlinux.org/viewtopic.php?id=309828
# https://unix.stackexchange.com/a/746767

## GDM ignores Wayland and uses X.Org by default
Wayland requires Kernel Mode Setting (KMS) running in order to work, and on some machines the GDM process start earlier than KMS, resulting in GDM unable to see Wayland and working only with X.Org. This might result in messages like the following showing up in your log:

 gnome-shellFailed to open gpu '/dev/dri/card0': GDBus.Error:org.freedesktop.DBus.Error.AccessDenied: Operation not permitted
 gnome-shell[569: Failed to create backend: No GPUs found
 systemdorg.gnome.Shell@wayland.service: Failed with result 'protocol'.
 systemd[505: Failed to start GNOME Shell on Wayland.

Alternatively, the same issue may lead to GDM not appearing or monitor only displaying the TTY output.

You can solve this problem by starting KMS earlier. You may also wish to just verify that Wayland is enabled in the GDM config (see above).

## Black screen on AMD or Intel GPUs when an NVIDIA (e)GPU is present
At first, without an NVIDIA device, GDM starts and works normally on Wayland, but stops working once an NVIDIA eGPU is plugged in (or the  module is loaded for other reasons). A typical symptom of the problem is a black screen with a blinking cursor upon logouts and GDM restarts and the following message in GDM's logs (accessed by running  as root):

 Gdm: Child process - was already dead.

The solution is the same as #GDM ignores Wayland and uses X.Org by default: Prevent  from running upon  module loading.

Notice that GDM on Wayland will no longer work once  has run. This is because  has been written into , which overrides . To fix the situation without a reboot, remove  and then restart GDM.

## GDM cannot be enabled
See systemd/FAQ#Failure to enable unit due to preexisting symlink.
