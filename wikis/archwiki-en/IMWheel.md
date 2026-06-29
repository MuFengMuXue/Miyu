# IMWheel

IMWheel is a tool for tweaking mouse wheel behavior, on a per-program basis. It can map mouse wheel input to keyboard input, increase mouse wheel speed, and has support for modifier keys.

## Installation
Install the  package.

## Configuration
See .

IMWheel matches window class strings with regular expressions for deciding which windows to apply tweaks to. To find the specific class strings that are being matched, kill all other IMWheel processes, then run this command:

 $ imwheel -d --debug --kill

This will run IMWheel in the foreground in debug mode. As you use your mouse and keyboard, you will be able to see the window property values that IMWheel is attempting to match.

## Edit your configuration file
Create or edit . In this configuration file lines can be added for each program you want to tweak mouse wheel behavior for.

The syntax of the translation definition is the following:
 , ,

  Key Modifiers Input:
   Alt_L, Alt_R, Meta_L, Meta_R, Control_L, Control_R, Shift_L, Shift_R or None
  Mouse Action Input:
   Up, Down, Left, Right, Thumb
  Key Action Output:
   KeySym Output Repetitions[, Delay Before KeyUp Event [, Delay Before Next KeyPress Event]]

The following example will increase the mouse wheel speed for the document viewer zathura:

 # Speed up scrolling for the document viewer
 "^org\.pwmt\.zathura$"
     None, Up, Button4, 4
     None, Down, Button5, 4

This example enables back/forward thumb buttons for all applications and increases scroll speed in Chromium:

 "^chromium$"
 None, Up, Button4, 3
 None, Down, Button5, 3
 ".*"
 None, Thumb1, Alt_L|Left
 None, Thumb2, Alt_L|Right

Keep in mind that certain values, like the Window title, are Unicode. This can lead to difficulties when trying to write regular expressions that will match them. For example, an em dash (—) looks very much like a standard dash (-), but in regex is considered three "characters", not one.

 and  may be used in the place of  and  respectively for the mouse wheel.

Matching all programs (using ".*") can cause unwanted behaviour in some programs; since IMWheel emulates multiple scroll actions for each one the user makes, programs that have actions bound to the mouse wheel will perform those actions more times than expected.

For example, terminal emulators in which scrolling selects commands from the history will jump multiple items per scroll.

IMWheel catches modifier keys for monitored mouse buttons, for passing them further you need to explicitly configure it to do so. In the example below, the left  and mouse wheel combinations are passed to Chromium for zooming in/out without multiplying:

 # Speed up scrolling for chromium and pass unchanged for zoom
 "^chromium$"
     None, Up, Button4, 4
     None, Down, Button5, 4
     Shift_L,   Up,   Shift_L|Button4, 4
     Shift_L,   Down, Shift_L|Button5, 4
     Control_L, Up,   Control_L|Button4
     Control_L, Down, Control_L|Button5

To match a certain program in the terminal, use Bash to set the program name in the window title before the program is started. See Bash/Prompt customization#Customizing the terminal window title. You may need to reconfigure your terminal emulator to allow the window title to be set by programs running in the shell. Some terminals, like Konsole and GNOME Terminal, do this automatically.

## Run IMWheel
Run IMWheel simply like so:

 $ imwheel

The program will print its PID and run in the background.

## Run IMWheel on startup using a service
To avoid starting IMWheel manually, you can run it as part of your systemd startup.

Example:

After creating the service above, reload the systemd manager configuration of the calling user and start/enable the  user unit. Verify that the user service is running by checking its unit status or by checking the journal.

## Run IMWheel on startup using a shell script
Alternatively, you can create a  script in :

And then, on restart, it will automatically read and run the file. Always test your script manually before putting it in /etc/profile.d

## Run IMWheel by connecting a device
IMWheel can also be started and stopped when a device, such as a bluetooth mouse, is connected and disconnected. For example, the scroll speed could be adjusted when an external mouse is connected.

The device name must be updated to match the systemd device.  Run the following command to get a list of possible devices:

 $ systemctl --all --full -t device

Example:

Enabling and verification of the service is the same as the startup service.  After enabling the service, it will activate IMWheel the next time the device is connected.

## Troubleshooting
## Back/forward buttons not working
You may need to restrict IMWheel so only the scroll wheel is affected to prevent it from breaking other mouse input like the back/forward buttons. You can do this with the -b option.

 $ imwheel -b "45"

See also a related question on Ask Ubuntu.

## Scroll speed is not affected when I hover over the target window
In order for IMWheel to affect the scroll speed of a window, it must be focused. Scroll speed of an unfocused window will remain unchanged.

## Freezing while scrolling Amazon.com in Chrome and Firefox
Presumably, Amazon.com runs JavaScript that loads content based on the user's assumed scroll point on the page, without taking IMWheel into consideration. This leads to pages with missing content, increased CPU usage, and other bugs.

You may consider disabling IMWheel for these browsers and instead solving the problem using a browser extension, like Fast Scroll in the Chrome Web Store (add "amazon.com" to blacklist or a similar bug occurs), or FoxScroller for Firefox.
