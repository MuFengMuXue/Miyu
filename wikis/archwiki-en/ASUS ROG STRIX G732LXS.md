# ASUS ROG STRIX G732LXS

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (NVIDIA) || ||
|-
| Wireless || ||
|-
| Ethernet ||  ||
|-
| Audio || ||
|-
| Touchpad || ||
|-
| Bluetooth || ||
|}

## Audio
## Speakers not working/quiet
You need to create:

You can check

to see which card is normally added to PCH and which to NVidia. You can see it after the Soundcards recognised by ALSA section Both are using snd_hda_nvidia and you normally can only apply the model to that and you want to apply to PCH. So if that comes after Nvidia you can only use

And you are good to go. Or

if PCH is the first one.

## Video
Works with envycontrol or optimus it seems to have better performance with only using NVIDIA and not hybrid.

Using supergfxctl and an external monitor created a very laggy experience when the laptop screen was turned off. Also for some reason optimus does not always start with the latest kernel. At this point I would suggest using envycontrol if you would like to use nvidia only.

See https://asus-linux.org/
