# Backlight

Screen brightness might be tricky to control. On some machines physical hardware switches are missing and software solutions may not work well. However, it is generally possible to find a functional method for a given hardware. This article aims to summarize all possible ways to adjust the backlight.

There are many ways to control brightness of a monitor, laptop or integrated panel (such as the iMac). According to these discussions and this wiki page the control method can be divided into these categories:

* brightness is controlled by vendor-specified hotkey and there is no interface for the OS to adjust the brightness.
* brightness is controlled by either the ACPI, graphic or platform driver. In this case, backlight control is exposed to the user through  which can be used by user-space backlight utilities.
* brightness is controlled by writing into a graphics card register through setpci.

## Hardware interfaces
## ACPI
The brightness of the screen backlight is adjusted by setting the power level of the backlight LEDs or cathodes. The power level can often be controlled using the ACPI kernel module for video. An interface to this module is provided via a  directory at .

The name of the directory depends on the graphics card model.

In this case, the backlight is managed by an ATI graphics card. In the case of an Intel card, the directory is called . In the following examples,  is used. If you use an Intel card, simply replace  with  in the examples.

The directory contains the following files related to brightness:

The maximum brightness can be read from , like this:

The brightness can be set by writing a number to . However, its value often differs from , and it's device dependent. (See also #Recent (2025) AMD changes.)

 # echo 5 > /sys/class/backlight/acpi_video0/brightness

Attempting to set a brightness greater than the maximum results in an error. By default, only  can change the brightness by this method.

To allow users in the  group to change the brightness, the  file's group and permissions must be changed at boot. The intuitive approach of using  and  keys in a udev rule does not work here. Those keys only manage device nodes under , and the backlight device has no  node. The brightness file is a sysfs attribute whose permissions (0644, root-owned) are hardcoded in the kernel driver via  and are not affected by udev permission keys.

The reliable approach is to use a  rule that explicitly invokes  and  on the file by its full literal path. The rule must also include a  match to target only the specific backlight device. Without it, the rule fires on every backlight subsystem event, causing a flood of errors in the system journal until the sysfs file becomes available.

First, find your backlight device name:
 $ ls /sys/class/backlight/
Then create the rule, substituting your device name (e.g. ,  or ):

After creating the file, either reboot or run:
 # udevadm control --reload
 # udevadm trigger --subsystem-match=backlight --action=add

## Kernel command-line options
Sometimes ACPI does not work well due to different motherboard implementations and ACPI quirks. This results in, for instance, inaccurate brightness notifications. This includes some laptops with dual graphics (e.g., NVIDIA/AMD dedicated GPU with Intel/AMD integrated GPU). Additionally, ACPI sometimes needs to register its own  backlight even if one already exists (such as ), which can be done by adding one of the following kernel parameters:

 acpi_backlight=video
 acpi_backlight=vendor
 acpi_backlight=native

## Udev rule
If the ACPI interface is available, the backlight level can be set at boot using a udev rule:

{{hc|/etc/udev/rules.d/81-backlight.rules|2=
# Set backlight level to 8
SUBSYSTEM=="backlight", ACTION=="add", KERNEL=="acpi_video0", ATTR{brightness}="8"
}}

