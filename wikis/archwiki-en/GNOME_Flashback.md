# GNOME/Flashback

GNOME Flashback (previously called GNOME fallback mode) is a shell for GNOME 3. The desktop layout and the underlying technology is similar to GNOME 2. It does not use 3D acceleration at all, so it is generally faster and less CPU intensive than GNOME Shell with llvmpipe.

## Installation
GNOME Flashback can be installed from the  package. It is recommended to install its optional dependencies also to get a more complete desktop environment.

You can also install the following packages which provide some additional applets for the GNOME Panel:
*
*
*

It is recommended to install the  group, which contains applications required for the standard GNOME experience.

## Starting
## Graphical log-in
Choose GNOME Flashback (Metacity) from the menu in a display manager of choice.

Those who wish to use Compiz with GNOME Flashback should select GNOME Flashback (Compiz) instead.

## Manually
* For the GNOME Flashback (Metacity) session, add the following to the  file:

* For the GNOME Flashback (Compiz) session, add the following to the  file:

After editing , GNOME Flashback can be launched with startx. See xinitrc for details.

## Configuration
GNOME Flashback shares most of its settings with GNOME. See  GNOME#Configuration for more details.

## Customizing GNOME Panel
* To configure the panel, hold down the  key, and right-click on it in an empty area.
* To move an applet on the panel, hold down the  key, and grab it with middle-button.

## Alternative window manager
You can use an alternative window manager with GNOME Flashback by creating a custom GNOME session with the following components:

where window-manager is the window manager you wish to use. See GNOME/Tips and tricks#Custom GNOME sessions.

Also see this article on running awesome as the window manager in GNOME.

## Tips and tricks
## Panel speed settings
;Hide/Unhide delay
To adjust the amount of time it takes for the panel to disappear or reappear when autohide is enabled, execute the following:
 $ gsettings set org.gnome.gnome-panel.toplevel:/org/gnome/gnome-panel/layout/toplevels/panel/ hide-delay time
 $ gsettings set org.gnome.gnome-panel.toplevel:/org/gnome/gnome-panel/layout/toplevels/panel/ unhide-delay time
where panel is either top-panel or bottom-panel and time is a value in miliseconds, e.g. 300.

;Animation speed
To set the speed at which panel animations occur, execute the following:
 $ gsettings set org.gnome.gnome-panel.toplevel:/org/gnome/gnome-panel/layout/toplevels/panel/ animation-speed value
where panel is either top-panel or bottom-panel and value is either ,  or .

## Replace applications menu icon
Replace  with your own icon (where  is the name of your icon theme).

After making the change, restart GNOME Panel: .
