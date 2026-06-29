# QEMU/Troubleshooting

## Mouse cursor is jittery or erratic
If the cursor jumps around the screen uncontrollably, adding an environment variable before starting QEMU might help:

 export SDL_VIDEO_X11_DGAMOUSE=0

## No visible Cursor
Add  to QEMU's options to see a mouse cursor.

If that still does not work, make sure you have set your display device appropriately, for example: .

Another option to try is  as mentioned in QEMU#Mouse integration. This overrides the default PS/2 mouse emulation and synchronizes pointer location between host and guest as an added bonus.

## Two different mouse cursors are visible
Apply the tip QEMU#Mouse integration.

## Keyboard issues when using VNC
When using VNC, you might experience keyboard problems described (in gory details) here. The solution is not to use the  option on QEMU, and to use  from . See also this message posted on libvirt's mailing list.

## Keyboard seems broken or the arrow keys do not work
Should you find that some of your keys do not work or "press" the wrong key (in particular, the arrow keys), you likely need to specify your keyboard layout as an option. The keyboard layouts can be found in .

 $ qemu-system-x86_64 -k keymap disk_image

## Could not read keymap file
 qemu-system-x86_64: -display vnc=0.0.0.0:0: could not read keymap file: 'en'

is caused by an invalid keymap passed to the  argument. For example,  is invalid, but  is valid - see .

## Guest display stretches on window resize
To restore default window size, press .

## ioctl(KVM_CREATE_VM) failed: 16 Device or resource busy
If an error message like this is printed when starting QEMU with  option:

 ioctl(KVM_CREATE_VM) failed: 16 Device or resource busy
 failed to initialize KVM: Device or resource busy

that means another hypervisor is currently running. It is not recommended or possible to run several hypervisors in parallel.

## libgfapi error message
The error message displayed at startup:

 Failed to open module: libgfapi.so.0: cannot open shared object file: No such file or directory

Install  or ignore the error message as GlusterFS is a optional dependency.