## setpci
In some cases (e.g. Intel Mobile 945GME it is possible to set the register of the graphics card to adjust the backlight. It means you adjust the backlight by manipulating the hardware directly, which can be risky and generally is not a good idea. Not all of the graphics cards support this method.

When using this method, you need to use  first to find out where your graphics card is.

 # setpci -s 00:02.0 F4.B=0

## External monitors
Display Data Channel Command Interface (DDC/CI) can be used to communicate with external monitors implementing Monitor Control Command Set (MCCS) over I2C. DDC can control brightness, contrast, inputs, etc on supported monitors. Settings available via the On-Screen Display (OSD) panel can usually also be managed via DDC. The kernel module  may need to be loaded if the  devices do not exist.

 can be used to query and set brightness settings:

 # ddcutil setvcp 10 70

Alternatively, one may use  to expose external monitors in sysfs. Then, after loading the  kernel module, one can use any backlight utility.

## Switch off the backlight
Switching off the backlight (for example when one locks a notebook) can be useful to conserve battery energy. Ideally the following command should work for any Xorg graphical session:

 $ xset dpms force off

The backlight should switch on again on mouse movement or keyboard input. Alternately,  could be used for a similar effect.

If the previous commands do not work, there is a chance that vbetool may work. Note, however, that in this case the backlight must be manually activated again. The command is as follows:

 $ vbetool dpms off

To activate the backlight again:

 $ vbetool dpms on

For example, this can be put to use when closing the notebook lid using acpid.

## Save and restore functionality
The systemd package includes the service , which is enabled by default and "static". It saves the backlight brightness level at shutdown and restores it at boot. The service uses the ACPI method described in #ACPI, generating services for each folder found in . For example, if there is a folder named , it generates a service called . When using other methods of setting the backlight at boot, it is recommended to stop systemd-backlight from restoring the backlight by setting the kernel parameter . See  for details.

Additionally, the  and  utilities support save and restore functionality. These two may be more useful if one wishes to restore the screen brightness on a per-user basis, however no systemd units are provided to accomplish this.

## Backlight utilities
{| class="wikitable sortable"
! Package name
! Controls keyboard backlights
! Reacts to ambient brightness
! Language
! License
! Notes
|-
|
|
|
| C
| MIT
| Simple notification daemon for the ACPI interface (reads )
|-
|
|
|
| Python3
| GPL-3.0-or-later
| "xbacklight" executable provided
|-
|
|
|
| C
| MIT
| Extremely small and simple. Supports relative adjustments.
|-
|
|
|
| Python3
| ISC
| Uses logind interface. Restricted to local users, but does not require suid or video group membership.
|-
|
|
|
| C
| GPL-2.0
| Dims the screen when there is no user input for some time.
|-
|
|
|
| C
| MIT
| -
|-
|
|
|
| C
| GPL-3.0-only
| Supports smooth and relative adjustments.
|-
|
|
|
| C
| GPL-3.0-or-later
| Manages screen temperature (Xorg only) and smoothly dims brightness after a timeout. Supports ambient light sensors [https://github.com/FedeDP/Clightd/wiki/Sensors. Can turn webcam into an ambient light sensor.
|-
|
|
|
| C
| GPL-3.0-or-later
| -
|-
|
|
|
| C
| AGPL-3.0
| Reacts to key presses.
|-
|
|
|
| C
| GPL-3.0-only
| Dependency free. Does not rely on X server.
|-
|
|
|
| Shell
| MIT
| -
|-
|
|
|
| Bash
| GPL
| Macbook screen/keyboard backlight CLI and auto-adjust on ambient light.
|-
|
|
|
| Rust
| ISC
| Automatic brightness adjustment based on screen contents and ambient light. Can use webcam or time to simulate ambient light sensor. Supports keyboards and external monitors. Uses wlroots.
|-
|
|
|
| C
| MIT
| Simple notification daemon for X11 (reads the RandR backlight property)
|-
|
|
|
| Perl
| GPL-2.0
| Small Perl script similar to xbacklight but using sysfs drivers.
|}

## light
Install  and add your user to the  user group.

Increase backlight brightness by 5 percent:

 $ light -A 5

Decrease backlight brightness by 5 percent:

 $ light -U 5

Set backlight brightness to 100 percent:

 $ light -S 100

## Using DBus with GNOME
Brightness can also be adjusted as the GNOME controls do. Changes are reflected in the GNOME UI using this method.

 $ gdbus call --session --dest org.gnome.SettingsDaemon.Power --object-path /org/gnome/SettingsDaemon/Power --method org.freedesktop.DBus.Properties.Set org.gnome.SettingsDaemon.Power.Screen Brightness ""

Steps in brightness for keyboard control can be implemented with this method as well.

 $ gdbus call --session --dest org.gnome.SettingsDaemon.Power --object-path /org/gnome/SettingsDaemon/Power --method org.gnome.SettingsDaemon.Power.Screen.StepUp
 $ gdbus call --session --dest org.gnome.SettingsDaemon.Power --object-path /org/gnome/SettingsDaemon/Power --method org.gnome.SettingsDaemon.Power.Screen.StepDown

## Using DBus with KDE
See https://userbase.kde.org/KDE_Connect/Tutorials/Useful_commands#Brightness_settings.

## Color correction
Color correction does not change the backlight power, it just modifies the video lookup table: this means that your battery life will be unaffected by the change. Nevertheless, it could be useful when no backlight control is available (desktop PCs or laptops with OLED screens).

*
*
*
*
*
*
*
*

## Wayland
Redshift does not support Wayland (although a patchset exists). But it is possible to apply the desired temperature in tty before starting a compositor. For example:

 $ redshift -m drm -PO 3000

Otherwise some compositors can apply color correction during runtime:

* On GNOME, the built-in Night Light can be used.
* On KDE Plasma, the built-in KDE#Night Light can be used.
* On Sway and other wlroots-based compositors, as well as Orbital, Redshift fork , , , or  can be used.

## Xorg: adjust perceived brightness with xrandr
xrandr may be used to adjust the perceived brightness.

To adjust perceived brightness above its maximum level (the same caveats mentioned above for Nvidia apply):

 $ xrandr --output output_name --brightness 2

This should roughly double luma in the image. It will sacrifice color quality for brightness, nevertheless it is particularly suited for situations where the ambient light is very bright (e.g. sunlight).

This can also be used to reduce perceived brightness in a dark room by specifying some value less than 1 (e.g. 0.5), this is useful when no backlight control is available (e.g. desktop PC).

The output name of the connected device may be determined by calling :

 $ xrandr | grep -w connected | cut -f '1' -d ' '

Users may find it convenient to implement this as an alias:

 $ alias b='echo -e "enter brightness:\n"; read val; xrandr --output output name --brightness "${val}"'

To automatically call xrandr when a backlight file changes,  can be used like so:

 $ oled_shmoled output_name

## NVIDIA settings
Users of NVIDIA's proprietary drivers can change display brightness via the nvidia-settings utility under "X Server Color Correction." However, note that this has absolutely nothing to do with backlight (intensity), it merely adjusts the color output. (Reducing brightness this way is a power-inefficient last resort when all other options fail; increasing brightness spoils your color output completely, in a way similar to overexposed photos.)

## Troubleshooting
## Backlight PWM modulation frequency (Intel i915 only)
Laptops with LED backlight are known to have screen flicker sometimes. This is because the most efficient way of controlling LED backlight brightness is by turning the LED's on and off very quickly varying the amount of time they are on.

However, the frequency of the switching, so-called PWM (pulse-width modulation) frequency, may not be high enough for the eye to perceive it as a single brightness and instead see flickering. This causes some people to have symptoms such as headaches and eyestrain.

If you have an Intel i915 GPU, then it may be possible to adjust PWM frequency to eliminate flicker.

Period of PWM (inverse to frequency) is stored in 2 higher bytes of  register (if you are using the Intel GM45 chipset use address  instead). To manipulate registers values, install the  package.

To increase the frequency, period must be reduced. For example:

Then to double PWM frequency divide 2 higher bytes (4 higher hex digits) by 2 and write back resulting value, keeping lower bytes unchanged:

 # intel_reg write 0xC8254 0x09141228

You can use an online calculator to calculate the desired value

To set new frequency automatically, consider writing an udev rule or install .

## Inverted Brightness (Intel i915 only)
Symptoms:

* after installing  systemd-backlight.service turns off the backlight during boot
** possible solution: mask systemd-backlight.service
* switching from X to another VT turns the backlight off
* the brightness keys are inverted (i.e. turning up the brightness makes the screen darker)

This problem may be solved by adding  to the list of kernel parameters.

## Unable to control eDP Panel brightness (Intel i915 only)
Embedded Display Port (eDP) v1.2 introduced a new display panel control protocol for backlight and other controls that works through the AUX channel By default the i915 driver tries to use PWM to control backlight brightness, which might not work.

To set the backlight through writes to DPCD registers using the AUX channel set  as a kernel parameter.

## sysfs modified but no brightness change
On some systems, the brightness hotkeys on your keyboard correctly modify the values of the acpi interface in  but the brightness of the screen is not changed. Brightness applets from desktop environments may also show changes to no effect.

If you have tested the recommended kernel parameters and only  works, then you may be facing an incompatibility between your BIOS and kernel driver.

In this case the only solution is to wait for a fix either from the BIOS or GPU driver manufacturer.

A workaround is to use the inotify kernel api to trigger  each time the value of  changes.

First install . Then create a script around inotify that will be launched upon each boot or through autostart.

{{hc|/usr/local/bin/xbacklightmon|
#!/bin/sh

path=/sys/class/backlight/acpi_video0

luminance() {
    read -r level < "$path"/actual_brightness
    factor=$(printf "$max" | awk '{print 100/$1}')
    printf "$level $factor" | awk '{print int($1*$2)}'
}

read -r max < "$path"/max_brightness

xbacklight -set "$(luminance)"

inotifywait -me modify --format '' "$path"/actual_brightness | while read; do
    xbacklight -set "$(luminance)"
done
}}

## NVIDIA-only laptops with nvidia_wmi_ec_backlight
On laptops where the Intel iGPU is disabled (e.g. via a MUX switch), such as the Razer Blade 18 (2023, RZ09-0484) with i9-13950HX and RTX 4090, the  driver registers a backlight device under  and accepts brightness values, but the panel brightness does not actually change. The kernel log may show:

 nvidia-modeset: ACPI reported no NVIDIA native backlight available; attempting to use ACPI backlight.

Adding  to the kernel parameters resolves the issue, allowing  to properly control the panel backlight.

## sysfs and xbacklight both not working
check dmesg if you have seen like this :

Change  to match the following:

Then regenerate the initramfs.

## Backlight not working in MATE
Make sure the  package is installed.

## Backlight control with function keys not working on Notebooks
Some Notebook Models e.g. Razer Blade 14, Lenovo Yoga Slim 7, Lenovo IdeaPad Gaming 3 and Acer AN517-41 have issues with backlight control, pass  and/or  as kernel parameters.

## Backlight keys not working in Xfce
In xfce4, the [https://docs.xfce.org/xfce/xfce4-power-manager/start Xfce4 Power Manager handles the brightness keys.

In some installations of Xfce, the "Handle display brightness keys" setting may be turned off by default.

To activate the brightness keys again, open the Xfce Power Manager dialog and toggle on "Handle display brightness keys":

 $ xfce4-power-manager -c

## xbacklight returns : No outputs have backlight property
Depending on the video card installed, sometimes xbacklight from  returns the message "No outputs have backlight property". Installing  provides an alternative xbacklight that may work as expected.

## Allow <5% brightness to persist on reboot (disable backlight clamp)
According to , if the udev property  is not set to false, the brightness is clamped to a value of at least 1 or 5% of maximum brightness, whichever is greater. This restriction will be removed when the kernel allows user space to reliably set a brightness value which does not turn off the display.

To allow <5% brightness to persist on reboot, create udev rule:

{{hc|/etc/udev/rules.d/99-backlight_clamp.rules|2=
# Allow <5% brightness to persist on reboot (disable clamped value of 5%)
SUBSYSTEM=="backlight", ENV{ID_BACKLIGHT_CLAMP}="0"
}}
