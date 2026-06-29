**Resources**

[[]][Home](https://developer.android.com/studio/index.html)

[[]][Package information](https://packages.gentoo.org/packages/dev-util/android-studio)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Android_Studio "wikipedia:Android Studio")

This article contains instructions for installing Android Studio.

## Contents

-   [[1] [Pre-Installation]](#Pre-Installation)
    -   [[1.1] [KVM and QEMU]](#KVM_and_QEMU)
    -   [[1.2] [Pulseaudio]](#Pulseaudio)
    -   [[1.3] [Wayland]](#Wayland)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
    -   [[2.3] [Files]](#Files)
    -   [[2.4] [Invocation]](#Invocation)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Grey screen on launch]](#Grey_screen_on_launch)
    -   [[3.2] [Emulator will not launch]](#Emulator_will_not_launch)
        -   [[3.2.1] [No Android Virtual Devices present]](#No_Android_Virtual_Devices_present)
        -   [[3.2.2] [Missing shared libraries]](#Missing_shared_libraries)
    -   [[3.3] [Emulator will crash Android Studio]](#Emulator_will_crash_Android_Studio)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Pre-Installation]

These pre-installation steps are required for the Android Studio Emulator to work. The package will still install and partially work without these steps, but the Emulator will either not launch, or may seem to be working but will give a cryptic message about \"waiting for target to come online\".

To have a fully functioning Emulator, it is required to have KVM enabled in the kernel (which means that the CPU and BIOS must support KVM), qemu installed, and pulseaudio installed.

If you are using ALSA and prefer not to install pulseaudio, it is possible to run android-studio via apulse.

### [KVM and QEMU]

See [QEMU article](https://wiki.gentoo.org/wiki/QEMU "QEMU") for information on how to set up KVM and install qemu.

QEMU should automatically create a new `kvm` group on the system and there should now be a [/dev/kvm] device.

Show all groups on the system to check if `kvm` was added:

`user `[`$`]`getent group`

Add the user account which will be using Android Studio to the `kvm` group (in the example, the username is `larry`):

`root `[`#`]`usermod -a -G kvm larry `

To check that the user was added to the `kvm` group:

`user `[`$`]`groups larry `

Log out then back in, if already connected with this account.

Make sure [/dev/kvm] is set to the correct ownership and mode permissions:

`user `[`$`]`ls -la /dev/kvm`

The desired permissions are mode `660`(`rw-rw----`) and the desired ownership should be `root:kvm`. This should already be set, if not, set the ownership and permission mode with the following commands:

`root `[`#`]` chown root:kvm /dev/kvm `

`root `[`#`]` chmod 660 /dev/kvm `

### [Pulseaudio]

See the [PulseAudio article](https://wiki.gentoo.org/wiki/PulseAudio "PulseAudio") for information on how to install PulseAudio.

If you are using ALSA and prefer not to install pulseaudio, then install the [media-sound/apulse](https://packages.gentoo.org/packages/media-sound/apulse) package and use it to run android-studio.

`user `[`$`]`apulse android-studio`

### [Wayland]

Since Android Studio Ladybug (2024.2.1) there is experimental Wayland support via **-Dawt.toolkit.name=WLToolkit** option. It can be added:

-   to the end of the command line invocation,
-   via [Help -\> Edit Custom VM Options],
-   directly to the [\~/.config/Google/AndroidStudio\<version\>/studio64.vmoptions] file.

\
It can be verified by selecting [Help -\> About -\> Copy and Close] and reviewing the text copied this way. If Wayland support is properly enabled and working, it should contain the line: *Toolkit: sun.awt.wl.WLToolkit*, otherwise the line may look like this: *Toolkit: sun.awt.X11.XToolkit*.

## [Installation]

### [USE flags]

### [USE flags for] [dev-util/android-studio](https://packages.gentoo.org/packages/dev-util/android-studio) [[]] [Android development environment based on IntelliJ IDEA]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 22:42] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask dev-util/android-studio`

### [Files]

-   [\~/Android] - the SDK lives here
-   [\~/AndroidStudioProjects] - projects created in Android Studio are found here

### [Invocation]

Launch Android Studio with the command:

`user `[`$`]`android-studio`

## [Troubleshooting]

### [Grey screen on launch]

Make sure the relevant java runtime environment variables have been set:

`user `[`$`]`export JDK_HOME=/usr/lib/jvm/openjdk-bin-xxx`

`user `[`$`]`export _JAVA_AWT_WM_NONREPARENTING=1`

### [Emulator will not launch]

Make sure the proper SDK tools and the Emulator are installed. This can be checked by going to [Tools \--\> Android \--\> SDK Manager]. Then click on the [SDK Tools] tab and make sure that the box next to [Android Emulator] is checked as well as the boxes next to [Android SDK Platform-Tools], and [Android SDK Tools].

#### [No Android Virtual Devices present]

Make sure an actual Android Virtual Device (AVD) has been created. Create an AVD by clicking on the green play button underneath the [Run] menu. Then click on [Create New Virtual Device] and follow the instructions from Android Studio.

See the pre-installation section above and make sure that the system supports KVM at the bios and processor level, that KVM is enabled correctly in the kernel, and that qemu and pulseaudio are correctly installed and working. Make sure [/dev/kvm] is set to mode `660` and `root:kvm`, as described in the pre-installation section.

Android Studio itself may only give cryptic information or may act as though the emulator is launching but never launch it. In the terminal where Android Studio was launched, there may be vague messages about timeout reached.

To find out what\'s really going on with the emulator, try launching it directly from the terminal. Assuming

`user `[`$`]`cd ~/Android/Sdk/emulator`

Then get a list of installed AVDs (Android Virtual Devices) with the command:

`user `[`$`]`./emulator -list-avds`

Try launching an AVD:

`user `[`$`]`./emulator -avd Nexus_5X_API_25 `

Where `Nexus_5X_API_25` is an example AVD name.

#### [Missing shared libraries]

Pay attention to the terminal and see if it lists any error messages about missing libraries or other information. For example, the following error message provides a good indication that the package [[[dev-libs/nss]](https://packages.gentoo.org/packages/dev-libs/nss)[]] is not installed:

    ../Android/Sdk/emulator/qemu/linux-x86_64/qemu-system-x86_64: error while loading shared libraries: libnss3.so: cannot open shared object file: No such file or directory

This problem is easily solved by emerging the missing package.

Check in Android Studio Event Log, particularly for something like: `Emulator: libGL error: unable to load driver: <your driver name>`. In this case, go to

`user `[`$`]`cd ~/Android/Sdk/emulator/lib64/libstdc++/`

or

`user `[`$`]`cd ~/Android/Sdk/emulator/lib/libstdc++/`

and move to some backup location the [libstdc++.so.\*] files from there. Now the emulator will try to work with the system libraries. Optionally, make symbolic link to the system [libstdc++.so.6], for example:

`user `[`$`]`ln -s /usr/lib64/gcc/x86_64-pc-linux-gnu/6.4.0/libstdc++.so.6 libstdc++.so.6`

Running Intel x86 Atom images on processors without ssse3 support may also give the warning `Emulator: emulator: WARNING: Host CPU is missing the following feature(s) required for x86 emulation: SSSE3`, but images up to API 22 are known to work despite of it (newer doesn\'t). For Intel x86 Atom_64 images, the warning is: `Emulator: emulator: WARNING: Host CPU is missing the following feature(s) required for x86_64 emulation: SSSE3 SSE4.1 SSE4.2`.

A system reboot might fix the issue so it is worth a shot if all else fails. Another thing to try is removing the emulator and the SDK and then reinstalling them. Also double check that all the pre-installation was followed correctly.

### [Emulator will crash Android Studio]

Try uninstalling and installing the emulator (in the built-in SDK Manager).

## [See also]

-   [qemu](https://wiki.gentoo.org/wiki/Qemu "Qemu") --- a generic, open-source hardware emulator and virtualization suite.
-   [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox") --- cross-platform virtualization software that allows users to run guest operating systems inside a host operating system without having to reboot.

## [External resources]

-   [adasss overlay](https://github.com/gentoo-mirror/adasss) - An overlay containing Android Studio (stable, beta, canary and archival) experimental ebuilds.
-   [android studio grey screen](https://github.com/swaywm/sway/issues/4455) - Grey screen problem solution.