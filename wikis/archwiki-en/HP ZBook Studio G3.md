# HP ZBook Studio G3

The HP Zbook Studio G3 is a workstation replacement laptop.

## Installation
Installation is generally pretty straight forward, however, there are some things to consider.
Follow the general instructions of the Installation guide

## Using hybrid graphics
Due to a kernel issue, use of nouveau or bbswitch may result in lockups. To prevent this, add  to your kernel command line (source, Kernel bug 156341).

## Disabling Hybrid graphics
If you do not mind greatly reducing your battery life and would like to use the NVIDIA graphics by default, you can change Hybrid graphisc in the firmware setup.

In the BIOS settings, (which you enter by pressing Escape during boot) change the graphics mode from Auto/Hybrid to discrete.

## Font size during installation
Due to the high screen resolution if this machine, you may want to change the font of your terminal during installation:
 # setfont sun12x22

## Dual boot with Windows
This laptop usually comes preloaded with Windows 7. Although the laptop boots in UEFI mode, it appears as though the Windows boot loader is present in the MBR of the hard drive (there is no EFI system partition).

It may be wise to install Arch with an MBR boot loader if you wish to preserve the Windows installation.

## Configuration
## X config
Install the NVIDIA driver.
If you are using the system in discrete graphics mode, you may need to run nvidia-xconfig as root to be able to run X.

## HiDPI configuration
If you are using a desktop environments such as gnome or KDE, they should have their own management tools.
If you are using more power-user type window managers such as i3, you may need to add the following line in your  file

The name of the output device depends on the graphics adapter and driver. Use xrandr to find out the actual name.

## Touchpad configuration
The touchpad may be "hijacked" by the  device driver. Although the touchpad is working, its configuration is fixed to two buttons, two-finger natural scrolling and no tapping; Any changes with  or other tools will have no effect.

To prevent this you have to blacklist  by adding the following lines to a  file in  (source):

After a reboot (unloading , if possible, may be sufficient) the touchpad should be fully configurable libinput device.

## Mute button LED indicator
To fix the mute button LED, create a file:
