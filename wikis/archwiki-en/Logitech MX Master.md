# Logitech MX Master

Logitech MX Master is a series of computer mice.

## Usage
The mouse should work with no special configuration if using the unified receiver USB dongle that comes with your purchase. Plug the dongle into your PC. Make sure the mouse is set to Channel 1 by pressing the  button underneath the mouse, then press and hold the button until it starts blinking quickly. It should turn solid shortly after a few seconds, and now be connected. If you want to connect to an unconnected receiver, see Logitech Unifying Receiver

To use Bluetooth, change the channel on the bottom of the mouse, and click the  button. Now, search for the mouse with a Bluetooth manager of your choice and pair. In future it should connect as soon as you switch to that channel when your Bluetooth is active. If you have problems with the mouse not showing when scanning, see Bluetooth#Device does not show up in scan.

The mouse exists in 4 major versions, the 3rd iteration having 5 revisions, but the functionalities are the same:

* MX Master,
* MX Master 2s,
* MX Master 3:

:{| class="wikitable sortable"
|+ MX Master 3 variations
|-
! Name !! Release !! Supports? !! Sold with?
|-
| MX Master 3 || 2019 || Unifying || Unifying + USB A-C
|-
| MX Master 3 for Mac || 2020 || Unifying || USB C-C
|-
| MX Master 3 for business || 2021 || rowspan="2" | Bolt || rowspan="2" | Bolt + USB A-C
|-
| MX Master 3S || rowspan="2" | 2022
|-
| MX Master 3S for Mac || Bolt || USB C-C
|}

* MX Master 4:

:{| class="wikitable sortable"
|+ MX Master 4 variations
|-
! Name !! Release !! Supports? !! Sold with?
|-
| MX Master 4 || 2025 || Bolt || Bolt + USB C-C
|-
| MX Master 4 for Mac || 2025 || Bolt || Bolt + USB C-C
|}

The new MX Master 4 haptic lacks some of the basic functionality controls like haptics or force sensing buttons which are only on the master branch but should be soon added to a release version. Pairing on a bolt receiver just works.

## Mappings for extra buttons
Install  or () to customize mouse settings:

* Easy programmable buttons.
* DPI selection.
* Smartshift (hyperfast and click-to-click wheel mode).
* HiresScroll.
* Gestures.

Both packages are mostly stable with the older Logitech Unifying Receiver.

LogiOps added Bolt support in v0.3.0, but it still has some issues. Using Bluetooth may help avoid these issues.

Solaar supports Bolt, including device pairing, but Solaar is currently not fully compatible with Wayland.

It is possible to simply use #Xbindkeys and tweak the desktop shortcuts to obtain some customization, but with some caveats (see notes below).

## Logiops
It can be executed as application via command line by running

 # logid

Or started as .

The configuration lives in . But the package comes with no configuration. One needs to create this specifying the name of the device to be used. To obtain that name launching from cli

 # logid -v

The name of the detected device is printed.

Then you can create the configuration file.

## Examples
See the configuration format documentation for more detail, including the list of CIDs (button codes) and the list of key codes.

This minimal configuration file simply makes each button work as a normal mouse button, ignoring gestures.  It will allow the extra buttons to be used normally, such as in games and by Xbindkeys (see below).

