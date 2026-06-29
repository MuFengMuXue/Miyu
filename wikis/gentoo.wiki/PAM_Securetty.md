This page goes over restricting [root] authentication with [PAM](https://wiki.gentoo.org/wiki/PAM "PAM").

## Contents

-   [[1] [pam_securetty.so]](#pam_securetty.so)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [/etc/securetty]](#.2Fetc.2Fsecuretty)
    -   [[2.2] [/etc/pam.d/system-auth]](#.2Fetc.2Fpam.d.2Fsystem-auth)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Can\'t determine the TTY]](#Can.27t_determine_the_TTY)
    -   [[3.2] [Can\'t log in]](#Can.27t_log_in)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [pam_securetty.so]

The [pam_securetty.so] module allows the system administrator to restrict the [TTYs] that [root] is able to authenticate on. The module first checks if a plaintext file [/etc/securetty] exists and is not [world] writable. If the file exists and the tests pass, the contents will be used as a list of \"secure\" [TTYs].

This module only affects [root]. If enabled, [pam_securetty.so] will always return `PAM_SUCCESS` for authentication attempts by [non-root] users.

## [Configuration]

### [][/etc/securetty]

The format of [/etc/securetty] is one device name per line, without the [/dev] prefix. The following example states that [/dev/tty1] and [/dev/tty2], as well as the implicit kernel [console] device, are secure. Authentication attempts on any other [TTYs] will be rejected.

[FILE] **`/etc/securetty`**

    tty1
    tty2

** Important**\
This file must **must not** be [world] writable.

### [][/etc/pam.d/system-auth]

[/etc/pam.d/system-auth] is used to configure the rules that PAM follows whenever system authentication needs to be done. This applies to physical logins as well as [su] and anything else which utilizes PAM\'s authentication capabilities. Taking a backup of the current PAM configuration will make it easy to revert changes if needed.

** Warning**\
A broken PAM configuration can result in every user (including [root]) being locked out of the system. Leaving a spare [root] login session open (such as in a [TTY]) while editing the configuration files will save having to boot from a live USB or through single-user mode to fix PAM.

An example PAM configuration snippet which uses the [pam_securetty.so] module is:

[FILE] **`/etc/pam.d/system-auth`**

    auth    required                    pam_securetty.so
    auth    [success=1 default=ignore]  pam_unix.so         nullok try_first_pass
    auth    [default=die]               pam_faillock.so     authfail

The module also provides an option, `noconsole`, which rejects authentication attempts on the kernel [console] unless that device is also specified in [/etc/securetty].

## [Troubleshooting]

### [][Can\'t determine the TTY]

If [/var/log/auth.log] contains an entry, such as the following, then PAM is unable to determine the [TTY] that an authenticating service is running on and will reject the authentication attempt:

[FILE] **`/var/log/auth.log`**

    Jan  1 00:00:01 hostname service: pam_securetty(service:auth): cannot determine user's tty
    Jan  1 00:00:01 hostname unix_chkpwd[11111]: password check failed for user (root)
    Jan  1 00:00:01 hostname service: pam_unix(service:auth): authentication failure; logname= uid= euid= tty= ruser= rhost=  user=root

A likely cause is that [service] is either not setting the `PAM_TTY` variable correctly or is otherwise unable to set it reliably. A workaround is to use the [pam_succeed_if.so] module to skip the [pam_securetty.so] checks for that service:

[FILE] **`/etc/pam.d/system-auth`**

    auth    [success=1 default=ignore]  pam_succeed_if.so   quiet_fail service = service
    auth    required                    pam_securetty.so
    auth    [success=1 default=ignore]  pam_unix.so         nullok try_first_pass
    auth    [default=die]               pam_faillock.so     authfail

** Warning**\
This negates the effects of [pam_securetty.so]. Only use if there isn\'t another option available and [service] is trusted. A better solution would be to see if [service] can be updated/improved to support `PAM_TTY`.

The `quiet_fail` option means that [pam_succeed_if.so] will not log failed tests. Without it, every PAM authentication attempt *not* originating from [service] would contain a line stating the test failed. To not log successes or failures, use the `quiet` option instead. These options help keep [/var/log/auth.log] a bit tidier.

### [][Can\'t log in]

If no user can log in, then the PAM configuration is likely broken. If there is still an active [root] login session available, then simply edit the current configuration or revert to the backup mentioned above. [See here](https://wiki.gentoo.org/wiki/YubiKey#Troubleshooting "YubiKey") for instructions on how to fix it if no [root] login sessions are available (e.g. after a reboot).

## [See also]

-   [PAM](https://wiki.gentoo.org/wiki/PAM "PAM") --- allows (third party) services to provide an authentication module for their service which can then be used on PAM enabled systems.
-   [YubiKey](https://wiki.gentoo.org/wiki/YubiKey "YubiKey") --- a hardware security device that can be used to safely store cryptographic keys, OTP tokens, and challenge response seeds
-   [Google Authenticator](https://wiki.gentoo.org/wiki/Google_Authenticator "Google Authenticator") --- describes an easy way to setup two-factor authentication on Gentoo.
-   [OATH-Toolkit](https://wiki.gentoo.org/wiki/OATH-Toolkit "OATH-Toolkit") --- toolkit for (OTP) One-Time Password authentication using HOTP/TOTP algorithms.

## [External resources]

-   [pam.conf(5)](//www.man7.org/linux/man-pages/man5/pam.conf.5.html), the [man] page describing PAM configuration files.
-   [pam_securetty(8)](//www.man7.org/linux/man-pages/man8/pam_securetty.8.html), the [man] page for the PAM module.
-   [pam_succeed_if(8)](//www.man7.org/linux/man-pages/man8/pam_succeed_if.8.html), the [man] page for the PAM module.