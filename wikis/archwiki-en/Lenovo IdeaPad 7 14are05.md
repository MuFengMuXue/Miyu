# Lenovo IdeaPad 7 14are05

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard || ||
|-
| GPU || ||
|-
| Webcam ||  ||
|-
| Bluetooth ||  ||
|-
| SD-card reader || ||
|-
| Audio || ||
|-
| Wi-Fi ||  ||
|-
| Fingerprint reader || ||
|-
| TPM || ||
|}

## Specifications
This device is marketed both as Lenovo IdeaPad Slim 7 as well as Lenovo Yoga Slim 7 depending on the region. Hence, the below instructions should in principle apply to both these models and minor variants.

## Installation
Enter the UEFI Firmware setup by pressing (Fn+) F2 during boot and disable Secure Boot which should deactivate boot loader and kernel verification for Windows 10 against Lenovo and Microsoft keys. Proceed to ensure that the machine allows for booting from a USB key. Boot with the latest Arch Linux ISO image and follow the Installation guide.

## Accessibility
The appearance of the UEFI Firmware interface is reminiscent of regular BIOS'es and solely keyboard-driven.

The device has a convenient feature which is enabled by default in the UEFI Firmware, where pressing of a key when the device is off will display the state of charge (SoC) of the battery.

## Firmware
Firmware updates are supported  via :

Firmware updates should become / be made available for the following devices:

* Integrated Camera
* Samsung NVMe SSD
* System Firmware
* Touchpad
* UEFI dbx

## Secure Boot
Optionally verify the UEFI Firmware version via:

 # dmidecode -s bios-version

In order to enable Secure Boot with your own custom keys, follow the steps as outlined on the Secure Boot page, up to the point of installing your own Platform Key (PK).

An attempt to install a custom Platform Key will fail using the mentioned methods, including using  as well as  with error messages such as 'operation not permitted'.

These errors are due to the fact that the PK file in the firmware has the 'immutable' bit set. Source for this idea was a comment in this thread from the author of . To verify the state of the 'immutable' bit, do:

 $ lsattr /sys/firmware/efi/efivars/PK-(Lenovo key UID)

The output should be;

 ----i--------------

where the single 'i' indicates that the immutable bit is indeed set.

Proceed to unset the 'immutable' bit by entering:

 # chattr -i /sys/firmware/efi/efivars/PK-(Lenovo key UID)

Next, install your custom Platform Key (PK) as per one of the methods mentioned in the Secure Boot page instructions (, part of  should work fine). It should install without error.

Check the correct installation of the new PK:

 $ efi-readvar

It should list all custom keys/certificates (PK, KEK, DB, optionally dbx) as enrolled in the machine's UEFI Firmware.

Set the immutable bit for the new PK:

 # chattr +i /sys/firmware/efi/efivars/PK-(UID of your new PK)

The instructions from the Secure Boot page apply again  from this point.

## Bluetooth
Bluetooth works out of the box by simply following the instructions on the Bluetooth page.

## Power management
See Power management/Suspend and hibernate for the details on the various supported sleep states.

There are descriptions of ways of re-enabling the S3 power state on similar devices (see Lenovo IdeaPad 5 14are05#Suspend and here for example). However this has not been tested as of yet on this machine by the author.

## Energy Saving
The tips on the Power management page can be followed in order to optimize the power savings for the machine, such as creating configuration files in  for WiFi and audio power saving. This can be tested, verified and optimized in conjunction with  for example. When idling, the machine should consume as little as around 3W.

## Battery Conservation Mode
A simplified summary of lithium-ion battery chemistry limitations is that lithium-ion cells can get damaged when fully drained, but equally dislike being kept at or near 100% SoC (State of Charge), which stresses the cells causing them to degrade faster than normal/expected. In case lithium-ion batteries are to be stored or otherwise remain unused for a prolonged period of time, a SoC of around 50% to 60% is advisable (it is for example no accident that nearly all new devices such as tablets, cellphones etc. are pre-charged to around 50% SoC when one first unpacks them).

Equally, lithium-ion batteries should preferably be charged at 0,5C, meaning that the input current (Amps) should not exceed half of the cell's rated capacity (e.g. 2100mAh rated AA cell should preferably be placed in a charger that charges at max 1050 mAmps). Charging at higher rates can be done safely (even much higher rates can be achieved under controlled conditions, such as with cooling to prevent a 'thermal runaway' reaction) but will put a strain on the cells causing for faster degradation.

Several Lenovo laptops including this machine have hardware in place that manages both of the above, called battery Conservation Mode. Under GNU/Linux, this mode can be set persistently from the command-line. When set, the machine will either discharge to 60% or charge up to 60%, depending on the current SoC being either higher or lower.

Thus, in this mode, one can use the device as a desktop machine and safely leave the charger connected for extended periods of time.

In order to set this mode, first verify that the 'ideapad_laptop' kernel module has been loaded:

 # lsmod | grep ideapad_laptop

If not, you can attempt to load it manually:

 # modprobe ideapad_laptop

To turn on battery Conservation Mode for the machine, perform the following action:

 # echo 1 > /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode

Check/verify the current value:

 $ cat /sys/bus/platform/drivers/ideapad_acpi/VPC2004\:00/conservation_mode

It should now list "1"

The laptop should now charge/discharge until it reaches 60%.

At 60% the reported battery state should, instead of "charging" or "discharging", be reported as "unknown"

## HDMI
## Video
The HDMI output will work out of the box. Read the Multihead and xrandr pages in order to set up a second monitor and for example switch between the internal eDP screen and an external HDMI monitor.

## Audio
Additionally,  can be made to output sound to the speakers of the external display, if present. In order to do this, set the external monitor as default output using e.g.  or  or check the PulseAudio page for further reference. When the external monitor goes into standby or is disconnected, audio will automatically switch back to the machine's speakers.

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
|  ||  ||  || Enables Fn lock
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
|  ||  ||  ||
|-
|  ||  ||  || Lock X screen
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables/disables keyboard backlight
|-
|  ||  ||  || Page Up
|-
|  ||  ||  || Page Down
|}

# The key is visible via  (see package ) and similar tools.
# The physical key has a symbol on it, which describes its function.

## Tips and tricks
## Screen brightness control
Brightness of the built-in (eDP) screen can be set by echoing any value between 0 and 255 to /sys/class/backlight/amdgpu_bl0/brighness, e.g.

 # echo 70 > /sys/class/backlight/amdgpu_bl0/brightness
