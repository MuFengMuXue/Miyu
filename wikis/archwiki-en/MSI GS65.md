# MSI GS65

{| class="wikitable archwiki-table-laptop"
|-
! Hardware !! PCI/USB ID !! Working?
|-
| Touchpad || ||
|-
| Keyboard ||  ||
|-
| GPU (Intel) ||  ||
|-
| GPU (NVIDIA) ||  ||
|-
| Webcam ||  ||
|-
| Ethernet ||  ||
|-
| Bluetooth ||  ||
|-
| Thunderbolt || ||
|-
| Audio ||  ||
|-
| Wi-Fi ||  ||
|}

For a general overview of laptop-related articles and recommendations, see Laptop.

## Installation
Secure Boot can be disabled from the Security tab and boot mode can optionally be switched from UEFI to legacy. This laptop has advanced UEFI settings if desired.

## Firmware
BIOS version E16Q2IMS.110 introduces many ACPI problems if booting is changed from UEFI to Legacy, including a flood of  at boot, which can be solved through kernel parameters:

*  allows to boot but most things will not work, including the keyboard and touchpad.
*  or  allows to boot and have working keyboard and touchpad, but the NVidia card will not work ; neither will the USB3 ports.
*  will allow most things to work: keyboard, touchpad, USB 3 devices, NVIDIA card.

## Video
## NVIDIA GPU multihead support
The HDMI and DP ports are wired to the Nvidia GPU, so some additional actions required to make the multihead to work with monitors connected to this ports. Thunderbolt port is wired to Intel GPU thus allowing for external monitor to be used with Nvidia GPU off. See Bumblebee#Output wired to the NVIDIA chip, though configuration from there possibly would not work as is.

Instructions to get the external monitor working on the HDMI and DP ports on MSI GS65:

1. Install  and .

2. Configure Xorg to use the  (not the ) video driver for the Intel GPU.

3. Make Xorg launched by intel-virtual-output to use the Nvidia GPU:

4. Restart X server

5. Launch the

6. Use  or other tool to turn on the monitor and adjust its position.

 $ xrandr --output VIRTUAL1 --right-of eDP1 --preferred

External monitor should be under the VIRTUAL1 output in . If not - check that  successfully run the X server on DISPLAY=:8 and the  shows the connected monitor.

Limitations

It looks like the only one is inability to use VDPAU hardware video decoding, though to be honest it could be used directly on DISPLAY=:8 as an ugly hack (make sure your WM ignores the external screen first). But NVENC/NVDEC does not depend on X and could be used with tools like ffmpeg and gstreamer, and the Intel Quick Sync VAAPI also works, so missing VDPAU is a minor issue.

## Hybrid graphics
Like most modern laptops with hybrid graphics, the GS65 uses the Optimus MUXless scheme and supports the ACPI methods necessary for the complete power down of the dedicated NVIDIA GPU (Runtime D3cold), saving large amounts of power when not in use.

If using the latest proprietary NVIDIA drivers  or , this should work nearly out of box without needing tools like Bumblebee simply by setting the  option of the  module:

If the laptop's power LED settles from orange to white, this means the NVIDIA GPU is currently powered down. Use this and tools like  to troubleshoot any configuration issues or misbehaving programs probing the GPU for no valid reason.

If you experience issues with the GPU's power management, visit PRIME#NVIDIA and this page for more details. If this still does not solve them, check if explicit ACPI D3cold capability is enabled in the advanced BIOS settings.

Note that some ACPI-related kernel parameters (like ) or custom DSDT tables might make  this feature inoperable. Proceed with care.

## Power management
An issue when sleeping is that the networking will be disabled when waking and set to airplane mode. This issue does not affect hibernation.

## Keyboard backlight
The Steel Series lights on the keyboard cannot be configured with  because this tool only works with region-based RGB lighting. For this laptop model, the tool  provides partial control.

If keyboard lights remain off, be sure you have rebooted after installing msi-perkeyrgb to refresh udev and that the brightness is turned to maximum with , then try the command again.

For switching colors with a key, create a script file:

