# Enlightenment

## Enlightenment
This comprises both the Enlightenment window manager and Enlightenment Foundation Libraries (EFL), which provide additional desktop environment features such as a toolkit, object canvas, and abstracted objects. It has been under development since 2005, but in February 2011 the core EFLs saw their first stable 1.0 release.

## Installation
Install the  package.

You might also want to install some EFL-based applications that integrates well with Enlightenment:

*  – A text editor
*  – A picture viewer
*  – A task manager
*  – A video player
*  – A terminal emulator.

The following are EFL-based applications, most in an early stage of development and not yet released:

*  – An EFL based user interface for ConnMan network manager
*  – An EFL based IDE
*  – Eperiodique periodic table viewer
*  – A Python Media Center
*  – An on-screen ruler and measurement tools

## Moksha
For Bodhi Linux's fork of Enlightenment, install the  package with optional modules.

It conflicts with , because it uses the same binary name and config files. Make sure to backup your config files under  before switching to it.

## Starting Enlightenment
Simply choose Enlightenment session from your favourite display manager or configure xinitrc to start it from the console.

## Entrance
Enlightenment has a new display manager called Entrance, which is provided by the  package. Entrance is quite sophisticated and its configuration is controlled by . It can be used by enabling .

## Manually
If you prefer to start Enlightenment manually, enter  in the console. See xinitrc for details.

To try the Wayland compositor, enter  instead.

## Configuration
Enlightenment has a sophisticated configuration system that can be accessed from the Main menu's Settings submenu.

## Network
ConnMan

Enlightenment's preferred network manager is ConnMan which can be installed from the  package. Follow the instructions on ConnMan to do the configuration.

For extended configuration, you may also install Econnman (available in AUR as  or ) and its associated dependencies. This is not required for general functionality though.

Adding the ConnMan Gadget to the Shelf

# Settings -> Extensions -> Modules
# under System
# Connection Manager
# Load that (select then hit Load).
# Right-click on the shelf at the bottom of the screen.
# Go to Shelf -> Contents
# Then, just scroll around and find ConnMan.
# and hit Add.

NetworkManager

You can also use  to manage your network connections - see NetworkManager for more information.

Note however that the applet will need Appindicator support to show in Enlightenment's system tray. See NetworkManager#Appindicator. As an alternative to using the applet, NetworkManager includes both CLI and TUI interfaces for network configuration - see NetworkManager#Usage.

## Polkit agent
Enlightenment version DR 0.24.0 ships with a built-in polkit agent, and no extra polkit package is required to authenticate for privileged actions. Earlier versions of Enlightenment do not ship with a graphical polkit authentication agent. If you want to access privileged actions (e.g. mount a filesystem on a system device), you have to install one and autostart it. For that you should go to Settings Panel > Apps > Startup Applications > System and activate it.

## GNOME Keyring integration
It is possible to use gnome-keyring in Enlightenment. However, at the time of writing, you need a small hack to make it work in full.
First, you must tell Enlightenment to autostart gnome-keyring. For that you should go to Settings Panel > Apps > Startup Applications > System and activate Certificate and Key Storage, GPG Password Agent, SSH Key Agent and "Secret Storage Service".
After this, you should set the following:

{{bc|1=
SSH_AUTH_SOCK=/run/user/${UID}/keyring/ssh
}}

This "hack" is used to override the automatic setting of the variable by "enlightenment-start" from "ssh-agent" to gnome-keyring.

More information on this topic in the GNOME Keyring article.

## System tray
Enlightenment has support for a system tray but it is disabled by default. To enable the system tray, open the Enlightenment main menu, navigate to the Settings submenu and click on the Modules option. Scroll down until you see the Systray option. Highlight that option and click the Load button. Now that the module has been loaded, it can be added to the shelf. Right click on the shelf you wish to add the Systray to, hightlight the Shelf submenu and click on the Contents option. Scroll down until you see Systray. Highlight that option and click the Add button.

## Notifications
Enlightenment provides a notification server through its Notification extension.
* Notifications may be displayed in any corner of the "screen" as defined below
* Available screen policies are Primary Screen, Current Screen, All Screens, and Xinerama
* Notifications may be filtered based on urgency (Low, Normal, or Critical in any combination)
* A default notification timeout may be set and optionally enforced for all notifications
* The notification server may also optionally ignore replace ID requests

## Themes
More themes to customize the look of Enlightenment are available from:
* enlightenment-themes.org
* relighted.c0n.de for the default theme in 200 different colors
* git.enlightenment.org (git clone the theme you like, run 'make' and you end up with a .edj theme file)
* packages.bodhilinux.com has a good collection (you will need to extract the .edj file from the .deb; bsdtar will do this and is part of the base Arch Linux install). A nice catalog can be seen at their wiki.
* exchange.enlightenment.org (archived)

You can install the themes (coming in .edj format) using the theme configuration dialog or by moving them to .

## GTK
To alter the GTK theme, go to Settings > All > Look > Application Theme.

## Modules and Gadgets
;Module:Name used in enlightenment to refer to the "backing" code for a gadget.
;Gadget:Front-end or user interface that should help the end users of Enlightenment do something.

Many Modules provide Gadgets that can be added to your desktop or on a shelf. Some Modules (such as CPUFreq) only provide a single Gadget while others (such as Composite) provide additional features without any gadgets.  Note that certain gadgets such as Systray can only be added to a shelf while others such as Moon can only be loaded on the desktop.

## "Extra" modules
Beyond the modules described here, more "extra" modules are available from .

