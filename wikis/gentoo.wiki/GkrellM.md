**Resources**

[[]][Home](http://www.gkrellm.net)

[[]][Wikipedia](https://en.wikipedia.org/wiki/GKrellM "wikipedia:GKrellM")

**GKrellM** is a powerful graphical system monitor. It integrates in a compact view a lot of customizable informations, like sensors, CPU/memory load, [filesystems](https://wiki.gentoo.org/wiki/Filesystem "Filesystem") usage, network traffic and so on. Every feature comes with customizable alarms and with the opportunity to run some personal script (to send a mail, stop a process, restart a service, etc) when critical situations occur.

A lot of official and unofficial **plugins** are available, for special tasks and fun. Many plugins are in the portage tree and many more are listed on the developer site.

Very powerful, GKrellM comes with a **daemon** that can be ran on a remote machine (i.e. a server deep in a cellar or far in the world) to monitor it from your wide-screen box.

If you want to try another program similar to GKrellM you can read about [Conky](https://wiki.gentoo.org/wiki/Conky "Conky"). Many users love Conky, because of the elegant interface and the textual configuration; but Conky cannot monitor remote (and therefore multiple) machines.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
-   [[3] [Remote monitoring]](#Remote_monitoring)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/gkrellm](https://packages.gentoo.org/packages/app-admin/gkrellm) [[]] [Single process stack of various system monitors]

  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------------
  [`X`](https://packages.gentoo.org/useflags/X)                     Build both the X11 gui (gkrellm) and the server (gkrellmd). Disabling this flag builds the server only
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)           Enable SSL support for mail checking with net-libs/gnutls (overrides \'ssl\' USE flag)
  [`hddtemp`](https://packages.gentoo.org/useflags/hddtemp)         Enable monitoring of hdd temperature (app-admin/hddtemp)
  [`lm-sensors`](https://packages.gentoo.org/useflags/lm-sensors)   Enable monitoring sensors via sys-apps/lm-sensors
  [`nls`](https://packages.gentoo.org/useflags/nls)                 Add Native Language Support (using gettext - GNU locale utilities)
  [`ntlm`](https://packages.gentoo.org/useflags/ntlm)               Enable NTLM authentication for mail checking with net-libs/libntlm
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                 Enable SSL support for mail checking with dev-libs/openssl
  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-02-17 02:44] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask app-admin/gkrellm`

## [Configuration]

If you emerged GKrellm with the *lm-sensors* USE flag, you have to configure [lm_sensors](https://wiki.gentoo.org/wiki/Lm_sensors "Lm sensors") before, to activate and tune up your motherboard sensors. Similarly, if you emerged with the *hddtemp* USE flag, you should setup [[[app-admin/hddtemp]](https://packages.gentoo.org/packages/app-admin/hddtemp)[]] before.

There are many configuration options available via graphical interface and they are very easy to find and understand. Hopefully, you don\'t need any special explanation. Be sure to note the detailed filesystem tool, that can be a graphical replacement of the **df** command and a notification system.

Every monitor comes with a warning level and an alarm level. The built-in warning and alarm task is a weak animation, but you can run (and repeat) a command to take an action against the problem.

## [Remote monitoring]

If you want to monitor a remote machine from a local machine, you have to run the gkrellmd daemon on the remote machine.

The configuration is quite easy ([/etc/gkrellmd.conf]) and the default values will work.

Once done, start the daemon:

`root `[`#`]`/etc/init.d/gkrellmd start`

If you want the daemon starts automatically when the machine starts:

`root `[`#`]`rc-update add gkrellmd default`

To monitor the remote system, just call the GKrellM program with the *-s* option from your local box:

`root `[`#`]`gkrellm -s REMOTE_MACHINE_NAME`

## [External resources]

-   [GKrellM developer page](http://members.dslextreme.com/users/billw/gkrellm/gkrellm.html)
-   Browse some screenshots at [muhri site](http://www.muhri.net/)
-   Screenshot about the graphical power of GKrellM at [Linuxcs.org](http://www.lynucs.org/?gkrellm)