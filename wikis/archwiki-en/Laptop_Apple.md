# Laptop/Apple

From Wikipedia:
: The Mac (known as Macintosh until 1999) is a family of personal computers designed and marketed by Apple Inc. The product lineup includes the MacBook Air and MacBook Pro laptops, as well as the iMac, Mac Mini, Mac Studio and Mac Pro desktops. Macs are sold with the macOS operating system.

## Model list
| MacBookPro3,1 Mid 2007 || 2007-08 ||  ||  ||  ||  ||  ||  || ||
|-
| #MacBook2,1 Mid 2007 || 2009-08 ||  ||  ||  ||  ||  ||  || ||
|-
| MacBookPro5,2 2009 || 2009-08 ||  ||  ||  ||  ||  ||  || || Might need
|-
| MacBookPro5 Mid 2009 || 2016-08-01 ||  ||  ||  ||  ||  ||  || || Switching to TTY does not work with NVIDIA, works with Nouveau.
|-
| #MacBookPro6,2 Mid 2010 || 2025-02-16 ||  ||  ||  ||  ||  ||  || ||
|-
| #MacBookPro7,1 Mid 2010 || 2021-11-04 ||  ||  ||  ||  ||  ||  || ||
|-
| MacBookPro8,1 Early 2011 || 2025-02-16 ||  ||  ||  ||  ||  ||  || || broadcom-wl required for full speed Wi-Fi.
|-
| MacBookAir4,2 Mid 2011 || 2023-04-28 ||  ||  ||  ||  ||  ||  || || broadcom-wl required for full speed Wi-Fi.
|-
| MacBookAir5,2 Mid 2012 || 2024-11-16 ||  ||  ||  ||  ||  ||  || || broadcom-wl required for full speed Wi-Fi.
|-
| MacBookPro9,x || 2018-03-01 ||  ||  ||  ||  ||  ||  || ||
|-
| MacBookAir6 2013 || 2014-10-01 ||  ||  ||  ||  ||  ||  || ||
|-
| MacBookAir 7,2 Early 2015 || 2021-11-01 ||  ||  ||  ||  ||  ||  || || Guide: https://github.com/AdhamNasr/Apple_mba-Arch-i3
|-
| MacBookPro11,2 2014 || 2025-05-06 ||  ||  ||  ||  ||  ||  || || Wi-Fi works with broadcom-wl. Bluetooth audio was choppy with PipeWire but works fine with PulseAudio.
|-
| MacBookPro 12,1 2015 || 2025-04-03 ||  ||  ||  ||  ||  ||  || || See Broadcom wireless#BCM43602 802.11ac Wireless LAN SoC.
|-
| MacBookPro13,3 2016 || 2026-03-18 ||  ||  ||  ||  ||  ||  || || See Broadcom wireless#BCM43602 802.11ac Wireless LAN SoC. Touch bar does not work
|-
| MacBookPro 14,1 Mid 2017 || 2026-04-08 ||  || * ||  ||  ||  ||  || || Will not wake from suspend. Sometimes the brcmfmac Wi-Fi driver fails. * Built-in audio will not work without  or comparable cirrus audio driver.
|-
| MacBookPro16,1 2019 || 2023-01-21 ||  ||  ||  ||  ||  ||  || || Must use t2linux provided kernel
|}

## Troubleshooting
## MacBook2,1 Mid 2007
## Boot loader
See UEFI#UEFI firmware bitness: this machine runs a 32-bit EFI. This means you should make sure the boot loader you choose supports mixed mode booting (i.e. a 64-bit OS on a 32-bit UEFI). For GRUB, use  as the target.

## Rebooting
The MacBook will not reboot properly by default. It needs the  kernel parameter.

## Microphone
If your microphone is not working, you have probably run into a driver bug which makes PulseAudio think the digital microphone is always plugged in, disabling the normal microphone.

To work around it, disable the PulseAudio plug detector with this patch:

## MacBookAir1,1 Early 2008
Since this model has only one USB port, you may find it easiest to install Arch with a powered USB hub. Plug a USB network adapter (wireless or ethernet adapter to plug into a USB port) and your Arch installation media into the USB hub.

