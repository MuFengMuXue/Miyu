[] This article is a **work in progress**; treat its contents with caution - [JM01085758](https://wiki.gentoo.org/wiki/User:JM01085758 "User:JM01085758") ([talk](https://wiki.gentoo.org/wiki/User_talk:JM01085758 "User talk:JM01085758") \| [contribs](https://wiki.gentoo.org/wiki/Special:Contributions/JM01085758 "Special:Contributions/JM01085758")).

**Resources**

[[]][manpage](https://man7.org/linux/man-pages/man7/kernel_lockdown.7.html)

Since kernel version 5.4,^[\[1\]](#cite_note-phoronix-1)^ support has been added for integrity and confidentiality lockdown modes. Lockdown is a Linux Security Module (LSM) which expands the traditional LSM focus on control once userspace is active to having an LSM enabled very early in the boot sequence, even before kmalloc() can request memory.^[\[2\]](#cite_note-2)^ Integrity mode disables features that allow userspace to modify the running kernel. Confidentiality mode does the same but goes further, also preventing extraction of confidential information.^[\[3\]](#cite_note-cmdline-3)^ Enabling either will prevent the loading of unsigned kernel modules as well as unencrypted hibernation or suspend to swap.^[\[4\]](#cite_note-man7-4)^ By default in Gentoo, neither mode is enabled, but on EFI x86 or arm64 with other distributions, lockdown may be automatically enabled when [Secure Boot](https://wiki.gentoo.org/wiki/Secure_Boot "Secure Boot") is enabled.^[\[4\]](#cite_note-man7-4)^

## Contents

-   [[1] [Background]](#Background)
-   [[2] [Kernel]](#Kernel)
-   [[3] [GRUB]](#GRUB)
-   [[4] [Impact]](#Impact)
-   [[5] [Vulnerabilities]](#Vulnerabilities)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)
-   [[8] [References]](#References)

### [Background]

The motivation for implementing this feature was \"to enforce a distinction between running as root and the ability to run code in kernel mode\".^[\[5\]](#cite_note-lwm-5)^ To quote Matthew Garrett, \"if you can run arbitrary code in the kernel then you can use the kernel to boot anything you want\",^[\[6\]](#cite_note-mjg-6)^ defeating the point of UEFI Secure Boot. Work on the lockdown LSM began in the early 2010s.^[\[7\]](#cite_note-7)^

### [Kernel]

[KERNEL] **menuconfig**

    Security options  --->
        [*] Basic module for enforcing kernel lockdown
        [*]   Enable lockdown LSM early in init
              Kernel default lockdown mode (Integrity)  --->

### [GRUB]

Lockdown modes can also be enabled via [GRUB](https://wiki.gentoo.org/wiki/GRUB "GRUB"): `GRUB_CMDLINE_LINUX="lockdown=integrity"`.^[\[3\]](#cite_note-cmdline-3)^

### [Impact]

Enabling one of the lockdown modes will affect one\'s ability to modify and/or read from the following:

-   [/dev/mem](https://wiki.gentoo.org/wiki//dev#mem "/dev")

<!-- -->

-   [/dev/kmem](https://wiki.gentoo.org/wiki//dev#kmem "/dev")

<!-- -->

-   [/dev/kcore](https://wiki.gentoo.org/wiki//dev#kcore "/dev")

<!-- -->

-   [/dev/port](https://wiki.gentoo.org/wiki//dev#port "/dev")^[\[8\]](#cite_note-8)^

<!-- -->

-   [Model-specific registers](https://wiki.gentoo.org/wiki/Model-specific_registers "Model-specific registers") (MSRs)

<!-- -->

-   [debugfs](https://wiki.gentoo.org/wiki/Debugfs "Debugfs")

A more extensive list can be seen here.^[\[4\]](#cite_note-man7-4)^

### [Vulnerabilities]

Kernels prior to 5.19 contain a trivial bypass bug, CVE-2022-21505.^[\[9\]](#cite_note-cve-9)[\[10\]](#cite_note-10)^

[CVE-2022-21499](https://access.redhat.com/security/cve/CVE-2022-21499), [patched](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=eadb2f47a3ced5c64b23b90fd2a3463f63726066) in May 2022.^[\[11\]](#cite_note-11)^

## [See also]

-   [Kernel Modules](https://wiki.gentoo.org/wiki/Kernel_Modules "Kernel Modules") --- object files that contain code to extend the [kernel](https://wiki.gentoo.org/wiki/Kernel "Kernel") of an operating system.
-   [Signed kernel module support](https://wiki.gentoo.org/wiki/Signed_kernel_module_support "Signed kernel module support") --- allows further hardening of the system by disallowing unsigned kernel modules, or kernel modules signed with the wrong key, to be loaded.
-   [Extended Verification Module](https://wiki.gentoo.org/wiki/Extended_Verification_Module "Extended Verification Module") --- used to validate security-sensitive extended attributes before allowing operations on the files.
-   [Integrity Measurement Architecture](https://wiki.gentoo.org/wiki/Integrity_Measurement_Architecture "Integrity Measurement Architecture") --- is responsible for calculating the hashes of files and programs before they are loaded

## [External resources]

-   [eBPF in kernel lockdown mode](https://lpc.events/event/7/contributions/678/attachments/580/1177/eBPF-in-kernel-lockdown-mode-short-paper.pdf)

## [References]

1.  [[[↑](#cite_ref-phoronix_1-0)] [[https://www.phoronix.com/news/Linux-5.4-Adds-Lockdown](https://www.phoronix.com/news/Linux-5.4-Adds-Lockdown)]]
2.  [[[↑](#cite_ref-2)] [[https://www.linux-magazine.com/Issues/2020/239/Lockdown-Mode](https://www.linux-magazine.com/Issues/2020/239/Lockdown-Mode)]]
3.  [[↑ ^[3.0](#cite_ref-cmdline_3-0)^ ^[3.1](#cite_ref-cmdline_3-1)^] [[https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html)]]
4.  [[↑ ^[4.0](#cite_ref-man7_4-0)^ ^[4.1](#cite_ref-man7_4-1)^ ^[4.2](#cite_ref-man7_4-2)^] [[https://man7.org/linux/man-pages/man7/kernel_lockdown.7.html](https://man7.org/linux/man-pages/man7/kernel_lockdown.7.html)]]
5.  [[[↑](#cite_ref-lwm_5-0)] [[https://lwn.net/Articles/751061/](https://lwn.net/Articles/751061/)]]
6.  [[[↑](#cite_ref-mjg_6-0)] [[https://mjg59.dreamwidth.org/50577.html](https://mjg59.dreamwidth.org/50577.html)]]
7.  [[[↑](#cite_ref-7)] [[https://www.zdnet.com/article/linux-to-get-kernel-lockdown-feature/](https://www.zdnet.com/article/linux-to-get-kernel-lockdown-feature/)]]
8.  [[[↑](#cite_ref-8)] [In the manpage, \"/dev/ioports\" is a typo.]]
9.  [[[↑](#cite_ref-cve_9-0)] [[https://www.phoronix.com/news/Linux-Fix-CVE-2022-21505](https://www.phoronix.com/news/Linux-Fix-CVE-2022-21505)]]
10. [[[↑](#cite_ref-10)] [[https://access.redhat.com/security/cve/CVE-2022-21505](https://access.redhat.com/security/cve/CVE-2022-21505)]]
11. [[[↑](#cite_ref-11)] [[https://nvd.nist.gov/vuln/detail/CVE-2022-21499](https://nvd.nist.gov/vuln/detail/CVE-2022-21499)]]