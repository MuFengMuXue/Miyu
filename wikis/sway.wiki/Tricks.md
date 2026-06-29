# Get workspace dimensions
    
    swaymsg -t get_outputs | jq -r '.. | select(.focused?) | .current_mode | "\(.width)x\(.height)"'

# Start a program on a specific workspace

    swaymsg 'workspace test; exec gnome-calculator; workspace back_and_forth'

This works as long as sway can match the PID of a new window to the PID of the exec'd command (or one of its children).

# Upload screenshot and copy url to clipboard

    bindsym $mod+Shift+Print exec slurp | grim -g - - | curl --form 'file=@-' http://0x0.st | wl-copy && swaynag -m "screenshot uploaded & url copied to clipboard"

# Take screenshots and open them in annotation tool

It's super convenient to be able to take a screenshot and pass it to Swappy for possible annotations in one step.
Actions in the `.desktop` file feel like a natural place to offer these options.

Using rofi as a launcher, ".desktop" file actions are findable if the `-drun-show-actions` is passed.

With these actions, you can snapshot any of the following and have
the result opened in swappy:

 - current window
 - current output
 - select a window
 - select an area

Install this file into `~/.local/share/applications/grimshot-swappy.desktop`:

```desktop
[Desktop Entry]
Name=Swappy
GenericName=Annotation Tool
GenericName[de]=Anmerkungswerkzeug
GenericName[fr]="Outil d'annotat"
GenericName[pt_BR]=Ferramenta de Anotação
Comment=A Wayland native snapshot editing tool
Comment[de]=Ein natives Wayland Bildschirmfoto-Bearbeitungswerkzeug
Comment[fr]="Un outil d'édition de capture d'écran avec support natif pour Wayland"
Comment[pt_BR]=Uma ferramenta de edição de snapshot nativa do Wayland
TryExec=swappy
Exec=swappy -f %F
Terminal=false
Type=Application
Keywords=wayland;snapshot;annotation;editing;
Icon=swappy
Categories=Utility;Graphics;Annotation;
StartupNotify=true
MimeType=image/png;image/jpeg;
Actions=current-window;current-output;select-window;select-area;

[Desktop Action current-window]
Name=Current Window
Exec=sh -c 'grimshot save active - | swappy -f -'

[Desktop Action current-output]
Name=Current Output
Exec=sh -c 'grimshot save output - | swappy -f -'

[Desktop Action select-window]
Name=Select Window
Exec=sh -c 'grimshot save window - | swappy -f -'

[Desktop Action select-area]
Name=Select Area
Exec=sh -c 'grimshot save area - | swappy -f -'
```


# HTML color picker

Bind this to a key, select a point on the screen and get a HTML color code for that point copied to the clipboard. Requires ImageMagick, `grim` and `slurp` to be installed.

    grim -g "$(slurp -p)" -t ppm - | convert - -format '%[pixel:p{0,0}]' txt:- | tail -n 1 | cut -d ' ' -f 4 | wl-copy

If you don't use a color picker frequently enough to remember the keybinding, you can create a simple .desktop file for it in ~/.local/share/applications/ and then launch it searching for the name with a desktop file launcher like Rofi. Here's an example .desktop file:

```desktop
[Desktop Entry]
Name=HTML Color Picker for Sway
Comment=Copies HTML color code to clipboard
Encoding=UTF-8
Version=1.0
Keywords=
Icon=
Exec=$HOME/.local/bin/html-color-picker-for-sway
Terminal=false
Type=Application
StartupNotify=true
```

Put the command above in `~/.local/bin/html-color-picker-for-sway` and add a shebang line as the first line: `#!/bin/sh`



# Tamefox - suspend Firefox when loses focus
```
#!/bin/sh
firefox=
swaymsg -m -t subscribe '["window"]' | \
        jq -r --unbuffered '.change +" "+  .container.app_id + " " + (.container.pid | tostring)' | \
        grep --line-buffered '^focus ' | \
        while read -r x app pid; do
                #echo "# x=$x app=$app pid=$pid" >&2
                if [ "$app" = 'firefox' ]; then
                        echo "CONT $pid" >&2
                        firefox=$pid
                        kill -CONT $pid
                        pkill -CONT -P $pid
                elif [ -n "$firefox" ]; then
                        echo "STOP $firefox" >&2
                        pkill -STOP -P $firefox
                        kill -STOP $firefox
                fi
        done
```
save it as `$HOME/bin/tamefox` and add this to your `.config/sway/config`:

    exec [ -x $HOME/bin/tamefox ] && $HOME/bin/tamefox

# Use space as $mod

If using Arch Linux, install Interception tools:
```
pacman -S interception-tools
```

Otherwise follow instructions here: https://gitlab.com/interception/linux/tools

Also install the space2meta plugin:

If using Arch, install from the AUR:
```
yay -S interception-space2meta
```
Otherwise follow instructions here: https://gitlab.com/interception/linux/plugins/space2meta

Drop this in /etc/interception/udevmon.yaml:

```
- JOB: intercept -g $DEVNODE | space2meta | uinput -d $DEVNODE
  DEVICE:
    EVENTS:
      EV_KEY: [KEY_SPACE]
```

Create a systemd service file with the following content:

