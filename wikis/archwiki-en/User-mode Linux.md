# User-mode Linux

User-mode-Linux (UML) is a method to run Linux inside Linux as a normal process. Please check for in-depth information what UML is and how it works.

## Why use UML?
Running UML is a safe way to run multiple instances of (Arch-)Linux at the same time. The single processes are separated from each other, which makes it secure to run, for example, a testing instance and a production instance on the same machine. If something goes wrong inside the testing instance, it does not interfere with the host Linux or the productive instance.

## HOWTO
There are three methods:

* Use hostfs with vde2 network (all UMLs use same file system)
* Use rootfs with tap network (require build image)
* Use [https://www.marionnet.org/ Marionnet

## Setup by hostfs + vde2
Hostfs means use the host's file system in read-only mode.

## Required packages
*
* Utility packages:

## Launch script
* download https://pastebin.com/qDE0D7Lk script as 2vm.bash
* use normal user to launch 2vm.bash (there are two VMs named as 'C1' & 'C2')
* modify the 2vm.bash to fit your requirements

## Setup by rootfs + tap
## Required packages
*
* Utility packages:

## Build rootfs image
1.) First you have to create a single, big file into which you will install Arch Linux. This command creates a single 1 GiB file, only containing zeros, which should be enough for a basic Arch Linux installation.
 dd if=/dev/zero of=rootfs bs=1M count=1024
or
 fallocate -l 1GiB ./rootfs

2.) After the build process you have to format the root file system image:
 mke2fs -F rootfs

3.) After formatting the file, you have to mount it. Executing the following command as root does the job (you have also to load the  module with ):
 mount -o loop rootfs /mnt

4.) Now the installation of the basic system may start:
 mkdir -p /mnt/var/lib/pacman
 pacman -Sy base -r /mnt
 cd /mnt/dev
 mknod --mode=660 ubd0 b 98 0
 chown root:disk ubd0

5.) Before the system can be booted with user-mode-Linux, some files inside the Arch basic system have to be customised. Add this line to :
 /dev/ubd0 / ext2 defaults 0 0

6.) Now unmount the file system.

 umount /mnt

7.) Next step is to set up networking. Therefore, you create a so called tun device (Please visit the UML how-to for further information about tun/tap), and give it an IP address. The following lines load the necessary  module, create a tun/tap device that is readable by the  group, and sets it up with the given IP address. For security, you should consider creating a certain UML group with read permissions for the network device.
 modprobe tun
 ip tuntap add tap0 mode tap group users
 chown root:users /dev/net/tun
 ip addr add 192.168.0.100/24 dev tap0

8.) Now you can boot the image.

To use the network, you have to announce the proper device to the UML kernel. (Mind that the user running the UML command needs enough rights to access the tun device!)
 vmlinux ubd0=rootfs eth0=tuntap,,,192.168.0.100

The options to eth0 () mean:
 eth0=transportmode,tuntap device,MAC address,hostip

Where transportmode is 'tuntap' in this example; the tuntap device is the device configured above; MAC address is the MAC address that the eth0 device in the UML system should get; hostip is the ip adress that the tuntap device in the host system gets. This should be an unused ip address of your hosts local network. The device and MAC address are optional and "guessed" if not supplied.

Example:
 eth0=tuntap,tap0,3f:2a:bb:00:00:00,192.168.0.100

Other important options are  for specifying the amount of RAM the guest system should be able to use (defaults to only 16MB);  to configure the virtual terminals and ubdb, ubdc, … for mounting additional filesystems.

Headless example:
  vmlinux ubd0=rootfs eth0=tuntap,,,192.168.0.100 mem=128M con=pty

9) If you are not presented with a login prompt but see something like , open the virtual console in another terminal with screen and press enter:
 screen /dev/pts/4

10) In the UML system you can configure the network manually:

 ip link set dev eth0 up
 ip addr add 192.168.0.200/24  broadcast + dev eth0
 ip route add default via 192.168.0.100
 echo 'nameserver 1.1.1.1' > /etc/resolv.conf

Gateway it the address you specified in 8; the local address should be another unused address from your network.

## Marionnet
Marionnet is a free application for virtual networks. For use, you must install , and see https://bugs.launchpad.net/marionnet/+bug/1580349.

## Usage
## Management console
With {[ic|uml_mconsole}} you can manage running UML systems:
 uml_mconsole socket-name

You can see the socket-names – also called UMID – of your UML systems in the folder :
 $ ls -l ~/.uml/
 drwxr-xr-x 1 michi users 16 11. Apr 19:52 I0KaOj
 drwxr-xr-x 1 michi users 16 11. Apr 19:14 LrPv03
 drwxr-xr-x 1 michi users 16 11. Apr 19:31 o8X27c

You can also specify it on start with the  option.

With  you can among others reboot/halt the system, add/remove storage devices or send special key combinations (sysrq, Ctrl-alt-del) to the system.