Scale Windows

The Scale Windows module, which requires compositing to be enabled, adds several features. The scale windows effect shrinks all open windows and brings them all into view. This is known in "Mission Control" in macOS. The scale pager effect zooms out and shows all desktops as a wall, like the compiz expo plugin. Both can be added to the desktop as a gadget or bound to a key binding, mouse binding or screen edge binding.

Some people like to change the standard window selection key binding  to use Scale Windows to select windows.  To change this setting, you navigate to Menu > Settings > Settings Panel > Input > Keys.  From here, you can set any key binding you would like.

To replace the window selection key binding functionality with Scale Windows, scroll through the left panel until you find the ALT section and then find and select .  Then, scroll through the right panel looking for the "Scale Windows" section and choose either Select Next or Select Next (All) depending on whether you would like to see windows from only the current desktop or from all desktops and click Apply to save the binding.

Available from upstream git.

## Default Keybindings
{| class="wikitable"
! Key !! Effect
|-
|
| Maximize vertically
|-
|
| Show "Clients" (windows) Menu
|-
|
| Show "Everything Launcher" (apps, windows, etc.)
|-
|
| Maximize left
|-
|
| Maximize right
|-
|
| Maximize horizontally
|-
|
| Flip to the desktop on the left
|-
|
| Flip to the desktop on the right
|-
|
| Show the desktop
|-
|
| Toggle fullscreen
|-
|
| Toggle iconic mode
|-
|
| Kill window
|-
|
| Invoke the screensaver
|-
|
| Maximize Window
|-
|
| Toggle shade up
|-
|
| Window menu
|-
|
| Close a window
|-
|
| Lower
|-
|
| Raise
|-
|
| Flip to desktop on left
|-
|
| Flip to desktop on right
|-
|
| Show "End session" dialog
|-
|
| Launch the default terminal
|}

## Troubleshooting
If you find some unexpected behavior, there are a few things you can do:
# try to see if the same behavior exists with the default theme
# disable any 3rd party modules you may have installed
# backup  and remove it (e.g. )

If you are sure you found a bug open an issue for the relevant component at https://git.enlightenment.org/.

## Compositing
When the configuration needs to be reset and the settings windows can no longer be approached, configuration for the compositor can be reset using the hardcoded keybinding .

## Unreadable fonts
If fonts are too small and your screen is unreadable, be sure the right font packages are installed.  and  are valid candidates.

You also should consider just increasing the scaling size under the Scaling. You can set scaling under Settings > Settings Panel > Look > Scaling.

## Backlight always dimmed
You may find that Enlightenment routinely dims the backlight to 0% on logout and will only restore it to 100% when you log into another Enlightenment session. Enlightenment assumes that whatever comes after it will set the backlight to whatever it prefers, if anything as this is what Enlightenment does at start. This is especially problematic when using another desktop environment alongside Enlightenment that cannot control backlight as the backlight will not automatically be restored to its normal level when using that desktop environment. To fix this issue, open the Enlightenment Settings Panel and, under the Look tab, click on the Composite option. Tick the Don't fade backlight box and click OK.

## Inconsistent cursor theme
You may find that the cursor theme for the desktop is different to the one used in applications such as Firefox. This is because desktop applications are using X cursor themes whilst Enlightenment has its own set of cursor themes. For consistency, you can set Enlightenment to always use the X cursor theme. To do this, open the Enlightenment Settings Panel and click on the Input tab. Click on the Mouse option. Change the theme from Enlightenment to X and click OK. You should now find that the same cursor theme is used everywhere. If the X cursor theme itself is not always consistent, see Cursor themes#The default cursor theme.

## Background images
You can just select wallpapers in the wallpaper settings dialog and import any image with the provided settings dialog, or you can put desired wallpapers into

LMB anywhere on the desktop will give access to the settings, select

Any new image copied in the  folder will get the list of available backgrounds auto-updated. You can drop animated gifs and even mp4 and other video files in here and use them as wallpapers if you want. Select desired wallpaper from drop-down menu. Inside the appropriate tabs in the global settings, you can adjust things like tiling of the background image, filling screen and such.

## Enlightenment DR16
Enlightenment, Development Release 16 was first released in 2000, and reached version 1.0 in 2009. Originally, the DR16 stood for the 0.16 version of the Enlightenment project. It is still under development today, regularly updated by its maintainer Kim 'kwo' Woelders. With compositing, shadows and transparencies, E16 kept all of the speed that presided over its foundation by original author Carsten "Rasterman" Haitzler but with up to date refinement.

## To install E16
Install .

 provides some additional themes to change the visual look.

See  for in depth documentation.

## Basic Configuration
Most configuration files for E16 reside in  and are text-based, editable at will. That includes the Menus too.

Shortcut keys can be either modified by hand, or with the e16keyedit software provided as source on the sourceforge page of the e16 project. Note that the keyboard shortcuts file is not created in  by default. You can copy the packaged version to your home directory if you wish to make changes:
 $ cp /usr/share/e16/config/bindings.cfg ~/.e16

## Start/Restart/Stop Scripts
Create an Init, a Start and a Stop folder in your  folder: any .sh script found there will either be executed at Startup (from Init folder), at each Restart (from Start folder), or at Shutdown (from Stop folder); provided you allowed it through the MMB / settings / session /  button and made them executable. Typical examples involves starting PulseAudio or your favorite network manager applet.

## Compositor
Shadows, Transparent effects et al can be found in MMB or RMB /Settings, under Composite .
