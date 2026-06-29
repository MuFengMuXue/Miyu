# Alienware 13

This article documents configuration and troubleshooting specific to the Alienware 13 laptop.

See the Installation guide for general installation instructions.

## Installation
Boot the computer and press  to access to the boot menu, from there we select the USB and boot from there.

If you get stuck into a nouveau loop or a black screen, change the kernel parameters with .

## Switching Windows from RAID to AHCI mode
The stock installation of Windows is in RAID mode which makes linux unable to see the NVMe disks. However once installed in RAID mode, Windows refuses to boot when the disk is in AHCI mode. You can however fix that by following those steps:

# Right-click the Windows Start Menu. Choose Command Prompt (Admin)
#* If you don’t see Command Prompt listed, it’s because you have already been updated to a later version of Windows.  If so, use this method instead to get to the Command Prompt:
#*# Click the Start Button and type
#*# Right-click the result and select Run as administrator
# Type this command and press : {{ic|bcdedit /set {current} safeboot minimal}}
#* If this command does not work for you, try
# Restart the computer and enter BIOS Setup (the key to press varies between systems).
# Change the SATA Operation mode to AHCI from either IDE or RAID (again, the language varies).
# Save changes and exit Setup and Windows will automatically boot to Safe Mode.
# Right-click the Windows Start Menu once more. Choose Command Prompt (Admin).
# Type this command and press ENTER: {{ic|bcdedit /deletevalue {current} safeboot}}
#* If you had to try the alternate command above, you will likely need to do so here also:
# Reboot once more and Windows will automatically start with AHCI drivers enabled.

Source: == Touchpad ==

If the touchpad does not work, try to unload the  module:

 # modprobe -r i2c_hid

and restart the graphical environment. If that helps, consider blacklisting the module.

## Wireless
The WiFi network of the Alienware 13 is a Atheros Qualcomm Killer N1525, which is not configured by the default installation. See the [https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1383184 ubuntu bug.

Fortunately, the following patch is able to get it to work. It was tested on Kernel 4.2.5-1 as follows:

 $ git clone https://github.com/sumdog/ath10k-firmware
 # cp -a ath10k-firmware/ath10k/QCA6174 /lib/firmware/ath10k/QCA6174
 # echo "options ath10k_core skip_otp=y" | tee -a /etc/modprobe.d/ath10k.conf

After a reboot, wireless should work, including WiFi AC speeds.

For Alienware 13 R3, the WiFi works out of the box. The following kernel error seems to be harmless.

 ath10k_pci 0000:3d:00.0: could not fetch firmware file 'ath10k/QCA6174/hw3.0/firmware-5.bin': -2

## R1 freezes on suspend/hibernate
Due to firmware crashes with the ath10 WiFi driver on R1 you may encounter system freezes upon suspend/hibernate. A workaround would be to unload the ath10 module before going down and load it back upon wake up. Create and make executable:

{{hc|/usr/lib/systemd/system-sleep/suspend.sh|2=
#!/bin/bash
if [ "${1}" == "pre" ]; then
   rmmod ath10k_pci ath10k_core
   sleep 1
elif [ "${1}" == "post" ]; then
   modprobe ath10k_pci
fi
}}

Do not forget to do a daemon-reload after that.

Note that the nouveau driver also can be the source of problems with suspend, so if the above does not help, try to either blacklist it or install the non-free NVIDIA driver to replace it.

## Graphics
The Kaby Lake R3 suffers from a X lockup when either trying to start X or running lspci when the discrete GPU is off. There are kernel bug and bumblebee bug open to track this issue. In the meantime you can add the following to your kernel commandline at boot:

R3 has support for Windows 2012, 2013, 2015. When using 2009, reboot is not available. 2015 works fine and also enables ACPI reboot.

To have switchable graphics see bumblebee instructions. The utility is able to turn on and off the dedicated graphics card on demand and without having to restart the computer or reopening session.

It is to be noted that some Alienware laptop (Alienware 13 R3) shows an lspci hang issue where lspci/startx/etc… hangs and freeze the system when probing inactive discrete NVIDIA GPU.

## Intel powersaving options
In order to get the most out of your battery life it is recommended to use the following additional powersaving options:

Refer to Dell XPS 13 (9360)#Power saving for additional information on each of them.

## OLED screen brightness
With Gnome, the brightness control keys toggles the on-screen display, but it does not change the brightness level. The screen blanking feature also does not work. The following command can be used to set the brightness to 50%.

 $ xrandr --output eDP1 --brightness .5

Until brightness control is supported by the kernel, we can use the following script to read off the brightness values from sysfs and apply xrandr brightness reduction to it:

{{hc|/usr/local/bin/xbacklightmon|2=
#!/bin/sh

path=/sys/class/backlight/acpi_video0

luminance() {
    read -r level ' "$path"/actual_brightness  while read; do
    xrandr --output eDP-1 --brightness "$(luminance)"
done
}}

Make it executable and add it to autostart and you are set. We use inotifywait to know when the value is modified so we do not busy wait but are still responsive.

## OLED screen does not light up after resume
Sometimes when you sleep the computer and resume it, the OLED screen will flicker but not actually light up again. To fix this use the following xrandr command:

This is a script so that it can easily run it if the monitor is off after resume: you can add it to a keyboard shortcut, or use run command, whichever is easier.

## HDMI/Mini-DP audio
The HDMI and the mini-DP are connected to the NVIDIA card, which means that in order for them to play audio you need to route it through the sound card attached to the NVIDIA device. However by default the GPU has its audio disabled for whatever reason. To enable it follow NVIDIA/Troubleshooting#No audio over HDMI

## Keyboard lights
To get access to the keyboard lights they can be controlling by sending data to the correct device ()

There are plenty of programs like pyAlienFX or Alienware-KBL and none of these work, but the following GitHub project that consists on sending data to USB using  that worked fine.

 $ git clone https://github.com/snooze6/hack-alienfx
 $ make all

In case of a compilation error similar to , try adding:

Once it is compiled, test by running:

 # ./run seq/snooze

and keyboard lights should work.

To register it as a command and can use this program without being root we can do the next:

 # cp run /usr/local/bin/
 # mkdir /usr/local/fx
 # cp seq/* /usr/local/fx
 # chmod 4755 /bin/fx
 # cp lights.sh /usr/local/bin/lights
 # chmod +x /usr/local/bin/lights

Now it should trigger by executing:

 $ lights
 $ lights on
 $ lights off

from a console.

We can simply add the commands to the energy admin or the startup to make keyboard lights change automatically.

If that does not work try alieneffects-13r3, specifically made for Alienware 13 R3 or alienfx.
