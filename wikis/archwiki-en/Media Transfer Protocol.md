# Media Transfer Protocol

The Media Transfer Protocol (MTP) can be used to transfer media files to and from many mobile phones (all Windows Phone 7/8/10 devices, most newer Android devices) and media players (e.g. Creative Zen).

## Connecting
To connect your computer to a device via MTP:

* the device needs to be connected to your computer via USB
* MTP needs to be enabled on the device
* the device's screen needs to be unlocked (for security reasons)

## FUSE filesystems
The following programs let you access MTP devices via a FUSE filesystem.

For the FUSE-based file systems, you might need to create the mount-point directory first. The directory  is used in the examples below.

FUSE mounts can generally be unmounted using .

## Android File Transfer
Mount your device on :

 $ aft-mtp-mount ~/mnt

If you want album art to be displayed, it must be named  and placed first in the destination folder. Then copy other files. Also, note that fuse could be 7-8 times slower than ui/cli file transfer.

If you want to interact with it via the command line interface, run the command:

 $ aft-mtp-cli

Type help in order to list all the commands available, exit to quit.

If you want to interact with it via the graphical user interface, start the android-file-transfer application, choose a destination folder and click any button on the toolbar. Available options are: Upload Album, Upload Directory and Upload Files. The latter two are self-explanatory. Upload album searches the source directory for album covers, and sets the best available cover.

## MTPfs
First edit your  and uncomment the following line:

 user_allow_other

Mount your device on :

 $ mtpfs -o allow_other ~/mnt

## jmtpfs
Mount device on :

 $ jmtpfs ~/mnt

Make this cohere to the rest of Linux (use regular mount/umount commands) by doing two steps

 $# ln -s
 $  ln -s /sbin/jmtpfs                        /sbin/mount.jmtpfs

add this line to ;

  #jmtpfs         fuse nodev,allow_other,                             0    0
   jmtpfs /home/sam/run/motog fuse nodev,allow_other,rw,user,noauto,noatime,uid=1000,gid=1000    0    0

Now mount the device and see if the options "took"

  $ mount /home/sam/run/motog
  Device 0 (VID=22b8 and PID=2e82) is a Motorola Moto G (ID2).
  Android device detected, assigning default bug flags
  $ mount
   ...
   jmtpfs on /home/sam/run/motog type fuse.jmtpfs (rw,nosuid,nodev,noexec,noatime,user_id=1000,group_id=1000,allow_other,user=sam)

## SIMPLE-MTPFS
Run  to list detected devices.

To mount the first device in the list to , run .

## go-mtpfs
Install , which will allow you to edit  and apply to your  and , which you can see after running mtp-detect. To the end of the line, add your user .

Mount device on :

 $ go-mtpfs ~/mnt

## libmtp
libmtp is a library MTP implementation, which also comes with some example command-line tools (which you can list using ).

Install the  package.

Run  to detect your device.

If an error is returned, make sure your user is in the  user group.

 is meant to be used as a library, not by an end user. Other then the  command, the other commands-line tools are likely to be unnecessarily error prone for daily work. The upstream author refers to them as examples. As of Jan2025, see lines 115-138 of the README file. For a more concrete example see the old, but demonstrating, suggestion for Copying file from MTP device using libmtp (over USB). It is recommended to use a front end.

## Frontends
## Media players
You can also use your MTP device in music players such as Amarok. To achieve this, you might have to edit  (the MTP device used in the following example is a Galaxy Nexus).
Run:

 $ lsusb

Search for your device. It should be something like that:

 Bus 003 Device 011: ID 04e8:6860 Samsung Electronics Co., Ltd GT-I9100 Phone S II, GT-P7500 Tab 10.1

And entry to  will be this:

 SUBSYSTEM=="usb", ATTR{idVendor}=="04e8", ATTR{idProduct}=="6860", MODE="0666", OWNER="Also reload udev rules:

 # udevadm control --reload

## File manager integration
To view the contents of your Android device's storage via MTP in your file manager, install the corresponding plugin:

* For file managers that use GVFS (GNOME Files), install  for MTP or  for PTP support.
* For file managers that use KIO (KDE's Dolphin), MTP support is included in  (dependency of dolphin).

After installing the required package, the device should show up in the file manager automatically and be accessible via an URL, for example .

## gvfs-mtp
The  is available in the official repositories.

With  you can get information about your device where Bus and Device numbers can be used with  and device ID for creating of a udev rule.

 Bus 002 Device 018: ID 04b7:88a9 Compal Electronics, Inc.

To see detected device with enabled MTP

Use gio mount:

Use lsusb:

To mount all available connected MTP devices use inline script

 gio mount -li | awk -F= '{if(index($2,"mtp") == 1)system("gio mount "$2)}'

To mount or unmount from a command with gvfs-mtp use Bus and Device numbers, e.g. to mount  and to unmount . The mounted device will be available in a directory that begins with mtp:host= and is located under /run/user/$UID/gvfs/.

To disable automount of MTP devices with gvfs you will need to change value true to false for variable AutoMount that is located in .

If your device is not showing up in the file manager then #libmtp is missing a native support and is not currently available in the list of the [https://sourceforge.net/p/libmtp/code/ci/HEAD/tree/src/music-players.h supported devices. If you will try to mount by using command line you may also get an error

The workaround to make it shown in the file manager is to write a udev rule for the device but it is no guaranty that you will be able to mount it by using MTP connection.

Use ID number that is represented by the pattern vendorId:productID, e.g. 04b7:88a9, and make a udev rule by creating a configuration file

{{hc|/etc/udev/rules.d/51-android.rules|
SUBSYSTEM=="usb", ATTR{idVendor}=="04b7", ATTR{idProduct}=="88a9", MODE="0660", GROUP="uucp", ENV{ID_MTP_DEVICE}="1", SYMLINK+="libmtp"
}}
Reload the udev rules.

 # udevadm control --reload

The file managers with support for gvfs will be able to show MTP devices and mount them if supported by #libmtp but if has no support and cannot be opened then change settings in the phone to PTP and install  for having access at least to the photos, command line mounting of PTP is a little similar to mounting of the MTP devices: .

## Troubleshooting
## libmtp (gvfs-mtp): filemanager (nautilus, pcmanfm, vifm and etc) hangs on accessing DCIM/Camera of Android device
Symptoms: everything works fine till moment of entering DCIM/Camera directory. In this case filemanager freezes and even in command line you cannot run even  on that directory.

Possible and very probable reason is the bug of libmtp.

It seems that it is caused by file with name like . Samsung phones for example like to create files with such names.

There are several tickets (one, two and etc) and questions (one, two) about it.

So possible workaround is to use different mtp option from #FUSE filesystems like go-mtpfs for such directories or somehow change file naming policy of your phone camera (or switch to another camera app like Open Camera for example).

## jmtpfs: Input/output error upon first access
Symptoms: jmtpfs successfully mounts, but as soon as one attempts to access files on the device (e.g. via ), an error is reported:

  cannot access : Input/output error

This appears to be a security feature: MTP does not work when the phone is locked by the lockscreen.  Unlock the phone and it should work again as long as the cord remains connected.

## kio-mtp: cannot use "Open with File Manager" action
If you are not able to use the action "Open with File Manager", you may work around this problem by editing the file .

Change the line  to .

## kio-mtp being called simultaneously by different services
Parallel usage of mtpfs and kio-mtp, as well as conflicting services using kio-mtp -music players included- should be avoided, as mentioned in this forum.

Amarok's plugin for MTP services, for example, might be preventing Dolphin (plasma) to access different phone model's files. Switching it off was a solution for at least one user.
