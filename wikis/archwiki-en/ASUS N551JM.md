# ASUS N551JM

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) || ||
|-
| GPU (Nvidia) || ||
|-
| Ethernet || ||
|-
| Wireless || ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Camera || ||
|-
| Card Reader || ||
|-
| Bluetooth || ||
|}

ASUS N551JM - this article covers hardware specific configuration. All topics covered can be performed after an installation of Arch Linux has been finished and the machine rebooted into it. Also this article could be applicable for the ASUS N551JK model.

For a general overview of laptop-related articles and recommendations, see Laptop, for a predecessor with a similar configuration, see ASUS N550JV.

## Graphics
For the hybrid graphics configuration, see Bumblebee.

## Display brightness
 and  will not produce any output (will not work) until you use the kernel parameter  to your boot loader (the blank space is needed).

Although for the Asus N751JK the kernel parameter  works for the brightness controls, it also brings some ACPI errors in the kernel log. Using the following kernel parameters prevents these errors, while the brightness controls still work: . The backslashes are needed for grub to escape the double quotes.

It might happen that display brightness adjustment will not work even when the kernel parameter is used. In this case, make sure you are still using kernel parameter  and load the  module with the following command:

 # modprobe asus_nb_wmi

## Audio
To enable the internal microphone and the external subwoofer support, install . This package installs the pincfg patch, and also enables the internal microphone by adding the asus-mode8 to the HDA driver options.

After installation, reboot the laptop to ensure all modules are loaded. Check if the fallback device is correctly set to Build-in Audio Analog Stereo with . See PulseAudio/Troubleshooting#Fallback device is not respected for more information. Also check for muted devices:

 $ alsamixer -c PCH

## Keyboard brightness
In some cases,  and  might not work out of the box with some desktop environments, so install . Load the module to control hotkeys:

 # modprobe asus-nb-wmi

and Enable/start the .

Now you can take control over the keyboard backlight:

## Touchpad
Touchpad works out of the box with the default synaptics drivers. You can tweak its options using the default Xorg configuration files. For example:

Rich multitouch gestures can be configured with Touchegg. To use two-finger or three-finger gestures, you should disable the corresponding features in the Xorg config:

## Troubleshooting
## nouveau problems
Sometimes the nouveau driver produces a lot of garbage log lines during boot and even causes a kernel panic. This is a bug in the driver. You can workaround this by installing the NVIDIA driver.

## Tips and tricks
## bbswitch
If you are using Bumblebee, you can install  package to manipulate the dedicated graphics card state. You can also change the default state of the dedicated graphics card.

## Touchpad switch
The touchpad can be toggled using a  script.

## Function keys
You can see the list of the function keys here: ASUS N550JV#Special keys for window managers.
