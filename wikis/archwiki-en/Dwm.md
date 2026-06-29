# Dwm

dwm is a dynamic window manager for Xorg. It manages windows in tiled, stacked, and full-screen layouts, as well as many others with the help of optional patches. Layouts can be applied dynamically, optimizing the environment for the application in use and the task being performed. dwm is extremely lightweight and fast, written in C and with a stated design goal of remaining under 2000 source lines of code. It provides multihead support for xrandr and Xinerama.

## Installation
dwm can be installed with the  package. Make any required configuration changes before building and installing, see makepkg.

## Configuration
dwm is configured at compile-time by editing some of its source files, specifically . For detailed information on these settings, see the included, well-commented  as well as the customisation section on the dwm website.

The official website has a number of patches that can add extra functionality to dwm. These patches primarily make changes to the  file but also make changes to the  file where appropriate. For information on applying patches, see the Patching packages article.

## Starting
Select Dwm from the menu in a display manager of choice. Alternatively, to start dwm with startx append  to  and prepend other programs to execute them as well, for example:

 redshift -O3500; xset r rate 300 50; exec dwm

## Usage
See the dwm tutorial for information on basic dwm usage.

## Tips and tricks
## Statusbar configuration
For more examples of status bars, see dwm reads the name of the root window and redirects it to the statusbar. The root window is the window within which all other windows are drawn and arranged by the window manager. Like any other window, the root window has a title/name, but it is usually undefined because the root window always runs in the background.

The information that you want dwm to show in the statusbar should be defined with  command in  or  (if you are using a display manager). For example:

 xsetroot -name "Thanks for all the fish!"

Dynamically updated information should be put in a loop which is forked to background - see the example below:

In this case the date is shown in RFC:3339 format and PCManFM is launched at startup.

## Conky statusbar
Conky can be printed to the statusbar with :

 (conky | while read LINE; do xsetroot -name "$LINE"; done) &
 exec dwm

If you do not want to spawn too many PIDs by 'xsetroot' command, you can compile this C program:

