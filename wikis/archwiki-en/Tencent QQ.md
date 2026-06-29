# Tencent QQ

QQ is an instant messaging software developed by Tencent, an imitation of ICQ, and a popular IM software in China. This page lists various solutions for Arch Linux using QQ.

## Native Linux version
The official Linux version powered by Electron is already available. To use it, install .

## Bubblewrap version
Alternatively, you can install  instead, which contains bubblewrap sandbox and some tweaks.

* Custom parameters to be passed to bwrap should be written in , you can set custom mount directory in this file.

* Custom parameters to be passed to electron should be written in .

## Virtual machine
You can run a complete Windows system in a virtual machine and run QQ in this. Compared with other schemes, this scheme has the smallest chance of error. The disadvantage is that it takes up more resources.

## Tips and tricks
## HiDPI support
On the HiDPI display, the QQ/TIM interface may be too small. Support for HiDPI has been added to the newer version of QQ/TIM. Just manually adjust Wine's DPI.

Execute , switch to the display tab in the opened window and adjust the DPI.

## Configuration under the tiled window manager
## Awesome
Wine QQ/TM may be out of control under the tiled window manager, and some configuration is required.

The following configuration has these effects:

* Set all TM windows to float.

* Clear unnecessary window borders to prevent the focus from moving to the menu when the menu pops up.

* When using tabbed conversation window, increased use of digital switches Alt+Number shortcut key, need to install xdotool.

* Automatically close the pop-up news window.

Add the following to the Awesome configuration:

 function myfocus_filter(c)
   if awful.client.focus.filter(c) then
     -- This works with tooltips and some popup-menus
     if c.class == 'Wine' and c.above == true then
       return nil
     elseif c.class == 'Wine'
       and c.type == 'dialog'
       and c.skip_taskbar == true
       and c.size_hints.max_width and c.size_hints.max_width < 160
       then
       -- for popup item menus of Photoshop CS5
       return nil
     else
       return c
     end
   end
 end

 awful.rules.rules = {
   -- All clients will match this rule.
   {
     rule = { },
     properties = {
       -- we use our own function
       focus = myfocus_filter,
       -- The following is the default part
       border_width = beautiful.border_width,
       border_color = beautiful.border_normal,
       keys = clientkeys,
       buttons = clientbuttons,
     }
   }, {
     rule_any = {
       instance = {'TM.exe', 'QQ.exe'},
     },
     properties = {
       -- This, together with myfocus_filter, make the popup menus flicker taskbars less
       -- Non-focusable menus may cause TM2013preview1 to not highlight menu
       -- items on hover and crash.
       focusable = true,
       floating = true,
       -- remove the border
       border_width = 0,
     }
   }, {
     -- Other rules
   }
 }

 alt_switch_keys = awful.util.table.join(
     -- it's easier for a vimer to manage this than figuring out a nice way to loop and concat
     awful.key({'Mod1'}, 1, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+1') end),
     awful.key({'Mod1'}, 2, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+2') end),
     awful.key({'Mod1'}, 3, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+3') end),
     awful.key({'Mod1'}, 4, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+4') end),
     awful.key({'Mod1'}, 5, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+5') end),
     awful.key({'Mod1'}, 6, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+6') end),
     awful.key({'Mod1'}, 7, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+7') end),
     awful.key({'Mod1'}, 8, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+8') end),
     awful.key({'Mod1'}, 9, function(c) awful.util.spawn('xdotool key --window ' .. c.window .. ' ctrl+9') end)
 )
 function bind_alt_switch_tab_keys(client)
     client:keys(awful.util.table.join(client:keys(), alt_switch_keys))
 end -- }}}

 client.connect_signal("manage", function (c, startup)
   -- other configuration

   if c.instance == 'TM.exe' then
     -- add Alt+n support
     bind_alt_switch_tab_keys(c)
     -- close all kinds of news notification small windows
     if c.name and c.name:match('^腾讯') and c.above then
       c:kill()
     end
   end

   -- other configuration
 end)

You can also look at the complete Awesome configuration.

## i3
In the native configuration, when  is started, it will be maximized automatically, and the border is not beautiful. The following two rules can be set in the i3  setting to improve:

 for_window floating enable
 for_window [instance="QQ.exe" border none

## Troubleshooting
## Font configuration
If you have problems displaying Chinese, you can try to execute   first.

See also fonts and Font configuration#Applications without Fontconfig support.

## File is occupied
Just kill the process of QQ or TIM.
After exiting QQ/TIM, some related processes are still running in the background. You can also use the following script to start QQ/TIM, it will first find the existing process, kill the process and start a new QQ/TIM.

{{hc|start-tim.sh|
#!/bin/sh
# script to start TIM
# kill TIM before start TIM
for pid in `pgrep TIM.exe`; do
	if [ -n ${pid} ]; then
		kill ${pid}
	fi
done
# start TIM
wine '~/.wine/drive_c/Program Files/Tencent/TIM/Bin/TIM.exe'
}}

The above example is applicable to TIM, and can be applied to QQ after a little modification.

## Unable to input emoticons under xfce4 (xfwm4)
Open the Settings Manager-Window manager tuning-focus, uncheck the ICCCM focus prompt to activate focus anti-theft and follow the standard.

The reason is that incompatibility occurs when the emoji window gains focus.

## Cannot enter Chinese under non-Chinese locale
Modify the  of the  file, which is usually located in , but must be copied to  in order to not get overwritten.

Add  to the  line.
For example, the original  was:

 Exec=".wine/drive_c/Program Files/QQ/Bin/QQ.exe"

Should be changed to:

 Exec=env LC_ALL=zh_CN.UTF-8 wine ".wine/drive_c/Program Files/QQ/Bin/QQ.exe"

## Cannot enter Chinese when the IME is activated (the Electron version)
Old electron version doesn't work with IBus IME well, see Electron issue with IBus IME.

You can launch QQ with an environment variable:
 GTK_IM_MODULE=xim qq

## Screen flicker when using a monitor with high refresh rate
See Chromium#Chromium rendering at 60 FPS despite using a display with a higher refresh rate.

## Hot updates of the native Linux version
The native Linux version of QQ sometimes notifies the user to download hot updates. These updates are downloaded to , and can be applied quickly with a restart of the application. However, this mechanism frequently runs into issues on Arch Linux.

## Empty login page after a hot update
If QQ shows an empty login page after a hot update, remove  and restart QQ. If it doesn't help, try #Rolling back from a hot update

## Rolling back from a hot update
If you want to roll back from a hot update version for any reason, add the current version to  in  and change  to the last good version, and then restart QQ. Next time, QQ will launch with the version specified in , and will not ask for updates in .
