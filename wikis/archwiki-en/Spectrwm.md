# Spectrwm

From spectrwm website:

:spectrwm is a small dynamic tiling window manager for Xorg. It tries to stay out of the way so that valuable screen real estate can be used for much more important stuff. It has sane defaults and does not require one to learn a language to do any configuration. It was written by hackers for hackers and it strives to be small, compact and fast.

Spectrwm is written in C and configured with a text configuration file. It was previously known as scrotwm.

## Installation
Install the  package.

## Starting
Run  with xinit.

## Configuration
spectrwm looks for the user configuration file in  and . If none of these exist it opens the global configuration file at . It also supports the XDG Base Directory paths.

Optionally, spectrwm can call  (in the user's path), which should output a text status message to  for the status bar.

The modkey (the main key to issue commands with) is set to , which is usually the  key.

There is also a screen lock key binding, which by default calls  from the  package.

 is also useful for screen saving and power management after an idle period and screen locking.

See Xdefaults for details of how to set up fonts, colours and other settings for  and . Run  to select the animation (or blank) and display power management (recommended).

## Keybindings
Default keybindings are in . In order to customize keybindings:

* Set  to  in your

* Copy-paste the contents of  to the end of your .

## Multiple monitors (Xinerama)
With a non-Xrandr multiple monitor setup create regions to split the total desktop area into one region per monitor:

 region                = screenregion                = screen[1:1280x1024+1280+0

## Statusbar
To enable the statusbar, uncomment these two items in  (or ). By default they are commented out and the statusbar is disabled.

 bar_action              = baraction.sh
 bar_delay               = 5

## Bash scripts
To test the status bar, place the following simple  in a
 (or ) directory which you have previously added to your $PATH in your ~/.bashrc file.

Press  to restart spectrwm and after a few seconds you should see the output in the status bar. If you have problems at this stage, make sure the script is executable, test it from the command line, and check the path/filename you specified in .

Here are some other ideas for status bar items: ethernet, email notification, disk space, mounts, now playing (mpc current).

The script may also show the date, in which case the built-in clock can be disabled:

 clock_enabled     = 0

## Conky
Instead of a bash script, Conky may be used. It should be used in non-graphical mode as shown below to output a text string to stdout which can be read in by spectrwm. First install .
It is not necessary to install the cut-down  (although that would work too).

In  set

 bar_action = conky

Then in each user's  file place for example:

 out_to_x no
 out_to_console yes
 update_interval 1.0
 total_run_times 0
 use_spacer none
 TEXT
 ${time %R %a,%d-%#b-%y} |Mail:${new_mails} |Up:${uptime_short} |Temp:${acpitemp}C |Batt:${battery_short} |${addr wlan0} |RAM:$memperc% |CPU:${cpu}% | ${downspeedf wlan0}

## Alternative status bar
An alternative is to use dzen2 to create a status bar. This has the advantage that colors and even icons may be used, but the disadvantage that the bar is not integrated with spectrwm. So the current workspace number and layout and the bar-toggle keybinding are not available. The "region" option can be used to reserve the required screen space.

For example to reserve 14 pixels at the top of the screen:

(adjust for your screen resolution).

Then, for example using i3status to supply the information:

 $ i3status | dzen2 -fn -*-terminus-medium-*-*-*-*-*-*-*-*-*-*-* &

Spectrwm's own bar can still be enabled and disabled with .

## Screenshots
Spectrwm has the facility to execute a script called  with the keybindings

*  − for a full screenshot
*  − for a screenshot of a single window

First install , then copy the default script supplied in the spectrwm package to a location in your , for example:

 $ cp /usr/share/spectrwm/screenshot.sh ~/bin

## Screen locking
By default the lock keybinding  executes xlock

 program= xlock

An alternative, if xscreensaver is already running, is to use

 program[lock      = xscreensaver-command -lock

## Using spectrwm
* To save space, window title bars are not shown. Window borders are one pixel wide. The border changes colour to indicate focus.
* Layouts are handled dynamically and can be changed on the fly. There are three standard layouts (stacking algorithms): vertical, horizontal and maximized (indicated in the status bar as ,  and )
* There is the concept of a master area (a working area). Any window can be switched to become the master and will then be shown in the master area. The master area is the left (top) portion of the screen in vertical (horizontal) mode. The size of the master area can be adjusted with the keys. By default the master area holds one window, but this can be increased.
* The area excluding the master area is called the stacking area. New windows are added to the stacking area. By default the stacking area has one column (row) in vertical (horizontal) mode, but this can be increased.
* Windows may be moved to a floating layer, i.e. removed from the tiling management. This is useful for programs which are not suitable for tiling.

Some of the most useful key bindings to be used with :

* : open terminal
* : invokes dmenu (where you can type the start of the program name and )
*  to : select workspaces 1 to 10
*  to : move the window to the workspace 1 to 10
*  or : select the next or previous workspace
*  or : select the next or previous screen
* : cycle through layouts (vertical, horizontal, maximized)
*  or : cycle through windows forwards or backwards
*  or : same as  or
* : move the current window to the master area
*  or :  increase or decrease the size of the master area

Advanced stacking (still accompanying ):

*  or : increase or decrease the number of windows in master area (default is 1)
*  or : increase or decrease the number of columns(rows) in stacking area in vertical(horizontal) mode (default is 1)
*  or : swap window position with the next or previous window
* : toggle between float and tile

Mouse bindings:

* : focus window
* : move window (and float it if tiled)
* : resize floating window
* : resize floating window keeping it centered

Other useful bindings (accompanying ):

* : close window
* : kill window
* : hide or show the status bar
* : restart spectrwm (reset desktops and reread spectrwm configuration without stopping running programs)
* : exit spectrwm

## Troubleshooting
## Help, I just logged in and all I see is a blank screen
Press  and an xterm will start. See the manual for other default key bindings. Also check your configuration file.

## Why does my window open in a desktop other than the current active one?
Currently the PID of window is used to determine the desktop for new windows. To workaround this with terminals for example, you can often pass an argument to open the terminal in a new process.

## Help, Xorg terminates after running startx
Make sure all the dependencies such as  are installed.

You may also use Xephyr against your xinitrc within another xsession to troubleshoot.
