# Intel GVT-g

Intel GVT-g is a deprecated technology that provides mediated device passthrough for Intel iGPUs on 5th generation (Broadwell) through 10th generation (Comet Lake) processors. It can be used to virtualize the GPU for multiple guest virtual machines, effectively providing near-native graphics performance in the virtual machine and still letting your host use the virtualized GPU normally. This is useful if you want accelerated graphics in Windows virtual machines running on ultrabooks without dedicated GPUs for full device passthrough. (Similar technologies exist for NVIDIA and AMD GPUs, but they are available only in the "professional" GPU lines like Quadro, Radeon Pro and so on.)

There is also a variant of this technology called GVT-d, which is Intel's name for full device passthrough using the vfio-pci driver. With GVT-d, the host cannot use the GPU while it is passed through to a guest.

## Prerequisite
Intel GVT-g support is limited to processors from the 5th generation (Broadwell) through the 10th generation (Comet Lake). This is due to a lack of support in the i915 driver for the Gen11 graphics architecture found in 10th generation mobile processors (Ice Lake), and all subsequent architectures [https://www.intel.com/content/www/us/en/support/articles/000058558/graphics.html. While Ice Lake processors support GVT-d (full GPU passthrough), they do not support GVT-g.

For Xe Architecture (Gen12) and newer, the SR-IOV feature is the intended replacement. Refer to QEMU/Guest graphics acceleration#SR-IOV for more details.

You will have to create a virtual GPU first, then assign it to your virtual machine. The guest with a virtual GPU sees it as a "regular" GPU−just install the latest native drivers. (The virtual GPU actually does need specialized drivers to work correctly, but all the required changes are present in the latest upstream Linux/Windows drivers.)

You will need to:

* Use at least Linux 4.16 and QEMU 2.12.
* Enable IOMMU by adding  to your kernel parameters.
* Enable kernel modules: ,  and .
* Add the  kernel parameter to enable GPU virtualization.
* Add the  kernel parameter, see warning at Intel graphics#Enable GuC / HuC firmware loading.
* Optionally for better performance in DMA-BUF (especially if used with 60 FPS Qemu patch) disable framebuffer compression by adding the  kernel parameter.

After rebooting with the  kernel module parameter, you should be able to create virtual GPUs.

## With mdevctl
Install .

* You can list the types of virtual GPUs which can be created on your system like this:
 $ mdevctl types

The lower-numbered types are capable of higher resolutions, larger video memory allocations and will be able to use more GPU time slices.

* Define a new virtual GPU and set it to auto-start (at boot), replacing type and parent (most likely the same as in the example) with one from the previous step:
 # mdevctl define --auto --uuid $(uuidgen) --parent 0000:00:02.0 --type i915-GVTg_V4_1

* To get an overview of the defined devices:
 $ mdevctl list -d

* Finally start the device using UUID from the previous step:
 # mdevctl start --uuid 8629ed0d-f6a9-458c-a54c-5650e39180e2

* You may need to restart libvirtd daemon to get the devices to show up.

## Without mdevctl
Use this section if for some reason you don't want to or cannot use the mdevctl instructions above.

* Find the PCI address of your GPU  (e.g. ) by running .
* Generate a virtual GPU GUID ( in commands below) which you will use to create and assign the virtual GPU. A single virtual GPU can be assigned only to a single virtual machine - create as many GUIDs as you want virtual GPUs. (You can do so by running .)

You can list the types of virtual GPUs which can be created on your system like this:
 $ ls /sys/devices/pci0000\:00/$GVT_PCI/mdev_supported_types

The lower-numbered types are capable of higher resolutions, larger video memory allocations and will be able to use more GPU time slices.

A description of each types capabilities can be accessed like this
 $ cat /sys/devices/pci0000\:00/$GVT_PCI/mdev_supported_types/$GVT_TYPE/description

Pick a type you want to use - we will refer to it as  below.

Use the GUID you have created to create a virtual GPU with a chosen type:

 # echo "$GVT_GUID" > "/sys/devices/pci0000\:00/$GVT_PCI/mdev_supported_types/$GVT_TYPE/create"

You can repeat this as many times as you want with different GUIDs. All created virtual GPUs will land in  - if you would like to remove a virtual GPU, you can do:

 # echo 1 > /sys/devices/pci0000\:00/$GVT_PCI/$GVT_GUID/remove

Continue with one of the two options below based on your preference.

## Option 1: libvirt QEMU hook
With libvirt, a libvirt QEMU hook can be used to automatically create the virtual GPU when the machine is started, and to remove it when the machine is stopped. Replace the variables with the values you found above and the DOMAIN with the name of the machine.

Do not forget to make the file executable and to quote each variable value e.g. . You will also need to restart the libvirtd daemon so that it is aware of the new hook.

## Option 2: systemd service at boot
Alternatively to a QEMU hook, you can let systemd create the virtual GPU at boot. This does not rely on libvirt and appears to have no GPU performance drawbacks on the host machine as long as the virtual GPU is not used by a virtual machine.

Create a bash script and place the echo command to create the virtual GPU determined in Prerequisite inside. Make it executable. Ensure that the script cannot be modified by unprivileged users as it will be run as root at boot.

Now create a systemd service to run the script and give it these properties:

 After=graphical.target
 Type=oneshot
 User=root

## Assign a virtual GPU to the virtual machine
If you run  or  as a regular user, it may complain that some path  is not writeable. You need to enable write access to that path for the account, with  or .

## QEMU CLI
To create a virtual machine with the virtualized GPU, add this parameter to the QEMU command line:

 -device vfio-pci,sysfsdev=/sys/bus/mdev/devices/$GVT_GUID

## libvirt
Add the following device to the  element of the virtual machine definition:

Replace  with the UUID of your virtual GPU.

## Getting virtual GPU display contents
There are several possible ways to retrieve the display contents from the virtual GPU.

## Using DMA-BUF display
## QEMU CLI
Add  to the end of  parameter, e.g.:

 -device vfio-pci,sysfsdev=/sys/bus/mdev/devices/$GVT_GUID,display=on,x-igd-opregion=on

## libvirt
First, modify the XML schema of the virtual machine definition so that we can use QEMU-specific elements later. Change

to

Then add this configuration to the end of the  element, i. e. insert this text right above the closing  tag:

## Using DMA-BUF with UEFI/OVMF
As stated above, DMA-BUF display will not work with UEFI-based guests using (unmodified) OVMF because it will not create the necessary ACPI OpRegion exposed via QEMU's nonstandard fw_cfg interface. See this OVMF bug for details of this issue.

According to this GitHub comment, the OVMF bug report suggests several solutions to the problem. It is possible to:

* patch OVMF (details) to add an Intel-specific quirk (most straightforward but non-upstreamable solution);
* patch the host kernel (details) to automatically provide an option ROM for the virtual GPU containing basically the same code but in option ROM format;
* extract the OpROM from the kernel patch (source) and feed it to QEMU as an override.

We will go with the last option because it does not involve patching anything. (Note: if the link and the archive go down, the OpROM can be extracted from the kernel patch by hand.)

 is available, which is an up-to-date fork of the archived i915ovmfPkg, it is a currently the most advanced GVT-g ROM for use with OVMF, see this discussion. The AUR package installs the UEFI rom file as . First boot can take a while, especially if the guest OS needs to install drivers, as is the case with Windows 10.

Download  and place it somewhere world-accessible (we will use  to make an example).

## QEMU CLI
To specify the vBIOS ROM file, append  to .

## libvirt
Then edit the virtual machine definition, appending this configuration to the  element we added earlier:

## Enable RAMFB display (optional)
This should be combined with the above DMA-BUF configuration in order to also display everything that happens before the guest Intel driver is loaded (i.e. POST, the firmware interface, and the guest initialization).

## QEMU CLI
Add  to the end of  parameter, e.g.:

 -device vfio-pci,sysfsdev=/sys/bus/mdev/devices/$GVT_GUID,display=on,x-igd-opregion=on,ramfb=on,driver=vfio-pci-nohotplug

## libvirt
First, follow the first step of this section to modify the XML schema.

Then add this configuration to the end of the  element, i.e. insert this text right above the closing  tag:

## Display virtual GPU output
Due to an issue with spice-gtk, the configuration is different depending on the SPICE client EGL implementation.

## Output using QEMU GTK display
This method will get you higher refresh rate and less lag / input delay than SPICE display on weak CPUs, at least with Windows guests. Also it is less CPU-intensive than Looking Glass. But you lose useful SPICE display features, such as:
* shared clipboard (can be re-gained, see QEMU#qemu-vdagent)
* live USB redirection (you will need to assign the USB device before booting the guest)
* mouse cursor being free to come in and out of the virtual machine (will be grabbed, except if you use the USB tablet input device)
* integration of the display output into virt-manager (will spawn separate window for the GTK display)

The display output will only begin to work when the guest has started its proper Intel GPU driver (usually at the login screen). This means that:
* It is best if you install the Intel GPU driver beforehand or use a different virtual display adapter (like -vga std or for libvirt) together with the Intel vGPU to install the Intel GPU driver, then remove the std video adapter.
* You will never see the operating system booting and if it crashes before login you need to switch to a different virtual display adapter.
* If you need access to the BIOS, you need to enable the RAMFB display.

## QEMU CLI
Add  to the command line. The QEMU VGA adapter can be disabled by adding , or you have two virtual screens, and the one connected to the QEMU VGA adapter is blank.

## libvirt
* Ensure the above added  device have the  attribute set to .
* Ensure you have added the dummy line  to your  (from step Using DMA-BUF display).
* Remove all  and  devices.

The QEMU GTK display window needs to be told what display output it should use to run OpenGL on.
On a laptop first disconnect any external displays so you only have the laptop screen as a display.
Get the number of the display that your GPU outputs to by pasting into a terminal:
An example would be  .
You may now reconnect any displays you were using before.
Insert the number you just determined in the  line below.

* Add the following QEMU command line arguments:

## scaling
In windowed mode,  makes the GTK display window size be as large as the resolution of the guest display is, this gives you 1:1 pixel aspect ratio. Turning this on or leaving it out makes the guest display stretch/shrink to how big the GTK window happens to be (ugly scaling).

In fullscreen, you will get scaling anyways and when you change the guest resolution, the scaling only updates when lowering the resolution. When you increase the resolution the image grows larger than your display, so you need to exit fullscreen and enter it again.

## GTK display CPU load
This is a tradeoff between methods of copying the guest framebuffer to the GTK display window.

 in place of  delegates the task of copying the guest framebuffer to the GPU (via DMA).

This reduces the CPU load of the GTK display and can yield a much more responsive guest, especially on weak CPUs.

When this frame buffer copy operation shares GPU resources with an application loading the GPU, the displayed FPS are likely to drop and stuttering (irregular intervals between displayed frames) is likely to occur.

## Output using SPICE with MESA EGL
## QEMU CLI
Add  to the command line.  must be installed.

## libvirt
# Ensure the above added  device have the  attribute set to .
# Remove all  and  devices.
# Add the following devices:

There is an optional attribute  in the  tag to allow specify the renderer, e.g.:

## Output using SPICE with NVIDIA EGL or VNC
## libvirt
# Ensure the above added  device have the display attribute set to 'on'.
# Remove all  and  devices.
# Add the following devices:

The  type can be changed to 'vnc' to use VNC instead.

Also there is an optional tag  inside  tag to force a specific renderer, do not put inside the 'spice' graphics due the mentioned bug, example:

## Disable all outputs
If all outputs are disabled, the only way to see the display output would then be using a software server like RDP, VNC or Looking Glass. See PCI passthrough via OVMF#Using Looking Glass to stream guest screen to the host for details.

## QEMU CLI
In the  parameter, remove  and change to . Add  to disable the QEMU VGA adapter.

## libvirt
To ensure no emulated GPU is added, one can edit the virtual machine configuration and do the following changes:

# Remove all  devices.
# Change the  device to be type 'none'.
# Ensure the above added  device have the  attribute set to 'off'.

## Troubleshooting
## Missing mdev_supported_types directory
If you have followed instructions and added  kernel parameter, but there is still no  directory, first double-check that the  module is loaded.

You should also check whether your hardware is supported. Check the output of dmesg for this message:

If that is the case, you may want to check upstream for support plans.
For example, for the "Coffee Lake" (CFL) platform support, see https://github.com/intel/gvt-linux/issues/53

## Windows hanging with bad memory error
If Windows is hanging due to a Bad Memory error look for more details via dmesg. If the host kernel logs show something like rlimit memory exceeded, you may need to increase the max memory Linux allows QEMU to allocate. Assuming you are in the group , add the following to  and restarting the system.

 # qemu kvm, need high memlock to allocate memory for vga-passthrough
 @kvm - memlock 8388608

## Using Intel GVT-G in combination with PRIME render offload
Using Intel GVT-G while also using NVIDIA's PRIME render offload on the host causes several issues on the guest. It is suggested to use bbswitch to keep the card powered off or use it in conjunction with Bumblebee, nvidia-xrun or optimus-manager.

## No display
If your virtual machine is not displaying anything when using RAMFB display, try setting the following additional options to the existing  tag:

## Garbled graphics
If your virtual machine is displaying artifacts when the mouse enters the virtual machine screen, the following workaround might work.

First modify the XML schema as shown on #libvirt 2.

Then, insert this right above the closing  tag, taking care to add to the existing  tag, if existing:

## Host hanging when trying to suspend
After creating a GVT-g virtual GPU, host may hang when trying to suspend. See github to trace this bug.

A workaround is to remove the created GVT-g virtual GPUs before suspend and recreate the GVT-g virtual GPUs after waking from suspend. You can install  package to automatically do this for you.

## Changing the display resolution of virtual GPU
The display resolution of vGPU, by default, is the maximum resolution the vGPU is capable of. The display content will be scaled to this resolution by vGPU regardless of what resolution is set by guest OS. This would produce bad quality pictures in the viewer.

To change the display resolution, append  and  configuration into the  element:
