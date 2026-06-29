# Xmonad

xmonad is a tiling window manager for X. Windows are arranged automatically to tile the screen without gaps or overlap, maximizing screen use. Window manager features are accessible from the keyboard: a mouse is optional.

xmonad is written, configured and extensible in Haskell. Custom layout algorithms, key bindings and other extensions may be written by the user in configuration files.

Layouts are applied dynamically, and different layouts may be used on each workspace. Xinerama is fully supported, allowing windows to be tiled on several physical screens.

## Installation
Install the  package which provides a very basic configuration, ideally also install  for most notably a more useful desktop configuration as well as additional tiling algorithms, configurations, scripts, etc.

Alternatively, install , the development version, with some additional dependencies; and likewise .

## Starting
Run  with xinit.

Alternatively, select Xmonad from the session menu in a display manager of choice.

Make sure you have the Xterm package installed or have changed the terminal emulator in the configuration. Otherwise you will not be able to do anything in xmonad.

## Configuration
Create the  directory and the  file and edit it as described below.

After changes to  are made, use the  shortcut to recompile and have them take effect.

Because the xmonad configuration file is written in Haskell, non-programmers may have a difficult time adjusting settings.  For detailed HOWTO's and example configurations, we refer you to the following resources:

* xmonad wiki
* xmonad configuration archive
* xmonad FAQ
* Arch Linux forum thread

The best approach is to only place your changes and customizations in  and write it such that any unset parameters are picked up from the built-in def function.

This is achieved by writing an  like this:

 import XMonad

 main = xmonad def
     { terminal    = "urxvt"
     , modMask     = mod4Mask
     , borderWidth = 3
     }

This simply overrides the default terminal and borderWidth while leaving all other settings at their defaults (inherited from the XConfig value def).

As things get more complicated, it can be handy to call configuration options by function name inside the main function, and define these separately in their own sections of your . This makes large customizations like your layout and manage hooks easier to visualize and maintain.

The simple  from above could have been written like this:

 import XMonad

 main = do
   xmonad $ def
     { terminal    = myTerminal
     , modMask     = myModMask
     , borderWidth = myBorderWidth
     }

 myTerminal    = "urxvt"
 myModMask     = mod4Mask -- Win key or Super_L
 myBorderWidth = 3

Also, order at top level (main, myTerminal, myModMask etc.), or within the {} does not matter in Haskell, as long as imports come first.

The following is taken from the 0.9 configuration file template. It is an example of the most common functions one might want to define in their main do block.

 {
   terminal           = myTerminal,
   focusFollowsMouse  = myFocusFollowsMouse,
   borderWidth        = myBorderWidth,
   modMask            = myModMask,
   -- numlockMask deprecated in 0.9.1
   -- numlockMask        = myNumlockMask,
   workspaces         = myWorkspaces,
   normalBorderColor  = myNormalBorderColor,
   focusedBorderColor = myFocusedBorderColor,

   -- key bindings
   keys               = myKeys,
   mouseBindings      = myMouseBindings,

   -- hooks, layouts
   layoutHook         = myLayout,
   manageHook         = myManageHook,
   handleEventHook    = myEventHook,
   logHook            = myLogHook,
   startupHook        = myStartupHook
 }

The package itself also includes a , which is the latest official example  that comes with the xmonad Haskell module as an example of how to override everything. This should not be used as a template configuration, but as examples of parts you can pick to use in your own configuration. It is located in an architecture and version dependant directory in  (e.g. ).

## A base desktop configuration
In  is a better default configuration for average desktop uses. It also helps with problems in some modern programs like Chromium.

It can be added like so:

 import XMonad
 import XMonad.Config.Desktop

 main = xmonad desktopConfig
     { terminal    = "urxvt"
     , modMask     = mod4Mask
     }

## Exiting xmonad
To end the current xmonad session, press . By default,  is the  key.
To confirm exit each time,

## Tips and tricks
## X-Selection-Paste
The keyboard-centered operation in xmonad can be further supported with a keyboard shortcut for X-Selection-Paste.

Also, there exists a function  in  that can be bound to a key using a line like:

Pressing the  key will now paste the mouse buffer in the active window.

## Keyboard shortcuts
Default keyboard shortcuts are listed .

## Targeting unbound keys
If you use xmonad as a stand alone window manager, you can edit the  to add unbound keyboard keys. You just need to find the Xf86 name of the key (such as ) and look it up in . It will give you a keycode (like ) which you can use to add a line like the following into list of keybindings in your :

  ((0,               0x1008FF2A), spawn "sudo systemctl suspend")

