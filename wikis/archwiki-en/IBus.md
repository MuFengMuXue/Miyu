# IBus

IBus (Intelligent Input Bus) is an input method framework, a type of application that allows for easily switching between different keyboard layouts. When combined with an input method editor, it also allows for typing non-Latin characters using a keyboard that does not natively support them.

## Installation
Install the  package.

Additionally, see Input method#List of available input method editors for a comprehensive list of available input method editors.

## Integration
Set the following the following environment variables:

For Wayland sessions:

 GTK_IM_MODULE=wayland
 XMODIFIERS=@im=ibus
 QT_IM_MODULES=wayland;ibus
 QT_IM_MODULE=ibus

For X11 sessions:

 GTK_IM_MODULE=ibus
 XMODIFIERS=@im=ibus
 QT_IM_MODULE=ibus

To launch IBus on user login, create an autostart entry with the following command:

 ibus start

Add the  flag when used on with Wayland compositor. On the next login IBus will start along with the user session.

## Configuration
See Locale for help with adding non-Latin language support to your system.

See Fonts#Non-latin scripts for a non-exhaustive list of available non-Latin fonts.

## GNOME
GNOME uses IBus by default, so you can simply go to Settings > Keyboard > Input Sources and add a keyboard layout for the language of your choice.

Some non-Latin languages (e.g. Simplified Chinese) need to enable the Show Extended Input Sources option in GNOME Tweaks.

## Other desktop environments
To launch the IBus preferences window, you can:

* Right-click on its tray icon and select Preferences, or
* Find and launch the GUI application IBus Preferences, or
* Run the command  in a terminal

The points of interest here are the keyboard shortcut for Next input method (which is the one you will want to use instead of the default shortcut provided by your desktop environment) and the Input Method tab where you can add or remove the different keyboard layouts (which is where you will want to do this instead of your desktop environment's default layout manager).

## Tips and tricks
## Emoji input
IBus supports the input of emoji icons. Type  and you will see the input prompt change to an underlined e character. You can then type the symbol or name of the emoji you want (e.g. :) or face) and press  to render it. If you are satisfied with the result press  to submit it and exit emoji input mode, or press  for a second time to open a dialog where you can further customize your desired emoji.

See  for more information.

## Unicode input
IBus supports the input of complex Unicode characters. Type  and you will see the input prompt change to an underlined u character. You can then type the code of the Unicode character you want and press  or  to render and submit it.

## Tray icon color
By default, IBus uses a dark blue color to display the language symbol of the currently active layout (e.g. EN). The color value is stored in a gsettings schema, so if you wish to change it you can run the following command:

 $ gsettings set org.freedesktop.ibus.panel xkb-icon-rgba 'COLOR'

The string  should conform to the following guidelines:

The RGBA value can be:

# a color name from X11,
# a hex value in form  where ,  and  are hex digits of the red, green, and blue,
# a RGB color in form  or
# a RGBA color in form  where ,  and  are either integers in the range 0 to 255 or percentage values in the range 0% to 100%, and  is a floating point value in the range 0 to 1 of the alpha.

## Layout switcher display delay
When pressing the Next input method hotkey, IBus displays a small dialog to signify the layout switch. By default this dialog is displayed 400ms after pressing the key, but this value can be changed by the user, with some interesting choices being '0' to display the dialog immediately without any delay, or a negative value (e.g. '-1') to switch the layouts without showing the window at all (which may be useful if you only use two layouts and simply switch from one to the other).

The value is stored in a gsettings schema, so if you wish to change it you can run the following command:

 $ gsettings set org.freedesktop.ibus.general switcher-delay-time 'VALUE'

To show the currently stored value, run the following command:

 $ gsettings get org.freedesktop.ibus.general switcher-delay-time

The string 'VALUE' should conform to the following guidelines:

Set popup delay milliseconds to show IME switcher window. The default is 400.

* 0 = Show the window immediately.
* 0  Do not show the window and switch prev/next engines.

## Using modifier key combinations to switch layouts
For some reason, the IBus preferences GUI will not let you use a subset of modifier key combinations (e.g. ) as the layout switching hotkey. However, IBus stores the hotkey as a string in a gsettings schema, so you can still use such combinations by directly editing that string:

 $ gsettings set org.freedesktop.ibus.general.hotkey triggers "The string  should be any valid modifier key combination written in a format that IBus recognizes, e.g. .

## rxvt-unicode
For rxvt-unicode to work correctly with IBus, you may need to add the following lines to :

 URxvt.inputMethod: ibus
 URxvt.preeditType: OverTheSpot

## Troubleshooting
## Missing packages due to pyenv
If using  to manage python versions and configuration,  dependencies may not be installed on the set global python version. This can happen if the global version is not the one managed by the system (to which dependencies that ibus depends on, such as  are installed). This may result in a running but non-functional ibus setup (ibus is in the system tray, but preferences can not be opened, etc). One way to verify this issue is to attempt to run  and see if any missing dependency errors arise.

To fix this issue, change your pyenv global version to the system version:

 pyenv global system

## Settings removed after restart
If you find your settings are being removed consistently after restart (input methods being reverted), you can confirm the engines set to be preloaded and the order in which they will be loaded:

 $ gsettings get org.freedesktop.ibus.general preload-engines
 ['xkb:us::eng'
 $ gsettings get org.freedesktop.ibus.general engines-order
 'anthy'

To ensure  gets loaded in this case, add it to the  list:

 $ gsettings set org.freedesktop.ibus.general preload-engines "'anthy'"

Changes your changes should be reflected immediately, and should persist across restarts.

## Ibus IME packages only input keyboard's native charset
A possible fix is to set the GTK_IM_MODULE environment variable to xim instead of ibus:

## Keys "stick" after being held down
In certain games, especially those running via Proton, keeping a key pressed for several seconds might result in that key "sticking" (continuing to be registered as pressed) until it is pressed and released again. Limited testing has found that simply killing the IBus daemon is sufficient to resolve the issue.