{{hc|/etc/logid.cfg|2=
devices: ({
  name: "Wireless Mouse MX Master 3";

  // A lower threshold number makes the wheel switch to free-spin mode
  // quicker when scrolling fast.
  smartshift: { on: true; threshold: 20; };

  hiresscroll: { hires: true; invert: false; target: false; };

  // Higher numbers make the mouse more sensitive (cursor moves faster),
  // 4000 max for MX Master 3.
  dpi: 1500;

  buttons: (

    // Make thumb button 10.
    { cid: 0x53; action = { type: "Keypress"; keys: }; },

    // Make top button 11.
    { cid: 0x56; action = { type: "Keypress"; keys: ["KEY_BACK";    }; }

  );
});
}}

For a more fully-featured configuration, see logid.example.cfg or this one:

{{hc|/etc/logid.cfg|2=
devices: (
{
    name: "Wireless Mouse MX Master 3";
    smartshift:
    {
        on: true;
        threshold: 30;
    };
    hiresscroll:
    {
        hires: true;
        invert: false;
        target: false;
    };

    thumbwheel:
    {
        divert: true;
        invert: false;

        left: {
                mode: "OnInterval";
                interval: 2;
                action: {
                        type: "Keypress";
                        keys: };
        };
        right: {
                mode: "OnInterval";
                interval: 2;
                action: {
                        type: "Keypress";
                        keys: ["KEY_VOLUMEUP";
                };
        };

        tap: {
            type: "Keypress";
            keys: };

    };
    dpi: 1000;

    buttons: (
        {
            cid: 0xc3;
            action =
            {
                type: "Gestures";
                gestures: (
                    {
                        direction: "Up";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: ["KEY_LEFTCTRL", "KEY_F10";
                        };
                    },
                    {
                        direction: "Down";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: "KEY_F7";
                        };
                    },
#                    {
#                        direction: "Left";
#                        mode: "OnRelease";
#                        action =
#                        {
#                            type: "CycleDPI";
#                            dpis: 500, 1000, 1500, 2000, 3000, 4000;
#                        };
#                    },
                    {
                        direction: "Left";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: "KEY_LEFT";
                        };
                    },

#                    {
#                        direction: "Right";
#                        mode: "OnRelease";
#                        action =
#                        {
#                            type = "ToggleHiresScroll";
#                        }
#                    },
                    {
                        direction: "Right";
                        mode: "OnRelease";
                        action =
                        {
                            type: "Keypress";
                            keys: "KEY_RIGHT";
                        }
                    },

                    {
                        direction: "None"
                        mode: "NoPress"
                    }
                );
            };
        },
        {
            cid: 0xc4;
            action =
            {
                type = "ToggleSmartshift";
            };
        },
        {
            # Next tab instead of fwd in history, Comment to default behavior
            cid: 0x53;
            action =
            {
                type :  "Keypress";
                keys: "KEY_PAGEUP";
            };
        },
        {
            # Previous tab instead of back in history, Comment to default behavior
            cid: 0x56;
            action =
            {
                type :  "Keypress";
                keys: "KEY_PAGEDOWN";
            };
        }
    );
},
{
# Another device to configure
name: "Other Logitech USB Receiver";

}
);
}}

## Xbindkeys
List of events sent by mouse:

{|class="wikitable"
! Physical action
! Defaults as
! With minimal logidconfiguration above
|-
|Left button
|
|
|-
|Press to wheel
|
|
|-
|Right button
|
|
|-
|Scroll wheel up
|
|
|-
|Scroll wheel down
|
|
|-
|Scroll hor_wheel right (up)
|
|
|-
|Scroll hor_wheel left (down)
|
|
|-
|Side-bottom button
|
|
|-
|Side-top button
|
|
|-
|Thumb button
|
|
|-
|Press "i" button under wheel
|
|
|}

Notes:

* It is impossible to move mouse cursor while thumb button is pressed, but possible to use any other actions (pressing buttons and scrolling wheels).  event is sent only after releasing thumb button.  Using logid to reassign this button removes this limitation.
* If you wish, you can get experience of thumb button like in Windows or Mac. In KDE go to System settings > Shortcuts > Global Shortcuts > KWin > Show all windows from all desktops. It is set to  by default. Set  for this action and apply settings.
* "I" button under wheel is undetectable in Linux by default, but works as switching wheel between free and rattle mode.  With logid it can be reassigned for use.
* Logitech gestures (moving mouse up/down/left/right while thumb pressed) are not detected in Linux, but are implemented in software by logid.

The vertical wheel and the two buttons near it should work right away, however the thumb button requires some special treatment, and you might want to remap the rest.

To remap the buttons of the mouse you can use the packages  and .

xbindkeys will redirect the buttons and xte (which is included in xautomation) will execute the custom key presses. To do so, create a configuration file named  in your home directory.

Here is a sample configuration for the vertical scroll wheel and the two buttons near it:

 # thumb wheel up => increase volume and unmute
 "amixer -D pulse set Master 4000+ unmute"
    b:6
 # thumb wheel down => lower volume
 "amixer -D pulse set Master 4000-"
    b:7
 # backward button => previous song
 "xte 'key XF86AudioPrev'"
    b:8
 # forward button => next song
 "xte 'key XF86AudioNext'"
    b:9

If using PulseAudio (more info here):

 # thumb wheel up => increase volume
 "pactl set-sink-volume @DEFAULT_SINK@ +2%"
    b:6
 # thumb wheel down => lower volume
 "pactl set-sink-volume @DEFAULT_SINK@ -2%"
    b:7

If you prefer to get a visual feedback on how the volume level changes you could use the following lines instead
(Tested in GNOME and KDE)

 # thumb wheel up => increase volume
 "xte 'key XF86AudioRaiseVolume'"
    b:6
 # thumb wheel down => lower volume
 "xte 'key XF86AudioLowerVolume'"
    b:7

Now start , preferably add that to the autostart list of your desktop environment.

The thumb button is special. With the Logitech software available for Windows and Mac, you would be able to map up to 5 actions to it: by pressing the button or by pressing the button and moving the mouse in one of four directions. As of November 2015, there is no way to enable the direction feature using Arch.