See Mac/Troubleshooting#Wi-Fi. If you cannot get any result by scanning wireless network after boot, unload modules  and  and load them again:

 # rmmod ssb
 # rmmod b43
 # modprobe b43

There is a good chance you will find what's wrong with DMA from the dmesg log.

Even if you can scan wireless networks after reloading the modules, it is still possible that you will only be able to connect to some networks, but not all of them. According to a more detailed discussion here: https://crunchbang.org/forums/viewtopic.php?id=17368, adding  options to the b43 module can solve this problem.

## MacBookAir2,1 Mid 2009
See Mac/Troubleshooting#Wi-Fi. Append  to .

## MacBookPro6,2 Mid 2010
Heat issues solved with .

On this model only the nouveau driver can be installed when booting in UEFI mode,  causes a black blank screen when Xorg loads.

## MacBookPro7,1 Mid 2010
Booting the installation media, you might encounter the following error:

 unable to handle kernel NULL pointer dereference at 0000000000000010" during pacpi_set_dmamode.

To fix this problem, boot with the option: . After chrooting, add  to  and regenerate the initramfs, see Installation guide#Configure the system.

## MacBookAir5,1 Mid 2012
If you have issues with waking from sleep while in X11 such as a black screen or showing the console with a frozen mouse cursor then remove  and install . This fixed errors such as
  (EE) bcm5974: unable to find touch point 0
and backtraces that causes X11 to crash. This might apply to Version 5,2 assuming they use the same trackpad.

## MacBookAir6,1 Early 2014
Unless you have a local repository on a USB disk, you need a USB to Ethernet adapter or a USB wireless adapter supported natively by the kernel to easily install Arch Linux, since you have to install the  package to make the internal wireless card work.

rEFInd uses 30 seconds to start booting, following Mac/Troubleshooting#Avoid long EFI wait before booting stops rEFInd from loading and it has to be re-installed.

## MacBookPro12,1/11,4+ 2015
## Wireless
The  driver is working, with newer firmware necessary for working 5GHz support ([https://bugzilla.kernel.org/show_bug.cgi?id=100201#c65 see here.)

## Keyboard and trackpad
Haptic feedback works out of the box due to the trackpad's built-in firmware.

There are several drivers available that provide multitouch support. The following have been confirmed working with the MacBookPro12,1.

For  the following configuration emulates some features from the macOS functionality. For more options see .

For  the following configuration is necessary to make the touchpad work fully.

## Graphics
Need apple_set_os to enable the integrated graphics. See PRIME for details on handling hybrid graphics.

If you are experiencing flickering issues with Xorg, you can set  as a kernel parameter, which will disable the power savings for the Intel graphics.

## MacBook9,1 Early 2016
* Booting from USB via EFI works fine, when giving the  kernel option. Remember to hold  on booting to enter the boot menu. In order to allow Linux boot directly from your system disk, you will first need to install rEFInd from the OSX recovery mode (hold  during boot, then open terminal, run the refind-install script).
* The wireless card works out of the box with .
* Suspend / hibernate does not work. The problem seems to be the NVMe that does not wake up. A potential solution to this has been offered, at https://bbs.archlinux.org/viewtopic.php?pid=2176149#p2176149. When booting from an external drive, suspend / hibernate works out of the box.
* Audio recording works out of the box. Audio playback works out of the box for headphones, not for built-in speakers. Cirrus driver patch needed for making the speakers work: https://github.com/leifliddy/macbook12-audio-driver
* The keyboard and the touchpad do not work out of the box. There is a work-in-progress driver available that works well: . Sometimes the touchpad does not work after booting but this can be fixed by reloading the driver with .
* The keyboard backlight does not work (no solution yet).
* For Bluetooth driver, see

## All Intel MacBooks since 2018
Internal keyboard, trackpad, Touch Bar (if your model has one), Wi-fi, and Bluetooth will not work unless you have necessary kernel modules and firmwares. You should follow the guide on https://wiki.t2linux.org/distributions/arch/installation/ for hardware support.

## iMac 2020
It seems the amdgpu driver has problems to set the native 5k resolution. If the display gets corrupted during boot when the amdgpu driver module is loaded, try forcing a lower resolution. Add e.g.  to your kernel parameters.
