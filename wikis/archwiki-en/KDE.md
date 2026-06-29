# KDE

KDE is a software project currently comprising a desktop environment (KDE Plasma), applications (KDE Applications), and Qt add-on libraries (KDE Frameworks).

## Installation
## Plasma
Install the  meta-package or the  group. For differences between  and  reference Package group. Alternatively, for a more minimal Plasma installation, install the  package. Upstream KDE has package and setup recommendations to get a fully-featured Plasma session.

If you are an NVIDIA user, ensure the DRM kernel mode setting is enabled.

## Plasma Mobile
Install  and .

## KDE applications
To install the full set of KDE Applications, install the  meta-package or the  group. If you only want KDE applications for a certain category, like gaming or education, install the relevant dependency of . Note that installing applications alone will not install any version of Plasma.

## Unstable releases
See Official repositories#kde-unstable for beta releases.

## Starting Plasma
Starting from Plasma 6.4, the Wayland session has matured enough to become the default and preferred one: the X11 session is only available separately with the  packageThe Xorg session is still supported, but will be [https://blogs.kde.org/2025/11/26/going-all-in-on-a-wayland-future/ removed in Plasma 6.8. See Wayland Known Significant Issues and X11 Known Significant Issues for more information.

Plasma can be started either using a display manager, or from the console.

## Using a display manager
* Select Plasma (Wayland) to launch a new session in Wayland.
* Select Plasma (X11) to launch a new session in Xorg.
* Select Plasma Mobile (Wayland) to launch a new Plasma Mobile session in Wayland.

## From the console
* To start a Plasma on Wayland session from a console, run * To start Plasma with xinit/startx, append  and  to your  file or run directly in the console . If you want to start Xorg at login, please see Start X at login.

## Configuration
Most settings for KDE applications are stored in . However, configuring KDE is primarily done through the System Settings application. It can be started from a terminal by executing .

## Personalization
## Plasma desktop
## Display configuration
For configuring multiple displays, use the KDE System settings display module or the  tool.

## Themes
There are different types of KDE themes, varying by scope of what they modify:

* [https://store.kde.org/browse?cat=121 Global themes, comprehensive packages that can include Plasma themes, application styles, colors, fonts, icons, cursors, splash screens, SDDM themes, and Konsole color schemes. Global themes can be applied with the  command line tool.
* Plasma themes, modifying the look of Plasma panels and widgets. These often have a recommended accompanying Kvantum or Aurorae theme to complete the look.
* Application styles, modifying the look of programs.
* Application styles that use theme engines such as Kvantum, QtCurve [https://github.com/DexterMagnific/QSvgStyle QSvgStyle and [https://store.kde.org/p/1167275/ Aurorae.
* #Icon themes, providing icons for applications, files, and actions.

For easy system-wide installation and updating, some themes are available in both the official repositories and the AUR.

Global themes can also be installed through System Settings > Colors & Themes > Global Theme > Get New....

## GTK application appearance
The recommended theme for a pleasant appearance in GTK applications is , a GTK theme designed to mimic the appearance of Plasma's Breeze theme.
Install  (part of the  group), relogin and select  as the GTK theme in System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style....

In some themes, tooltips in GTK applications have white text on white backgrounds making it difficult to read. To change the colors in GTK2 applications, find the section for tooltips in the  file and change it. For GTK3 application two files need to be changed,  and .

Some GTK2 programs like  still look hardly usable due to invisible checkboxes with the Breeze or Adwaita skin in a Plasma session. To workaround this, install and select e.g. the Numix-Frost-Light skin of the  under System Settings > Colors & Themes > Application Style > Configure GNOME/GTK Application Style... > GTK theme. Numix-Frost-Light looks similar to Breeze.

## Faces
Plasma and SDDM will both use images found at  as users' avatars. To configure with a graphical interface, you can use System Settings > Users. The file corresponding to your username can be removed to restore the default avatar.

## Widgets
Plasmoids are widgets for Plasma desktop shell designed to enhance the functionality of desktop, they can be found on the AUR.

Plasmoid scripts can also be installed by right-clicking onto a panel or the desktop and choosing Enter Edit Mode > Add Widgets... > Get New Widgets... > Download New Plasma Widgets. This will present a front-end for https://store.kde.org/ that allows you to install, uninstall, or update third-party Plasmoid scripts with just one click.

## Sound applet in the system tray
Install  or  (start Kmix from the Application Launcher).  is now installed by default with , no further configuration needed.

## Disable panel shadow
As the Plasma panel is on top of other windows, its shadow is drawn over them. To disable this behaviour without impacting other shadows, install  and run:

 $ xprop -remove _KDE_NET_WM_SHADOW

then select the panel with the plus-sized cursor. [https://forum.kde.org/viewtopic.php%3Ff=285&t=121592.html For automation, install  and create the following script:

Make the script executable.

The script can be run on login with Add Login Script in Autostart:

 $ kcmshell6 autostart

## Display scaling / High DPI displays
See HiDPI#KDE Plasma.

## Plasma Mobile
The plasma-phone-settings repository contains several recommended settings which can be applied globally () and/or per user ().

## Lock screen
 (or ) locks the screen immediately after login. This is useful in combination with SDDM#Autologin.

## Virtual keyboard
To use a virtual keyboard in the Wayland session, install  and enable it in System Settings > Keyboard > Virtual Keyboard.

If your device has a hardware keyboard, but you want to use the virtual keyboard, add the  environment variable to your Wayland session.

To use a virtual keyboard in the X11 session, choose an appropriate one from List of applications/Utilities#On-screen keyboards and run it manually.

## Window decorations
[https://store.kde.org/browse/cat/114/ Window decorations can be found in the AUR.

They can be changed in System Settings > Colors & Themes > Window Decorations, there you can also directly download and install more themes with one click.

## Icon themes
Icon themes can be installed and changed on System Settings > Colors & Themes > Icons.

## Space efficiency
The Plasma Netbook shell has been dropped from Plasma 5, see the following KDE forum post. However, you can achieve something similar by editing the file  adding  in the  section.

## Thumbnail generation
To allow thumbnail generation for media or document files on the desktop and in Dolphin, install  and .

Then enable the thumbnail categories for the desktop via right click on the desktop background > Configure Desktop and Wallpaper... > Icons > Configure Preview Plugins....

In Dolphin, navigate to Configure > Configure Dolphin... > Interface > Previews.

## Night Light
Plasma provides a Redshift-like feature (working on both Xorg and Wayland) called Night Light. It makes the colors on the screen warmer to reduce eye strain at the time of your choosing. It can be enabled in System Settings > Colors & Themes > Night Light.

## Printing
You can also configure printers in System Settings > Printers. To use this method, you must first install the following packages , , . See CUPS#Configuration.

## Samba/Windows support
The Dolphin share functionality requires the package  and usershares, which the stock  does not have enabled. Instructions to add them are in Samba#Enable Usershares, after which sharing in Dolphin should work out of the box after restarting Samba.

Accessing Windows shares from Dolphin works out of the box. Use the path  to browse the files.

Unlike GTK file browsers which utilize GVfs also for the launched program, opening files from Samba shares in Dolphin via KIO makes Plasma copy the whole file to the local system first with most programs (VLC is an exception).
To workaround this, you can use a GTK based file browser like  with  and  (and  for saving login credentials) to access SMB shares in a more able way.

Another possibility is to mount a Samba share via  to make it look to Plasma like if the SMB share was just a normal local folder and thus can be accessed normally.
See Samba#Manual mounting and Samba#Automatic mounting.

A GUI solution is available with , which offers basically the same functionality via an easy to use option located at System Settings > Network Drivers. However, it might break with new KDE Plasma versions.

## KDE Desktop activities
KDE Desktop Activities are special workspaces where you can select specific settings for each activity that apply only when you are using said activity.

## Power management
Install  for an integrated Plasma power managing service. This service offers additional power saving features, monitor brightness control (if supported) and battery reporting including peripheral devices.

## Autostart
Plasma can autostart applications and run scripts on startup and shutdown. To autostart an application, navigate to System Settings > Autostart and add the program or shell script of your choice. For applications, a .desktop file will be created, for login scripts, a .desktop file launching the script will be created.

* Place Desktop entries (i.e. .desktop files) in the appropriate XDG Autostart directory.
* Place or symlink shell scripts in one of the following directories:
** : for executing scripts at login before launching Plasma.
** : for executing scripts when Plasma exits.

See official documentation.

## Phonon
From Wikipedia:

:Phonon is the multimedia API provided by KDE and is the standard abstraction for handling multimedia streams within KDE software and also used by several Qt applications.

:Phonon was originally created to allow KDE and Qt software to be independent of any single multimedia framework such as GStreamer or xine and to provide a stable API for a major version's lifetime.

Phonon is being widely used within KDE, for both audio (e.g., the System notifications or KDE audio applications) and video (e.g., the Dolphin video thumbnails). It can use the following backends:

* VLC:
* GStreamer: , see GStreamer#Installation for additional codec support
* mpv:

KDE recommends only the VLC backend, as the GStreamer backend is unmaintained.

## Backup and restore
Plasma stores personalized desktop settings as configuration files in the XDG_CONFIG_HOME folder. Use the detail of configuration files to select and choose a method of backup and restore.

## systemd startup
Plasma uses a systemd user instance to launch and manage all the Plasma services. This is the default startup method since Plasma 5.25, but can be disabled to use boot scripts instead with the following command (however this may stop working in a future release):

 $ kwriteconfig6 --file startkderc --group General --key systemdBoot false

More details about the implementation can be read in Edmundson's blog: Plasma and the systemd startup.

## Spell checking
KDE applications use  for spell checking. See its optional dependencies for the supported spell checkers.

Configure it in System Settings > Spell Check.

## Running KWin Wayland on NVIDIA
See https://community.kde.org/Plasma/Wayland/Nvidia.

## Applications
The KDE project provides a suite of applications that integrate with the Plasma desktop. See the  group for a full listing of the available applications. Also see KDE for related KDE application pages.

Aside from the programs provided in KDE Applications, there are many other applications available that can complement the Plasma desktop. Some of these are discussed below.

## System administration
## Terminate Xorg server through KDE System Settings
Navigate to the submenu System Settings > Keyboard > Advanced (tab) > Key sequence to kill the X server and ensure that the checkbox is ticked.

## KCM
KCM stands for KConfig Module. KCMs can help you configure your system by providing interfaces in System Settings, or through the command line with kcmshell6. Some applications bundle their configuration modules, while others need to be installed separately:

*
*
*

More KCMs can be found at linux-apps.com.

## Desktop search
KDE implements desktop search with a software called Baloo, a file indexing and searching solution.

## Web browsers
The following web browsers can integrate with Plasma:

*
*
*
*

## PIM
KDE offers its own stack for personal information management (PIM). This includes emails, contacts, calendar, etc. To install all the PIM packages, you could use the  package group or the  meta package.

## Akonadi
Akonadi is a system meant to act as a local cache for PIM data, regardless of its origin, which can be then used by other applications. This includes the user's emails, contacts, calendars, events, journals, alarms, notes, and so on. Akonadi does not store any data by itself: the storage format depends on the nature of the data (for example, contacts may be stored in vCard format).

Install . For additional addons, install .

## SQLite
By default Akonadi will use SQLite and store the database in . To configure Akonadi to use SQLite explicitly, edit the Akonadi configuration file to match the configuration below:

## PostgreSQL
Akonadi supports either using the existing system-wide PostgreSQL instance, i.e. , or running a PostgreSQL instance with user privileges and the database in .

## Per-user PostgreSQL instance
Install  and .

Edit the Akonadi configuration file so that it has the following contents:

Start Akonadi with , and check its status: .

## System-wide PostgreSQL instance
This requires an already configured and running PostgreSQL.

Create a PostgreSQL user account for your user:

 createuser username

Create a database for Akonadi:

 [postgres$ createdb -O username -E UTF8 --locale=C -T template0 akonadi-username

Edit the Akonadi configuration file to match the configuration below:

Start Akonadi with , and check its status: .

## MySQL
For Akonadi to run a managed MariaDB instance (see MySQL for alternative providers) with the database stored in , edit the Akonadi configuration file to match the configuration below:

## System-wide MySQL instance
Akonadi supports using the system-wide MySQL for its database.===== Disabling Akonadi =====

Users who want to disable Akonadi would need to not start any KDE applications that rely on it. See this [https://userbase.kde.org/Akonadi#Disabling_the_Akonadi_subsystem section in the KDE userbase for more information.

## KDE Connect
KDE Connect provides several features to connect your Android or iOS phone with your Linux desktop:

* Share files and URLs to/from KDE from/to any app, without wires.
* Touchpad emulation: Use your phone screen as your computer's touchpad.
* Notifications sync (4.3+): Read your Android notifications from the desktop.
* Shared clipboard: copy and paste between your phone and your computer.
* Multimedia remote control: Use your phone as a remote for Linux media players.
* Wi-Fi connection: no usb wire or bluetooth needed.
* RSA Encryption: your information is safe.

You will need to install KDE Connect both on your computer and on your phone. For PC, install  package. For Android, install KDE Connect from Google Play or from F-Droid. If you want to browse your phone's filesystem, you need to install  as well and configure filesystem exposes in your Android app. For iOS, install KDE Connect from the App Store. Not all features from the Android version are available on the iOS version.

To use remote input functionality on a Plasma Wayland session, the  package is required.

It is possible to use KDE Connect even if you do not use the Plasma desktop. For GNOME users, better integration can be achieved by installing  instead of . To start the KDE Connect daemon manually, execute .

If you use a firewall, you need to open UDP and TCP ports  through .

Sometimes, KDE Connect will not detect a phone. You can restart the services by running  and then opening kdeconnect in system settings or running  followed by . You can also use Pair new device > Add devices by IP on KDE Connect for Android.

## Tips and tricks
## Use a different window manager
It is possible to use a window manager other than KWin with Plasma. This allows you to combine the functionality of the KDE desktop with the utility of a tiling window manager, which may be more fleshed out than KWin tiling scripts.

The component chooser settings in Plasma no longer allows changing the window manager, but you are still able to swap KWin via other methods.

## Replacing KWin service
Since KDE 5.25, Plasma's systemd based startup is enabled by default.

To replace KWin in this startup, you must first mask the  for the current user to prevent it from starting.

Then, create a new systemd user unit to start your preferred WM To use it, do (as user units) a daemon-reload, make sure you have masked  then enable the newly created .

## Using script-based boot and KDEWM
Plasma's script-based boot is used by disabling #systemd startup. If you have done so, you can change the window manager by setting the  environment variable before Plasma is invoked.

## System-wide
If you have root access, you can also add an XSession that will be available to all users as an option on the login screen.

First, create a script with execution permissions as follows:

Replace  to the path to your preferred WM. Ensure the path is correctly set. If KDE is unable to start the window manager, the session will fail and the user will be returned to the login screen.

Then, to add an XSession, add a file in  with the following content:

## KWin tiling window scripts
A list of KWin extensions that can be used to make KDE behave more like a tiling window manager.

*
*
*

## KWin debug console
KWin has a [https://blog.broulik.de/2025/10/little-kwin-helpers/ built-in debug console for inspecting runtime properties such as surfaces, input events, and clipboard contents. It can be started from KRunner (Open KWin debug console) or from your terminal by running:

 $ qdbus6 org.kde.KWin /KWin org.kde.KWin.showDebugConsole

## Configuring monitor resolution / multiple monitors
To enable display resolution management and multiple monitors in Plasma, install . This provides additional options to System Settings > Display & Monitor.

## Configuring ICC profiles
On X11, ICC profiles are handled by . To configure them in Plasma, install . This provides additional options in System Settings > Color Management. ICC profiles can be imported using Import Profile.

For Wayland sessions, color management is handled by the compositor, i.e. KWin for Plasma. In this case, no additional package is required. The color profile can be configured per monitor in System Settings > Display & Monitor > Color Profile.

## HDR
HDR support only works in a Wayland session. System Settings > Display & Monitor > High Dynamic Range > Enable HDR.

For more information on displaying HDR content see HDR monitor support. Development details about HDR in Plasma can be found on Xaver Hugl's blog posts.

When enabling HDR mode in KDE Plasma, SDR content can appear extremely dark, sometimes making the screen nearly unreadable. To address this, KDE provides two key sliders in display settings: Maximum SDR Brightness, which adjusts the brightness mapping for SDR content in HDR mode, and Brightness which controls the overall display backlight or luminance.

## Disable opening application launcher with Super key (Windows key)
To disable this feature, you currently have to edit the  config file and set the  key under  to an empty string:

Alternatively, you can also run the following command:

 $ kwriteconfig6 --file kwinrc --group ModifierOnlyShortcuts --key Meta ""

## Disable bookmarks showing in application menu
With the Plasma Browser integration installed, KDE will show bookmarks in the application launcher.

To disable this feature, go to System Settings > Search > Plasma Search and uncheck Bookmarks.

## IBus Integration
IBus is an input method framework and can be integrated into KDE. See IBus#Integration for details.

Using IBus may be required when using KDE on Wayland to offer accented characters and dead keys support === Enable hotspot in plasma-nm ===

See NetworkManager#Sharing internet connection over Wi-Fi.

## Restore previous saved session
If you have System Settings > Session > Desktop Session > Session Restore > On login, launch apps that were open: On last logout (default) selected, ksmserver (KDE's session manager) will automatically save/load all open applications to/from  on logout/login.

## Receive local mail in KMail
If you have set up local mail delivery with a mail server that uses the Maildir format, you may want to receive this mail in KMail. To do so, you can re-use KMail's default receiving account "Local Folders" that stores mail in .

Symlink the  directory (where Maildir format mail is commonly delivered) to the Local Folders' inbox:

 $ ln -s .local/share/local-mail/inbox ~/Maildir

Alternatively, add a new receiving account with the type Maildir and set  as its directory.

## Configure Plasma for all users
Edit  files in the . For example, to configure the Application Launcher for all users, edit . To prevent the files from being overwritten with package updates, add the files to Pacman's NoUpgrade

## Disable hibernate
Properly disable the hibernate feature and hide it from the menu with a Polkit policy rule.

{{hc|/etc/polkit-1/rules.d/99-disable-hibernate.rules|
// Disable hibernate for all users
polkit.addRule(function(action, subject) {
   if ((action.id == "org.freedesktop.login1.hibernate")) {
      return polkit.Result.NO;
   }
});
polkit.addRule(function(action, subject) {
   if ((action.id == "org.freedesktop.login1.hibernate-multiple-sessions")) {
      return polkit.Result.NO;
   }
});
}}

Alternatively, add the following lines to a file in :

## Using window rules
Kwin has the ability to specify rules for specific windows/applications. For example, you can force enable the window titlebar even if the application developer decided that there should not be one. You can set such rules as specific starting position, size, minimize state, keeping above/below others and so on.

To create a rule you can press  when the window of interest is in focus. Then, in More Actions > Configure special application/window settings, you can set the desired property. A list of created rules is available from System Settings > Window Management > Window Rules.

## Mount network shares in fixed location
By default KDE mount manager () will mount network shares to {{ic|${XDG_RUNTIME_DIR}/kio-fuse-6-char-random-string}}.

Create directory, e.g.  in your home directory:

 $ mkdir ~/mnt_kio

Override default  using a drop-in file:

Now if you mount your network shares via dbus or by openning some file from remote share in Dolphin:

They will be mounted to .

## Locally Integrated Menu
To have the menu bar integrated with the title bar, install  from the AUR, then in System Settings > Window Decorations, select 'Material' and add the Application Menu button to the title bar (preferably as second from the left).

## Pre-authorize remote control on Wayland
Xdg-desktop-portal-kde has support for remote input from a remote desktop session, a virtual KVM switch, kde-connect, emulated devices like a controller using steam-input, etc. This authorization is lost after the application or the desktop-portal is restarted, which causes the "Remote control requested" window pop up every time and makes unattended access impossible.

As of plasma version 6.3, a permission system was [https://invent.kde.org/plasma/xdg-desktop-portal-kde/-/merge_requests/326 implemented, which allows to pre-authorize applications. Currently, the permission api is only available through the  cli, although applications do not need to run as a flatpak to be able to get pre-authorized.

As per the upstream docs and  man pages, you need to figure out if the application you want to authorize sets an application ID or not. If started through a runner like KRunner, it gets set by plasma and is usually the filename of the -file under .

For example, to pre-authorize a virtual KVM switch like , you would do:
 $ flatpak permission-set kde-authorized remote-desktop de.feschbar.LanMouse yes
If you start it as a daemon in a systemd user-unit, you should use the name of that unit instead:
 $ flatpak permission-set kde-authorized remote-desktop lan-mouse yes
If you application does not set an ID, you can leave that field empty:
 $ flatpak permission-set kde-authorized remote-desktop "" yes

## Ambient Light Sensor
Starting with Plasma 6.6.0, the screen brightness can be controlled automatically by an Ambient Light Sensor if your device is equipped with one.

To enable this feature,  needs to be installed which is an optional dependency of  and hence not installed by default. This enables the  and after restarting the Plasma session, the option "Automatically adapt to environment" will show up in Plasma Display Configuration.

Internally, this feature uses a brightness curve which is adapted automatically according to brightness settings by the user.

The current implementation of automatic brightness does not support X11 but not due to technical limitationsFor X11 support check out .

## Troubleshooting
## KDE applications fail to start in GNOME after upgrade to KDE 6
Wayland is used by default for KDE 6 applications, and the KDE applications fail to work under GNOME Wayland (and potentially other DEs/WMs) in this scenario. This can be fixed by setting the  environment variable.

This is a workaround for KDE bugs and not a problem with Wayland itself.

## KDE icons missing after upgrade to KDE 6
After the last upgrade to KDE 6 you may notice issues with all of the KDE icons not displaying. Newly created accounts showed them just fine.

The issue for this is that the theme got lost while upgrading and had to be reassigned manually. For this go to System Settings > Colors & Themes > Icons and select the theme you would like to use for the icons again.

## qt5ct and kvantum bugs after upgrade
Latest update might cause incompatible HiDPI scaling that made some interfaces becomes too big for your screen, some icons are missing or can not be displayed, and missing panels or widgets.

Try to remove  and  related package, then apply default global Plasma theme. If the problem persists, try clearing all your KDE configuration and reinstalling  to overwrite the configuration. Be sure to check HiDPI scaling in KDE system settings as well.

## Fonts are huge or seem disproportional
Try to force font DPI to  in System Settings > Text & Fonts > Fonts.

If that does not work, try setting the DPI directly in your Xorg configuration as documented in Xorg#Setting DPI manually.

## Configuration related
Many problems in KDE are related to its configuration.

## Plasma desktop behaves strangely
Plasma problems are usually caused by unstable Plasma widgets (colloquially called plasmoids) or Plasma themes. First, find which was the last widget or theme you had installed and disable or uninstall it.

So, if your desktop suddenly exhibits "locking up", this is likely caused by a faulty installed widget. If you cannot remember which widget you installed before the problem began (sometimes it can be an irregular problem), try to track it down by removing each widget until the problem ceases. Then you can uninstall the widget, and file a bug report on the [https://bugs.kde.org/ KDE bug tracker only if it is an official widget. If it is not, it is recommended to find the entry on the KDE Store and inform the developer of that widget about the problem (detailing steps to reproduce, etc.).

If you cannot find the problem, but you do not want all the settings to be lost, navigate to  and run the following command:

 $ for j in plasma*; do mv -- "$j" "${j%}.bak"; done

This command will rename all Plasma related configuration files to *.bak (e.g. ) of your user and when you will relogin into Plasma, you will have the default settings back. To undo that action, remove the .bak file extension. If you already have *.bak files, rename, move, or delete them first. It is highly recommended that you create regular backups anyway. See Synchronization and backup programs for a list of possible solutions.

## Clean cache to resolve upgrade problems
The problem may be caused by old cache. Sometimes, after an upgrade, the old cache might introduce strange, hard to debug behaviour such as unkillable shells, hangs when changing various settings, Ark being unable to extract archives or Amarok not recognizing any of your music. This solution can also resolve problems with KDE and Qt applications looking bad after an update.

Rebuild the cache using the following commands:

 $ rm ~/.config/Trolltech.conf
 $ kbuildsycoca6 --noincremental

Optionally, empty the  folder contents, however, this will also clear the cache of other applications:

 $ rm -rf ~/.cache/*

Sometimes, empty the  folder does not work, for example, if you encountered the following error:

 kf.service.sycoca: The menu spec file ( "" ) contains a Layout or DefaultLayout tag without the mandatory Merge tag inside. Please fix it.

It might be something related to outdated configuration files. In the above case, moving  folder away may fix the issue. In other cases, try moving each file out of  folder could be a good way to check what triggers the error.

## Plasma desktop does not respect locale/language settings
Plasma desktop may use different settings than you set at KDE System Settings panel, or in  (per Locale#Variables). First thing to do is log out and log in after removing , if this does not fix the issue, try to edit the file manually. For example, to set  variable to  and the  variable to :

## Cannot change theme, icons, fonts, colors in systemsettings; most icons are not displayed
Make sure that  environment variable is unset, the command  should show empty output. Otherwise if you had an environment set (most likely qt5ct or qt6ct) the variable will force qt5ct/qt6ct settings upon Qt applications, the command  should unset the environment.

An easier (and more reliable) solution can be to uninstall completely qt5ct and qt6ct.

## Volume control, notifications or multimedia keys do not work
Hiding certain items in the System Tray settings (e.g. Audio Volume, Media Player or Notifications) also disables related features. Hiding the Audio Volume disables volume control keys, Media Player disables multimedia keys (rewind, stop, pause) and hiding Notifications disables showing notifications.

## Login Screen KCM does not sync cursor settings to SDDM
The Login Screen KCM reads your cursor settings from , without this file no settings are synced. The easiest way to generate this file is to change your cursor theme in System Settings > Colors & Themes > Cursors, then change it back to your preferred cursor theme.

## Missing panels/widgets
A crash or hardware change can modify the screen numbers, even on a single monitor setup. The panels/widgets can be missing after such an event, this can be fixed in the  file by changing the  values.

## Graphical problems
Make sure you have the proper driver for your GPU installed. See Graphics processing unit#Installation to identify your hardware and choose the driver for it. If you have an older card, it might help to #Disable desktop effects manually or automatically for defined applications or #Disable compositing.

## Forcing dGPU usage on hybrid graphics systems
Hybrid graphics is a power management strategy commonly used in laptops that keeps the dedicated graphics processor (dGPU) inactive when not needed, defaulting to the integrated graphics processor (iGPU) for basic desktop rendering to conserve battery life.

While this approach saves power, it can result in suboptimal desktop performance, including low frame rates in animations and potential graphical artifacts, even on systems with capable dGPUs.

Forcing KDE Plasma to utilize the discrete GPU can significantly improve desktop responsiveness and visual quality.

## Method 1: DRI_PRIME (Open-source drivers)
For systems using open-source graphics drivers (Intel + AMDGPU, Intel + Nouveau), you can globally set the  environment variable to specify the dGPU:

The index value (0 or 1) depends on your system configuration. Verify which index corresponds to your dGPU by running:

## Method 2: KWIN_DRM_DEVICES (KWin-specific)
For direct control over KWin's GPU selection, create a startup script that sets the DRM device priority:

To identify your DRM cards and their corresponding GPUs:

List the dGPU first in the  variable to prioritize it for rendering.

## Getting current state of KWin for support and debug purposes
This command prints out a summary of the current state of KWin including used options, used compositing backend and relevant OpenGL driver capabilities. See more on Martin's blog.

 $ qdbus6 org.kde.KWin /KWin org.kde.KWin.supportInformation

## Disable desktop effects manually or automatically for defined applications
Plasma has desktop effects enabled by default and e.g. not every game will disable them automatically. You can disable desktop effects in System Settings > Window Management > Desktop Effects and you can toggle desktop effects with .

Additionally, you can create custom KWin rules to automatically disable/enable compositing when a certain application/window starts under System Settings > Window Management > Window Rules.

## Enable transparency
If you use a transparent background without enabling the compositor, you will get the message:

 This color scheme uses a transparent background which does not appear to be supported on your desktop

In System Settings > Display & Monitor > Compositor, check Compositing: Enable on startup and restart Plasma.

## Disable compositing
In System Settings > Display & Monitor > Compositor, uncheck Compositing: Enable on startup and restart Plasma.

## Flickering in fullscreen when compositing is enabled
In System Settings > Display & Monitor > Compositor, uncheck Compositing: Allow applications to block compositing. This may harm performance.

## Effects such as Expose, Overview and Desktop Grid are jerky
Setting the environment variable  for KWIN reduces jerking in some Quick Scene Graphics based effects. For this purpose, it is sufficient to create a drop-in for the service running KWIN:

(in the case of Wayland session, use  as directory name)

Then restart the session.

Another try is to set  instead of .

## Plasma cursor sometimes shown incorrectly
Create the directory  (alternatively, ), then, inside it, create a file named , then add to it the following contents:

If applicable, replace  with the cursor theme you use (cursor themes can be found in , e.g. ).

On Wayland, it is necessary for  to be installed for GTK/GNOME applications to correctly apply cursor themes.

## Firefox and Thunderbird ignore cursor theme
Firefox and Thunderbird running under Wayland will refer to GSettings to determine which cursor to display.

To sync KDE settings to GTK applications, install .

If you do not want to install an extra package, you can set the cursor theme manually:

 $ gsettings set org.gnome.desktop.interface cursor-theme cursor-theme-name

## Cursor jerking/flicking when changing roles (e.g., when mousing over hyperlinks)
Try installing the appropriate 2D acceleration driver for your system and window manager.

## Unusable screen resolution set
Your local configuration settings for kscreen can override those set in . Look for kscreen configuration files in  and check if mode is being set to a resolution that is not supported by your monitor.

## Blurry icons in system tray
In order to add icons to tray, applications often make use of the library appindicator. If your icons are blurry, check which version of libappindicator you have installed. If you only have  installed, you can install  as an attempt to get clear icons.

## Cannot change screen resolution when running in a virtual machine
When running Plasma in a VMware, VirtualBox or QEMU virtual machine, kscreen may not allow changing the guest's screen resolution to a resolution higher than 800×600.

The workaround is to set the  option in . Alternatively try using a different graphics adapter in the virtual machine, e.g. VBoxSVGA instead of VMSVGA for VirtualBox and Virtio instead of QXL for QEMU. See KDE Bug 407058 for details.

## Dolphin, Kate, etc. stuck long time when opening
Check whether your user directories (, , etc.) are read-only.

## Spectacle screenshot uses old screen state
In System Settings > Display & Monitor > Compositor, change Keep window thumbnails from Only from Shown windows to Never. If you are using Intel graphics, ensure that  is not installed.

## Poor font rendering in GTK applications
See XDG Desktop Portal#Poor font rendering in GTK applications on KDE Plasma.

## Improper window resizing
You may observe that windows of some applications do not resize properly, but rather, the resized portion is transparent and mouse clicks are sent to the underlying window. To correct this behavior, change KDE's GTK3 theme to something other than oxygen-gtk.

## Random lockups while using modesetting or nouveau driver for old nvidia cards
See Nouveau#Random lockups with kernel error messages.

## Sound problems
## No sound after suspend
If there is no sound after suspending and KMix does not show audio devices which should be there, restarting plasmashell and pulseaudio may help:

 $ killall plasmashell
 $ systemctl --user restart pulseaudio.service
 $ plasmashell

Some applications may also need to be restarted in order for sound to play from them again.

## MP3 files cannot be played when using the GStreamer Phonon backend
This can be solved by installing the GStreamer libav plugin (package ). If you still encounter problems, you can try changing the Phonon backend used by installing another such as .

Then, make sure the backend is preferred via phononsettings.

## No volume control icon in tray and cannot adjust sound by function key
Check if you have  installed.

## No sound after a short time
If  contains entries saying , try commenting the following line in :

 #load-module module-suspend-on-idle

If the issue persists,  or  may have installed  alongside . To fix the issue, replace  with . If  is preferred, replace  with . See PipeWire#PulseAudio clients and this forum thread for more details.

## Power management
## No Suspend/Hibernate options
If your system is able to suspend or hibernate using systemd but do not have these options shown in KDE, make sure  is installed.

## No power profile options
Make sure you installed  and .
Run powerprofilesctl and check the driver. If it is  or , you are done, otherwise see CPU frequency scaling#Scaling drivers for more information on enabling them.

## KMail
## Clean Akonadi configuration to fix KMail
See for details.

If you want a backup, copy the following configuration directories:

 $ cp -a ~/.local/share/akonadi ~/.local/share/akonadi-old
 $ cp -a ~/.config/akonadi ~/.config/akonadi-old

## Empty IMAP inbox in KMail
For some IMAP accounts KMail will show the inbox as a top-level container (so it will not be possible to read messages there) with all other folders of this account inside.[https://bugs.kde.org/show_bug.cgi?id=284172. To solve this problem simply disable the server-side subscriptions in the KMail account settings.

## Authorization error for EWS account in KMail
While setting up EWS account in KMail, you may keep getting errors about failed authorization even for valid and fully working credentials. This is likely caused by broken communication between KWallet and KMail. To workaround the issue set a passsword via qdbus:

 $ qdbus6 org.freedesktop.Akonadi.Resource.akonadi_ews_resource_0 /Settings org.kde.Akonadi.Ews.Wallet.setPassword "XXX"

## Aggressive QXcbConnection / kscreen.xcb.helper journal logging
See Qt#Disable/Change Qt journal logging behaviour.

## KF5/Qt 5 applications do not display icons in i3/FVWM/awesome
See Qt#Configuration of Qt 5/6 applications under environments other than KDE Plasma.

## Problems with saving credentials and persistently occurring KWallet dialogs
It is not recommended to turn off the KWallet password saving system in the user settings as it is required to save encrypted credentials like Wi-Fi passphrases for each user. Persistently occuring KWallet dialogs can be the consequence of turning it off.

In case you find the dialogs to unlock the wallet annoying when applications want to access it, you can let the display managers Plasma Login Manager, SDDM and LightDM unlock the wallet at login automatically, see KDE Wallet#Unlock KDE Wallet automatically on login. The first wallet needs to be generated by KWallet (and not user-generated) in order to be usable for system program credentials.

In case you want the wallet credentials not to be opened in memory for every application, you can restrict applications from accessing it with  in the KWallet settings.

If you do not care for credential encryption at all, you can simply leave the password forms blank when KWallet asks for the password while creating a wallet. In this case, applications can access passwords without having to unlock the wallet first.

## Discover does not show any applications
This can be solved by installing .

## Discover stops showing updates from Arch repositories
Discover sometimes will not remove its PackageKit alpm lock. To release it, remove . Use "Refresh" in Discover and updates should appear (if there are any updates pending).

## High CPU usage of kscreenlocker_greet with NVIDIA drivers
As described in KDE Bug 347772 NVIDIA OpenGL drivers and QML may not play well together with Qt 5. This may lead  to high CPU usage after unlocking the session. To work around this issue, set the  environment variable to .

Then kill previous instances of the greeter with .

## OS error 22 when running Akonadi on ZFS
If your home directory is on a ZFS pool, create a  file with the following contents:

 innodb_use_native_aio = 0

See MariaDB#OS error 22 when running on ZFS.

## Some programs are unable to scroll when their windows are inactive
This is caused by the problematic way of GTK3 handling mouse scroll events. A workaround for this is to set environment variable . However, this workaround also breaks touchpad smooth scrolling and touchscreen scrolling.

## TeamViewer behaves slowly
When using TeamViewer, it may behave slowly if you use smooth animations (such as windows minimizing). See #Disable compositing as a workaround.

## Kmail, Kontact and Wayland
Kmail may become unresponsive, show a black messageviewer or similar, often after having been minimized and restored. A workaround may be to set environment variable . See [https://bugs.kde.org/show_bug.cgi?id=397825 KDE Bug 397825.

## Unlock widgets (Plasma ≥ 5.18)
If you previously locked your widgets, you will probably find yourself unable to unlock them again.
You just have to run this command to do so:

 $ qdbus6 org.kde.plasmashell /PlasmaShell evaluateScript "lockCorona(false)"

The new  does not require to lock them back up but if want to do that:

 $ qdbus6 org.kde.plasmashell /PlasmaShell evaluateScript "lockCorona(true)"

## KIO opens URLs with the wrong program
Check file associations regarding HTML, PHP, etc... and change it to a browser. KIO's cache files are located in . See also xdg-utils#URL scheme handlers.

## Lock the screen before suspending and hibernating
In the System Settings application, KDE offers a setting to automatically lock the screen after waking up from sleep. Upon resuming, some users report that the screen is briefly showed before locking. To prevent this behavior and have KDE lock the screen before suspending, create a hook in  by creating the following file as the root user:

The use of  is necessary in order for the  command to complete before the device is suspended. Using a lower timeout may not allow for this to complete.

After creating the file, make it executable.

Finally, make sure that the KDE setting is enabled by going to System Settings > Screen Locking and checking the Lock screen automatically: After waking from sleep checkbox.

## X11 shortcuts conflict on Wayland
Some X11 software like  can grab keyboard input since KDE 5.27. Others like VMware cannot grab correctly. It is inappropriate to force grab [https://gitlab.freedesktop.org/xorg/xserver/-/issues/1332 in Xserver or in compositors. You can solve it in an elegant way as follows:

* Right click the window titlebar (e.g. VMware or Citrix);
* More Actions > Configure Special Window Settings...
* Click Add Property... and select Ignore global shortcuts.
* Select force and yes. Apply it.

## System settings not applying when changed
This can be caused because system settings cannot access/modify the .config folder in your home directory.

To fix this, you need to change the owner of the folder:

 # chown user:user /home/user/.config

 refers to the name of the user that you are logged into in KDE Plasma. If the name of your home directory is not the same as the user you are logged in as, you can change it accordingly.

If this does not work, you might need to change the permissions of the folder:

 # chmod 755 /home/user/.config

## Plasma 6 Global Menu not working with some applications
There are issues with the Widget "Global Menu" not working with some applications even after installing  and . The fix is to install the  and to restart your Session.

## Automatic mounting of internal drives not working
It is necessary to add a Polkit rule allowing mounting of internal drives without elevated privileges:

{{hc|/etc/polkit-1/rules.d/10-udisks2.rules|2=
polkit.addRule(function(action, subject) {
  if (action.id == "org.freedesktop.udisks2.filesystem-mount-system") {
    return polkit.Result.YES;
  }
});
}}

## Various screen problems
KDE's  uses  by default, but may not be compatible with certain screen types (especially laptop screens) and lead to various screen problems such as frozen image, black screen after logging in, flickering etc. To mitigate the problem, you can try to disable it.

Powerdevil can be configured with drop-in file for the user unit:

Finally, restart the  user unit.
