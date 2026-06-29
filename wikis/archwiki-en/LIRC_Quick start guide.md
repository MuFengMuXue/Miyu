# LIRC/Quick start guide

Step-by-step LIRC setup guide for USB (MCE Center Edition) IR receiver with universal remote control.

This is a quick-start guide only. Please refer to man pages of the commands and files used and online documentation for in-depth help.

## Prerequisites
* Get a USB IR receiver, preferably an MCE model which is almost always supported out-of-the-box.
* Re-purpose an old universal remote control you have lying around the house.

## Setup
# Connect the USB IR receiver.
# Ensure there are fully charged batteries in your remote control.
# Get some kind of output/response from the remote using :  Point the remote control at the IR receiver and press some buttons. This will attempt to autodetect the correct input device using the default "devinput" driver. However, this might not work without manual configuration of protocols.
# If no button presses are detected for most keys, change IR protocols. If you get no response to the remote control buttons you want to use, you likely need to enable different protocols: Look at the output of  (as well as ). When you have problems, run  as root.
# If no button presses are detected for most keys, try different universal remote control device modes. You may also need to try different universal remote control device modes (TV, DVD, Audio, etc., buttons) in order to detect button presses when you are getting started. (You could possibly reprogram the universal remote's modes, but that would likely be a long trial-and-error process to find a setting that works.)
# After reconfiguring IR protocols and remote control device mode, retest:  Point the remote control at the IR receiver and press some buttons. If button presses for most keys are not detected repeat the prior two steps until they are (or just run  as root).
# If you have narrowed down what protocols you need to support for your remote control, set them:  Otherwise, you can just use all protocols:
# Determine the correct device for your IR receiver. Use either the default "devinput" driver or the older "default" driver:
# Use the device found for your USB IR receiver, e.g., :  or just try:  See if button presses are detected.
# If required, edit , e.g., if you are using the driver "default" instead of "devinput".
# Test your remote to see if scancodes are printed:  See if button presses are detected.
# Use a drop-in file: . At the  section add the following line:  where each protocol string is replaced by the protocol(s) you need (or just use ).
# Start the lirc daemon, , so you can record keypresses in order to write an lircd configuration file for your remote control.
# Use irrecord to record keypress scancodes. Run:  to save/record the keystrokes to be used for your application. Follow 's instructions.
# Install the recorded lircd configuration file:
# Move  to  to disable it, because you are not using an IR keyboard and/or mouse, just the IR receiver:
# Restart  so you use the newly created lircd configuration file.
# Test to make sure the keys you recorded are correctly detected, that is, the correct key symbol is output for each button you press:  See if the correct key symbols are reported, and if repeated signals are properly rejected.

## Troubleshooting
## Keypresses are not detected
Follow #Setup.

## Repeated keypress events
If you are having keypress repeating problems (each button press is echoed multiple times), examine the output of . The second column value is the repeat count. This will increment when repeated signals are detected. Each decoded button press with its count reset to "00" is reported as a separate button press event by lircd.

To fix this problem, generally the "gap" parameter sampled by  in the  file should be adjusted, often to a much larger value (e.g., from 44968 up to 113975).

After editing/adjusting any lircd configuration file, be sure to restart lircd (as shown above).

## Final configuration
Write an lircrc file for your end user application. This file is used by all client programs built with lirc support that attach to lircd to read IR control events. Edit  to issue commands to the program to be controlled. Test this configuration by running:

 $ ircat prog

to see if the correct "config" strings for program  are being output when you press all the buttons you wish to use. Note:  If  is not read by your application or just does not work, an alternate default location is .

## Final testing
Finally, run your end user application and test remote control button presses to control it. If it works, you are done! If not, review and repeat the above sections as necessary to get each configuration step working before proceeding to the next step or section.
