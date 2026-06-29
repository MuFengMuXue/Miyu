# Xmobar

xmobar is a lightweight, text-based, status bar written in Haskell. It was originally designed to be used together with xmonad, but it is also usable with any other window manager. While xmobar is written in Haskell, no knowledge of the language is required to install and use it.

## Installation
Install the  package.

## Running
If the configuration file is saved as :
 $ xmobar &
Alternatively, the path to a configuration file can be specified:
 $ xmobar /path/to/config &
The following is an example of how to configure xmobar using command line options:
 $ xmobar -B white -a right -F blue -t '%LIPB%' -c 'Weather "LIPB" [ 36000]' &
This will run xmobar right-aligned, with white background and blue text, using the  plugin. Note that the output template must contain at least one command. Read the following section for further explanation of options.

The flag  can specify the x display to run xmobar on and it will effectively override the configuration options pickBroadest and allDesktops.

## Configuration
The configuration for xmobar is normally defined in  or by specifying a set of command line options when launching xmobar. Any given command line option will override the corresponding option in the configuration file. This can be useful to test new configurations without having to edit a configuration file.

Following is an example  file, followed by a description of each option. Note that each option has a corresponding command line option.

Note: The configuration file is (a subset of) Haskell source code, so '' starts a single-line comment.

{{bc|
Config {

   -- appearance
     font =         "Bitstream Vera Sans Mono Bold 9"
   , bgColor =      "black"
   , fgColor =      "#646464"
   , position =     Top
   , border =       BottomB
   , borderColor =  "#646464"

   -- layout
   , sepChar =  "%"   -- delineator between plugin names and straight text
   , alignSep = "}{"  -- separator between left-right alignment
   , template = "%battery% | %multicpu% | %coretemp% | %memory% | %dynnetwork% }{ %RJTT% | %date% || %kbd% "

   -- general behavior
   , lowerOnStart =     True    -- send to bottom of window stack on start
   , hideOnStart =      False   -- start with window unmapped (hidden)
   , allDesktops =      True    -- show on all desktops
   , overrideRedirect = True    -- set the Override Redirect flag (Xlib)
   , pickBroadest =     False   -- choose widest display (multi-monitor)
   , persistent =       True    -- enable/disable hiding (True = disabled)

   -- plugins
   --   Numbers can be automatically colored according to their value. xmobar
   --   decides color based on a three-tier/two-cutoff system, controlled by
   --   command options:
   --     --Low sets the low cutoff
   --     --High sets the high cutoff
   --
   --     --low sets the color below --Low cutoff
   --     --normal sets the color between --Low and --High cutoffs
   --     --High sets the color above --High cutoff
   --
   --   The --template option controls how the plugin is displayed. Text
   --   color can be set by enclosing in  tags. For more details
   --   see http://projects.haskell.org/xmobar/#system-monitor-plugins.
   , commands =

        -- weather monitor
        [ Run Weather "RJTT" [ "--template", " | °C | % | hPa"
                             ] 36000

        -- network activity monitor (dynamic interface resolution)
        , Run DynNetwork     [ "--template" , ": kB/s|kB/s"
                             , "--Low"      , "1000"       -- units: B/s
                             , "--High"     , "5000"       -- units: B/s
                             , "--low"      , "darkgreen"
                             , "--normal"   , "darkorange"
                             , "--high"     , "darkred"
                             ] 10

        -- cpu activity monitor
        , Run MultiCpu       [ "--template" , "Cpu: %|%"
                             , "--Low"      , "50"         -- units: %
                             , "--High"     , "85"         -- units: %
                             , "--low"      , "darkgreen"
                             , "--normal"   , "darkorange"
                             , "--high"     , "darkred"
                             ] 10

        -- cpu core temperature monitor
        , Run CoreTemp       [ "--template" , "Temp: °C|°C"
                             , "--Low"      , "70"        -- units: °C
                             , "--High"     , "80"        -- units: °C
                             , "--low"      , "darkgreen"
                             , "--normal"   , "darkorange"
                             , "--high"     , "darkred"
                             ] 50

        -- memory usage monitor
        , Run Memory         [ "--template" ,"Mem: %"
                             , "--Low"      , "20"        -- units: %
                             , "--High"     , "90"        -- units: %
                             , "--low"      , "darkgreen"
                             , "--normal"   , "darkorange"
                             , "--high"     , "darkred"
                             ] 10

        -- battery monitor
        , Run Battery        [ "--template" , "Batt: "
                             , "--Low"      , "10"        -- units: %
                             , "--High"     , "80"        -- units: %
                             , "--low"      , "darkred"
                             , "--normal"   , "darkorange"
                             , "--high"     , "darkgreen"

                             , "--" -- battery specific options
                                       -- discharging status
                                       , "-o"	, "% ()"
                                       -- AC "on" status
                                       , "-O"	, "Charging"
                                       -- charged status
                                       , "-i"	, "Charged"
                             ] 50

        -- time and date indicator
        --   (%F = y-m-d date, %a = day of week, %T = h:m:s time)
        , Run Date           "%F (%a) %T" "date" 10

        -- keyboard layout indicator
        , Run Kbd            [ ("us(dvorak)" , "DV")
                             , ("us"         , "US")
                             ]
        ]
   }
}}

* font - The name of the font to use.".
Example:
 font = "Bitstream Vera Sans Mono 8"

* additionalFonts - List of fonts to be used with the  tag.
Example:
 additionalFonts = [ "Bitstream Vera Sans Mono 8", "Source Code Pro 10"]
