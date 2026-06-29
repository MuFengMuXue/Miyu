# Install Arch Linux on WSL

Arch Linux provides an official WSL (Windows Subsystem for Linux) image as part of the archlinux-wsl project.

Images are built and released monthly and aim to provide the simplest but complete system to offer an outright Arch Linux experience with WSL.

## Installation
## Install WSL
Enable virtualization in the UEFI Setup, then install the Windows Subsystem for Linux from the Microsoft Store.

## Update WSL
To update to the latest stable version of WSL and WSLg, run the following command in an elevated Windows command-line shell:

 > wsl --update

To update to the latest pre-release version, run instead:

 > wsl --update --pre-release

## Install Arch Linux in WSL
From a Windows system with WSL 2 installed, use one of the following installation methods.

## Automated installation
Run the following command in a Windows shell:

 > wsl --install archlinux

You can then run Arch Linux in WSL via the  application from the Start menu, or by running  in a Windows shell.

## Manual installation
Download the latest Arch Linux .wsl image and double-click on it to start the installation or run the following command in a Windows shell:

 > wsl --install --from-file WSL_image

For instance:

 > wsl --install --from-file C:\Users\Username\Downloads\archlinux-2025.04.01.121271.wsl

You can then run Arch Linux in WSL via the  application from the Start menu, or by running  in a Windows shell.

## Tips and tricks
## Set default user
To set a different default user than , first ensure the user has been created, then append the following to the  file:

 default=username

Make sure to give your  user a password before you close your session. If you find yourself 'locked out', invoke

 > wsl -u root

from a CMD window in the windows host.

The change will apply at the next session. To terminate your current session, run the following command in a Windows shell:

 > wsl --terminate archlinux

If you are using WSL 2.4.10 or later, you can set the default user for your distribution with:

 > wsl --manage archlinux --set-default-user username

This change will take effect the next time you launch the distribution.

## Open URLs in the WSL hosts browser
In order to open links in your Windows host browser install the  package. This is important for various commands like  and widely used in the authentication flows of the various cloud provider CLI tools (i.e. ).

