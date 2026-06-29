# Screen capture

This article lists and describes screenshot and screencast software.

## Screenshot software
## Dedicated software
## Application list
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*
*

## Usage
## maim
 is aimed to be an improved scrot.

Save the full screen to file:

 $ maim filename

Prompt for selection and save to file:

 $ maim --select filename

Save the active window to file, assuming  is installed:

 $ maim --window $(xdotool getactivewindow) filename

Prompt for selection, save without cursor, and store it to clipboard, assuming  is installed:

 $ maim -s | xclip -selection clipboard -t image/png -i

## scrot
 enables taking screenshots from the CLI and offers features such as a user-definable time delay. Unless instructed otherwise, it saves the file in the current working directory.

 $ scrot -t 20 -d 5

The above command saves a dated .png file, along with a thumbnail (20% of original), for Web posting. It provides a 5 second delay before capturing in this instance.

You can also use standard date and time formatting when saving to a file.  e.g.,

 $ scrot ~/screenshots/%Y-%m-%d-%T-screenshot.png

saves the screenshot in a filename with the current year, month, date, hours, minutes, and seconds to a folder in your home directory called "screenshots"

See  for more information.

## Desktop environment specific
## Budgie
Budgie ships with its own screenshot utility called BudgieScreenshot.

It allows capturing the whole screen using , the active window or a selected area. See Keyboard Shortcuts for the shortcut to a specific action.

## Cinnamon
The default installation of Cinnamon does not provide a screenshot utility. Installing  will enable screenshots through the Menu > Accessories > Screenshot or by pressing .

## GNOME
GNOME users can press  or click the camera icon in the system menu. You can also optionally install  and open it via Apps > Accessories > Take Screenshot.

GNOME features built-in screen recording with the  key combination. A red circle is displayed in the bottom right corner of the screen when the recording is in progress. After the recording is finished, a file named  is saved in the  directory. In order to use the screencast feature the  and  packages need to be installed.

## KDE
If you use KDE, you might want to use Spectacle.

Spectacle is provided by the  package.

## Xfce
If you use Xfce you can install  and then add a keyboard binding:

Xfce Menu > Settings > Keyboard > Application Shortcuts

If you want to skip the Screenshot prompt, type  in terminal for the options.

## Other desktop environments or window managers
For other desktop environments such as LXDE or window managers such as Openbox and Compiz, one can add the above commands to the hotkey to take the screenshot. For example:

 $ import -window root ~/Pictures/$(date '+%Y%m%d-%H%M%S').png

Note that import is part of the  package. Adding the above command to the  key to Compiz allows to take the screenshot to the Pictures folder according to date and time.

Note that  in Openbox does not pass the string to a shell, so in order to run the subcommand, you need to run  manually. For example, add the following to the keyboard section of your  file:

If the  above does not work, see Keyboard input and use different keysym or keycode.

## Packages including a screenshot utility
## ImageMagick/GraphicsMagick
See ImageMagick#Screenshot taking.

## GIMP
You also can take screenshots with GIMP (File > Create > Screenshot...).

## imlib2
 provides a binary  to take screenshots. To take a screenshot of the full screen, type:

 $ imlib2_grab screenshot.png

## FFmpeg
See FFmpeg#Screen capture.

## Screencast software
See also FFmpeg#Screen capture and Wikipedia:Comparison of screencasting software.

Screencast utilities allow you to create a video of your desktop or individual windows.

*
*
*
*
*
*
*
*
:*  – plugin for GNOME screencast feature, supports Wayland
*
*
*
*
*
*
*
*
*

## Annotation and visualization tools
Some tools that can be used to annotate things during screencasts or show elements like pressed keys, or mouse activity.

