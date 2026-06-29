**vlock** is a **V**irtual Console **lock** program.

## Contents

-   [[1] [Concepts]](#Concepts)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Disable SysRq key]](#Disable_SysRq_key)

### [Concepts]

Sometimes a malicious local user could cause more problems than a sophisticated remote one. [vlock] is a program that locks one or more sessions on the Linux console to prevent attackers from gaining physical access to the machine.

## [Installation]

### [USE flags]

### [USE flags for] [app-misc/vlock](https://packages.gentoo.org/packages/app-misc/vlock) [[]] [Allows to lock one or all of the sessions of your console display]

  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`pam`](https://packages.gentoo.org/useflags/pam)           Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`selinux`](https://packages.gentoo.org/useflags/selinux)   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)         Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  ----------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-09-02 17:00] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

To install [[[app-misc/vlock]](https://packages.gentoo.org/packages/app-misc/vlock)[]]:

`root `[`#`]`emerge --ask app-misc/vlock`

## [Usage]

When not working in a virtual console, switch to one by pressing [CTRL]+[ALT]+[F1] through [F6]. By default, [vlock] locks the current console session. Use the `-a` switch in order to lock all console sessions.

`user `[`$`]`vlock -a`

It is also possible to use vlock from an X session. Use the `-n` option to make vlock switch to an empty virtual console.

`root `[`#`]`usermod -a -G vlock larry`

`user `[`$`]`vlock -na`

### [Disable SysRq key]

The magic [SysRq] key combination can unlock consoles when least expected. In order to prevent this, disable the SysRq mechanism while consoles are locked like so:

`user `[`$`]`vlock -sa`

If a user does not know how to use the [SysRq] key, then it is probably not needed. Disable it when configuring the kernel:

[KERNEL] **Disabling Magic SysRq key**

    Kernel hacking --->
      [ ] Magic SysRq key