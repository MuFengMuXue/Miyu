# Picom

picom is a standalone compositor for Xorg, suitable for use with window managers that do not provide compositing. picom is a fork of compton, which is a fork of xcompmgr-dana, which in turn is a fork of xcompmgr.

## Installation
Install the  package.

## Configuration
The default configuration is available in . For modifications, it can be copied to  or .

To use another custom configuration file with picom, use the following command:

 $ picom --config path/to/picom.conf

See  for details.

## Disable shadows for some windows
The  option can disable shadows for windows if required. For currently disabled windows, see To disable shadows for menus add the following to  in :

 # menu        = { shadow = false; };
 dropdown_menu = { shadow = false; };
 popup_menu    = { shadow = false; };
 utility       = { shadow = false; };

The other  values that can be used are defined in the EWMH standard: , , , , , , , , , , , , , , and .

## Opacity
To set opacity (in effect transparency) for focused and unfocused windows (for example terminal emulators), add the following to your :

 rules: ({
   match = "class_g = 'URxvt' && focused";
   opacity = 0.9;
 }, {
   match = "(class_g = 'URxvt' || class_g = 'Alacritty')"
           " && !focused";
   opacity = 0.6;
 })

See also #Tabbed windows (shadows and transparency).

## Usage
picom may be manually enabled or disabled at any time during a session, or autostarted as a background process for sessions. There are also several optional arguments that may be used to tweak the compositing effects provided. These include:

