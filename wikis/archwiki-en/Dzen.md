# Dzen

Dzen is "a general purpose messaging, notification and menuing program for X11. It was designed to be scriptable in any language and integrate well with window managers like dwm, wmii and xmonad though it will work with any window manager."

## Installation
Install the  package, which includes Xft, XPM, and Xinerama support.

## Usage
Dzen receives string from a pipe and output it graphically, this fact makes dzen scriptable in any language.
Example:
 $ echo "Hello World" | dzen2 -p

## Options
Dzen has a lot of options. The following list explains some of them:
*  Foreground color.
*  Background color.
*  Font.
*  Align the title window content, l(eft), c(enter), r(ight).
*  Width of the title window.
*  Align the slave window content. See .
*  Number of lines in the slave window.
*  Events and action.
*  Menu mode.
*  Update contents of title and slave window simultaneously.
*  Persist EOF (optional timeout in seconds).
*  X position .
*  Y position .
*  Height of the line (default: fontheight + 2 pixels).
*  Width of the window.
*  Version.

## Making a pop-up with dzen
The following code will open a dzen window in the top right corner of the screen. It will have a width of 100px, a height of 15px with a black foreground and white background (right button click to close dzen).

 $ seq 1 3 | dzen2 -p -w '100' -h '15' -fg '#000000' -bg '#FFFFFF'

Note that the window is with the number 3 in the middle, try to run the same code with  option.

 $ seq 1 3 | dzen2 -p -w '100' -h '15' -fg '#000000' -bg '#FFFFFF' -l '2'

Now when you hover the mouse through the dzen it will uncollapse the slave window. If you click on the lines in the slave window nothing will happen, try to use the  option.

 $ seq 1 3 | dzen2 -p -w '100' -h '15' -fg '#000000' -bg '#FFFFFF' -l '2' -m

Now if you click on the lines it will print the numbers in your terminal. This feature is useful to make menus.

But if you want to center the numbers and align the title to the left, you will need the options:  and .

 $ seq 1 3 | dzen2 -p -w '100' -h '15' -fg '#000000' -bg '#FFFFFF' -l '2' -m -ta 'l' -sa 'c'

## Configuration
Dzen is able to read font and color settings from X resources. As an example, you can add following lines to :
 dzen2.font:       -*-fixed-*-*-*-*-*-*-*-*-*-*-*-*
 dzen2.foreground: #22EE11
 dzen2.background: black

## Tips and tricks
## Using custom fonts with dzen
Dzen follows the X Logical Font Description, so it will only find fonts in the X font path. See Fonts#Older applications for details.

## Dzen and Conky
Conky can be used to pipe information directly to dzen for output in a status bar.
This can be done with  and , a stripped-down version of the Conky status utility.

The following example displays the average load values in red and the current time in the default dzen foreground colour:

{{hc|~/.conkyrc|
conky.config = {
      background = false
    , out_to_console = true
    , out_to_x = false
    , update_interval = 1.0
    , total_run_times = 0
    , use_spacer = none
}

conky.text = ^fg(\#ff0000)${loadavg 1 2 3} ^fg()${time %a %b %d %I:%M%P}
}}

Simply execute  in your startup scripts.

## Clickable areas and popups
dzen2 allows you to define clickable areas using .
You can use this property to create popups giving arbitrary information, as seen in various screenshot gifs like this.

A simple example can be:
{{hc|sysinfo_popup.sh|
 #/bin/bash

 #A simple popup showing system information

 HOST=$(uname -n)
 KERNEL=$(uname -r)
 UPTIME=$( uptime | sed 's/.* up //' | sed 's/us.*//' | sed 's/ day, /d /'\
          | sed 's/ days, /d /' | sed 's/:/h /' | sed 's/ min//'\
            |  sed 's/,/m/' | sed 's/  / /')
 PACKAGES=$(pacman -Q | wc -l)
 UPDATED=$(awk '/upgraded/ {line=$0;} END { $0=line; gsub(/\[\/,"",$0); \
          printf "%s %s",$1,$2;}' /var/log/pacman.log)

 (
 echo "System Information" # Fist line goes to title
 # The following lines go to slave window
 echo "Host: $HOST "
 echo "Kernel: $KERNEL"
 echo "Uptime: $UPTIME "
 echo "Pacman: $PACKAGES packages"
 echo "Last updated on: $UPDATED"
 ) | dzen2 -p -x "500" -y "30" -w "220" -l "5" -sa 'l' -ta 'c'\
    -title-name 'popup_sysinfo' -e 'onstart=uncollapse;button1=exit;button3=exit'

 # "onstart=uncollapse" ensures that slave window is visible from start.
}}
Save this script and make it executable and then use the  attribute in your conkyrc (or the script that you pipe to dzen2) to trigger it.

This will bind the script to mouse button 1 and execute it when it is clicked over the text.

## Gadgets
There are some gadgets on dzen that may be used to make a good customize. Follow below some of they with a brief explanation and examples.

## dbar
Dbar receive a pipe from another command with any number and outputs a semi-graphical progress bar with it, by default the max number of 100% is . The maximum and minimum values can be changed with / respectively.

Output example:
 50%

Code example:
{{hc|~/test|
#!/bin/sh

(
amixer get Master | \
awk '/Left:/{gsub(/:punct:/,"",$5);left=$5}
     /Right:/{gsub(/:punct:/,"",$5);right=$5}
     END {print left ORS right}'
) | dbar -max 100 -min 0 -s '|' -l 'Vol'
}}

See README.dbar for details.

## gdbar
Gdbar as well as dbar outputs a progress bar based on a value of 100%, but here it is full-graphical. Gdbar have the same options of dbar with some additional options. Some of the options are:
*  set the foreground.
*  set the background.
* / set the width and height respectively.

Code example:
{{hc|~/test|
#!/bin/sh

(
amixer get Master | \
awk '/Left:/{gsub(/:punct:/,"",$5);left=$5}
     /Right:/{gsub(/:punct:/,"",$5);right=$5}
     END{print left ORS right}'
) | gdbar -max 100 -min 0 -l 'Vol ' -bg '#777777' -fg '#00ff00' -ss '2' | dzen2 -p -l '1' -w '150' -y '100' -x '100' -ta c -sa c -e 'onstartup=uncollapse;button3=exit'
}}

See README.gdbar for details.

## Others
Information about others gadgets can be found here.
