# Xfwm

xfwm is the window manager for the Xfce environment.

## Installation
Install the  package.

## Starting
Run  with xinit.

## Configuration
Most xfwm settings can be accessed through , for window behavior and shortcuts, , for advanced settings and compositing, and , for the number of workspaces and their names.

## Composite manager
To enable or disable the Xfwm compositor and adjust its settings, go to Window Manager Tweaks:

 $ xfwm4-tweaks-settings

Alternatively, it can be enabled with  or using xfconf. For example:

 $ xfconf-query -c xfwm4 -p /general/use_compositing -s true

## Window roll-up
Double clicking the titlebar, or clicking roll window up in the window menu, causes the window contents to disappear leaving only the titlebar. To disable this functionality with , run:

 $ xfconf-query -c xfwm4 -p /general/mousewheel_rollup -s false

## Window tiling
Xfwm can "tile" a window automatically when it is moved to an edge of the screen. It does so by resizing it to fit the top half of the screen. To enable or disable this behaviour with , run:

 $ xfconf-query -c xfwm4 -p /general/tile_on_move -s false
 $ xfconf-query -c xfwm4 -p /general/tile_on_move -s true

Alternatively, (un)check Window Manager Tweaks > Accessibility > Automatically tile windows when moving toward the screen edge.

## Extra settings provided by the Xfce settings manager
Install the  package.

## Additional themes
Install the  package.

The themes installed will be shown in the  window.

## Tips and tricks
## Hide the titlebar when window is maximized
Go to  and check .

## Troubleshooting
## No icons shown in browser for downloaded items
This is fixed by installing the  package.

## Number of workspaces changes unexpectedly
Keep in mind Xfwm assigns shortcuts to adding and removing workspaces. By default these are  and , respectively.

If the number of workspaces resets at login, change the amount after Xfwm is started. This is ensured by the  command. or, from :

See also: [https://forum.xfce.org/viewtopic.php?id=6056 Logout alters workspaces

## Video tearing
If you experience video tearing, you could try to change the  mode option of xfwm (glx, xpresent or off), try it with this command$ xfwm4 --replace --vblank=glx &

in order to save it:

 $ xfconf-query -c xfwm4 -p /general/vblank_mode -s glx

If you use Intel graphics and you have already enabled "TearFree" option in Xorg as described in Intel graphics#Tearing, then disable Synchronize drawing to the vertical blank option.

If this does not fix the tearing, consider disabling Xfwm's compositor and using an alternative composite manager.

## Horizontal line above dock windows
Xfwm may incorrectly render shadows above some dock windows (e.g.Plank). This would result in a horizontal line across the screen. A workaround is to disable Show shadows under dock windows under Settings > Window Manager Tweaks > Compositor.
