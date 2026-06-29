[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Fapolicyd&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

[fapolicyd] is a simple application whitelisting daemon for Linux. [fapolicyd] provides a software framework that controls the execution of applications based on a user-defined policy^[\[1\]](#cite_note-Red_Hat-1)^. It is one of the most efficient ways to prevent running untrusted and possibly malicious applications on the system.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Components]](#Components)
-   [[3] [Configuration]](#Configuration)
-   [[4] [Policy]](#Policy)
-   [[5] [Trust]](#Trust)
-   [[6] [References]](#References)

### [Installation]

`root `[`#`]`emerge --ask sys-apps/fapolicyd`

### [Components]

[fapolicyd] provides the following components:

-   The **fapolicyd service** [fapolicyd]
-   **fapolicyd command-line utility** [fapolicyd-cli]
-   **fapolicyd package manager plugins** [ebuilddb], [rpmdb], [debdb]
-   **fapolicyd rule language** see [/usr/share/fapolicyd/sample-rules/README-rules]
-   **fagenrules script** - Run to generate and update rules from fragment files.

### [Configuration]

The fapolicyd service configuration is located in [/etc/fapolicyd/]. The structure is as follows:

-   [/etc/fapolicyd/fapolicyd.trust]: contains a list of manually trusted files (the file database).
-   [/etc/fapolicyd/rules.d/]: directory for files containing allow and deny execution rules.
-   [/etc/fapolicyd.conf]: fapolicy daemon configuration options.

** Tip**\
[/var/lib/fapolicyd/] contains the fapolicyd trust database.

### [Policy]

The policy is evaluated from top to bottom with the first match winning. The current design for policy is that it is split up into units of rules that are designed to work together\[\^2\^\]\[2\]. They are copied into [/etc/fapolicyd/rules.d/]. When the service starts, the systemd service file runs [fagenrules] which assembles the units of rules into a comprehensive policy^[\[2\]](#cite_note-fapolicyd_repository-2)^.

### [Trust]

The fapolicyd framework introduces the concept of trust. An application is trusted when it is properly installed by the system package manager, and therefore it is registered in the system package manager database^[\[1\]](#cite_note-Red_Hat-1)^. The fapolicyd daemon can be configured to use the RPM database, the Deb database, or the Ebuild database as a list of trusted binaries and scripts.

## [References]

1.  [[↑ ^[1.0](#cite_ref-Red_Hat_1-0)^ ^[1.1](#cite_ref-Red_Hat_1-1)^] [[https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/assembly_blocking-and-allowing-applications-using-fapolicyd_security-hardening](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/assembly_blocking-and-allowing-applications-using-fapolicyd_security-hardening)]]
2.  [[[↑](#cite_ref-fapolicyd_repository_2-0)] [[https://github.com/linux-application-whitelisting/fapolicyd](https://github.com/linux-application-whitelisting/fapolicyd)]]