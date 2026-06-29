# Asusctl

allows ROG & TUF laptop owners to control their laptops from a CLI, it supports keyboard control (brightness, RGB and backlight effects), setting a custom charge limit, changing system power profiles, setting custom fan curves and controlling AniMe matrix displays.

## Installation
Install the  package or alternatively from a custom repository.

Some Laptops may require a custom version of Linux for all supported features to work. see custom kernel for details.

## Configuration
 stores its configuration files in , Aura and AniMe profile files are stored in  and the  user specific file is .

## RGB/Keyboard backlight
Supported laptop models are stored in , if your laptop is not working out of the box then you can add it to this list to see if its supported. See README.md for details.

If you still have no support then you should open an issue on the projects Gitlab page.

## Custom effects
Defining custom effects is handled by a systemd service and settings are stored at . To make use of custom effects you should enable the  user unit.

See the  section of the ASUS Linux manual for details.

## AniMe matrix display
For laptops that have an AniMe matrix display, the settings and options to control it are stored at .

To make use of it under Linux you first need to enable the  user unit.

See the  section of the ASUS Linux manual for details.

## Usage
Issuing the command  on its own will output a list of supported options. You can also use subvalues to list options from subcategories, for example  will list all options from the BIOS subcategory.

When dealing with subcategories, your current setting can be queried by swapping the case of the flag. Uppercase flags make changes, lowercase flags query current setting. For example  will return the current panel overdrive state while  will set it to enabled.

## Show supported options
The following command is used to display all the options your laptop supports:

 $ asusctl info --show-supported

## Charge limit
Set a battery charge limit with the following:

 $ asusctl battery limit limit

where limit is between 20 and 100.

## RGB/Keyboard backlight
Use the following commands to toggle LED modes:

Next mode:

 $ asusctl aura --next-mode

Previous mode:

 $ asusctl aura --prev-mode

## Panel overdrive
If your laptop supports panel overdrive it can be toggled with the following command:

 $ asusctl armoury set panel_overdrive

## Power profiles
,  and  modes are supported.

Change power profiles with the following:

 $ asusctl profile set profile

or use the following to cycle through all profiles:

 $ asusctl profile next

You can set a power profile in  if you wish to have one automatically loaded during boot.

## Using the MUX switch
## Switching to discrete graphics only (MUX switch)
supergfxctl is capable of detecting whether the MUX switch is enabled or not and does not cause the display manager to fail if it is enabled. Using other Optimus managers with asusctl to control a MUX might cause issues.

Switching to discrete graphics is done with the following command:

 $ supergfxctl -m AsusMuxDgpu

and then rebooting.

## Switching back to Optimus mode
Switching to Optimus mode is done with the following command:

 $ supergfxctl -m hybrid

and then rebooting.

## Using the MUX switch with a Wayland client
Switching over to the dGPU should work as normal on Wayland clients however NVIDIA GPU users should consult NVIDIA#Wayland configuration before trying to switch. NVIDIA GPUs still have some issues running certain applications under Wayland.

## rog-control-center
Many functions of asusctl can be controlled in a GUI, it is packaged as  or can be obtained from the custom repository.

If your laptop has RGB, backlighting effects or an AniMe matrix display then using this tool will drastically improve your ability to control them.

## Custom fan curves
Using rog-control-center it is possible to define custom fan curves for both the CPU and GPU, for each of the supported power profiles.