You can also search for the Xf86 key name in Graphics.X11.ExtraTypes.XF86 module, and use its  constant (such as ) instead of a keycode as shown in the previous example. You will also need to import the module in your  for the key constant to be available. See more elaborate example with multiple keys in format used by  function:

 import Graphics.X11.ExtraTypes.XF86

 ...

 myKeys = [
    ((0, xF86XK_PowerDown),         spawn "sudo systemctl suspend")
  , ((0, xF86XK_AudioRaiseVolume),  spawn "amixer -D pulse sset Master 10%+")
  , ((0, xF86XK_AudioLowerVolume),  spawn "amixer -D pulse sset Master 10%-")
  , ((0, xF86XK_AudioMute),         spawn "amixer -D pulse sset Master toggle")
  , ((0, xF86XK_MonBrightnessUp),   spawn "brightnessctl set +10%")
  , ((0, xF86XK_MonBrightnessDown), spawn "brightnessctl set 10%-")
  ...
  ]

## Run X () actions by touching the edge of your screen with your mouse
With XMonad.Hooks.ScreenCorners, users can have KDE-like screen corners with XMonad.

## Switch workspaces with ScreenCorners (KDE-like)
Define a series of operations in startupHook:

Then add screenCornerEventHook to handleEventHook:

    myConfig = def {
    ...
        handleEventHook = ...  screenCornerEventHook  ...
    ...
    }

Finally add screenCornerLayoutHook:

    ...
    myLayoutHook = screenCornerLayoutHook $ ......
    ...
    myConfig = def {
    ...
    layoutHook = myLayoutHook
    ...
    }

## Increase the number of workspaces
By default, xmonad uses a set of 9 workspaces.  You can change this by changing the workspaces parameter:

{{hc|xmonad.hs|
import XMonad
import XMonad.Util.EZConfig (additionalKeys)

main=do
  xmonad $ def
    { ...
    , workspaces = myWorkspaces
    , ...
    } `additionalKeys` myAdditionalKeys

myWorkspaces = ++ (map snd myExtraWorkspaces) -- you can customize the names of the default workspaces by changing the list

myExtraWorkspaces = [(xK_0, "0") -- list of (key, name)

myAdditionalKeys =
    [ -- ... your other hotkeys ...
    ] ++ [
        ((myModMask, key), (windows $ W.greedyView ws))
        | (key, ws) > checkKeymap myConfig myKeymap
        ...other operation you defined here...
    ...
} `additionalKeysP` myKeymap}}

## Making room for docks/panels/trays (Xmobar, Tint2, Conky, etc)
Wrap your layouts with avoidStruts from XMonad.Hooks.ManageDocks for automatic dock/panel/trayer spacing:

 import XMonad
 import XMonad.Hooks.ManageDocks

 main=do
   xmonad $ docks def
     { ...
     , layoutHook=avoidStruts $ layoutHook def
     , manageHook=manageHook def  manageDocks
     , ...
     }

If you ever want to toggle the gaps, this action can be added to your key bindings:
 ,((modMask x, xK_b     ), sendMessage ToggleStruts)

## Adding tags to windows
with XMonad.Actions.TagWindows, users can operate on windows having the same tags.

## Equally sized gaps between windows
If your goal is to have equally sized gaps between individual windows and the screen, the following code will not work as expected:
 layoutHook = spacing 10 $ Tall 1 (3/100) (1/2) ||| Full

This makes each window have its own spacing in each direction. If you have two windows side-by-side, the spacing in the middle will be combined, creating a gap that is twice as large as needed.

A workaround is to specify both a screen and a window spacing, but only use the top and left margins for the screen and bottom and right margins for the windows. To do this, change the above code into:

  layoutHook = spacingRaw False (Border 10 0 10 0) True (Border 0 10 0 10) True $ Tall 1 (3/100) (1/2) ||| Full

## Using xmobar with xmonad
xmobar is a light and minimalistic text-based bar, designed to work with xmonad.
To use xmobar with xmonad, you will need two packages in addition to the  package. These packages are  and , or you can use .

Here we will start xmobar from within xmonad, which reloads xmobar whenever you reload xmonad.

Open  in your favorite editor, and choose one of the two following options:

## Quick, less flexible
Common imports:
 import XMonad
 import XMonad.Hooks.DynamicLog

The xmobar action starts xmobar and returns a modified configuration that includes all of the options described in #More configurable.
 main = xmonad =" }

-- Key binding to toggle the gap for the bar.
toggleStrutsKey XConfig {XMonad.modMask = modMask} = (modMask, xK_b)

-- Main configuration, override the defaults to your liking.
myConfig = def { modMask = mod4Mask }
}}

