Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/SSH/de "SSH (43% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/SSH/es "SSH (26% translated)")
-   [français](https://wiki.gentoo.org/wiki/SSH/fr "SSH (22% translated)")
-   [italiano](https://wiki.gentoo.org/wiki/SSH/it "SSH (3% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/SSH/hu "SSH (89% translated)")
-   [русский](https://wiki.gentoo.org/wiki/SSH/ru "SSH (60% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/SSH/zh-cn "SSH (32% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/SSH/ja "SSH (88% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/SSH/ko "SSH (23% translated)")

**Resources**

[[]][Home](https://www.openssh.com/)

[[]][Package information](https://packages.gentoo.org/packages/net-misc/openssh)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Secure_Shell "wikipedia:Secure Shell")

[[]][ssh(1)](https://man.openbsd.org/ssh)

[[]][sshd(8)](https://man.openbsd.org/sshd)

[[]][sshd_config(5)](https://man.openbsd.org/man5/sshd_config.5)

[[]][[#openssh](ircs://irc.libera.chat/#openssh)] ([[webchat](https://web.libera.chat/#openssh)])

[![Ohloh Logo](/images/thumb/c/c1/Ohloh-logo.png/30px-Ohloh-logo.png)][Open Hub](https://www.openhub.net/p/openssh)

**SSH** (**S**ecure **SH**ell) is the ubiquitous tool for logging into and working on remote machines securely. All sensitive information is strongly encrypted, and in addition to the remote shell, SSH supports file transfer, and port forwarding for arbitrary protocols, allowing secure access to remote services. It replaces the classic [telnet](https://en.wikipedia.org/wiki/telnet "wikipedia:telnet"), [rlogin](https://en.wikipedia.org/wiki/Berkeley_r-commands "wikipedia:Berkeley r-commands"), and similar non-secure tools - but SSH is not just a remote shell, it is a complete environment for working with remote systems.

In addition to the main [ssh] command, the SSH suite of programs includes tools such as [[scp](https://wiki.gentoo.org/wiki/Scp "Scp")] (**S**ecure **C**opy **P**rogram), [[sftp](https://wiki.gentoo.org/wiki/Sftp "Sftp")] (**S**ecure **F**ile **T**ransfer **P**rotocol), or [[ssh-agent](https://wiki.gentoo.org/wiki/Keychain "Keychain")] to help with key management. The standard SSH port is port 22.

Several versions of SSH [have existed](https://www.openssh.com/history.html). Today the most popular implementation of SSH, and de-facto standard, is [OpenBSD](https://www.openbsd.org/)\'s **OpenSSH**. This comes **[pre-installed](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)") on Gentoo**, and is published under a [BSD (\"and freer\")](https://cvsweb.openbsd.org/cgi-bin/cvsweb/~checkout~/src/usr.bin/ssh/LICENCE?rev=1.20&content-type=text/plain) license.

SSH is multi-platform, and is very widely used: OpenSSH is installed by default on most Unix-like OSs, on Windows10, on MacOS, and can be installed on Android or \"jailbroken\" iOS (SSH clients are available). This makes SSH a great tool for working with heterogeneous systems.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Check install]](#Check_install)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Commands]](#Commands)
    -   [[2.2] [Escape sequences]](#Escape_sequences)
    -   [[2.3] [Passwordless authentication to a remote SSH server]](#Passwordless_authentication_to_a_remote_SSH_server)
        -   [[2.3.1] [Client]](#Client)
            -   [[2.3.1.1] [ssh-keygen]](#ssh-keygen)
            -   [[2.3.1.2] [GnuPG]](#GnuPG)
            -   [[2.3.1.3] [Trusted Platform Module (TPM)]](#Trusted_Platform_Module_.28TPM.29)
        -   [[2.3.2] [Server]](#Server)
        -   [[2.3.3] [Single machine testing]](#Single_machine_testing)
    -   [[2.4] [Remote services over ssh]](#Remote_services_over_ssh)
    -   [[2.5] [Copying files to a remote host]](#Copying_files_to_a_remote_host)
    -   [[2.6] [ssh-agent]](#ssh-agent)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Files]](#Files)
    -   [[3.2] [Create keys]](#Create_keys)
    -   [[3.3] [Server configuration]](#Server_configuration)
    -   [[3.4] [Client configuration]](#Client_configuration)
    -   [[3.5] [Intrusion prevention]](#Intrusion_prevention)
    -   [[3.6] [Service]](#Service)
        -   [[3.6.1] [OpenRC]](#OpenRC)
        -   [[3.6.2] [systemd]](#systemd)
-   [[4] [Tips]](#Tips)
    -   [[4.1] [Terminal multiplexers to preserve sessions]](#Terminal_multiplexers_to_preserve_sessions)
    -   [[4.2] [SSH over intermittent connections]](#SSH_over_intermittent_connections)
    -   [[4.3] [Open new tabs for session with Kitty terminal]](#Open_new_tabs_for_session_with_Kitty_terminal)
    -   [[4.4] [Benchmark the optimal rounds for an ed25519 key]](#Benchmark_the_optimal_rounds_for_an_ed25519_key)
-   [[5] [Troubleshooting]](#Troubleshooting)
    -   [[5.1] [Permissions are too open]](#Permissions_are_too_open)
    -   [[5.2] [Death of long-lived connections]](#Death_of_long-lived_connections)
    -   [[5.3] [New key does not get used]](#New_key_does_not_get_used)
    -   [[5.4] [X11 forwarding, not forwarding, or tunneling]](#X11_forwarding.2C_not_forwarding.2C_or_tunneling)
    -   [[5.5] [Wayland forwarding over ssh]](#Wayland_forwarding_over_ssh)
    -   [[5.6] [The current time is displayed for PrintLastLog]](#The_current_time_is_displayed_for_PrintLastLog)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installation]

### [Check install]

Deployments of Gentoo Linux should already have OpenSSH installed, as the [[[net-misc/openssh]](https://packages.gentoo.org/packages/net-misc/openssh)[]] package is part of the [system set](https://wiki.gentoo.org/wiki/System_set_(Portage) "System set (Portage)"). The presence and proper functioning of OpenSSH can be checked by running the [ssh] command, which should output a usage statement:

`user `[`$`]`ssh`

    usage: ssh [-46AaCfGgKkMNnqsTtVvXxYy] [-B bind_interface]
               [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
               [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
               [-i identity_file] [-J [user@]host[:port]] [-L address]
               [-l login_name] [-m mac_spec] [-O ctl_cmd] [-o option] [-p port]
               [-Q query_option] [-R address] [-S ctl_path] [-W host:port]
               [-w local_tun[:remote_tun]] destination [command]

If no usage statement is printed, OpenSSH may be corrupt, or not installed. Try re-installation by following the [emerge section](https://wiki.gentoo.org/wiki/SSH#Emerge "SSH"), just as if rebuilding after a USE flag change. If OpenSSH were uninstalled, this should reinstall it. It should then remain installed, as part of the system set.

If this does not try to install OpenSSH, the package may have been [masked](https://wiki.gentoo.org/wiki//etc/portage/package.mask "/etc/portage/package.mask"), or even listed in [package.provided](https://wiki.gentoo.org/wiki//etc/portage/profile/package.provided "/etc/portage/profile/package.provided"), though this would be unusual.

### [USE flags]

### [USE flags for] [net-misc/openssh](https://packages.gentoo.org/packages/net-misc/openssh) [[]] [Port of OpenBSD\'s free SSH release]

  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+pie`](https://packages.gentoo.org/useflags/+pie)                       Build programs as Position Independent Executables (a security hardening technique)
  [`+ssl`](https://packages.gentoo.org/useflags/+ssl)                       Enable additional crypto algorithms via OpenSSL
  [`audit`](https://packages.gentoo.org/useflags/audit)                     Enable support for Linux audit subsystem using sys-process/audit
  [`debug`](https://packages.gentoo.org/useflags/debug)                     Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)               Add kerberos support
  [`ldns`](https://packages.gentoo.org/useflags/ldns)                       Use LDNS for DNSSEC/SSHFP validation.
  [`legacy-ciphers`](https://packages.gentoo.org/useflags/legacy-ciphers)   Enable support for deprecated, soon-to-be-dropped DSA keys. See https://marc.info/?l=openssh-unix-dev\>m=170494903207436\>w=2.
  [`libedit`](https://packages.gentoo.org/useflags/libedit)                 Use the libedit library (replacement for readline)
  [`livecd`](https://packages.gentoo.org/useflags/livecd)                   Enable root password logins for live-cd environment.
  [`pam`](https://packages.gentoo.org/useflags/pam)                         Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`security-key`](https://packages.gentoo.org/useflags/security-key)       Include builtin U2F/FIDO support
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                 !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)                   !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`test`](https://packages.gentoo.org/useflags/test)                       Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)           Verify upstream signatures on distfiles
  [`xmss`](https://packages.gentoo.org/useflags/xmss)                       Enable XMSS post-quantum authentication algorithm
  ------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-05 16:07] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

After changing USE flags [just for the OpenSSH package](https://wiki.gentoo.org/wiki//etc/portage/package.use "/etc/portage/package.use"), rebuild OpenSSH for the new flags to be applied. As OpenSSH is in the system set, `--oneshot` should be used to avoid adding it to the [world file](https://wiki.gentoo.org/wiki/Selected-packages_set_(Portage) "Selected-packages set (Portage)"):

`root `[`#`]`emerge --ask --changed-use --oneshot net-misc/openssh`

After changing any global USE flags in [make.conf](https://wiki.gentoo.org/wiki/Make.conf "Make.conf") that affect the OpenSSH package, emerge world to update to the new USE flags:

`root `[`#`]`emerge --ask --verbose --update --deep --newuse @world`

## [Usage]

### [Commands]

OpenSSH provides several commands, see each command\'s [man page](https://wiki.gentoo.org/wiki/Man_page "Man page") for usage information:

-   [[[scp(1)]](https://man.archlinux.org/man/scp.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - secure file copy
-   [[[sftp(1)]](https://man.archlinux.org/man/sftp.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - secure file transfer
-   [[[ssh-add(1)]](https://man.archlinux.org/man/ssh-add.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - add private key identities to the authentication agent
-   [[[ssh-agent(1)]](https://man.archlinux.org/man/ssh-agent.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - authentication agent
-   [[[ssh-copy-id(1)]](https://linux.die.net/man/1/ssh-copy-id)][[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page") - use locally available keys to authorize logins on a remote machine
-   [[[ssh-keygen(1)]](https://man.archlinux.org/man/ssh-keygen.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - authentication key utility
-   [[[ssh-keyscan(1)]](https://man.archlinux.org/man/ssh-keyscan.1.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - gather SSH public keys from servers
-   [[[sshd(8)]](https://man.archlinux.org/man/sshd.8.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] - OpenSSH daemon

### [Escape sequences]

During an active SSH session, pressing the tilde ([\~]) key starts an escape sequence. Enter the following for a list of options:

`ssh>``~?`

Note that escapes are only recognized immediately after a newline. They may not always work with some shells, such as [fish](https://wiki.gentoo.org/wiki/Fish "Fish").

### [Passwordless authentication to a remote SSH server]

Handy for [git](https://wiki.gentoo.org/wiki/Git "Git") server management.

** See also**\
For more details see the [Security Handbook](https://wiki.gentoo.org/wiki/Security_Handbook/Securing_services#SSH "Security Handbook/Securing services").

** Warning**\
Leaving the passphrase empty implies the private key file will not be encrypted. An attacker having access to the local filesystem will be able to read the private key.

** Note**\
The default file names of the keys must not be changed, or the server may persist in asking for a password even after running `ssh-copy-id`. The file name will be one of:

-   [id_rsa]
-   [id_ecdsa]
-   [id_ed25519]

depending on the key algorithm used.

Make sure an account for the user exists on the server. The clients\' [id_ed25519.pub] will be copied to the server\'s [\~/.ssh/authorized_keys] file in the user\'s home directory.

#### [Client]

##### [ssh-keygen]

Clients need public and private keys. A pair may be created with (of course, **not entering** a passphrase):

`user `[`$`]`ssh-keygen -t ed25519`

    Generating public/private ed25519 key pair.
    Enter file in which to save the key (/home/larry/.ssh/id_ed25519):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    Your identification has been saved in /home/larry/.ssh/id_ed25519
    Your public key has been saved in /home/larry/.ssh/id_ed25519.pub
    The key fingerprint is:
    SHA256:riDdFuPhN7alEsAvm717gM1IZBP3DYXGo5apQG7OUM1 larry@client
    The key's randomart image is:
    +--[ED25519 256]--+
    | .+   ..+o.      |
    | o +   Ao+.o     |
    |. o A Oo  . .    |
    | =   + .o +      |
    |  o   . S= + .   |
    |     . *. B + .  |
    |      o.=  * o   |
    |     ...+ = .    |
    |      .. .+=     |
    +----[SHA256]-----+

Then authorize the public key with the server:

`user `[`$`]`ssh-copy-id -i ~/.ssh/id_ed25519.pub <username>@<server>`

    /usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/larry/.ssh/id_ed25519.pub"
    /usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
    /usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
    larry@<server>'s password:

    Number of key(s) added: 1

    Now try logging into the machine, with:   "ssh '<server>'"
    and check to make sure that only the key(s) you wanted were added.

Afterwards a passwordless login should be possible doing:

`user `[`$`]`ssh <server>`

    larry@<server>

##### [GnuPG]

See [Usage of GPG keys instead of SSH keys](https://wiki.gentoo.org/wiki/Hetzner_Cloud_(ARM64)#Usage_of_GPG_keys_instead_of_SSH_keys "Hetzner Cloud (ARM64)").

\

##### [][Trusted Platform Module (TPM)]

See [Using a TPM for your SSH keys](https://wiki.gentoo.org/wiki/Trusted_Platform_Module/SSH "Trusted Platform Module/SSH").

#### [Server]

The file [/etc/ssh/sshd_config] should be set to `PasswordAuthentication no` after the client adds their public key.

Then [restart the sshd service](https://wiki.gentoo.org/wiki/SSH#Service "SSH") to authenticate without passwords.

#### [Single machine testing]

The above procedure can be tested out locally:

`user `[`$`]`ssh-keygen -t ed25519`

    Generating public/private ed25519 key pair.
    Enter file in which to save the key (/home/larry/.ssh/id_ed25519):
    Enter passphrase (empty for no passphrase):
    Enter same passphrase again:
    ...

`user `[`$`]`mv ~/.ssh/id_ed25519.pub ~/.ssh/authorized_keys`

`user `[`$`]`ssh localhost`

### [Remote services over ssh]

SSH may be used to access remote services, such as HTTP, HTTPS, fileshares, etc., through an encrypted \"tunnel\". Remote service access is detailed in the [SSH tunneling](https://wiki.gentoo.org/wiki/SSH_tunneling "SSH tunneling") and [SSH jump host](https://wiki.gentoo.org/wiki/SSH_jump_host "SSH jump host") articles.

### [Copying files to a remote host]

The [SFTP](https://wiki.gentoo.org/wiki/SFTP "SFTP") command, a part of SSH, uses the SSH File Transfer Protocol to copy files to a remote host. [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") is also an alternative for this.

** Note**\
The [OpenSSH 8.0 release notes](https://www.openssh.com/txt/release-8.0), from 2019, state \"*The scp protocol is outdated, inflexible and not readily fixed. We recommend the use of more modern protocols like sftp and rsync for file transfer instead.*\". The [OpenSSH 8.8 release notes](https://www.openssh.com/txt/release-8.8), from 2021, state \"*A near-future release of OpenSSH will switch scp(1) from using the legacy scp/rcp protocol to using SFTP by default.*\".

### [ssh-agent]

OpenSSH comes with [ssh-agent], a daemon to cache and prevent from frequent ssh password entries. When run, the environment variable `SSH_AUTH_SOCK` is used to point to ssh-agent\'s communication socket. The normal way to setup [ssh-agent] is to run it as the top most process of the user\'s session. Otherwise the environment variables will not be visible inside the session.

Depending on the way the graphical user session is configured to launch, it can be tricky to find a suitable way to launch [ssh-agent]. As an example for the [lightdm] display manager, edit and change [/etc/lightdm/Xsession] from:

`user `[`$`]`exec $command `

into:

`user `[`$`]`exec ssh-agent $command `

To tell [ssh-agent] the password once per session, either run `ssh-add` manually or make use of the `AddKeysToAgent` option.

Recent [Xfce](https://wiki.gentoo.org/wiki/Xfce "Xfce") will start [ssh-agent] (and [gpg-agent]) automatically. If both are installed both will be started which makes identity management especially with SmartCards more complicated. Either stop XFCE from autostarting at least SSH\'s agent or disable both and use the shell, X-session or similar.

`user `[`$`]`xfconf-query --channel xfce4-session --property /startup/ssh-agent/enabled --create --type bool --set false `

`user `[`$`]`xfconf-query --channel xfce4-session --property /startup/gpg-agent/enabled --create --type bool --set false `

## [Configuration]

### [Files]

-   [/etc/conf.d/sshd] - Gentoo\'s config file for sshd daemon. See man sshd for options.
-   [/etc/ssh/ssh_config] - Global (system wide) client configuration file.
-   [/etc/ssh/sshd_config] - Global (system wide) daemon configuration file.
-   [/etc/ssh/ssh_config.d/\*.conf] - Conventional sub-directory of .conf files read by ssh
-   [/etc/ssh/sshd_config.d/\*.conf] - Conventional sub-directory of .conf files read by sshd daemon.
-   [/etc/ssh/sshd_config.d/99_penalities.conf] - Conventional filename for additional configuration rules for the daemon.
-   [\~/.ssh/config] - User\'s configuration file

### [Create keys]

** Important**\
This section pertains to the keys used by the system, **not** the user keys that reside in [\~/.ssh].

In order to provide a secure shell, cryptographic keys are used to manage the encryption, decryption, and hashing functionalities offered by SSH.

On first run, the [sshd] init-script will generate all system keys if they don\'t already exist. Usually there is no need to recreate them (unless the system has been compromised), but if such a need arises, this can be done manually through the [ssh-keygen] command (RSA, ECDSA and Ed25519 algorithms):

`root `[`#`]`ssh-keygen -t rsa -b 4096 -f /etc/ssh/ssh_host_rsa_key -N "" `

`root `[`#`]`ssh-keygen -t ecdsa -f /etc/ssh/ssh_host_ecdsa_key -N "" `

`root `[`#`]`ssh-keygen -t ed25519 -f /etc/ssh/ssh_host_ed25519_key -N "" `

To reduce the attack vector, enable only one trusted algorithm, as shown below:

[FILE] **`/etc/ssh/sshd_config`**

    # Only Ed25519 host key
    HostKey /etc/ssh/ssh_host_ed25519_key

And remove other `HostKey` keys, if present.

Check that only the key with the specified algorithm is used:

`user `[`$`]`ssh-keyscan <SERVER IP>`

### [Server configuration]

The SSH server deamon can be configured by adding files to the following directory:

-   [/etc/ssh/sshd_config.d/]

It is also possible to perform further configuration in OpenRC\'s [/etc/conf.d/sshd]. For detailed information on how to configure the server read the [[[sshd_config(5)]](https://man.archlinux.org/man/sshd_config.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] man page.

The server provides means to validate its configuration using test mode:

`root `[`#`]`/usr/sbin/sshd -t`

** Important**\
Always validate the configuration changes prior restarting the service in order to keep the remote login available.

### [Client configuration]

The [ssh] client and related programs ([scp], [sftp], etc.) can be configured using the following configuration files or directories:

Per user configuration:

-   [\~/.ssh/config]

Per host configuration:

-   [/etc/ssh/ssh_config.d/\*.conf]

For more information read the [[[ssh_config(5)]](https://man.archlinux.org/man/ssh_config.5.en)[[]](https://wiki.gentoo.org/wiki/Special:MyLanguage/man_page "Special:MyLanguage/man page")] [man page](https://wiki.gentoo.org/wiki/Man_page "Man page").

### [[] Intrusion prevention]

SSH is a commonly attacked service. OpenSSH version 9.7 released a **built-in** *intrusion prevention mechanism*. To configure and activate the brute-force preventing mechanism use following configuration steps.

Create [/etc/ssh/sshd_config.d/99_penalities.conf] file with following configuration overwriting the default OpenSSH values:

[FILE] **`/etc/ssh/sshd_config.d/99_penalities.conf`**

    # IP whitelist, where penalty does not hit. Trusted networks.
    # Default is empty
    PerSourcePenaltyExemptList 192.168.0.0/16

    # Block IP subnets instead of individual IP's
    # Default value is 32:128 (IPv4/IPv6)
    PerSourceNetBlockSize 24:64

    # Block every occurrence for 3600 seconds
    # Default is crash:90 authfail:5 refuseconnection:10 noauth:1 grace-exceeded:10
    PerSourcePenalties crash:3600 authfail:3600 refuseconnection:3600 noauth:3600 grace-exceeded:3600

** Important**\
Substitute the example `192.168.0.0/16` entry with **your own trusted** IP network(s) where the penality does not hit. Source IP network(s) where you connect from to this SSHD server.

Restart the OpenSSH daemon.

`root `[`#`]`rc-service sshd restart`

Now the OpenSSH daemon blocks every brute-force attack for the configured time of 3600 seconds (1 hour). Adjust the blocking times to your liking.

Additional tools such as [sshguard](https://wiki.gentoo.org/wiki/Sshguard "Sshguard") or [fail2ban](https://wiki.gentoo.org/wiki/Fail2ban "Fail2ban") help monitor logs and can black list remote IP\'s which have repeatedly attempted yet failed to authenticate. Utilize them as needed to secure a frequently attacked system.

### [Service]

Commands to run the SSH server will depend on active init system.

#### [OpenRC]

Add the OpenSSH daemon to the default runlevel:

`root `[`#`]`rc-update add sshd default`

Start the sshd daemon with:

`root `[`#`]`rc-service sshd start`

The OpenSSH server can be controlled like any other [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC")-managed service:

`root `[`#`]`rc-service sshd start `

`root `[`#`]`rc-service sshd stop `

`root `[`#`]`rc-service sshd restart `

** Note**\
Active SSH connections to the server remain unaffected when issuing [rc-service sshd restart].

#### [systemd]

To have the OpenSSH daemon start when the system starts:

`root `[`#`]`systemctl enable sshd.service`

    Created symlink from /etc/systemd/system/multi-user.target.wants/sshd.service to /usr/lib64/systemd/system/sshd.service.

To start the OpenSSH daemon now:

`root `[`#`]`systemctl start sshd.service`

To check if the service has started:

`root `[`#`]`systemctl status sshd.service`

## [Tips]

### [Terminal multiplexers to preserve sessions]

It is possible to use a [terminal multiplexer](https://wiki.gentoo.org/wiki/Recommended_tools#Terminal_multiplexers "Recommended tools") to resume a session after a dropped connection. [Tmux](https://wiki.gentoo.org/wiki/Tmux "Tmux") and [Screen](https://wiki.gentoo.org/wiki/Screen "Screen") are two popular multiplexers that can be used to be able to reconnect to a session, even if a command was running when the connection dropped out.

### [SSH over intermittent connections]

When on unstable Internet connections, or when roaming between networks (such as when moving wifi networks), [mosh](https://wiki.gentoo.org/wiki/Mosh "Mosh") can help avoid dropping SSH sessions.

### [Open new tabs for session with Kitty terminal]

By using the [SSH kitten](https://sw.kovidgoyal.net/kitty/kittens/ssh/#opt-kitten-ssh.remote_kitty) for the [Kitty](https://wiki.gentoo.org/wiki/Kitty "Kitty") terminal emulator, it is possible to open new \"tabs\", or windows, on the current SSH session without having log in again.

Kitty also provides other practical SSH functionality.

### [Benchmark the optimal rounds for an ed25519 key]

** Tip**\
It is highly advisable to conduct benchmarking for the *ed25519* key generation process, particularly considering the default value of 16 rounds and the potential performance improvements achievable with higher round values.

[FILE] **`ssh-benchmark.sh`Benchmark SSH Ciphers**

    #!/bin/sh

    rounds="16 32 64 100 150"
    num_runs=20

    for r in $rounds; do
        printf "Benchmarking 'ssh-keygen -t ed25519 -a %s' on average:\n" "$r"
        total_time=0
        i=1
        while [ $i -le $num_runs ]; do
            start_time=$(date +%s.%N)
            ssh-keygen -t ed25519 -a "$r" -f test -N test >/dev/null 2>&1
            end_time=$(date +%s.%N)
            runtime=$(echo "$end_time - $start_time" | bc)
            total_time=$(echo "$total_time + $runtime" | bc)
            rm test >/dev/null 2>&1
            printf "Run %s: %s seconds\n" "$i" "$runtime"
            i=$((i + 1))
        done
        average_time=$(echo "scale=3; $total_time / $num_runs"| bc)
        printf "Average execution time: %s seconds\n\n" "$average_time"
    done

** Note**\
It is highly recommended to perform benchmarking for ed25519 key generation, considering both security and performance aspects. While the highest recommended round may offer superior security, it\'s essential to find the optimal balance based on individual requirements and time constraints. By conducting benchmark tests, one can evaluate the trade-off between security and performance, ensuring the selection of an appropriate round value for ed25519 keys.

Benchmarking is a crucial process to measure the performance and efficiency of a system or a specific component, such as cryptographic algorithms. In the context of SSH (Secure Shell) ciphers, it is important to determine the optimal number of rounds for generating *ed25519* keys.

The provided script, [ssh-benchmark.sh], conducts benchmarking on the [ssh-keygen] command with different round values for *ed25519* keys. The script executes the [ssh-keygen] command multiple times with varying round values and measures the execution time for each run. It then calculates the average execution time for each round value.

By benchmarking different round values, system administrators and security professionals can identify the optimal round value that strikes a balance between security and performance. Higher round values generally provide stronger security but can result in increased computational overhead. Finding the right balance ensures that *ed25519* keys are generated efficiently without compromising security.

Benchmarking helps identify potential bottlenecks, vulnerabilities, or areas that require improvement in security systems. It assists in selecting the most suitable algorithms and configurations for a particular use case, ensuring that security measures are robust and effective.

## [Troubleshooting]

There are 3 different levels of debug modes that can help troubleshooting issues. With the `-v` option SSH prints debugging messages about its progress. This is helpful in debugging connection, authentication, and configuration problems. Multiple `-v` options increase the verbosity. Maximum verbosity is three levels deep.

`user `[`$`]`ssh example.org -v `

`user `[`$`]`ssh example.org -vv `

`user `[`$`]`ssh example.org -vvv `

### [Permissions are too open]

An ssh connection will only work if the file permissions of the [\~/.ssh] directory and contents are correct.

-   The [\~/.ssh] directory permissions should be 700 (drwx\-\-\-\-\--), i.e. the owner has full access and no one else has any access.
-   Under [\~/.ssh]:
    -   public key files\' permissions should be 644 (-rw-r\--r\--), i.e. anyone may read the file, only the owner can write.
    -   all other files\' permissions should be 600 (-rw\-\-\-\-\-\--), i.e. only the owner may read or write the file.

These permissions need to be correct on the client and server.

### [Death of long-lived connections]

Many internet access devices perform Network Address Translation ([NAT](https://wiki.gentoo.org/wiki/NAT "NAT")), a process that enables devices on a private network such as that typically found in a home or business place to access foreign networks, such as the internet, despite only having a single IP address on that network. Unfortunately, not all NAT devices are created equal, and some of them incorrectly close long-lived, occasional-use TCP connections such as those used by SSH. This is generally observable as a sudden inability to interact with the remote server, even though the [ssh] client program has not exited.

In order to resolve the issue, OpenSSH clients and servers can be configured to send a \'keep alive\', or invisible message aimed at maintaining and confirming the live status of the link:

-   To enable keep alive *for all clients connecting to the local server*, set `ClientAliveInterval 30` (or some other value, in seconds) within the [/etc/ssh/sshd_config] file.
-   To enable keep alive *for all servers connected to by the local client*, set `ServerAliveInterval 30` (or some other value, in seconds) within the [/etc/ssh/ssh_config] or [\~/.ssh/config] file.
-   Set `TCPKeepAlive no` to help eliminate disconnections.

For example, to modify the server\'s configuration, add following file:

[FILE] **`/etc/ssh/sshd_config.d/01_ClientAlive.conf`Help disconnects occur less often (server)**

    # The following ClientAlive values will keep an inactive session open for 30 minutes
    ClientAliveCountMax 60
    ClientAliveInterval 30
    #
    # Deactivate TCPKeepAlive
    TCPKeepAlive no

To modify the client\'s configuration, add following file:

[FILE] **`/etc/ssh/ssh_config.d/01_ServerAlive.conf`Help disconnects occur less often (client)**

    # The following ServerAlive values will keep an inactive session open for 2 hours
    ServerAliveInterval 60
    ServerAliveCountMax 120

### [New key does not get used]

This scenario covers the case when a key to access a remote system has been created, the public key installed on the remote system, but the remote system is (for some reason) not accessible via ssh. This can happen if the name of the keyfile is not known to ssh.

Confirm which key files ssh is trying by running it with one of the verbose options, as described at the start of the [Troubleshooting section](https://wiki.gentoo.org/wiki/SSH#Troubleshooting "SSH"). The verbose output will include the names of the keyfiles it is trying, and the one (if any) that actually gets used.

The default key files for the system are listed in the [/etc/ssh/ssh_config], see the commented-out lines containing `IdentityFile` directives.

There are several ways to use a key with a non-default name.

The key name can be specified on the command line every time:

`user `[`$`]`ssh -i ~/.ssh/my_keyfile user@remotesys`

Alternatively, add following ssh configuration file to add a special case for ssh to the remote system:

[FILE] **`/etc/ssh/ssh_config/02_remotesys.conf`Define keyfiles to use for host remotesys**

    Host remotesys
        IdentityFile ~/.ssh/id_rsa
        IdentityFile ~/.ssh/my_keyfile

If any are specified, it appears to be necessary to specify *all* the desired keys on a remote host. Read up on the ssh IdentityFile.

### [][X11 forwarding, not forwarding, or tunneling]

**Problem**: After having made the necessary changes to the configuration files for permitting X11 forwarding, it is discovered X applications are executing on the server and are not being forwarded to the client.

**Solution**: What is likely occurring during SSH login into the remote server or host, the `DISPLAY` variable is either being unset or is being set *after* the SSH session sets it.

Test for this scenario perform the following after logging in remotely:

`user `[`$`]`echo $DISPLAY`

    localhost:10.0

The output should be something similar to `localhost:10.0` or `localhost2.local:10.0` using server side `X11UseLocalhost no` setting. If the usual `:0.0` is not displayed, check to make sure the `DISPLAY` variable within [\~/.bash_profile] is not being unset or re-initializing. If it is, remove or comment out any custom initialization of the `DISPLAY` variable to prevent the code in [\~/.bash_profile] from executing during a SSH login:

`user `[`$`]`ssh -t larry@localhost2 bash --noprofile`

Be sure to substitute `larry` in the command above with the proper username.

A trick that works to complete this task would be to define an alias within the users\' [\~/.bashrc] file.

### [Wayland forwarding over ssh]

[Wayland](https://wiki.gentoo.org/wiki/Wayland "Wayland")-based systems require additional software for forwarding GUI applications.

Install [Waypipe](https://wiki.gentoo.org/wiki/Waypipe "Waypipe") on both client and server:

`root `[`#`]`emerge --ask gui-apps/waypipe`

To run a remote command with [waypipe], prefix the ssh command with [waypipe]. For example to open Kate on a remote server:

`user `[`$`]`waypipe ssh <user>@<host> kate`

Further it functions like normal ssh. So to open a secure shell that can launch GUI applications:

`user `[`$`]`waypipe ssh <user>@<host>`

### [The current time is displayed for PrintLastLog]

By default, [/etc/pam.d/system-login] runs:

[CODE]

    session      optional    pam_lastlog.so silent

This updates the last login time, before `PrintLastLog` in sshd. In order for `PrintLastLog` to work, this pam line must be disabled. Alternatively, `PrintLastLog` can be disabled and the *silent* option can be removed:

[CODE]

    session      optional    pam_lastlog.so

## [See also]

-   [Autossh](https://wiki.gentoo.org/wiki/Autossh "Autossh") --- a command that detects when [SSH] connections drop and automatically reconnects them.
-   [dropbear](https://wiki.gentoo.org/wiki/Dropbear "Dropbear") --- a lightweight SSH server. It runs on a variety of POSIX-based platforms.
-   [Keychain](https://wiki.gentoo.org/wiki/Keychain "Keychain") --- This document describes how to use [SSH] shared keys along with the keychain program.
-   [Mosh](https://wiki.gentoo.org/wiki/Mosh "Mosh") --- a SSH client server that is aware of connectivity problems of the original SSH implementation.
-   [SCP](https://wiki.gentoo.org/wiki/SCP "SCP") --- an interactive file transfer program, similar to the [copy] command, that copies files over an encrypted SSH transport.
-   [SFTP](https://wiki.gentoo.org/wiki/SFTP "SFTP") --- an interactive file transfer program, similar to [FTP](https://wiki.gentoo.org/wiki/FTP "FTP"), which performs all operations over an encrypted [SSH] transport.
-   [SSHFS](https://wiki.gentoo.org/wiki/SSHFS "SSHFS") --- a secure shell client used to mount remote filesystems to local machines.
-   [SSH tunneling](https://wiki.gentoo.org/wiki/SSH_tunneling "SSH tunneling") --- a method of connecting to machines on the other side of a gateway machine.
-   [SSH jump host](https://wiki.gentoo.org/wiki/SSH_jump_host "SSH jump host") --- employed as an alternative to [SSH tunneling](https://wiki.gentoo.org/wiki/SSH_tunneling "SSH tunneling") to access internal machines through a gateway.
-   [rsync](https://wiki.gentoo.org/wiki/Rsync "Rsync") --- a powerful file sync program capable of efficient file transfers and directory synchronization.
-   [Securing the SSH service](https://wiki.gentoo.org/wiki/Security_Handbook/Securing_services#SSH "Security Handbook/Securing services") (Security Handbook)
-   [Starting the SSH daemon --- Gentoo Handbook --- Installation](https://wiki.gentoo.org/wiki/Handbook:AMD64/Installation/Media#Optional:_Starting_the_SSH_daemon "Handbook:AMD64/Installation/Media")

## [External resources]

-   [[[net-misc/connect]](https://packages.gentoo.org/packages/net-misc/connect)[]] --- [SSH Proxy Command \-- connect.c](https://github.com/gotoh/ssh-connect)
-   [https://lonesysadmin.net/2011/11/08/ssh-escape-sequences-aka-kill-dead-ssh-sessions/amp/](https://lonesysadmin.net/2011/11/08/ssh-escape-sequences-aka-kill-dead-ssh-sessions/amp/) - A blog entry on escape sequences.
-   [https://hackaday.com/2017/10/18/practical-public-key-cryptography/](https://hackaday.com/2017/10/18/practical-public-key-cryptography/) - Practical public key cryptography (Hackaday).
-   [https://www.akadia.com/services/ssh_putty.html](https://www.akadia.com/services/ssh_putty.html) - Port forwarding explained.