# Android

Plug your phone to your computer using a USB cable adapted for your device.
Make sure this USB cable has a data line (not all cables do).

On your smartphone, you should see the charging icon.
If this is the case, go to your notifications, scroll to the bottom until you see the notification saying that your phone is connected in Charging mode.

Click on the notification, and then set it to File transfer mode, MTP or something similar.

You should now see your phone being detected by most desktop environments.

## Synchronization
There are various applications to transfer files, synchronize notifications and more.

## All-in-one
* KDE Connect () – integrates your Android device with the KDE or Gnome desktop (featuring synced notifications & clipboard, multimedia control, and file/URL sharing).

## Synchronized notifications
*  – provides notification synchronization over LAN featuring authentication, encryption and more

## Transferring files
*  USB cable
** Media Transfer Protocol for modern Android devices
** USB mass storage for older devices
** Android Debug Bridge
* special USB sticks / regular USB stick with adapter
* Bluetooth
* Arch Linux software with Android counterparts
** client or server for protocols that can be used to transfer files (eg. SSH, FTP, Samba or HTTP)
** cloud synchronization clients
** Syncthing
**  – cross-platform file sharing
**  – transfer files over Wi-Fi from your computer to your mobile device by scanning a QR code
**  - An open source cross-platform alternative to AirDrop

## App development
The officially supported way to build Android apps is to use #Android Studio.=== Android Studio ===

