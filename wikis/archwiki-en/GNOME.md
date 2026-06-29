# GNOME

GNOME (/(ɡ)noʊm/) is a desktop environment that aims to be simple and easy to use. It is designed by The GNOME Project and is composed entirely of free and open-source software. It uses Wayland, and the available sessions are

* GNOME, the default, runs GNOME Shell on Wayland. Traditional X applications are run through Xwayland.
* GNOME Classic provides a "traditional desktop experience" (with an interface similar to GNOME 2) by using certain extensions and values. Thus, it is a customized form of GNOME Shell rather than a truly distinct mode.

## Installation
The following package groups are available:

*  contains the base GNOME desktop and the well-integrated core applications;
*  contains various extra applications extending the GNOME ecosystem.
*  contains development tools as well as some further applications and games that fits well into GNOME.

The base desktop consists of GNOME Shell, a plugin for the Mutter window manager. It can be installed separately with .

Unstable releases can also be used, see Official repositories#gnome-unstable.

## Starting
GNOME can be started either graphically with a display manager or manually from the console (some features may be missing). The display manager included in  is GDM.

## Graphically
If you installed the  group and want GNOME to start automatically on next boot, enable . You can then select the desired session: GNOME or GNOME Classic (only displayed if  is installed) from the display manager's session menu.

If you prefer to start GNOME right away, thereby avoiding a reboot, start the aforementioned  from a graphically unoccupied tty instead.

## Manually
## Session type
GNOME session inherits session type from systemd. Systemd session type is determined from  environment variable when the session is started, and can only be changed by the controller of that session afterwards. See the systemd issue on Github.

Therefore merely setting  after login does not work. Instead, create a systemd drop-in file to set environment for getty :

To show session type after reload:
 $ loginctl session-status

## Start session
After  and login session type is set correctly, manually starting a Wayland session is possible with:
 $ gnome-session

Running  directly is not recommended, because it lacks session management.

Note that manual invocation of Gnome does not require  (consequently also the accompanying ) at all and is thus also accessible for users with a (possibly very) minimal installation of Gnome composing of a selected few packages included in the more inclusive  group in accordance to personal preference.

To start on login to tty1, add to your :

The  flag prevents gnome-session from starting a login shell which sources the profile again and loops.

Firefox and QT applications do not respect , so add variables for them as well:

## GNOME applications in Wayland
When the GNOME session is used, GNOME applications will be run using Wayland. For debugging cases, https://docs.gtk.org/gtk3/running.html and https://docs.gtk.org/gtk4/running.html list options and environment variables.

## Navigation
To learn how to use the GNOME shell effectively, read the GNOME Shell Cheat Sheet; it highlights GNOME shell features and keyboard shortcuts. Features include task switching, keyboard use, window control, the panel, overview mode, and more. A few of the shortcuts are:

* : show notification list
* : show application grid
* : cycle active applications
*  (the key above  on US keyboard layouts): cycle windows of the application in the foreground
* , then enter  or : restart the shell in case of graphical shell problems (only in X/legacy mode, not in Wayland mode).

See /Tips and tricks#Navigation for changes to the default configuration making the window-switching resemble that of Windows.

See Keyboard navigation for more shortcuts.

## Legacy names
{| class="wikitable"
! Legacy
! Current
|-
| Baobab
| Disk Usage Analyzer
|-
| Decibels
| Audio Player
|-
| Epiphany
| Web
|-
| Loupe
| Image Viewer
|-
| Nautilus
| Files
|-
| Papers
| Document Viewer
|-
| Showtime
| Video Player
|-
| Simple Scan
| Document Scanner
|-
| Snapshot
| Camera
|}

## Configuration
GNOME Settings (gnome-control-center) and GNOME applications use the dconf configuration system to store their settings.

You can directly access the dconf database using the  command line tool. This also allows you to configure settings not exposed by the user interfaces. Command line tool  can directly modify the underlying database, bypassing validation. The configuration keys of gsettings and dconf are equivalent, but in a slightly different format:  in gsettings would be  in dconf.

Up until GNOME 3.24, settings were applied by the GNOME settings daemon (located at ), which could be run outside of a GNOME session.

