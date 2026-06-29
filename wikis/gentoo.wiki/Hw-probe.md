**Resources**

[[]][Home](https://linux-hardware.org/?d=Gentoo)

[[]][Package information](https://packages.gentoo.org/packages/sys-apps/hw-probe)

[[]][GitHub](https://github.com/linuxhw/hw-probe/)

[![Gentoo1.png](/images/thumb/3/30/Gentoo1.png/300px-Gentoo1.png)](https://wiki.gentoo.org/wiki/File:Gentoo1.png)

[](https://wiki.gentoo.org/wiki/File:Gentoo1.png "Enlarge")

[![Gentoo2.png](/images/thumb/d/d4/Gentoo2.png/300px-Gentoo2.png)](https://wiki.gentoo.org/wiki/File:Gentoo2.png)

[](https://wiki.gentoo.org/wiki/File:Gentoo2.png "Enlarge")

[![Gentoo3.png](/images/thumb/a/a8/Gentoo3.png/300px-Gentoo3.png)](https://wiki.gentoo.org/wiki/File:Gentoo3.png)

[](https://wiki.gentoo.org/wiki/File:Gentoo3.png "Enlarge")

The [linux hardware database](https://linux-hardware.org/?d=Gentoo) is an automatically created dataset, based on information collected through the [hw-probe] utility. The information accessible on the [linux-hardware website](https://linux-hardware.org/?d=All) can help to check operability of hardware devices, view logs and find drivers.

In addition to the [[[sys-apps/hw-probe]](https://packages.gentoo.org/packages/sys-apps/hw-probe)[]] package provided in the [Gentoo repository](https://wiki.gentoo.org/wiki/Ebuild_repository#The_Gentoo_ebuild_repository "Ebuild repository"), there is [hw-probe.AppImage](https://github.com/linuxhw/hw-probe#appimage) and [a flatpak](https://flathub.org/apps/details/org.linux_hardware.hw-probe).

The database is backed up to [the linuxhw github repository](https://github.com/linuxhw/) for statistical analysis by third parties. The project is active, and there are currently new additions for Gentoo every day.

## Contents

-   [[1] [Install]](#Install)
    -   [[1.1] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Submitting information]](#Submitting_information)
    -   [[2.3] [Statistics]](#Statistics)
    -   [[2.4] [Privacy]](#Privacy)
-   [[3] [External resources]](#External_resources)

## [Install]

### [Emerge]

Install [[[sys-apps/hw-probe]](https://packages.gentoo.org/packages/sys-apps/hw-probe)[]]:

`root `[`#`]`emerge --ask sys-apps/hw-probe`

## [Usage]

### [Invocation]

`user `[`$`]`hw-probe --help `

    NAME:
      Hardware Probe (hw-probe)
      A tool to probe for hardware, check operability and find drivers

    DESCRIPTION:
      Hardware Probe (hw-probe) is a tool to probe for hardware,
      check its operability and upload result to the BSD hardware database.

      By creating probes you contribute to the "HDD/SSD Desktop-Class Reliability
      Test" study: https://github.com/linuxhw/SMART

    USAGE:
      hw-probe [options]

    EXAMPLE:
      hw-probe -all -upload

    PRIVACY:
      Private information (including the username, machine's hostname, IP addresses,
      MAC addresses, UUIDs and serial numbers) is NOT uploaded to the database.

      The tool uploads 32-byte prefix of salted SHA512 hash of MAC addresses and serial
      numbers to properly identify unique computers and hard drives. UUIDs are decorated
      in the same way, but formatted like regular UUIDs in order to save readability of
      logs. All the data is uploaded securely via HTTPS.

    INFORMATION OPTIONS:
      -h|-help
          Print this help.

      -v|-version
          Print version info.

      -dumpversion
          Print the tool version (1.6) and don't do anything else.

    GENERAL OPTIONS:
      -all
          Enable all probes.

      -probe
          Probe for hardware. Collect only
          hardware related logs.

      -logs
          Collect system logs.

      -log-level N
          Set the logging level to N.
          Available values:

            - minimal
            - default
            - maximal

      -minimal|-min
          Collect minimal number of logs. Equal to --log-level=min.

      -maximal|-max
          Collect maximal number of logs. Equal to --log-level=max.

      -enable LIST
          Comma separated list of logs to enable in addition to
          current log level.

      -disable LIST
          Comma separated list of logs to disable in current
          log level. Some logs cannot be disabled. For example,
          you can disable collecting of 'fstab', but you cannot
          disable logging of 'smartctl'.

      -printers
          Probe for printers.

      -scanners
          Probe for scanners.

      -check
          Check devices operability.

      -id|-name DESC
          Any description of the probe.

      -upload
          Upload result to the hardware database. You will get
          a permanent URL to view the probe.

          By use of this option you confirm uploading of 32-byte
          prefix of salted SHA512 hash of MAC addresses and serial
          numbers to prevent duplication of computers in the DB.

      -hwinfo-path PATH
          Path to a local hwinfo binary.

      -proxy ADDRESS:PORT
          Set outgoing http/https proxy using syntax: proxy.domain.local:3128

    INVENTORY OPTIONS:
      -i|-inventory-id ID
          Mark the probe by inventory ID.

      -generate-inventory-id
          Generate new inventory ID.

      -email ADDR
          Email for node status notifications.

    MONITORING OPTIONS:
      -start
          Start monitoring of the node.

      -stop
          Stop monitoring of the node.

      -remind-inventory
          Remind node inventory ID.

    OTHER OPTIONS:
      -save DIR
          Save probe package to DIR. This is useful if you are offline
          and need to upload a probe later (with the help of -src option).

      -src|-source PATH
          A probe to upload.

      -fix PATH
          Update list of devices and host info
          in the probe using probe data.

      -show-devices
          Show devices list.

      -show
          Show host info and devices list.

      -show-host
          Show host info only.

      -verbose
          Use with -show option to show type and status of the device.

      -pci-ids  PATH
      -usb-ids  PATH
      -sdio-ids PATH
      -pnp-ids  PATH
          Path to .ids file to read missed device names.

      -list
          List executed probes (for debugging).

      -clean
          Do nothing. Obsolete option.

      -save-uploaded
          Save uploaded probes.

      -debug|-d
          Do nothing. Obsolete option.

      -dump-acpi
          Probe for ACPI table.

      -decode-acpi
          Decode ACPI table.

      -import DIR
          Import probes from the database to DIR for offline use.

          If you are using Snap or Flatpak package, then DIR will be created
          in the sandbox data directory.

          Provide inventory ID by -i option in order to import your inventory.

    DATA LOCATION:
      Probes info is saved in the /root/HW_PROBE directory.

### [Submitting information]

Anybody can submit computer details to the database with a single command:

`root `[`#`]`hw-probe -all -upload`

    Probe for hardware ... Ok
    Reading logs ... Ok
    Uploaded to DB, Thank you!
    Probe URL: https://linux-hardware.org/?probe=65e73516b5

### [Statistics]

Creating a hardware probe contributes to following 2 projects and studies:

-   [HDD/SSD desktop-class reliability test](https://github.com/linuxhw/SMART)
-   [Devices with bad Linux-compatibility](https://github.com/linuxhw/HWInfo)

### [Privacy]

** Warning**\
Please note that a 32-byte prefix of salted SHA512 hashes of MAC addresses and serial numbers are uploaded to the server in order to properly identify unique computers and parts. These are unlikely to be reversible.

Private info is not collected. Moreover, it\'s safer to share logs by hw-probe rather than share manually, because most private data is removed or hashed at the client side before uploading.

## [External resources]

-   [https://linux-hardware.org](https://linux-hardware.org)