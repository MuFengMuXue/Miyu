# Mac/Troubleshooting

This page contains troubleshooting solutions for Apple Macs. Most models have their own section in Laptop/Apple for even more specific issues.

## Video
Different Mac models have different graphic cards.
To see which graphics card you have type:

 $ lspci -nnd ::03xx

* If it returns a string containing , read Intel graphics.
* If it returns , read NVIDIA.
* If it returns two lines, with both  and , your Mac has dual graphics. See MacBookPro10,x#Graphics for an example of one such setup that might apply in other cases.

* Otherwise if it returns  or , read ATI or AMDGPU.

## NVIDIA
If you boot in EFI mode and NVIDIA binary drivers are working only in BIOS mode (e.g. you get black screen on EFI boot), try the approach described on Ask Ubuntu.

For the backlight to work properly you may need the  package. If backlight control does not work afterwards, you should blacklist the  kernel module. If backlight control does not work even this way, try setting  in .

Alternatively, you can choose to use the  package. If you do so, you may wish to change the step settings in  to something around 5000-10000 depending on how many levels of brightness you desire (the max brightness is around 80000).

If the brightness does not function correctly through pommed, make sure you have installed the  package and insert

 $ find . -name "*" -exec sed -i 's/mbp_backlight/nvidia_backlight/' '{}' \;

into the second line of the pommed PKGBUILD build() function and rebuild the package. See the following forum post for details.

Another possible solution is:

 $ find . -name "*" -exec sed -i 's/nvidia_backlight/apple_backlight/' '{}' \;

Alternatively, run nvidia-settings, edit  and add this line into the  section:

 Option "RegistryDwords" "EnableBrightnessControl=1"

Save, reboot and check if the backlight control works. See Ubuntu's Wiki page for the MacBookPro5,5 for details.

## Touchpad
The touchpad should have basic functionality by default. A true multitouch driver which behaves very similarly to native macOS is included in the  package.  Configuration options are documented in the readme.

The following mtrack options work well on a MacBook7,1:

 Option "Thumbsize" "50"
 Option "ScrollDistance" "100"

Probably, you also need to add:

 MatchDevicePath "/dev/input/event10"

To disable tap-to-click (that is, to press down to click) by default, add the following to your mtrack configuration section

 Option "TapButton1" "0"
 Option "TapButton2" "0"
 Option "TapButton3" "0"

## Natural scrolling
To configure natural two finger scrolling similar to macOS, refer to Touchpad Synaptics#Natural scrolling.

If you are using , you can simply swap the scroll up and scroll down buttons (along with the scroll left and scroll right):

## Older MacBook models
On older MacBook models (pre-multitouch, e.g. MacBook2,1), the touchpad will not function properly until you install . See Touchpad Synaptics for details.

## Keyboard
Mac keyboards work by default. For swapping  keys with  keys see Apple Keyboard.

Map them with xbindkeys or through desktop environment preferences. Alternatively, install the  package.

Edit the  according to your hardware, building it from  or  example files.

Note that you can also run it without a configuration file, the defaults may work for you. Then enable/start .

## Keyboard backlight
The keyboard backlight is controlled by .  Write the desired value to  in that directory. See Keyboard backlight for detailed information. Common choices for backlight control are  and .

Ensuring the keyboard backlight is on when entering the LUKS decryption password

This can be done via initcpio hooks. First, create an executable install script:

{{hc|/etc/initcpio/install/mac_kb_backlight|
#!/usr/bin/env bash

build() {
  add_module applesmc
  add_runscript
}
}}

Next, create an executable hook:

{{hc|/etc/initcpio/hooks/mac_kb_backlight|
#!/usr/bin/env bash

run_hook() {
  if [ -f "/sys/class/leds/smc::kbd_backlight/brightness" ]; then
    echo 100 > "/sys/class/leds/smc::kbd_backlight/brightness"
  fi
}
}}

Finally, add this custom hook to the  array in , and ensure it is placed before the  hook:

 HOOKS=(... mac_kb_backlight encrypt ...)

