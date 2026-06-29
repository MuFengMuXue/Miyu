**Resources**

[[]][Home](https://www.all-day-breakfast.com/wm2/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Wm2 "wikipedia:Wm2")

**wm2** is a minimalist [window manager](https://wiki.gentoo.org/wiki/Window_manager "Window manager") for [X11](https://wiki.gentoo.org/wiki/X11 "X11"). It provides an unusual style of window decoration and as little functionality as its author feels comfortable with in a window manager.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Starting]](#Starting)
-   [[3] [Usage]](#Usage)

## [Installation]

### [Emerge]

Install [[[x11-wm/wm2]](https://packages.gentoo.org/packages/x11-wm/wm2)[]]:

`root `[`#`]`emerge --ask x11-wm/wm2`

### [Additional software]

Other handy accessories are [[[x11-misc/xbindkeys]](https://packages.gentoo.org/packages/x11-misc/xbindkeys)[]] and [[[x11-misc/dmenu]](https://packages.gentoo.org/packages/x11-misc/dmenu)[]].

## [Configuration]

All changes are made by editing /etc/wm2.conf and rebuilding. From the *wm2* [man page](https://wiki.gentoo.org/wiki/Man_page "Man page"): \"wm2 is not configurable, except by editing the source and recompiling the code, and is really intended for people who don\'t particularly want their window manager to be too friendly\".

### [Starting]

To start wm2 you can use a [display manager](https://wiki.gentoo.org/wiki/Display_manager "Display manager") or [[startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide")].

If want to use [[startx](https://wiki.gentoo.org/wiki/Xorg/Guide#Using_startx "Xorg/Guide")] and want [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind") support, setup elogind and create the following file:

[FILE] **`~/.xinitrc`**

    exec dbus-launch --sh-syntax --exit-with-session wm2

## [Usage]

When you start wm2, you see only a black screen. If you installed and configured xbindkeys, you can use the key combination you defined to start a terminal. You can also left-click on the wm2 desktop for a \"menu\" \-- if there are no minimized windows, the only menu item is \"new\" \-- this starts a new terminal (xterm by default, but this can be changed). If there are minimized windows, they will also be listed in this menu; you can return them to their original size by clicking on the menu.

wm2 (like FLWM) uses \"sideways\" or vertical titlebars. wm2 is one of the \"influences\" for FLWM. Left-click on the titlebar or window frame brings the window to the top of the stack. Left-click and drag on the titlebar moves the window. Windows can only be resized by left-click and drag on their lower-right corner. Right-click on the titlebar moves a window to the bottom of the stack. The mouse pointer automatically moves to the titlebar on the next activated window, so repeated right clicks on the titlebar will cycle through the stack, no matter what position windows occupy on the desktop. Clicking on the (only) button on the title bar minimizes (hides) the window. Windows close when you close the application running in them, or you can force a window closed by left-click and hold on the titlebar button for at least 1.5 seconds (until the cursor changes to a cross) and then release. The man page says this about this process: \"I know, it\'s not very easy. On the other hand, things like Windows95 tend to obscure the fact that most windows have a perfectly good close option.\"

The default focus mode is \"sloppy\" \-- moving the mouse pointer into a window gives the window focus but does not bring it to the top of the stack. You must explicity click the title bar to change stack position.

To exit wm2 you can kill the process, or move the mouse pointer to the extreme lower right corner of the screen and left-click. The menu will appear with an \"exit wm2\" option on it. Selecting this option closes wm2.

wm2 does work with conky and feh (or nitrogen) but not with any panels I tried.