# Awesome

From the awesome website:

:awesome is a highly configurable, next generation framework window manager for Xorg. It is very fast and extensible It is primarily targeted at power users, developers and any people dealing with every day computing tasks and who want to have fine-grained control on its graphical environment.

## Installation
Install the  package.

## Starting
Run  with xinit. To use the included xsession file, see Display manager.

## With GNOME
You can set up GNOME to use awesome as the visual interface, but have GNOME work in the background. See .

## XFCE
See Xfce#Use a different window manager.

## Configuration
The lua based configuration file is at .

## Creating the configuration file
First, run the following to create the directory needed in the next step:

 $ mkdir -p ~/.config/awesome/

Whenever compiled, awesome will attempt to use whatever custom settings are contained in ~/.config/awesome/rc.lua. This file is not created by default, so we must copy the template file first:

 $ cp /etc/xdg/awesome/rc.lua ~/.config/awesome/

The API for the configuration often changes when awesome updates. So, remember to repeat the command above when you get something strange with awesome, or you want to modify the configuration.

For more information about configuring awesome, check out the [https://awesomewm.org/apidoc/documentation/90-FAQ.md.html#Configuration configuration section at awesome docs

## Examples
Some good examples of rc.lua would be as follows:

* Awesome screenshot thread
* Setkeh's Awesome Configuration
* User configuration that supports different themes, including a status bar
* Awesome configuration with two modern themes

## Extensions
Several extensions are available for awesome:

{| class="wikitable"
! Extension
! Functionality
! Version
|-
|
* Revelation
| Bring up a view of all opened clients
| Awesome 3.5+
|-
|
* Shifty
| Dynamic tagging
| Awesome 3.5
|-
|
* Naughty
| Pop-up notifications
| Awesome 3.5+
|-
|
* Vicious
* Obvious
* Bashets
| Additional widgets
| Awesome 3.5
|-
|}

## Autostart
To implement the XDG Autostart specification, install  and  and add the following lines to :

{{hc|~/.config/awesome/rc.lua|
awful.spawn.with_shell(
    'if (xrdb -query | grep -q "^awesome\\.started:\\s*true$"); then exit; fi;' ..
    'xrdb -merge /dev/null'", false) end),

This function saves screenshots inside , edit as needed.

## Removing window gaps
As of awesome 3.4, it is possible to remove the small gaps between windows; in the awful.rules.rules table there is a properties section, add to it

  size_hints_honor = false

## Transparency
See composite manager.

In awesome 3.5, window transparency can be set dynamically using signals. For example,  could contain the following:

 client.connect_signal("focus", function(c)
                               c.border_color = beautiful.border_focus
                               c.opacity = 1
                            end)
 client.connect_signal("unfocus", function(c)
                                 c.border_color = beautiful.border_normal
                                 c.opacity = 0.7
                              end)

## Conky
If using conky, you must set it to create its own window instead of using the desktop. To do so, edit  to contain

 own_window yes
 own_window_transparent yes
 own_window_type desktop

Otherwise strange behavior may be observed, such as all windows becoming fully transparent. Note also that since conky will be creating a transparent window on your desktop, any actions defined in awesome's  for the desktop will not work where conky is.

## wiboxes
There is built-in pseudo-transparency for wiboxes. To enable it, append 2 hexadecimal digits to the colors in your theme file (e.g. , which is usually a copy of ), like shown here:

 theme.bg_normal = "#000000AA"

where "AA" is the transparency value.

To change transparency for the actual selected window by pressing  you can also use  and the following modification to your :

 globalkeys = gears.table.join(
     -- your keybindings
     awful.key({ modkey }, "Next", function (c)
         awful.util.spawn("transset-df --actual --inc 0.1")
     end),
     awful.key({ modkey }, "Prior", function (c)
         awful.util.spawn("transset-df --actual --dec 0.1")
     end),
     -- Your other key bindings
     [...
 )

## Widget spacing
The default  places widgets including keyboard layout and clock in a wibox with little spacing. It is possible to add extra spacing between widgets using the  property:

        { -- Right widgets
        layout = wibox.layout.fixed.horizontal,
        spacing = 10,
        mykeyboardlayout,
        ...

## ImageMagick
You may have problems if you set your wallpaper with imagemagick's display command. It does not work well with xcompmgr. Please note that awsetbg may be using display if it does not have any other options. Installing habak, feh, hsetroot or whatever should fix the problem (grep -A 1 wpsetters /usr/bin/awsetbg to see your options).

## Passing content to widgets with awesome-client
You can easily send text to an awesome widget. Just create a new widget:

 mywidget = widget({ type = "textbox", name = "mywidget" })
 mywidget.text = "initial text"

To update the text from an external source, use awesome-client:

 echo -e 'mywidget.text = "new text"' | awesome-client

Do not forget to add the widget to your wibox.

## Using a different panel with awesome
If you like awesome's lightweightness and functionality but do not like the way its default panel looks, you can install a different panel, for example .

Then add it to the autorun section of your . You may also comment out the section which creates wiboxes for each screen (starting from {{ic|1=mywibox= awful.wibox({ position = "top", screen = s })}}) but it is not necessary. Do not forget to check your  for errors by typing:

 $ awesome -k rc.lua

You should also change your  keybinding, in order to start some other application launcher instead of built in awesome. See List of applications/Other#Application launchers for  examples. Do not forget to add:

{{bc|
      properties = { floating = true } },
    { rule = { instance = "$yourapplicationlauncher" },
}}

to your .

## Application directories in menubar
 includes [https://awesomewm.org/apidoc/popups_and_bars/menubar.html menubar. By default, pressing  will open a dmenu-like applications menu at the top of the screen. This menu searches for  files in  and .

You can extend or replace these directories by modifying :

Note that the  files are re-read each time awesome starts, thereby slowing down the startup. If you prefer other means of launching programs, the menubar can be disabled in   by removing  and other references to the  variable.

## Pop-up menus
There is a simple menu by default since awesome 3, simplifying custom menus. If you want a freedesktop.org menu, you could take a look at [https://github.com/copycat-killer/awesome-freedesktop awesome-freedesktop.

If you prefer to use an external applications menu when you click on the Awesome icon, or right-click on an empty area of the desktop, you can follow the instructions in Xdg-menu#Awesome. However this menu is not updated when you add or remove programs. So, be sure to run the command to update your menu. It may look something like:

 $ xdg_menu --format awesome --root-menu /etc/xdg/menus/arch-applications.menu >~/.config/awesome/archmenu.lua

## Titlebars
It is easy to enable titlebars in awesome by simply setting the variable titlebars_enabled to true in the configuration file. （in rules area）

    { rule_any = {type = { "normal", "dialog" }
      }, properties = { titlebars_enabled = true }
    },

However, you may want to be able to toggle the titlebar on or off. You can do this by simply adding something like this to your key bindings: (in clientkeys of  Key bindings. And do not put the code to the end of the clientkeys area)

    -- working toggle titlebar
    awful.key({ modkey, "Control" }, "t", function (c) awful.titlebar.toggle(c)         end,
              {description = "Show/Hide Titlebars", group="client"}),

Then you may want to initially hide the titlebars. To do that just add this immediately after the title bar is created (inside the  signal handler):

 awful.titlebar.hide(c)

## Battery notification
See this blog post for a simple battery notification to add to . Note that it needs naughty for the notifications (installed by default in version 3.5). Other examples are available at awesome wiki.

## Media Controls
It is possible to control both volume and media playback via a combination of  (available via the  package) and . The following can be added to the relevant key binding section of your rc.lua configuration file:

    -- Volume Keys
    awful.key({}, "XF86AudioLowerVolume", function ()
      awful.util.spawn("amixer -q -D pulse sset Master 5%-", false) end),
    awful.key({}, "XF86AudioRaiseVolume", function ()
      awful.util.spawn("amixer -q -D pulse sset Master 5%+", false) end),
    awful.key({}, "XF86AudioMute", function ()
      awful.util.spawn("amixer -D pulse set Master 1+ toggle", false) end),
    -- Media Keys
    awful.key({}, "XF86AudioPlay", function()
      awful.util.spawn("playerctl play-pause", false) end),
    awful.key({}, "XF86AudioNext", function()
      awful.util.spawn("playerctl next", false) end),
    awful.key({}, "XF86AudioPrev", function()
      awful.util.spawn("playerctl previous", false) end),

## Steam Keyboard
The on screen Steam Keyboard that can be activated by the Steam Controller appears to freeze after trying to type one character. This is because the client that is supposed to receive the input has to be focused to receive it and the keyboard will wait until this input is successfully send. Manually focusing another client will send the input to this client and unfreeze the keyboard again until the next character is entered.

The trick to getting the keyboard to work correctly is to prevent it ever receiving focus. Add the following signal to your configuration (or merge with an existing client focus signal):

 client.connect_signal("focus", function(c)
     if awful.rules.match(c, { name = "^Steam Keyboard$" }) then
         awful.client.focus.history.previous()
     end
 end)

This will return the focus to the last client whenever the keyboard receives focus. As the input to the keyboard is handled by the Steam client and as such does not need focus, inputting text will now work correctly.

## Troubleshooting
## Debugging rc.lua
Xephyr allows you to run X nested in another X's client window. This allows you to debug  without breaking your current desktop. Start by copying  into a new file (e.g. ), and modify it as needed. Then run new instance of awesome in Xephyr, supplying  as a configuration file like this:

 $ Xephyr :1 -ac -br -noreset -screen 1152x720 &
 $ DISPLAY=:1.0 awesome -c ~/.config/awesome/rc.lua.new

The advantage of this approach is that if you introduce bugs you do not break your current awesome desktop, potentially crashing X applications and losing work. Once you are happy with the new configuration, copy  to  and restart awesome.

## Automatic reload
In addition to the method above, you can use  in order to automatically reload the Awesome instance inside Xephyr when updating any configuration file inside the  directory:
 #!/usr/bin/env bash

 Xephyr :1 -ac -br -noreset -screen 1920x1080 -dpi 96 &
 sleep 1
 DISPLAY=:1.0 awesome -c ~/.config/awesome/rc.lua.new &
 instance=$!

 while inotifywait -r -e close_write ~/.config/awesome; do
 	kill -s SIGHUP $instance
 done

## awmtt
 (Awesome WM Testing Tool) is an easy to use wrapper script around Xephyr. By default, it will use . If it cannot find that test file, it will use your actual . You can also specify the location of the configuration file you want to test:

 $ awmtt start -C ~/.config/awesome/rc.lua.new

When you are done testing, close the window with:

 $ awmtt stop

Or immediately see the changes you are doing to the configuration file by issuing:

 $ awmtt restart

## aawmtt
 (Another Awesome WM Testing Tool) is an alternative implementation of , which includes Live-Reload by default.
It is similar to awmtt-ng, but includes some fixes for the XOrg Display detection which does not work on some machines with awmtt-ng.
It differs from awmtt in that it does not try to run a test file first, but just runs the default config.

To simply open a Xephyr window with awesome loaded, run:

 $ aawmtt

The output of awesome will now be printed to your terminal and upon changing any files in your configuration folder, awesomewm will be reloaded.

In case you want to modify the directory that is watched for file changes, or the location of your configuration file, simply run:

 $ aawmtt --config "location_of_config_file" --watch "directory_to_watch_for_changes"

The directory that is watched for changes defaults to the parent directory of your config file, so by default it would be "~/.config/awesome".

## Log Files
If you are using LightDM, awesome will log errors to `$HOME/.xsession-errors`. If you use  to start awesome, the entry "Where are logs, error messages or something?" in the FAQ may be a helpful resource.

## Mod4 key
Awesome recommends to remap , which by default should be the  or "Windows" key. If for some reason it is not mapped to , use xmodmap to find out what is.  To change the mapping, use  to find the keycode and name of the key to be mapped.  Then add something like the following to

 xmodmap -e "keycode 115 = Super_L" -e "add mod4 = Super_L"
 exec awesome

The problem in this case is that some xorg installations recognize keycode 115, but incorrectly as the 'Select' key. The above command explictly remaps keycode 115 to the correct 'Super_L' key.

To remap  with  (conflict with ) see:

 tail -50 /usr/share/X11/xkb/rules/evdev

To set the caps lock key as  add the following to :

 setxkbmap -option caps:hyper

## Fix Java (GUI appears gray only)
See Java#Gray window, applications not resizing with WM, menus immediately closing and === Eclipse: cannot resize/move main window ===

If you get stuck and cannot move or resize the main window (using mod4 + left/right mouse button) edit the  and set fullscreen/maximized to false (if set) and reduce the width and height to numbers smaller than your single screen desktop area.

 can be found in . Edit the line:

 , nil, function () awful.spawn("scrot -s") end)

Note that  is passed to the  argument of . Instead, the callback function is passed as fourth argument, which is the argument named .

## YouTube: fullscreen appears in background
If YouTube videos appear underneath your web browser when in fullscreen mode, or underneath the panel with controls hidden, add this to

 { rule = { instance = "plugin-container" },
   properties = { floating = true } },

With Chromium add

 { rule = { instance = "exe" },
   properties = { floating = true } },

or:

 { rule = { role = "_NET_WM_STATE_FULLSCREEN" },
   properties = { floating = true } },

See [https://bbs.archlinux.org/viewtopic.php?pid=1085494#p1085494.

## Prevent the mouse scroll wheel from changing tags
In your , change the Mouse Bindings section to the following:

 -- {{{ Mouse bindings
 root.buttons(gears.table.join(
     awful.button({ }, 3, function () mymainmenu:toggle() end)
 ))
 -- }}}

## Duplicate menu-entries generated by Xdg-menu
Xdg-menu will generate duplicate entries if you copy desktop-files from /usr/share/applications to ~/.local/share/applications even though it might be preferable to simply override the originals, for example using a different theme for a specific application. One solution to the problem is to filter the generated output trough awk to remove entries with a name identical to the previous entry.

  xdg_menu --format awesome --root-menu /etc/xdg/menus/arch-applications.menu | awk -F, '{if (a!=$1) print $a; a=$1}' >~/.config/awesome/archmenu.lua

## Some Shortcuts not Working in Xfce4 overlapping Keys
Check your
 $ xfce4-keyboard-settings

for Overlapping keys like "Super L" or Key Combinations which should be run by Awesome

## Memory leaks
Some users experience memory leaks even without activity. When using a lot of widgets leaks can occur at a rate up to 5 MB/min. To mitigate this you can enforce more frequent garbage collection by adding this to your :

 -- Run garbage collector regularly to prevent memory leaks
 gears.timer {
        timeout = 30,
        autostart = true,
        callback = function() collectgarbage() end
 }