*
*
*  (doesn't seem to display anything with Wayland)

## Wayland
Capturing the screen on Wlroots-based compositor can be done using:

*  or grimshot (from ) for screenshots
*  (whole screen only)
*  or  for video
*
*  (full/rectangular part of screen)
*  works, need to select grim for capture in configuration GUI

Optionally,  can be used to select the part of the screen to capture. If your GPU supports vaapi encoding,  can be a more efficient alternative to .

## Screenshot
Take a screenshot of the whole screen:

 $ grim screenshot.png

Take a screenshot of current window in Sway:

 $ swaymsg -t get_tree | jq -r '.. | select(.focused?) | .rect | "\(.x),\(.y) \(.width)x\(.height)"' | grim -g - screenshot.png

Take a screenshot of current window in Hyprland:

 $ hyprctl -j activewindow | jq -r '"\(.at\(.size[0)x\(.size| grim -g - screenshot.png

Take a screenshot of a part of the screen:

 $ slurp | grim -g - screenshot.png

Take a screenshot of a part of the screen and put the output into the clipboard using :

 $ slurp | grim -g - - | wl-copy

Take a screenshot of a part of the screen, save to a file, and put the output into the clipboard using :

 $ slurp | grim -g - - | tee ~/Pictures/$(date +%s).png | wl-copy

## Screencasting
*  now supports both Qt (it's base environment) and GNOME Desktop Environments (DE) for screencast screen, window or screen area. The DE will open a window asking to accept access (fullscreen for fullscreen or cropped part, window, for window) at each new record on GNOME.

## Via GNOME screencast
,  and  support screen recording on Wayland using GNOME screencast feature.

## Via the WebRTC protocol
See PipeWire#WebRTC screen sharing.

Chromium and Firefox should now be able to access the screenshare. You can verify this through [https://mozilla.github.io/webrtc-landing/gum_test.html Mozilla's getUserMedia / getDisplayMedia Test Page.

## Hyprland
The Hyprland window manager allows screen casting and recording with OBS (including selection of individual windows and workspaces) when used with  ===== Sway =====

Configuration for screen sharing with selection on Sway is covered by default in .

## Other wlroots based compositors
Capture a video of the whole screen with filename  (the default is ):

 $ wf-recorder -f recording.mp4

Capture a video of a part of the screen:

 $ wf-recorder -g "$(slurp)"

for those on a different wlroots based compositors, such as dwl: you will need to do the following,

install  with the gtk version then follow XDG Desktop Portal#Configuration with PipeWire installed then restart

See PipeWire#WebRTC screen sharing.

## Via a virtual webcam video feed
See v4l2loopback#Casting Wayland using wf-recorder.

Install  (or ) and . Load the  kernel module with the following parameters:

 # modprobe v4l2loopback exclusive_caps=1 card_label=VirtualVideoDevice

Verify that a new virtual video device  has been created:

Start recording the screen with  and feed the output to the new virtual video device  created by :

 $ wf-recorder --muxer=v4l2 --codec=rawvideo --file=/dev/video2 -x yuv420p

The  colour space is required for the video output to be compatible with Zoom [https://github.com/ammen99/wf-recorder/pull/43.

You can now select the above virtual video device as your "webcam" in video calling/video conferencing applications (the device is called ). You can use  (part of ), , or  (part of ) to verify that the virtual video device indeed outputs your screenshare:

 $ ffplay /dev/video2

 $ mpv av://v4l2:/dev/video2

 $ gst-launch-1.0 -v v4l2src device=/dev/video2 ! glimagesink

If Firefox is unable to read the video stream and prints a message like "AbortError: Starting video failed", try preloading :
 $ LD_PRELOAD=/usr/lib/v4l1compat.so firefox

## Sharing individual applications
As explained above,  is able to record only a portion of the screen by first selecting a region with . To use this functionality for sharing a specific region/application window through a virtual video device, start recording the screen with the following modified command:

 $ wf-recorder -g "$(slurp)" --muxer=v4l2 --codec=rawvideo --file=/dev/video2 -x yuv420p

After selecting a region of the screen, you will be able to access the video feed through the virtual video device  as above.

## Screencast Wayland windows with X11 applications
You can share native Wayland windows (or the whole screen/workspace) to the X11 application. For this you need to use . See Fixing Wayland: Xwayland screen casting  for details.

## Terminal
## Capture with ANSI codes
You can use the  command, part of the  package.
Just run  and from that moment, all the output is going to be saved to the  file, including the ANSI codes.

Once you are done, just run  and the  would ready. The resulting file can be converted to HTML using the  package (not to be confused with ansi2html from ).

To convert the  file to , do the following:

 $ ansi2html --bg=dark  typescript.html

Actually, some commands can be piped directly to ansi2html:

 $ ls --color|ansi2html --bg=dark >output.html

That does not work on every single case, so in those cases, using  is mandatory.

## Framebuffer
Use  or  to take a screenshot.

## Virtual console
## Screenshot
If you merely want to capture the text in the console and not an actual image, you can use , which is part of the  package.  The following command will dump the textual contents of virtual console 1 to a file  in the current directory:

 # setterm -dump 1 -file screen.dump

Root permission is needed because the contents of  need to be read.

## Screencast of console
 allows to record a whole terminal session activity, which is saved in a file in its own (open) format. This file can be played with the same tool or an HTML5 version of the tool, and can be shared on the asciinema.org official web site of the application, or on any own hosted HTML version.

Usage:  or .

*  records the session,  can pause/resume it, /exit of the session will stop it. Name of output file is optional.

Interesting arguments for recording:

*  if you just want to record a specific command action/output
*  record for 1.2 seconds only
*  add a title to the terminalcast

Other functions than recording:

*  play an asciinema record file
*  upload the file on asciinema.org for sharing
*  manage recordings on asciinema.org account

## Troubleshooting
## Screenshot uses old screen state
See KDE#Spectacle screenshot uses old screen state.

## NVIDIA clipping background
If the NVIDIA driver is in use and the screen recording is experiencing background clipping, enable the  setting. See NVIDIA/Troubleshooting#Avoid screen tearing for details.
