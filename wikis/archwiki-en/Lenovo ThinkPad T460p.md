# Lenovo ThinkPad T460p

{| class="wikitable archwiki-table-laptop"
! Hardware !! PCI/USB ID !! Working?
|-
| Bluetooth (Broadcom) || ||
|-
| Bluetooth (Intel) ||  ||
|-
| Webcam (Acer) ||  ||
|-
| Webcam (Chicony) ||  ||
|-
| Ethernet ||  ||
|-
| WLAN (Broadcom) ||  ||
|-
| WLAN (Intel) ||  ||
|-
| WWAN (Huawei) ||  ||
|-
| WWAN (Sierra) ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Touchpad || ||
|-
| Touchscreen || ||
|-
| Trackpoint || ||
|-
| Keyboard || ||
|-
| TPM || ||
|-
| Fingerprint reader ||  ||
|-
| Smart card reader ||  ||
|-
| SD card reader ||  ||
|-
| Audio ||  ||
|}

The performance class variant of the Lenovo ThinkPad T460.

## Firmware
It is recommended that you peruse all the available options and features in the BIOS as there are many of them and in some cases you will get unexpected behaviours, e.g. swapping the  and  keys, enabling topmost keyboard row  to  functionality as the default, etc. To access the BIOS, press  on boot-up. Enable Diagnostics mode bootup instead of Quick mode to make it easier to enter the BIOS.

## Secure boot
In laptops with Secure Boot enabled, if you install a kernel module provided by a 3rd party or compiled by yourself, modprobe will not load it and will throw an error similar to this:

 modprobe: ERROR: could not insert 'vboxdrv': Required key not available

Secure Boot will prevent this module from running until you provide a valid signature for it. Therefore, you can either try to sign it yourself or disable Secure Boot altogether. Unfortunately, the current Secure Boot firmware (v2.11 2016/09/26) installed in the ThinkPad T460 series BIOS is unable to complete the signing process, thus it is recommended to disable it in the BIOS configuration until this issue is resolved.

See also: == Fingerprint reader ==

The T460p's Validity fingerprint reader is [https://gitlab.freedesktop.org/libfprint/wiki/-/wikis/Unsupported%20Devices unsupported by the fprint project's  library. Thus, installing the  package instead is necessary for the fingerprint reader to function. Discussion surrounding an official driver can be found at https://forums.lenovo.com/t5/_/Validity-Fingerprint-Reader-Linux/td-p/3352145.

See https://github.com/3v1n0/libfprint#readme regarding device initialization. To initialize the fingerprint reader without using a Windows installation, install  and run the following command:

 # validity-sensors-tools -t initializer

See also https://linux-hardware.org/?id=usb:138a-0090.