{{bc|1=
#include
#include
#include
#include

int main(int argc, char * argv[)
{
        Display * dpy = NULL;
        Window win = 0;
        size_t length = 0;
        ssize_t bytes_read = 0;
        char * input = NULL;

        dpy = XOpenDisplay(getenv("DISPLAY"));
        if (dpy == NULL)
        {
                fprintf(stderr, "Can't open display, exiting.\n");
                exit(1);
        }
        win = DefaultRootWindow(dpy);

        while ((bytes_read = getline(&input, &length, stdin)) != EOF)
        {
                input- 1 = '\0';
                XStoreName(dpy, win, input);
                XFlush(dpy);
                fprintf(stderr, "Input: %s", input);
                fprintf(stderr, "\nbytes read: %ld\n", bytes_read);
        }
        free(input);
        return 0;
}
}}

Save this code to file dwm-setstatus.c, compile:

 $ gcc dwm-setstatus.c -lX11 -o dwm-setstatus

move 'dwm-setstatus' within your $PATH (, for example)

 # mv dwm-setstatus /usr/local/bin

and run:

 $ conky | dwm-setstatus

To do this, conky needs to be told to output text to the console only. The following is a sample conkyrc for a dual core CPU, displaying several usage statistics:

{{bc|
conky.config = {
out_to_console = true,
out_to_x = false,
background = false,
update_interval = 2,
total_run_times = 0,
use_spacer = 'none',
};
conky.text =
$mpd_smart :: ${cpu cpu1}% / ${cpu cpu2}%  ${loadavg 1} ${loadavg 2 3} :: ${acpitemp}c :: $memperc% ($mem) :: ${downspeed eth0}K/s ${upspeed eth0}K/s :: ${time %a %b %d %I:%M%P}
;
}}

For icons and color options, see dzen.

## Restart dwm
To restart dwm without logging out or closing applications, change or add a startup script so that it loads dwm in a while loop, for example:

dwm can now be restarted without destroying other X windows by pressing the usual Mod-Shift-Q combination.

It is a good idea to place the above startup script into a separate file,  for instance, and execute it through . Consider running the script with  to avoid security implications with remaining logged in after the X server is terminated; see Xinit#Autostart X at login for more information. From this point on, when you wish to end the X session, simply execute , or bind it to a convenient keybind. Alternatively, you could setup your dwm session script so that it relaunches dwm only if the binary changes.  This could be useful in the case where you change a setting or update the dwm code base.

## Bind the right Alt key to Mod4
When using Mod4 (the Super/Windows Key) as the , it may be equally convenient to have the right  key () act as . This will allow you to perform otherwise awkward keystrokes one-handed, such as zooming with +.

First, find out which keycode is assigned to :

 $ xmodmap -pke | grep Alt_R

Then simply add the following to the startup script (e.g. ), changing the keycode 113 if necessary to the result gathered by the previous  command:

Reassign  to :

 xmodmap -e "keycode 113 = Super_L"

Make sure X keeps it out of the "mod1" group:

 xmodmap -e "remove mod1 = Super_L"

After doing so, any functions that are triggered by the  key press will also be triggered by an  key press.

## Use both Alt keys as Meta in DWM
Use xmodmap to assign  as a secondary meta key in DWM (provided already using Mod1Mask (Alt_R))

## Space around font in dwm's bar
By default, dwm's bar adds 2px around the size of the font. To change this, modify the following line:

## Disable focus follows mouse
To disable focus follows mouse behaviour, comment out the following line in definition of struct handler:

Note that this change can cause some difficulties; the first click on an inactive window will only bring the focus to it. To interact with window contents (buttons, fields etc), you need to click again. Also, if you have several monitors, you may notice that the keyboard focus does not switch to another monitor activated by clicking.

## Floating layout for some windows
For some windows, such as preferences dialogs, it does not make sense for these windows to be tiled - they should be free-floating instead. For example, to make Firefox's preferences dialog float, add the following to your rules array in :

 { "Firefox",     NULL,       "Firefox Preferences",        1

to use multimedia keys. Now we can map common tasks to these keys.

## Adjusting volume
Install the  package. Now in  we may add commands for mute and volume increase/decrease.

{{bc|1=
/* commands */
...

static const char *up_vol= { "pactl", "set-sink-volume", "@DEFAULT_SINK@", "+10%",   NULL };
static const char *down_vol[ = { "pactl", "set-sink-volume", "@DEFAULT_SINK@", "-10%",   NULL };
static const char *mute_vol= { "pactl", "set-sink-mute",   "@DEFAULT_SINK@", "toggle", NULL };
...

static const Key keys[ = {
       ...

       { 0,             XF86XK_AudioMute,         spawn,          {.v = mute_vol } },
       { 0,             XF86XK_AudioLowerVolume,  spawn,          {.v = down_vol } },
       { 0,             XF86XK_AudioRaiseVolume,  spawn,          {.v = up_vol } },

       ...
};
}}

## Audio Controls (play/pause, next track, previous track)
Install the  package. Now in  we may add commands to control last used player.

{{bc|1=
/* commands */
...

static const char *play_pause= { "playerctl", "play-pause", NULL };
static const char *next_track[ = { "playerctl", "next", NULL };
static const char *prev_track= { "playerctl", "previous", NULL };
...

static const Key keys[ = {
       ...

	    { 0,             XF86XK_AudioPlay,         spawn,          {.v = play_pause} },
	    { 0,             XF86XK_AudioNext,         spawn,          {.v = next_track} },
	    { 0,             XF86XK_AudioPrev,         spawn,          {.v = prev_track} },

       ...
};
}}

{{Tip|If you only plan on using multimedia buttons for one specific player, use the  option, e.g. {{bc|1=static const char *play_pause= { "playerctl", "play-pause", "--player=vlc", NULL };}}.}}

## Adjusting brightness
Install the  package. Now in  we may add commands for dimming and brightening the screen.

{{bc|1=
/* commands */
...

static const char *brighter[ = { "brightnessctl", "set", "10%+", NULL };
static const char *dimmer= { "brightnessctl", "set", "10%-", NULL };
...

static const Key keys[ = {
       ...

       { 0,             XF86XK_MonBrightnessDown, spawn,          {.v = dimmer } },
       { 0,             XF86XK_MonBrightnessUp,   spawn,          {.v = brighter } },

       ...
};
}}

## Adjusting keyboard backlight brightness
Install the  package. Now in  we may add commands for dimming and brightening the keyboard backlight.

Find the name of your device

 brightnessctl --list

Look for , where  is the manufacturer of your device, e. g.  or  for Apple,  for Asus etc.

{{bc|1=
/* commands */
...

static const char *kbd_up= { "brightnessctl", "--device=vendor::kbd_backlight", "set", "+10%", NULL };
static const char *kbd_down[ = { "brightnessctl", "--device=vendor::kbd_backlight", "set", "10%-", NULL };
...

static const Key keys= {
       ...

       { 0,             XF86XK_KbdBrightnessUp,   spawn,          {.v = kbd_up } },
       { 0,             XF86XK_KbdBrightnessDown, spawn,          {.v = kbd_down } },

       ...
};
}}

## Autostart
A [https://dwm.suckless.org/patches/autostart/ patch is available. It runs  and  before entering the handler loop. One or both of these files can be omitted.

## Troubleshooting
## Fixing misbehaving Java applications
See Java#Gray window, applications not resizing with WM, menus immediately closing.

## Fixing gaps around terminal windows
If there are empty gaps of desktop space outside terminal windows, it is likely due to the terminal's font size. Either adjust the size until finding the ideal scale that closes the gap, or toggle  to 0 in .

This will cause dwm to ignore resize requests from all client windows, not just terminals. The downside to this workaround is that some terminals may suffer redraw anomalies, such as ghost lines and premature line wraps, among others.

Alternatively, if you use the st terminal emulator, you can apply the anysize patch and recompile st.

## Arabic Letter-shaping
dwm status bar does not have letter-shaping support. However, you can use tools like|  for applying letter-shaping using Unicode Arabic Presentation Form-B. E.g instead of:

 xsetroot -name "لِخَـوْلَةَ أطْـلالٌ بِبُرْقَةِ ثَهْمَـدِ"

Use:

 xsetroot -name "$(echo "لِخَـوْلَةَ أطْـلالٌ بِبُرْقَةِ ثَهْمَـدِ" | fribidi --nopad)"
