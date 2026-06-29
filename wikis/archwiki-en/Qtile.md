# Qtile

From the project's website:
:Qtile is a full-featured, hackable tiling window manager written in Python. Qtile is simple, small, and extensible. It is easy to write your own layouts, widgets, and built-in commands. It is written and configured entirely in Python, which means you can leverage the full power and flexibility of the language to make it fit your needs.

## Installation
Install  the  package.

## Starting
## Xorg
To run Qtile as an X11 window manager, run  with xinit.

## Wayland
Start Qtile as a Wayland compositor by running .

For the status of the Wayland development progress of Qtile, see https://github.com/qtile/qtile/discussions/2409.

## Configuration
As described in Configuration Lookup (or in the alternate documentation), Qtile provides a default configuration file at  that will be used in absence of user-defined ones.

The default configuration includes the shortcut  to open a new terminal (selected from a hardcoded list), and  to quit Qtile.

The most recent default configuration file can be downloaded from the git repository at libqtile/resources/default_config.py.

Several more complete configuration file examples can be found in the qtile-examples repository.

The configuration is fully done in Python: for a very quick introduction to the language you can read this tutorial.

Before restarting Qtile you can test your configuration file for syntax errors using the command:

 $ python -m py_compile ~/.config/qtile/config.py

If the command gives no output, your script is correct.

Alternatively, the command:

 $ qtile check

will perform a syntax check followed by additional type checking.

## Groups
In Qtile, the workspaces (or views) are called Groups. They can be defined as following:

## Group rules
The following example shows how you can automatically move applications to workspaces based on properties such as title and wm_class. You might want to use xprop if you are running on X to get these.

{{bc|1=
from libqtile.config import Group, Match
...
def is_text_editor(window):
    result = "neovim" in (window.name or "").lower()
    return result

def is_terminal(window):
    result = "kitty" in (window.name or "").lower() and not is_text_editor(window)
    return result
...
groups = [
    Group(name=str(idx), **group)
    for idx, group in enumerate(
        [
            {
                "label": "term",
                # restrict layouts since tiling is handled by kitty
                "layouts": "matches": [
                    Match(func=is_terminal),
                ,
            },
            {
                "label": "browser",
                "matches": [
                    Match(role="browser"),
                ],
            },
            {
                "label": "music",
                "matches": [
                    Match(title="YouTube Music"),
                ],
            },
            {"label": "text editor", "matches": {"label": "other"},
        ,
        start=1,
    )
]
...
}}

## Keys
You can configure your shortcuts with the Key class.
Here is an example of the shortcut  to quit the window manager.

You can find out which  corresponds to which key with the command Xmodmap.

## Sound
You can add shortcuts to easily control the sound volume and state by adding a user to the audio group and using the  command-line interface, which can be installed through the  package.

## Language
You can add shortcuts to easily switch between keyboard layouts in different languages using setxkbmap for example :

## Screens
Create one Screen class for every monitor you have. The bars of Qtile are configured in the Screen class as in the following example:

## Bars and widgets
You can find a list of all the built-in widgets in the official documentation (or in the alternate documentation).

If you want to add a widget to your bar, just add it like in the example above (for the  widget). For example, if we want
to add a battery notification, we can use the  widget:

## Using Polybar as the main bar
To use Polybar instead of the default bar, you need to delete contents of the screen class:

To restart Polybar with Qtile, add Polybar's launching script with  command to restart Key in #Keys class, for example:

## Autostart
You can autostart applications using hooks, specifically the  hook. For a list of available hooks see the documentation (or the alternate documentation).

Here is an example where an application starts only once:

## Debugging
Qtile writes its log into

## xinit
Starting Qtile on a different virtual screen can help diagnosing issues:

 $ echo "exec qtile start" > /tmp/.start_qtile; xinit /tmp/.start_qtile -- :2

## Xephyr
Qtile provides a Xephyr development script that can be easily modified to instantiate a system-installed package by replacing:

 env DISPLAY=${XDISPLAY} QTILE_XEPHYR=1 ${PYTHON} "${HERE}"/../bin/qtile start -l ${LOG_LEVEL} $@ &

with

 env DISPLAY=${XDISPLAY} QTILE_XEPHYR=1 qtile start -l ${LOG_LEVEL} $@ &
## Tips and tricks
## Automatically migrate configuration
You can create a pacman hook that uses qtile migrate to check for any breaking changes in your configuration after a Qtile upgrade. Requires you have , and  installed.
 Operation = Upgrade

 Type = Package
 Target = qtile

 [Action
 Description = Migrate Qtile configuration in case of breaking changes
 When = PostTransaction
 Depends = qtile
 #--yes will always say yes to any migrations remove it if you don't want that
 Exec = /bin/sh -c "/usr/bin/qtile migrate --yes"