## Verify XMobar config
The template and default xmobarrc contains this.

At last, open up  and make sure you have  in the template and run the plugin. E.g.
{{hc|~/.xmobarrc|
Config { ...
       , commands = [ Run StdinReader, .... ]
         ...
       , template = " %StdinReader% ... "
       }
}}

Now, all you should have to do is either to start, or restart, xmonad.

## Controlling xmonad with external scripts
Here are a few ways to do it,

* use the following xmonad extension, XMonad.Hooks.ServerMode.

* simulate keypress events using  or similar programs. See this Ubuntu forums thread. The following command would simulate the keypress :
 xdotool key Super+n

*  -If you have desktopConfig or EwmhDesktops configured, this is a very easy to use and standard utility.

## Launching another window manager within xmonad
If you are using , as of January of 2011, you can restart to another window manager from within xmonad. You just need to write a small script, and add stuff to your . Here is the script.

And here are the modifications you need to add to your :

{{hc|~/.xmonad/xmonad.hs|
import XMonad
--You need to add this import
import XMonad.Util.Replace

main do
    -- And this "replace"
    replace
    xmonad $ def
    {
    --Add the usual here
    }

}}

You also need to add the following key binding:

Just remember to add a comma before or after and change the path to your actual script path. Now just  (restart xmonad to refresh the configuration), and then hit  and you should have Openbox running with the same windows open as in xmonad. To return to xmonad you should just exit Openbox. Here is a link to adamvo's  which uses this setup Adamvo's xmonad.hs

## KDE and xmonad
The xmonad wiki has instructions on how to run xmonad inside KDE

It also might be a good idea to set a global keyboard shortcut in KDE to start xmonad in case it is accidentally killed or closed.

## Disable plasmashell
You might want to disable plasmashell (the KDE5 thing responsible for desktop background, taskbar, tray, etc.).

   cp /etc/xdg/autostart/plasmashell.desktop ~/.config/autostart/

Then edit  and replace  with . The result will look like this:

## Example configurations
Below are some example configurations from fellow xmonad users.  Feel free to add links to your own.

* brisbin33 :: simple, useful, readable :: config screenshot
* jelly :: Configuration with prompt, different layouts, twinview with xmobar :: xmonad.hs
* MrElendig :: Simple configuration, with xmobar :: xmonad.hs, .xmobarrc, screenshot.
* thayer :: A minimal mouse-friendly config ideal for netbooks :: configs screenshot
* vicfryzel :: Beautiful and usable xmonad configuration, along with xmobar configuration, xinitrc, dmenu, and other scripts that make xmonad more usable. :: git repository, screenshot.
* vogt :: Check out adamvo's config and many others in the official Xmonad/Config archive
* wulax :: Example of using xmonad inside Xfce. :: xmonad.hs, screenshot.
* alex-courtis :: Clean xmonad, xmobar, media keys, screenshot, j4/dmenu; fonts rendered at the DPI reported by the monitor :: xmonad.hs, screenshot.
* TobbeBob123 :: Config for TobbeBob123 where you can see all the keybinding with a simple keybinding (). If you want a whole and complete Xmonad with theme and everything you see in the picture linked. You can run the script called TobbeOS. :: TobbeOS. Xmonad repository, Screenshot.
* AzureOrange :: Split configuration for xmonad built with stack (gaps, layouts, scratchpads, window management and window swallowing etc.) with xmobar, trayer and dmenu. :: xmonad.hs screenshot

## Troubleshooting
## Xfce 4 and xmonad
Use  instead of  after importing  in , e.g. adapting the minimal configuration above:

 import XMonad
 import XMonad.Config.Xfce

 main = xmonad xfceConfig
     { terminal    = "urxvt"
     , modMask     = mod4Mask
     }

Also add an entry to Settings > Session and Startup > Application Autostart that runs .

## Missing xmonad-x86_64-linux
xmonad should automatically create the  file (in ). If this it not the case, grab a configuration file from the xmonad wiki or create your own. Put the  and all others files in  and run this command from the directory:

 $ xmonad --recompile

Now you should see the file.

## Problems with Java applications
If you have problems, like Java application Windows not resizing, or menus immediately closing after you click, see Java#Gray window, applications not resizing with WM, menus immediately closing.

## Empty space at the bottom of gvim or terminals
See Vim#Empty space at the bottom of gVim windows for a solution which makes the area match the background color.

You can also configure xmonad to respect size hints, but this will leave a gap instead. See the documentation on Xmonad.Layout.LayoutHints.