If you look at the keys the button triggers you will notice that it sends a series of keys, confusing xbindkeys. You need to add a short sleep here so xbindkeys will only react on the first keys send so we can at least map one action to it:

 # thumb button => play/pause music
 # Credit to gregmuellegger https://bbs.archlinux.org/viewtopic.php?pid=1551271#p1551271
 # We need a sleep here since the button triggers a few more key codes.
 # It also triggers Control+Mod2+Control_L and Alt+Mod2+Alt_L. The sleep
 # prevents that X receives those keypresses simultaniously. Therefore they
 # might interfere and trigger unwanted actions. By the sleep we make sure that
 # the Alt+Left is receive as distinct event.
 "sleep 0.1 && xte 'key XF86AudioPlay'"
    m:0xc + c:23

Remember that all changes to  require a restart of the xbindkeys process:

 $ pkill xbindkeys && xbindkeys

## Power
Battery status can be read as described on Logitech Unifying Receiver. e.g. Solaar () has a system tray utility.

## Smart shift
Smart shift is where the scroll wheel switches from click-to-click to smooth scrolling automatically, based on the speed at which it is being spun.

## Logiops
Any mouse button can be assigned to switch between modes.  The default settings are with the smart-shift threshold around 20 and the top button (just below the wheel) used to toggle between always-smooth and smart-shift (clicky when scrolling slowly only).  Increasing the threshold number requires the wheel to be spun faster before it will switch into smooth-scrolling mode.

To reproduce the default settings, use this snippet in the configuration file as shown above:

{{hc|/etc/logid.cfg|2=
...
  smartshift: { on: true; threshold: 20; };
  buttons: (
    // Make top button (0xc4) switch modes
    { cid: 0xc4; action = { type = "ToggleSmartshift"; }; },
...
}}

Change the threshold or use a different button (cid) as needed.

## Solaar
Instead of logid, Solaar can also be used to change the sensitivity of changing the mouse wheel mode (between hyperfast and click-to-click), install . A slider appears that can be set somewhere between 0 and 50 (inclusive). 0 means always in hyperfast mode, 50 means always in click-to-click mode.

To change the sensitivity, change this value somewhere between 0 and 50.

## Troubleshooting
## Laggy mouse movements in Bluetooth mode
See Bluetooth mouse#Mouse lag

## Sticky mouse in Bluetooth mode after few seconds idling
See Power management#USB autosuspend to blacklist your device.

## Thumbwheel horizontal scrolling behavior different (inverted) compared to under Windows
This is a known behavior added in  (to correct the weird behavior (quirks) that the vertical/horizontal scroll wheels of this mouse (and many other Logitech products, too) is configured differently. However if one is to use this mouse on different operating systems frequently and finds this autocorrection behavior inconvenient, it is possible to specifically turn it off:

See also [https://gitlab.freedesktop.org/libinput/libinput/-/tree/main/quirks for a list of quirks patched for other devices.

## Missing scroll events on MX Master 3
When the scroll wheel is in ratcheting mode and one switches the direction of scroll (scroll up by two steps and down by one step instantly), the last step may not be picked up. This could mean unpredictable scrolling in firefox when smooth scrolling is disabled, or when one uses the scroll wheel to switch tabs in qt widget based applications. This is because MX Master 3 is registered as a high resolution scrolling device, which continues to send high resolution events even in ratcheting mode To filter out the high resolution events, use

To find the product IDs (as they vary between manufacturing runs and connection type), first find the device node:

 # libinput list-devices | grep "MX Master 3" -A 5 | grep Kernel | awk '{print $2}'
 /dev/input/event9

Then query the device node for its IDs:

 # udevadm info -a /dev/input/event9 | grep id/
     ATTRS{id/product}=="4082"
     ATTRS{id/vendor}=="046d"

Copy the  and  IDs into the  and  fields, prefixing them with  as shown.

## Hi-resolution scrolling
The Logitech MX Master 3S supports high-resolution (fractional) scrolling via its electromagnetic scroll wheel. On Arch Linux, whether hi-res scrolling works depends on the connection method used.

When connected via the Logitech Bolt Receiver, the MX Master 3S only exposes standard mouse wheel events. In this mode, libinput reports fixed scroll steps (e.g. ), and smooth or fractional scrolling is not available. This is a limitation of the kernel driver, which does not expose high-resolution scroll events for this device over the Bolt Receiver. [https://www.phoronix.com/news/Linux-Disable-HiRes-Scroll-USB

When connected over Bluetooth, the MX Master 3S exposes fractional scroll events correctly. In this configuration,  reports smaller scroll deltas (e.g. ), and hi-resolution scrolling works as expected. This connection method is therefore recommended for users who want smooth scrolling behavior.

Users may still notice a small dead-zone or occasional jump when scrolling very slowly. This behavior is caused by the mechanical FreeSpin wheel and HID report granularity and is considered normal.