GNOME 3.24, however, replaced the GNOME settings daemon with several separate settings plugins  which were later moved to . These plugins are now controlled via desktop files under  (matching ). To run these plugins outside of a GNOME session, you will now need to copy/edit the appropriate desktop entries to .

The configuration is usually performed user-specific; this section does not cover how to create configuration templates for multiple users.

## System settings
## Color
The daemon  reads the display's EDID and extracts the appropriate color profile. Most color profiles are accurate and no setup is required; however, for those that are not accurate, or for older displays, color profiles can be put in  and directed to.

## Night Light
GNOME comes with a built-in blue light filter similar to Redshift. You can enable and customise the time you want to enable Night Light from the display settings menu. Furthermore, you can tweak the kelvin temperature with the following  setting, where 5000 is an example value:

 $ gsettings set org.gnome.settings-daemon.plugins.color night-light-temperature 5000

## Date & time
If the system has a configured Network Time Protocol daemon, it will be effective for GNOME as well. The synchronization can be set to manual control from the menu, if required.

GNOME supports automatic time zone selection (can be enabled in Date & Time section of the system settings, given that location services are enabled (see Privacy section of the settings).

To show the date in the top bar, execute:

 $ gsettings set org.gnome.desktop.interface clock-show-date true

Additionally, to show week numbers in the calendar opened on the top bar, execute:

 $ gsettings set org.gnome.desktop.calendar show-weekdate true

## Default applications
Upon installing GNOME for the first time, you may find that the wrong applications are handling certain protocols. For example, totem opens videos instead of a previously used VLC. Some of the associations can be set from system settings via Default Applications.

For other protocols and methods, see Default applications for configuration.

## Mouse and touchpad
Most touchpad settings can be set from system settings via Mouse & Touchpad.

Depending on your device, other configuration settings may be available, but not exposed via the default GUI. For example, a different touchpad

to be set manually:

 $ gsettings set org.gnome.desktop.peripherals.touchpad click-method 'fingers'

or via .

## Resize windows by mouse
By default, you can use your mouse to move windows by holding down , clicking and holding the left mouse button and dragging the mouse around.

Additionally, you can enable using your mouse to resize windows by holding down , clicking and holding the right mouse button and dragging the mouse around:

 $ gsettings set org.gnome.desktop.wm.preferences resize-with-right-button true

If you don't like the  key, you can also change the modifier to something else, like  or :

 $ gsettings set org.gnome.desktop.wm.preferences mouse-button-modifier "''"

## Network
NetworkManager is the native tool of the GNOME project to control network settings from the shell. If you have not already, install the  package and enable the  systemd unit.

While any other network manager can be used alternatively, NetworkManager provides the full integration via the shell network settings and a status indicator applet  (not required for GNOME).

## Online accounts
Some online accounts, such as Nextcloud, require  and  to be installed for full functionality in GNOME applications such as GNOME Files and GNOME Documents See [https://help.gnome.org/users/gnome-help/stable/accounts.html.en Online accounts for more information.

## Search
The GNOME shell has a search that can be quickly accessed by pressing the  key and starting to type. The  package is installed by default as a dependency of  from the  group and provides an indexing application and metadata database. It can be configured with the Search menu item in Settings. It is started automatically by gnome-session when the user logs in.

localsearch does not automatically recurse into all directories under the user's home directory, so you may need to add custom paths via the Search > Search locations menu item. To exclude a directory from the indexing, create an empty  file.

A status is available with  and the indexed content can be searched (), edited (), or reset from the commandline. See  and , or the online help for reference.

The database uses  and can also be queried directly, if needed.

## Accessibility
GNOME has accessibility settings available via Settings > Accessibility. The main settings may be toggled directly after enabling a top bar icon, but note further settings are available via the sub-menus for Seeing, Hearing, Typing, Pointing and clicking and Zoom. See https://help.gnome.org/users/gnome-help/stable/a11y.html.en for information on them.

Additionally, a default set of keyboard shortcuts can be set via Settings > Keyboard > View and Customize Keyboard Shortcuts > Accessibility. For example, pressing ,  and  toggles zooming.

## Device security settings
GNOME has a Device Security panel via the Settings > Privacy & Security > Device Security menu. This requires  in order to function.=== Advanced settings ===

As noted above, many configuration options such as changing the GTK theme or the window manager theme are not exposed in GNOME Settings (gnome-control-center). Those users that want to configure these settings may wish to use the GNOME Tweaks (), a convenient graphical tool which exposes many of these settings.

GNOME settings (which are stored in the DConf database) can also be configured using the  (a graphical DConf configuration tool) or the [https://developer.gnome.org/gio/stable/GSettings.html gsettings command line tool. The GNOME Tweaks does not do anything else in the background of the GUI; note though that you will not find all settings described in the following sections in it.

## Extensions
The catalogue of extensions is available at https://extensions.gnome.org, they can be installed either through official repositories (only a few), the AUR or through the browser directly from the GNOME project.

Installed extensions can also be configured, enabled or disabled through a GUI with gnome-extensions-app, from the command line with , or from the browser. In your browser, extensions can be installed then activated in the browser by setting the switch in right top right of the screen to ON and clicking Install on the popup window (if the extension in question is not installed). Installed extensions may be seen at https://extensions.gnome.org/local/, where available updates can be checked.

The  package provides a set of very useful extensions maintained as part of the GNOME project.

 is a graphical tool which can also be used to install and remove extensions, as well as enable and disable them, both system-wide and for a user. Prior to using it, consider its list of known issues.

To enable usage of extensions (disabled by default):

 $ gsettings set org.gnome.shell disable-user-extensions false

To list currently enabled extensions:

 $ gsettings get org.gnome.shell enabled-extensions

The above command may list extensions that have been removed. To only list extensions that are enabled and installed, use gnome-extensions instead:

 $ gnome-extensions list --enabled

For more information about GNOME shell extensions, see https://extensions.gnome.org/about/.

## Appearance
## Themes
GNOME uses Adwaita by default. To apply Adwaita-dark only to GTK 2 applications, use the following symlink:

 $ ln -s /usr/share/themes/Adwaita-dark ~/.themes/Adwaita

To select new themes (move them to the appropriate directory and) use GNOME Tweaks or the GSettings commands below.

For the GTK theme:

 $ gsettings set org.gnome.desktop.interface gtk-theme theme-name

For the icon theme:

 $ gsettings set org.gnome.desktop.interface icon-theme theme-name

See GTK#Themes and Icons#Icon themes.

## Titlebar button order
To set the order for the GNOME window manager (Mutter, Metacity):

 $ gsettings set org.gnome.desktop.wm.preferences button-layout ':minimize,maximize,close'

## GNOME Shell themes
The theme of GNOME Shell itself is configurable. To use a Shell theme, firstly ensure that you have the  package installed. Then enable the User Themes extension, either through the GNOME Extensions application or through the GNOME Shell Extensions webpage. Shell themes can then be loaded and selected using GNOME Extensions.

There are a number of GNOME Shell themes available in the AUR, many themes do not have the same name format, so instead try searching for the appropriate theme in the AUR. Shell themes can also be downloaded from gnome-look.org.

## AppIndicators/Top bar icons
To enable AppIndicators, which is useful for controlling/monitoring certain applications running in the background, Install  or , restart the GNOME Shell, then enable the AppIndicator extension in the GNOME Extensions application or by running

 $ gnome-extensions enable $(gnome-extensions list  grep -m 1 appindicatorsupport)

## Shell animation speed
The GNOME shell animation can be sped up, slowed down or disabled. See GNOME/Tips and tricks#Change animation speed.

## Shell blur
Blur my Shell is an extension that adds blur effects to the overview screen as well as the shell itself and other apps. Install  or  for development updates. This extension is highly customizable, and you may choose to blur certain applications.

## Better Alt-Tab Functionality
The default Alt-Tab in GNOME is very simple and does not show overviews of the selected windows. You can change the Alt-Tab shortcut from "Switch Applications" to "Switch Windows" in Settings to show window overviews.

You can also use Coverflow Alt-Tab. It is an extension that expands the Alt-Tab behavior and adds features to make switching between applications easier while also giving it a better look. Install , then you may change the configuration of this extension to your liking.

Note: Super-` provides "Switch windows of an application` by default.

## Autostart
GNOME implements XDG Autostart.

The  allows managing autostart-entries.

## Desktop
## Dash to Dock
To move the dash out of the overview and turn it into a dock to easily launch and switch applications, install .

## Startup in Overview Mode
Starting from GNOME 40, the desktop will start directly into Overview Mode instead of an empty desktop (like in previous versions). To mimic legacy behaviour, one may install .

Alternatively, you can disable it using gsettings if using :

 $ gsettings set org.gnome.shell.extensions.dash-to-dock disable-overview-on-startup true

See the discussion at ==== Clipboard history ====

Unlike other desktop environments, GNOME does not have a built-in tool to manage the clipboard history. This can be done however with the help of an extension. Install .

## Weather
To display the current weather information in the top panel based on a chosen location, install . The weather information is updated in real-time and displays useful data such as conditions, wind speed, pressure, etc...

## Sound input/output device selector
By default, if you want to change your sound input or output device or change your microphone's volume, you need to open GNOME Control Center and configure these settings from there. To integrate a device selector and a microphone volume slider, install  or . Further configuration can be done after installation.

## Fonts
Fonts can be set for Window titles, Interface (applications), Documents and Monospace. See the Fonts tab in the Tweaks for the relevant options.

For hinting, RGBA will likely be desired as this fits most monitors types, and if fonts appear too blocked reduce hinting to Slight or None.

## Input methods
GNOME has integrated support for input methods through IBus. Only  and the wanted input method engine (e.g.  for Intelligent Pinyin) needed to be installed. After installation, the input method engine can be added as a keyboard layout under Keyboard > Input Sources in GNOME Settings (gnome-control-center).

## Keyboard Layout quirks
If you are using an alternative keyboard layout like Neo2 which uses multiple layers/modifiers, you might need to go to Keyboard > Type Special Characters in GNOME Settings (gnome-control-center) and change the Alternate Characters Key away from Right Alt so that it can be used as a native modifier of the keyboard layout. Setting it to e.g. Left Alt prevents Alt+Tab, so be careful what you change it to.
Without this change, your left Mod3 key might work, but the right one (AltGr) does not. (As of 2021-05-18)

## Power
When you are using a laptop, you might want to alter the following settings controlling behavior when idle, screen lock power button presses and lid close:

 $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-timeout 3600
 $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type hibernate
 $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-timeout 1800
 $ gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-battery-type hibernate
 $ gsettings set org.gnome.settings-daemon.plugins.power power-button-action suspend
 $ gsettings set org.gnome.desktop.lockdown disable-lock-screen true

To keep the monitor active when the lid is closed:

 $ gsettings set org.gnome.settings-daemon.plugins.xrandr default-monitors-setup do-nothing

GNOME 3.24 deprecated the following settings:

 org.gnome.settings-daemon.plugins.power button-hibernate
 org.gnome.settings-daemon.plugins.power button-power
 org.gnome.settings-daemon.plugins.power button-sleep
 org.gnome.settings-daemon.plugins.power button-suspend
 org.gnome.settings-daemon.plugins.power critical-battery-action

## Do not suspend when laptop lid is closed
The settings panel of GNOME does not provide an option for the user to change the action triggered when the laptop lid is closed. To change the lid switch action system-wide, edit the systemd settings in . To turn off suspend on lid close, set , as described in Power management#ACPI events.

## Change critical battery level action
The settings panel does not provide an option for changing the critical battery level action. These settings have been removed from dconf as well. They are now managed by upower. Edit the upower settings in . Find these settings and adjust to your needs.

## Power modes
Install the power-profiles-daemon optional dependency (of ) for power profiles support. Explicitly starting/enabling the  service is unnecessary since gnome-shell and GNOME Settings both request its activation upon launching.

When the service is active, power profiles can be managed through the Power section of GNOME Settings and in the system menu.

## Screencast
The built-in screenshot tool comes without the Screencast option by default. Install the  optional dependency (of ) to enable screen recording.

## Use a different window manager
GNOME Shell does not support using a different window manager, however GNOME Flashback provides sessions for Metacity and Compiz. Furthermore, it is possible to define your own custom GNOME sessions which use alternative components.

Replacing GNOME Shell with a different Wayland compositor will cause certain sections of  (GNOME Settings) to populate incorrectly. gnome-control-center will work, but since  (GNOME Shell) will not be available to provide settings for populating these sections, they will not have an effect or may not populate accurately with your settings. Sections affected are bluetooth, display, and mouse/touchpad to name a few.
