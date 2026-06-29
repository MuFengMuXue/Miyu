# Logitech Marble Mouse

The Logitech Marble Mouse is a pointing device with four buttons and a trackball, also known as the Trackman Marble. The Marble Mouse is usable either left- or right-handed. It requires some configuration to enable scrolling with the trackball. For a detailed image, see: Logitech Marble Mouse (or here).

## Installation
The mouse is detected at boot time or whenever it is "hot-plugged" into a booted system, automatically. No special installation is required.

## Basic function
The Logitech Marble Mouse has a trackball and four buttons, namely Large left button, Large right button, Small left button and Small right button. It does not have a scroll wheel, neither it has a middle button (conventionally the button placed "under the wheel"). As such, default usability is bad on modern systems and applications that rely heavily on those functions. However, it is possible to enable both of those functions with some simple configurations (see #Button mapping and #Scroll modifier).

When no additional configuration is specified, buttons are mapped to these functions:

{| class="wikitable"
|+ Default Button Actions
! Button !! Result
|-
| Large left button || left-click
|-
| Both large buttons || middle-click 1
|-
| Large right button || right-click
|-
| Small left button || browser back
|-
| Small right button || browser forward
|}

# Both large buttons clicked simultaneously creates a middle-click emulated event. This is enabled by default for pointer devices without a middle button.

{| class="wikitable"
|+ Non-button Input Actions
! Action     !! Result
|-
| Roll ball down || move cursor down
|-
| Roll ball up || move cursor up
|-
| Roll ball left || move cursor left
|-
| Roll ball right || move cursor right
|}

By default, Logitech Marble Mouse has no way of performing scroll events. However, scrolling is possible by assigning a scroll modifier, i.e. a button that when held down trackball movements are converted to scroll events.

## Button mapping
In modern systems, the best way to remap buttons is to configure mappings in udev/hwdb that apply directly in the kernel (check Map scancodes to keycodes for details).

The default scancode-to-event mappings for Logitech Marble Mouse buttons are as follows:

{|class="wikitable"
|-
! Button !! Scancode !! Default Event
|-
| Large left button ||  ||
|-
| Large right button ||  ||
|-
| Small left button ||  ||
|-
| Small right button ||  ||
|}

There is no mapping for  event by default, but it's possible to remap one of the  scancodes to the  event and make the respective button to behave like a proper middle button.

For example, to remap the Small left button to middle button, create an  file as follows (pay attention to case and indentation):

After that, update the hardware database index and manually force udev to trigger the new rule:

 # systemd-hwdb update
 # udevadm trigger

It is possible to check which event is being raised by each button press by using . If the remapping worked, pressing Small left button should output events like this:

## Troubleshooting libinput quirk
In some systems Logitech Marble Mouse libinput configuration includes a "quirk" that completely disables BTN_MIDDLE events, so after remapping a button to btn_middle in hwdb, said button will "stop working" completely (even if  still reports  events). It's possible to check this using , by running  as root and making sure that clicking the remapped button does not output any events.

To fix that, create an override quirks file as follows (if the file already exists, append the following contents to it):

then reboot to make sure the config takes effect.

Now clicking the remapped button should output events like this:

## Scroll modifier
One huge limitation for the Logitech Marble Mouse is the lack of a scroll wheel or scroll ring. This limitation is overcome by assigning a scroll modifier: a mouse button which allows the trackball to scroll. When the scroll modifier is held, the trackball movement becomes scroll events.

When defining the scroll modifier button, the ID used to specify the button is a number associated with the event, and not directly the hardware button. That means if buttons were remapped in the kernel (#Button mapping), the ID used will correspond to the remapped button. The event ID numbers (and default buttons) are in the table below:

{|class="wikitable"
|-
! Default Hardware Button !! Event !! Event number
|-
| Large left button ||  || 1
|-
| (none) ||  || 2  †
|-
| Large right button ||  || 3
|-
| Small left button ||  || 8
|-
| Small right button  ||  || 9
|}

The scroll modifier button is implemented in libinput, but libinput is made so the upper layers are the ones responsible for configurations (check libinput for details), so the proper way to define the scroll modifier will depend on whether Wayland or X11 is used, and also on the desktop environment. The following sections show how to configure the scroll modifier (as well as other settings) in different systems.

## GNOME 3 and Wayland
GNOME provides a limited set of configuration options for enabling a scroll modifier and adjusting the acceleration behaviour of the mouse cursor. These setings can be modified using  and are also available via dconf under .

Change the following option to assign a button as a scroll modifier:

 $ gsettings set org.gnome.desktop.peripherals.trackball scroll-wheel-emulation-button

, where ' is the ID of the libinput event that should act as the modifier (see #Scroll modifier). To deactivate the scroll modifier'', set the  to 0.

It's also possible to enable scroll modifier lock by setting:

 $ gsettings set org.gnome.desktop.peripherals.trackball scroll-wheel-emulation-button-lock true

Middle-click emulation is enabled by default for Logitech Marble Mouse and cannot be disabled in settings. It will be disabled however when the libinput quirk is modified so that a BTN_MIDDLE event is enabled (see #Troubleshooting libinput quirk). If after that one still wishes to use middle-click emulation, it can be reenabled with:

 $ gsettings set org.gnome.desktop.peripherals.trackball middle-button-emulation true

The trackball can be configured to either use a "flat" or "adaptive" acceleration profile or to just use its "default" one. To do that, set

 $ gsettings set org.gnome.desktop.peripherals.trackball accel-profile

to the desired value.

## Sway and Wayland
When running Wayland, the aforementioned configuration files have no effect. Sway provides a limited set of configuration options for enabling mouse wheel emulation and adjusting the acceleration behaviour of the mouse cursor.
In your sway configuration file, add the following section to enable scrolling with the marble while the small left button is pressed:

 input "1133:50184:Logitech_USB_Trackball" {
     scroll_method on_button_down
 }

## Hyprland
Hyprland also supports a limited set of options for wheel emulation. Add the following block your configuration:

{{hc|hyprland.conf|2=
device {
    name = logitech-usb-trackball
    scroll_method = on_button_down
}
}}

You can also configure  or  per the Hyprland input documentation.

The middle click emulation when clicking both the left mouse button and the right mouse button simultaneously seems to work without additional configuration.

## Plasma and Wayland
When running a Plasma Desktop session in Wayland, you can configure scrolling with , you just have to find the right event number, which you can determine from , for example:

 event="$(basename $(readlink /dev/input/by-id/usb-Logitech_USB_Trackball-event-mouse))"
 qdbus org.kde.KWin /org/kde/KWin/InputDevice/$event org.kde.KWin.InputDevice.scrollOnButtonDown true

By default the small left button is used. If you want to use the small right button, set

 qdbus org.kde.KWin /org/kde/KWin/InputDevice/$event org.kde.KWin.InputDevice.scrollButton 276

For other buttons, follow the table below:
{| class="wikitable"
! Button           !! Kwin button code    !! Function (default)
|-
| Large button left || 272 || normal click
|-
| Large button right || 273 || right click
|-
| Small button Left || 275 || browser forward
|-
| Small button right || 276 || browser back
|}

## X11
When using an X11 based desktop, libinput can be configured using the X11 configuration files and utilities. It requires that  be installed. Configurations can be added to file . If the file exists, append the contents to it's end. Some basic configuration samples are shown below.

This:

* Enables horizontal and vertical scrolling by pressing and holding the BTN_SIDE button (Small left button by default) while moving the trackball.
* Enables middle-click emulation by pressing the two large buttons simultaneously.

If you remapped a real button to BTN_MIDDLE as per #Button mapping, you can use the following:

This:

* Enables horizontal and vertical scrolling by pressing and holding the BTN_MIDDLE event (i.e. the real button remapped to this event) while moving the trackball.
* As the BTN_MIDDLE event (ID 2) is enabled and remapped to a real button, there is no need for "MiddleEmulation". However, it can still be enabled if necessary.

Some other notable configuration options are:

 Option "ScrollButtonLock" "true" # enable scroll modifier lock mode
 Option "LeftHanded" "true" # swap left and right buttons
 Option "HorizontalScrolling" "false" # disable horizontal scrolling

Check  for a comprehensive list of options.

## Additional tweaks
## Console (gpm)
See Console mouse support for details. Within the console you can use  with type option set to imps2. Edit ' such that:

 GPM_ARGS="-m /dev/input/mice -t imps2"

This lets you use the large left button for selecting text and the right button to extend the selection. The small left button acts as a middle-click; it pastes the selection.
