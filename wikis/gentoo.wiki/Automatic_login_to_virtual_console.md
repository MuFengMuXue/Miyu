** Warning**\
Automatic logins pose security risks. Anyone who can start the computer can get access to the operating system. Consider a BIOS password for additional security.

Gentoo supports different init systems. Each init system requires their own solution for auto-login.\
All involve passing `--autologin <username>` to the terminal handler called agetty, but how this is done differs per init system

## Contents

-   [[1] [Automatic login for different init systems]](#Automatic_login_for_different_init_systems)
    -   [[1.1] [sysvinit]](#sysvinit)
    -   [[1.2] [openrc-init]](#openrc-init)
    -   [[1.3] [systemd]](#systemd)
-   [[2] [Continue with starting an X session]](#Continue_with_starting_an_X_session)

## [Automatic login for different init systems]

### [sysvinit]

Edit [/etc/inittab] as follows:

[FILE] **`/etc/inittab`**

    # TERMINALS
    c1:12345:respawn:/sbin/agetty --autologin <username> --noclear 38400 tty1 linux
    c2:2345:respawn:/sbin/agetty 38400 tty2 linux
    c3:2345:respawn:/sbin/agetty 38400 tty3 linux
    c4:2345:respawn:/sbin/agetty 38400 tty4 linux
    c5:2345:respawn:/sbin/agetty 38400 tty5 linux
    c6:2345:respawn:/sbin/agetty 38400 tty6 linux

### [openrc-init]

Start with the [openrc-init](https://wiki.gentoo.org/wiki/OpenRC/openrc-init "OpenRC/openrc-init") instructions, and adapt it for auto login on the first tty as follows:

Create a file [/etc/conf.d/agetty.tty1]:

[FILE] **`/etc/conf.d/agetty.tty1`**

    agetty_options="--autologin <username> --noclear"

Then for the changes to take affect you can restart tty1 with the following command:

`root `[`#`]`rc-service agetty.tty1 restart`

** Note**\
This will kick you out of your graphical session if it\'s being hosted on tty1, make sure everything being worked on is saved to disk before continuing.

### [systemd]

[FILE] **`/etc/systemd/system/getty@tty1.service.d/override.conf`**

    [Service]
    Type=simple
    ExecStart=
    ExecStart=-/sbin/agetty --autologin <username> --noclear %I 38400 linux

## [Continue with starting an X session]

This is described at [X without Display Manager](https://wiki.gentoo.org/wiki/X_without_Display_Manager "X without Display Manager").