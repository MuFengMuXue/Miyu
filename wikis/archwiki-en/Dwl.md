# Dwl

dwl is a wlroots-based Wayland compositor, similar in spirit to dwm. It is minimal, fast, and extensible through community-made patches. By default, it comes with very little functionality, it is usable in its base state, but more QOL features can be applied if desired.

## Installation
dwl can be installed with the  or  packages. Make any required configuration changes before building and installing, see makepkg.

## Configuration
dwl is configured at compile-time by editing some of its source files, specifically . For detailed information on these settings, see the included, well-commented .

The official website has a number of patches that can add extra functionality to dwl. These patches primarily make changes to the  file but also make changes to the  file where appropriate. For information on applying patches, see the Patching packages article.

## Enable XWayland
To build dwl with Xwayland enabled, install  and uncomment the following lines in the build file like so:

## Usage
dwl can be started from a display manager of choice, by selecting the desktop entry in the menu that it provides.

For starting dwl from a getty, execute the command as follows:

 $ dwl

You can also autostart a command using the  flag. This command will have information about selected layouts, current window title, app-id, and tags written to it's stdin by dwl. You can use this to populate your status bar. If your command does not consume the data sent by dwl, append  to it like this:

 dwl -s 'sh /path/to/autostart.sh <&-'

If using a display manager, this can be appended to the  line in the desktop entry.

## Tips and tricks
## Floating layout for some windows
For some windows, such as preferences dialogs, it does not make sense for these windows to be tiled - they should be free-floating instead. For example, to make Firefox's preferences dialog float, add the following to your rules array:

{{hc|/path/to/config.def.h|2=
static const Rule rules= {
...
{ NULL, "Firefox Preferences", 1 << 8, 1, -1 },
...
};
}}

## Taking screenshots
The script below will first create a directory , then if that succeeds it will take a screenshot and save it to a file with the current date and extension  in that newly made directory:

Additionally, if you also want to take screenshots with a selection box instead of taking a screenshot of all monitors, create the following:

For taking a screenshot and saving it to the clipboard instead of it being saved to a place on the filesystem create the script below:

Finally add the following:

{{hc|/path/to/config.def.h|2=
static const Key keys[ = {
...
{ 0, XKB_KEY_Print, spawn, SHCMD("path/to/scripts/screenshot.sh") },
{ WLR_MODIFIER_SHIFT, XKB_KEY_Print, spawn, SHCMD("path/to/scripts/screenshotsel.sh") },
{ WLR_MODIFIER_CTRL, XKB_KEY_Print, spawn, SHCMD("path/to/scripts/screenshotselcopy.sh") },
...
};
}}

This maps taking screenshots to the  key, taking screenshots with a selection box to the  keys, and finally taking screenshots then copying it to the clipboard with  keys.

## Adjusting volume
install , or , then add these options for volume management:

{{hc|/path/to/config.def.h|2=
static const char *up_vol= { "pactl", "set-sink-volume", "@DEFAULT_SINK@", "+10%",   NULL };
static const char *down_vol[ = { "pactl", "set-sink-volume", "@DEFAULT_SINK@", "-10%",   NULL };
static const char *mute_vol= { "pactl", "set-sink-mute",   "@DEFAULT_SINK@", "toggle", NULL };

static const Key keys[ = {
...
{ 0, XKB_KEY_XF86AudioRaiseVolume, spawn, {.v = up_vol } },
{ 0, XKB_KEY_XF86AudioLowerVolume, spawn, {.v = down_vol } },
{ 0, XKB_KEY_XF86AudioMute, spawn, {.v = mute_vol } },
...
};
}}

## Autostart
A patch is available, that allows you to autostart specified applications. One such example can be seen below:

{{hc|/path/to/config.def.h|2=
/* Autostart */
static const char *const autostart= {
    "wbg", "/path/to/your/image", NULL,
    NULL /* terminate */
};
}}

You can specify more applications by adding them to the list, each entry comma-separated and followed by . For example, you could start a bar, a notification daemon, or any background service you need. Just make sure each command and its arguments are properly quoted.

## Better mouse resizing
By default when resizing dwl will warp the cursor to the bottom right corner, with a [https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/better-resize patch this behavior can be changed.

That patch allows you to configure window resizing to be more flexible, instead of warping to the bottom right corner it comes with multiple modes:

* Warping the cursor to a selected corner.
* Locking the cursor in place while resizing.
* Disabling cursor warping altogether.
* Relative corner resizing, with this whichever corner the cursor is closest to is the one that will be resized.

A working configuration example of this patch can be found below:

With this, when resizing the corner closest to the cursor will be selected, the cursor will not warp, and finally the cursor will not lock itself in place.

## Troubleshooting
## Fixing misbehaving Java applications
See Java#Gray window, applications not resizing with WM, menus immediately closing.

## Fixing gaps around terminal windows
If there are empty gaps of desktop space outside terminal windows, it is likely due to the terminal's font size. Either adjust the size until finding the ideal scale that closes the gap, or toggle  to 0 in .

This will cause dwl to ignore resize requests from all client windows, not just terminals. The downside to this workaround is that some terminals may suffer redraw anomalies, such as ghost lines and premature line wraps, among others.

Alternatively, if you use the st terminal emulator, you can apply the anysize patch and recompile st.
