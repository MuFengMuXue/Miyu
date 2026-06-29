**Resources**

[[]][Home](https://launchpad.net/~wenchien/+archive/ubuntu/freefall)

**freefall** is a simple daemon providing HDD shock protection for HP laptops supporting the feature officially called \"HP Mobile Data Protection System 3D\" or \"HP 3D DriveGuard\".

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Kernel]](#Kernel)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Services]](#Services)
        -   [[2.2.1] [OpenRC]](#OpenRC)
-   [[3] [Testing]](#Testing)
    -   [[3.1] [Testing shock protection]](#Testing_shock_protection)

## [Installation]

### [Kernel]

You need to activate the following kernel option either as built-in or as module.

[KERNEL]

    Device drivers --->
        [*] X86 Platform Specific Device Drivers  --->
            <*> HP laptop accelerometer

### [Emerge]

The freefall daemon and init script can be found in [[[sys-apps/linux-misc-apps]](https://packages.gentoo.org/packages/sys-apps/linux-misc-apps)[]]:

`root `[`#`]`emerge --ask sys-apps/linux-misc-apps`

## [Configuration]

### [Files]

Set the HDD in the [/etc/conf.d/freefall] configuration file.

### [Services]

#### [OpenRC]

Start freefall daemon:

`root `[`#`]`/etc/init.d/freefall start`

To start freefall at boot time, add it to your boot runlevel:

`root `[`#`]`rc-update add freefall boot`

## [Testing]

After reboot with new kernel, check if hp_accel driver was initialized correctly:

`user `[`$`]`dmesg | grep hp_accel`

### [Testing shock protection]

** Warning**\
Be careful while performing this test and keep the laptop above something soft. Simulating free fall over the desk or a hard floor is bad idea!

Find the HDD\'s [unload_heads] file, it will be somewhere in the [/sys] directory:

`user `[`$`]`find /sys -name unload_heads`

Go to its directory and run:

`user `[`$`]`watch --difference=permanent cat unload_heads`

Lift the laptop into free space and simulate free fall while holding it firmly. About a 10 cm drop should be enough.

If the disk protection works then the HDD should make \"click\" sound, see one of your laptop\'s LEDs flashing and the watch value\'s background should permanently turn black.