* fgColor - The colour of the font, takes both colour names like  and hex colours like .
* bgColor - The colour of the bar, takes both colour names like  and hex colours like .
* position - The position of the bar. Keywords are: /, /,  and .
** / - The top/bottom of the screen.
** / - The top/bottom of the screen with a fixed width. TopW/BottomW takes 2 arguments:
*** Alignment: eft, enter or ight aligned.
*** Width: An integer for the width of the bar in percentage.
**  - A fixed position on the screen, with a fixed width. Static takes 4 arguments:
*** xpos: Horisontal position in pixels, starting at the upper left corner.
*** ypos: Vertical position in pixels, starting at the upper left corner.
*** width: The width of the bar in pixels.
*** height: The height of the bar in pixels.
**  - Specify on which screen the bar is positioned. Takes 2 arguments:
*** screenNr: Index of the screen to position the bar on.
*** position: The positioning of the bar, this is one of the above keywords followed by their arguments.
Example - centered at the bottom of the screen, with a width of 75% of the screen:
 position = BottomW C 75
Example - top left of the screen, with a width of 1024 pixels and height of 15 pixels:
 position = Static { xpos = 0 , ypos = 0, width = 1024, height = 15 }

* border - The position and appearance of a border. Keywords are:  and
** / - The top/bottom of the bar
**  - The entire perimeter of the bar
** // - Same as other options, except you can specify how many pixels off the bar's edge the border should be drawn. Each option takes a single integer argument.
Example - border placed 3 pixels off bottom edge of the bar:
 border: BottomBM 3

* sepChar - The character to be used for indicating commands in the output template. Default character is .
* alignSep - A string of characters for aligning text in the output template. The text before the first character will be left aligned, the text between them will be centered, and the text to the right of the last character will be right aligned. Default string is {{ic|"}{"}}.
* iconRoot - The root folder where icons are stored.
* template - The output template is a string containing the text and commands that will be displayed. It contains the alias for a , written text and color tags that sets the colour of text. The tags used in this template string can also be used in the  custom templates. The template tags include:
** prints the output of the command
** will print string with #f0f0f0 as foreground and #101010 as background ( either can be omitted )
** will print string with the nth, in this case the first, font in the listx of additionalFonts, with 0 being the default font.
** will print the XBM or XPM icon in the path ( it will use iconRoot ++ path/to/icon if it does not start with /, ./ or ../). Transparent XPM icons will ignore the fc tags and use the default bgcolor, while XBM icons will use the local ( or default ) background and foreground. xmobar will use icons regardless of size but to align them with text bgcolor and fgcolor the optimal height is 20px, there is no width restriction.
** will execute a command when string is clicked with button 1 ( left mouse button ).
** outputs an arbitrary string of length len.
Example:
 template = "%StdinReader%}{%cpu% %memory% battery: %battery% %date%"

* commands For setting the options of the programs to run. Commands is a comma seperated list of commands, optionally specified with options.
Example - runs the  plugin, with the specified template and the  plugin, with default args. Both update every second:
 commands = Memory ["-t","Mem: %" 10, Run Swap 10

And finally some options which control the bar's general behavior---each is set to a single  or  value:

* lowerOnStart - Controls whether to keep the bar behind all other windows.
* hideOnStart - Controls whether to hide the bar on start.
* allDesktops - Controls whether to show the bar on all desktops.
* overrideRedirect - An option necessary for some window managers to prevent the bar from being treated like a normal window.
* pickBroadest - On multi-monitor setups place the bar on the widest monitor instead of the first.
* persistent - Controls whether to always be visible or not, regardless of the bar's 'hidden' state.

## Tips and tricks
There are various plugins that can be used with xmobar - to name a few, there are plugins for disk usage, ram, cpu, battery status, weather report and network activity. A detailed description of each plugin, its dependencies and how to configure it is on the project website.

## GMail integration
Assuming you have either xmobar-gmail-darcs or xmobar-gmail installed, you can configure  as follows. Add the GMail plugin to the commands list:
 , Run GMail "gmail.username" "GmailPassword" "Mail: " 3000

Then add the command to the template
 , template = "... %gmail.username% ..."

## MPD integration
There is a plugin to pull information to display on the status bar about MPD's currently playing song. To add a simple plugin displaying the artist and song of the current track, add this line to your commands list in your :

 , Run MPD ":  - " 10

Finally, you will need to place the plugin some place in your template, as follows:

 , template = "%StdinReader% }{ ... %mpd% ..."

## Conky-Cli integration
It is possible to utilize the features of  such as disk space, top and system messages, by piping the information from conky into a text file and read the contents from it.
Following is a bash script to use with xmobar for this purpose.

Add the following line to the commands section in .
 , Run Com ".xmonad/conkyscript" "conky" 300
This makes the script run every 30 seconds.

Then add the following to your  before the  entry.
 .xmonad/conkyscript &
 sleep 6 && xmobar &

Then add  to your template section.

## Simple conky-cli integration
Just place this code:
 Run Com "conky" ["-q", "-i", "1" "conky" 600
in your .

## Troubleshooting
## xmonad unresponsive except for focused window
If xmonad does not respond to clicks and hotkeys but you can still type in the focused window it is likely being caused by the logHook piping to a handle that is not being read.

To solve this add an  or  in the template of your xmobar as well as run the respective command (i.e. ) in the command section. In case of multiple instances of xmobar check that all the bars you are piping to have the StdinReader, if not either add it or remove the bar from  in your logHook.
