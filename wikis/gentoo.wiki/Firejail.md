**Resources**

[[]][Home](https://firejail.wordpress.com/)

[[]][Official documentation](https://firejail.wordpress.com/documentation-2/)

[[]][GitHub](https://github.com/netblue30/firejail)

[[]][[#firejail](ircs://irc.libera.chat/#firejail)] ([[webchat](https://web.libera.chat/#firejail)])

**Firejail** is a SUID sandboxing program. It reduces the risk of security breaches by restricting the running environment of untrusted applications using, among other things, [Linux namespaces](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Sandboxing_the_Firefox_Browser_with_Firejail#Resource_Isolation_via_Linux_Namespaces "User:Sakaki/Sakaki's EFI Install Guide/Sandboxing the Firefox Browser with Firejail") and [seccomp-bpf](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Sandboxing_the_Firefox_Browser_with_Firejail#Permitted_Syscall_Management_via_Seccomp-BPF "User:Sakaki/Sakaki's EFI Install Guide/Sandboxing the Firefox Browser with Firejail"). The software includes security profiles for a large number of applications like [Mozilla Firefox](https://wiki.gentoo.org/wiki/Firefox "Firefox"), [Chromium](https://wiki.gentoo.org/wiki/Chromium "Chromium"), [VLC](https://wiki.gentoo.org/wiki/VLC "VLC"), or [Transmission](https://wiki.gentoo.org/wiki/Transmission "Transmission").

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Profiles]](#Profiles)
    -   [[2.2] [Using Firejail by default]](#Using_Firejail_by_default)
    -   [[2.3] [System-wide Configuration]](#System-wide_Configuration)
    -   [[2.4] [Kernel]](#Kernel)
-   [[3] [Usage]](#Usage)
-   [[4] [Troubleshooting]](#Troubleshooting)
    -   [[4.1] [firemon]](#firemon)
    -   [[4.2] [Verbose arguments]](#Verbose_arguments)
-   [[5] [Possible obstacles]](#Possible_obstacles)
    -   [[5.1] [not all executables from \--private-bin list were found.]](#not_all_executables_from_--private-bin_list_were_found.)
    -   [[5.2] [user namespaces not available in the current kernel.]](#user_namespaces_not_available_in_the_current_kernel.)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/firejail](https://packages.gentoo.org/packages/sys-apps/firejail) [[]] [Security sandbox for any type of processes]

  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+chroot`](https://packages.gentoo.org/useflags/+chroot)                 Enable chrooting to custom directory
  [`+dbusproxy`](https://packages.gentoo.org/useflags/+dbusproxy)           Enable DBus proxying to filter access in supporting profiles
  [`+file-transfer`](https://packages.gentoo.org/useflags/+file-transfer)   Enable file transfers between sandboxes and the host system
  [`+globalcfg`](https://packages.gentoo.org/useflags/+globalcfg)           Enable global config file
  [`+network`](https://packages.gentoo.org/useflags/+network)               Enable networking features
  [`+private-home`](https://packages.gentoo.org/useflags/+private-home)     Enable private home feature
  [`+userns`](https://packages.gentoo.org/useflags/+userns)                 Enable attaching a new user namespace to a sandbox (\--noroot option)
  [`X`](https://packages.gentoo.org/useflags/X)                             Enable X11 sandboxing
  [`apparmor`](https://packages.gentoo.org/useflags/apparmor)               Enable support for custom AppArmor profiles
  [`contrib`](https://packages.gentoo.org/useflags/contrib)                 Install contrib scripts
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                 !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-04-16 14:50] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

The `X` USE flag sandbox replaces the regular X11 server with Xpra or Xephyr server. This prevents X11 keyboard loggers and screenshot utilities from [accessing the main X11 server](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Sandboxing_the_Firefox_Browser_with_Firejail#Demonstrating_the_X11_Vulnerability "User:Sakaki/Sakaki's EFI Install Guide/Sandboxing the Firefox Browser with Firejail") but introduces a lot of additional dependencies.

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/firejail`

## [Configuration]

Firejail comes with numerous default profiles for many popular applications located in [/etc/firejail/]. In many cases the default profile configuration is sufficient. In addition to configuring a profile users may wish to set up a shortcut to enable firejail to be run by default for their selected application.

### [Profiles]

The list of preconfigured profiles is available in [/etc/firejail/].

If you wish to make customizations for an existing profile simply copy it to your home directory and edit as necessary:

`user `[`$`]`cp /etc/firejail/firefox.profile ~/.config/firejail/firefox.profile`

To make a profile for an application without a preconfigured profile you can use the default profile as a basis:

`user `[`$`]`cp /etc/firejail/default.profile ~/.config/firejail/`*`app-name`*`.profile`

Here are some example options you may wish to include in a custom profile:

[FILE] **`~/.config/firejail/`*`app-name`*`.config`Custom profile example**

    whitelist ~/pictures/

    whitelist ~/share/
    read-only ~/share/

    whitelist ~/dev/WebExtensions/
    read-only ~/dev/WebExtensions/

    whitelist ~/.cache/fish/

    blacklist /mnt
    blacklist /opt

### [Using Firejail by default]

A symbolic link to [/usr/bin/firejail] under the name of a program, will start the program in Firejail sandbox. A good place is [/usr/local/bin] directory. For example to run Firefox with firejail by default:

`root `[`#`]`ln -s /usr/bin/firejail /usr/local/bin/firefox`

This works for clicking on desktop environment icons, menus etc. Use [firejail \--tree] to verify the program is sandboxed.

`user `[`$`]`firejail --tree`

    23615:larry:firejail /usr/bin/firefox
      23616:larry:firejail /usr/bin/firefox
        23618:larry:/usr/bin/firefox

Alternatively you can create the following file instead and make it executable:

[FILE] **`/usr/local/bin/firefox`Firejail Desktop Integration**

    #!/bin/bash
    firejail /usr/bin/firefox $@

This method allows command line options to be passed to firejail. Remember to make it executable with [chmod +x /usr/local/bin/firefox].

To use Firejail by default for all applications for which it has profiles, run the [firecfg] tool as root.

`root `[`#`]`firecfg`

** Important**\
In the default configuration, firecfg will build a symbolic link for patch, this action will make portage work incorrectly, maybe you need to remove the link or do some configurations for patch.

### [System-wide Configuration]

System-wide configuration is set in [/etc/firejail/firejail.config]. If you have executables in [/usr/local/bin] corresponding to one of your firejailed applications combined with the `private-bin` profile option then make sure `private-bin-no-local` is set to `yes`

[FILE] **`/etc/firejail/firejail.config`System-wide settings example**

    # Remove /usr/local directories from private-bin list, default disabled.
    private-bin-no-local yes

### [Kernel]

Optionally you can enable user namespaces in the kernel so they can be utilized by firejail:

[KERNEL] **Enabling user namespaces**

    General setup --->
      Namespaces support --->
        <*>  User namespace

## [Usage]

Usage is simple as:

`user `[`$`]`firejail firefox`

Private mode can be used as a quick way of hiding all the files in your home directory from sandboxed programs. It is enabled using `--private` command line option:

`user `[`$`]`firejail --private firefox`

Additionally, [firejail] can provide full graphical isolation for X11-based programs like [firefox]; an in-depth tutorial for doing so may be read [here](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Sandboxing_the_Firefox_Browser_with_Firejail "User:Sakaki/Sakaki's EFI Install Guide/Sandboxing the Firefox Browser with Firejail").

## [Troubleshooting]

### [firemon]

**Firejail** comes with a tool **firemon** which can be used to help with troubleshooting. To use it run [firemon] as root then in a separate terminal start the application you wish to troubleshoot with [firejail *application*].

### [Verbose arguments]

Consider to use following arguments:

    --trace --debug-caps --debug-errnos --debug-syscalls --debug-protocols --debug-blacklists --debug-whitelists --debug-caps --debug-errnos --debug-private-lib --debug-protocols --debug-syscalls

## [Possible obstacles]

### [not all executables from \--private-bin list were found.]

Either disable the `private-bin` option in your application profile or ensure `private-bin-no-local yes` is set in [/etc/firejail/firejail.config].

### [user namespaces not available in the current kernel.]

Make sure user namespaces are set in the kernel. `CONFIG_USER_NS=y`

## [See also]

[User:Sakaki/Sakaki\'s EFI Install Guide/Sandboxing the Firefox Browser with Firejail](https://wiki.gentoo.org/wiki/User:Sakaki/Sakaki%27s_EFI_Install_Guide/Sandboxing_the_Firefox_Browser_with_Firejail "User:Sakaki/Sakaki's EFI Install Guide/Sandboxing the Firefox Browser with Firejail") - tutorial-style article, introducing [firejail]\'s protection features in some depth, as well as the additional steps required to fully *graphically* isolate software such as [firefox].

## [External resources]

-   [Basic Usage on the Firejail Wordpress](https://firejail.wordpress.com/documentation-2/basic-usage/)
-   [Firefox Guide on the Firejail Wordpress](https://firejail.wordpress.com/documentation-2/firefox-guide/)
-   [Firejail on the Arch Wiki](https://wiki.archlinux.org/index.php/Firejail)