## Kernel panic on LIVE-environments
If you start a live-environment (or better: booting a system) you may encounter this:

 [ end Kernel panic - not syncing: VFS: Unable to mount root fs on unknown block(0,0)

or some other boot hindering process (e.g. cannot unpack initramfs, cant start service foo).
Try starting the virtual machine with the  switch and an appropriate amount of RAM, if the ram is to low you will probably encounter similar issues as above/without the memory-switch.

## Windows 7 guest suffers low-quality sound
Using the  audio driver for Windows 7 guest may result in low-quality sound. Changing the audio driver to  by passing the  arguments to QEMU and installing the AC97 driver from Realtek AC'97 Audio Codecs in the guest may solve the problem. See Red Hat Bugzilla – Bug 1176761 for more information.

## Could not access KVM kernel module: Permission denied
If you encounter the following error:

 libvirtError: internal error: process exited while connecting to monitor: Could not access KVM kernel module: Permission denied failed to initialize KVM: Permission denied

Systemd 234 assigns a dynamic ID for the  group (see ). To avoid this error, you need edit the file  and change the line with  to .

## "System Thread Exception Not Handled" when booting a Windows virtual machine
Windows 8 or Windows 10 guests may raise a generic compatibility exception at boot, namely "System Thread Exception Not Handled", which tends to be caused by legacy drivers acting strangely on real machines. On KVM machines this issue can generally be solved by setting the CPU model to .

## Certain Windows games/applications crashing/causing a bluescreen
Occasionally, applications running in the virtual machine may crash unexpectedly, whereas they would run normally on a physical machine. If, while running  as root, you encounter an error mentioning , the reason for those crashes is that KVM injects a General protection fault (GPF) when the guest tries to access unsupported Model-specific registers (MSRs) - this often results in guest applications/OS crashing. A number of those issues can be solved by passing the  option to the KVM module, which will ignore unimplemented MSRs.

Cases where adding this option might help:

* GeForce Experience complaining about an unsupported CPU being present.
* StarCraft 2 and L.A. Noire reliably blue-screening Windows 10 with . The blue screen information does not identify a driver file in these cases.

## High interrupt latency and microstuttering
This problem manifests itself as small pauses (stutters) and is particularly noticeable in graphics-intensive applications, such as games.

* One of the causes is CPU power saving features, which are controlled by CPU frequency scaling. Change this to  for all processor cores.
* Another possible cause is PS/2 inputs. Switch from PS/2 to Virtio inputs, see PCI passthrough via OVMF#Passing keyboard/mouse via Evdev.

## QXL video causes low resolution
QEMU 4.1.0 introduced a regression where QXL video can fall back to low resolutions, when being displayed through spice. For example, when KMS starts, text resolution may become as low as 4x10 characters. When trying to increase GUI resolution, it may go to the lowest supported resolution.

As a workaround, create your device in this form:

 -device qxl-vga,max_outputs=1...

## Virtual machine not booting when using a Secure Boot enabled OVMF
 and  files from  are built with SMM support. If S3 support is not disabled in the virtual machine, then the virtual machine might not boot at all.

Add the  option to the qemu command.

See  and https://github.com/tianocore/edk2/blob/master/OvmfPkg/README for more details and the required options to use Secure Boot in QEMU.

## Virtual machine not booting into Arch ISO
When trying to boot the virtual machine for the first time from an Arch ISO image, the boot process hangs. Adding  to kernel boot options by pressing  in the boot menu you will get more boot messages and the following error:

 :: Mounting '/dev/disk/by-label/ARCH_202204' to '/run/archiso/bootmnt'
 Waiting 30 seconds for device /dev/disk/by-label/ARCH_202204 ...
 ERROR: '/dev/disk/by-label/ARCH_202204' device did not show up after 30 seconds...
    Falling back to interactive prompt
    You can try to fix the problem manually, log out when you are finished
 sh: can't access tty; job control turned off

The error message does not give a good clue as to what the real issue is. The problem is with the default 128MB of RAM that QEMU allocates to the virtual machine. Increasing the limit to 1024MB with  solves the issue and lets the system boot. You can continue installing Arch Linux as usual after that. Once the installation is complete, the memory allocation for the virtual machine can be decreased. The need for 1024MB is due to RAM disk requirements and size of the installation media. See [https://lists.archlinux.org/archives/list/arch-releng@lists.archlinux.org/message/D5HSGOFTPGYI6IZUEB3ZNAX4D3F3ID37/ this message on the arch-releng mailing list and this forum thread.

## Guest CPU interrupts are not firing
If you are writing your own operating system by following the OSDev wiki, or are simply getting stepping through the guest architecture assembly code using QEMU's  interface using the  flag, it is useful to know that many emulators, QEMU included, usually implement some CPU interrupts leaving many hardware interrupts unimplemented. One way to know if your code is firing an interrupt, is by using the  argument.

to enable showing interrupts/exceptions on stdout.

To see what other guest debugging features QEMU has to offer:

 $ qemu-system-x86_64 -d help

or replace  for your chosen guest architecture.

## KDE with sddm does not start spice-vdagent at login automatically
Remove or comment out  from . == Bluetooth audio quality drops after QEMU starts ==

Disable the WirePlumber profile's auto-switching feature to prevent it from using mono audio profiles.
 $ wpctl settings --save bluetooth.autoswitch-to-headset-profile false

## Linux guest boot hangs with GRUB in UEFI mode
After updating to  202505-1 or newer, it becomes impossible to boot many Linux distributions that use GRUB in UEFI mode (known examples include versions of Rocky Linux, Debian, RHEL and Fedora). This also extends to the distributions' live ISO images.

Issue tracker: [https://gitlab.archlinux.org/archlinux/packaging/packages/edk2/-/issues/9 archlinux/packaging/packages/edk2#9

As of  202508-1, this issue still persists.

## Symptoms
* When attempting to boot a GRUB menu entry:
** the graphical SPICE console freezes
** exception information reporting a page fault is printed to the serial console
** CPU usage for QEMU is pinned at 100% on 1 core

## Example of serial console output
## Workarounds
* Manually downgrade  to 202411-1 and hold version until fix is released
* Apply patch from Debian's edk2 as detailed on the issue tracker and add a fwcfg line with needed guests.
* Install Fedora's EDK2-OVMF  alongside , and change the firmware path on launch for needed guests.
