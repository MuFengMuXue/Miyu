# ASUS AT3IONT-I

This page describes the steps necessary to get all of the features of the ASUS AT3IONT-I working correctly. It assumes you already successfully installed Arch Linux and installed the basic software (ALSA for audio,  and  packages for wireless in the Deluxe edition, etc.)

## Audio over HDMI
## ALSA
Many ION boards exhibit problems when trying to play sound through HDMI. They usually require a custom ALSA configuration via  (or, alternatively, on a per-user basis via ).

{{hc|/etc/asound.conf|2=# Needed in order to get sound over HDMI to function

#$ aplay -l
# **** List of PLAYBACK Hardware Devices ****
# card 0: NVidia NVidia, device 0: ALC887 Analog Analog
#   Subdevices: 1/1
#   Subdevice #0: subdevice #0
# card 0: NVidia NVidia, device 1: ALC887 Digital Digital
#   Subdevices: 1/1
#   Subdevice #0: subdevice #0
# card 0: NVidia NVidia, device 3: NVIDIA HDMI HDMI
#   Subdevices: 1/1
#   Subdevice #0: subdevice #0

pcm.!default {
  type plug
  slave.pcm "dmix:0,3"
}
}}

Also, please note that audio over HDMI currently only works in an X session (graphical environment). If you are trying to get the sound to work when running on a virtual terminal, it will not work. Please see this post on the Arch Forums.

## PulseAudio
If you are loathe to mess with your PulseAudio settings in , it might be enough to just unmute the  channel in . It is hidden, as you need to press , then select  and scroll to the far right before you can find it. Highlight it, and then press  to unmute.

## Deluxe Edition
The deluxe edition comes with a few extra goodies, such as DC power on-board, mini-PCI WiFi, RCA stereo output, on-board Bluetooth, and an included IR Remote.

## Bluetooth
The Bluetooth chip is an Atheros with a device ID of . It uses the  driver which has been included in the kernel since ~2.6.33 and works out of the box with the default Arch kernel.

## Wireless
The wireless chipset is an Atheros AR9285.

It uses the  driver, which has been included in the default kernel since 2.6.27. In other words, udev should load the driver without problems -- there should be no extra configuration to get wireless working on the ASUS AT3IONT-I.

## RCA Stereo Output
Untested.

## Remote
The Asus remote has limited functionality out of the box. Everything except the eight 'special' media buttons at the bottom. Also, you may have to blacklist the kernals  module since is fails out. LIRC's  module handles the remote better, but still does not support all the buttons on the Asus remote.

Source of the following approach and module developer: user pj7 on a Ubuntu forum thread.

The included IR receiver requires a kernel module to be built to accommodate it. Apparently, it is a rather tricky little device. It seems to work best with the included remote -- it coverts the included remotes' button presses directly to keyboard keystrokes, but when using another MCE remote it reports to the system the raw code. It seems to understand other signals, but you will need a remote that sends the right signal. This results in limited functionality of the device where it can only use the included ASUS remote, a JP1 Programmable remote (to program the known signals), or a universal remote that has the ability to learn the IR signals of the ASUS remote.

As a result, this section will focus on getting the included remote working with the included receiver, based on pj7's driver.

Download the source and then extract with . The resulting directory will include the source files, along with a Linux-to-X11 input key map. Before you build the source, you must edit . This file maps the button presses to Linux input keys. Be aware that Linux input ''does not equal'' X11 input. Graphical programs, such as media players, Kodi, and the like, are only aware of X11 inputs, and so you must match a X11 input with a Linux input to. That's what the  file is for.

For example, if you wish to define the "Next Track" button as "XF86AudioNext" (which most programs will look for to play the next item in the playlist), you will need to define  in  as  rather than . This is because  maps to "XF86AudioNext" (KEY_NEXT does not register as anything).

Once you have finished mapping the buttons, run :

Install the driver with  (as root).

Now we must make sure the driver loads correctly. One thing that you must do is blacklist the  driver that tries to load whenever the IR Reciever is detected. Then you must make sure that the new  driver loads before  as  will try to take over the receiver. This can all be easilly accomplished by the  line in :

You have to blacklist mceusb in :

(rebooting the computer might be necessary)

After that, all the buttons on the Asus remote should work. If you find that you would rather assign different actions to button presses, it is easy to edit the  file and  again. Alternatively, you may be interested in Xmodmap.

## Resources
* ASUS AT3IONT-I deluxe on Ubuntu forums
