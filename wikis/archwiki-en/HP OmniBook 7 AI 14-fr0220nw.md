# HP OmniBook 7 AI 14-fr0220nw

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU ||  ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|-
| NPU ||  ||
|}

## Installation
Secure Boot was not tested.

 must be installed to get audio, and  to get Bluetooth, Wi-Fi, and extra GPU functionality like hardware video decoding.

The UEFI implementation deletes any other boot loaders if it detects that  exists on the EFI system partition.  will successfully add a new entry to the boot table, but it is going to be gone by the time the laptop reboots. This means that dual-booting with Windows is only possible by copying the real Windows Boot Manager to a separate file (say, ), overwriting  with your desired boot loader, and chainloading the real Windows Boot Manager from it. Keep in mind that the file will get occasionally overwritten by Windows updates.

The Customized Boot option mentioned in Laptop/HP#Troubleshooting is not available in this laptop.

## Audio
Speaker/mic mute LEDs (located on the  and  keys) do not work by default as the audio chip uses the same IDs as another hardware configuration (mailing list thread here).

This can be fixed by passing a  parameter to the  module, for example by creating a file with the following content and saving it as  :

 options snd-sof-intel-hda-generic hda_model=103c:876e

or any of the other methods listed in Setting module options.

## Power management
Suspending works okay, and causes a flurry of (harmless) key presses to be reported :

 atkbd serio0: Unknown key pressed (translated set 2, code 0xab on isa0060/serio0).
 atkbd serio0: Use 'setkeycodes e02b ' to make it known.

Hibernation works okay too, also without the kernel's  parameter which means the UEFI implementation does not seem to destroy the  variable. No extra key presses are reported when entering hibernation.

## Keyboard backlight
Seems to be managed entirely by firmware as there are no entries in  to manipulate it. However, pressing the backlight key does raise an event - see table below.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || See #Keyboard backlight control below
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || See #FnLock control below
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|}

# The key is visible to  and similar tools
# The physical key has a symbol on it, which describes its function

## Keyboard backlight control
Pressing the key is reported by the kernel's  module as an "Unknown key code" :

 hp_wmi: Unknown key code - 0x30021aa
 hp_wmi: Unknown key code - 0x33221aa
 hp_wmi: Unknown key code - 0x36421aa

 is reported when turning the backlight on to "level 1" from completely off,  when going from "level 1" to "level 2", and  when going from "level 2" to completely off.

## FnLock control
Similarly to backlight control, this is recognised by the kernel's  module as an "Unknown key code" :

 hp_wmi: Unknown key code - 0x21ab
 hp_wmi: Unknown key code - 0x121ab

 is reported when turning FnLock on, and  when turning it off.
