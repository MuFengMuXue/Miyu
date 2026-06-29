# ASUS ROG G533QS

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (AMD) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Wi-Fi ||  ||
|-
| Ethernet ||  ||
|-
| Audio ||  ||
|-
| Touchpad || ||
|-
| Bluetooth ||  ||
|}

## Audio
## Rear speakers not working/quiet
Add the following kernel module parameter:

 snd-hda-intel model=alc294-lenovo-mic

Install , run hdajackretask.

* Select Realtek ALC285 from the dropdown menu.
* Check the box marked Show unconnected pins.
* Override pin  with Internal Speaker (Back).
* Override pin  with microphone.
* Override pin  with Internal Speaker (LFE).
* Click Install boot override and reboot.

## Troubleshooting
## USB-C to video
Install  and .

Enable/start   .

 # supergfxctl -m Dedicated
 # echo 0 > /sys/devices/platform/asus-nb-wmi/dgpu_disable
 # echo 1 > /sys/bus/pci/rescan
 # echo 0 > /sys/devices/platform/asus-nb-wmi/dgpu_disable

Enable/start the  user unit.

Add the following kernel parameters to your boot loader:

 rd.driver.blacklist=nouveau modprobe.blacklist=nouveau

Autostart the following:

 xrandr --setprovideroutputsource modesetting NVIDIA-0
 xrandr --auto