Remember to regenerate the initramfs images after these steps to include the custom script.

## Wi-Fi
Different Mac models have different wireless cards.

Check what card you have:

 # lspci -nnd ::0280

* If you have an Atheros card, all should work out-of-the-box.
* If you have a Broadcom card, follow Broadcom wireless#Installation.
* 5.0 and 6.0 generation Macs may have a BCM43xx, follow Broadcom wireless#broadcom-wl.
** If you have the correct Broadcom DKMS driver (i.e. ) installed and your Wi-Fi card is still not being recognized, try rebuilding the driver (See Dynamic Kernel Module Support).

## Fan Control
 is a fan control daemon that supports most Intel Macs, its configuration file is located at .

 is available for MacBook Pro users.

## Power management
TLP is a very simple set of scripts that will maximize your battery duration. A MacBook Air 2013 with TLP provides about 11 hours of light usage with just TLP installed.
All the usual power management recommendations apply as well.

## Disabling Thunderbolt
Linux still has poor power management for Thunderbolt adapters on Macs. This can cause the TB adapter(s) to be always-on and prevent the CPU from going into the deepest power-saving states drawing ca. 2W additional power even when not in use [https://github.com/Dunedan/mbp-2016-linux/issues/24#issuecomment-310952415. An easy way to see the CPU states is using powertop. The problem arises when the CPU does not go below C3 as a package (Pkg%pc3).

One workaround is to add  to the kernel parameters, thereby telling the firmware that the system is not compatible with macOS This should disable the TB adapter (at least on older Macs), and thus reduce power consumption greatly, but will probably come with side-effects (e.g. no Thunderbolt, maybe others?).

It is also possible to blacklist the thunderbolt module and then putting the controllers to sleep with

 # echo auto > /sys/bus/pci/devices/0000:07:00.0/power/control

Check the correct device number with lspci. This can also be automated. This method reduces power consumption slightly, but still consumes 0.9 W more than the previous method on a MacBook Air 2013.

## Suspend and hibernate
Issues were reported where the machine would "suspend immediately after resume" in certain conditions when suspending by closing the lid. This was solved by setting the option "sleep-inactive-ac-type" to "nothing" using dconf-editor, option path: org &rarr; gnome &rarr; settings-daemon &rarr; plugins &rarr; power).

See Suspend and hibernate for details on how to configure hibernation. Noticeably, you will need a swap partition or file (see the mentioned article for further instructions).

Slow wake ups from a suspend state can be resolved by disabling Thunderbolt. See #Disabling Thunderbolt.

## Wake up after suspend
Occasionally a Mac laptop may wake up immediately after suspending. This may not be immediately evident as the screen may stay off despite the system being awake, and can be checked by seeing whether the keyboard backlight stays on.

In , check to see that XHC1 and LID0 are enabled. If they are, one can temporarily disable just LID0 with the following to see if the issue resolves

 # echo LID0 > /proc/acpi/wakeup

To make the change persistent, create:

And then enable/start . To wake the system from this point, use the keyboard.

If this does not resolve the issue, XHC1 may be the issue and one can disable both it and LID0 temporarily with the following to see if it goes away.

 # echo XHC1 > /proc/acpi/wakeup && echo LID0 > /proc/acpi/wakeup

Disabling only XHC1 is not recommended if you have this bug, since it may result in glitchy behavior. Disable both on every boot as follows:

To wake the system from this point, only the power button can be used.

## Light sensor
The values can be read from : it returns two-tuples like (4,0).

If you want to use the built in light sensor to automatically adjust screen and keyboard backlight brightness:

*
*

## Sound
First of all follow ALSA wiki page, then if something does not work correctly, continue reading this part.

## Kernel options
Edit your  or  appending this line:

 options snd_hda_intel model=intel-mac-auto

This should automatically specify the codec in your Mac.

Specific models may need more help. You can try specifying other options according to your hardware. All possible settings are listed in Kernel Documentation, available online:

