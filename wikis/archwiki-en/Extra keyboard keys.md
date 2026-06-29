# Extra keyboard keys

This article assumes you have read Keyboard input.

Many keyboards include some special keys (also called hotkeys or multimedia keys), which are supposed to execute an application or print special characters (not included in the standard national keymaps). udev contains a large database of mappings specific to individual keyboards, so common keyboards usually work out of the box. If you have very recent or uncommon piece of hardware, you may need to adjust the mapping manually.

## Laptops
## Apple MacBooks
All the required information is available on the Apple Keyboard dedicated article.

## Asus M series
In order to have control over the light sensor and the multimedia keys on your Asus machine, you should use the following command:

 # echo 1 > /sys/devices/platform/asus_laptop/ls_switch

To have it run on boot create a systemd tmpfile:

## Asus N56VJ (or possibly others)
If most of your special keys do not work, try loading the asus-nb-wmi kernel module with
 # modprobe asus-nb-wmi

then check xev again. If you combine this with the  boot option, you may get weird results in xev, so try not using it. If this did fix things, make sure to make the module load at boot with methods described in Kernel modules#Automatic module loading.

## Lenovo T460p (or possibly others)
Out of the box, the backlight keys (on , ) might not be available, even via the  interface. To fix this, follow Backlight#Kernel command-line options.

## Gaming Keyboards
Gaming keyboards have some special features which may cause them to "misbehave" in Linux.

## Cooler Master CM Storm QuickFire TK
This keyboard has two features that could cause confusion in Linux: N-Key Rollover and the Win-Lock Key.

N-Key Rollover can cause problems with the Function keys. To disable N-key rollover, hold down the FN lock key (next to right-ctrl) until it lights up, then hold Escape and press 6 to switch to 6-key rollover. Hold down the FN lock key to disable the Fn lock.

The Win-Lock Key completely disables the Super (Windows) keys. Simply press the FN lock key and F12 together to toggle Win-Lock on and off.

## Corsair K series keyboards
There is a winlock button on these keyboards that can disable the use of the Super (Windows) keys. This button is located at the top right of the keyboard next to the num and capslock buttons. CKB can be used to disable this functionality entirely preventing further locking. However, in a default state, simply pressing the button would enable the Super (Windows) keys again.

## Logitech G series G710 and 710+
This keyboard has a row of 6 programmable G keys. In order to use them as intended by Logitech, you need to install  and start .

## Logitech G613
This keyboard has a row of 6 programmable G keys. In order to use them as intended by Logitech, you need to install . Within solaar, you will be able to divert the G-Key functions and remap them.

## Logitech MX
These keyboards have special keys such as Snipping Tool, Mic Mute that does not produce key codes. Using , you can divert these keys and remap them.

## Non-standard keyboards
## Royal Kludge RK61 and possibly other Apple keyboards
Some Apple keyboards (including the Royal Kludge RK61) have the function – keys defaulted to mac media keys. If no  is available, this is the only available behavior unless the default Apple Keyboard behavior is changed. In order to remedy this, make sure the keyboard is being identified as an Apple keyboard using the following command:

 # lsusb | grep "Apple.*Keyboard"

Proceed to Apple Keyboard#Function keys do not work if an Apple Keyboard is found.
