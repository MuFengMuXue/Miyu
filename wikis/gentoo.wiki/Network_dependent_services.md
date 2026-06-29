**[] Deprecated article**\
\

This article is **deprecated (obsolete)**. Contents are [no longer relevant], and are intended for historical reference only!

\
TLDR: **Do not use this article!**

Services like netmount or fetchmail which depend on an available network connection could be started/stopped with the following setup:^[\[1\]](#cite_note-bug522206-1)^

## Contents

-   [[1] [Precondition]](#Precondition)
-   [[2] [Implementation]](#Implementation)
-   [[3] [Result]](#Result)
-   [[4] [References]](#References)

### [Precondition]

Precondition is that [network management](https://wiki.gentoo.org/wiki/Network_management "Network management") is done with [dhcpcd](https://wiki.gentoo.org/wiki/Network_management_using_DHCPCD "Network management using DHCPCD").

### [Implementation]

Get the patch for dhcpcd:^[\[2\]](#cite_note-2)^

`root `[`#`]`mkdir -p /etc/portage/patches/net-misc/dhcpcd-6.9.0`

`root `[`#`]`wget `[`https://522206.bugs.gentoo.org/attachment.cgi?id=402858`](https://522206.bugs.gentoo.org/attachment.cgi?id=402858)` -P /etc/portage/patches/net-misc/dhcpcd-6.9.0`

Get the patch for openrc:^[\[3\]](#cite_note-3)^

`root `[`#`]`mkdir -p /etc/portage/patches/sys-apps/openrc-0.13.11`

`root `[`#`]`wget `[`https://bugs.gentoo.org/attachment.cgi?id=402856`](https://bugs.gentoo.org/attachment.cgi?id=402856)` -P /etc/portage/patches/sys-apps/openrc-0.13.11`

Re-emerge both dhcpcd and openrc:

`root `[`#`]`emerge -1avt =net-misc/dhcpcd-6.6.7 =sys-apps/openrc-0.13.11`

Add one line **start_inactive=true** to the init script:^[\[4\]](#cite_note-4)^

`root `[`#`]`wget `[`https://522206.bugs.gentoo.org/attachment.cgi?id=384410`](https://522206.bugs.gentoo.org/attachment.cgi?id=384410)

`root `[`#`]`patch /etc/init.d/dhcpcd < attachment.cgi?id=384410`

Restart dhcpcd:

`root `[`#`]`/etc/init.d/dhcpcd restart`

Later versions than the presently stable of net-misc/dhcpcd and sys-apps/openrc have not been tested with these patches. It does not work for [sys-apps/openrc-0.16.4](https://bugs.gentoo.org/show_bug.cgi?id=522206#c38).

### [Result]

Services having \"need net\" in their init.d scripts like fetchmail would then start after dhcpcd is started.

[FILE] **`/etc/init.d/fetchmail`**

    #!/sbin/runscript

    piddir=$
    pid_file=$/$.pid
    rcfile=/etc/$rc

    depend()

`root `[`#`]`eselect rc start fetchmail `

    Starting init script
    dhcpcd          * Starting DHCP Client Daemon ...
    fetchmail       * WARNING: fetchmail is scheduled to start when dhcpcd has started            [ ok ]

They will be stopped when dhcpcd turns inactive and will be restarted when dhcpcd is back.

`user `[`$`]`rc-config show default`

      dhcpcd                    [inactive]
      fetchmail                 [stopped]

This should be sufficient for most end user computers. For more complex requirements in dependency behaviour see [OpenRC#Dependency_behaviour](https://wiki.gentoo.org/wiki/OpenRC#Dependency_behaviour "OpenRC").

\

## [References]

1.  [[[↑](#cite_ref-bug522206_1-0)] [[[[Bug 522206 -- net-misc/dhcpcd-6.4.3 fails to start/stop network dependant services like ntpd, sshd, fetchmai]](https://bugs.gentoo.org/show_bug.cgi?id=522206)[]], [Gentoo\'s Bugzilla Main Page](https://bugs.gentoo.org/), (Last modified) April 9th, 2015. Retrieved on May 7th, 2015.]]
2.  [[[↑](#cite_ref-2)] [[[[99-openrc_dhcpcd_hook.patch, updated for epatch_user]](https://bugs.gentoo.org/show_bug.cgi?id=522206#c37)[]], [Gentoo\'s Bugzilla Main Page](https://bugs.gentoo.org/), May 8th, 2015. Retrieved on May 10th, 2015.]]
3.  [[[↑](#cite_ref-3)] [[[[runscript-background.patch, updated for epatch_user]](https://bugs.gentoo.org/show_bug.cgi?id=522206#c36)[]], [Gentoo\'s Bugzilla Main Page](https://bugs.gentoo.org/), May 8th, 2015. Retrieved on May 10th, 2015.]]
4.  [[[↑](#cite_ref-4)] [Roy Marples. [[[Mark the dhcpcd service as starting inactive]](https://bugs.gentoo.org/show_bug.cgi?id=522206#c3)[]], [Gentoo\'s Bugzilla Main Page](https://bugs.gentoo.org/), September 8th, 2014. Retrieved on May 7th, 2015.]]

\