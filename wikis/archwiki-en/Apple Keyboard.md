# Apple Keyboard

Some keyboard models that use the Apple keyboard driver may have swapped keys or missing functionality. This article describes how to change the settings for the keyboard so that it behaves as expected.

## Numlock is on
You may find that the numlock is on. The symptoms are that only the physical keys ,,,,,,,, and surrounding keys work and output numbers. To fix this hit  twice or thrice. You might need to use a utility like .

Alternatively, set the keycodes manually using xmodmap to avoid use Numlock:

 keycode  90 = KP_0 KP_0 KP_0 KP_0 KP_0 KP_0
 keycode  87 = KP_1 KP_1 KP_1 KP_1 KP_1 KP_1
 keycode  88 = KP_2 KP_2 KP_2 KP_2 KP_2 KP_2
 keycode  89 = KP_3 KP_3 KP_3 KP_3 KP_3 KP_3
 keycode  83 = KP_4 KP_4 KP_4 KP_4 KP_4 KP_4
 keycode  84 = KP_5 KP_5 KP_5 KP_5 KP_5 KP_5
 keycode  85 = KP_6 KP_6 KP_6 KP_6 KP_6 KP_6
 keycode  79 = KP_7 KP_7 KP_7 KP_7 KP_7 KP_7
 keycode  80 = KP_8 KP_8 KP_8 KP_8 KP_8 KP_8
 keycode  81 = KP_9 KP_9 KP_9 KP_9 KP_9 KP_9

## Repeating keys on a wireless keyboard
Unpair the keyboard and then re-pair it. The trick is to hold down the power button throughout the entire pairing process.

## hid_apple module options
* - Mode of top-row keys
**0 - disabled
**1 - normally media keys, switchable to function keys by holding Fn key (=auto on Apple keyboards)
**2 - normally function keys, switchable to media keys by holding Fn key (=auto on non-Apple keyboards)
**3 - auto (Default)
* – Controls ISO vs ANSI layout handling (swap of the backtick/tilde and greater-than/less-than keys).
** 0 – disabled (assume ANSI layout)
** 1 – enabled (assume ISO layout)
** -1 – auto-detect (default)
* - Swap the  () and  () keys
**0 - as silkscreened, Mac layout (Default)
**1 - swapped, PC layout
* - Swap the  and  keys
**0 - as silkscreened, Mac layout (Default)
**1 - swapped, PC layout

## Function keys do not work
If your  keys do not work, this is probably because the kernel driver for the keyboard has defaulted to using the media keys and requiring you to use the  key to get to the  keys. To change the behavior temporarily, append  to .

 # echo 2 >> /sys/module/hid_apple/parameters/fnmode

To make the change permanent, set the   option to 2:

To apply the change to your initial ramdisk, in your mkinitcpio configuration (usually ), make sure you either have  included in the  variable or  in the  variable. You would then need to regenerate the initramfs.

## Switching Cmd and Alt/AltGr
This will switch the left  and  key as well as the right / and  key.

Temporary and immediate solution:

 # echo "1" > /sys/module/hid_apple/parameters/swap_opt_cmd

Permanent change, taking place at next reboot:

You then need to regenerate the initramfs.

## Swap the function and left control keys
This will switch the  and left  keys.

Temporary and immediate solution:

 # echo "1" > /sys/module/hid_apple/parameters/swap_fn_leftctrl

Permanent change, taking place at next reboot:

You then need to regenerate the initramfs.

## PrintScreen and SysRq
Apple Keyboards have an  key instead of a / key. This means that Alt+SysRq sequences do not work, and application actions associated with  (such as taking screenshots in many games that work under Wine) do not work. To fix this, you can add  to your . This will map / to , as well as  to  and  to .

Alternatively, follow the Map scancodes to keycodes article to map the  scancode to the / keycode, where 458856 (0x070068) is the scancode of , and  is the keycode of /.

## Treating Apple keyboards like regular keyboards
Depending on the customisations you want to accomplish, there are two solutions available and some options that are in the kernel. You need to choose one of the other.

