# Lenovo IdeaPad U330p

## Overview
This subnotebook exists in two configurations (see below)

There are no major issues with the first one. Everything works.
There is a Wi-Fi issue with the second one, but it is repairable.

This page contains just some comments that may be useful during installation or troubleshooting.

## Hardware
The unit used for testing contained the following hardware:

* Intel Core i5-4200U Processor

* Intel HD Graphics 4400

* Atheros AR9462 Wireless Network Adapter or Intel 7260

* A thin Seagate 500GB hybrid drive (i.e. 500GB HDD + 8GB SSD) or 256GB SSD

## Installation
The best way to ensure that Arch Linux is correctly installed is to follow the Installation guide step by step.

In the second configuration your Wi-Fi will not work out of the box (connection will drop repeatedly). There is a work-around:
unload iwlmvm and iwlwifi kernel modules (iwlwifi needs iwlmvm)

 # modprobe -r iwlmvm iwlwifi

and load iwlwifi without 11n support. For the parameter list see

 # modinfo -p iwlwifi

to load use

 # modprobe iwlwifi 11n_disable=1

iwlmvm will then load automatically, if you load iwlmvm before iwlwifi, it will load iwlwifi automatically with default parameters.

Check with

 # systool -v -m iwlwifi

that 11n_disable is set to 1.
Now you have a stable Wi-Fi. To set  permanently after the installation see Kernel modules

You may also have to enable software encryption. The configuration file  will look like this:

## BIOS setup
Before booting with the USB stick, enter the BIOS in order to prepare the machine for the new OS. For that purpose, press the small button on the side panel next to the HDMI port. A boot menu will appear. Select "BIOS Setup", and then:

* In the "Security" menu, disable "Secure Boot" (although Arch Linux can be configured to work with secure boot, this will probably spare you a few issues during installation).
* In the "Boot" menu, leave "Boot Mode" set to "UEFI", and "USB Boot" enabled.
* In the "Exit" menu, set "OS Optimized Defaults" to "Other OS". Exit by saving changes.

## Configuration
## Sound card
Set the default sound card by creating an  file in :

and then reboot.

Install  and run  to unmute the channels, as described here.

## Video driver
Use .

## Touchpad
Install .

This will make sure that the touchpad works correctly and will also provide two-finger scrolling.

## Troubleshooting
## Use of headphones
If you use headphones often and you shutdown the machine with the headphones plugged in, it may happen that in the next reboots the sound is directed to the headphones by default, even when the headphones are not plugged in.

To fix this issue:

* Plug the headphones in and out. The sound should now be directed to the speakers.

* Install and run  once (you do not have to do anything, just open it, browse through the different tabs, and close it).

* Reboot the machine (ensuring that the headphones are not plugged in). The sound should now be directed back to the speakers by default.

## Network connectivity/latency
When using NetworkManager, it appears that wireless networking is not as responsive as it could or should be. For example, there is a noticeable lag when trying to acess some websites that should open immediately (e.g. Google, YouTube, etc.)

On the Web, there are several reports of connectivity/latency problems with this particular hardware (Atheros AR9462). However, some testing with Wicd seems to indicate that the network adapter is working fine.

There are some things that can be tried to alleviate this problem:

* Disable IPv6 in NetworkManager. Go to Wi-Fi settings and turn off IPv6 for each wireless network that you connect to.

* Create an  file to specify the option :

and then reboot.
