# Bspwm

bspwm is a tiling window manager that represents windows as the leaves of a full binary tree. bspwm supports multiple monitors and is configured and controlled through messages. EWMH is partially supported.

## Installation
Install  for the window manager itself and  for the X hotkey daemon.

## Starting
Run  using xinit.

## Configuration
The example configuration is located in .

Copy/install  from there into  and  into .

The file  needs to be executable since the default example is simply a shell script that in turn
configures bspwm via the  command.

 $ install -Dm755 /usr/share/doc/bspwm/examples/bspwmrc ~/.config/bspwm/bspwmrc
 $ install -Dm644 /usr/share/doc/bspwm/examples/sxhkdrc ~/.config/sxhkd/sxhkdrc

These two files are where you will be setting wm settings and keybindings, respectively.

See the  and  manuals for detailed documentation.

## Note for multi-monitor setups
The example bspwmrc configures ten desktops on one monitor like this:

 bspc monitor -d I II III IV V VI VII VIII IX X

You will need to change this line and add one for each monitor, similar to this:

 bspc monitor DVI-I-1 -d I II III IV
 bspc monitor DVI-I-2 -d V VI VII
 bspc monitor DP-1 -d VIII IX X

You can use  or  to find the monitor names.
Note that if monitor names contain special characters, the entire name needs to be escaped by a percentage sign  to get identified correctly.

The total number of desktops were maintained at ten in the above example. To address each desktop, you should refer to the exact desktop names (defined by the  command above) in your  like this:
 # focus or send to the given desktop
 alt + {_,shift + }{1-9,0}
     bspc {desktop --focus,node --to-desktop} '{I,II,III,IV,V,VI,VII,VIII,IX,X}'
Note: In default config, sxhkd refers to desktops by number. But those change each time the monitor setup is changed.

Desktops in bspwm are activated by their index. Unless explicitly set, bspwm will automatically choose the display order, which determines the desktop index. If you encounter issues with desktops being on the wrong display, you should explicitly set the display order. similar to this:

 bspc wm -O DVI-I-1 DVI-I-2 DP-1

 bspc monitor DVI-I-1 -d I II III IV
 bspc monitor DVI-I-2 -d V VI VII
 bspc monitor DP-1 -d VIII IX X

If you want to automate your monitor-screens setup in case you periodically change monitor layouts, you need to use a conditional structure to check if a specific monitor is connected and configure it appropriately; you can place the following script in place of the standard  command:

The previous script uses xrandr to set the virtual display configuration and bspc to assign the appropriate desktops layout.

Note that you should first set your preferred monitor layout with , then export the xrandr configuration script and then copy the contents inside the script in place of the xrandr command.

## Rules
bspwm can apply rules to windows based on the class name, which is the second string within the WM_CLASS property specified by ICCM. To determine the class name, you can:

# Install .
# Run .
# Click on the window of interest to indicate it to .
# Record the second string from the output of the command.

There are two ways to configure window rules (as of cd97a32).

The first is by using the built in rule command, as shown in the example bspwmrc:

The second option is to use an external rule command. This is more complex, but can allow you to craft more complex window rules.  See these examples for a sample rule command.

## Panels
## Using lemonbar
An example panel for  is provided in the examples folder on the GitHub page. You might also get some insights from the lemonbar wiki page. The panel will be executed by placing  in your bspwmrc. Check the optdepends in the  package for dependencies that may be required.

To display system information on your status bar you can use various system calls.  This example will show you how to edit your  to get the volume status on your BAR:

{{bc|
panel_volume()
{
        volStatus=$(amixer get Master | tail -n 1 | cut -d '-f 4 | sed 's/.*//g')
        volLevel=$(amixer get Master | tail -n 1 | cut -d '-f 2 | sed 's/%.*//g')
        # is alsa muted or not muted?
        if [ "$volStatus" == "on"
        then
                echo "%{Fyellowgreen} $volLevel %{F-}"
        else
                # If it is muted, make the font red
                echo "%{Findianred} $volLevel %{F-}"
        fi
}}}

Next, we will have to make sure it is called and redirected to :

## Using polybar
Polybar can be used by adding  to your bspwmrc configuration file, where  is the name of the bar.

## Scratchpad
## Using pid
You can emulate a dropdown terminal.

First create a file called :
{{hc|/usr/local/bin/scratch|
#!/bin/bash

name="$1"
filename=/tmp/"$1"

bspc_write_nodeid() {
    while true
    do
        flag=false
        for id in $(bspc query -d focused -N -n .floating.sticky.hidden)
        do
            bspc query --node $id -T | grep -q $name && { echo $id > $filename; flag=true; break; }
        done
         "$flag" == "true"  && break
        sleep 0.1s
    done
}

hide_all_except_current(){
    for id in $(bspc query -d focused -N -n .floating.sticky.!hidden)
    do
        bspc query --node $id -T | grep -qv $name && bspc node $id --flag hidden=on
    done
}

toggle_hidden() {
    [ -e "$filename" ] || exit 1
    hide_all_except_current
    id=$("
	exit 1
fi

pids=$(xdotool search --class ${1})
for pid in $pids; do
	echo "Toggle $pid"
	bspc node $pid --flag hidden -f
done
}}

Then add this to your bspwm config.

To toggle the window a custom rule in sxhkd is necessary. Give as parameter the custom class name.

## Other
For a scratch-pad which can use any window type without pre-defined rules, see: For a more sophisticated scratchpad script that supports many terminals out of the box and has flags for doing things like optionally starting a tmuxinator/tmux session, turning any window into a scratchpad on the fly, and automatically resizing a scratchpad to fit the current monitor see .

## Different monitor configurations for different machines
Since the  is a shell script, it allows you to do things like these:

 #!/bin/bash -

 if  $HOSTNAME == myhost ; then
     bspc monitor eDP1 -d I II III IV V VI VII VIII IX X
 elif  $HOSTNAME == otherhost ; then
     bspc wm -O VGA-0 VGA-1
     bspc monitor VGA-0 -d I II III IV V
     bspc monitor VGA-1 -d VI VII VIII IX X
 elif  $HOSTNAME == yetanotherhost ; then
     bspc wm -O DVI-I-2 DVI-I-3
     bspc monitor DVI-I-3 -d VI VII VIII IX X
     bspc monitor DVI-I-2 -d I II III IV V
 fi

## Set up a desktop where all windows are floating
Here is how to setup the desktop 3 to have only floating windows. It can be useful for GIMP or other applications with multiple windows.

Put this script somewhere in your  and call it from  or similar (with a  at the end):

 #!/bin/bash

 # change the desktop number here
 FLOATING_DESKTOP_ID=$(bspc query -D -d '^3')

 bspc subscribe node_add | while read -a msg ; do
    desk_id=${msg[2}
    wid=${msg[ "$FLOATING_DESKTOP_ID" = "$desk_id"  && bspc node "$wid" -t floating
 done

(source)

## Keyboard
Bspwm does not handle any keyboard input and instead provides the bspc program as its interface.

For keyboard shortcuts you will have to setup a hotkey daemon like  ( for the development version).

## Troubleshooting
## Blank screen and keybindings do not work
* Make sure  is installed.
* Make sure you are starting sxhkd (in the background as it is blocking).
* Make sure  is executable.
* The example configuration file for sxhkd specifies urxvt as the terminal emulator. If you do not have this installed, edit  to point to the terminal emulator of your choosing.

## Cursor themes do not apply to the desktop
See Cursor themes#Change X shaped default cursor

## Window box larger than the actual application
This can happen if you are using GTK3 applications and usually for dialog windows. Create or add the following:

{{hc|~/.config/gtk-3.0/gtk.css|
.window-frame, .window-frame:backdrop {
  box-shadow: 0 0 0 black;
  border-style: none;
  margin: 0;
  border-radius: 0;
}

.titlebar {
  border-radius: 0;
}
}}

(source: Bspwm forum thread)

## Problems with Java applications
If you have problems, like Java application Windows not resizing, or menus immediately closing after you click, see Java#Gray window, applications not resizing with WM, menus immediately closing.

Furthermore, some applications based on Java can not display any window content at all (e.g. Intellij IDEs like PyCharm, CLion, etc). A solution is to install  and add the following line:

Additionally, these errors can often be solved by setting an environment variable for the JVM within e.g :

 export _JAVA_AWT_WM_NONREPARENTING=1

## Problems with keybindings using fish
If you use fish, you will find that you are unable to switch desktops. This is because bspc's use of the ^ character is incompatible with fish. You can fix this by explicitly telling sxhkd to use bash to execute commands:

 $ set -U SXHKD_SHELL /usr/bin/bash

Alternatively, the ^ character may be escaped with a backslash in your sxhkdrc file.

## Performance issues using fish
sxhkd uses the shell set in the SHELL environment variable in order to execute commands. fish can have long initialization time due to large or improper configuration files, thus all sxhkd commands can take much longer to execute than with other shells. To fix this without changing your default SHELL you can make tell sxhkd explicitly to use bash, or another faster shell to execute commands (for example, sh):

 $ set -U SXHKD_SHELL sh

## Error messages "Could not grab key 43 with modfield 68" on start
Either you try to use the same key twice, or you start sxhkd twice. Check bspwmrc and  or  for excessive commands starting sxhkd.