## Chromium/Chrome will not go fullscreen
If Chrome fails to go fullscreen when  is pressed, you can use the XMonad.Hooks.EwmhDesktops extension found in the  package. Simply add the  statement to your :
 import XMonad.Hooks.EwmhDesktops

and then add  to the appropriate place; for example:

After a recompile/restart of xmonad, Chromium should now respond to  (fullscreen) as expected.

## Multitouch / touchegg
Touchégg polls the window manager for the  (in order to fetch a list of windows it should listen for mouse events on.) By default, xmonad does not supply this property. To enable this, use the XMonad.Hooks.EwmhDesktops extension found in the  package.

## Keybinding issues with an azerty keyboard layout
Users with a keyboard with azerty layout can run into issues with certain keybindings. Using the XMonad.Config.Azerty module will solve this.

## GNOME 3 mod4+p changes display configuration instead of launching dmenu
If you do not need the capability to switch the display-setup in the gnome-control-center, just execute

as your user, to disable the xrandr plugin which grabs .

## Chrome/Chromium not displaying defined window border color
Chromium and Chrome browser windows will not have the defined border color per default but a blurred transparent one. This problem is known for a long time but easy to fix.
Activating `Use system title bar and borders` in the browser options should fix it immediately.

## Problems with focused border in VirtualBox
A known issue with Virtualbox (Ticket #6479) can cause problems with the focused window border. A solution can be found by installing a compositing manager like xcompmgr which overrides the incorrect behavior of vboxvideo.

## Steam games (Half-Life, Left 4 Dead, …) and xmonad
There seems to be some trouble with xmonad and Source engine based games like Half-Life. If they do not start or get stuck with a black screen, a workaround is to start them in windowed mode. To do so, right click on the game in your Steam library and choose properties, click on launch options and enter -windowed

Another solution is to float the window of the game using the manage hook. For example, the following line can be used for Half-Life:

  className =? "hl_linux" --> doFloat

This can also be worked around by making xmonad pay attention to EWMH hints and including its fullscreen hook [https://hackage.haskell.org/package/xmonad-contrib/docs/XMonad-Hooks-EwmhDesktops.html:

   main = xmonad $ ewmh def{ handleEventHook =
            handleEventHook def  fullscreenEventHook }

This has a few other effects and makes it behave more akin to fullscreen applications in other WMs.

## LibreOffice - focus flicking between main window and dialog
The LibreOffice UI defaults to the gtk engine outside a desktop environment. This may cause problems with some xmonad configurations resulting in focus rapidly flicking between the LibreOffice main window and any open LibreOffice dialog window. Effectively locking the application. In this case the environment variable  can be set to explicitly force LibreOffice to use another UI theme as outlined in LibreOffice#Theme For instance

 $ export SAL_USE_VCLPLUGIN=gen lowriter

to use the general (QT) UI.

## IntelliJ IDEA and xmonad
## Dialog windows
IntelliJ IDEA has received better support for tiling window managers. But there are still some annoying issues, some of them have simple solutions:

* The Find In Files dialog window closes immediately if mouse pointer moves out of the dialog window boundaries. This only happens with the Find In Files dialog window, and is not reproducible with the Navigate to… dialog. The Find In Files behavior is expected, assuming the default "focus follows mouse" logic of xmonad. The Find In Files window closes when it loses focus on all systems.
:Solution: You can change it by "pinning" the popup — there is a corresponding button in top right corner * When viewing changed files between Git commits (using the Changes Between aaaa and local version bbbb dialog), the window with file-level diffs opens behind the dialog window.
:Solution: Unknown

## Problems with finding shared libraries after update
The xmonad executable is located in . After upgrading xmonad, an old executable might persist and need in that case be removed for xmonad to compile a new executable. Alternatively use .

The recompilation can be automated by adding a pacman hook like the following to  (you may have to first create the  directory):

 [Trigger
 Operation = Upgrade
 Type = Package
 Target = xmonad

 Description = Recompiling xmonad...
 When = PostTransaction
 Exec = /usr/bin/sudo -u YOUR_USERNAME /usr/bin/xmonad --recompile

Where  is the username that you run xmonad from.

In the case that  cannot find any modules at all (including  itself), try regenerating the package database cache:

 # ghc-pkg recache

## Broken/missing XMonad.Prompt and window decorations
XMonad by default uses the font  [https://wiki.haskell.org/Xmonad/Frequently_asked_questions#Tabbed_or_other_decorated_layouts_not_shown.
If this font is missing those windows simply fail to render at all. Easiest fix is to install .
