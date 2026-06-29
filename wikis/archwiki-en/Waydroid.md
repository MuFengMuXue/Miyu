# Waydroid

Waydroid is a container-based approach to boot a full Android system on a regular Linux system.

## Prerequisites
## CPU requirements
The requirements depend on the CPU architecture. You can check this table for more information.

You can check if you have the required CPU instructions with .

## GPU requirements
Waydroid currently works best with Intel GPUs. They should work out of the box.

All AMD GPUs have been supported; if Waydroid does not work you might also want to try to build a new Waydroid image (which works for Radeon 680M), or try the NVIDIA instructions below.

NVIDIA GPUs do not work currently, but there are 2 workarounds.

# Switch to integrated graphics card if possible
# Use software rendering (see #Software rendering)

## Wayland session manager
Waydroid only works in a Wayland session manager, so make sure you are in a Wayland session.

Note that even if you are in X11, many Wayland session managers support nested session (so you can run it inside your X11 session), the simplest example is .

## Kernel modules
You need to run a kernel which comes with the  module. It is included in the , and  kernels, but if you use a different kernel you may need to add it via DKMS or recompiling.

## DKMS modules
The binder's DKMS module have to be used when the current kernel does not provide .

Install  and load the kernel module  with module options  (see bug report).

 # modprobe binder-linux devices=binder,hwbinder,vndbinder

Optionally, you can setup  to be loaded at boot by creating configuration files in  and  (See Kernel module for more information).

You will also need to use the Kernel parameter  to work around oops on kernels 5.18+. See Segmentation fault when mounting /dev/binderfs

## Building a kernel
Alternatively, you can recompile the  kernel — or other kernel packages (>=5.7) — with the necessary options. Also see Kernel#Compilation.

When building a minimal kernel, keep the following requirements in mind:

* IPv6 support. Without IPv6 networking built into your kernel, there will be no IPv4 connectivity in Waydroid.
* Netlink sockets ().
* PSI ().
* Loop block devices () - the  module must be loaded before starting Waydroid.

When setting compilation options, you have 2 options available; binder and binderfs. Instructions for both are provided below.

## Using binder
The modules can either be compiled into the kernel (), into modules (), or not at all (). Also, not all combinations in the configuration are possible, and some options will require other options.

The configuration options below will compile binder as a module, while the last option specifies that there will be three devices created in the  directory, when the binder module is loaded.

When building a kernel from the AUR, one can update the configuration with the following steps:

# run , which will download the sources, verify and extract them and run the  function.
# edit the  file (with the dot in the filename), which is located at the base of the kernel directory.
# at the end of the  function was probably a command which regenerates the makefiles with information from the configuration, possibly . Move that to the  function, or execute it yourself.
# run , which will continue from the place where  stopped.

## Using binderfs
The binder kernel module has been known to cause issues for several users. To address these issues, binderfs was created. One has to choose between the old and the new way when compiling the kernel. With the options below, one will use binderfs instead.

With the kernel sources comes also a simple script to set configuration options. It will not do dependency checks, just like when editing the configuration by hand. When being in the same directory where the  file lies, one can execute the following commands:

When building a kernel from the AUR, it is enough to insert these lines at the right place in the PKGBUILD, usually in .

## Setup binder devices
Make sure you have the latest version of Waydroid package, and Waydroid will automatically take care of this.

## Installation
Install the  package.

Optionally, install  or  to provide the needed Android image through AUR. It is however recommended to let Waydroid itself handle downloading the images.

Afterwards init Waydroid, this will automatically download the latest Android image if it is not yet available.

 # waydroid init

To init with GApps support:

 # waydroid init -s GAPPS

Next start/enable the .

Waydroid should now work.

## Usage
Make sure that  is started then run:

 $ waydroid session start

The Waydroid session is now active, the following are command examples to interact with it:

Launch a GUI:

 $ waydroid show-full-ui

Launch a shell:

 # waydroid shell

Install an application:

 $ waydroid app install $path_to_apk

Get the application list:

 $ waydroid app list

Run an application (Note, $package_name referes to the `packageName` attribute as shown by the list command and not to the literal name of the package as shown in the `Name` attribute):

 $ waydroid app launch $package_name

## Network
The network should work out of the box, if it is not, you might need to make sure packet forwarding is enabled in the kernel and allow the following rules through your firewall before running Waydroid session start.

Taking  as an example:

* DNS traffic needs to be allowed:
**
**
* Packet forwarding needs to be allowed:
**

For , you can use those commands:

* DNS:
**
**
* Packet forwarding:
**
* Add the waydroid interface to a trusted:
**

## Tips and tricks
## Enable Window integration with Desktop Window Manager
waydroid by default always runs in fullscreen.

If you want waydroid to integrate with your Desktop Environments Window Manager:

start a waydroid session with:
 $ waydroid session start

set the required property:
 $ waydroid prop set persist.waydroid.multi_windows true

restart the session:
 $ waydroid session stop
 $ waydroid session start

now apps should start in their own desktop windows.

more in the official Docs

## Software rendering
Make sure that you have already run:

 # waydroid init

