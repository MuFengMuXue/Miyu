# Clevo W840SU

The W840SU is a device by the taiwanese OEM manufacturer Clevo. It is sold as Schenker S403, Tuxedo  Book UC1402 and Nexoc B401. A touch version exists as W840SU-T or UT1402. The hardware is configurable and includes an Intel Haswell Core i3/i5/i7, Intel HD 4400 graphics, a 7 mm harddrive, a mSATA device (storage, 3g/LTE modem) and a HDMI output.

## Installation
Installing Arch Linux is straightforward and most of the hardware works out of the box.

## Airplane Mode
Use xbindkeys to map the key 255 (NoSymbol) to some script that disables wifi and bluetooth and enables the airplane mode LED.

 $ cat ~/.xbindkeysrc
 "sudo /home/user/bin/setAirplane.sh"
    m:0x0 + c:255
    NoSymbol

Enable the LED with:

 # echo 1 > /sys/class/leds/tuxedo::airplane/brightness

## Webcam
The webcam needs to be activated by pressing FN+F10, otherwise you do not see the device.

## Sound
Sound mostly works out of the box. Using PulseAudio simplyfies configuration, switching outputs is possible.

Microphone

The volume control for the microphone is mislabeled and reads Digital in ALSA.

## Touchpad
The touchpad works out of the box with the synaptics driver. All current features are supported including two finger scroll, two- and three finger click and optional mouse buttons for the edges. Use synclient for configuration.
Four finger recognition and three finger swipe gestures do not seem to work, though.
