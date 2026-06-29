# Lenovo ThinkPad P1

Lenovo ThinkPad P1 was released in 2018 and has up to Intel Core i7-8850H or Xeon E-2176M 6-core processor, up to 64 GB DDR4 RAM, and up to NVIDIA Quadro P2000 graphics.

## Installation
## Do not change to "Discrete Graphics" with BIOS v1.15
https://www.reddit.com/r/thinkpad/comments/a2g0k4/warning_do_not_change_from_hybrid_graphics_to/

This might potentially brick your device and require Lenovo to replace your motherboard.
Apparently verified on BIOS v1.15 and still not resolved.

You will want to use BIOS v1.18 or newer.  BIOS v1.17 (released Dec 24, 2018) originally fixed the issue for the mass majority; however, this version has been removed due to additional bricking issues that happen occasionally related to the Hybrid graphics options when changed.

## Firmware update
Before installation, it is recommended that you boot into Windows 10 and use the preinstalled Lenovo Vantage software to install any necessary firmware updates, particularly this one.

## Installation with hybrid graphics
Currently the live CD might not boot normally if your BIOS is configured to enable hybrid graphics. See NVIDIA Optimus for details. Two options are possible:

* Disable hybrid graphics by changing your BIOS settings to "Discrete only" (Be careful, this might brick your latpop: #Do not change to "Discrete Graphics" with BIOS v1.15)
* Alternatively, before booting into live CD, press  and add  to your kernel parameters.

If you choose to use the second option, you might also want to include  in your .

## HiDPI screen
Some configurations of ThinkPad P1 comes with a HiDPI screen. See HiDPI#Linux console (tty) for more details.

## Graphics
There are two difficulties with configuring graphics on ThinkPad P1: there is no "integrated graphics only" option in the BIOS, and the external display ports (HDMI, etc.) are wired into the NVIDIA chip. Depending on your needs, you might choose from the following options:

## Discrete only
As the P1 is an hybrid device with both an integrated and discrete video card, the NVIDIA drivers have to be setup to use Optimus in order to properly work with external outputs and the integrated laptop screen. Setup NVIDIA Optimus as instructed in NVIDIA Optimus#Use NVIDIA graphics only.
Note that this method will keep your NVIDIA graphics card always on, which might dramatically shorten your battery life.

## Black screen after X starts with NVIDIA drivers
Even if using Optimus, the driver might anyway fail to detect the laptop screen using the auto-generated  file and you might experience a black screen after X has been started. See NVIDIA Optimus#No screens found on a laptop/NVIDIA Optimus for more details.

If you are able to connect an external monitor and verify it works, you can inspect the  output to verify only HDMI and Display Port outputs are actually detected. The  tool should as well display only external video output connections.

In order to instruct the driver about the integrated laptop screen, the  file has to be modified to add a  to the  (see NVIDIA/Troubleshooting#Screen(s) found, but none have a usable configuration)

Use the following as

   Section "Device"
       Identifier      "nvidia"
       Driver         "nvidia"
       VendorName     "NVIDIA Corporation"
       BusId          "1:0:0"
       Option         "AllowEmptyInitialConfiguration"
       Option	      "ConnectedMonitor" "eDP"
       Option	      "CustomEDID" "eDP:/sys/class/drm/card0-eDP-1/edid"
       Option	      "IgnoreEDID" "false"
       Option	      "UseEDID" "true"
   EndSection

After re-starting X, the integrated screen output  should show be now detected and properly usable.

If the laptop screen gets detected but  fails to properly detect the available resolutions, remove the  and  options from  and restart X

## Hybrid graphics with Reverse PRIME
Set up Reverse PRIME to do the main rendering on the Intel chip, while still being able to use the external display outputs wired to the NVIDIA chip. Battery life should remain decent with this option.

## Hybrid graphics with Bumblebee
See Bumblebee for detailed instructions. If Xorg refuses to start after setting up Bumblebee, try generating an Xorg configuration by running  and copy it to .

Because Bumblebee normally disables the NVIDIA card, display outputs such as HDMI might not show up in . You may want to refer to Bumblebee's multi-monitor setup page.

## Hybrid graphics with bbswitch only
This method requires manual switching between integrated and discrete graphics mode. Switching between them requires restarting all Xorg instances, although it does not require a restart.

Install the appropriate NVIDIA graphics drivers and . Generate an Xorg configuration by running  and copy it to . You may also create , though it should not be necessary.

After loading the module with

 # modprobe bbswitch

you can switch to discrete graphics with the following Bash function:

 discrete() {
     killall Xorg
     modprobe nvidia_drm
     modprobe nvidia_modeset
     modprobe nvidia
     tee /proc/acpi/bbswitch  /tmp/gpu_state && echo ON > /proc/acpi/bbswitch"
#ExecStart=/usr/bin/modprobe nvidia

Install
WantedBy=shutdown.target
WantedBy=reboot.target
WantedBy=hibernate.target
WantedBy=suspend-then-hibernate.target
WantedBy=sleep.target
WantedBy=suspend.target
}}

And a service to disable the card again at resume if it was originally off:
