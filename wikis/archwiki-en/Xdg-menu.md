# Xdg-menu

xdg-menu is a tool that generates XDG Desktop Menus for the following window managers:

* awesome
* Blackbox
* Fluxbox
* FVWM
* IceWM
* JWM
* Openbox
* PekWM
* twm
* Window Maker

KDE, GNOME, Xfce and Enlightenment are already XDG compatible.

## Installation
Install the  package.

## Menu hierarchy
* Applications
** Accessibility
** Accessories
** Development
** Education
** Games
** Graphics
** Internet
** Multimedia
** Office
** Other
** Science
** Settings
** System

## Configuration
xdg_menu relies on three sets of information to generate menus: a root menu or in other words an XML menu template generally passed on the command line, information cached when it was last run, and a series of configuration files.

* You can find some XML menu templates in .
* If altering the code in xdg_menu to change layout, make sure you delete everything in  or you will spend hours trying to figure out why your changes to the perl script do not take.
* You can find individual application configurations in .

Other configuration file directories can be found under . In most cases you will not need to touch these. However if you want to change how your menu is layed out you can alter the menu template for minor changes. Major changes require tweaking the actual xdg_menu perl script. If you find that applications do not appear or that they are called strange things, then you will need to look at the .desktop file in . Check the desktop entry specification.

## Adding desktop entries from other directories
By default, the Xdg-menu will be populated with applications which install their desktop entries to . To add applications to the menu which install their desktop entry to a user folder such as , edit the  file and add an  tag for the relevant directory, see below:

## Usage
## xdg_menu
## update-menus
update-menus updates WM's menus from XDG data and can be configured to do it automaticaly.

This is a script wrapper around xdg_menu that relies on

To use it, you need to install the  package (xdg_menu)

In , you have to select from a list of window managers for which the menu should be generated. Comments with # are allowed.

All generated menus are placed in . See wm-specific #Examples section of this page to get more information.

## Examples
## Awesome
## With xdg_menu
Generate the menu:

 $ xdg_menu --format awesome > ~/.config/awesome/xdg_menu.lua

Then, edit file  as shown below.

* Add a require statement for your new  file.
* Add an entry to your  object for your new menu which calls .

{{bc|1=
...
xdg_menu = require("xdg_menu")
...

...
mymainmenu = awful.menu({ items = { { "awesome", myawesomemenu, beautiful.awesome_icon },
                                    { "Applications", xdgmenu },
                                    { "open terminal", terminal }
                                  }
                        })
...
}}

## Blackbox
## With xdg_menu
Generate the menu:

 $ xdg_menu --format blackbox > ~/.blackbox/xdg_menu

Change file  to include the generated menu. For example, add this line:

 (xdg_menu)

## With update-menus
* Uncomment blackbox in .
* Run  as root.
* Change file  to include the generated menu:

 [include (/var/cache/xdg-menu/blackbox/boxrc)

## Fluxbox
## With xdg_menu
Generate the menu:

 $ xdg_menu --format fluxbox > ~/.fluxbox/xdg_menu

Change file  to include the generated menu. For example, add this line:

 (xdg_menu)

## With update-menus
* Uncomment fluxbox in .
* Run  as root.
* Change file  to include generated menu:

 [include (/var/cache/xdg-menu/fluxbox/boxrc)

## Fvwm
## With xdg_menu
Change file  to read the generated menu and add it into the root menu:

## With update-menus
* Uncomment fvwm2 in .
* Run  as root.
* Change file  to read the generated menu and add it into the root menu:

## IceWM
## With xdg_menu
Add the following line to :

 includeprog xdg_menu --format icewm

Or just run the following command to add below the Programs menu:

 $ xdg_menu --format icewm >> ~/.icewm/programs

## With update-menus
* Uncomment icewm in .
* Run  as root.
* Add the following line to :

 include "/var/cache/xdg-menu/icewm/programs"

Or just make a symlink to  in  to add below the Programs menu.

## JWM
## With xdg_menu
Add the following line below the  element in :

 exec: xdg_menu --format jwm --fullmenu

## With update-menus
* Uncomment jwm in .
* Run  as root.
* Add the following line below the  element in :

 /var/cache/xdg-menu/jwm/menu.xml

## Openbox
Using xdg_open as a pipe menu gives you the added benefit of having a menu that automatically updates when you install new applications.

Add the following line below the  element in :

A very basic example:

## With update-menus
* Uncomment openbox in .
* Run  as root.
* Add the following line below the  element in :

## PekWM
## With xdg_menu
Add the following line below the  element in :

 Entry = "" { Actions = "Dynamic /usr/bin/xdg_menu --format pekwm-dynamic" }

## With update-menus
* Uncomment pekwm in .
* Run  as root.
* Add the following line below the  element in :

 INCLUDE = "/var/cache/xdg-menu/pekwm/menu"

## twm
## With xdg_menu
Use:

 $ xdg_menu --format twm > my-twm-menu

And add it into  manually. In the case of twm derivatives with m4 preprocessing such as vtwm or ctwm it can be included by adding:

{{bc|
sinclude(`/PATH/TO/my-twm-menu')
...
menu "defops"
{
...
    "Applications"  f.menu "Applications"
...
}
}}

To .

## With update-menus
* Uncomment twm in .
* Copy  to  and specify applications menu in  menu:
{{bc|
menu "defops"
{
...
    "Applications"  f.menu "Applications"
...
}
}}
* Run  as root.
* Run .

## Window Maker
## With xdg_menu
Add the following line to :

 ("Applications", OPEN_MENU, "| xdg_menu --format WindowMaker"),

## With update-menus
* Uncomment WindowMaker in .
* Run  as root.
* Add the following line to :

 ("Applications", OPEN_MENU, "/var/cache/xdg-menu/WindowMaker/wmrc"),