* [https://docs.kernel.org/sound/alsa-configuration.html Advanced Linux Sound Architecture - Driver Configuration guide
* HD-Audio
* HD-Audio Codec-Specific Models

## Model-specifics
For example, if you have a MacBookPro12,1, you might need

 options snd-hda-intel index=1,0

instead. Alternatively, for MacBookPro5,X, you can use:

 options snd_hda_intel model=mb5

(note that the jack output is controlled with "HP").

If you have an iMac8,1, you should instead use

 options snd-hda-intel model=mbp3 position_fix=2

For Aluminium iMacs, see iMac Aluminium#Getting sound to work right

For MacBook2,1 (late 2008/early 2009)s with a SigmaTel STAC9221 A1 chip, use

 options snd_hda_intel model=macbook

## Disabling S/PDIF
Some (most?) Mac models have an optical S/PDIF audio jack in the same jack as the headphone jack. You can see it when it is active as a red light glowing out of the headphone jack. It can trick PulseAudio into preferring it and routing all your audio out it.

If you are not getting any sound in or out, confirm that  > Configuration > Profile says "Analog Stereo Duplex" instead of "Digital"

or just run

 $ pacmd set-card-profile 0 output:analog-stereo+input:analog-stereo

Also check if you need to edit  to workaround faulty plug detection causing PulseAudio to failover to "Digital".

See Laptop/Apple#Microphone for how to edit this to get the MacBook2,1's microphone to work.

## Auto-Mute Mode
The internal speaker might not be disabled when using the headphone jack. To solve this, enable "Auto-Mute Mode".

You can either do this using :

# Run
# Press  and pick  to get more detailed controls
# Use the arrow keys to select "Auto-Mute Mode"
# Press  to enable it

or with :

 $ amixer -c 0 cset name='Auto-Mute Mode' 1

Optionally, run  as root to make the change permanent.

## USB audio interface
In some cases, it can actually be easier to set up sound using a USB audio interface rather than the jack directly.

With , go to , choose  for all devices and choose  for your USB device. You can then use the headphone jack on the USB device for speakers or headphones. This should work immediately and on startup.

## Bluetooth
Bluetooth should work out-of-the box. See the article on Bluetooth to install and configure all software needed.

## Magic Mouse
If you use a magic mouse you will find it works nicely out of the box. You might want to tweak some settings such as scroll-speed or acceleration. There is no GUI for this at this time. The only way to set these settings is to instruct the kernel driver () with parameters. Create a modprobe config file for your mouse.

This will instruct the driver to have a fast scroll-speed, do exponential acceleration and do not emulate a 3 button mouse. You can find an overview of all parameters and their current settings in .

To try different settings without rebooting you can also set them through the command line:

 # echo 55 > /sys/module/hid_magicmouse/parameters/scroll_speed

## Webcam
## iSight
iSight webcams on MacBooks or pre 6,2 MacBook Pros (6,2 came out around 2010) require the Apple's proprietary firmware that cannot be redistributed. It must be extracted from macOS and loaded onto Arch.

There is a pre-extracted copy available in the form of the  package.

If you want to do it yourself you will need to install  to extract the firmware. This package also includes a udev rule and ELF binary that are necessary, even once you have extracted the firmware file into , for the file to be loaded every time you boot your computer (namely  which uses ).

Instructions:

First you need to get the firmware out of a particular file located on your macOS install. It is located in .

To mount the macOS drive if multi-booting:

 # mkdir /media/macOS
 # mount -t hfsplus /dev/sda2 /media/macOS

You can also download a copy of the file from https://archive.org/details/AppleUSBVideoSupport.

Then, install the  package.

Locate the  file in the macOS directory listed above. Either copy it over to your Arch system (Any macOS installation should do, such as an iMac, not just one specific to your system) or, if multi-booting, mount the macOS drive and navigate to the directory. (On 10.6 (Snow Leopard) and 10.7 (Lion) the directory is .) In that directory you can go ahead and extract the driver:

 # ift-extract --apple-driver AppleUSBVideoSupport

When it is done, check that the firmware has been found:

 # ls /usr/lib/firmware/isight.fw

Once successful, completely shutdown your Mac and start it back up again (to clear the hardware state of the webcam). Do not reboot.

It should be automatically loaded at boot; if it is not you can load the  module manually or load it at boot.

## FaceTime HD Camera
Recent Macs include the FaceTime HD Camera, which may be connected by PCIe. You can confirm this by looking for "FaceTime HD Camera" in the output of . The  and  packages installs a  module (and firmware) to support these devices. The module should be loaded automatically after installation.

If the webcam shows incorrect colors, this may be due to missing sensor calibration files. Instructions for extracting the calibration files from Apple BootCamp drivers are given in this page: https://github.com/patjak/facetimehd/wiki/Extracting-the-sensor-calibration-files

See Multimedia#Webcam for applications with which to test.

## Temperature sensors
For reading temperature just install . See lm_sensors for more information.

## Avoid long EFI wait before booting
If your Mac spends 30 seconds with "white screen" before booting you need to tell the firmware where the booting partition is. This is done via the  utility in MacOS.

Boot macOS and open a terminal. If you do not have MacOS installed, you have several alternatives:

* boot the Mac into the MacOS recovery
* use the MacOS install DVD
* boot from another Mac (connect the two computers via firewire or thunderbolt, start the other Mac while holding the T button, boot your Mac while holding the Options button (alt)).

Either way, once you have got a macOS terminal running on your Mac you need to execute the following command if the booting partition is EFI:

 # bless --device /dev/diskXsY --file=/Volumes/efi/EFI/BOOT/BOOTX64.EFI --setBoot

or if the booting partition is not EFI:

 # bless --device /dev/diskXsY --setBoot --legacy

To know the value to put in  you can print a list of the partitions with the  command, and find your boot partition.

See also https://bbs.archlinux.org/viewtopic.php?pid=833215.

## kworker using high CPU
Sometime with the addition of Yosemite, some users found that kworker CPU usage will spike, as discussed here. This is sometimes the result of runaway ACPI interrupts.

To check and see, you can count the number of recent ACPI interrupts and see if any of them are out of control.

 $ grep . -r /sys/firmware/acpi/interrupts/

If you see that one particular interrupt is out of control (possibly GPE66), i.e., registering hundreds of thousands of lines, you can try disabling it (replace XX with the runaway interrupt):

 # echo "disable" > /sys/firmware/acpi/interrupts/gpeXX

Disabling random ACPI interrupts could cause all kinds of problems, so do this at your own risk. If this fixes the problem, there is discussion about how to make a systemd service that automatically disables an interrupt at every boot here.

## Mavericks upgrade breaks Arch boot option
For some multi-boot users who utilize a separate Linux boot partition, the OS X Mavericks upgrade may overwrite the boot partition with Apple's own recovery boot filesystem. This breaks the Arch Linux boot option in rEFIt/rEFInd. The best way to proceed in this situation is to abandon a separate boot partition and use the EFI system partition (ESP) to install the boot loader of your choice. It is also recommended that you use rEFInd instead of rEFIt as development on the latter has halted.

Assuming grub2 as the boot loader:

Use the Arch LiveCD to boot to a shell and chroot to your broken Arch Linux environment.

Mount the ESP on .

Edit the fstab and remove the old boot partition and make ESP the new boot partition. Now mount the ESP as the new  partition.

 # mount -a

Reinstall the  package.

Create a new initramfs and vmlinuz in /boot.

 # mkinitcpio -p linux

Install grub.

 # grub-install --target=x86_64-efi --efi-directory=/boot --bootloader-id=grub --recheck --debug

Create a new grub.cfg file.

 # grub-mkconfig -o /boot/EFI/grub/grub.cfg

Make sure that grub.cfg is in the same directory as grubx64.efi.

Generate a new refind_linux.conf file in /boot simply by running mkrlconf.sh which comes with rEFInd.

Exit the chroot environment.

Reboot. You should see a new entry for Arch Linux in rEFInd and it should boot to your Arch Linux installation.
