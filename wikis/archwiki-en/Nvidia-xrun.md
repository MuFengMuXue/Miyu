# Nvidia-xrun

nvidia-xrun is a utility that allows NVIDIA Optimus-enabled laptops to run X server with discrete NVIDIA graphics on demand. This solution offers full GPU utilization, compatibility and better performance than Bumblebee.

X server can only be used with integrated graphics or discrete NVIDIA graphics, but not both, so the user might want to switch to a separate virtual console and start another X server using different graphics from what was used for the first X server.

## Installation
Install:

* The NVIDIA driver
* (recommended) or  (old method, uses bumblebee to switch off the dedicated card)
* Any window manager, since running application directly like with  is not recommended.

## Configuration
## Setting the right bus id
Find your display device bus id:

 $ lspci -d 10de::03xx | awk '{print $1}'

It might return something similar to . Then create a file (for example ) to set the proper bus id:

Also this way you can adjust some NVIDIA settings if you encounter issues:

## External GPU setup
You can also use this in an external GPU setup. Make sure to load the nvidia-modeset and nvidia-drm modules and add the option  to the "Device" section.

Change the auto-generated configuration to use the internal display on devices with multiple NVIDIA cards:

Remember to set the bus id to the correct graphics card.

## Automatically run window manager
For convenience you can create an  file with your favorite window manager. (if using nvidia-xrun  0.3.78 should disable the card automatically so this method is unneccessary}}
When the NVIDIA card is not needed, bbswitch can be used to turn it off. The nvidia-xrun script will automatically take care of running a window manager and waking up the NVIDIA card. To achieve that, you need to:

Load the  module on boot:

 # echo 'bbswitch' > /etc/modules-load.d/bbswitch.conf

Disable the  module on boot:

 # echo 'options bbswitch load_state=0 unload_state=1' > /etc/modprobe.d/bbswitch.conf

After a reboot, the NVIDIA card will be off. This can be seen by querying 's status:

 $ cat /proc/acpi/bbswitch

To force the card to turn on/off respectively run:

 # echo OFF > /proc/acpi/bbswitch
 # echo ON > /proc/acpi/bbswitch

For more about bbswitch see Bumblebee-Project/bbswitch.

## Usage
## Start  at boot
Enable  - this shuts down the NVIDIA card during boot.

Once the system boots, from the virtual console, login to your user, and run .

If above does not work, switch to unused virtual console and try again.

As mentioned before, running applications directly with  does not work well, so it is best to create an  file as outlined earlier, and use  to launch your window manager.

## Troubleshooting
## NVIDIA GPU fails to switch off or is set to be default
See #Use bbswitch to manage the NVIDIA card.

If NVIDIA GPU still fails to switch off, or is somehow set to be default whenever you use or not , then you might likely need to blacklist specific modules (which were previously blacklisted by Bumblebee). Create this file and restart your system:

There seems to be a race condition between  and  which loads the  modules. If the latter runs first,  will hang (actually the  command) during device removal. If on the other hand  runs first then it will succeed, and later the modules will fail to load with an error (which is harmless but ugly). For this reason it might be better to always blacklist the above modules.

DRM kernel mode setting should be enabled for PRIME synchronization to work (for example on muxless devices where only the Intel GPU is connected to outputs). However, consider disabling it in case there is an issue. See NVIDIA#DRM kernel mode setting

On certain hardware, the NVIDIA GPU exposes two devices on the PCI bus: a 3D controller and an audio device. In this case, both devices need to be removed from the bus in order for the GPU  to fully power down. This can be done by simply adding a line for the audio device bus id in , and the corresponding line in the function   in  to remove the second device.
