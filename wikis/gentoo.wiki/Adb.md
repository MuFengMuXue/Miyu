** Note**\
This wiki article has been created for **non-rooted** devices. For **rooted** devices please create another article or add a rooted section at bottom.

**ADB** stands for Android Debug Bridge^[\[1\]](#cite_note-1)^, and it is a part of the Android Software Development Kit (SDK)^[\[2\]](#cite_note-2)^. It can be installed with [[[dev-util/android-tools]](https://packages.gentoo.org/packages/dev-util/android-tools)[]].

## Contents

-   [[1] [ADB Internals]](#ADB_Internals)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Install Android SDK Platform-Tools]](#Install_Android_SDK_Platform-Tools)
-   [[3] [Set up a device for development]](#Set_up_a_device_for_development)
    -   [[3.1] [USB Communication]](#USB_Communication)
    -   [[3.2] [Pair with a device for secure TCP/IP communication]](#Pair_with_a_device_for_secure_TCP.2FIP_communication)
    -   [[3.3] [Connect to a device via TCP/IP]](#Connect_to_a_device_via_TCP.2FIP)
    -   [[3.4] [General commands]](#General_commands)
-   [[4] [Reboot]](#Reboot)
-   [[5] [File transfers]](#File_transfers)
-   [[6] [App installation]](#App_installation)
-   [[7] [Backup]](#Backup)
    -   [[7.1] [Create full backup]](#Create_full_backup)
    -   [[7.2] [Create shared backup]](#Create_shared_backup)
    -   [[7.3] [Restore a backup]](#Restore_a_backup)
    -   [[7.4] [Extract a backup (.ab extension) on PC]](#Extract_a_backup_.28.ab_extension.29_on_PC)
-   [[8] [HTC backup]](#HTC_backup)
-   [[9] [Fastboot]](#Fastboot)
    -   [[9.1] [Booting into fastboot]](#Booting_into_fastboot)
-   [[10] [Troubleshooting]](#Troubleshooting)
-   [[11] [External Sources]](#External_Sources)
-   [[12] [References]](#References)

## [ADB Internals]

As a whole, everything works through the following components:

1\. **ADB server** : This is a background process that runs on the host machine. Its purpose is to sense the USB ports to know when devices are attached/removed, as well as when emulator instances start/stop. It thus maintains a list of \"connected devices\" and assigns a \'state\' to each one of them: OFFLINE, BOOTLOADER, RECOVERY or ONLINE. The ADB server is really one giant multiplexing loop whose purpose is to orchestrate the exchange of data (packets, really) between clients, services and devices.

2\. **ADB daemon (adbd)**: The \'adbd\' program runs as a background process within an Android device or emulated system. Its purpose is to connect to the ADB server (through USB for devices, through TCP for emulators) and provide a few services for clients that run on the host. The ADB server considers that a device is ONLINE when it has successfully connected to the adbd program within it. Otherwise, the device is OFFLINE, meaning that the ADB server detected a new device/emulator, but could not connect to the adbd daemon. The BOOTLOADER and RECOVERY states correspond to alternate states of devices when they are in the bootloader or recovery mode.

3.. **ADB command-line client**: The \'adb\' command-line program is used to run adb commands from a shell or a script. It first tries to locate the ADB server on the host machine, and will start one automatically if none is found. Then, the client sends its service requests to the ADB server. Currently, a single \'adb\' binary is used for both the server and client. this makes distribution and starting the server easier.

3.. **Three components of adb pipeline**: As outlined in the overview, this codebase generates three components (Client, Server (a.k.a Host), and Daemon (a.k.a adbd)). The central part is the Server which runs on the Host computer. On one side the Server exposes a "Smart Socket" to Clients such as adb or DDMLIB. On the other side, the Server continuously monitors for connecting Daemons (as USB devices or TCP emulator). Communication with a device is done with a Transport.

    +----------+              +------------------------+
    |   ADB    +----------+   |      ADB SERVER        |                   +----------+
    |  CLIENT  |          |   |                        |              (USB)|   ADBD   |
    +----------+          |   |                     Transport+-------------+ (DEVICE) |
                          |   |                        |                   +----------+
    +-----------          |   |                        |
    |   ADB    |          v   +                        |                   +----------+
    |  CLIENT  +--------->SmartSocket                  |              (USB)|   ADBD   |
    +----------+          ^   | (TCP/IP)            Transport+-------------+ (DEVICE) |
                          |   |                        |                   +----------+
    +----------+          |   |                        |
    |  DDMLIB  |          |   |                     Transport+--+          +----------+
    |  CLIENT  +----------+   |                        |        |  (TCP/IP)|   ADBD   |
    +----------+              +------------------------+        +----------|(EMULATOR)|

## [Installation]

#### [Install Android SDK Platform-Tools]

Android SDK Platform-Tools is a component for the Android SDK. It includes tools that interface with the Android platform, primarily. Each user that wants to use ADB needs to be in the android group which is provided by [[[dev-util/android-udev-rules]](https://packages.gentoo.org/packages/dev-util/android-udev-rules)[]].

`root `[`#`]`echo "dev-util/android-tools udev" >> /etc/portage/package.use`

`root `[`#`]`emerge --ask dev-util/android-tools`

For the following command replace larry with the username:

`root `[`#`]`usermod -aG android larry `

## [Set up a device for development]

#### [USB Communication]

Enable the USB Debugging option on the Android device under Settings \> Developer options.

For Android 4.2 and later, Developer options is hidden by default; use the following stepsː

1.  On the device, go to Settings \> About \<device\>.
2.  Tap the Build number seven times to make Settings \> Developer options available enable.
3.  Go back to system settings and scroll down to bottom \> Developer Options.
4.  Now hit Enable USB-Debugging.

** Tip**\
You might also want to enable the Stay awake option, to prevent Device from sleeping while plugged into the USB port

#### [][Pair with a device for secure TCP/IP communication]

Since ***Android 11*** it is possible to connect to Wifi-debugging by pairing the device over wifi (access point)

On the android device, open Developer options , and enable Wireless debugging , then click the Pair device with pairing code , it will show the connecting information and pairing code on your android device and you will now be able to pair your device. (select pairing by code since qr-code is for android-studio and qemu emulator by default but there are third-party programs for this via the terminal such as \"npm-wifi\" but it is not default)

** Note**\
Currently it is not possible to set a static port for security reasons so the port will be randomly followed every time you want to pair to the device

`user `[`$`]`adb pair <host:port> `

#### [][Connect to a device via TCP/IP]

** Warning**\
On android versions older than Android 11, you don\'t need an authentication key for adb connect so if you don\'t absolutely have to use usb or wifi debugging instead of over ip/tcp and be sure to execute ***adb disconnect*** when you are done to close the connection to be safe

`user `[`$`]`adb connect 192.168.1.80:5555`

    connected to 192.168.1.80:5555

#### [General commands]

Start ADB daemon

`user `[`$`]`adb start-server`

Enter remote shell command (interactive shell if no command given)

`user `[`$`]`adb shell`

Sometimes it may be necessary to kill adb if the device is not showing up connect. This can occur when adb is running before connecting the device. In this case kill and restart the adb server

`user `[`$`]`adb kill-server`

Kick connection from host side to force reconnect

`user `[`$`]`adb reconnect`

Kick connection from device side to force reconnect

`user `[`$`]`adb reconnect device`

Reset offline/unauthorized devices to force reconnect

`user `[`$`]`adb reconnect offline`

Restart adbd listening on USB

`user `[`$`]`adb usb`

Restart adbd listening on TCP on PORT

** Note**\
Default port is 5555, for a random port :0 should be used

** Note**\
Using this command requires usb cable to be connected between the computer running `adbd`. It is not possible to enable adb over tcpip without a usb connection between the computer running the adb server and the phone being debugged. For debugging purely over a Wifi connection (\"pairing\") see [Pair with a device for secure TCP/IP communication](https://wiki.gentoo.org/wiki/Android/adb#Pair_with_a_device_for_secure_TCP.2FIP_communication "Android/adb").

List devices

`user `[`$`]`adb devices [-l]`

Listen on all network interfaces, not just localhost

`user `[`$`]`adb -a`

Use USB device (error if multiple devices connected)

`user `[`$`]`adb -d`

Use TCP/IP device (error if multiple TCP/IP devices available)

`user `[`$`]`adb -e`

Use device with given serial

** Note**\
Overrides \$ANDROID_SERIAL

`user `[`$`]`adb -s <serial>`

Dump device state

`user `[`$`]`adb get-state`

Print device serial number

`user `[`$`]`adb get-serialno`

Print device path

`user `[`$`]`adb get-devpath print <device-path>`

Attach a detached USB device

`user `[`$`]`adb attach`

Detach from a USB device to allow use by other processes

`user `[`$`]`adb detach`

## [Reboot]

Normal mode

`user `[`$`]`adb reboot`

Recovery mode

`user `[`$`]`adb reboot recovery`

Bootloader mode

`user `[`$`]`adb reboot bootloader`

Fastboot mode

`user `[`$`]`adb reboot fastboot`

FastbootD mode FastbootD is a new mode Android devices could boot to by using ADB Command, via Fastboot Command, and from the Stock Recovery as well for devices using A/B partitions for flashing. The easiest way to keep track of the difference between bootloader/fastboot and fastbootd is to first reboot to the bootloader via adb and then we gonna use fastboot command instead of adb command to fastbootd mode

`user `[`$`]`adb reboot bootloader`

## [File transfers]

Copy local files/directories to device

`user `[`$`]`adb push mypicture.png /storage/on/device`

Copy local directories to device

`user `[`$`]`adb push myfolder /storage/on/device`

Copy local files from directory to device folder

** Note**\
Trailing slash on the directory will transfer files instead of folder

`user `[`$`]`adb push myfolder/ /storage/on/device`

Copy files from device

`user `[`$`]`adb pull /storage/on/device/mypicture.png`

Copy paths from device

`user `[`$`]`adb pull /storage/on/device /home/̩$(whoami)/android-folder/`

Copy all files from device folder [myfolder/] directory name

`user `[`$`]`adb push myfolder/ /storage/on/device`

## [App installation]

Copy custom app (.apk) to the device and install it

`user `[`$`]`adb install com.android.custom_app.apk`

Push multiple APKs to the device for a single package to install

`user `[`$`]`adb install-multiple com.android.custom_app.apk...`

Push one or more packages to the device and install them atomically

`user `[`$`]`adb install-multi-package com.android.custom_app.apk...`

Removes app package from the device

** Note**\
Keep application data and cache directories with \'-k\'

`user `[`$`]`pm uninstall [-k] com.android.custom_app.apk`

## [Backup]

** Warning**\
WARNING: adb backup is deprecated and may be removed in a future release

#### [Create full backup]

`user `[`$`]`adb backup -all -f <filepath>/backup.ab“`

#### [Create shared backup]

`user `[`$`]`adb backup -apk -shared -all -f <filepath>/backup.ab“`

#### [Restore a backup]

`user `[`$`]`adb restore <filepath>/backup.ab`

#### [][Extract a backup (.ab extension) on PC]

`user `[`$`]`( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" ; tail -c +25 backup.ab ) | tar xfvz - `

## [HTC backup]

With a non rooted device, the only things you can backup locally is what the couple device/android will let you do. That is pretty much the same files you can copy with the already mentioned software. With the Android 4.x devices, a nice solution to make such a partial backup is the so-called [\"adb backup\"](https://android.stackexchange.com/questions/28296/full-backup-of-non-rooted-devices/28315#28315).

`user `[`$`]`adb backup [-f <file>] [-apk|-noapk] [-shared|-noshared] [-all] [-system|nosystem] []`

where:

-   -f : the path of the \*.ab file that will be saved on your computer. This file is a compressed file that contains an archive of the data/apks from your device.
-   -apk\|-noapk : indicates if the \*.apk files should be backed up (default is -noapk)
-   -shared\|-noshared: enable/disable backup of the device\'s shared storage / SD card contents (default is -noshared)
-   -all : indicates that you want the entire system backed up. you can use the packages filter to just backup specific packages, or use -all for a full system backup.
-   -system\|-nosystem: indicates if all the system applications and data are included when backing up. (default is -system)
-   \ : this is where you can list specific packages to backup. Use these if you want to back up only specific applications. If using -all, you do not need to specify packages.

To backup the phone into [\~/HTC_backup]

`user `[`$`]`cd ~ `

`user `[`$`]`mkdir HTC_backup `

`user `[`$`]`adb devices `

will start the daemon and show you the devices on the USB.

`user `[`$`]`adb backup -apk -shared -all -system -f ~/HTC_backup/backup<date_of_the_day>.ab`

will backup every thing the device will let you to backup.

`user `[`$`]`adb restore ~/HTC_backup/backup<date_of_the_day>.ab`

will restore the backup into the device.

To stop the daemon:

`user `[`$`]`adb kill-server`

## [Fastboot]

**Fastboot** is a communication protocol used primarily with Android devices. It is implemented in a command-line interface tool of the same name and as a mode of the bootloader of Android devices. It is included with the Android SDK package used primarily to modify the flash filesystem via a USB connection from a host computer. It requires that the device be started in Fastboot mode. If the mode is enabled, it will accept a specific set of commands sent to it via USB using a command line. Fastboot allows to boot from a custom recovery image. Fastboot does not require USB debugging to be enabled on the device. Not all Android devices have fastboot enabled.

Android device manufacturers are allowed to choose if they want to implement fastboot or some other protocol.

### [Booting into fastboot]

You can flash a device when it\'s in the fastboot bootloader mode.

To enter fastboot mode when a device is undergoing a *cold* boot proccess by press \'**vol down\'** + \'**power button\'** in 7000ms, this applies to all android devices regardless model to restart device in any state, for enter fastboot mode keep holding the combination after device is restarted from the key combo and release the keys when device has entering download mode

** Note**\
It is possible to reboot to fastboot via adb or from the device from a terminal application. Doing it directly from the phone should skip adb in the command

`user `[`$`]`adb reboot bootloader`

## [Troubleshooting]

**no permissions (missing udev rules? user is in the plugdev group);** emerge with the [`udev`](https://packages.gentoo.org/useflags/udev) USE flag enabled.

## [External Sources]

-   [Android Developers - Flashing A Devices](https://source.android.com/docs/setup/build/running#flashing-a-device)
-   [Android Developers - Relocking Fastboot](https://source.android.com/docs/setup/build/running#relocking-the-bootloader)
-   [Android Online Tool - Install an Android build in three easy steps](https://flash.android.com/welcome)
-   [Arch Wiki - Android Debug Bridge](https://wiki.archlinux.org/title/Android_Debug_Bridge)
-   [Genymobile/scrcpy - Display and control your Android device](https://github.com/Genymobile/scrcpy)
-   [Open Android Backup - Shell script that makes securely backing up Android devices easy](https://github.com/mrrfv/open-android-backup)

** Note**\
Online flashing tool doesn\'t support flashing Android onto tablets or Chrome OS devices

## [References]

1.  [[[↑](#cite_ref-1)] [[https://developer.android.com/studio/command-line/adb.html](https://developer.android.com/studio/command-line/adb.html)]]
2.  [[[↑](#cite_ref-2)] [[https://developer.android.com/sdk/](https://developer.android.com/sdk/)]]