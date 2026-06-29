# Accessibility

There are many different methods of providing accessibility to users that have a physical or visual handicap. However, unless a desktop environment is used, the configuration might require some tinkering until one gets it right.

## Desktop environments
Most modern desktop environments ship with an extensive set of features, among which one can find a tool for configuring the accessibility options. Generally, these options can be found listed under those of 'accessibility', or under those of the corresponding input device (e.g. 'keyboard' and 'mouse'). For example, with GNOME and KDE.

## Xorg accessibility features
The Xorg server has features (accessx) for physical assistance by setting parameters via the X keyboard extension. This section covers examples.

For speech recognition, see also Text to speech

## Sticky keys with xserverrc
One method of enabling desktop environment-independent accessibility function is by passing it through X, given that it is build with XKB support. This can be done by setting parameters for the X server, as specified in its man page:
 [ timeout [ timeout_mask [ feedback [ options_mask  ] ] ]
               enables(+) or disables(-) AccessX key sequences (Sticky Keys).

 -ardelay milliseconds
               sets the autorepeat delay (length of time in milliseconds  that
               a key must be depressed before autorepeat starts).

 -arinterval milliseconds
               sets  the  autorepeat  interval (length of time in milliseconds
               that should elapse between autorepeat-generated keystrokes).

These parameters must be placed in the file , which you may need to create.

For example, to enable Sticky Keys without timeout and without audible or visible feedback, the following can be used:
 if [ -z "$XDG_VTNR" ]; then
   exec /usr/bin/X -nolisten tcp "$@" +accessx 0 0x1e 0 0xcef
 else
   exec /usr/bin/X -nolisten tcp "$@" vt$XDG_VTNR +accessx 0 0x1e 0 0xcef
 fi

Note that once X has started, e.g. by executing , it still requires you to press the shift key 5 times to enable Sticky Keys. Unfortunately, this is needed each time X starts. Alternatively, a script can be used to automate this process.

Similar to most implementations, Sticky Keys can be disabled by pressing a modifier key and any other key at the same time.

## Remapping mouse buttons
By using xmodmap, you can map functions to mouse buttons independent of your graphical environment. For this, you need to know which physical button on your mouse is read as which number, which can be found by a tool such as . Generally, the physical buttons of left, middle, and right are read as the first, second, and third button, respectively.

Once you have acquired these, continue by creating a configuration file on a suitable location, e.g. . Next, open the file with your favourite editor, and write the keyword  followed by an enumeration of the previously-found number of mouse buttons.

For example, a three button mouse with a scroll wheel is able to provide five physical actions: left, middle, and right click, as well as scroll up and scroll down. This can be mapped to the same functions by using the following line in the configuration file:
 pointer = 1 2 3 4 5

Here, the location will tell the action required to perform an internal mouse-button function. For example, a mapping for left-handed people (left- and right button switched) might look like
 pointer = 3 2 1 4 5

When you are done, you can test and inspect your mapping by running :
 $ xmodmap ~/.mouseconfig
 $ xmodmap -pp

Once satisfied, you can enable it on start by placing the first line in .

## Mouse keys
Mouse keys is a Xorg feature (like StickyKeys) to use the keyboard (especially a numeric keypad) as a pointing device. It can replace a mouse, or work beside it. It is disabled by default. You can use

 $ xset q | grep "Mouse Keys"

to see status. To enable it for a session:

 $ setxkbmap -option keypad:pointerkeys

If you use a xmodmap configuration, be aware setxkbmap resets it.

To enable Mouse keys permanently, add

 Option "XkbOptions" "keypad:pointerkeys"

to the keyboard configuration file. This will make the  shortcut toggle mouse keys.

For more, see Keyboard configuration in Xorg#Using X configuration files and X keyboard extension#Mouse control for advanced configuration.

## Generic solutions
The following solutions are agnostic the chosen display server and desktop environment.

## Sticky keys in a TTY
In order to enable Sticky Keys in a TTY, you require to know the exact keycodes of the keys to be used. These can be found by a tool like  or . Alternatively, you can inspect the output of dumpkeys, provided that the current keymap is correct.

For example, a Logitech Ultra-X will provide the following keycodes for the modifier keys:

 LCtrl = 29
 LShift = 42
 LAlt = 56
 RShift = 54
 RCtrl = 97

Next, use dumpkeys to determine the range of the keycodes:

Continue by creating a new file with a suitable name, e.g. "stickyKeys", and use your favourite editor to combine the previously-found information with the desired key function.

In case of the keycodes found earlier, you would get:

 keymaps 0-63
 keycode 29 = SCtrl
 keycode 42 = SShift
 keycode 56 = SAlt
 keycode 54 = SShift
 keycode 97 = SCtrl

Here, the letter "S" in front of a modifier key denotes that we want the sticky version of that key.

Load your new mapping by running the following command:

 # loadkeys ./stickyKeys

If you are satisfied by the results, then move the file to a suitable directory. To have it enabled on boot, see the following systemd unit:

## Sticky keys with keyd
keyd () is a system-wide key remapping daemon for Linux that can be configured to provide sticky keys functionality for Xorg and Wayland, and for the Linux virtual console.

To enable this functionality, first install and enable . Next, create the configuration file:

You can now enable/start the .

## Visual assistance
As with physical assistance, most modern desktop environments ship with an extensive set of features to tweak the visual aspects of your system. Generally, these options can be found listed under those of 'accessibility' or 'visual assistance'. Alternatively, useful options might be found in the settings of the individual applications.

## Speech recognition
See Speech recognition.

## Console and virtual terminal emulators
* Edit .
* Edit .

## Known issues
Configuration of input devices is not recognized by software that circumvents the software layer, e.g. Wine, VirtualBox, and QEMU.

## Troubleshooting
Most graphical applications should work out of the box, such as Gtk-, Qt- or Gecko-based ones. You can verify the functionality by running . The application of choice should appear and have a deeply nested tree structure of children. Issues may arise if:

* The application is Chromium- or Electron-based. These programs typically need both the environment variable , and an additional argument  when launching. For Chrome you can replace the latter step with enabling the accessibility options inside , however this seems to not persist after restart.
* The application is Java-based. In this case, you need to install the ATK bridge  (depending on your Java version).
* In the rare case that the application is an exotic, old application built with , such as some programs that have not been maintained since 2015, you need to install .
* As a last resort, any of these other environment variables may help: , , , , .

## Disable accessibility
If you do not need accessibility and want to save processes a little:

* Set the  and  environment variables.
* Mask the  user unit.
* Override the  and  dbus services.
* Override the  autostart entry.

You can also use NoExtract in  to skip the files from being installed.