[https://developer.android.com/studio/index.html Android Studio is the official Android development environment based on IntelliJ IDEA. It provides integrated Android developer tools for development and debugging.

You can install it with the  package.
For the Beta branch, install the  package.
For the Canary branch, install the  package.

Android Studio creates a  directory in home directory. To reset Android Studio, this directory can be removed.

The Android Studio Setup Wizard installs the required #SDK packages and places the SDK by default in .

To build apps from the command-line (using e.g. ) set the ANDROID_HOME environment variable to your SDK location.

Android Studio has experimental Wayland support since 2024.2, you can enable it by going to Menu > Help > Edit Custom VM Options and adding  as a parameter.

## SDK packages
Android SDK packages can be installed directly from upstream using #Android Studio's SDK Manager or the sdkmanager command line tool (part of the Android SDK Tools). Some Android SDK packages are also available as AUR packages, they generally install to .

The required SDK packages are:

{| class="wikitable"
! Android SDK Package !! SDK-style path !!  AUR package !! AUR dummy !! CLI tools
|-
| Command-Line Tools || tools ||  ||  || apkanalyzer, avdmanager, lint, retrace, screenshot2, sdkmanager
|-
| SDK Build-Tools || build-tools;version ||  ||  || aapt, aapt2, aidl, apksigner, bcc_compat, d8, dexdump, dx, lld, llvm-rs-cc, mainDexClasses, split-select, zipalign
|-
| SDK Platform-Tools || platform-tools ||  ||  || adb, dmtracedump, e2fsdroid, etc1tool, #fastboot, hprof-conv, make_f2fs, make_f2fs_casefold, mke2fs, sload_f2fs, sqlite3, systrace
|-
| SDK Platform || platforms;android-level || , older versions ||  (unnecessary)
|}

The  package provides adb, #fastboot,  and  from the SDK Platform-Tools along with  and .

## Android Emulator
The Android Emulator is available as the  SDK package, the  package, and there is also a dummy package for it: .

To run the Android Emulator you need an Intel or ARM System Image. You can install them through the AUR, with the sdkmanager or using Android Studio's AVD Manager.

If Wayland is used, make sure to read Wayland#Qt, as it might be the case that the emulator complains about Wayland.

## Other SDK packages in the AUR
The Android Support Library is now available online from Google's Maven repository.
You can also install it offline through the  SDK package (also available as ).

## Using /opt/android-sdk as read-only with CoW
The AUR packages install the SDK in . This directory has root permissions, so to use it as your regular user, you should have another directory with write permissions.

To do so, you should use , a FUSE package around overlayfs. This will allow to access read-only  directory and write modifications without copying the data (Copy-On-Write conception).

First, create directories to host the overlay:

 $ LOWER=/opt/android-sdk
 $ UPPER="$HOME/.local/android/.sdk/upper"
 $ WORK="$HOME/.local/android/.sdk/work"
 $ ANDROID_HOME="$HOME/.local/android/sdk"
 $ mkdir -p "$UPPER" "$WORK" "$ANDROID_HOME"

Then mount your overlay and export the Android home variable:

 $ fuse-overlayfs -o squash_to_uid=$(id -u),squash_to_gid=$(id -g),lowerdir=$LOWER,upperdir=$UPPER,workdir=$WORK $ANDROID_HOME
 $ export ANDROID_HOME

You can now use any Android tool (`sdk-manager` for instance) with your copy-on-write setup.

You can unmount it as with any other FUSE fs:

 $ fusermount -u $ANDROID_HOME

## Other IDEs
Android Studio is the official Android development environment based on IntelliJ IDEA. Alternatively, you can use Netbeans with the NBAndroid-V2. All are described below.

## Netbeans
If you prefer using Netbeans as your IDE and want to develop Android applications, use NBAndroid-V2 .

Install  package and follow the instructions from the NBANDROID README.

## Vim / Neovim
It is possible to write  applications for Android and iOS using (Neo)vim like an IDE. Install coc using a Vim plugin manager. Also install the coc-flutter extension for autocompletion (like in Android Studio) and to load the code into an Android emulator.

## Emacs
To develop a mobile  application using Emacs, as the official instruction at flutter.dev suggests, install lsp-dart.

## Other Tools
## Marvin
Marvin is a tool which helps beginners set up an Android development environment. Installing  helps you set up the following things: JDK, Android SDK, IDE(s), and AVD.

## Building
Please note that these instructions are based on the official AOSP build instructions. Other Android-derived systems such as LineageOS will often require extra steps.

## Required packages
To build AOSP 13 you need a TTF font installed (e.g. ) and the dependencies of the  metapackage.

Additionally, LineageOS (as well as other many Android distributions like ArrowOS,PixelExperience etc)  requires the following dependencies of the  metapackage.

## Java Development Kit
The required JDK version depends on the Android version you are building:

* For Android 9 (Pie) and up, Java is included with the Android source and no separate installation is needed.
* For Android 7 and 8 (Nougat and Oreo), OpenJDK 8 is required, which is available with the  package.

## Setting up the build environment
Install the  package.

Create a directory to build.

 $ mkdir ~/android
 $ cd ~/android

## Downloading the source code
This will clone the repositories. You only need to do this the first time you build Android, or if you want to switch branches.

* The  has a  switch that operates similarly to the one used with . Since it controls the number of simultaneous downloads, you should adjust the value depending on downstream network bandwidth.

* You will need to specify a branch (list of branches) to check out with the  switch. If you leave the switch out, you will get the so-called master branch.

Wait a long time. Just the uncompiled source code, along with the  and  directories that are used to keep track of it, are very large. As of Android 10, at least 250 GB of free disk space is required.

## Building the code
This should do what you need for AOSP:

 $ source build/envsetup.sh
 $ lunch full-eng
 $ make -j4

If you run lunch without arguments, it will ask what build you want to create. Use -j with a number between one and two times number of cores/threads.

The build takes a very long time.

## Testing the build
When finished, run/test the final image(s).

 $ emulator

## Creating a flashable Image
To create an image that can be flashed it is necessary to:

 make -j8 updatepackage

This will create a zip image under  (hammerhead being the device name) that can be flashed.

## Flashing
In some cases, you want to return to the stock Android after flashing custom ROMs to your Android mobile device. For flashing instructions of your device, please use XDA forums.

## Fastboot
Fastboot (as well as adb) is included in the  package.

## Samsung devices
Samsung devices cannot be flashed using Fastboot tool. Alternatives are Heimdall and Odin (by using Windows and VirtualBox).

## samloader
To download original Samsung firmware, a platform independent script, samloader can be used.

## Heimdall
 is a cross-platform open-source tool suite used to flash firmware (also known as ROMs) onto Samsung mobile devices and is also known as an alternative to Odin.

The flashing instructions can be found on Heimdall's GitHub repository or on XDA forums.

## Odin (Virtualbox)
It is also possible to restore firmware (Android) on the Samsung devices using Odin, but inside the VirtualBox.

Arch Linux (host) preparation:

# Install VirtualBox together with its extension pack and guest additions.
# Install your preferred, but compatible with Odin, Windows operating system (with VirtualBox guest additions) into a virtual hard drive using VirtualBox.
# Open VirtualBox settings of your Windows operating system, navigate to USB, then tick (or make sure it is ticked) Enable USB 2.0 (EHCI) Controller.
# At VirtualBox running Windows operating system, click in the menu bar Devices > USB Devices, then click on your Samsung mobile device from the list, which is connected to your computer via USB.

Windows (guest) preparation:

# Install Samsung drivers.
# Install Odin.
# Download required Samsung firmware (Android) for your smartphone model.

Check if configuration is working:

# Turn your device into Download mode and connect to your Linux machine.
# In virtual machine toolbar, select Devices > USB > ...Samsung... device.
# Open Odin. The white box (a big one at the bottom-left side) named Message, should print a line similar to this:

  Added!!

which means that your device is visible to Odin & Windows operating system and is ready to be flashed.

## Run Android apps on Arch Linux
There are several projects and methods which support running Android on Arch Linux (or other distributions). As listed below:

* Container-based solutions tend to be the most popular. They are the closest you can get to run Android app natively on a non-Android Linux kernel. They tend to be the best integrated with your system and have good performance. Notable ones are:
** Waydroid is a fork of Anbox, and it is gaining popularity. It is more performant, because it runs closer to the hardware. It is based on a newer LineageOS 20.0 (Android 13) based image with the option to install the Google Play Store and other Open Gapps. Beside running apps in standalone windows, it can also run a full Android UI.

* There are also a few Chromium extensions that can run android apps:
** Arc Welder was an extension by google to test how apps would run on Chrome OS, but is now discontinued.
** ARChon is an unmaintained open source extension to run android apps on Chromium-based browsers. As of July 2023, the sample app does not work because "Old versions of Chrome apps won't open on Linux devices after 2022".

* Of course it is also possible to run a full android emulator. One upside to this is that you can run arm apps on x86. A downside is worse performance. Examples are:
** Android studio's built-in emulator, as earlier mentioned in this article.
** Genymotion is a pay for Android emulation/testing suite.

* There are also x86_64 compatible OS images based on Android, which can run inside common virtual machines (including KVM with VirtIO GPU) or on bare metal.
** Bliss OS is an Android-based open source OS that incorporates many optimizations and features, pre-rooted with KernelSU. ARM emulation is also included.
** For older Android versions, see Android-x86.

## Troubleshooting
## Android Studio: Android Virtual Devices show 'failed to load'.
Make sure you have exported the variable  as explained in #Android Studio.

## Android Studio: 'failed to create the SD card'
If you try to run an AVD (Android Virtual Device) under x86_64 Arch and get the error above, install the  package from the multilib repository.

## Eclipse: During Debugging "Source not found"
Most probably the debugger wants to step into the Java code. As the source code of Android does not come with the Android SDK, this leads to an error. The best solution is to use step filters to not jump into the Java source code. Step filters are not activated by default. To activate them: Window > Preferences > Java > Debug > Step Filtering.
Consider to select them all. If appropriate you can add the android.* package. See Use Step Filters.

## ValueError: unsupported pickle protocol
One fix is to issue:

 $ rm ~/.repopickle_.gitconfig

If that does not work, then try this:

 $ find /path/to/android-root -name .repopickle_config -delete

## libGL error: failed to load driver: swrast OR AVD does not load and no error message displayed
Sometimes, beginning to load an AVD will cause an error message similar to this to be displayed, or the loading process will appear to finish but no AVD will load and no error message will be displayed.

The AVD loads an incorrect version of libstdc++, you can remove the folder libstdc++ from  (for 64-bit) or  (for 32-bit) , e.g.:

 $ rm -r ~/.android-sdk/emulator/lib64/libstdc++

Note that in versions before Android Studio 3.0, this directory was in a different location:

 $ rm -r ~/Android/Sdk/emulator/lib64/libstdc++

Alternatively you can set and export ANDROID_EMULATOR_USE_SYSTEM_LIBS in ~/.profile as:

 export ANDROID_EMULATOR_USE_SYSTEM_LIBS=1

Reference: Android Studio user guide

Fix for the .desktop file might be achieved by using env command, prefixing the Exec line Desktop entries#Modify environment variables

 env ANDROID_EMULATOR_USE_SYSTEM_LIBS=1

## sh: glxinfo: command not found
Here is the full error:

 Cannot launch AVD in emulator.
 Output:
 sh: glxinfo: command not found
 sh: glxinfo: command not found
 libGL error: unable to load driver: swrast_dri.so
 libGL error: failed to load driver: swrast
 X Error of failed request:  BadValue (integer parameter out of range for operation)
   Major opcode of failed request:  154 (GLX)
   Minor opcode of failed request:  24 (X_GLXCreateNewContext)
   Value in failed request:  0x0
   Serial number of failed request:  32
   Current serial number in output stream:  33
 QObject::~QObject: Timers cannot be stopped from another thread

You can try to install glxinfo () but if your computer has enough power you could simply use software to render graphics.  To do so, go to Tools > Android > AVD Manager, edit the AVD (click the pencil icon), then select Software - GLES 2.0 for Emulated Performance > Graphics.

## Android Emulator: no keyboard input in xfwm4
In xfwm4, the vertical toolbar buttons window that is on the right of the emulator takes focus from the emulator and consumes keyboard events.
(bug report)

You can use the workaround described in # Open the xfwm4 settings.
# Switch to the Focus tab.
# Change the Focus Model to "Focus follow mouse".
# Disable Automatically raise windows when they receive focus option below.

## Android Emulator: Window is shaking and blinking when used in WM tiled mode
When using Tiled Window Manager like dwm, Android Emulator will shake and blink. You can use the workaround described in [https://github.com/esjeon/krohnkite/issues/72#issuecomment-613789987 krohnkite issue 72 (window floating is induced by  in dwm).

## Android Emulator: Segmentation fault (core dumped)
When using Nouveau drivers try to disable gpu hardware acceleration.

In some devices it can only be done by editing .# Set
# Set

## Android Emulator: Not launching / qemu-system: address resolution failed
There is an issue where no emulator-window shows up after starting a virtual device in android-studio. If this applies to you, launch the emulator from the console and inspect its output:

 $ emulator -avd $(emulator -list-avds)

If on any line, it says anything similar to:

 qemu-system-x86_64 : address resolution failed for ::1:46189: Name or service not known

you may try disabling IPv6:

 $ sysctl net.ipv6.conf.all.disable_ipv6=1

If this solves the issue and the virtual device shows up in android-studio, you may consider a permanent change:

## Android Emulator: Emulator terminated with exit code 134
If running Wayland, a graphical error like  may be worked around by forcing X11 with .

## adb: sideload connection failed: insufficient permissions for device
If you get the errors:

 adb: sideload connection failed: insufficient permissions for device
 See [https://developer.android.com/tools/device.html https://developer.android.com/tools/device.html for more information
or
 adb: trying pre-KitKat sideload method...
 adb: pre-KitKat sideload connection failed: insufficient permissions for device
 See https://developer.android.com/tools/device.html for more information

You might be able to solve it by restarting the adb server:

  $ adb kill-server
  # adb start-server

Alternatively, make sure you have installed the Android udev rules. See #Fastboot.

## License not accepted
Since SDK packages from the AUR are installed to  which is owned by root, the  command for accepting the licenses must also be ran as root. If this script is not ran as root, accepting the licenses will silently fail.

You can confirm the licenses were successfully accepted by checking if the license appears in the  directory.

## Building Lineageos error: module manifest_input.classifier-service does not exist
This error arises on devices that require a vendor directory to be populated before breakfast will succeed, as noted in the warning section. Extract proprietary blobs and continue.

## Building Lineageos common.mk: error:missing libthermalclient (or other library or .so file)"
(hardware/qcom/sm7250/display/composer/../common.mk: error: "vendor.qti.hardware.display.composer-service (EXECUTABLES android-arm64) missing libthermalclient (SHARED_LIBRARIES andr oid-arm64)"
You can set ALLOW_MISSING_DEPENDENCIES=true in your environment if this is intentional, but that may defer real problems until later in the build.)

You either have not extracted proprietary blobs, the image you extracted from did not have all of them, or the extraction script did not work correctly.
Either find a different image to extract blobs from, use a different extraction script or use blobs from  themuppets

## Building Lineageos AssertionError: Failed to execute: out/soong/host/linux-x86/bin/mke2fs -O ^has_journal...
e2fsprogs disabled orphan_file in version 1.47.0, so it either must be downgraded for the old command to succeed, or the option orphan_file should be removed from /etc/mke2fs.conf on the machine you're building on, since the bundled mke2fs reads the host's config file.

To downgrade: e2fsprogs 1.46.0 on arch linux archive

## Building Lineageos ExternalError: Failed to run command '
if you scroll up a bit, see:
Sum of sizes in google_dynamic_partitions_partition_list is 4883337216, which is greater than google_dynamic_partitions_size (4873781248)
[0224/122117.280262:FATAL:generate_delta_main.cc(619) Check failed: payload_config.target.ValidateDynamicPartitionMetadata().

Some users had success with setting the option , GMS being Google Mobile Services, more commonly - GApps. This option may or may not be suitable to your needs. Some strongly discourage using this option even as a fix to this error.

Issue seems to come from changes being made, resulting in larger file sizes. To leave more space for the partitions, it is recommended to lower the parameter  by an amount at least equivalent to the difference between the numbers you get in the error. This option is set in a makefile, for example in  or, if you don't see it there, in a file it includes, for example google devices have common parameters in
