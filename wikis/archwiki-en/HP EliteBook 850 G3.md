# HP EliteBook 850 G3

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU (Intel) ||  ||
|-
| GPU (AMD) ||   ||
|-
| Ethernet ||  ||
|-
| Wi-Fi ||  ||
|-
| Cellular ||  ||
|-
| Bluetooth ||  ||
|-
| NFC ||  ||
|-
| Audio ||  ||
|-
| Webcam ||  ||
|-
| Memory Card Reader ||  ||
|-
| Touch-pad || ||
|-
| Fingerprint Reader ||  ||
|-
| Fan Control ||  ||
|-
| TPM ||  ||
|-
| Smart Card Reader ||  ||
|-
| Battery ||  ||
|-
| HP Docking || ||
|}

The HP Elitebook 850 G3 is a business grade workstation laptop released in 2017, the laptop is very durable and the ecosystem of HP devices are a well fit for a neat portable system. Most of the internal parts are cross compatible with the generation 4 (G4) Elitebooks and can easily be upgraded and be swapped in and out for wanted/remove unwanted features.

## Firmware
## UEFI / Secure Boot
Secure Boot and TPM backed disk encryption is tested and works. Enrolling custom keys for secure boot is supported but is not tested, proceed with caution.

## Configuration
## AMD Graphics
The AMD Radeon R7 M365X is supported by both radeon and AMDGPU drivers, but AMDGPU driver performs better.

## Fan control
Fan control requires additional software to be configured. Install  read Fan speed control for more information.

 # nbfc config -s "HP EliteBook 850 G3"

## Cellular
NetworkManager uses ModemManager for mobile broadband connection support.

Setting up  does not set up the modem properly. Add the following udev rule & script to manually configure the modem to operational mode,

{{hc|/etc/udev/rules.d/99-hp-modem.rules|2=
ACTION=="add", ATTR{idVendor}=="03f0", ATTR{idProduct}=="9d1d", RUN+="/usr/local/bin/hp-modem-setup.sh"
}}

Give executable permissions to the modem set up script, reload udev and trigger an usb even to set up the device:

 # udevadm trigger --action=add /sys/bus/usb/devices/1-3

Confirm that the modem is set up by running:

 $ mmcli -L

## Touchpad
To enable synaptics intertouch on Synaptics TM3140-001 for a better touch pad experience:

 # modprobe -r psmouse
 # modprobe psmouse synaptics_intertouch=1

If all works well you can make the changes persistent in next boot by adding the driver parameter to Kernel parameters.

## Tips and tricks
## Battery
Setting charging thresholds on the fly is unsupported. HP Intelligent charging can be used on windows to change battery health configurations on the fly while powered on. However battery health configurations (Maximize for Duration/Health, Let HP Manage..) could be set in the firmware setup. Maybe a UEFI variable + reboot mechanism of some sort can be developed as a workaround.

## HP Docking
The docking port on the right side of the device below the sim card slot is and older docking standard that is now discontinued. To recognize whether the device is docked or not the path to the device can be found out by running:

 $ find /sys/devices/platform -name dock -print -exec cat {} \;

A list of tested docks are listed,
{| class="wikitable"
! Dock !! Working?
|-
| HP UltraSlim Docking Station (B9C87AA#ABA) ||
|}

## Systemd + Udev
Below commands guides on how to setup docked and mobile targets with udev on a systemd configured system to aid with other tasks in the system. This can flexibly be used to for example mount file systems when docked or de/activate other systemd units that match the device profile when docked / mobile.

{{hc|/etc/udev/rules.d/99-dock-detect.rules|2=
# trigger an action(a) when the SMSC USB5534 hub in the dock is added

SUBSYSTEM=="usb", ACTION=="add",    ATTR{idVendor}=="0424", ATTR{idProduct}=="5434",      RUN+="/bin/systemctl start docked.target"
SUBSYSTEM=="usb", ACTION=="remove", DEVPATH=="/devices/pci0000:00/0000:00:14.0/usb2/2-4", RUN+="/bin/systemctl stop  docked.target"

SUBSYSTEM=="usb", ACTION=="add",    ATTR{idVendor}=="0424", ATTR{idProduct}=="5434",      RUN+="/bin/systemctl stop  mobile.target"
SUBSYSTEM=="usb", ACTION=="remove", DEVPATH=="/devices/pci0000:00/0000:00:14.0/usb2/2-4", RUN+="/bin/systemctl start mobile.target"
}}

Here is an example use case where hpfall can be deactivated when the system is docked.

## HPFall (HP 3D DriveGaurd)
The laptop built to work with hard drives has an accelerometer to unload the drive head to prevent damage to the hard drive. If you have a harddrive the same feature is implemented by hpfall and is tested and works, follow the guide in hpfall to configure. The accelerometer can also be used for other purposes, values can be read using the jstest utility from the .

 $ jstest /dev/input/js0

## NFC
The NFC device on the board is unsupported by the NFC software/firmware stack.

## Fingerprint
The fingerprint device "Validity Sensors, Inc. VFS495 Fingerprint Reader" does not work, as the firmware is proprietary and it's functionality is obscure to be integrated to the linux pam components. There are reverse engineered drivers that work with older kernels and older versions of libcrypto and other dependencies but later versions of packages seems to break commonly linked resources.

## Function keys
{| class="wikitable"
! Key(s) !! Control Action !! Status (assuming appropriate software)
|-
|  || Suspend || Sleep / Suspend the device to RAM by default, can be configured for hybrid sleep if set up.
|-
|  || Keyboard Backlight || Toggle keyboard backlight levels. (Off, Low, High)
|-
|  || Monitor Modes || Switch between monitor modes. (Extended, Mirrored, Joined, etc.)
|-
| , || Brightness Control || Main / In-built monitor brightness control, down and up respectively.
|-
| ,  || Volume Control || Volume up/down control respectively on the main audio output source.
|-
|  || Mute Audio Input || Toggle to mute the main audio input source. (Turn on/off mic)
|-
|  || Screen Capture || Triggers screen snipping/capture.
|-
|  || Radio Control || Toggles all radio devices on/off. (Cellular, Wifi, & Bluetooth)
|-
|  || Audio Mute || Toggles all audio outputs on/off.
|}
