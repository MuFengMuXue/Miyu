**Resources**

[[]][Home](https://www.libvirt.org/)

[[]][Official documentation](https://www.libvirt.org/docs.html)

[[]][Package information](https://packages.gentoo.org/packages/app-emulation/libvirt)

[[]][GitLab](https://gitlab.com/libvirt/libvirt)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Libvirt "wikipedia:Libvirt")

[[]][Bugs (upstream)](https://libvirt.org/bugs.html)

[[]][virsh(1) man page](https://www.libvirt.org/manpages/virsh.html)

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/libvirt)

[virsh] is a CLI-based [virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") management toolkit, used to create, pause, shut down, and list domains.

[Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") is a C toolkit to interact with the virtualization capabilities of recent versions of Linux (and other OSes).

[Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") (and [virsh]) currently support [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU"), [LXC](https://wiki.gentoo.org/wiki/LXC "LXC"), [Xen](https://wiki.gentoo.org/wiki/Xen "Xen"), [KVM](https://wiki.gentoo.org/wiki/KVM "KVM"), [OpenVZ](https://wiki.gentoo.org/wiki/OpenVZ "OpenVZ"), [VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox") and [VMware](https://wiki.gentoo.org/wiki/VMware "VMware") ESX.

** Tip**\
For GUI-based management, use [virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager").

\

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [System user/group]](#System_user.2Fgroup)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Environment variables - Test]](#Environment_variables_-_Test)
    -   [[2.3] [Files]](#Files)
    -   [[2.4] [User permissions]](#User_permissions)
    -   [[2.5] [Service]](#Service)
        -   [[2.5.1] [libvirtd service - status by CLI]](#libvirtd_service_-_status_by_CLI)
        -   [[2.5.2] [libvirtd service - status by explicit channel]](#libvirtd_service_-_status_by_explicit_channel)
        -   [[2.5.3] [libvirtd service - status by environment variable]](#libvirtd_service_-_status_by_environment_variable)
        -   [[2.5.4] [libvirtd service - status by config file]](#libvirtd_service_-_status_by_config_file)
    -   [[2.6] [Networking]](#Networking)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [General info]](#General_info)
    -   [[3.2] [Checking domain]](#Checking_domain)
    -   [[3.3] [Checking networking]](#Checking_networking)
    -   [[3.4] [Checking storage pools]](#Checking_storage_pools)
    -   [[3.5] [List available commands]](#List_available_commands)
    -   [[3.6] [Invocation]](#Invocation)
-   [[4] [Removal]](#Removal)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

See [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") for installation of [virsh].

\

#### [][System user/group]

For non-root usage of [virsh], the user must be a member of the [libvirt] group, defined by [[[acct-group/libvirt]](https://packages.gentoo.org/packages/acct-group/libvirt)[]] and used by the [[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]] package.

** Tip**\
See [User/group permissions](https://wiki.gentoo.org/wiki/Libvirt#permissions "Libvirt") in [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") for adding a user to the **[libvirt]** group.

\

## [Configuration]

### [Environment variables]

Optional environment variables that are read and checked by the [virsh] command:

  ------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Optional environment variable name   Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           Type
  `LIBVIRT_AUTH_FILE`       Authentication, for libvirt clients (virsh, virt-manager) connecting to the [libvirtd] daemon. Contains authentication credentials for connecting to a libvirt daemon (like libvirtd or virtqemud) when using certain authentication mechanisms, particularly Polkit or SASL. Its file format is a simple INI containing a **[\[credentials\]]** section line followed by **[username=]** and **[password=]** key-value lines. If `LIBVIRT_AUTH_FILE` is explicitly set, libvirt uses that. If not set, libvirt checks [\$XDG_CONFIG_HOME/libvirt/auth.conf]; if `XDG_CONFIG_HOME` is unset, then libvirt checks [\$HOME/.config/libvirt/auth.conf]. SECURITY: The file should be readable only by the user.   file path
  `LIBVIRT_DEFAULT_URI`     Specify the default connection URI to a hypervisor or virtualization backend (like QEMU/KVM, Xen, LXC, etc.). It tells libvirt-based tools (like virsh, virt-manager, or libvirt API clients) which hypervisor and transport to connect to by default, when a URI is not explicitly given. Default for regular users is [qemu:///session]; for root, [qemu:///system]. See the [[[virt-admin(1)]](https://man.archlinux.org/man/virt-admin.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.                                                                                                                                                                                                    URI
  `LIBVIRT_LOG_FILTERS`     A **[component:level]** colon-pair, each separated by commas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         **[level]**s are **[error]**, **[warning]**, **[info]**, **[debug]**, **[trace]**. Some **[component]**s are **[qemu]**, **[network]**, **[storage]**, **[cpu]**, **[driver]**, **[interface]**, **[xml]**, **[domain]**, **[migration]**, **[security]**, **[host]**, **[api]**, **[config]**, **[event]**, and **[util]**
  `QEMU_AUDIO_DRV`          Audio driver to select.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               **[pa]**, **[none]**, **[alsa]**, **[coreaudio]**, **[jack]**, **[oss]**, **[pipewire]**, **[sdl]**, **[spice]** or **[wav]**
  `SDL_AUDIODRIVER`         SDL (Simple DirectMedia Layer) to control which audio backend is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                **[pipewire]**, **[pulseaudio]**, **[esd]**, **[alsa]**, **[jack]**, **[dsp]**, or **[arts]**
  `VIRTD_PATH`              Path in which to find the [libvirtd] executable; colon-separated directory spec(s). If not found or defined, fall back to `LIBVIRTD_PATH`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      colon-separated directory path(s)
  `LIBVIRTD_PATH`           Pathin in which to find the [libvirtd] executable; colon-separated directory spec(s). If `VIRTD_PATH` is not found nor defined, this variable is tried.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         colon-separated directory path(s)
  ------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Debugging-related environment variables:

  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------
  Debug environment variable name     Description                                                                                                                                               Type
  `LIBVIRT_DEBUG`          Sets the verbosity level of libvirt logging. Works in conjunction with `LIBVIRT_LOG_OUTPUTS` to specify how much detail is included in logs.   verbosity level: 0 (fewer messages) to 4 (most verbose)
  `LIBVIRT_LOG_OUTPUTS`    Controls where log messages go (stdout, stderr, file, etc.) and what gets logged.                                                                         file path
  `LIBVIRT_GNUTLS_DEBUG`   Enable GNUTLS debug, if defined.                                                                                                                          (none)
  `LIBVIRT_LIBSSH_DEBUG`   Enable LIBSSH debug, if defined; use `TRACE_LIBSSH=<level>` to define debug level.                                                                        (none)
  ----------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------

\
[systemd](https://wiki.gentoo.org/wiki/Systemd "Systemd") support:

  ----------------------------------- ------------------------------------------------------------------------------------------------------------ -------------------------
  systemd environment variable name   Description                                                                                                  Type
  `LISTEN_FDS`             Informs a service how many file descriptors have been passed to it by socket activation. For systemd only.   file descriptor ID
  `LISTEN_PID`             The PID of the process the file descriptors are for (should match your PID). For systemd only.               process ID
  `NOTIFY_SOCKET`          Inform systemd of its actual UNIX socket path for the client. For systemd only.                              Unix domain socket path
  ----------------------------------- ------------------------------------------------------------------------------------------------------------ -------------------------

\
Environment variables for [libvirt_leasehelper] during network setup:

  ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------
  libvirt_leasehelper environment variable name   Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       Type
  `DNSMASQ_CLIENT_ID`                  A custom DHCP client ID set by the VM\'s DHCP client, or a MAC address, depending on how the VM was configured. Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver.                                                                                                                                                                                        14-hex, 14-hex, colon-separated, or user-defined string
  `DNSMASQ_IAID`                       The 32-bit IAID provided by the DHCP IPv6 client. Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver.                                                                                                                                                                                                                                                      32-bit Decimal, or Hex (prefix, no-prefix, colon-separated)
  `DNSMASQ_INTERFACE`                  The bridge network interface name on which the lease event occurred. Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver.                                                                                                                                                                                                                                   network interface name
  `DNSMASQ_LEASE_EXPIRES`              Unix timestamp specifying when the lease will expire (or 0 if expired). Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver.                                                                                                                                                                                                                                UNIX timestamp (i.e., seconds since the epoch: Jan 1, 1970)
  `DNSMASQ_OLD_HOSTNAME`               Old hostname before the current lease change (as sent by client via DHCP option 12). Set by [dnsmasq] when a DHCP lease update causes a client\'s hostname to change. Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver. May be empty if previously not set.   hostname/DNS label (RFC1036/RFC1123)
  `DNSMASQ_SERVER_DUID`                Uniquely identifies a DHCPv6 server. Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver.                                                                                                                                                                                                                                                                   hostname (RFC3315)
  `DNSMASQ_SUPPLIED_HOSTNAME`          Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver.                                                                                                                                                                                                                                                                                                        hostname/DNS label (RFC1036/RFC1123)
  `VIR_BRIDGE_NAME`                    Contains the hostname explicitly supplied by the client during its DHCP request - typically via DHCPv4 option 12 (Host Name) or DHCPv6 option 39 (FQDN or Client FQDN). Different from `DNSMASQ_HOSTNAME`, which may include DNS-derived or static-host config values. Used by [libvirt_leaseshelper] with [dnsmasqd] during bridge driver.                      simple Linux bridge name
  ----------------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------------------------------------------------------

\
[VirtualBox](https://wiki.gentoo.org/wiki/VirtualBox "VirtualBox") support:

  -------------------------------------- ------------------------------------------------------------------------------------------------------ ------------------
  VirtualBox environment variable name   Description                                                                                            Type
  `DISPLAY`                   The X server display and screen to which graphical applications should be sent. For VirtualBox only.   X Display Offset
  `VBOX_APP_HOME`             For VirtualBox only.                                                                                   directory path
  -------------------------------------- ------------------------------------------------------------------------------------------------------ ------------------

\
Deprecated environment variables:

  ---------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------
  Deprecated environment variable name     Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             Type
  `LIBVIRT_ADMIN_DEFAULT_URI`   Administration; see [[[virt-admin(1)]](https://man.archlinux.org/man/virt-admin.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page. (Deprecated; use `LIBVIRT_DEFAULT_URI`.)   URI
  `VIRSH_DEFAULT_CONNECT_URI`              Administration; see [[[virsh(1)]](https://man.archlinux.org/man/virsh.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page. (Deprecated; use `LIBVIRT_DEFAULT_URI`.)                  URI
  ---------------------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------

\
Optional environment variables that are read and checked by the [libvirt.so] library linked by [libvirtd]:

+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| libvirt environment variable name      | Description                                                                                                                                                                                                                                                                                                                       | Type                              |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `LC_ALL`                    | to force all locale settings (like language, number formatting, collation, etc.) for programs running in the environment.                                                                                                                                                                                                         | locale name                       |
|                                        |                                                                                                                                                                                                                                                                                                                                   |                                   |
|                                        | Overrides all other locale-related variables such as `LANG`, `LC_CTYPE`, `LC_TIME`, `LC_NUMERIC`, `LC_MESSAGES`, etc.                                                                                                                                                      |                                   |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `LD_PRELOAD `               | Overrides library search paths; useful for debugging alternative [GTK](https://wiki.gentoo.org/wiki/GTK "GTK") or [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") builds. Useful for debugging by swapping out the [malloc] function. | colon-separated directory path(s) |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `LD_LIBRARY_PATH`           | Overrides library search paths; useful for debugging alternative GTK or QEMU builds.                                                                                                                                                                                                                                              | colon-separated directory paths   |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `DYLD_INSERT_LIBRARIES`     | Works similarly to `LD_PRELOAD` but for macOS platforms. SIP blocks this for macOS system binaries. Only works with `DYLD_FORCE_FLAT_NAMESPACE=1` setting.                                                                                                                                                  | colon-separated directory path(s) |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `DYLD_FORCE_FLAT_NAMESPACE` | macOS has a two-level-deep namespace. Set to `1` to flatten. May cause symbol collisions.                                                                                                                                                                                                                                         | digit                             |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `USER`                      | Login username of the current user. Often used by shell scripts.                                                                                                                                                                                                                                                                  | username                          |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `LOGNAME`                   | Used by system (e.g., [login], [at]).                                                                                                       | username                          |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+
| `TMPDIR`                    | Temporary directory where programs should write temporary files.                                                                                                                                                                                                                                                                  | directory path                    |
+----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+

### [Environment variables - Test]

A list of all testing environment variables that are read and checked by the [virsh] command:

-   `LIBVIRT_AUTOSTART` - If set to **[0]**, disables auto-launching [libvirtd], but only if there are any unprivileged hypervisor drivers required.
-   `LIBVIRT_DIR_OVERRIDE` - Ensure that any third-party apps using [libvirt.so] from the build tree get files resolved to the build/source tree too. Typically useful for language bindings running tests against non-installed libvirt.

### [Files]

Whenever a domain starts, [virsh] checks for the [domain](https://wiki.gentoo.org/wiki/Libvirt/domain "Libvirt/domain") XML file in each of the following paths:

-   System mode: [/etc/libvirt/qemu/]
-   User mode: [\$HOME/.config/libvirt/qemu/]

\
Files that are read by the host-side OS [virsh] command:

-   [/etc/libvirt/hooks/]
-   [/etc/libvirt/libvirt-admin.conf]
-   [/etc/libvirt/libvirt.conf]
-   [/etc/libvirt/libvirtd.conf]
-   [/etc/libvirt/libxl.conf]
-   [/etc/libvirt/libxl-lockd.conf]
-   [/etc/libvirt/libxl-sanlock.conf]
-   [/etc/libvirt/lxc.conf]
-   [/etc/libvirt/nwfilter/]
-   [/etc/libvirt/secrets/]
-   [/etc/libvirt/storage/]
-   [/etc/libvirt/virtlockd.conf]
-   [/etc/libvirt/virtlogd.conf]

<!-- -->

-   [/proc/cgroups]
-   [/proc/cpuinfo]
-   [/proc/modules]
-   [/proc/mounts]
-   [/proc/net/dev]
-   [/proc/stat]
-   [/proc/sys/ipv4/ip_forward]
-   [/proc/sys/ipv6/conf/all/forwarding]
-   [/proc/sys/ipv6/conf/%s/%s]
-   [/proc/vz/vestat] - Only with [openvz]
-   [/sys/class/fc_host/host0]
-   [/sys/class/fc_remote_ports]
-   [/sys/class/scsi_host]
-   [/sys/devices/system]
-   [/sys/devices/system/%s/cpu/online]
-   [/sys/devices/system/cpu/online]
-   [/sys/devices/system/node/node0/access1]
-   [/sys/devices/system/node/node0/meminfo]
-   [/sys/devices/system/node/node0/memory_side_cache]
-   [/sys/devices/system/node/online]
-   [/sys/fs/resctrl]
-   [/sys/fs/resctrl/info/%s/num_closids]
-   [/sys/fs/resctrl/%s/schemata]
-   [/sys/fs/resctrl/info/%s/min_cbm_bits]
-   [/sys/fs/resctrl/info/L3_MON]
-   [/sys/fs/resctrl/info/L3_MON/num_rmids]
-   [/sys/fs/resctrl/info/MB/bandwidth_gran]
-   [/sys/fs/resctrl/info/MB/min_bandwidth]
-   [/sys/fs/resctrl/info/MB/num_closids]
-   [/sys/kernel/mm/ksm]
-   [/sys/kernel/mm/transparent_hugepage/hpage_pmd_size]
-   [/var/lib/libvirt/boot]
-   [/var/lib/libvirt/dnsmasq]
-   [/var/lib/libvirt/images]
-   [/var/lib/libvirt/sanlock]

\

### [User permissions]

To use [virsh] as a non-root user, ensure each user has been added to the [libvirt] group:

`host-root#``gpasswd -a <user> libvirt`

See [libvirt configuration](https://wiki.gentoo.org/wiki/Libvirt#Configuration "Libvirt") for more setup enabling the user to use the [virsh] command.

\

### [Service]

[virsh] requires the [libvirtd] daemon to be started. See [libvirt service](https://wiki.gentoo.org/wiki/Libvirt#Service "Libvirt") for more commands.

Three quick command-line tests to check if the daemon is up and running:

\

#### [libvirtd service - status by CLI]

`host-root#``virsh list --all`

    virsh list --all
     Id   Name       State
    ---------------------------
     16   gentoo     running
     -    gentoo2    shut off

\

#### [libvirtd service - status by explicit channel]

`host-root#``virsh -c qemu:///system list --all`

    virsh -c qemu:///system list --all
     Id   Name       State
    ---------------------------
     16   gentoo     running
     -    gentoo2    shut off

\

#### [libvirtd service - status by environment variable]

By environment variable, run:

[CODE] **Use environment variable to define connect type**

    export VIRSH_DEFAULT_CONNECT_URI=qemu:///system

then run:

`host-root#``virsh list --all`

    virsh  list --all
     Id   Name       State
    ---------------------------
     16   gentoo     running
     -    gentoo2    shut off

\

#### [libvirtd service - status by config file]

The libvirt configuration file is in the following directory order:

1\. [/etc/libvirt/libvirt.conf]

** Note**\
There is no \$HOME nor user-specific [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") configuration file.

[CODE] **Libvirt configuration settings**

    #
    # This can be used to setup URI aliases for frequently
    # used connection URIs. Aliases may contain only the
    # characters  a-Z, 0-9, _, -.
    #
    # Following the '=' may be any valid libvirt connection
    # URI, including arbitrary parameters

    #uri_aliases = [
    #  "hail=qemu+ssh://root@hail.cloud.example.com/system",
    #  "sleet=qemu+ssh://root@sleet.cloud.example.com/system",
    #]

    #
    # These can be used in cases when no URI is supplied by the application
    # (@uri_default also prevents probing of the hypervisor driver).
    #
    #uri_default = "qemu:///system"

Use **[\@uri_default]** if using this configuration file is copied as-is across multiple hosts; no probe for hypervisor driver done here, but if it does exist, use them.

\

### [Networking]

The [virsh] communicates with [libvirtd](https://wiki.gentoo.org/wiki/Libvirt/libvirtd "Libvirt/libvirtd") daemon through:

-   UNIX domain socket to communicate with a local [libvirtd] domain controller; or
-   [inet] network socket to communicate with a remote [libvirtd] domain controller/host.

\
The syntax of the libvirt connect URI is:

       transport+protocol:///path
       transport+protocol://[user@]hostname[:port]/[path|target]

\
See [URI in Libvirt](https://wiki.gentoo.org/wiki/Libvirt#URI "Libvirt") for more detailed breakdowns of Connect Type URI.

\

## [Usage]

Users of [Bash](https://wiki.gentoo.org/wiki/Bash "Bash") can access auto-complete of [virsh] options by pressing [Tab] as needed.

[virsh] selects the connection URI based on the following order of priority:

1.  command line option: `-c URI`, as described in [the URI specification](https://wiki.gentoo.org/wiki/Libvirt#Connect_types_-_Default "Libvirt"). Typically [qemu:///session], to avoid the system default.
2.  environment variable: `LIBVIRT_DEFAULT_URI`.
3.  user config file: [\$XDG_CONFIG_HOME/libvirt/libvirt.conf], via the `uri_default = "qemu:///system"` config line.
4.  user config file: [\$HOME/.config/libvirt/libvirt.conf], via the `uri_default = "qemu:///system"` config line.
5.  system config file: [/etc/libvirt/libvirt.conf], via the `uri_default = "qemu:///system"` config line.
6.  compiled-in default: usually `qemu:///system`.

### [General info]

All guest virtual machines and containers managed by the [libvirt] API can be listed with:

`host-root#``virsh nodeinfo`

    CPU model:           x86_64
    CPU(s):              4
    CPU frequency:       1600 MHz
    CPU socket(s):       1
    Core(s) per socket:  4
    Thread(s) per core:  1
    NUMA cell(s):        1
    Memory size:         16360964 KiB

[virsh] can check communication with the [libvirtd] daemon via a Unix socket by running:

`host-root#``virsh sysinfo`

    <sysinfo type='smbios'>
      <bios>
        <entry name='vendor'>Dell Inc.</entry>
        <entry name='version'>A22</entry>
        <entry name='date'>11/29/2018</entry>
        <entry name='release'>4.6</entry>
      </bios>
      <system>
        <entry name='manufacturer'>Dell Inc.</entry>
        <entry name='product'>OptiPlex 3010</entry>
        <entry name='version'>01</entry>
        <entry name='serial'>JRJ0SW1</entry>
        <entry name='uuid'>4c4c4544-0052-4a10-8030-cac04f535731</entry>
        <entry name='sku'>OptiPlex 3010</entry>
        <entry name='family'>Not Specified</entry>
      </system>
      <baseBoard>
        <entry name='manufacturer'>Dell Inc.</entry>
        <entry name='product'>042P49</entry>
        <entry name='version'>A00</entry>
        <entry name='serial'>/JRJ0SW1/CN701632BD05R5/</entry>
        <entry name='asset'>Not Specified</entry>
        <entry name='location'>Not Specified</entry>
      </baseBoard>
      <chassis>
        <entry name='manufacturer'>Dell Inc.</entry>
        <entry name='version'>Not Specified</entry>
        <entry name='serial'>JRJ0SW1</entry>
        <entry name='asset'>Not Specified</entry>
        <entry name='sku'>To be filled by O.E.M.</entry>
      </chassis>

        <entry name='socket_destination'>CPU 1</entry>
        <entry name='type'>Central Processor</entry>
        <entry name='family'>Core i5</entry>
        <entry name='manufacturer'>Intel(R) Corporation</entry>
        <entry name='signature'>Type 0, Family 6, Model 58, Stepping 9</entry>
        <entry name='version'>Intel(R) Core(TM) i5-3470 CPU @ 3.20GHz</entry>
        <entry name='external_clock'>100 MHz</entry>
        <entry name='max_speed'>3200 MHz</entry>
        <entry name='status'>Populated, Enabled</entry>
        <entry name='serial_number'>Not Specified</entry>
        <entry name='part_number'>Fill By OEM</entry>
      </processor>
      <memory_device>
        <entry name='size'>8 GB</entry>
        <entry name='form_factor'>DIMM</entry>
        <entry name='locator'>DIMM1</entry>
        <entry name='bank_locator'>Not Specified</entry>
        <entry name='type'>DDR3</entry>
        <entry name='type_detail'>Synchronous</entry>
        <entry name='speed'>1600 MT/s</entry>
        <entry name='manufacturer'>8C26</entry>
        <entry name='serial_number'>00000000</entry>
        <entry name='part_number'>TIMETEC-UD3-1600</entry>
      </memory_device>
      <memory_device>
        <entry name='size'>8 GB</entry>
        <entry name='form_factor'>DIMM</entry>
        <entry name='locator'>DIMM2</entry>
        <entry name='bank_locator'>Not Specified</entry>
        <entry name='type'>DDR3</entry>
        <entry name='type_detail'>Synchronous</entry>
        <entry name='speed'>1600 MT/s</entry>
        <entry name='manufacturer'>8C26</entry>
        <entry name='serial_number'>00000000</entry>
        <entry name='part_number'>TIMETEC-UD3-1600</entry>
      </memory_device>
      <oemStrings>
        <entry>Dell System</entry>
        <entry>1[0585]</entry>
        <entry>3[1.0]
    </entry>
        <entry>12[www.dell.com]
    </entry>
        <entry>14[1]</entry>
        <entry>15[11]</entry>
      </oemStrings>
    </sysinfo>

### [Checking domain]

To list all the guest VMs and containers maintained by [virt-manager], run:

`host-root#``virsh list --all`

     Id   Name                  State
    --------------------------------------
     1    gentoo                running

### [Checking networking]

All libvirt-managed virtual networks can be listed with:

`host-root#``virsh net-list --all`

     Name        State    Autostart   Persistent
    ----------------------------------------------
     default     active   yes         yes

### [Checking storage pools]

Storage pools maintained by [virt-manager] can be checked by running:

`host-root#``virsh pool-list --all`

     Name        State    Autostart
    ---------------------------------
     default     active   yes
     Downloads   active   yes

\

### [List available commands]

The group of [list]-related options can be obtained via:

`host$``virsh help | grep list`

        get-user-sshkeys               list authorized SSH keys for given user (via agent)
        domblklist                     list all domain blocks
        domiflist                      list all domain virtual interfaces
        list                           list domains
        checkpoint-list                List checkpoints for a domain
        iface-list                     list physical host interfaces
        nwfilter-list                  list network filters
        nwfilter-binding-list          list network filter bindings
        net-list                       list networks
        net-port-list                  list network ports
        nodedev-list                   enumerate devices on this host
        secret-list                    list secrets
        snapshot-list                  List snapshots for a domain
        pool-list                      list pools
        vol-list                       list vols

Add the `--help` option for more detailed options specific to a particular command, e.g. the [iface-list] command:

`host$``virsh iface-list --help`

      NAME
        iface-list - list physical host interfaces

      SYNOPSIS
        iface-list [--inactive] [--all]

      DESCRIPTION
        Returns list of physical host interfaces.

      OPTIONS
        --inactive       list inactive interfaces
        --all            list inactive & active interfaces

\

### [Invocation]

`host$``virsh --help`

    # virsh --help

    virsh [options]... [<command_string>]
    virsh [options]... <command> [args...]

      options:
        -c | --connect=URI      hypervisor connection URI
        -d | --debug=NUM        debug level [0-4]
        -e | --escape <char>    set escape sequence for console
        -h | --help             this help
        -k | --keepalive-interval=NUM
                                keepalive interval in seconds, 0 for disable
        -K | --keepalive-count=NUM
                                number of possible missed keepalive messages
        -l | --log=FILE         output logging to file
        -q | --quiet            quiet mode
        -r | --readonly         connect readonly
        -t | --timing           print timing information
        -v                      short version
        -V                      long version
             --version[=TYPE]   version, TYPE is short or long (default short)
      commands (non interactive mode):

     Domain Management (help keyword 'domain')
        attach-device                  attach device from an XML file
        attach-disk                    attach disk device
        attach-interface               attach network interface
        autostart                      autostart a domain
        blkdeviotune                   Set or query a block device I/O tuning parameters.
        blkiotune                      Get or set blkio parameters
        blockcommit                    Start a block commit operation.
        blockcopy                      Start a block copy operation.
        blockjob                       Manage active block operations
        blockpull                      Populate a disk from its backing image.
        blockresize                    Resize block device of domain.
        change-media                   Change media of CD or floppy drive
        console                        connect to the guest console
        cpu-stats                      show domain cpu statistics
        create                         create a domain from an XML file
        define                         define (but don't start) a domain from an XML file
        desc                           show or set domain's description or title
        destroy                        destroy (stop) a domain
        detach-device                  detach device from an XML file
        detach-device-alias            detach device from an alias
        detach-disk                    detach disk device
        detach-interface               detach network interface
        domdisplay                     domain display connection URI
        domfsfreeze                    Freeze domain's mounted filesystems.
        domfsthaw                      Thaw domain's mounted filesystems.
        domfsinfo                      Get information of domain's mounted filesystems.
        domfstrim                      Invoke fstrim on domain's mounted filesystems.
        domhostname                    print the domain's hostname
        domid                          convert a domain name or UUID to domain id
        domif-setlink                  set link state of a virtual interface
        domiftune                      get/set parameters of a virtual interface
        domjobabort                    abort active domain job
        domjobinfo                     domain job information
        domname                        convert a domain id or UUID to domain name
        domrename                      rename a domain
        dompmsuspend                   suspend a domain gracefully using power management functions
        dompmwakeup                    wakeup a domain from pmsuspended state
        domuuid                        convert a domain name or id to domain UUID
        domxml-from-native             Convert native config to domain XML
        domxml-to-native               Convert domain XML to native config
        dump                           dump the core of a domain to a file for analysis
        dumpxml                        domain information in XML
        edit                           edit XML configuration for a domain
        event                          Domain Events
        get-user-sshkeys               list authorized SSH keys for given user (via agent)
        inject-nmi                     Inject NMI to the guest
        iothreadinfo                   view domain IOThreads
        iothreadpin                    control domain IOThread affinity
        iothreadadd                    add an IOThread to the guest domain
        iothreadset                    modifies an existing IOThread of the guest domain
        iothreaddel                    delete an IOThread from the guest domain
        send-key                       Send keycodes to the guest
        send-process-signal            Send signals to processes
        lxc-enter-namespace            LXC Guest Enter Namespace
        managedsave                    managed save of a domain state
        managedsave-remove             Remove managed save of a domain
        managedsave-edit               edit XML for a domain's managed save state file
        managedsave-dumpxml            Domain information of managed save state file in XML
        managedsave-define             redefine the XML for a domain's managed save state file
        memtune                        Get or set memory parameters
        perf                           Get or set perf event
        metadata                       show or set domain's custom XML metadata
        migrate                        migrate domain to another host
        migrate-setmaxdowntime         set maximum tolerable downtime
        migrate-getmaxdowntime         get maximum tolerable downtime
        migrate-compcache              get/set compression cache size
        migrate-setspeed               Set the maximum migration bandwidth
        migrate-getspeed               Get the maximum migration bandwidth
        migrate-postcopy               Switch running migration from pre-copy to post-copy
        numatune                       Get or set numa parameters
        qemu-attach                    QEMU Attach
        qemu-monitor-command           QEMU Monitor Command
        qemu-monitor-event             QEMU Monitor Events
        qemu-agent-command             QEMU Guest Agent Command
        guest-agent-timeout            Set the guest agent timeout
        reboot                         reboot a domain
        reset                          reset a domain
        restore                        restore a domain from a saved state in a file
        resume                         resume a domain
        save                           save a domain state to a file
        save-image-define              redefine the XML for a domain's saved state file
        save-image-dumpxml             saved state domain information in XML
        save-image-edit                edit XML for a domain's saved state file
        schedinfo                      show/set scheduler parameters
        screenshot                     take a screenshot of a current domain console and store it into a file
        set-lifecycle-action           change lifecycle actions
        set-user-sshkeys               manipulate authorized SSH keys file for given user (via agent)
        set-user-password              set the user password inside the domain
        setmaxmem                      change maximum memory limit
        setmem                         change memory allocation
        setvcpus                       change number of virtual CPUs
        shutdown                       gracefully shutdown a domain
        start                          start a (previously defined) inactive domain
        suspend                        suspend a domain
        ttyconsole                     tty console
        undefine                       undefine a domain
        update-device                  update device from an XML file
        vcpucount                      domain vcpu counts
        vcpuinfo                       detailed domain vcpu information
        vcpupin                        control or query domain vcpu affinity
        emulatorpin                    control or query domain emulator affinity
        vncdisplay                     vnc display
        guestvcpus                     query or modify state of vcpu in the guest (via agent)
        setvcpu                        attach/detach vcpu or groups of threads
        domblkthreshold                set the threshold for block-threshold event for a given block device or it's backing chain element
        guestinfo                      query information about the guest (via agent)

     Domain Monitoring (help keyword 'monitor')
        domblkerror                    Show errors on block devices
        domblkinfo                     domain block device size information
        domblklist                     list all domain blocks
        domblkstat                     get device block stats for a domain
        domcontrol                     domain control interface state
        domif-getlink                  get link state of a virtual interface
        domifaddr                      Get network interfaces' addresses for a running domain
        domiflist                      list all domain virtual interfaces
        domifstat                      get network interface stats for a domain
        dominfo                        domain information
        dommemstat                     get memory statistics for a domain
        domstate                       domain state
        domstats                       get statistics about one or multiple domains
        domtime                        domain time
        list                           list domains

     Host and Hypervisor (help keyword 'host')
        allocpages                     Manipulate pages pool size
        capabilities                   capabilities
        cpu-baseline                   compute baseline CPU
        cpu-compare                    compare host CPU with a CPU described by an XML file
        cpu-models                     CPU models
        domcapabilities                domain capabilities
        freecell                       NUMA free memory
        freepages                      NUMA free pages
        hostname                       print the hypervisor hostname
        hypervisor-cpu-baseline        compute baseline CPU usable by a specific hypervisor
        hypervisor-cpu-compare         compare a CPU with the CPU created by a hypervisor on the host
        maxvcpus                       connection vcpu maximum
        node-memory-tune               Get or set node memory parameters
        nodecpumap                     node cpu map
        nodecpustats                   Prints cpu stats of the node.
        nodeinfo                       node information
        nodememstats                   Prints memory stats of the node.
        nodesuspend                    suspend the host node for a given time duration
        sysinfo                        print the hypervisor sysinfo
        uri                            print the hypervisor canonical URI
        version                        show version

     Checkpoint (help keyword 'checkpoint')
        checkpoint-create              Create a checkpoint from XML
        checkpoint-create-as           Create a checkpoint from a set of args
        checkpoint-delete              Delete a domain checkpoint
        checkpoint-dumpxml             Dump XML for a domain checkpoint
        checkpoint-edit                edit XML for a checkpoint
        checkpoint-info                checkpoint information
        checkpoint-list                List checkpoints for a domain
        checkpoint-parent              Get the name of the parent of a checkpoint

     Interface (help keyword 'interface')
        iface-begin                    create a snapshot of current interfaces settings, which can be later committed (iface-commit) or restored (iface-rollback)
        iface-bridge                   create a bridge device and attach an existing network device to it
        iface-commit                   commit changes made since iface-begin and free restore point
        iface-define                   define an inactive persistent physical host interface or modify an existing persistent one from an XML file
        iface-destroy                  destroy a physical host interface (disable it / "if-down")
        iface-dumpxml                  interface information in XML
        iface-edit                     edit XML configuration for a physical host interface
        iface-list                     list physical host interfaces
        iface-mac                      convert an interface name to interface MAC address
        iface-name                     convert an interface MAC address to interface name
        iface-rollback                 rollback to previous saved configuration created via iface-begin
        iface-start                    start a physical host interface (enable it / "if-up")
        iface-unbridge                 undefine a bridge device after detaching its device(s)
        iface-undefine                 undefine a physical host interface (remove it from configuration)

     Network Filter (help keyword 'filter')
        nwfilter-define                define or update a network filter from an XML file
        nwfilter-dumpxml               network filter information in XML
        nwfilter-edit                  edit XML configuration for a network filter
        nwfilter-list                  list network filters
        nwfilter-undefine              undefine a network filter
        nwfilter-binding-create        create a network filter binding from an XML file
        nwfilter-binding-delete        delete a network filter binding
        nwfilter-binding-dumpxml       network filter information in XML
        nwfilter-binding-list          list network filter bindings

     Networking (help keyword 'network')
        net-autostart                  autostart a network
        net-create                     create a network from an XML file
        net-define                     define an inactive persistent virtual network or modify an existing persistent one from an XML file
        net-destroy                    destroy (stop) a network
        net-dhcp-leases                print lease info for a given network
        net-dumpxml                    network information in XML
        net-edit                       edit XML configuration for a network
        net-event                      Network Events
        net-info                       network information
        net-list                       list networks
        net-name                       convert a network UUID to network name
        net-start                      start a (previously defined) inactive network
        net-undefine                   undefine a persistent network
        net-update                     update parts of an existing network's configuration
        net-uuid                       convert a network name to network UUID
        net-port-list                  list network ports
        net-port-create                create a network port from an XML file
        net-port-dumpxml               network port information in XML
        net-port-delete                delete the specified network port

     Node Device (help keyword 'nodedev')
        nodedev-create                 create a device defined by an XML file on the node
        nodedev-destroy                destroy (stop) a device on the node
        nodedev-detach                 detach node device from its device driver
        nodedev-dumpxml                node device details in XML
        nodedev-list                   enumerate devices on this host
        nodedev-reattach               reattach node device to its device driver
        nodedev-reset                  reset node device
        nodedev-event                  Node Device Events

     Secret (help keyword 'secret')
        secret-define                  define or modify a secret from an XML file
        secret-dumpxml                 secret attributes in XML
        secret-event                   Secret Events
        secret-get-value               Output a secret value
        secret-list                    list secrets
        secret-set-value               set a secret value
        secret-undefine                undefine a secret

     Snapshot (help keyword 'snapshot')
        snapshot-create                Create a snapshot from XML
        snapshot-create-as             Create a snapshot from a set of args
        snapshot-current               Get or set the current snapshot
        snapshot-delete                Delete a domain snapshot
        snapshot-dumpxml               Dump XML for a domain snapshot
        snapshot-edit                  edit XML for a snapshot
        snapshot-info                  snapshot information
        snapshot-list                  List snapshots for a domain
        snapshot-parent                Get the name of the parent of a snapshot
        snapshot-revert                Revert a domain to a snapshot

     Backup (help keyword 'backup')
        backup-begin                   Start a disk backup of a live domain
        backup-dumpxml                 Dump XML for an ongoing domain block backup job

     Storage Pool (help keyword 'pool')
        find-storage-pool-sources-as   find potential storage pool sources
        find-storage-pool-sources      discover potential storage pool sources
        pool-autostart                 autostart a pool
        pool-build                     build a pool
        pool-create-as                 create a pool from a set of args
        pool-create                    create a pool from an XML file
        pool-define-as                 define a pool from a set of args
        pool-define                    define an inactive persistent storage pool or modify an existing persistent one from an XML file
        pool-delete                    delete a pool
        pool-destroy                   destroy (stop) a pool
        pool-dumpxml                   pool information in XML
        pool-edit                      edit XML configuration for a storage pool
        pool-info                      storage pool information
        pool-list                      list pools
        pool-name                      convert a pool UUID to pool name
        pool-refresh                   refresh a pool
        pool-start                     start a (previously defined) inactive pool
        pool-undefine                  undefine an inactive pool
        pool-uuid                      convert a pool name to pool UUID
        pool-event                     Storage Pool Events
        pool-capabilities              storage pool capabilities

     Storage Volume (help keyword 'volume')
        vol-clone                      clone a volume.
        vol-create-as                  create a volume from a set of args
        vol-create                     create a vol from an XML file
        vol-create-from                create a vol, using another volume as input
        vol-delete                     delete a vol
        vol-download                   download volume contents to a file
        vol-dumpxml                    vol information in XML
        vol-info                       storage vol information
        vol-key                        returns the volume key for a given volume name or path
        vol-list                       list vols
        vol-name                       returns the volume name for a given volume key or path
        vol-path                       returns the volume path for a given volume name or key
        vol-pool                       returns the storage pool for a given volume key or path
        vol-resize                     resize a vol
        vol-upload                     upload file contents to a volume
        vol-wipe                       wipe a vol

     Virsh itself (help keyword 'virsh')
        cd                             change the current directory
        echo                           echo arguments
        exit                           quit this interactive terminal
        help                           print help
        pwd                            print the current directory
        quit                           quit this interactive terminal
        connect                        (re)connect to hypervisor

      (specify help <group> for details about the commands in the group)

      (specify help <command> for details about the command)

## [Removal]

To remove the [[[app-emulation/libvirt]](https://packages.gentoo.org/packages/app-emulation/libvirt)[]] package (toolkit, library, and utilities), run:

`root `[`#`]`emerge --ask --depclean --verbose app-emulation/libvirt`

## [See also]

-   [Virtualization](https://wiki.gentoo.org/wiki/Virtualization "Virtualization") --- the concept and technique that permits running software in an environment separate from a computer operating system.
-   [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") --- a generic, open-source hardware emulator and virtualization suite.
-   [QEMU/Front-ends](https://wiki.gentoo.org/wiki/QEMU/Front-ends "QEMU/Front-ends") --- facilitate VM management and use

<!-- -->

-   [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") --- a virtualization management toolkit
-   [Libvirt/QEMU_networking](https://wiki.gentoo.org/wiki/Libvirt/QEMU_networking "Libvirt/QEMU networking") --- details the setup of Gentoo networking by [Libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") for use by guest containers and [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU")-based virtual machines.
-   [Libvirt/QEMU_guest](https://wiki.gentoo.org/wiki/Libvirt/QEMU_guest "Libvirt/QEMU guest") --- creation of a guest domain (virtual machine, VM), running inside a QEMU hypervisor, using tools found in [[[libvirt]](https://packages.gentoo.org/packages/libvirt)[]] package.

<!-- -->

-   [Virt-manager](https://wiki.gentoo.org/wiki/Virt-manager "Virt-manager") --- lightweight GUI application designed for managing virtual machines and containers via the [libvirt](https://wiki.gentoo.org/wiki/Libvirt "Libvirt") API.
-   [Virt-manager/QEMU_guest](https://wiki.gentoo.org/wiki/Virt-manager/QEMU_guest "Virt-manager/QEMU guest") --- creation of a guest virtual machine (VM) running inside a QEMU hypervisor using just the [virt-manager] GUI tool.

<!-- -->

-   [QEMU/Linux guest](https://wiki.gentoo.org/wiki/QEMU/Linux_guest "QEMU/Linux guest") --- describes the setup of a Gentoo Linux guest in [QEMU](https://wiki.gentoo.org/wiki/QEMU "QEMU") using Gentoo bootable media.

\

## [External resources]

-   [Red Hat Virtualization Network Configuration](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/5/html/virtualization/chap-virtualization-network_configuration)