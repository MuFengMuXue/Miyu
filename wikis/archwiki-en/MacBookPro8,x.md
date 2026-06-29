# MacBookPro8,x

This page contains tips on installing Arch Linux on an Early 2011 MacBook Pro.

discuss at https://bbs.archlinux.org/viewtopic.php?pid=1021706

## Installation
Following the installation guide works for the most part, but it is necessary to add some kernel parameters when booting due to issues with the graphics card as well as potentially switch kernel module to get the wireless network to work:

## 8,1
Forum thread: BBS#136833

Add following to kernel parameters.

  i915.enable_fbc=1 usbcore.autosuspend=1 h

## 8,2 and 8,3
If, after installation, the screen freezes after boot, try booting with the kernel parameter

  radeon.modeset=0

in order to disable the ATI Radeon graphics card.

## Using rEFInd and an EFI boot stub
Using rEFInd as a boot manager as an alternative to GRUB or systemd-boot is possible, but may need some configuration.

## Install rEFInd
Consult Installing rEFInd

Boot into Mac OS X

  # mkdir -p /efi/refind
  # cp -r refind/* /efi/refind/
  # rm /efi/refind/refind_ia32.efi
  # mv /efi/refind/refind.conf-sample /efi/refind/refind.conf and adjust it
  # bless --setBoot --folder /efi/refind --file /efi/refind/refind_x64.efi

## Setting up the EFI boot stub
Follow EFI boot stub.

## Add kernel modules
Without this, you will get  error.

Edit :

  MODULES="..ahci libahci.."

Then regenerate the initramfs.

## BIOS boot
Boot into BIOS emulation mode. AMD card works, but intel card does not.

Use rEFInd to load GRUB legacy.

## Wireless network
See Broadcom wireless for b43 installation and usage.

## Keyboard and touchpad
## Keyboard
Default  key represents , if you want it represents to . Set  parameters to hid_apple module.
See Kernel modules#Setting module options for more information.

## Touchpad
Two finger scrolling and left-click works out of the box. Unfortunately the right-click is not functional.

There are two drivers to provide features to the touchpad (including right and middle click): mtrack which is reported to work well and Synaptics which provides more features but might require some tuning.

mtrack:

Mtrack is available in . The configuration is done via the  file. Check if the mtrack module is properly loaded in the  file. Sometimes xorg loads other drivers before, like eg. synpatics, and the mtrack driver is not used at all.

For an MBP 8,3 I needed to use the following config (in ) to stop it picking up other input devices by mistake:

 Section "InputClass"
   Identifier "Multitouch Touchpad"
   Driver "mtrack"
   MatchDevicePath "/dev/input/event*"
   MatchProduct "bcm5974"
   MatchIsTouchpad "true"
 EndSection

synaptics:

See Touchpad Synaptics#Installation for synaptics installation and configuration instructions.

  #list all possible configurable parameters.
  synclient

  #To change a value for a command use `synclient command=X`
  #Example:
  synclient HorizTwoFingerScroll=1

After you have successfully tried and tested your options through synclient, you can make these changes permanent by adding them to

## Video and screen
13-inch

Intel HD Graphics 3000: works with .

Adjust Brightness: works with .

For example:

 $ xbacklight -inc 7 # increase brightness
 $ xbacklight -dec 7 # decrease brightness

or you can use a simple bash script that provides screen and keyboard backlight management by simple cli (-d for display / -k for keyboard)

 #!/bin/bash
 case $1 in
        -d|--display)
            if [ "$2" != "0" ]
                then
                    echo "$* 4882) / 100) % 4883" > /sys/class/backlight/intel_backlight/brightness
            fi;;
        -k|--keyboard)
            echo "$* 255) / 100) % 256" > /sys/class/leds/smc\:\:kbd_backlight/brightness;;
        -h|--help)
            echo -e "MacBook 8.1 brightness helper\n\t-d\tset display brightness (0-100%)\n\t-k\tset keyboard brightness (0-100%)\n";;
        *)
            echo -e "Unknown option try -h or --help";;
 esac

Save it in  and mark it as executable.

For usage, run:

 $ macbackl --help

15-inch and 17-inch

AMD Radeon HD 6490M: Unknown.

AMD Radeon HD 6750M and 6770M: works with .

## Sound
8,3

Some applications (e.g. VLC) have intermittent crackling; appending 'tsched=0' to 'module-udev-detect' in /etc/pulse/default.pa fixes this.

## Suspend and hibernate
8,1

For s2ram install  and add to file  following content:

  SUSPEND_MODULES="bcma b43"
  SLEEP_MODULE=uswsusp

Without this, system hangs after the machine wakes up and tries to reconnect to the wireless network.

## HFS+
HFS is mounted as Read-Only. By turning journaling off in OS X, the HFS+ file system will be read/write under Linux.

## Bluetooth
I had problems pairing devices, nothing was detected with

 hcitool scan

There seems to be a conflict between the bluetooth module and the b43 one (wifi). The solution is creating  with the following content:
 options b43 btcoex=0

## Troubleshooting
## Broken integrated GPU
The 8.2 macbook pro models with integrated graphics card have a manufacturing issue that causes the lead-free solder of the GPU to crack, inhibiting its ability to function. The problem begins by seeing red lines on the monitor and then failing to boot OS X. Apple issued a repair program, but the odds are that your GPU will die again soon.

It is still possible to boot linux using the outb 0x750 lines in grub2 as described above, however this is a nuisance because it may be impossible to read the monitor when the problem is severe, making installation impossible. In addition, you may also wish to use another boot loader other than GRUB.

It is possible to fix the problem by forcing the EFI to use the integrated graphics card.

If you want to force the EFI to use the integrated graphics card, then check the following topic: force 2011 macbook to use integrated card. You may need to append radeon.modeset=0 to your kernel command line so that linux does not attempt to use it:

 radeon.modeset=0

## Grub2-EFI boot: Intel invalid ROM contents
If you see this error on boot and notice the screen output seemingly frozen, you need to disable KMS.

You have two options, use grub to disable the discrete GPU or disable the discrete GPU in the EFI.

' use grub '

Append the following to your /etc/grub/defaults LINUX line:

 i915.modeset=0 radeon.modeset=0

However, newer versions of the Xorg Intel/i915 driver require KMS to work; without it the X server will fallback to framebuffer mode, with poor performance. The underlying issue is that the Intel KMS driver selects the wrong video output; to fix this try the following settings (tested on an 8,3/17" MBP):

 radeon.modeset=0 i915.modeset=1 i915.lvds_channel_mode=2

This should give you Intel graphics output. Note that this requires kernel 3.5rc1 or higher; use linux-mainline from Aur if necessary. See this bug for more details.

You may find you need to enable the Intel device; if using Grub, the following should enable it at boot time:

 set gfxpayload=keep
 # Switch gmux to IGD
 outb 0x728 1
 outb 0x710 2
 outb 0x740 2

Alternatively, if you have OS X available you can use gfxCardStatus to switch to the Intel device before booting into Linux.

' Force EFI to use integrated '

If you want to force the EFI to use the integrated graphics card, then check the following topic: force 2011 macbook to use integrated card. You may need to append radeon.modeset=0 to your kernel command line so that linux does not attempt to use it:

 radeon.modeset=0
