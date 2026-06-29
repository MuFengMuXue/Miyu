# Dropbox

Dropbox is a file sharing system with a GNU/Linux client. Use it to transparently sync files across computers and architectures. Simply drop files into your  folder, and they will automatically sync to your centralized repository.

## Installation
## AUR
 can be installed. As a last resort, the Dropbox website has instructions for a headless install via command line.

# After installing the package, you can start Dropbox from your application menu or run  from the command-line. The client icon will appear in the system tray.
# A pop-up will notify you that Dropbox is running from an unsupported location. Click on Don't ask again since you know that you have installed it from AUR rather than from the official homepage.
# Eventually a pop-up will ask you to log in to your Dropbox account or create a new account. Enter your credentials.
# After some time you will see a "Welcome to Dropbox" pop-up, which will give you the opportunity to view a short tour of Dropbox.
# Press the "Finish and go to My Dropbox".

## Required/optional packages
Before launching  for the first time, it is mandatory to have  and optionally have  installed. Otherwise, the program is unable to sign the binaries, verify the signatures and show dropbox in the system tray, when it is started the next time. For some reason,  has not marked these packages as a required/optional dependencies but it is still such.

## Optional packages
{| class="wikitable"
|command-line interface
|
|-
|GNOME/Files integration
|
|-
|Nemo integration
|
|-
|Thunar integration
|
|-
|Dolphin integration
|
|-
|Caja integration
|
|}

Note that in order to access the GUI and the settings, the only way is via a tray icon. You need an X panel with a system tray or a standalone system tray application for that.

## Prevent automatic updates
Since at least version 2.4.6 (see comments around 2013-11-06 on AUR), Dropbox has had an auto-update capability which downloads a new binary to the  folder.  The service then attempts to hand over control to this binary and dies, causing systemd to re-start the service, generating a conflict and an endless loop of log-filling, CPU-eating misery.

A workaround is to prevent Dropbox from downloading the automatic update by creating the  folder and making it read-only:

 $ rm -rf ~/.dropbox-dist
 $ install -dm0 ~/.dropbox-dist

This appears to be necessary for modern Dropbox clients to operate successfully from systemd on arch.

Also see the relevant Dropbox forum post.

## Autostart
In the Dropbox preferences, under the "General" tab there should be a "Start Dropbox on system startup" checkbox. Try checking this box and seeing if Dropbox starts automatically.

If that does not work, uncheck the box and use one of the following methods instead:

## Autostart with your WM/DE
For KDE users, no further steps are required, as KDE saves running applications when logging out and restarts them automatically. Similarly for Xfce users, Dropbox will be restarted automatically next time you login since the  file has been placed in .

