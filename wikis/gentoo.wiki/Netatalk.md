**Resources**

[[]][Home](http://netatalk.sourceforge.net/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Netatalk "wikipedia:Netatalk")

**Netatalk** is a free, open-source implementation of the [Apple Filing Protocol](https://en.wikipedia.org/wiki/Apple_Filing_Protocol "wikipedia:Apple Filing Protocol") (AFP). It allows Unix-like operating systems to serve as file, print and time servers for [Macintosh](https://en.wikipedia.org/wiki/Macintosh "wikipedia:Macintosh") computers.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Services]](#Services)

## [Installation]

### [Emerge]

Install [[[net-fs/netatalk]](https://packages.gentoo.org/packages/net-fs/netatalk)[]]:

`root `[`#`]`emerge --ask net-fs/netatalk`

## [Configuration]

In this example, the icon model that appears on clients is a Mac Pro and all private IPv4 hosts are allowed access to a Time Machine volume.

Create the [/mnt/storage/TimeMachine] folder:

`root `[`#`]`mkdir /mnt/storage/TimeMachine`

Allow all users read+write access. In practice a more secure configuration should be used with uam list = \"uams_dhx.so uams_dhx2.so\"

`root `[`#`]`chmod 777 /mnt/storage/TimeMachine`

Edit [/etc/afp.conf]:

[FILE] **`/etc/afp.conf`**

    [Global]
        mimic model = MacPro
        hosts allow = 10.0.0.0/8 172.16.0.0/20 192.168.0.0/16
        uam list = uams_guest.so
    [TimeMachine]
        path = /mnt/storage/TimeMachine
        time machine = yes

## [Usage]

### [Services]

To start [netatalk]:

`root `[`#`]`/etc/init.d/netatalk start`

To start [netatalk] at boot:

`root `[`#`]`rc-update add netatalk default`