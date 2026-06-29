[] The information in this article is probably **outdated**. You can help the Gentoo community by verifying and [updating this article](https://wiki.gentoo.org/index.php?title=Corosync&action=edit).

**Resources**

[[]][Home](http://corosync.github.io/corosync/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Corosync_Cluster_Engine "wikipedia:Corosync Cluster Engine")

[[]][Package information](https://packages.gentoo.org/packages/sys-cluster/corosync)

[[]][GitHub](https://github.com/corosync/corosync)

**Corosync** is the currently preferred [cluster](https://wiki.gentoo.org/wiki/Cluster "Cluster") messaging layer in the Linux cluster community. It is typically used with [Pacemaker](https://wiki.gentoo.org/wiki/Pacemaker "Pacemaker") to set up Gentoo-based clusters.

## Contents

-   [[1] [Installing]](#Installing)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Download]](#Download)
    -   [[1.3] [Unmask]](#Unmask)
    -   [[1.4] [Install]](#Install)
-   [[2] [Configuring]](#Configuring)
    -   [[2.1] [Note for two-node clusters]](#Note_for_two-node_clusters)
    -   [[2.2] [Note on hostnames]](#Note_on_hostnames)
-   [[3] [Running]](#Running)
-   [[4] [Debugging]](#Debugging)
-   [[5] [Next steps]](#Next_steps)
-   [[6] [See also]](#See_also)
-   [[7] [External resources]](#External_resources)

## [Installing]

Recently there has been a fair amount of standardization-oriented changes within the Linux cluster community. Perhaps as a result, at present the version of Corosync available in the portage tree is out of date.

### [USE flags]

### [USE flags for] [sys-cluster/corosync](https://packages.gentoo.org/packages/sys-cluster/corosync) [[]] [OSI Certified implementation of a complete cluster engine]

  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`augeas`](https://packages.gentoo.org/useflags/augeas)       Enable augeas support
  [`dbus`](https://packages.gentoo.org/useflags/dbus)           Enable dbus support for anything that needs it (gpsd, gnomemeeting, etc)
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`snmp`](https://packages.gentoo.org/useflags/snmp)           Add support for the Simple Network Management Protocol if available
  [`systemd`](https://packages.gentoo.org/useflags/systemd)     Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`watchdog`](https://packages.gentoo.org/useflags/watchdog)   Enable watchdog support
  [`xml`](https://packages.gentoo.org/useflags/xml)             Add support for XML files
  ------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2024-03-17 06:17] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Download]

To get the absolutely latest version of Corosync installed (usually a good idea), you can take the following steps.

First, download the \'git HEAD\' (latest release) *corosync* ebuild from [here](https://bugs.gentoo.org/attachment.cgi?id=320006) ([[[bug #429416]](https://bugs.gentoo.org/show_bug.cgi?id=429416)[]]) and temporarily install it to an [ebuild repository](https://wiki.gentoo.org/wiki/Ebuild_repository "Ebuild repository").

`root `[`#`]`mkdir -p /usr/local/portage/sys-cluster/corosync `

`root `[`#`]`cd /usr/local/portage/sys-cluster/corosync `

`root `[`#`]`wget -O corosync-9999.ebuild 'https://bugs.gentoo.org/attachment.cgi?id=320006' `

`root `[`#`]`ebuild corosync-9999.ebuild manifest `

You can also unmask and emerge the latest version from portage which is pretty recent.

### [Unmask]

Next, unmask the package:

`root `[`#`]`echo '=sys-cluster/corosync-9999' >>/etc/portage/package.unmask`

If you are on amd64 or another untested architecture, you may also need to do the following:

`root `[`#`]`echo '=sys-cluster/corosync-9999' >>/etc/portage/package.accept_keywords`

### [Install]

Now install corosync:

`root `[`#`]`emerge --ask sys-cluster/corosync`

## [Configuring]

Gentoo installs the example corosync configuration in to [/etc/corosync/corosync.conf.example]. First copy this to [/etc/corosync/corosync.conf]:

`root `[`#`]`cp /etc/corosync/corosync.conf.example /etc/corosync/corosync.conf`

Then edit the file to express your appropriate configuration. The main resources for configuration are the [man pages](https://wiki.gentoo.org/wiki/Man_page "Man page"), accessible via:

`user `[`$`]`man corosync_overview `

`user `[`$`]`man corosync.conf `

For the *quorum* section, you can also review:

`user `[`$`]`man votequorum`

### [Note for two-node clusters]

If you only have two nodes, you will need to enable the *two_nodes* directive under the *quorum* section, ie:

    quorum

### [Note on hostnames]

When building clusters with Corosync and Pacemaker, the primary management tool **crm_mon** will identify hosts based upon their hostname. Therefore it is desirable to set a hostname that is definitely unique on each node. You can achieve this easily in one of two ways, either setting up hostname entries on your DHCP server (if nodes are DHCP configured), or by setting the hostname from a unique identifier (such as the eth0 MAC address). Here\'s my hack for the latter, which I run from a custom [/init] (passed as a kernel option to diskless nodes with [NFS](https://wiki.gentoo.org/wiki/NFS "NFS") root):

    # set hostname
    hostname `cat /sys/class/net/eth0/address|sed 's/://'`
    echo "hostname=\"`hostname`\"" >/etc/conf.d/hostname

If you find yourself with the cluster remembering old/wrong hostname for nodes and you are still in the testing phase, then you can resolve the issue by shutting down all cluster nodes, removing their [/var/lib/corosync/ring\*] cache files, and restarting. This might not be a good idea on live clusters.

## [Running]

Corosync is managed as a standard [OpenRC](https://wiki.gentoo.org/wiki/OpenRC "OpenRC") service, ie. you can start and stop it as follows.

`root `[`#`]`/etc/init.d/corosync start`

`root `[`#`]`/etc/init.d/corosync restart`

`root `[`#`]`/etc/init.d/corosync status`

`root `[`#`]`/etc/init.d/corosync stop`

## [Debugging]

Corosync logs to [/var/log/cluster/corosync.log] by default. To view the log, run:

`user `[`$`]`tail -f /var/log/cluster/corosync.log`

If you are having issues even starting Corosync successful (such as receiving \"Status: crashed\" when executing */etc/init.d/corosync status*), then you can start the daemon manually with the -f (foreground) option as follows. (You might also consider first enabling the *log_to_stderr* directive within [/etc/corosync/corosync.conf]):

`root `[`#`]`/usr/sbin/corosync -f`

## [Next steps]

Once you have corosync installed and talking between a couple of machines, you may wish to move on to installing [Pacemaker](https://wiki.gentoo.org/wiki/Pacemaker "Pacemaker").

## [See also]

-   [Cluster](https://wiki.gentoo.org/wiki/Cluster "Cluster") --- a set of computers that cooperate together to provide some service or perform some action.
-   [Logrotate](https://wiki.gentoo.org/wiki/Logrotate "Logrotate") --- a tool to periodically rotate (archive), delete, and optionally compress and/or mail historic log files.

## [External resources]

-   For help with configurations, try #linux-cluster (Corosync-oriented) on Libera Chat [IRC](https://wiki.gentoo.org/wiki/IRC "IRC").