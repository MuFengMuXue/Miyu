# Dell G5 SE 5505

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| GPU ||  ||
|-
| Wi-Fi ||  ||
|-
| Bluetooth ||  ||
|-
| Audio ||  ||
|-
| Touchpad ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|}

This page describes the Dell G5 SE 5505 laptop in thorough detail.

## Installation
Before booting into the installation media, disable Secure Boot in your BIOS. The BIOS is accessed by pressing the  or  key during the POST screen. To access the boot menu directly, press  during the POST screen. Install Arch Linux as usual with the UEFI installation method. It may be required to use the  kernel parameters if GPU crashes are experienced. If there is an active Windows partition present, disable fast startup to prevent complications while installing Arch.

## Accessibility
If you are an individual with accessibility needs, this will unfortunately not be a great device for you. The FN shortcuts, BIOS UI, thermal management quirks, basic display, and lack of error code beeps are not accommodating for those with accessibility needs. This device contains no diagnostic LEDs aside from the ambiguous status indicator LED near the charge port.

## Firmware
There are a few ways to update the firmware on this device. Using Windows and the Dell provided tools on the support page for this laptop is certainly one of them, but that method often causes many issues.

Before we begin, make sure UEFI Capsule Updates is enabled in the UEFI settings. Passing firmware updates (especially UEFI or similar I/O updates) from an OS to the NVRAM (where firmware data is "physically stored" on the motherboard) is impossible to achieve otherwise.

Since we are downloading files to a storage medium with very limited storage capacity, it is important to make sure there is sufficient available space in the NVRAM partition. Often times the above referenced Dell support tools used to install capsule updates from Windows fills the NVRAM with dump logs.

Navigate to the  and make sure to remove all  files within this directory, if any.

Now there are no dump files, we can update the system firmware by running fwupd. When running  your device may restart: do not touch anything, especially the power button/AC adapter and let the updates run their course.

## Graphics and display
## Drivers
By default, there is very basic graphical functionality and performance. install  to run general 3D programs.
See AMDGPU and Vulkan for full graphics installation information and instruction.

## Screen tearing
There is no screen tearing out of the box for Wayland sessions, but for gaming (at the time of writing) Wayland has considerable render and input latency unless the game is running in exclusive full-screen mode.

To eliminate screen tearing on X11 environments, see AMDGPU#Tear free rendering. This will also increase input and render latency unless pertinent display environment variables are explicitly configured.

## Dedicated GPU override
Many programs will default usage to the integrated GPU. To force (almost) any program to take advantage of the dedicated GPU, run , where  is the desired process you want to launch with your dGPU. For steam titles, adding DRI_PRIME=1 %command% to the launch options will make that specific title launch with the dGPU.
For further clarification, read PRIME#For open source drivers - PRIME.

## Resizable BAR support
AMD's Smart Access Memory ("Resizable BAR") will not function on this device until it is manually enabled.
The default BIOS configuration does not have SAM enabled, nor does it have an option available to enable it.
Use of a BIOS editing tool, such as Smokeless Runtime Efi Patcher (SREP) is required to enable SAM/Resizable BAR.

## Thermal and power management
## Fan control
An easy way to manually control fans, or to manually create custom fan curves i to use a this python script which can more accurately push the fans according to CPU and GPU temperatures. This script also restores the defunct  "boost" functionality by providing a command that manually activates the boost profile as defined by UEFI data.

## Monitoring sensor data
By default, the kernel loads the  module to check CPU thermals. To monitor GPU temperature and see fan speeds, you will have to force load the  kernel module (see for its documentation), which is not loaded by default on this laptop.

 # modprobe dell-smm-hwmon restricted=0 ignore_dmi=1

To make this setting permanent, create:

and

You should now see a dell result in the result of .

## CPU
The packages  and  (optional GUI for ryzenadj) should work out of the box to control maximum temperature and TDP of your CPU. For example, the following command will restrict your CPU TDP to 40 Watts and maximum temperature to 70°C (perfectly safe on this laptop).
 # ryzenadj -a 40000 -b 40000 -c 40000 -f 70

see [https://github.com/FlyGoat/RyzenAdj and for detailed instructions on how to use these tools.

## Frequency
Undervolting and overclocking are not conventionally possible on this laptop.  does not seem to have any effect on zen2 processors.[https://github.com/r4m0n/ZenStates-Linux/issues/8#issuecomment-679468427

 is working down to 1.40 GHz.  fails to load with BIOS Version 1.14.0:

 kernel: amd_pstate: the _CPC object is not present in SBIOS or ACPI disabled.

This more than likely ties into the strange no sleep/hibernation issue.

The default BIOS lacks CPPC support and an option to enable it, leading to this error. To enable CPPC and subsequently allow the  driver to load, a BIOS editing tool like Smokeless Runtime Efi Patcher (SREP) is required.

## GPU
It may be possible to use . Also see AMDGPU#Overclocking. Unknown compaitibility (2024-06-04)

While it increases performance, the battery lasts under two hours when  is used and the dedicated GPU never turns off.

Since Kernel Version 6.0.x and BIOS Version: 1.13.0 amdgpu power management sees fewer GPU crashes.

Show power management profiles:
 # cat /sys/class/drm/card?/device/pp_power_profile_mode

Enable power saving mode (as root):

 # echo manual > /sys/class/drm/card0/device/power_dpm_force_performance_level
 # echo "2" > /sys/class/drm/card0/device/pp_power_profile_mode

See amdgpu kernel documentation

## Disabling dGPU
To potentially reduce power draw by disabling the dedicated GPU, a udev rule can be employed. Create the following rule (e.g., at /etc/udev/rules.d/90-disable-dgpu.rules) :

{{hc|/etc/udev/rules.d/90-disable-dgpu.rules|2=
ACTION=="add", \
  KERNEL=="0000:03:00.0", \
  SUBSYSTEM=="pci", \
  ATTR{class}=="0x03\
  ATTR{power/control}="auto", \
  ATTR{remove}="1"
}}

For more context and discussion, refer to this [https://bbs.archlinux.org/viewtopic.php?id=292457 forum thread.

Alternatively, the dedicated GPU can be disabled via a BIOS editor like Smokeless Runtime Efi Patcher (SREP), similar to enabling CPPC or Resizable BAR.

## System power states
Suspension and hibernation features simply do not work. You can try to enabling its support via BIOS injection, see == Keyboard ==

The keyboard for this device features a four section LED backlight with 18.7mm x 18.05mm keys. The keyboard by defauly features a QWERTY layout. The North American model contains 81 keys, the UK mod contains 82 keys, and the model released in Japan contains 85 keys.

## Function key
{| class="wikitable"
|-
! Input Key
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Enables Game Shift Mode. OS dependent unless a compatibility script is installed.
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
|  ||  ||  ||
|-
|  ||  ||  ||
|-
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