{{hc|msi-rgb-switch.sh|
profs=(aqua chakra default disco drain freeway plain rainbow-split roulette disable)
fn="./.msi-rgb"
touch $fn
prof=$(cat $fn)
if [ -z $prof ]; then
    echo "0" > $fn
    vl=0
else
    nv=$(($((prof+1)) > 9 ? 0 : $((prof+1))))
    echo $nv > $fn
    vl=$nv
fi
if [ ${profs= "disable" ; then
    msi-perkeyrgb -m GS65 -d
else
    msi-perkeyrgb -m GS65 -p ${profsfi
}}

and map the script to a shortcut key. This will rotate to the next RGB color automatically.

## Function keys
{| class="wikitable"
|-
! Key
! Visible?1
! Marked?2
! Effect
|-
|  ||  ||  || Inputs .
|-
|  ||  ||  || /
|-
|  ||  ||  || . This also brings the webcam online and exposes it to the kernel.
|-
|  || 4 ||  || Unmapped.
|-
|  ||  ||  || /Airplane mode. Hardblocks Wi-Fi and removes Bluetooth from the USB bus. Enabled by EC. See #Airplane mode switch.
|-
|  ||  ||  || . Enabled by EC. See #Airplane mode switch.
|-
|  ||  ||  || Similar to  but does not send . See #Airplane mode switch.
|-
|  || 3 ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || Non-functional.
|-
|  || 4 ||  || Increases keyboard backlight brightness.
|-
|  || 4 ||  || Decreases keyboard backlight brightness.
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
|  || 4 ||  || Unmapped.
|-
|  || 4 ||  || Unmapped.
|}

# The key is visible to  and similar tools.
# The physical key has a symbol on it, which describes its function.
# systemd-logind handles this by default.
# Triggers unknown key events. Can be mapped to valid keycodes with  or Input remap utilities. Monitor  when pressing these keys.

## Airplane mode switch
The airplane mode key combinations ,  and  are disabled by default. They can re-enabled in a couple ways. This is especially relevant as resuming from sleep usually hardblocks the Wi-Fi card.

## Using kernel parameters
The simplest and safest method is by adding the following kernel parameters:

 acpi_osi=! acpi_osi="Windows 2009"

However, this might alter or disable other power management features, as this works by tricking the ACPI DSDT into thinking it's running on an older version of Windows.

## Using the EC (Embedded Controller)
Another more surgical, slightly riskier but more complete solution which does not involve ACPI, is to use  to write to the laptop's EC which temporarily restores the switch's functionality. Write byte  at offset . Unless you have the above kernel parameters active, the value before writing should be . Check with .

 # isw -s 0x34 48

After a few seconds, the key combinations should work.

Additionally, with the airplane mode's functionality restored, writing  (disable) or  (enable) at offset  will change the state of the radio killswitch:

 # isw -s 0x2e 9

These commands can be used as part of systemd units and other scripts to automate control of the platform's airplane mode and mitigate sleep resume issues.

Perform these actions at your own risk. The offsets should be identical for you, but always double-check your own EC's memory dump using , comparing values against the above, before writing to it. Do not write to any other location unless you know what you are doing. If you encounter unexpected issues, you may need to reset the EC by powering off the laptop and either removing the battery or pressing the pinhole switch on the underside for 10 seconds with the AC cable disconnected. Connect the cable before booting.

A more detailed explanation can be found on the Talk:MSI GS65#Unblocking wifi after sleep page.

## Touchpad
Multi gestures do not work out the box, but are detected with .

## Thermals
Fan control by "Fancontrol (lm-sensors)" or "NoteBook Fan Control (NBFC)" is not supported, but by the use of the tool  you can control the fans in the same way as Dragon Center on Windows.

## Microphone
GS65 has twin microphones, which is pleasing to have for noise reduction and echo cancellation, as well as background sounds suppression via beamforming technique. To get the best of it, configure:

Also, it could be useful to add  to  to disable automatic gain control.

If you are using PipeWire instead of PulseAudio, use the following configuration instead:

{{hc|/etc/pipewire/pipewire.conf.d/echo-cancel.conf|
context.modules = [
   {   name = libpipewire-module-echo-cancel
       args = {
           # If you want to keep format from master device
           use_master_format = true
           aec_method = webrtc
           aec_args = {
               beamforming = true
               mic_geometry = "-0.025,0,0,0.025,0,0"
               analog_gain_control = false
           }
           source_name = "echo-cancel-source"
           sink_name = "echo-cancel-sink"
       }
   }

}}

Optionally, make the  your default:

{{hc|/etc/wireplumber/main.lua.d/51-default-source.lua|
default_sources  {
   "echo-cancel-source"
}
}}

Restart the    user units.

Confirm if it is working with:

 $ pw-cli ls Node | grep -i echo

or

 $ pactl list sources short}}

You should see  as a source and select it in applications which use the microphone.

## Known issues
## Lockup Issue (lspci and poweroff hang)
Symptoms:
* lspci hangs
* poweroff hangs

Applies to: Arch boot ISO and systems with nouveau or without nvidia driver installed. See NVIDIA Optimus#Lockup issue (lspci hangs).

Solutions:
* Arch ISO: Add  to the kernel parameters (https://superuser.com/a/1301487).
* System using : Should not run into this issue.  may not work and cause this, however.
* System using nouveau: Add  to the kernel parameters. This disables runtime power-management, which causes this issue to begin with.

## Cheese hangs while opening the camera
The issue can be fixed by installing  and running:

 $ vlc v4l:// :v4l-vdev="/dev/video0"

Following this, cheese should work correctly.

## Wi-Fi is hardblocked (airplane mode) after waking up from suspend
Waking from suspend will have Wi-Fi in airplane mode. https://askubuntu.com/questions/1043547/wifi-hard-blocked-after-suspend-in-ubuntu-on-gs65

Wi-Fi can be reactivated by either using the airplane mode key combination twice or by hibernating and rebooting.

A  way to mitigate this is by setting systemd to hibernate instead of suspending.

## System freeze
From time to time the graphical interface will freeze and the keyboard will be unresponsive, though audio keeps running. It tends to happen when CPU temperature is high and CPUs are throttling.

There is no known solution for this.

It is not clear what causes this issue:

Issue caused by the Intel E2500 Wi-Fi card.

Wi-Fi card ask for a hardware reset. (System will freeze for +/- 10s)

Fixed by replacing the Wi-Fi card.

## Display outputs do not work after suspend
If the laptop is suspended with another monitor connected, then on wake all display outputs do not recognise when an external display is connected to any port.  This persists across reboots.  Worryingly it also persists if you reboot into Windows.

One workaround is to boot into Windows, suspend the laptop, then wake it.  Connected displays will then be recognised when rebooting into Windows or Arch. Another workaround is to suspend and wake until the connected display is recognized. Sometimes this takes several tries but it avoids having to boot into Windows.

Another workaround is to disable audio devices.