(see #Installation section for more information)

Then, add the following:

Then run

 # waydroid upgrade --offline

to apply configurations to actual props.

Finally, run  restart the .

## Setting viewport dimensions
To set the dimensions of the waydroid window use the following commands with the dimensions adjusted to your liking:

 $ waydroid prop set persist.waydroid.width 576
 $ waydroid prop set persist.waydroid.height 1024

Then restart the .

## USB Controller Device
To enable connection with USB controller devices such as gamepads run these commands while the waydroid session is running:
 $ waydroid prop set persist.waydroid.udev true
 $ waydroid prop set persist.waydroid.uevent true
After running these commands restart the waydroid session.

## Troubleshooting
If you run into issues, take a look at the official Issue Tracker: Waydroid issue tracker.

## General tips
Waydroid is in rapid development so if you face issues, here is a good list of steps to do first:

# Make sure your Waydroid package is up to date.
# Make sure you have the latest Waydroid image by running
# Reset Waydroid: stop the , run  and start the service again.
# You may also want to do little cleanup, run

::

## ARM apps incompatible
Use casualsnek's  (to install a translation layer.

Due to optimizations in the translation layers, It is recommended to use libndk on AMD CPUs and libhoudini on Intel CPUs. However some apps will work on one translation layer and not another. so you may need to try both if a game does not work or gets bad performance.

Install libndk arm translation:

 # waydroid-extras install libndk

Install libhoudini arm translation:

 # waydroid-extras install libhoudini

## Rotated apps are unusable
See [https://github.com/waydroid/waydroid/issues/70 Issue 70.

Click F11 to switch the current app to windowed mode.

## Failed to start Clipboard manager service
Install  and its dependency for your graphical session ( for X11 or  for Wayland).

## Sometimes the physical keyboard does not work
Press the left  key.

## dnsmasq: failed to open pidfile /run/waydroid-lxc/dnsmasq.pid: Permission denied
An AppArmor rule is likely not set. Add the following rule:

{{hc|/etc/apparmor.d/usr.sbin.dnsmasq|
@{run}/waydroid-lxc/ r,
@{run}/waydroid-lxc/* rw,
}}

## Commands inside Waydroid shell outputs inaccessible or not found
On Arch based distributions there is a "bug" that may appear while working with lxc-attach that may cause this issue with commands inside  like  or .

A possible workaround for this would be replace the  command with:

 # lxc-attach -P /var/lib/waydroid/lxc/ -n waydroid --clear-env

## WARNING: Service manager /dev/binder has died
See Issue 136.

You should enable PSI.

Add  to the kernel command line.

If enabling PSI does not fix this error, it is likely due to having ia32 emulation disabled. Try the following to enable the ia32 vdso:

Note that the Liquorix kernel will never work with Waydroid, as it uses certain schedulers that are incompatible with PSI.

## Graphical Corruption on multi-gpu systems
Currently Waydroid needs to run on the same GPU the host compositor is running on. The two ways of fixing this is to either edit  to be the correct GPU or to change the GPU the compositor runs on.

A convenience script to achieve this can be found at the following address: https://raw.githubusercontent.com/Quackdoc/waydroid-scripts/refs/heads/main/waydroid-choose-gpu.sh

## No internet connection
## Docker/iptables forwarding issue
When using Docker by default  is configured with  ( see https://github.com/docker/for-linux/issues/103 for more information ), which needs to be changed to  as described as well in the official Waydroid documentation: https://docs.waydro.id/debugging/networking-issues

In order to fix the internet connection for other LXC containers in the system ( such as Waydroid ) you can disable this behavior in your  file, by adding the following property ( as described in https://github.com/docker/for-linux/issues/103#issuecomment-3680138560 ):

{{hc|/etc/docker/daemon.json|{
    "ip-forward-no-drop": true
}
}}

Once added remember to restart  and .
## IPv6 needs to be enabled for Waydroid to work
Make sure IPv6 is enabled on your system even if you are not using it, otherwise Waydroid won't have Internet access. https://bbs.archlinux.org/viewtopic.php?id=301559

## This device isn't Play Protect certified
See: https://docs.waydro.id/faq/google-play-certification

If you get this error you need to enter waydroid shell and retrieve the android id:

 # waydroid shell
 # ANDROID_RUNTIME_ROOT=/apex/com.android.runtime ANDROID_DATA=/data ANDROID_TZDATA_ROOT=/apex/com.android.tzdata ANDROID_I18N_ROOT=/apex/com.android.i18n sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"

Afterwards enter the id into this site: https://www.google.com/android/uncertified

Wait a few minutes and restart waydroid.

## Waydroid hangs after a while
This is likely due to the audio server dying, see Issue 576 and Issue 829 for details.

A workaround is to run:

 # sysctl -w kernel.pid_max=65535

You can make it permanent by creating a  file in  and adding  to it.

## Application need unroot device
According to Issue 1060, add following can bypass the root detection:

then use
 waydroid upgrade --offline
to apply the configuration.

## Waydroid "Phone is Starting" and boot animation loop on a ZFS rootfs
Make sure the  property of the zfs dataset housing {{ic|${HOME}/.local/share/waydroid}} is set to . This can be set any time with  to make waydroid work on ZFS. The default value on Linux is  which can lead to this scenario.