* : Run as a background process for a session (e.g. when autostarting for a window manager such as Openbox)
* : Enable shadow effects
* : Disable shadow effects on panels and docks (deprecated, use #Disable shadows for some windows)
* : Disable shadow effects for application windows and drag-and-drop objects (deprecated, use #Disable shadows for some windows)
* : Use a specified configuration file

Many more options are available, including setting timings, displays to be managed, the opacity of menus, window borders, and inactive application menus. See .

To manually enable default compositing effects during a session, use the following command:

 $ picom &

To autostart picom as a background process for a session, the  argument can be used (may cause a display freeze):

 $ picom -b

Here is an example where additional arguments that require values to be set have been used:

 $ picom -cfF -o 0.38 -O 200 -I 200 -t 0 -l 0 -r 3 -D2 -m 0.88

## Multihead
If a multihead configuration is used without xinerama - meaning that X server is started with more than one screen - then picom will start on only one screen by default. It can be started on all screens by using the  environment variable. For example, to run on X screen 0 in the background:

  DISPLAY=":0" picom -b

The above should work on all monitors. If it does not then try an older method that manually specifies each display:

 seq 0 3 | xargs -l1 -I@ picom -b -d :0.@

## Grayscale
It is possible to convert windows to grayscale by use of [https://learnopengl.com/Getting-started/Shaders shaders.

As per , start by editing the default shader from the picom's sources.

{{hc|/path/to/shader/file.glsl|2=
#version 330

in vec2 texcoord;
uniform sampler2D tex;
uniform float opacity;

vec4 default_post_processing(vec4 c);

vec4 window_shader() {
	vec2 texsize = textureSize(tex, 0);
	vec4 color = texture2D(tex, texcoord / texsize, 0);

	color = vec4(vec3(0.2126 * color.r + 0.7152 * color.g + 0.0722 * color.b) * opacity, color.a * opacity);

	return default_post_processing(color);
}
}}

Then start picom by including the file path to the shader. The  backend will also, probably, be necessary.

 $ picom --backend glx --window-shader-fg /path/to/shader/file.glsl

## Troubleshooting
Recent versions of picom had some problem with DRI2 acceleration and exhibited severe flickering when DRI2 is in use (picom bug, mesa bug).  This has been worked around and reported to be working, but may still affect some users.  DRI3 is unaffected by this particular issue.

The use of compositing effects may on occasion cause issues such as visual glitches when not configured correctly for use with other applications and programs.

## Conky
To disable shadows around Conky windows, have the following in :

 own_window_class conky

In the case this solution fail with blur effect, you can try this in :

 own_window_type= 'desktop'

## dwm and dmenu
dwm's statusbar is not detected by any of picom's functions to automatically exclude window manager elements. Neither dwm statusbar nor dmenu have a static window id. If you want to exclude it from inactive window transparency (or other), you will have to either patch a window class into the source code of each, or exclude by less precise attributes. The following example is with dwm's status on top, which allows a resolution independent of location exclusion:

 $ picom  --focus-exclude "x = 0 && y = 0 && override_redirect = true"

Otherwise, where using a configuration file:

 focus-exclude = "x = 0 && y = 0 && override_redirect = true";

The override redirect property seems to be false for most windows- having this in the exclusion rule prevents other windows drawn in the upper left corner from being excluded (for example, when dwm statusbar is hidden, x0 y0 will match whatever is in dwm's master stack).

## Firefox
See #Disable shadows for some windows.

To disable shadows for Firefox elements add the following to shadow-exclude in :

 "class_g = 'firefox' && argb",

See for more information.

## slock
slock does not set a class or window id, one can edit the source code so that the slock window sets one and then catch it using picom's window rules.

You will need to write a function that sets the class or window id. It can be enabled by adding the following to your :

{{bc|1=
static void set_window_class(Display *dpy, Window win) {
    XClassHint *class_hint = XAllocClassHint();
    if (!class_hint) {
        fprintf(stderr, "slock: unable to allocate class hint\n");
        return;
    }
    class_hint->res_name = "slock";
    class_hint->res_class = "slock";
    XSetClassHint(dpy, win, class_hint);
    XFree(class_hint);
}
}}

Where inactive window transparency has been enabled (the  argument when running as a command), this may provide troublesome results when also using slock. One solution is to amend the transparency to . For example, where running picom arguments as a command:

 $ picom  -i 0.2

Otherwise, where using a configuration file:

 inactive-dim = 0.2;

Alternatively, you may try to exclude slock by its window id, or by excluding all windows with no name.

Exclude all windows with no name from picom using the following options:

 $ picom  --focus-exclude "! name~=''"

Find your slock's window id by running the command:

 $ xwininfo & slock

Quickly click anywhere on the screen (before slock exits), then type your password to unlock. You should see the window id in the output:

 xwininfo: Window id: 0x1800001 (has no name)

Take the window id and exclude it from picom with:

 $ picom  --focus-exclude 'id = 0x1800001'

Otherwise, where using a configuration file:

 focus-exclude = "id = 0x1800001";

As a more simple solution, you could exclude fullscreen programs on the configuration file, for example:

 { match = "fullscreen"; opacity = 1.0; corner-radius = 0; round-borders = 0; shadow = false; },

## Flicker
Applies to fully maximized windows (in sessions without any panels) with the default  caused and resolved by the following option:

 unredir-if-possible = false;

See [https://github.com/chjj/compton/issues/402 for more information.

## Fullscreen tearing
If you observe screen tearing of video playback only in fullscreen, see #Flicker.

## Lag when using xft fonts
If you experience heavy lag when using Xft fonts in applications such as xterm or urxvt try:

 --xrender-sync --xrender-sync-fence

or the xrender backend.

See for more information.

## Tabbed windows (shadows and transparency)
When windows with transparency are tabbed, the underlying tabbed windows are still visible because of transparency. Each tabbed window also draws its own shadow resulting in multiple shadows.

Removing the multiple shadows issue can be done by adding the following to the already existing [https://github.com/yshui/picom/blob/248bffede73e520a4929dd7751667d29d4169d59/picom.sample.conf#L175-L181 shadow-exclude list:

 "_NET_WM_STATE@:32a *= '_NET_WM_STATE_HIDDEN'"

Not drawing underlying tabbed windows can be enabled by adding the following to your :

 opacity-rule = [
   "95:class_g = 'URxvt' && !_NET_WM_STATE@:32a",
   "0:_NET_WM_STATE@*= '_NET_WM_STATE_HIDDEN'",
   "0:_NET_WM_STATE@[1:32a *= '_NET_WM_STATE_HIDDEN'",
   "0:_NET_WM_STATE@*= '_NET_WM_STATE_HIDDEN'",
   "0:_NET_WM_STATE@[3:32a *= '_NET_WM_STATE_HIDDEN'",
   "0:_NET_WM_STATE@*= '_NET_WM_STATE_HIDDEN'"
 ;

Note that  is the Xorg class name of your terminal. Change this if you use a different terminal. You can query a window's class by running the command  and clicking the window.

See for more information.

## Unable to change the background color with xsetroot
Currently, picom is incompatible with 's  option, a workaround is to use  to set the background color:

 $ hsetroot -solid '#000000'

See [https://github.com/chjj/compton/issues/162 for more information.

## Screentearing with NVIDIA's proprietary drivers
Try launching picom with  or enabling vsync in :

 vsync = true;

Or alternatively, for better latency, enable . See #Enable Triple Buffering and ForceFullCompositionPipeline.

## Lag with NVIDIA's proprietary drivers
## Use Xrender backend
Try launching picom with  or add:

 backend = "xrender";

to your  file.

See for more information.

## Disable flipping
Another option to reduce lag with the glx backend is to disable "allow flipping" in nvidia settings (OpenGL section). This can also be done from the command line:

 $ nvidia-settings -a 'AllowFlipping=0'

## Enable triple buffering and ForceFullCompositionPipeline
Triple buffering can reduce latency in some cases, to enable it add the following lines to :

 Section "Device"
     Identifier "NVIDIA Card"
     Driver     "nvidia"
     VendorName "NVIDIA Corporation"
     BoardName  "GeForce GT 740"

     Option     "TripleBuffer" "On"
 EndSection

The  option provides less latency than picom's implementation of vsync, to enable it add the following line to the same file:

     Option     "ForceFullCompositionPipeline" "On"

To disable vsync in picom launch it with the  option or change the vsync parameter to false in :

 vsync = false;

See [https://github.com/yshui/picom/issues/620#issuecomment-869666038 for more information.

To load settings after reboot (see Autostarting) run

 $ nvidia-settings --load-config-only

## Xorg leaking GPU memory with NVIDIA proprietary drivers
See #Lag with NVIDIA's proprietary drivers.

## Slock after suspend
When using a systemd service to trigger slock on a suspend or hibernate action, one may find the screen unlocked for a few seconds after resume. To prevent, disable window fading:

 $ picom --no-fading-openclose

## Screen sharing
A shadowed overlay on screen sharing and shadows of Zoom Meetings pop-up windows might be avoided by adding the following to .

 shadow-exclude = [
   "name = 'cpt_frame_xcb_window'",
   "class_g ?= 'zoom'",
 ];

Blurred screen sharing is disabled by adding Zoom Meetings to  with

 blur-background-exclude = [
   "class_g ?= 'zoom'",
 ];

For Microsoft Teams, the red border around the shared content is implemented with a mostly transparent window. Having blur enabled makes it impossible to work with and should be disabled as follows:

 shadow-exclude = [
   "name = 'rect-overlay'",
 ];

 blur-background-exclude = [
   "name = 'rect-overlay'",
 ];

## Disable window fade in and fade out effect when switching between workspaces
Adding  flag can disable the fade in and fade out effect when switching to a new workspace. === Switching windows occasionally results in strange window transparency issues ===

This issue can happen after setting opacity in . Setting  in  would fix this issue.
