This page contains [[changes](https://wiki.gentoo.org/index.php?title=Non_root_Xorg&diff=1305815)] which are not marked for translation.

\
This page describes how an unprivileged user can run [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") without using suid.

** Important**\
The logind provider does not provide the same level of access as the legacy SUID-enabled Xorg does. The elogind provider allows a locally seated user to be granted access to \$TTY and input devices. Users who wish to start X remotely will need to take extra steps to ensure that a seat is given to the user from which they start X, or stay with the legacy behaviour of X with suid.

## Contents

-   [[1] [Requisites]](#Requisites)
    -   [[1.1] [The logind provider]](#The_logind_provider)
    -   [[1.2] [elogind service running]](#elogind_service_running)
-   [[2] [Security issues with running xorg-server as root]](#Security_issues_with_running_xorg-server_as_root)
-   [[3] [Verification]](#Verification)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Cannot start Xorg as regular user]](#Cannot_start_Xorg_as_regular_user)
    -   [[4.2] [Framebuffer \"Permission denied\"]](#Framebuffer_.22Permission_denied.22)
-   [[5] [See also]](#See_also)
-   [[6] [References]](#References)
-   [[7] [External resources]](#External_resources)

## [Requisites]

### [The logind provider]

Currently there are two logind providers in Gentoo, [systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") and [elogind](https://wiki.gentoo.org/wiki/Elogind "Elogind"). Users of systemd [profile](https://wiki.gentoo.org/wiki/Profile_(Portage) "Profile (Portage)") and users of desktop profiles (both systemd and non-systemd ones) will already have a logind interface provided; users of [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") with default profile will be required to globally enable the `elogind` [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag") and update the system with [emerge -ND \@world]. It is also required to re-login after `elogind` has been enabled, to activate it. If either the `systemd` or `elogind` USE flag is enabled on [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]] together with the `suid` USE flag, instead of installing with suid enabled, [[[x11-base/xorg-server]](https://packages.gentoo.org/packages/x11-base/xorg-server)[]] will be installed with suid-wrapper, which will only preserve suid if the graphics driver in use really requires root.

The elogind users are recommended to add elogind to the boot runlevel. While it is not strictly necessary, since elogind can be started upon receiving an event over dbus, it will clash with other services that depend on elogind, like fwupd, resulting in OpenRC trying to start already started elogind and thus failing to do so.

### [elogind service running]

It is required to have *elogind* started in the boot runlevel so that pam_elogind can communicate with elogind daemon:

`root `[`#`]`rc-update add elogind boot`

`root `[`#`]`/etc/init.d/elogind start`

## [Security issues with running xorg-server as root]

Several vulnerabilities have been discovered in the X.Org X server. Missing input sanitising in X server extensions may result in local privilege escalation if the X server is configured to run with root privileges.^[\[1\]](#cite_note-1)^ These vulnerabilities can result in an attacker accessing confidential information^[\[2\]](#cite_note-2)^ as well as potentially bypassing protections provided by ASLR.^[\[3\]](#cite_note-3)^

** Note**\
Debian documentation and other online publications released after January 25, 2012 are under the MIT (Expat) License. ^[\[4\]](#cite_note-4)[\[5\]](#cite_note-5)^

## [Verification]

Some popular [display managers](https://wiki.gentoo.org/wiki/Display_manager "Display manager") (like [[[x11-misc/lightdm]](https://packages.gentoo.org/packages/x11-misc/lightdm)[]]^[\[6\]](#cite_note-6)^) don\'t support an unprivileged user running Xorg.

After a graphical login, the X server should not be running under root but a regular user:

`user `[`$`]`ps -fC X`

    UID          PID    PPID  C STIME TTY          TIME CMD
    larry       712     711  3 14:56 tty1     00:02:20 /usr/bin/X -nolisten tcp -keeptty :0

## [Troubleshooting]

### [Cannot start Xorg as regular user]

The majority of problems with running Xorg as a user other than root after switching to *elogind* come down to issues with PAM. One can confirm that *elogind* is working by running [loginctl user-status]. If *elogind* is running correctly, the output should look something like this:

`user `[`$`]`loginctl user-status `

    user (1000)
             Since: Tue 2020-10-13 12:03:02 CDT; 2h 16min ago
             State: active
          Sessions: *1
            Linger: no
              Unit: user-1000.slice

If instead it shows an error, for example:

`user `[`$`]`loginctl user-status `

    Failed to create bus connection: No such file or directory

or if [startx] still fails, then it\'s worth to check:

-   Have the configuration files in /etc been updated after updating the system with the new USE flags? ([dispatch-conf])
-   (elogind users) Is there any trace of *pam_elogind.so* in [/etc/pam.d/system-auth]?
-   Is the dbus service running?
-   (elogind users) Is the elogind service running? (It may be desirable to run [rc-update add elogind boot])
-   Is regular user added to the video group?

### [][Framebuffer \"Permission denied\"]

If starting [Xorg] as [root] works, but not as [user], and the log file mentioned in the [startx] error contains the following line, then [user] cannot access the raw framebuffer device.

[FILE] **`Xorg.0.log`**

    [   108.953] (EE) open /dev/fb0: Permission denied

This can be fixed by adding [user] to the [video] group. In order to apply the new permissions, [user] must log out and log back in.

`root `[`#`]`ls -l /dev/fb0 `

    crw-rw----. 1 root video 29, 0 Apr 26 19:39 /dev/fb0

`root `[`#`]`usermod -a -G video user `

## [See also]

-   [Xorg](https://wiki.gentoo.org/wiki/Xorg "Xorg") --- an open source implementation of the [X server](https://wiki.gentoo.org/wiki/X_server "X server").
-   [Xorg/Guide](https://wiki.gentoo.org/wiki/Xorg/Guide "Xorg/Guide") --- explains what Xorg is, how to install it, and the various configuration options.
-   [X server](https://wiki.gentoo.org/wiki/X_server "X server") --- the main component of the X Window system which abstracts the hardware and provides the foundation for most graphical user interfaces, like [desktop environments](https://wiki.gentoo.org/wiki/Desktop_environment "Desktop environment") or [window managers](https://wiki.gentoo.org/wiki/Window_manager "Window manager"), and their applications.

## [References]

1.  [[[↑](#cite_ref-1)] [[\"DSA-4758-1 xorg-server \-- security update\"](https://web.archive.org/web/20201012165130/https://www.debian.org/security/2020/dsa-4758) Archived from [\"the original\"](https://www.debian.org/security/2020/dsa-4758).]]
2.  [[[↑](#cite_ref-2)] [[\"CVE-2020-14345\"](https://web.archive.org/web/20201012165147/https://security-tracker.debian.org/tracker/CVE-2020-14345). Archived from [\"the original\"](https://security-tracker.debian.org/tracker/CVE-2020-14345).]]
3.  [[[↑](#cite_ref-3)] [[\"CVE-2020-14347\"](https://web.archive.org/web/20201012165143/https://security-tracker.debian.org/tracker/CVE-2020-14347). Archived from [\"the original\"](https://security-tracker.debian.org/tracker/CVE-2020-14347).]]
4.  [[[↑](#cite_ref-4)] [The license information for Debian WWW Pages can be found [\"here\"](https://web.archive.org/web/20201012165157/https://www.debian.org/license). Archived from [\"the original\"](https://www.debian.org/license).]]
5.  [[[↑](#cite_ref-5)] [The MIT (Expat) License can be found [\"here\"](https://web.archive.org/web/20201012171659/https://www.debian.org/legal/licenses/mit). Archived from [\"the original\".](https://www.debian.org/legal/licenses/mit)]]
6.  [[[↑](#cite_ref-6)] [[Support non-root X · Issue #18 · canonical/lightdm · GitHub](https://github.com/canonical/lightdm/issues/18), May 14th, 2018. Retrieved on January 17th, 2021]]

\

## [External resources]

-   [Rootless Xorg](https://wiki.archlinux.org/title/Xorg#Rootless_Xorg) in ArchLinux Wiki
-   [xinit](https://wiki.archlinux.org/title/Xinit) in ArchLinux Wiki. In paritcular description around `"$XDG_VTNR"`.