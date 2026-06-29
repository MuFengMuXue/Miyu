This page contains [[changes](https://wiki.gentoo.org/index.php?title=Distcc&oldid=1407189&diff=1431645)] which are not marked for translation.

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Distcc&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Distcc/de "Distcc (74% translated)")
-   [English]
-   [Türkçe](https://wiki.gentoo.org/wiki/Distcc/tr "Distcc (10% translated)")
-   [español](https://wiki.gentoo.org/wiki/Distcc/es "Distcc (76% translated)")
-   [français](https://wiki.gentoo.org/wiki/Distcc/fr "Distcc (55% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/Distcc/it "Distcc (16% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Distcc/hu "distcc (90% translated)")
-   [polski](https://wiki.gentoo.org/wiki/Distcc/pl "Distcc (7% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Distcc/ru "Distcc (75% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Distcc/zh-cn "Distcc (32% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Distcc/ja "Distcc (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Distcc/ko "Distcc (50% translated)")

**Resources**

[[]][Home](https://github.com/distcc/distcc)

[[]][Package information](https://packages.gentoo.org/packages/sys-devel/distcc)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Distcc "wikipedia:Distcc")

[[]]This article has some todo items:\

-   Extract content relating to Portage to [Portage with Distcc](https://wiki.gentoo.org/index.php?title=Portage_with_Distcc&action=edit&redlink=1 "Portage with Distcc (page does not exist)"), removing references to pump mode, since [distcc-pump] was removed in [[[bug #702146]](https://bugs.gentoo.org/show_bug.cgi?id=702146)[]]. Use the [talk page](https://wiki.gentoo.org/wiki/Talk:Distcc "Talk:Distcc") to propose a different name.

** Warning**\
Before reading this article the user should be asking if distcc is the right tool for the task at hand. In nearly all cases distcc is the slowest way to offload compiling as linking still happens locally and distcc adds many compile time issues. The general rules is nearly always that the user wants to set up a binary host using [Chrooting](https://wiki.gentoo.org/wiki/Binary_package_guide#Chrooting "Binary package guide") or [Building for other architectures](https://wiki.gentoo.org/wiki/Binary_package_guide#Building_for_other_architectures "Binary package guide"). Feel free to ask in [[#gentoo](ircs://irc.libera.chat/#gentoo)] ([[webchat](https://web.libera.chat/#gentoo)]) with the system requirements and a short explanation as to why you think distcc might be the better choice for the usage case if unsure.

**Distcc** is a program designed to distribute compiling tasks across a network to participating hosts.

Distcc comprises a server, [distccd], and a client program, [distcc]. Distcc can work transparently with [ccache](https://wiki.gentoo.org/wiki/Ccache "Ccache"), [Portage](https://wiki.gentoo.org/wiki/Portage "Portage"), and Automake with a small amount of setup.

When planning on using [distcc] to help bootstrap a Gentoo installation, make sure to read [Using distcc to bootstrap](https://wiki.gentoo.org/wiki/Distcc#To_bootstrap "Distcc").

If using hosts to run distcc that are of a different architecture, or run a different toolchain, see [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling").

** Note**\
Distcc can introduce compile-time issues, like bug [[[bug #691544]](https://bugs.gentoo.org/show_bug.cgi?id=691544)[]], so the first troubleshooting step when encountering such issues should be to disable distcc to see if it solves it.

** Tip**\
Using a second, faster, machine to build binary packages and [setting up a binary package host](https://wiki.gentoo.org/wiki/Binary_package_guide#Setting_up_a_binary_package_host "Binary package guide") can advantageously replace some use cases of distcc. It may be easier to set up and will cover all compilers and build systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Requirements across all hosts]](#Requirements_across_all_hosts)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service]](#Service)
        -   [[2.1.1] [OpenRC]](#OpenRC)
        -   [[2.1.2] [systemd]](#systemd)
    -   [[2.2] [Specifying participating hosts]](#Specifying_participating_hosts)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [With Portage]](#With_Portage)
        -   [[3.1.1] [CFLAGS and CXXFLAGS]](#CFLAGS_and_CXXFLAGS)
    -   [[3.2] [With automake]](#With_automake)
    -   [[3.3] [With ccache]](#With_ccache)
        -   [[3.3.1] [Configure distccd]](#Configure_distccd)
        -   [[3.3.2] [Configure ccache]](#Configure_ccache)
        -   [[3.3.3] [Configure portage]](#Configure_portage)
        -   [[3.3.4] [Testing distcc with ccache manually]](#Testing_distcc_with_ccache_manually)
            -   [[3.3.4.1] [Remote]](#Remote)
            -   [[3.3.4.2] [Client]](#Client)
        -   [[3.3.5] [Testing distcc with ccache using emerge]](#Testing_distcc_with_ccache_using_emerge)
        -   [[3.3.6] [Future usage]](#Future_usage)
    -   [[3.4] [To bootstrap]](#To_bootstrap)
        -   [[3.4.1] [Step 1: Configure Portage]](#Step_1:_Configure_Portage)
        -   [[3.4.2] [Step 2: Getting distcc]](#Step_2:_Getting_distcc)
        -   [[3.4.3] [Step 3: Setting up distcc]](#Step_3:_Setting_up_distcc)
    -   [[3.5] [Extras]](#Extras)
    -   [[3.6] [Monitoring utilities]](#Monitoring_utilities)
    -   [[3.7] [SSH for communication]](#SSH_for_communication)
        -   [[3.7.1] [Reverse SSH]](#Reverse_SSH)
    -   [[3.8] [Testing]](#Testing)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [ERROR: failed to open /var/log/distccd.log]](#ERROR:_failed_to_open_.2Fvar.2Flog.2Fdistccd.log)
    -   [[4.2] [Some packages do not use distcc]](#Some_packages_do_not_use_distcc)
    -   [[4.3] [Mixed GCC versions]](#Mixed_GCC_versions)
    -   [[4.4] [-march=native]](#-march.3Dnative)
    -   [[4.5] [Get more output from emerge logs]](#Get_more_output_from_emerge_logs)
    -   [[4.6] [Failed to create directory /dev/null/.cache/ccache/tmp: Not a directory]](#Failed_to_create_directory_.2Fdev.2Fnull.2F.cache.2Fccache.2Ftmp:_Not_a_directory)
    -   [[4.7] [Portage build failing with errors that are apparently not connected with distcc at all]](#Portage_build_failing_with_errors_that_are_apparently_not_connected_with_distcc_at_all)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [Installation]

Before configuring [distcc], let\'s first look into the installation of the [[[sys-devel/distcc]](https://packages.gentoo.org/packages/sys-devel/distcc)[]] package on all hosts.

### [Requirements across all hosts]

In order to use [distcc], all of the computers on the network need to have the same GCC versions. For example, mixing 3.3.x (where the x varies) is okay, but mixing 3.3.x with 3.2.x may result in compilation errors or runtime errors.

Verify that all systems use the same version of binutils ([eselect binutils list]) or many packages will fail linking with various errors like text relocation.

### [USE flags]

### [USE flags for] [sys-devel/distcc](https://packages.gentoo.org/packages/sys-devel/distcc) [[]] [Distribute compilation of C code across several machines on a network]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`gssapi`](https://packages.gentoo.org/useflags/gssapi)       Enable support for net-libs/libgssglue
  [`gtk`](https://packages.gentoo.org/useflags/gtk)             Add support for x11-libs/gtk+ (The GIMP Toolkit)
  [`gui`](https://packages.gentoo.org/useflags/gui)             Enable support for a graphical user interface
  [`hardened`](https://packages.gentoo.org/useflags/hardened)   Activate default security enhancements for toolchain (gcc, glibc, binutils)
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)           Add support for IP version 6
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`xinetd`](https://packages.gentoo.org/useflags/xinetd)       Add support for the xinetd super-server
  [`zeroconf`](https://packages.gentoo.org/useflags/zeroconf)   Support for DNS Service Discovery (DNS-SD)
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-21 05:26] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

Distcc ships with a graphical monitor to monitor tasks that a computer is sending away for compilation. This monitor is enabled when the `gui` USE flag is set.

### [Emerge]

After [configuring the USE setting](https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/USE#Declaring_USE_flags_for_individual_packages "Handbook:AMD64/Working/USE"), install the [[[sys-devel/distcc]](https://packages.gentoo.org/packages/sys-devel/distcc)[]] package:

`root `[`#`]`emerge --ask sys-devel/distcc`

** Important**\
Remember to install [[[sys-devel/distcc]](https://packages.gentoo.org/packages/sys-devel/distcc)[]] on all of the participating machines.

## [Configuration]

### [Service]

In order to have [distccd] started automatically, follow the next set of instructions.

#### [OpenRC]

Edit [/etc/conf.d/distccd] and make sure to set the `--allow` directive to allow only trusted clients. For added security, use the `--listen` directive to tell the [distccd] daemon what IP to listen on (for multi-homed systems). More information on [distcc] security can be found at [Distcc security notes](https://cdn.rawgit.com/distcc/distcc/master/doc/web/security.html).

** Warning**\
Anyone who can connect to the distcc server port can run arbitrary commands on that machine as the distccd user.

The following example allows the distcc clients running at `192.168.0.4` and `192.168.0.5` to connect to the [distccd] server running locally:

[FILE] **`/etc/conf.d/distccd`Allowing specific clients to connect to distccd**

    DISTCCD_OPTS="--port 3632 --log-level notice --log-file /var/log/distccd.log -N 15 --allow 192.168.0.4 --allow 192.168.0.5"

When logging to a file in [/var/log], create the log and give appropriate permissions:

`root `[`#`]`touch /var/log/distccd.log `

`root `[`#`]`chown distcc:root /var/log/distccd.log `

** Important**\
It is important to use `--allow` and `--listen`. Please read the [distccd] man page or the above security document for more information.

Now start the [distccd] daemon on all the participating computers:

`root `[`#`]`rc-update add distccd default `

`root `[`#`]`rc-service distccd start `

#### [systemd]

Edit the [/etc/systemd/system/distccd.service.d/00gentoo.conf] file to add the allowed clients in [CIDR](https://en.wikipedia.org/wiki/CIDR "wikipedia:CIDR") format. Matching the example will add all IP addresses in the 192.168.1.xxx range:

[FILE] **`/etc/systemd/system/distccd.service.d/00gentoo.conf`Setting ALLOWED_SERVERS**

    Environment="ALLOWED_SERVERS=192.168.1.0/24"

Or an example with multiple clients and a manually specified log-level:

[FILE] **`/etc/systemd/system/distccd.service.d/00gentoo.conf`Setting ALLOWED_SERVERS**

    Environment="ALLOWED_SERVERS=127.0.0.1 --allow 192.168.1.0/24 --allow 10.1.1.1/24 --log-level error"

** Note**\
The variable name `ALLOWED_SERVERS` here is rather confusing as it refers to the *clients* that are allowed to connect to the local distccd server. Nevertheless, it is this variable which is used in the distccd service as value for the `--allow option` -- see the [/usr/lib/systemd/system/distccd.service] file for additional information.

** Important**\
In contrast to OpenRC, environment variables put in [/etc/env.d/\*] will not take effect for systemd users even after running [env-update] and restarting the [distccd] service. This is because [/etc/environment.d] generated by [env-update] is only sourced by systemd user instance. Whereas, [distccd] is spawned by systemd system instance.

To set the proper environment variables for [distccd], place them into [/etc/systemd/system/distccd.service.d/00gentoo.conf], for example:

[FILE] **`/etc/systemd/system/distccd.service.d/00gentoo.conf`**

    [Service]
    Environment="ALLOWED_SERVERS=192.168.121.0/24"
    Environment="DISTCC_VERBOSE=1"
    Environment="DISTCC_SAVE_TEMPS=1"
    Environment="CCACHE_DIR=/var/cache/ccache"

** Warning**\
The `Environment=` directive in [/etc/systemd/system/distccd.service.d/00gentoo.conf] file does not support variable expansion. `Environment="PATH=/usr/lib/ccache/bin:$PATH"` will be treated as is, therefore will not work as intended.

For workaround, edit [distccd.service] by running the following command:

`root `[`#`]`systemctl edit --full distccd.service`

This will open up an editor. Change the line with `ExecStart=` directive to:

[CODE] **Workaround for appending to `PATH`**

    ExecStart=/bin/bash -c "PATH=/usr/lib/ccache/bin:$PATH exec /usr/bin/distccd --no-detach --daemon --port 3632 -N 15 --allow $ALLOWED_SERVERS --log-level debug"

Alternatively, it is possible to write a shell script wrapper for [/usr/bin/distccd].

Reload the unit files after making such changes:

`root `[`#`]`systemctl daemon-reload`

Enable auto-starting [distccd] and then start the service:

`root `[`#`]`systemctl enable distccd `

`root `[`#`]`systemctl start distccd `

### [Specifying participating hosts]

Use the [distcc-config] command on the local clients to set the list of hosts (systems running distccd as a service).

The following is an example list of host definitions. In most cases, variants of lines 1 and 2 suffice. The latter uses the `/limit` syntax to inform [distcc] about the maximum amount of jobs to be launched on this node. More information about the syntax used in lines 3 and 4 can be found in the [distcc manual page](https://cdn.rawgit.com/distcc/distcc/master/doc/web/man/distcc_1.html).

[CODE] **Examples of host definitions**

    192.168.0.1          192.168.0.2                       192.168.0.3
    192.168.0.1/2        192.168.0.2                       192.168.0.3/10
    192.168.0.1:4000/2   192.168.0.2/1                     192.168.0.3:3632/4
    @192.168.0.1         @192.168.0.2:/usr/bin/distccd     192.168.0.3

There are many other methods of setting up hosts. See the man page ([man distcc]) for more details.

If compilations should also occur on the local machine, add `localhost` in the hosts list. Conversely if the local machine is not to be used to compile, omit it from the hosts list. On a slow machine using localhost may actually slow things down. Make sure to test the settings in order to tune for best performance.

Configure [distcc] to use the hosts mentioned on the first line in the example:

`root `[`#`]`/usr/bin/distcc-config --set-hosts "localhost 192.168.0.1 192.168.0.2 192.168.0.3"`

Distcc also supports a *pump* mode, by invoking the [pump] command. This may significantly reduce build time when multiple files are compiled in parallel. It caches preprocessed headers on the server side and, as a result, gets rid of repeated uploading and preprocessing of these header files.

To configure a host for pump mode, add the `,cpp,lzo` suffix to the hosts definitions. Pump mode requires both `cpp` *and* `lzo` flags (regardless of the files being C or C++):

`root `[`#`]`/usr/bin/distcc-config --set-hosts "192.168.0.1,cpp,lzo 192.168.0.2,cpp,lzo 192.168.0.3,cpp,lzo"`

Hosts also need to be in:

[FILE] **`/etc/distcc/hosts`Should match \--set-hosts**

    192.168.0.1
    192.168.0.2
    192.168.0.3

Optionally, to set the maximum number of threads used by a host, add a forward slash \"/\" after each host:

[FILE] **`/etc/distcc/hosts`Specify max number of threads**

    192.168.0.1/8
    192.168.0.2/4
    192.168.0.3/16

The same applies to the [distcc-config] command. If the maximum threads number is not specified, it will default to 4.

## [Usage]

### [With Portage]

Setting up [Portage](https://wiki.gentoo.org/wiki/Portage "Portage") to use [distcc] is easy. It is a matter of enabling the [distcc] feature, and setting a decent value for the number of simultaneous build jobs (as [distcc] increases the amount of build resources).

Set the `MAKEOPTS` variable and `FEATURES` variable as shown below.

A common strategy is to:

-   set the value of `N` to *twice* the number of *total* (local + remote) CPU cores + 1, and
-   set the value of `M` to the number of *local* CPU cores

The use of `-lM` in the `MAKEOPTS` variable will prevent spawning too many tasks when some of the [distcc] cluster hosts are unavailable (increasing the amount of simultaneous jobs on the other systems) or when an ebuild is configured to disallow remote builds (such as with gcc). This is accomplished by refusing to start additional jobs when the system load is at or above the value of `M`.

[FILE] **`/etc/portage/make.conf`Setting MAKEOPTS and FEATURES**

    # Replace N and M with the right value as calculated previously
    MAKEOPTS="-jN -lM"
    FEATURES="distcc"

For instance, when there are two quad-core host PCs running [distccd] and the local PC has a dual core CPU, then the `MAKEOPTS` variable could look like this:

[FILE] **`/etc/portage/make.conf`MAKEOPTS example for 2 quad-core (remote) and one dual core (local) PC**

    # 2 remote hosts with 4 cores each = 8 cores remote
    # 1 local host with 2 cores = 2 cores local
    # total number of cores is 10, so N = 2*10+1 and M=2
    MAKEOPTS="-j21 -l2"

#### [CFLAGS and CXXFLAGS]

When editing the [make.conf] file, make sure that it does not have `-march=native` in the `CFLAGS` or `CXXFLAGS` variables. [distccd] will not distribute work to other machines if `march` is set to `native`. `CXXFLAGS` should list exact platform including a few extra flags as necessary for the CPU. Something like:

[FILE] **`/etc/portage/make.conf`inlined \*FLAGS**

    # Minimal list of flags is generated with resolve-march-native
    COMMON_FLAGS="-march=sandybridge -mtune=sandybridge -maes" # don't use -march=native!
    CFLAGS="$"
    CXXFLAGS="$"

Install [[[app-misc/resolve-march-native]](https://packages.gentoo.org/packages/app-misc/resolve-march-native)[]] to determine what `-march=native` would resolve into.

See [Inlining `-march=native` for distcc](https://blogs.gentoo.org/mgorny/2014/06/23/inlining-marchnative-for-distcc/) for more information.

### [With automake]

Update the `PATH` variable to include [/usr/lib/distcc/bin/] in front of the directory that contains [gcc] ([/usr/bin/]). There is a caveat. If [ccache] is used, then put the [distcc] location after the [ccache] one:

`root `[`#`]`export PATH="/usr/lib/ccache/bin:/usr/lib/distcc/bin:$"`

Put this in the user\'s [\~/.bashrc] or equivalent file to have the `PATH` set every time the user logs in, or set it globally through an [/etc/env.d/] file.

Instead of calling [make] alone, add in `-jN` (where `N` is an integer). The value of `N` depends on the network and the types of computers that are used to compile. A heuristic approach to the right value is given earlier in this article.

### [With ccache]

To make [Ccache](https://wiki.gentoo.org/wiki/Ccache "Ccache") work with [distcc], some prerequisites **must** be fulfilled:

-   Ccache is successfully set up *locally*
-   Distcc is successfully set up on the desired hosts

The following setup will work as follows:

[CODE] **Flow diagram**

    [client]                                                      [remote]
    '''ccache''' <miss?> → compile it and save cache files,
    <hit?>           also distribute other source code → '''distcc''' → '''ccache''' <miss?> → compile it, save cache files, return cache file to client
      ↓                                                           <hit?>
    use the local cache file                                        ↓
                                                     return local cache file to client

** Warning**\
The following configuration **must** be done on all desired hosts!

#### [Configure distccd]

In order to let the daemon [distccd] use [ccache], it **must** masquerade the path [/usr/bin] with [/usr/lib/ccache/bin].

[FILE] **`/etc/conf.d/distccd`**

    PATH="/usr/lib/ccache/bin:$"

When [ccache] should itself automatically use [distcc], [ccache] should use the prefix `distcc`:

** Warning**\
This can lead to recursion where [distcc] would return error code 111. It is not compatible with `FEATURES` \"ccache\" **and** \"distcc\", because portage **and** [ccache] would both enable [distcc] and create a loop.

[FILE] **`/etc/conf.d/distccd`**

    CCACHE_PREFIX="distcc"

\
Additionally [distccd] **must** be aware of the environment variables `DISTCC_DIR` and `CCACHE_DIR`:

** Warning**\
These variables **must** be set somewhere in [/etc/env.d/], otherwise [ccache] tries to put cache files in [\$/.ccache/], which might result in a *COMPILE_ERROR*, due to insufficient permissions. To pinpoint this, use the [testing example](https://wiki.gentoo.org/wiki/Distcc#Testing "Distcc") mentioned below and [export DISTCC_SAVE_TEMPS=\"1\"] as mentioned [here](https://wiki.gentoo.org/wiki/Distcc#Get_more_output_from_emerge_logs "Distcc"). This will provide error logs from the remote site in [/tmp/] by default. The logs will look like this: [distcc_server_stderr\_\*.txt]. Be aware, that these environment variables cannot be set in [/etc/conf.d/distccd], since they will not be read from [distccd] for some reason.

[FILE] **`/etc/env.d/03distcc_ccache`**

    CCACHE_DIR="/var/cache/ccache"
    DISTCC_DIR="/var/tmp/portage/.distcc"

Next, update the environment variables:

`root `[`#`]`env-update`

    >>> Regenerating /etc/ld.so.cache...

Finally, restart the daemon [distccd] to adapt all changes:

`root `[`#`]`rc-service distccd restart`

#### [Configure ccache]

** Warning**\
When using [distcc] with [ccache], it is necessary to prepare the cache directories **manually**, since the daemon [distccd] only works with the user `distcc` for some reason and it cannot create directories within [/var/cache/ccache/]. It is not sufficient to add this user to the group `portage`. Also be aware, that the variable `cache_dir_levels`, defined in [ccache.conf], specifies how many subdirectories have to be created. The following example uses the default, which is `2`.

First, prepare the cache directories:

`root `[`#`]`cd "/var/cache/ccache/" `

`root `[`#`]`mkdir   tmp `

`root `[`#`]`for first_level_directory in $(find . -maxdepth 1 -type d -not -name "." -and -not -name "tmp"); do pushd "$" >/dev/null; mkdir  ; popd >/dev/null; done `

The second command ([mkdir]) will create the *first level directories* from [a] to [z], [0] to [9] and [tmp]. The following [for] loop will then look for the *first level directories* ([find . -maxdepth 1 -type d]), excluding the current directory [.] and [tmp] (`-not -name "." -and -not -name "tmp"`). It then descends into each of them ([pushd]), creates the *second level directories* from [a] to [z] and [0] to [9] ([mkdir]) and goes back to the previous directory ([popd]), which is [/var/cache/ccache/].

** Important**\
The current directory [.] **must** be excluded with `-not -name "."`, otherwise the first [pushd] command will go to the current directory [.] and then goes back to whatever directory is currently on the stack via [popd]. It will navigate through the entire stack until it is empty, creating directories, where each [pushd] command fails. If this happens, one can search for them using [find / -type d -name \"0\"] and remove them with [rm \--recursive \[a-z\] \[0-9\]]. It is advised to do this **manually!**

When the preparation is done, every directory - including the directory [ccache] itself - **must** be owned by the user `distcc`:

`root `[`#`]`find /var/cache/ccache -type d -exec chown distcc:portage "" +`

#### [Configure portage]

To use [emerge] with [distcc] and [ccache], make sure, that both features are enabled and that `CCACHE_DIR` is set in [/etc/portage/make.conf]:

[FILE] **`/etc/portage/make.conf`**

    [...]
    FEATURES="distcc ccache"
    CCACHE_DIR="/var/cache/ccache"

It might be redundant to set `CCACHE_DIR` here, since it is already defined in [/etc/env.d/03distcc_ccache], mentioned [here](https://wiki.gentoo.org/wiki/Distcc#Configure_distccd "Distcc"). But to make absolutely sure, configure it like that.

#### [Testing distcc with ccache manually]

##### [Remote]

First enable verbose logging by setting `--log-level` to `debug` in [/etc/conf.d/distccd]:

[FILE] **`/etc/conf.d/distccd`**

    [...]
    DISTCCD_OPTS="$ --log-level debug"
    [...]

After that, restart the daemon to adapt the changes:

`root `[`#`]`rc-service distccd restart`

Also check, if there are directories in [/var/cache/ccache] - including the directory [ccache] itself - which are not owned by the user `distcc` and correct their owner permissions:

`root `[`#`]`chown -R distcc:portage /var/cache/ccache `

##### [Client]

Make sure, that the following environment variables are present in the current shell:

`root `[`#`]`export PATH="/usr/lib/ccache/bin:$" `

`root `[`#`]`export CCACHE_DIR="/var/cache/ccache" `

`root `[`#`]`export DISTCC_DIR="/var/tmp/portage/.distcc" `

`root `[`#`]`export DISTCC_SAVE_TEMPS="1" `

`root `[`#`]`export DISTCC_VERBOSE="1" `

After that, navigate to a temporary directory within [/tmp/] and compile the [example](https://wiki.gentoo.org/wiki/Distcc#Testing "Distcc") mentioned below:

`root `[`#`]`cd $(mktemp --directory) `

`root `[`#`]`distcc gcc -c main.c -o main.o `

This will provide a verbose output, while also keeping temporary files receiving from the remote site in [/tmp/] by default:

[CODE]

    [...]
    distcc[29466] (dcc_cleanup_tempfiles_inner) skip cleanup of /tmp/distcc_9c42f0a6.i
    distcc[29466] (dcc_cleanup_tempfiles_inner) skip cleanup of /tmp/distcc_server_stderr_9cc0f0a6.txt
    [...]

Any occuring error from the remote site are saved in [/tmp/distcc_server_stderr\_\*.txt].

If the compilation was successful, the following line will be shown:

[CODE]

    [...]
    distcc[29466] compile main.c on 192.168.0.4 completed ok
    [...]

On the remote site, it will look like this:

[CODE]

    [...]
    distccd[13296] (dcc_check_compiler_masq) /usr/lib/ccache/bin/gcc is a safe symlink to /usr/bin/ccache
    [...]
    distccd[13296] (dcc_job_summary) client: 192.168.0.4:33880 COMPILE_OK exit:0 sig:0 core:0 ret:0 time:20ms gcc main.c

The important part here, is, that any symlink of [/usr/lib/ccache/bin/] is a save symlink to [/usr/bin/ccache].

Also, on the remote site, there should be the cached file [2beaa22dc2a2873d6869d69411840c-17229.o] in [/var/cache/ccache/c/0/], assuming, the example with its filename was copied from this wiki article. Generally, one can monitor the ccache size using [watch \"ccache \--show-stats\"], while compiling.

#### [Testing distcc with ccache using emerge]

Check, if necessary environment variables are present for the current shell, see [here](https://wiki.gentoo.org/wiki/Distcc#Future_usage "Distcc") and that [/etc/portage/make.conf] was configured properly, see [here](https://wiki.gentoo.org/wiki/Distcc#Configure_portage "Distcc").

To produce some cached files on the remote site, one can compile small packages like `htop` and `bzip2` on the client:

`root `[`#`]`emerge --ask sys-process/htop app-arch/bzip2`

#### [Future usage]

Make sure, that the following environment variables are always set in the desired shell:

[CODE]

    PATH="/usr/lib/ccache/bin:$"
    CCACHE_DIR="/var/cache/ccache"
    DISTCC_DIR="/var/tmp/portage/.distcc"

### [To bootstrap]

TODO: [ **Todo:**]

-   Check this section for outdated information. Notably \"USE=\'-\*\'\" and \"\--nodeps\" may no longer be advised. See Discussion page for more informaiton.

\

Using [distcc] to bootstrap (i.e. build a working toolchain before installing the remainder of the system) requires some additional steps to take.

#### [Step 1: Configure Portage]

Boot the new box with a Gentoo Linux LiveCD and follow the [installation instructions](https://wiki.gentoo.org/wiki/Handbook:AMD64 "Handbook:AMD64"), while keeping track of the instructions in the [Gentoo FAQ](https://wiki.gentoo.org/wiki/FAQ "FAQ") for information about bootstrapping. Then configure Portage to use [distcc]:

[FILE] **`/etc/portage/make.conf`Configure Portage to use distcc**

    FEATURES="distcc"
    MAKEOPTS="-jN"

Update the `PATH` variable in the installation session as well:

`root `[`#`]`export PATH="/usr/lib/ccache/bin:/usr/lib/distcc/bin:$"`

#### [Step 2: Getting distcc]

Install [[[sys-devel/distcc]](https://packages.gentoo.org/packages/sys-devel/distcc)[]]:

`root `[`#`]`USE='-*' emerge --nodeps sys-devel/distcc`

#### [Step 3: Setting up distcc]

Run [distcc-config] to setup distcc; substitute the `host#` in the example with the IP addresses or hostnames of the participating nodes.

`root `[`#`]`/usr/bin/distcc-config --set-hosts "localhost host1 host2 host3 ..."`

Distcc is now set up to bootstrap! Continue with the proper installation instructions and do *not* forget to run [emerge distcc] after running [emerge \@system]. This is to make sure that all of the necessary dependencies are installed.

** Note**\
[Distcc] may not appear to be used during bootstrap and [emerge \@system]. This is expected as some ebuilds do not work well with distcc, so they intentionally disable it.

### [Extras]

The [distcc] application has additional features and applications to support working in a [distcc] environment.

### [Monitoring utilities]

Distcc ships with two monitoring utilities. The text-based monitoring utility is always built and is called [distccmon-text]. Running it for the first time can be a bit confusing, but it is really quite easy to use. If the program is run with no parameter it will run just once. However, if it is passed a number it will update every `N` seconds, where `N` is the argument that was passed.

`user `[`$`]`distccmon-text 10`

The other monitoring utility is only enabled when the `gui` USE flag is set. This one is GTK based, runs in an X environment, and it is quite lovely. The GUI monitor is called [distccmon-gnome].

`user `[`$`]`distccmon-gnome`

To monitor Portage\'s [distcc] usage:

`root `[`#`]`DISTCC_DIR="/var/tmp/portage/.distcc/" distccmon-text 10 `

`root `[`#`]`DISTCC_DIR="/var/tmp/portage/.distcc/" distccmon-gnome`

** Important**\
If the distcc directory is elsewhere, change the `DISTCC_DIR` variable accordingly.

A trick is to set `DISTCC_DIR` in environment variables:

`root `[`#`]`echo 'DISTCC_DIR="/var/tmp/portage/.distcc/"' >> /etc/env.d/03distcc_dir`

This creates a file with following content:

[FILE] **`/etc/env.d/03distcc_dir`**

    DISTCC_DIR="/var/tmp/portage/.distcc/"

** Important**\
Be aware that `DISTCC_DIR` must be set somewhere else than [/etc/env.d/02distcc], as it gets overwritten everytime, when using [distcc-config]! [distcc-config \--set-env DISTCC_DIR \<some_path\>] does not work.

Now update the environment:

`root `[`#`]`env-update `

`root `[`#`]`source /etc/profile`

Finally, start the GUI application:

`root `[`#`]`distccmon-gnome`

### [SSH for communication]

Setting up distcc via SSH includes some pitfalls. First, generate an SSH key pair without password setup. Be aware that portage compiles programs as the Portage user (or as root if `FEATURES="userpriv"` is not set). The home folder of the Portage user is [/var/tmp/portage/], which means the keys need to be stored in [/var/tmp/portage/.ssh/]

** Warning**\
Home folder of the Portage user changed in recent versions to [/var/lib/portage/home], but this folder cannot be used for distcc via SSH because it is out of the accessible path during compilation. It should be updated:

`root `[`#`]`usermod -d /var/tmp/portage portage`

`root `[`#`]`ssh-keygen -b 2048 -t rsa -f /var/tmp/portage/.ssh/id_rsa`

Second, create a section for each host in the SSH configuration file:

[FILE] **`/var/tmp/portage/.ssh/config`Add per-host sections**

    Host test1
        HostName 123.456.789.1
        Port 1234
        User UserName

    Host test2
        HostName 123.456.789.2
        Port 1234
        User UserName

Send the public key to each compilation node:

`root `[`#`]`ssh-copy-id -i /var/tmp/portage/.ssh/id_rsa.pub UserName@CompilationNode`

** Warning**\
Because home folder of the distcc user changed in recent versions to [/dev/null] and login to nologin, you either need to use another UserName or to update distcc account on the host:

`root `[`#`]`usermod -d /var/lib/distcc -s /bin/bash distcc`

Also make sure that each host is available in the [known_hosts] file:

`root `[`#`]`ssh-keyscan -t rsa <compilation-node-1> <compilation-node-2> [...] > /var/tmp/portage/.ssh/known_hosts`

Fix the file ownership as follows:

`root `[`#`]`chown -R portage:portage /var/tmp/portage/.ssh/`

To set up the hosts `test1` and `test2`, run:

`root `[`#`]`/usr/bin/distcc-config --set-hosts "@test1 @test2"`

Please note the `@` (@ sign), which specifies ssh hosts for distcc.

Finally, tell [distcc] which SSH binary to use:

[FILE] **`/etc/portage/make.conf`**

    DISTCC_SSH="ssh"

It is not necessary to run the [distccd] initscript on the hosts when [distcc] communicates via SSH.

#### [Reverse SSH]

As an alternative to distcc\'s built-in SSH solution, a compiling server can connect to the distcc client via SSH, redirecting the client\'s distcc TCP port to the compiling server. There is no need for password-less SSH keys on the client:

`user `[`$`]`ssh -R3632:127.0.0.1:3632 root@distcc-client`

Note that distcc uses [localhost] as a literal keyword for special purpose so that [127.0.0.1] has to be used instead. For multiple compiling servers each needs its own port redirection on the client (e.g. 127.0.0.1:4000, 127.0.0.1:4001 etc). Assert that IP addresses and ports are listed in [/etc/distcc/hosts] on the client.

### [Testing]

To test [distcc], write a simple *Hello distcc* program and run [distcc] in verbose mode to see if it communicates properly.

[FILE] **`main.c`**

    #include <stdio.h>

    int main()

Next, turn on verbose mode, compile the program using [distcc] and link the generated object file into an executable:

`user `[`$`]`export DISTCC_VERBOSE=1 `

`user `[`$`]`distcc gcc -c main.c -o main.o # or 'pump distcc <...>' `

`user `[`$`]`gcc main.o -o main `

** Note**\
Replace [distcc] command with [pump distcc] for use pump mode.

There should be a bunch of output about [distcc] finding its configuration, selecting the host to connect to, starting to connect to it, and ultimately compile [main.c]. If the output does not list the desired [distcc] hosts, check the configuration.

Finally, ensure the compiled program works properly. To test each host, enumerate each compile host in the hosts file.

`user `[`$`]`./main`

    Hello distcc!

## [Troubleshooting]

If a problem occurs while using [distcc], then this section might help in resolving the problem.

### [][ERROR: failed to open [/var/log/distccd.log]]

As of January 22nd, 2015 emerging fails to create the proper [distccd.log] file in [/var/log/]. This apparently only effects version 3.1-r8 of distcc. This bug is in the process of being corrected (see [[[bug #477630]](https://bugs.gentoo.org/show_bug.cgi?id=477630)[]]). It is possible to work around this by manually creating the log file, giving it proper ownership, and restarting the distccd daemon:

`root `[`#`]`mkdir -p /var/log/distcc `

`root `[`#`]`touch /var/log/distcc/distccd.log `

`root `[`#`]`chown distcc:daemon /var/log/distcc/distccd.log `

Next update the [/var/log] path of the [distccd] configuration file in [/etc/conf.d/distccd] to the [distcc] directory created in the step before:

[FILE] **`/etc/conf.d/distccd`Updating log path**

    DISTCCD_OPTS="--port 3632 --log-level notice --log-file /var/log/distcc/distccd.log -N 15

Finally, restart the distccd service:

`root `[`#`]`/etc/init.d/distccd restart`

### [Some packages do not use distcc]

As various packages are installed, users will notice that some of them aren\'t being distributed (and aren\'t being built in parallel). This may happen because the package\' [Makefile] doesn\'t support parallel operations, or the maintainer of the ebuild has explicitly disabled parallel operations due to a known problem.

Sometimes [distcc] might cause a package to fail to compile. If this happens, please [report](https://wiki.gentoo.org/wiki/Bugzilla/Bug_report_guide "Bugzilla/Bug report guide") it.

[Rust](https://wiki.gentoo.org/wiki/Rust "Rust") package is known to cause excessive IO utilization as `--local-load` is ignored and `--jobs` is usually too high for local build resources. A [package.env](https://wiki.gentoo.org/wiki/Package.env "Package.env") needs to be provisioned with non-distcc [MAKEOPTS](https://wiki.gentoo.org/wiki/MAKEOPTS "MAKEOPTS") values to workaround this behavior.

[FILE] **`/etc/portage/env/nodistcc.conf`**

    MAKEOPTS="-jN"
    FEATURES="-distcc"

[FILE] **`/etc/portage/package.env/nodistcc`**

    dev-lang/rust           nodistcc.conf
    mail-client/thunderbird nodistcc.conf
    sys-libs/libcxx         nodistcc.conf
    www-client/firefox      nodistcc.conf

### [Mixed GCC versions]

If the environment hosts different GCC versions, there will likely be very weird problems. The solution is to make certain all hosts have the *exact* same GCC version. Corollary: if you have a weird problem, double-check the compiler invocations (from local and remote logs), and verify equality of versions strings (output of `$ --version`).

Recent Portage updates have made Portage use `$-gcc` (minus gcc) instead of `gcc`. This means that if i686 machines are mixed with other types (i386, i586) then the builds will run into troubles. A workaround for this may be to run:

`root `[`#`]`export CC='gcc' CXX='c++'`

It is also possible to set the `CC` and `CXX` variables in [/etc/portage/make.conf] to the values list in the command above.

** Important**\
Doing this explicitly redefines some behavior of Portage and may have some weird results in the future. Only do this if mixing CHOSTs is unavoidable.

** Note**\
Having the right version of gcc as a slot on a server isn't enough. Portage uses [distcc] as a replacement for the compiler referenced by the `CHOST` variable (i.e. `x86_64-pc-linux-gnu`) and [distccd] invokes it by exactly same name. The right version of gcc should be a default system's compiler on all involved compilation hosts.

### [][-march=native]

Starting with GCC 4.3.0, the compiler supports the `-march=native` option which turns on CPU auto-detection and optimizations that are worth being enabled on the processor on which GCC is running. This creates a problem when using [distcc] because it allows the mixing of code optimized for different processors. For example, running [distcc] with `-march=native` on a system that has an AMD Athlon processor and doing the same on *another* system that has an Intel Pentium processor will mix code compiled on both processors together.

Heed the following warning:

** Warning**\
Do **not** use `-march=native` or `-mtune=native` in the `CFLAGS` or `CXXFLAGS` variables of [make.conf] when compiling with [distcc].

See the [CFLAGS and CXXFLAGS section](https://wiki.gentoo.org/wiki/Distcc#CFLAGS_and_CXXFLAGS "Distcc") and [Inlining `-march=native` for distcc](https://blogs.gentoo.org/mgorny/2014/06/23/inlining-marchnative-for-distcc/) for more information. Use of [[[app-misc/resolve-march-native]](https://packages.gentoo.org/packages/app-misc/resolve-march-native)[]] is also an option.

### [Get more output from emerge logs]

It is possible to obtain more logging by enabling verbose mode. This is accomplished by adding `DISTCC_VERBOSE` to [/etc/portage/bashrc]:

[FILE] **`/etc/portage/bashrc`Enabling verbose logging**

    export DISTCC_VERBOSE=1

The verbose logging can then be found in [/var/tmp/portage/\$CATEGORY/\$PF/temp/build.log].

Keep in mind that the first [distcc] invocation visible in [build.log] isn't necessary the first [distcc] call during a build process. For example a build server can get a one-minute backoff period during the configuration stage when some checks are performed using a compiler ([distcc] sets a backoff period when compilation on a remote server failed, it doesn't matter whether it failed on local machine or not).

Dig into the [/var/tmp/portage/\$CATEGORY/\$PF/work/] directory to investigate such situations. Find other logs, or call [make] explicitly from within the working directory.

Another interesting variable to use is `DISTCC_SAVE_TEMPS`. When set, it saves the standard output/error from a remote compiler which, for Portage builds, results in files in the [/var/tmp/portage/\$CATEGORY/\$PF/temp/] directory.

[FILE] **`/etc/portage/bashrc`Saving temporary output**

    export DISTCC_SAVE_TEMPS=1

### [][Failed to create directory /dev/null/.cache/ccache/tmp: Not a directory]

This error can be discovered from the standard error output file in the server if `DISTCC_SAVE_TEMPS` is set. It only occurs when using [distccd] with [ccache].

Likely, it is because `CCACHE_DIR` is not properly set, or not passed correctly to [distccd]. [ccache] will then default to [\$HOME/.cache/ccache] as its cache folder. However, [ccache] is run by [distccd] under user **distcc**, which is a non-login account. See [systemd section](https://wiki.gentoo.org/wiki/Distcc#systemd "Distcc") and [With ccache section](https://wiki.gentoo.org/wiki/Distcc#With_ccache "Distcc") for setting `CCACHE_DIR`.

### [Portage build failing with errors that are apparently not connected with distcc at all]

When builds are failing with errors that do not seem to be connected to distcc, but the build works with `FEATURES="-distcc"`, it has been reported that builds sometimes fail because of `DISTCC_VERBOSE=1`. Try the build with `DISTCC_VERBOSE=0`.

## [See also]

-   [Distcc/Cross-Compiling](https://wiki.gentoo.org/wiki/Distcc/Cross-Compiling "Distcc/Cross-Compiling") --- shows the reader how to set up distcc for cross-compiling across different processor architectures.

## [External resources]

-   [Inlining `-march=native` for distcc](https://blogs.gentoo.org/mgorny/2014/06/23/inlining-marchnative-for-distcc/)
-   [Distcc on Github](https://github.com/distcc/distcc)
-   [Distcc homepage](https://distcc.github.io/)

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **Lisa Seelye, [Mike Gilbert (floppym)](https://wiki.gentoo.org/wiki/User:Floppym "User:Floppym") , Erwin, [Sven Vermeulen (SwifT)](https://wiki.gentoo.org/wiki/User:SwifT "User:SwifT") , Lars Weiler, Tiemo Kieft, and **\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*