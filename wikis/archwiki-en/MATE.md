# MATE

From MATE homepage:

:The MATE Desktop Environment is the continuation of GNOME 2. It provides an intuitive and attractive desktop environment using traditional metaphors for Linux and other Unix-like operating systems. MATE is under active development to add support for new technologies while preserving a traditional desktop experience.

## Installation
MATE can be installed with one of the following:

*The  group contains the core desktop environment required for the standard MATE experience.
*The  group contains additional utilities and applications that integrate well with the MATE desktop. Installing just the  group will not pull in the whole  group via dependencies. If you want to install all MATE packages then you will need to explicitly install both groups.

The base desktop consists of ,  and .

## MATE applications
MATE is largely composed of GNOME 2 applications and utilities, forked and renamed to avoid conflicting with their GNOME 3 counterparts. Below is a list of common GNOME applications which have been renamed in MATE.

{| class="wikitable"
! Application
! GNOME 2
! MATE
|-
| Menu editor
| Alacarte
|
|-
| File manager
| Nautilus
|
|-
| Window manager
| Metacity
|
|-
| Text editor
| Gedit
|
|-
| Image viewer
| Eye of GNOME
| Eye of MATE ()
|-
| Document viewer
| Evince
|
|-
| Archive manager
| File Roller
|
|}

Other applications and core components prefixed with GNOME (such as GNOME Terminal, GNOME Panel, GNOME Menus, etc.) have had the prefix changed to MATE so they become MATE Panel, MATE Menus etc.

## Additional MATE packages
There are a number of other unofficial MATE applications that are contributed to and maintained by the MATE community and therefore not included in the  or  groups.

*
*
*
*
*

Additional packages need to be installed to take advantage of some of Caja's advanced features - see File manager functionality.

## Starting MATE
Choose MATE from the menu in a display manager of choice.

Alternatively, to start MATE with startx, append  to your  file.

## Configuration
MATE can be configured with its Control Center application (mate-control-center) provided by the  package. To manage some hardware, you may need to install additional tools.

; Audio
: ALSA and PulseAudio backends are supported by the  package.
; Bluetooth
: For Bluetooth device support, install the  package. See Blueman.
; Networking
: For configuring the network, install the  package. See NetworkManager.
; Power
: UPower backend is supported by the  package.
; Printers
: For configuring the printers, install the  package.

## Accessibility
MATE is well suited for use by individuals with sight or mobility impairment. Install ,  (Screen reader for individuals who are blind or visually impaired) and  (On-screen keyboard useful for mobility impaired users)

Before starting MATE for the first time, enter the following command as the user who needs accessibility features:

 $ gsettings set org.mate.interface accessibility true

Once you start MATE, you can configure the accessibility applications via System > Preferences > Assistive Technologies, although if you need Orca, you will need to run it from the  run window in order to start getting speech.

## Notifications
;Battery discharge

To disable the notification on battery discharge, run:

 $ gsettings set org.mate.power-manager notify-discharging false

;Brightness

See Backlight#Kernel command-line options.

## Tips and tricks
## Disabling compositing
Compositing is enabled by default. To disable it, navigate to Look and Feel > Windows > General in the System Preferences and tick the box alongside Enable software compositing window manager. Alternatively, you can run the following from the terminal:

 $ gsettings set org.mate.Marco.general compositing-manager false

## Disabling new window centering
By default, new windows are placed in the center. To disable centering new windows, navigate to run Windows > Placement in the System Preferences and tick the box alongside Center new windows. Alternatively, you can run the following from the terminal:

 $ gsettings set org.mate.Marco.general center-new-windows false

## Disabling window snapping
Window snapping is enabled by default. To disable it, navigate to run Windows > Placement in the System Preferences and tick the box alongside Enable window tiling. Alternatively, you can run the following from the terminal:

 $ gsettings set org.mate.Marco.general allow-tiling false

## Undecorating maximized windows
Hiding the decorations of maximized windows is possible with the use of  tool; after installation navigate to Look and Feel > MATE Tweak > Windows in the System Preferences and enable Undecorate maximized windows in the Window Behaviour section.

## Show or hide desktop icons
By default, MATE shows multiple icons on the desktop: the content of your desktop directory, computer, home and network directories, the trash and mounted drives. You can show or hide them individually or all at once using .

## Hide all desktop icons
 $ gsettings set org.mate.background show-desktop-icons false

Doing so may cause some graphics artifacts on secondary monitors.

## Hide individual icons
Hide computer icon:

 $ gsettings set org.mate.caja.desktop computer-icon-visible false

Hide user directory icon:

 $ gsettings set org.mate.caja.desktop home-icon-visible false

Hide network icon:

 $ gsettings set org.mate.caja.desktop network-icon-visible false

Hide trash icon:

 $ gsettings set org.mate.caja.desktop trash-icon-visible false

Hide mounted volumes:

 $ gsettings set org.mate.caja.desktop volumes-visible false

Replace  with  for the icons to reappear.

## Use a different window manager
The marco window manager can be replaced with another window manager via either of the following methods:

;Using gsettings (recommended)
Execute the following to specify a different window manager for MATE:

 $ gsettings set org.mate.session.required-components windowmanager wm-name

;Using MATE session autostart
You can autostart a window manager of your choice using mate-session-properties. This means that the autostarted window manager will replace the default window manager at login. Navigate to Startup Applications in the System Preferences. In the dialog click Add. The command should take the syntax .