For Cinnamon users, it is recommended to start Dropbox client by configuring Startup Applications with a little delay (Cinnamon issue #4396). Starting Dropbox with systemd works, running in background, but there is no icon on systray due to some Cinnamon bugs (#481, #2846).

If that does not work, you can start the Dropbox sync client along with your window manager by adding  to your xinitrc (or , depending on your setup).

## Autostart on boot with systemd
To have Dropbox automatically start when your system boots, simply enable the systemd service, passing your username as the instance identifier. The service unit to be enabled takes the format .

By default, running the service does not give you an icon in the system tray because it does not know which X display to use. If you want to have tray support, use a drop-in file for the provided service. Both  and  need to be set correctly for the icon to appear.  will be replaced with the instance name of the service, in this case :

Note that with the above edit Dropbox will fail to start unless an X session is launched.

## Autostart on login with systemd
To have Dropbox automatically start when you log in, simply enable the user service.

If you want Dropbox to appear in your system tray, you will need to edit the user unit so that it knows which X display the system tray is in. Both  and  need to be set correctly for the icon to appear,  will need to be replaced with your username on the system:

Note that with the above edit Dropbox will fail to start unless an X session is launched.

## Accessing the files without installing a sync client
If all you need is basic access to the files in your Dropbox, you can use the web interface at https://www.dropbox.com/ to upload and download files to your Dropbox. This can be a viable alternative to running a Dropbox daemon and mirroring all the files on your own machine.

The  package provides a command-line interface to many cloud storage services including Dropbox.

## Encrypting your Dropbox files
If you want to store sensitive data in your Dropbox, you should encrypt it before doing so. Syncing to Dropbox is encrypted, but all files are (for the time being) stored on the server unencrypted just as you put them in your Dropbox.

* Dropbox works with TrueCrypt, and after you initially uploaded the TrueCrypt volume to Dropbox, performance is quite okay, because Dropbox has a working binary diff.
* Another possibility is to use EncFS, which has the advantage that all files are encrypted separately, i.e. you do not have to determine in advance the size of the content you want to encrypt and your encrypted directory grows and shrinks while you add/delete/modify files in it. You can also mount an encrypted volume at startup using the  option of  to avoid having to input the passphrase, but note that your encrypted files are not secure from someone who has direct access to your computer.
* A third option is to use gocryptfs. It is similar to EncFS, except that gocryptfs uses authenticated encryption, for protecting both confidentiality and integrity (tamper-resistance) of the data.

See also Data-at-rest encryption#Cloud-storage optimized.

## Setup EncFS with Dropbox
Follow the Wiki instructions to install EncFS.

Assuming you have set your Dropbox directory as :

Create a folder.  Files you want synced to Dropbox will go in here.

 $ mkdir ~/Private

Run the following and enter a password when asked:

 $ encfs ~/Dropbox/Encrypted ~/Private

Your secure folder is ready for use; creating any file inside  will automatically encrypt it into , which will then be synced to your cloud storage. This same command can be used if you wish to mount the EncFS folder again manually.

To mount your EncFS folder on every boot, follow the instructions in the EncFS wiki page.

## Multiple Dropbox instances
If you need to separate or distinguish your data, personal and work usage for example, you can subscribe to Dropbox with different email addresses and have their directories synced by different Dropbox instances running on a single machine.

The basic principle and general how-to are described in the Dropbox Wiki.

To summarize, you can setup new or additional instances with:

Once that is done, stop any Dropbox instance still running and start them like this:

Pay attention to use different  binaries. Even when setting a custom HOME value, the  or  wrappers allow only one instance and when started they will kill the one already running.

## Dropbox on laptops
Dropbox itself is pretty good at dealing with connectivity problems. If you have a laptop and roam between different network environments, Dropbox will have problems reconnecting if you do not restart it. Try one of the methods described below first, and if for some reason the problem remains, you may try one of these hackish solutions: [https://bbs.archlinux.org/viewtopic.php?pid=1012343#p1012343.

## Using netctl
For netctl, use  and  respectively in every network profile you use, or for example in  to start Dropbox automatically whenever profile on  is active. Add '|| true' to your command to make sure netctl will bring up your profile, although Dropbox fails to start.

 ExecUpPost="any other code; su -c 'DISPLAY=:0 /usr/bin/dropbox &' your_user || true"
 ExecDownPre="any other code; killall dropbox"

Obviously,  has to be edited and  can be omitted if you do not have any. The above will make sure that Dropbox is running only if there is a network profile active.

## Using NetworkManager
For NetworkManager, use its dispatcher feature.

Create the following file:

or, for the systemd alternative:

Do not forget to change scripts to be owned by root and to make them executable.

## Troubleshooting
## Dropbox asks for root on startup
This might be because it tries to fix permissions it does not accept. It can happen when you use btrfs on a partition that is used by Arch and Windows and forget to configure the Windows driver to use proper UID and GID. Check if that is the case:

 find ~/Dropbox -user nobody

Fix permissions and configure your driver properly. The asking for root modal should disappear automatically.

Note that this can appear if permissions on any file inside the Dropbox folder are incorrect, not only the Dropbox folder itself.

## Dropbox keeps saying Downloading files
But in fact now files are synced with your box. This problem is likely to appear when your Dropbox folder is located on a NTFS partition whose mount path contains spaces, or permissions are not set for that partition. See more in the forums. To resolve the problem, pay attention to your entry in . Avoid spaces in the mount path and set write permissions with the "default_permissions" option:

 UUID=01CD2ABB65E17DE0 /run/media/username/Windows ntfs-3g uid=username,gid=users,default_permissions 0 0

## Change the Dropbox location from the installation wizard
Some users experience the problem during setting-up Dropbox that they cannot select a Dropbox folder other than . In this case, when the window for changing the path is shown, hit , enter the location (e.g. /mnt/data/Dropbox) and click on the Choose or Open button.

## Context menu entries in file manager do not work
Several file managers such as Thunar, GNOME Files or its fork Nemo come with extensions that provide context menu entries for files and folders inside your Dropbox. Most of them will result in a browser action such as opening the file or folder in dropbox.com or sharing the link. If you experience these entries not working, then it is likely you have not set the  variable which Dropbox requires. See Environment variables for details.

## Connecting...
It may happen that Dropbox cannot connect successfully because it was loaded before an internet connection was established, as described in several threads (for many years). This can happen on wireless connections, or fast loading machines on wired networks. The best solution to this problem, for wired and wireless connections, is #Dropbox on laptops which will ensure that Dropbox is started only after the connection is established.

An alternative solution, for those not using netctl or NetworkManager, is to delay the startup of Dropbox:

*
* Prevent Dropbox from doing a standard autostart by unchecking Dropbox - Preferences - General - Start Dropbox on system startup. This removes .
* Edit  and replace  with . Tweak the timeout parameter, the value of  is a good start.

Another possibility is that Arch Linux by default updates to and installs dbus-broker, reverting to dbus-daemon-units will fix this, Dropbox seems to not support dbus-broker.

## Dropbox does not start - "This is usually because of a permission error"
## Check permissions
Make sure that you own Dropbox's directories before running the application. This includes

* - Dropbox's configuration directory
* - Dropbox's download directory (default)

You can ensure this by changing their owner with .

This error could also be caused by  being full.

## Re-linking your account
Dropbox's FAQ suggests that this error may be caused by misconfiguration and is fixed by (re)moving the current configuration folder

 # mv ~/.dropbox ~/.dropbox.old

and restarting Dropbox.

## Errors caused by running out of space
A common error that might happen is that there is no more available space on your  and  partitions. If this happens, Dropbox will crash on startup with the following error in its log:

 Exception: Not a valid FileCache file

A detailed story of such an occurrence can be found in the forums. Make sure there is enough space available before launching Dropbox.

Another case is when the root partition is full:

 OperationalError: database or disk is full

Check to see the available space on partitions with .

## Filesystem monitoring problem
If you have a lot of files to sync in your Dropbox folder, you might get the following error:

 Unable to monitor filesystem
 Please run: echo 100000 | sudo tee /proc/sys/fs/inotify/max_user_watches and restart Dropbox to correct the problem.

This can be fixed easily by adding

 fs.inotify.max_user_watches = 100000

to  and then reload the kernel parameters

 # sysctl --system

## Proxy settings
The easiest way to set Dropbox's proxy settings is by defining them manually in the Proxies tab of the Preferences window. Alternatively, you can also set it to 'Auto-detect' and then export your proxy server to the http_proxy env variable prior to starting Dropbox (HTTP_PROXY is also usable)

or

## Missing tray icon in GNOME
GNOME 3.26 removed support for tray icons in bug 785956 which will prevent the Dropbox icon from showing. To restore tray icons, an appropriate extension such as App Indicator needs to be installed.

## Missing tray icon in Cinnamon
Since Cinnamon is using XApp.StatusIcon (replacing the deprecated Gtk.StatusIcon in GNOME, see above), to pass information through dbus in multiple desktop environments, make sure you have the XApp Status Applet (xapp-status) installed and added to the panel, otherwise the Dropbox status icon might not display at all.

## Missing tray icon in wlroots (sway, river)
Starting Dropbox with  and  in the environment seems to do the trick. Tested with waybar (uses SNI).

## Unable to open the Sign In dialog
If attempting to open the system tray Sign In option fails, especially in i3-wm, it may be because the qt5 dependency is missing. Install .
