# Cwc

CwC is:

: an extensible Wayland compositor with dynamic window management based on wlroots. Highly influenced by Awesome window manager, CwC uses Lua for its configuration and C plugins for extensions.

## Installation
Install the  package.

## Starting
Select cwc from the menu in a display manager of choice.

## LXQT
LXQt#Wayland Session

## Configuration
System-wide CwC configuration files are in  while user configuration files are in :

*  — the main CwC resource configuration file.
*  — CwC keybindings
*  — where to launch startup apps

## Creating the configuration file
First, run the following to create the directory needed in the next step:

 $ mkdir -p ~/.config/cwc/

Whenever started, CwC will attempt to use whatever custom settings are contained in . Then fall back to  This file is not created by default, so we must copy the template file first:

 $ cp /usr/share/cwc/defconfig/* ~/.config/cwc/

## Autostart
Autostarting is done by

 ~/.config/cwc/oneshot.lua

for example:

 cwc.spawn_with_shell("swaybg --output '*' --color '#222222'")

## Wallpaper
You can use a wallpaper setter such as feh or .

## Tips and tricks
## Screenshot
See Keyboard input to ensure the  button is assigned correctly. Then install a screen capturing program such as flameshot

Add to the  array:

 kbd.bind({ MODKEY }, "Print", function()
    cwc.spawn_with_shell("flameshot full")

## Removing window gaps
it is possible to remove the small gaps between windows; in the screen/tag config table there is a properties section, add to it:

 cwc.screen.set_useless_gaps(3)

## Media controls
It is possible to control both volume and media playback via a combination of  (available via the  package) and . The following can be added to the relevant key binding section of your rc.lua configuration file:

   ------------ Audio Media Keys
    kbd.bind({}, "XF86AudioLowerVolume", function()
        local cmd = string.format("pactl set-sink-volume @DEFAULT_SINK@ %s%%", "-3")
        cwc.spawn_with_shell(cmd)
    end, { exclusive = true, repeated = true })
    kbd.bind({}, "XF86AudioRaiseVolume", function()
        local cmd = string.format("pactl set-sink-volume @DEFAULT_SINK@ %s%%", "+3")
        cwc.spawn_with_shell(cmd)
    end, { exclusive = true, repeated = true })
    kbd.bind({}, "XF86AudioMute", function()
        cwc.spawn_with_shell("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    end, { exclusive = true })
    kbd.bind({}, "XF86AudioMicMute", function()
        cwc.spawn_with_shell("pactl set-source-mute @DEFAULT_SOURCE@ toggle")
    end, { exclusive = true })

    -------------- Media Player Keys
    kbd.bind({}, "XF86AudioPlay", function()
        cwc.spawn_with_shell("playerctl play-pause")
    end, { exclusive = true })
    kbd.bind({}, "XF86AudioNext", function()
        cwc.spawn_with_shell("playerctl next")
    end, { exclusive = true })
    kbd.bind({}, "XF86AudioPrev", function()
        cwc.spawn_with_shell("playerctl previous")
    end, { exclusive = true })
    kbd.bind({}, "XF86AudioStop", function()
        cwc.spawn_with_shell("playerctl stop")
    end, { exclusive = true })
    kbd.bind({}, "XF86AudioRewind", function()
        cwc.spawn_with_shell("playerctl position 5-")
    end, { exclusive = true })
    kbd.bind({}, "XF86AudioForward", function()
        cwc.spawn_with_shell("playerctl position 5+")
    end, { exclusive = true })

## Waybar
To use cwc with waybar you will need to load the plugin:

Then follow the dwl waybar page

## Troubleshooting
## Java GUI appears gray
See Java#Gray window, applications not resizing with WM, menus immediately closing and https://bbs.archlinux.org/viewtopic.php?pid=450870.
