# MSI Vector A18 HX A9WX

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad ||  ||
|-
| Keyboard ||  ||
|-
| GPU (AMD) ||  ||
|-
| rowspan="2" | GPU (NVIDIA) || ||
|-
|  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Wi-Fi || rowspan="2" |  ||
|-
| Bluetooth ||
|-
| Speakers || rowspan="2" |  ||
|-
| Microphone ||
|-
| TPM 2.0 || ||
|}

MSI Vector A18 HX A9WX refers to the following laptop models:

* MSI Vector A18 HX A9WIG
* MSI Vector A18 HX A9WHG

The only apparent difference between the models is the dedicated NVIDIA GPU (RTX 5080 Max-Q or RTX 5070-Ti Max-Q) and the  varied display options that both models have.

The MSI Raider A18 HX A9WX models are nearly identical to the Vector A9WX, the only difference being more RGB Leds on the Raiders and there being an RTX 5090 model among the Raiders.

These laptops seem to work extremely well out of the box with the biggest issue being lack of support for interacting with the mux switch and rgb keyboard lighting from linux.

## Audio
Speakers work perfectly out of the box.

If the speakers mysteriously stop working on the laptop and will not work even on other operating systems, a BIOS update may resolve the issue. This problem can happen after a hard shutdown (holding the power button), thus using SysRq keyboard shortcuts for hard shutdowns instead should help avoid this situation.

Microphone is not detected. It was not detected on windows 10 either, so it's possible that laptop does not have a mic or the testing was done on a defective model (since the soundcard works the microphone should work too)

## Wi-Fi and Bluetooth
Occasionally after a reboot, Bluetooth and/or Wi-Fi will malfunction. This can be fixed with a cold boot.

## Touchpad
It works, gestures and palm detection have not been tested.

## Function keys
{| class="wikitable"
|-
! Key
! Detected
! Labeled
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Keyboard Brightness
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||  (Screen switch)
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Fan Mode
|-
|  ||  ||  ||
|-
|  ||  ||  || Crosshair
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Fn-Lock(Hardware)
|-
|  ||  ||  || Unknown
|-
|  ||  ||  || Unknown
|}

## Binding unbound keys
When pressing a key that is not bound properly (like the bluetooth key) dmesg will output a message like the following:

 atkbd serio0: Unknown key released (translated set 2, code 0xf3 on isa0060/serio0).
 atkbd serio0: Use 'setkeycodes e057 ' to make it known.

See Map scancodes to keycodes#Using setkeycodes.

Sometime between the original writing of this page and now, a regression seems to have broken the TouchpadToggle button on this model.

 gives us  with  being an unmapped (NoSymbol) key instead of  which it used to be before.

The simplest solution to this problem is to just bind this key combination to your touchpad toggling method. If you need the keycode for it you can use  or  to obtain it (in your environment it will likely not be the same as the one given by showkey which is 194).

## RGB Backlighting
Besides the keyboard lighting button, there is currently no way to control the RGB lighting. If you change the RGB lighting from Windows, the changes will stay even after rebooting into linux.

There is a gitlab issue for openrgb here.
