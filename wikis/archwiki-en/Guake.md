# Guake

Guake is a top-down terminal for GNOME (in the style of Yakuake for KDE, Tilda or the terminal used in Quake).

## Installation
Install the  package.

## Usage
Once installed, you can start Guake from the terminal with:

 $ guake

After guake has started you can right click on the interface and select Preferences to change the hotkey to drop the terminal automatically, by default it is set to .

## Autostartup
You may want Guake to load on starting up Desktop Environment. To do this, you need to
 # cp /usr/share/applications/guake.desktop /etc/xdg/autostart/

See Autostarting for more info.

## Guake scripting
Like Yakuake, Guake allows to control itself at runtime by sending the D-Bus messages. Thus it can be used to start Guake in a user defined session. You can create tabs, assign names for them and also ask to run any specific command in any opened tab or just to show/hide Guake window, manually in a terminal or by creating a custom script for it.

Example of such a script is given below this section.

You can use guake executable itself to send D-Bus messages. Here is the list of available options you may be interested in:

* ,  — toggle the visibility of the terminal window. Actually, you can just type , and it will toggle the visibility of already running instance.
* ,  — put Guake to fullscreen mode.
*  — show Guake main window.
*  — hide Guake main window.
* ,  — create new tab and select it. Value of  used to set a current directory for the tab, if specified.
* ,  — select tab with index . Tab indexes are started with 0.
* ,  — print index of currently selected tab.
* ,  — execute an arbitrary command  in the selected tab.
* ,  — used with  to specify index  of a tab to rename. Default value is 0.
*  — set the tab name to . You can reset tab title to default value by passing a single dash (). Use  option to specify which tab to rename.
*  — set the hexadecimal () background color  of the selected tab.
*  — set the hexadecimal () foreground color  of the selected tab.
* ,  — same as , but renames the currently selected tab.
* ,  — shutdown running Guake instance.

Multiple options may be combined in a single call. If there is no guake instance running, all of the options specified will be applied to the newly created instance.

To display list of all available options, type .

There are 2 ways of starting guake while applying these scripts
* copying the below example into a file like  making it executable and running that file instead of guake
* right clicking on  and adding the path to the  script in the "On start:" field while making certain to comment out  and  from the script below

The second option is preferable if you want the script to run regardless of how guake is started and you can still instruct guake not to run the script with  if needed.

Example:

Notice than we should wait some time calling sleep to avoid race conditions between running instances.

## Troubleshooting
## Floating mode in window managers
Guake may not open in floating mode with some window managers. This can be resolved by using Guake's window class string ( or  per ). For example, see "WM_CLASS" in i3#Correct handling of floating dialogs for i3.

## Toggling Guake visibility does not work (Wayland)
If you are using Wayland, the Guake visibility toggle hotkey may not work under some applications. This is because Guake uses a global hotkey library made for X environments and there is no equivalent global hotkey interface for Wayland. Many applications (e.g. Firefox) run on Wayland through Xwayland where the Guake toggle will work but others that natively run Wayland (e.g. GNOME applications) disable Guake toggle functionality.

If you do not wish to switch over to an X environment, a simple workaround requires configuring a shortcut with your window manager/desktop environment for the command .

See github issue for more details.

## Guake is blurry on Wayland
If you are using a Wayland desktop environment with fractional scaling guake might be blurry. If this is the case it is likely because your desktop environment is upscaling guake for you. Guake does not respect the  environment variable. Instead, to make guake use Wayland set the  environment variable.
