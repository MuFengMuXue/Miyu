[] This article is a **work in progress**; treat its contents with caution - [WavyEbuilder](https://wiki.gentoo.org/wiki/User:WavyEbuilder "User:WavyEbuilder") ([talk](https://wiki.gentoo.org/index.php?title=User_talk:WavyEbuilder&action=edit&redlink=1 "User talk:WavyEbuilder (page does not exist)") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/WavyEbuilder "Special:Contributions/WavyEbuilder")).

**Resources**

[[]][Bubblewrap repository](https://github.com/containers/bubblewrap)

**Bubblewrap** is a low-level unprivileged sandboxing tool used by [Flatpak](https://wiki.gentoo.org/wiki/Flatpak "Flatpak"). Bubblewrap makes extensive use of user namespaces in the Linux kernel to allow unprivileged users to sandbox programs.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Kernel]](#Kernel)
-   [[2] [Troubleshooting]](#Troubleshooting)
-   [[3] [Possible obstacles]](#Possible_obstacles)
    -   [[3.1] [User namespaces not available in the current kernel]](#User_namespaces_not_available_in_the_current_kernel)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [sys-apps/bubblewrap](https://packages.gentoo.org/packages/sys-apps/bubblewrap) [[]] [Unprivileged sandboxing tool, namespaces-powered chroot-like solution]

  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`suid`](https://packages.gentoo.org/useflags/suid)         Enable setuid root program(s)
  ----------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 00:41] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

The `suid` USE flag can be used to support using bubblewrap without user namespaces by setting suid on the `bwrap` binary.

### [Emerge]

`root `[`#`]`emerge --ask sys-apps/bubblewrap`

### [Kernel]

User namespaces can be enabled in the kernel so that `suid` is not required on the `bwrap` binary:

[KERNEL] **Enabling user namespaces**

    General setup --->
      Namespaces support --->
        <*>  User namespace

## [Troubleshooting]

## [Possible obstacles]

### [User namespaces not available in the current kernel]

Make sure user namespaces are enabled in the kernel or enable the `suid` USE flag. `CONFIG_USER_NS=y`

## [External resources]

-   [Introduction to basic sandboxing with bubblewrap](https://sloonz.github.io/posts/sandboxing-1/)
-   [Bubblewrap on the Arch Wiki](https://wiki.archlinux.org/title/Bubblewrap)