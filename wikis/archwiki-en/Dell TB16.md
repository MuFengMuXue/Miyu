# Dell TB16

Dell's TB16 is a popular Thunderbolt Dock with power-delivery, ethernet, USB, audio, HDMI, DisplayPort, mini-DP and VGA.  It generally works well in Linux when configured correctly with up-to-date firmware, but works better with some notebooks than others.  If you are in the market for a new dock, you are better off purchasing Dell's newer WD19 series, which has reviewed more positively and does not suffer from the various issues reported against the TB16.  See also Dell's note on their Official TB16 Ubuntu Support and its limitations.

## Configuration
## Thunderbolt Security
You should either:

* Disable Thunderbolt security in the BIOS (recommended)
* Use boltctl to temporarily authorize or permanently enroll the dock ''and cable''.

Thunderbolt security "works" but may result in random instability, particularly system freezes on resume, and USB HID devices (mouse, keyboard) behaving erratically.  It is suggested to ensure your system is completely stable before enabling this.

## Dell Type-C Dock Configuration
The TB16 is commonly used with Dell laptops, which have a special BIOS option which may cause stability issues.  You should disable the following option:

* Dell Type-C Dock Configuration
** Always Allow Dell Docks (uncheck this)

## Firmware Updates
## Github
A new community-driven method, mentioned in in this github repo by flhofer , provides a new approach that lets you flash most of TB16 firmware on any Thunderbolt-equipped system.

The list of components that can be updated with this method are:
# Synaptics MST-1 VMM3320: DP + VGA stream processing
# Synaptics MST-2 VMM3330: mini-DP + HDMI stream processing
# Thunderbolt TB16 Cable: Intel DSL6540 'Alpine Ridge' TB bridge
# Thunderbolt TB16 Dock: Intel DSL6540 'Alpine Ridge' TB bridge and USB3.1
# ASM USB controller: ASM 1042A USB 3.0 host controller

## Reddit
The firmware updates provided for Windows at Dell's TB16 Support: Drivers page include firmware that cannot be updated in Linux, such as the ASMedia USB Host Controller firmware which fixes numerous instability USB issues and Synaptics controller (DisplayPort).

To summarize jasondclinton's post on reddit:

# The NVM updates to the TB controller can be flashed by Linux (using the standard nvm_nonactive nvm_authenticate sysfs interface)
# There is no way to install the ASMedia, Synaptics, etc firmwares - so you might as well flash everything from Windows.
# You need all the latest updates for the docker firmware updater to even see the TB16.

Ensure you have the latest:

# BIOS firmware
# Windows Update
# Dell Update
# Thunderbolt NVM firmware (for the Thunberbolt controller on your device) - should be covered by Windows & Dell updates
# TB16 firmware updater from the drivers page above.

Even after having used the firmware updater, there are still other firmwares from the same Dell support page, which supersede the versions included in the firmware updater, that should be downloaded and installed afterwards, e.g. the ASMedia driver / firmware.  If in doubt, install all updates on the page.

jasondclinton also notes that the official NVM updates are often far behind Intel's latest releases (e.g. TB16's 1.0.0 firmware includes NVM 16 wherehas Intel had already released NVM 33 at time of writing).  It is unknown if there is an easy way to update these independently.

## Troubleshooting
## Bus issues
Issues such as the USB bus (and all connected devices) failing when plugging/unplugging devices are improved by following all the instructions above (notably, *disabling* Thunderbolt Security, "Dell Type-C Dock configuration options" and firmware updates).  Read the firmware updates section carefully: not all updates are possible via Linux.

Some devices behave differently in the dock vs directly on laptop's USB ports, e.g. Microsoft's keyboard receiver is erratically put to sleep, or gets stuck repeating a particular key.  The un-intuitive fix for this is to disable Thunderbolt security (see note about this above).

## Disabling PCIE power manage
Issues with the USB bus failing can also be mitigated by disabling PCIE power management in the TLP config.  Create an  with the following line:

Verify that you have the correct serial using  as in the comments.

Run  as root to reload the configuration.

## Unbinding and Rebinding
You can use this script to recover from bus failures without rebooting.  Useful for laptops without great compatibility with the TB16, especially after resuming from suspend:

{{bc|
#!/bin/sh

# 0b:00.0 USB controller ASMedia Technology Inc. ASM1042A USB 3.0 Host Controller [1b21:1142
SERIAL=$(lspci -Dd "1b21:1142" | awk '{ print $1 }')
DRIVER="/sys/bus/pci/drivers/xhci_hcd"

echo -n $SERIAL | sudo tee $DRIVER/unbind
sleep 4
echo -n $SERIAL | sudo tee $DRIVER/bind
}}

## Blank screen on boot with Nvidia drivers
If, when using Nvidia drivers, you get a black screen on boot with the dock and 3 external monitors connected, there is a good chance the machine is trying to use the 3 external displays plus the internal display of the laptop. This can be resolved by writing a block into  or your display manager's custom xstart scripts e.g. for SDDM the default for KDE. the file is
{{hc|/usr/share/sddm/scripts/Xsetup|
xrandr --setprovideroutputsource modesetting NVIDIA-0

internaldisp=""
if [ `xrandr | grep " connected " | wc -l` -gt 3 ]; then
        xdisplays=`xrandr | grep " connected " | awk '{print $1}'`
        for xdisplay in $xdisplays; do
                if  "$xdisplay" == "$internaldisp"* ; then
                        xrandr --output $xdisplay --off
                else
                        xrandr --output $xdisplay --auto
                fi
        done
else
        xrandr --auto
fi
}}
