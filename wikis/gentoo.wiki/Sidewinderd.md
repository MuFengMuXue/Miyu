**Resources**

[[]][Home](https://github.com/tolga9009/sidewinderd/)

**sidewinderd** is a user space daemon that enables special keys and macro recording for various Logitech and Microsoft gaming peripherals.

## Contents

-   [[1] [Hardware]](#Hardware)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Kernel]](#Kernel)
    -   [[2.2] [Software]](#Software)
        -   [[2.2.1] [Overlay]](#Overlay)
        -   [[2.2.2] [Manual]](#Manual)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Service]](#Service)
        -   [[3.1.1] [OpenRC]](#OpenRC)
        -   [[3.1.2] [systemd]](#systemd)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [Macro recording]](#Macro_recording)
        -   [[4.1.1] [Logitech G105]](#Logitech_G105)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Overlay]](#Overlay_2)
    -   [[5.2] [Manual]](#Manual_2)
-   [[6] [Troubleshooting]](#Troubleshooting)

## [Hardware]

  ------------------------- ------------------------ ----------------- ---------------------- -------------
  Device                    Vendor ID / Product ID   Vendor Name       Product Name           Supported
  Logitech G105             `046d:c248`              Logitech, Inc.    G105 Gaming Keyboard   Yes
  Logitech G710/G710+       `046d:c24d`              Logitech, Inc.    G710 Gaming Keyboard   Not tested
  Microsoft SideWinder X4   `045e:0768`              Microsoft Corp.   Sidewinder X4          Not tested
  Microsoft SideWinder X6   `045e:074b`              Microsoft Corp.                          Not tested
  ------------------------- ------------------------ ----------------- ---------------------- -------------

## [Installation]

### [Kernel]

[KERNEL] **Enabling user level driver and HID support**

        Device Drivers --->
              Input device support --->
                [*]   Miscellaneous devices --->
                        <*>   User level driver support
              HID support --->
                [*]   /dev/hidraw raw HID device support

### [Software]

#### [Overlay]

An ebuild is available in the [fowlay](https://repos.gentoo.org/#fowlay) overlay. For general info on overlays read [here](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository"). To add the overlay do

`root `[`#`]`eselect repository enable fowlay `

`root `[`#`]`emerge --sync fowlay`

and to emerge sidewinderd do

`root `[`#`]`emerge --ask games-util/sidewinderd`

#### [Manual]

Install the required dependencies:

`root `[`#`]`emerge --ask --noreplace dev-libs/libconfig dev-libs/tinyxml2 dev-util/cmake dev-vcs/git`

Clone the sidewinderd [Git](https://wiki.gentoo.org/wiki/Git "Git") repository:

`root `[`#`]`git clone https://github.com/tolga9009/sidewinderd.git /usr/local/src/sidewinderd`

Build and install sidewinderd:

`root `[`#`]`mkdir /usr/local/src/sidewinderd/build `

`root `[`#`]`cd /usr/local/src/sidewinderd/build `

`root `[`#`]`cmake -DCMAKE_INSTALL_PREFIX=/usr .. `

`root `[`#`]`make && make install `

## [Configuration]

Specify the username to run sidewinderd as:

[FILE] **`/etc/sidewinderd.conf`**

    user = "larry";

** Important**\
It is ***not*** recommended to run sidewinderd as [root].

To record macros without delays set `capture_delays` to `false`:

[FILE] **`/etc/sidewinderd.conf`**

    capture_delays = false;

### [Service]

#### [OpenRC]

Create the following service file if sidewinderd was installed manually.

[FILE] **`/etc/init.d/sidewinderd`**

    #!/sbin/openrc-run

    command="/usr/bin/sidewinderd"
    command_args="-c /etc/sidewinderd.conf -d"

    depend()

Make the service file executable:

`root `[`#`]`chmod +x /etc/init.d/sidewinderd`

Start sidewinderd:

`root `[`#`]`rc-service sidewinderd start`

Start sidewinderd at boot:

`root `[`#`]`rc-update add sidewinderd default`

#### [systemd]

Start sidewinderd:

`root `[`#`]`systemctl start sidewinderd`

Start sidewinderd at boot:

`root `[`#`]`systemctl enable sidewinderd`

## [Usage]

### [Macro recording]

#### [Logitech G105]

If sidewinderd started successfully, the [MR], [M1], [M2], [M3] and [G1] through [G6] keys should now be usable. Three sets of macro profiles can be switched between using the [M1], [M2] and [M3] keys. Recorded macros are stored in their respective profile directories e.g.[\~/.local/share/sidewinderd/profile\_

To record a macro for the [G1] key in the [M1] profile, press [M1], [MR], [G1], the desired key sequence, and [MR] again. To playback the recorded macro, press the [G1] key.

## [Removal]

#### [Overlay]

`root `[`#`]`emerge --ask --depclean --verbose games-util/sidewinderd`

#### [Manual]

Delete the following files:

`root `[`#`]`rm /etc/init.d/sidewinderd `

`root `[`#`]`rm /etc/sidewinderd.conf `

`root `[`#`]`rm /usr/bin/sidewinderd `

`root `[`#`]`rm /usr/lib/systemd/system/sidewinderd.service `

## [Troubleshooting]

The following error message from manually installed sidewinderd has been observed after a world update of Gentoo on 2017-11-26:

    sidewinderd: error while loading shared libraries: libconfig++.so.9: cannot open shared object file: No such file or directory

It is probably due to the update of [[[dev-libs/libconfig]](https://packages.gentoo.org/packages/dev-libs/libconfig)[]] from 1.5 to 1.7.1. To fix the issue, re-sync the sidewinderd git repository, then [build and install](#Software) sidewinderd again.