## Use a patch to hid-apple
While the original  module does not have options to further customize the keyboard, like swapping  and left  keys or having  on the left side of , there is a patched version adding this functionality to the module. To use it, install the  package. This will install the patched  and mask out the original one.

The package uses DKMS to automatically recompile the module during kernel upgrades. While the  will be pulled in by dependency. You still need to install an appropriate kernel header package manually. See the DKMS page for more info.

In addition to the patched kernel module, a configuration file is also provided by the package at , which enables PC-like layout by default:

* Top-row keys are normally function keys, switchable to media keys by holding Fn key, as in #Function keys do not work.
* Four keys at the lower left corner act as , , , , in this order.
* Two keys at the lower right corner act as , , in this order.
* If you have an  key, it will act as  key.

If you wish to change the default options, copy the configuration file to  and make desired changes:

 # cp {/usr/lib,/etc}/modprobe.d/hid_apple.conf

The file under  will completely override the one with the same name under , and the content is NOT merged.

Alternatively, put additional options in a file with a different name if you want to keep default ones.

Please refer to the project README for the exact meaning of each configuration option and tweaking the configuration file to suit your needs. Learn more about  at Kernel module#Using modprobe.d.

After installation, reboot for the change to take effect, or #Change the behavior without reboot.

## Troubleshooting configuration not picked up by the module
First, make sure the patched version is loaded, see what parameters are provided by the module:

 $ ls /sys/module/hid_apple/parameters/

If you do not see new options like , , etc., check your DKMS installation.

Then, check if configuration files are correctly included in the initramfs:

 $ mkdir /tmp/initramfs
 $ cd /tmp/initramfs
 # lsinitcpio -x /boot/initramfs-linux.img

Check the presence and content of  and any other relevant configuration files in . If they are not there, you should check your  to include those. By default, there should be a  hook that automatically include those files, if not, add it to the HOOKS array after .

Alternatively, specify those files in FILES array explicitly:

 FILES=(/usr/lib/modprobe.d/hid_apple.conf)

Finally, regenerate the initramfs and reboot.

## Use un-apple-keyboard
If you do not need all of these customizations and you do not want to compile a new module manually or using dkms, there is an AUR package  which does not rely on a new kernel module, but rather just to mappings. It enables the following features:

* The keyboard is considered as an ISO keyboard (e.g.  located at the right of the  key are working like expected).
* The function keys are disabled by default. You need to press the  key in combination to trigger them. By default, the behavior are thus keys  to
* The  and  keys are swapped.
*  is mapped to ,  to  and  to .

The first 3 aforementioned features are brought to you using the default linux kernel module .

The last one is provided by providing a mapping to .

## Change the behavior without reboot
To reload the kernel module without reboot, run

## Magic Keyboard does not connect
If you have a magic keyboard that will not connect to the system through the built in tools, such as the Gnome 3 bluetooth menu in settings, install  and its dependencies and attempt to connect with it.  If it still fails to connect, make sure you have bluetoothctl and hcitool installed.

## Enable dvorak/dvp
By default xkb loads translation table (actually called )  for macintosh keyboard:

 $ setxkbmap -print -verbose 10 | grep symbols

This translation table located in  and do not contains dvorak/dvp layout. You can use default translation table from  and add command  in your  for forced loading layout:

 # mv /usr/share/X11/xkb/symbols/macintosh_vndr/us /usr/share/X11/xkb/symbols/macintosh_vndr/us.back
 # cp /usr/share/X11/xkb/symbols/us /usr/share/X11/xkb/symbols/macintosh_vndr/us
 $ echo "setxkbmap -v 10 -layout us -variant dvp" >> .xprofile

## No input during root disk decryption
You may have to manually add the  module to the mkinitcpio configuration:

 MODULES=(hid_apple)

Or place the keyboard hook before autodetect so that all keyboard drivers are included:

 HOOKS=(... keyboard autodetect ...)

Regenerate the initramfs after doing either of these.