## Run graphical applications with WSLg
[https://github.com/microsoft/wslg WSLg (Windows Subsystem for Linux GUI) is a project that aims to enable running Linux applications with audio (PulseAudio) and graphical (X11 and Wayland) support within WSL.

WSLg is enabled by default. You can disable it by setting  to  in the WSL configuration file.

## Hardware accelerated rendering
To enable GPU video accelerated rendering in WSL, install the following packages:

*  - Contains the  Gallium driver for OpenGL
*  - Contains the experimental  (also known as ) Vulkan driver

You will need to install the  (and  if you also want to run 32-bit applications) as well.

If OpenGL falls back to the llvmpipe software renderer for Intel GPUs, you need to create a symlink for libedit:

 # ln -s /usr/lib/libedit.so /usr/lib/libedit.so.2

See https://github.com/microsoft/wslg/issues/996 and Gentoo:Gentoo in WSL#OpenGL falling back to llvmpipe software renderer on Intel GPUs for more information.

## Avoid unnecessary GTK4 dependencies
 has a dependency on , which in turn pulls in several dependencies (such as , , , and ) that may be undesirable inside a WSL environment, resulting in unnecessary installations inside the Arch guest.

To prevent this, install  from the AUR. It is a dummy package that satisfies the  dependency without installing any of those packages, keeping your WSL environment lean.

## WSL interoperability
WSL features interoperability between the Windows and WSL. This allows you to run Windows binaries from within WSL.

It is enabled by default. You can disable it by setting  to  in the  file. Various tools have been created to allow you to utilise Windows services and features from within WSL.

## Bridge the ssh-agent service from Windows
[https://github.com/mame/wsl2-ssh-agent wsl2-ssh-agent is a tool that allows you to use the Windows SSH agent from within WSL.

This is especially useful if you utilise  SSH keys requiring the use of physical security keys or even Windows Hello.

Install  and add the following to your :

 eval "$(/usr/sbin/wsl2-ssh-agent)"

Restart your shell and the  environment variable should be configured correctly.

## PAM authentication with Windows Hello
WSL-Hello-Sudo is a PAM plugin that allows you to authenticate your user via Windows Hello.

Install  and run . The installer will copy a Windows executable to a directory of your choosing and store a certificate used to authenticate beside it.

Add  to any  configuration files you wish to authenticate with Windows Hello for. For example, with sudo:

## Passing devices to WSL
WSL 2 is a Hyper-V virtual machine. This allows for passthrough for physical devices from the host (Windows) to the guest (WSL 2).

## Mount a disk
WSL 2 supports attaching and mounting disks available to Windows.

To do so, first idenitfy the  for the given disk with the following PowerShell command:

 > GET-CimInstance -query "SELECT * from Win32_DiskDrive"

Once you have found the disk you would like to pass, run the following on Windows (with Administrator privileges):

 > wsl --mount DeviceID --bare

Once attached, you should be able to see the device with lsblk.

To unmount a disk, run:

 > wsl --unmount DeviceID

For more information, see https://learn.microsoft.com/en-us/windows/wsl/wsl2-mount-disk.

## Connect USB devices
usbipd-win is a project which allows for sharing locally connected USB devices to other machines, including WSL 2.

You first need to install the software on Windows. You can either run the installer (.msi) from the latest release or use use the Windows Package Manager:

 > winget install usbipd

Once installed, identify the USB devices available using and take note of the bus ID by running the following on Windows:

 > usbipd list

Prepare the USB device you have selected by running (this requires Administrator privileges):

 > usbipd bind --busid busid

Then, attach the USB device to WSL 2 using:

 > usbipd attach --wsl --busid busid

Once attached, you should be able to see the device with .

To detatch a USB device, run:

 > usbipd detach --busid busid

For more information, see https://learn.microsoft.com/en-us/windows/wsl/connect-usb.

## Adjust locale
By default, WSL will try to set your locale to match windows. If you want to override this, run:
 ln -sf /etc/locale.conf /etc/default/locale

Then set your locale the same way you would in any other installation.

## Troubleshooting
## Failure when running Docker containers
One might face the following error when running a Docker container from WSL:

 Error response from daemon: path / is mounted on / but it is not a shared or slave mount
 Error: failed to start containers

It is also possible that commands like  simply hang forever without producing any output.

This is because Docker expects the root () directory to be mounted with rshared propagation.

To do so, run:

 # mount --make-rshared /

To make the change persistent, you can create a systemd service that runs this command early in the boot:

Then start/enable .

## Docker takes longer to initialize
If you start your WSL Session using  or after start/enable  and executing  or any other docker command, it might take a very long time for docker to initialize.

That's because  wants to start  and that fails.

So disable  fixes that.

## Container cannot set caps
Running rootless podman (or docker) may give errors like:

 ERROrunning `/usr/sbin/newuidmap 410 0 1000 1 1 100000 65536`: newuidmap: Could not set caps
 Error: cannot set up namespace using "/usr/sbin/newuidmap": should have setuid or have filecaps setuid: exit status 1

or:

 WARN[0000 "/" is not a shared mount, this could cause issues or missing mounts with rootless containers

The easiest fix is to just reinstall .

## User session errors and early crashes
One may face user session related errors at WSL distribution startup or shutdown, with messages like:

 Failed to start the systemd user session for username. See journalctl for more details.

This might lead to an "incomplete" user session being started (e.g.  reporting the user as "not logged in" and the  directory not being populated, resulting in eventual errors with some tools like rootless ).

In specific cases some people may also suffer from early crashes where the WSL window would unexpectedly close after a few seconds (or after a few commands being executed), then resulting in the above user session related errors when being restarted post-crash.

While the actual cause of the above symptoms is currently unknown, enabling session lingering seems to help:

 # loginctl enable-linger username