```
[Unit]
Description=Monitor input devices for launching tasks
Wants=systemd-udev-settle.service
After=systemd-udev-settle.service
Documentation=man:udev(7)

[Service]
ExecStart=/usr/bin/udevmon -c /etc/interception/udevmon.yaml
Nice=-20
Restart=on-failure
OOMScoreAdjust=-1000

[Install]
WantedBy=multi-user.target
```

(Taken from: https://gitlab.com/interception/linux/tools/-/blob/master/udevmon.service)

Enable the service:

```
sudo systemctl enable udevmon.service
```

Start the service:

```
sudo systemctl start udevmon
```

The space key should now behave as the Super/Windows/Mod4 key when held and combined with another key.


**If your chording style does not agree with this method:**

You may find that your typing style makes it hard to hit the "chord timing" needed to trigger the Mod4 key.
There is an alternative plugin for interception-tools you can use which changes the behaviour of the tool. Feel free to play with the "TAP_MILLISEC" value in `/etc/interception/spacetomod4.yaml` to adjust it to your taste (increase it if you find you trigger the Mod key by accident as you type).

Install this alternative plugin for interception tools:

```
yay -S interception-dual-function-keys

```

Create a new file in /etc/interception (name it spacetomod4.yaml for example) with the following content:


```
TIMING:
    TAP_MILLISEC: 200
    DOUBLE_TAP_MILLISEC: 0

MAPPINGS:
    - KEY: KEY_SPACE
      TAP: KEY_SPACE
      HOLD: KEY_LEFTMETA
```

Modify the /etc/interception/udevmon.yaml file to this instead:


```
- JOB: "intercept -g $DEVNODE | dual-function-keys -c /etc/interception/spacetomod4.yaml | uinput -d $DEVNODE"
  DEVICE:
    EVENTS:
      EV_KEY: [KEY_SPACE, KEY_LEFTMETA]
```

And remember to restart the udevmon service:


```
sudo systemctl restart udevmon
```

# Get rid of main taskbar and move time/date to window title bar. 

For those of us who want every pixel of real estate!

The changes are:

* mode overlay
* workspace_buttons no
* background #ffffff10

```
#
# Status Bar:
#
# Read `man 5 sway-bar` for more information about this section.
bar {
    position top
    # This makes the tabs come at the same height as the bar. We then make the bar transparent
and we have them both "fused"
    mode overlay
    # When the status_command prints a new line to stdout, swaybar updates.
    # The default just shows the current date and time.
    status_command while date +'%Y-%m-%d %l:%M:%S %p'; do sleep 1; done
    # Workspace buttons don't look good when the bar is transparent
    workspace_buttons no
    colors {
        statusline #ffffff
        #background #323232
        # Transparent bar
        background #ffffff10
        inactive_workspace #32323200 #32323200 #5c5c5c
    }
}
```

# Copying and Pasting

Most stuff on sway I got working pretty easily, but the copy & paste setup was quite hard. With this setup I got it working as I want. I hope somebody else may find it useful.

```
# There are two wl-paste processes running, one for the primary and one for the normal clipboard
exec                     wl-paste    -t text --watch clipman store
exec                     wl-paste -p -t text --watch clipman store
# The keybind to select a clipping
bindsym $mod+y           exec clipman --primary pick --tool rofi
# Clear all clippings
bindsym $mod+Shift+y     exec clipman clear -a
# Remove a selected clipping
bindsym $mod+Mod1+y      exec clipman clear --tool rofi
# Empty the current clipping
bindsym $mod+Ctrl+y      exec : | wl-copy -p
```

References:
* https://github.com/bugaevc/wl-clipboard (for `wl-paste` / `wl-copy`)
* https://github.com/chmouel/clipman (for `clipman`)



# Increase scroll speed on some apps

This script set 6x scroll speed only if app like chromium is focused, require https://github.com/acrisci/i3ipc-python.

```python
#!/usr/bin/env python
import i3ipc
scroll_apps = ['discord', 'kitty']
default_speed = 1  # Reading current value would be nice
increased_speed = 6

def on_window_focus(i3, e):
    v = default_speed
    window_class = getattr(e.container, 'window_class', None)
    app_id = getattr(e.container, 'app_id', None)
    if window_class:
        c = window_class
    elif app_id:
        c = app_id
    else:
        return

    if c in scroll_apps:
        v = increased_speed
    i3.command(f'input type:pointer scroll_factor {v}')


i3 = i3ipc.Connection()
i3.on('window::focus', on_window_focus)
i3.main()
```

# Use a Trackball to Scroll

If you use a trackball as the pointing device, it is often tempting to use it also for scrolling. This can be achieved via a combination of 3 input options: `scroll_method`, `scroll_button`, and `scroll_button_lock`. Below is an example for the Elecom Deft Pro Trackball:

```
input "1390:306:ELECOM_TrackBall_Mouse_DEFT_Pro_TrackBall" {
  # Pressing BTN_TASK (the button above the Bluetooth/wireless switch, behind the left-click button) toggles scrolling with the trackball.
  scroll_method on_button_down
  # To use another button, use `libinput debug-events` to find out the key code and replace BTN_TASK with it.
  scroll_button BTN_TASK
  # Comment out the following line if you prefer using the trackball to scroll when holding down BTN_TASK, instead of let BTN_TASK toggle trackball scrolling.
  scroll_button_lock enabled
}
```