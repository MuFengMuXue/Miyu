# VirtualBox/Install Arch Linux as a guest

This article is about installing Arch Linux in VirtualBox.

Boot the Arch installation media through one of the virtual machine's virtual drives. Then, complete the installation of a basic Arch system as explained in the Installation guide.

## Installation
## Installation in EFI mode (optional)
Enabling EFI for Arch as guest is optional. If you want to install Arch Linux in EFI mode inside VirtualBox, you must change the firmware mode for the virtual machine. This must be done before installing Arch as guest, changing the option afterwards will result in an unbootable machine unless the setting is reverted.

To enable EFI for a virtual machine using the graphical interface, open the settings of the virtual machine, choose System item from the panel on the left and Motherboard tab from the right panel, and check the checkbox Enable EFI (special OSes only).

Alternatively the same can be accomplished from the command line using VBoxManage:

 $ VBoxManage modifyvm "Virtual machine name" --firmware efi

 will set the firmware for the virtual machine to EFI with the bitness matching the virtual machine's CPU. To get a specific EFI bitness, set the firmware to  for x86_64 EFI or  for IA32 EFI.

After selecting the kernel from the Arch Linux installation media's menu, the media will hang for a minute or two and will continue to boot the kernel normally afterwards. Be patient.

## Install the Guest Additions
VirtualBox Guest Additions provides drivers and applications that optimize the guest operating system including improved image resolution and better control of the mouse. Within the installed guest system, install:

*  for VirtualBox Guest utilities with X support
*  for VirtualBox Guest utilities without X support

The guest additions running on your guest, and the VirtualBox application running on your host must have matching versions, otherwise the guest additions (like shared clipboard) may stop working. If you upgrade your guest (e.g. ), make sure your VirtualBox application on this host is also the latest version. "Check for updates" in the VirtualBox GUI is sometimes not sufficient; check the VirtualBox.org website.

## Configuration
## Load the VirtualBox kernel modules
To load the modules automatically, enable  which loads the modules and synchronizes the guest's system time with the host.

To load the modules manually, type:

 # modprobe -a vboxguest vboxsf vboxvideo

## Set optimal framebuffer resolution
See VirtualBox#Set guest starting resolution.

## Launch the VirtualBox guest services
After the rather big installation step dealing with VirtualBox kernel modules, now you need to start the guest services. The guest services are actually just a binary executable called  which will interact with your X Window System.  manages the following features:

* shared clipboard and drag and drop between the host and the guest;
* seamless window mode;
* the guest display is automatically resized according to the size of the guest window;
* checking the VirtualBox host version

All of these features can be enabled independently with their dedicated flags:

 $ VBoxClient --clipboard
 $ VBoxClient --draganddrop
 $ VBoxClient --seamless
 $ VBoxClient --checkhostversion
 $ VBoxClient --vmsvga

Notice that  can only be called with one flag at a time, each call spawning a dedicated service process. As a shortcut, the  bash script enables all of these features.

 installs  that launches  on logon. If your desktop environment or window manager does not support XDG Autostart, you will need to set up autostarting yourself, see Autostarting#On desktop environment startup and Autostarting#On window manager startup for more details.

VirtualBox can also synchronize the time between the host and the guest, to do this, start/enable the .

Now, you should have a working Arch Linux guest. Note that features like clipboard sharing are disabled by default in VirtualBox, and you will need to turn them on in the per-VM settings if you actually want to use them (e.g. Settings > General > Advanced > Shared Clipboard).

## Auto-resize Guest Display
This option will automatically change the resolution of the Arch guest, whenever the window of the virtual machine is resized. This option is enabled by default, and in graphical interface is located at View > Auto-resize Guest Display. When using KDE Plasma, on GUI login screen (Session) select Plasma (X11) instead of the default session Plasma (Wayland), which does not work with auto-resize.

## Hardware acceleration
Hardware acceleration can be activated in the VirtualBox options. The GDM display manager 3.16+ is known to break hardware acceleration support. So if you get issues with hardware acceleration, try out another display manager (lightdm seems to work fine). [https://bbs.archlinux.org/viewtopic.php?id=200025 If the hardware acceleration does not work as expected, try changing the Graphics Controller option found under the Screen tab in the Display options of the settings GUI. It seems that depending on the host GPU type, not all emulated controllers work equally well.

## Enable shared folders
Shared folders are managed on the host, in the settings of the Virtual Machine accessible via the GUI of VirtualBox, in the Shared Folders tab. There, Folder Path, the name of the mount point identified by Folder name, and options like Read-only, Auto-mount and Make permanent can be specified. These parameters can be defined with the  command line utility. See [https://www.virtualbox.org/manual/ch04.html#sharedfolders there for more details.

No matter which method you will use to mount your folder, all methods require some steps first.

To avoid this issue , make sure the  kernel module is properly loaded. It should be, since we enabled all guest kernel modules previously.

Two additional steps are needed in order for the mount point to be accessible from users other than root:

* the  package created a group  (done in a previous step);
* your user must be in  user group.

## Manual mounting
Use the following command to mount your folder in your Arch Linux guest:

 # mount -t vboxsf -o gid=vboxsf shared_folder_name mount_point_on_guest_system

where  is the Folder name assigned by the hypervisor when the share was created.

If the user is not in the vboxsf group, to give them access to our mountpoint we can specify the  options  and  with the corresponding values of the user. These values can obtained from the  command run against this user. For example:

 # mount -t vboxsf -o uid=1000,gid=1000 home /mnt

## Automounting
In order for the automounting feature to work you must have checked the auto-mount checkbox in the GUI or used the optional  argument with the command .

The shared folder should now appear as . If users cannot access the shared folders, check that  has permissions  or is owned by the  group if using permissions . This is currently not the default if the  directory is created by .

You can use symlinks if you want to have a more convenient access and avoid to browse in that directory, e.g.:

 $ ln -s /media/sf_shared_folder_name ~/my_documents

## Mount at boot
You can mount your directory with fstab. However, to prevent startup problems with systemd,  should be added to . This way, the shared folders are mounted only when those mount points are accessed and not during startup. This can avoid some problems, especially if the guest additions are not loaded yet when systemd reads fstab and mounts the partitions.

 sharedFolderName  /path/to/mntPtOnGuestMachine  vboxsf  uid=user,gid=group,rw,dmode=700,fmode=600,noauto,x-systemd.automount

* : the value from the VirtualMachine's Settings > SharedFolders > Edit > FolderName menu. This value can be different from the name of the real folder name on the host machine. To see the VirtualMachine's Settings go to the host OS VirtualBox application, select the corresponding virtual machine and click on Settings.
* : if not existing, this directory should be created manually (for example by using mkdir).
* / are directory/file permissions for directories/files inside .

As of 2012-08-02, mount.vboxsf does not support the  option:

 desktop  /media/desktop  vboxsf  uid=user,gid=group,rw,dmode=700,fmode=600,nofail  0  0

## Troubleshooting
## Access serial port from guest
See Working with the serial console#Connect using a terminal emulator program.

## TTY text too small during installation
From the host, VirtualBox Manager, set the Display Scale-factor to 2.00 or 3.00.

## Guest freezes after starting Xorg
Faulty or missing drivers may cause the guest to freeze after starting Xorg, see for example and [https://bbs.archlinux.org/viewtopic.php?id=156079. Try disabling 3D acceleration in Settings > Display, and check if all Xorg drivers are installed.

## Fullscreen mode shows blank screen
On some window managers (i3, awesome), VirtualBox has issues with fullscreen mode properly due to the overlay bar. To work around this issue, disable Show in Full-screen/Seamless option in Guest Settings > User Interface > Mini ToolBar.  See the upstream bug report for more information.

If the guest's screen goes black above a certain size (e.g. above 2048 pixels wide), increasing the Settings > Display > Screen > Video Memory can help.

## Linux guests have slow/distorted audio
The AC97 audio driver within the Linux kernel occasionally guesses the wrong clock settings when running inside VirtualBox, leading to audio that is either too slow or too fast. To fix this, create a file in  with the following line:

 options snd_intel8x0 ac97_clock=48000

## Linux guests have slow/laggy audio
In some cases, audio can have laggy performance (for example lag behind video when streaming video online). A possible workaround can be to use the Intel HD Audio controller in VirtualBox and disable its power saving by adding the following line in a file in  in the guest OS:

 options snd_hda_intel power_save=0 power_save_controller=N

## Arch: pacstrap script fails
If you used pacstrap to also #Install the Guest Additions before performing a first boot into the new guest, you will need to  as root before using pacstrap again; a failure to do this will render it unusable.

## Windows host: VERR_ACCESS_DENIED
To access the raw VMDK image on a Windows host, run the VirtualBox GUI as administrator.

## No hardware 3D acceleration in Arch Linux guest
 package as of version 5.2.16-2 does not contain the file . This causes the Arch Linux guest to not have proper 3D acceleration. See .

To deal with this problem, apply the patch set at . Some fix to the patch set is required to make it work for version 5.2.16-2.

## Plasma resets guest's resolution to 800×600
See KDE#Cannot change screen resolution when running in a virtual machine.

## Black screen with Plasma-X11 minimal install
If you used  minimal install instead of  (which includes Wayland support), then probably you will have black screen with cursor after starting Plasma-X11 session.

To fix this, resize the VirtualBox window several times, then set resolution manually in VirtualBox window itself by: View > Virtual Screen 1 > Resize to 1024x768 (or other resolution you like).

Then install .

Open in KDE launcher System Settings > Startup and Shutdown > Background Services, stop and unselect KScreen2 and save settings. Issue should go away forever.
