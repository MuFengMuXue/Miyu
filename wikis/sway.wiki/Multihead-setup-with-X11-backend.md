**This setup is not recommended. If at all possible, do not run sway this way as features may not work or behave unexpectedly.**

This guide explains how to set up sway running under X11 (e.g. started from an X11 login manager) on multiple monitors.

1. Set up your xorg.conf such that your monitors are presented as a unified screen (e.g. using Xinerama or TwinView). Make sure the ordering corresponds to what you actually want.

2. Start sway with `WLR_X11_OUTPUTS` set to the number of monitors, e.g. `WLR_X11_OUTPUTS=2 sway`

3. Use `DISPLAY=:0 xdotool search --name ''` to get all window ids in the underlying X11 screen. Then use `DISPLAY=:0 xdotool getwindowname <window-id>` to figure out which of the windows is which sway output. You want windows with a name like `wlroots - X11-n`, where `n` is the number of the output.

4. Move the sway outputs to the correct location on the X11 screen with xdotool. E.g. for two monitors with 1920x1080 resolution, do `DISPLAY=:0 xdotool windowmove <window-id-1> 0 0; DISPLAY=:0 xdotool windowmove <window-id-2> 1920 0`

5. Configure the correct resolution for all your outputs in your sway config.

I have created a script to automate steps 3 and 4 for two outputs with a width of 1920 pixels:

```
#!/bin/bash
windows=$(DISPLAY=:0 xdotool search --name '')
win1=''
win2=''
for win in $windows
do
    name=$(DISPLAY=:0 xdotool getwindowname $win)
    if [[ $name == "wlroots - X11-1" ]]
    then
        win1=$win
    elif [[ $name == "wlroots - X11-2" ]]
    then
        win2=$win
    fi
done
DISPLAY=:0 xdotool windowmove $win1 1920 0
DISPLAY=:0 xdotool windowmove $win2 0 0
```