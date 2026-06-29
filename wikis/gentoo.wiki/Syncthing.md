**Resources**

[[]][GitHub](https://github.com/syncthing/syncthing)

[[]][Home](https://syncthing.net/)

[[]][[#syncthing](ircs://irc.libera.chat/#syncthing)] ([[webchat](https://web.libera.chat/#syncthing)])

[[]][Wikipedia](https://en.wikipedia.org/wiki/Syncthing "wikipedia:Syncthing")

[[]][Official documentation](https://docs.syncthing.net/)

**Syncthing** is a continuous file synchronization program. It synchronizes files between two or more computers in real time. Syncthing is available on Linux, MacOS, Android, Windows and other operating systems, making it a good choice for cross platform file sharing.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
        -   [[2.2.2] [systemd]](#systemd)
    -   [[2.3] [Firewall]](#Firewall)
    -   [[2.4] [Sandboxing]](#Sandboxing)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Invocation]](#Invocation)
    -   [[3.2] [Running Syncthing as an individual user]](#Running_Syncthing_as_an_individual_user)
    -   [[3.3] [Running Syncthing as a system service]](#Running_Syncthing_as_a_system_service)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [Changing the user of init service]](#Changing_the_user_of_init_service)
    -   [[4.2] [Syncing files with Android]](#Syncing_files_with_Android)
    -   [[4.3] [Headless syncthing with ssh tunnel]](#Headless_syncthing_with_ssh_tunnel)
-   [[5] [More documentation]](#More_documentation)
-   [[6] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [net-p2p/syncthing](https://packages.gentoo.org/packages/net-p2p/syncthing) [[]] [Open Source Continuous File Synchronization]

  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`tools`](https://packages.gentoo.org/useflags/tools)             Install stdiscosrv, strelaysrv and other tools to /usr/libexec/syncthing/.
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-12 13:51] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask net-p2p/syncthing`

## [Configuration]

To view all available configuration options:

`user `[`$`]`man 5 syncthing-config`

### [Files]

[\$HOME/.local/state/syncthing]

[/etc/conf.d/syncthing] (OpenRC)

[/var/lib/syncthing/.config/syncthing/config.xml] (systemd system service)

### [Service]

#### [OpenRC]

OpenRC can start Syncthing at startup:

`root `[`#`]`rc-update add syncthing default `

#### [systemd]

Syncthing can be started as a user with systemd:

`user `[`$`]`systemctl --user enable syncthing.service`

`user `[`$`]`systemctl --user start syncthing.service`

### [Firewall]

Syncthing requires port 22000 (UDP and TCP) to be open for syncing, and port 21027/UDP to be open for discovery.

Using [Ufw](https://wiki.gentoo.org/wiki/Ufw "Ufw"), you can allow them like this:

`root `[`#`]`ufw allow syncthing`

Similarly, using [Firewalld](https://wiki.gentoo.org/wiki/Firewalld "Firewalld") you can allow them like this:

`root `[`#`]`firewall-cmd --zone=public --add-service=syncthing --permanent`

`root `[`#`]`firewall-cmd --zone=public --reload`

Additionally, if using the web interface from remote machines, the port 8384 needs to be allowed. This service is called [syncthing-gui] in both Firewalld and UFW, respectively. Keep in mind that this shouldn\'t be done without TLS and proper authentication; a better approach using SSH tunnels is described [below](#Headless_syncthing_with_ssh_tunnel).

Refer to the [Syncthing\'s page on firewalls](https://docs.syncthing.net/users/firewall.html) for further information.

### [Sandboxing]

Since Syncthing can access all files by default, it\'s a good idea to either run Syncthing in a containerized environment or sandbox it using [Firejail](https://wiki.gentoo.org/wiki/Firejail "Firejail") or [AppArmor](https://wiki.gentoo.org/wiki/AppArmor "AppArmor").

## [Usage]

### [Invocation]

`user `[`$`]`syncthing --help`

    Usage: syncthing <command>

    Flags:
      -h, --help    Show context-sensitive help.

    Commands:
      serve
        Run Syncthing

      decrypt
        Decrypt or verify an encrypted folder

      cli
        Command line interface for Syncthing

    Run "syncthing <command> --help" for more information on a command.

### [Running Syncthing as an individual user]

Syncthing can be started as a common user:

`user `[`$`]`syncthing`

It will create the following directories at first use:

[\$/.config/syncthing]

[\$/Sync]

Syncthing will also fire up a browser page at [http://127.0.0.1:8384](http://127.0.0.1:8384) for monitoring and configuration.

### [Running Syncthing as a system service]

[Upstream mentions the following commands](https://docs.syncthing.net/users/autostart.html#how-to-set-up-a-system-service) can be used to start syncthing has a system service. Do the following steps when using syncthing in a server to client architecture:

`root `[`#`]`systemctl enable syncthing@syncthing.service`

This will run the syncthing executable as the syncthing user, which is created when syncthing is installed.

Check the status of the service by issuing:

`root `[`#`]`systemctl status syncthing@syncthing.service`

## [Troubleshooting]

### [Changing the user of init service]

User and group with which Syncthing creates and modifies the synced files, can be changed by uncommenting the following lines in [/etc/conf.d/syncthing]:

\

[FILE] **`/etc/conf.d/syncthing`Changing the default user of syncthing init service**

    # <2.0.14
    #SYNCTHING_USER="syncthing"
    #SYNCTHING_GROUP="syncthing"

    # >=2.0.14 (first known version to use `command_user' instead of `SYNCTHING_USER' and `SYNCTHING_GROUP')
    #command_user="syncthing:syncthing"

### [Syncing files with Android]

If files are shared with Android, make sure to enable \"Ignore Permissions\" in the advanced tab. This option disables comparing and syncing file permissions and is useful on systems with nonexistent or custom permissions (e.g. FAT, exFAT, Synology, Android).

### [Headless syncthing with ssh tunnel]

The easiest thing to do is reverse proxy [ssh](https://wiki.gentoo.org/wiki/Ssh "Ssh") to access the config. It is in the documentation:

`user `[`$`]`ssh -L 9090:localhost:8384 <name>@<ip>`

Now the page [http://localhost:9090](http://localhost:9090) can be opened on the computer and make edits to the browser page.

## [More documentation]

Syncthing provides a number of man pages:

-   [synthing](https://www.mankier.com/1/syncthing)
-   [syncthing-config](https://www.mankier.com/5/syncthing-config)
-   [syncthing-faq](https://www.mankier.com/7/syncthing-faq)
-   [syncthing-networking](https://www.mankier.com/7/syncthing-networking)
-   [syncthing-device-ids](https://www.mankier.com/7/syncthing-device-ids)

## [See also]

-   [Rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") --- a powerful file sync program capable of efficient file transfers and directory synchronization.