## Prevent Caja from managing the desktop
To prevent Caja from managing the desktop, execute the following:
 $ gsettings set org.mate.background show-desktop-icons false
 $ killall caja  # Caja will be restarted by session manager

## Change window decoration button order
You can change the button order using the graphical dconf-editor or the gsettings command line tool:

 $ gsettings set org.mate.Marco.general button-layout 'close,maximize,minimize:'

and put menu, close, minimize and maximize in your desired order, separated by commas. The colon is used to specify on which side of the titlebar the window buttons will appear and must be used for the changes to apply.

## Auto open file manager after drive mount
By default, MATE automatically opens a new file manager window when a drive is mounted. To disable this:

 $ gsettings set org.mate.media-handling automount-open false

And to disable automounting:

 $ gsettings set org.mate.media-handling automount false

## Spatial view in Caja
To ensure that each new folder opens in a new window (known as spatial view), open Caja's preferences dialog, click on the behaviour tab and tick the 'Open each folder in its own window' option. Alternatively, execute the following command which achieves the same effect:
 $ gsettings set org.mate.caja.preferences always-use-browser false

## Change font DPI setting
You can alter the DPI (dots per inch) of the fonts in MATE by right-clicking on the desktop and choosing Change desktop background > Fonts > Details > Resolution.

## Change applications menu icon
By default, the applications menu icon is set to . To use a different icon, copy your icon to a folder such as  and execute the following:
 $ gsettings set org.mate.panel.menubar icon-name icon
where icon is the name of your icon. Do not include the file extension in the icon name. Finally, restart MATE Panel.

## Panel speed settings
;Hide/Unhide delay
To adjust the amount of time it takes for the panel to disappear or reappear when autohide is enabled, execute the following:
 $ dconf write /org/mate/panel/toplevels/panel/(un)hide-delay time
where panel is either top or bottom and time is a value in miliseconds, e.g. 300.

;Animation speed
To set the speed at which panel animations occur, execute the following:
 $ dconf write /org/mate/panel/toplevels/panel/animation-speed value
where panel is either top or bottom and value is either ,  or .

## Set the terminal for caja-open-terminal
The  extension uses GSettings to determine which terminal to use - mate-terminal is the default. To change the terminal that will be used, run the following command

 $ gsettings set org.mate.applications-terminal exec my-terminal

where my-terminal is the name of the terminal executable to be launched, for example: xterm.

## Troubleshooting
## Toggling compositing
Some software may have issues rendering graphics when working on an environment using the NVIDIA proprietary drivers and a compositing window manager.

To easily toggle the compositing feature, save the following script somewhere within the Home directory:

and then create a custom keyboard shortcut that executes the file, e.g. , to .

## Vertical sync for compositing
Mate's window manager, marco, supports tear-free software compositing via DRI3/Xpresent. If your graphics driver does not support DRI3 (e.g. the Nvidia Proprietary driver), marco does not support vertical synchronization via OpenGL, which may cause video tearing with enabled compositing. [https://github.com/mate-desktop/marco/issues/91 In this case, consider a different composite manager with OpenGL support such as picom.

## Consistent cursor theme
See Cursor themes#Desktop environments.

## Use of gradient backgrounds with LightDM
If you wish to use the default MATE (1.8) Stripes background as the LightDM background as well so as to make for seamless transition from LightDM to MATE, you will find that it is runtime-constructed from a grayscale PNG upon which MATE layers a vertical blue-to-green gradient, something which LightDM does not currently support. If insistent, you can work around this by temporarily setting  to , either through the  tool available from the  menu or by running

 $ gsettings set org.mate.background show-desktop-icons false

from the Alt-F2  dialog, then running  from said dialog and hitting  before the panel reappears. You are then presented with a  dialog for exactly that fully rendered, screen-sized PNG that you need for LightDM. Run

 $ gsettings set org.mate.background show-desktop-icons true

to have your desktop icons reappear, if desired.

## Enabling panel shadow
Due to a race condition, the panel shadow does not appear after logging in to the MATE desktop, even with compositing enabled. Copy  and add a delay:

If this has no effect, increase the delay duration.

## Logout/shutdown delayed by at-spi-registryd
When logging out or shutting down, you may find that you are presented with an A program is still running: at-spi-registryd.desktop popup. As a workaround, you can prevent at-spi-registryd from starting - see GTK#Suppress warning about accessibility bus - though this may have an effect on some accessibility features.

## Caja's text file preview
Since the migration to GTK 3 this feature is not working.[https://github.com/mate-desktop/caja/issues/1047

## GTK 2 applications seem to ignore default MATE themes
Themes that come with  need optional dependencies  and  for GTK 2 themes to function properly.

## Extra decoration on CSD applications
An extra decoration can appear on CSD applications (Firefox, Visual Studio Code...) when they are unmaximized.Uninstalling the package  solves the issue.

## Keyboard layout selector
When multiple keyboard layouts are enabled, a layout selection icon is displayed in the system tray. Because of a bug ([https://github.com/mate-desktop/libmatekbd/issues/28), depending on the currently used theme, it sometimes happens to be displayed with white font on bright background (or in some other barely legible configuration, such as with green font).

This issue can be worked around by manually setting the font color (e.g.,  for black):
 $ gsettings set org.mate.peripherals-keyboard-xkb.indicator foreground-color '0 0 0'
