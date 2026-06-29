**Resources**

[[]][Home](https://www.smartmontools.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/S.M.A.R.T. "wikipedia:S.M.A.R.T.")

**smartmontools** is a utility to read and monitor the S.M.A.R.T. (Self-Monitoring, Analysis and Reporting Technology) information of ATA/SATA and SCSI/SAS drives.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Hardware]](#Hardware)
    -   [[1.2] [USE flags]](#USE_flags)
    -   [[1.3] [Emerge]](#Emerge)
-   [[2] [Usage]](#Usage)
    -   [[2.1] [Invocation]](#Invocation)
    -   [[2.2] [Examples]](#Examples)
        -   [[2.2.1] [Information]](#Information)
        -   [[2.2.2] [Identify the Drive]](#Identify_the_Drive)
        -   [[2.2.3] [Activation]](#Activation)
        -   [[2.2.4] [Print health]](#Print_health)
        -   [[2.2.5] [Print capabilities]](#Print_capabilities)
        -   [[2.2.6] [Print vendor specific attributes]](#Print_vendor_specific_attributes)
        -   [[2.2.7] [Running Tests]](#Running_Tests)
        -   [[2.2.8] [Print logs]](#Print_logs)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [S.M.A.R.T. daemon]](#S.M.A.R.T._daemon)
    -   [[3.2] [OpenRC service]](#OpenRC_service)
-   [[4] [External resources]](#External_resources)

## [Installation]

### [Hardware]

S.M.A.R.T. support needs to be enabled in the [BIOS](https://wiki.gentoo.org/wiki/BIOS "BIOS") or EFI firmware for correct operation.

### [USE flags]

### [USE flags for] [sys-apps/smartmontools](https://packages.gentoo.org/packages/sys-apps/smartmontools) [[]] [Tools to monitor storage systems to provide advanced warning of disk degradation]

  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------
  [`+daemon`](https://packages.gentoo.org/useflags/+daemon)                   Install the monitoring daemon (smartd) and associated scripts.
  [`+update-drivedb`](https://packages.gentoo.org/useflags/+update-drivedb)   Install a script to update the drivedb file.
  [`caps`](https://packages.gentoo.org/useflags/caps)                         Build against sys-libs/libcap-ng to allow smartd to drop its privileges.
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                   !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`static`](https://packages.gentoo.org/useflags/static)                     !!do not set this during bootstrap!! Causes binaries to be statically linked instead of dynamically
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                   Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)             Verify upstream signatures on distfiles
  --------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-01-16 00:56] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [[[sys-apps/smartmontools]](https://packages.gentoo.org/packages/sys-apps/smartmontools)[]]:

`root `[`#`]`emerge --ask sys-apps/smartmontools`

## [Usage]

### [Invocation]

`root `[`#`]`smartctl -h`

    smartctl 7.2 2020-12-30 r5155 [x86_64-linux-5.10.61-gentoo] (local build)
    Copyright (C) 2002-20, Bruce Allen, Christian Franke, www.smartmontools.org

    Usage: smartctl [options] device

    ============================================ SHOW INFORMATION OPTIONS =====

      -h, --help, --usage
             Display this help and exit

      -V, --version, --copyright, --license
             Print license, copyright, and version information and exit

      -i, --info
             Show identity information for device

      --identify[=[w][nvb]]
             Show words and bits from IDENTIFY DEVICE data                (ATA)

      -g NAME, --get=NAME
            Get device setting: all, aam, apm, dsn, lookahead, security,
            wcache, rcache, wcreorder, wcache-sct

      -a, --all
             Show all SMART information for device

      -x, --xall
             Show all information for device

      --scan
             Scan for devices

      --scan-open
             Scan for devices and try to open each device

    ================================== SMARTCTL RUN-TIME BEHAVIOR OPTIONS =====

      -j, --json[=cgiosuvy]
             Print output in JSON or YAML format

      -q TYPE, --quietmode=TYPE                                           (ATA)
             Set smartctl quiet mode to one of: errorsonly, silent, noserial

      -d TYPE, --device=TYPE
             Specify device type to one of:
             ata, scsi[+TYPE], nvme[,NSID], sat[,auto][,N][+TYPE], usbcypress[,X], usbjmicron[,p][,x][,N], usbprolific, usbsunplus, sntjmicron[,NSID], sntrealtek, intelliprop,N[+TYPE], jmb39x[-q],N[,sLBA][,force][+TYPE], jms56x,N[,sLBA][,force][+TYPE], marvell, areca,N/E, 3ware,N, hpt,L/M/N, megaraid,N, aacraid,H,L,ID, cciss,N, auto, test

      -T TYPE, --tolerance=TYPE                                           (ATA)
             Tolerance: normal, conservative, permissive, verypermissive

      -b TYPE, --badsum=TYPE                                              (ATA)
             Set action on bad checksum to one of: warn, exit, ignore

      -r TYPE, --report=TYPE
             Report transactions (see man page)

      -n MODE[,STATUS], --nocheck=MODE[,STATUS]                     (ATA, SCSI)
             No check if: never, sleep, standby, idle (see man page)

    ============================== DEVICE FEATURE ENABLE/DISABLE COMMANDS =====

      -s VALUE, --smart=VALUE
            Enable/disable SMART on device (on/off)

      -o VALUE, --offlineauto=VALUE                                       (ATA)
            Enable/disable automatic offline testing on device (on/off)

      -S VALUE, --saveauto=VALUE                                          (ATA)
            Enable/disable Attribute autosave on device (on/off)

      -s NAME[,VALUE], --set=NAME[,VALUE]
            Enable/disable/change device setting: aam,[N|off], apm,[N|off],
            dsn,[on|off], lookahead,[on|off], security-freeze,
            standby,[N|off|now], wcache,[on|off], rcache,[on|off],
            wcreorder,[on|off[,p]], wcache-sct,[ata|on|off[,p]]

    ======================================= READ AND DISPLAY DATA OPTIONS =====

      -H, --health
            Show device SMART health status

      -c, --capabilities                                            (ATA, NVMe)
            Show device SMART capabilities

      -A, --attributes
            Show device SMART vendor-specific Attributes and values

      -f FORMAT, --format=FORMAT                                          (ATA)
            Set output format for attributes: old, brief, hex[,id|val]

      -l TYPE, --log=TYPE
            Show device log. TYPE: error, selftest, selective, directory[,g|s],
            xerror[,N][,error], xselftest[,N][,selftest], background,
            sasphy[,reset], sataphy[,reset], scttemp[sts,hist],
            scttempint,N[,p], scterc[,N,M], devstat[,N], defects[,N], ssd,
            gplog,N[,RANGE], smartlog,N[,RANGE], nvmelog,N,SIZE

      -v N,OPTION , --vendorattribute=N,OPTION                            (ATA)
            Set display OPTION for vendor Attribute N (see man page)

      -F TYPE, --firmwarebug=TYPE                                         (ATA)
            Use firmware bug workaround:
            none, nologdir, samsung, samsung2, samsung3, xerrorlba, swapid

      -P TYPE, --presets=TYPE                                             (ATA)
            Drive-specific presets: use, ignore, show, showall

      -B [+]FILE, --drivedb=[+]FILE                                       (ATA)
            Read and replace [add] drive database from FILE
            [default is +/etc/smart_drivedb.h
             and then    /var/db/smartmontools/drivedb.h]

    ============================================ DEVICE SELF-TEST OPTIONS =====

      -t TEST, --test=TEST
            Run test. TEST: offline, short, long, conveyance, force, vendor,N,
                            select,M-N, pending,N, afterselect,[on|off]

      -C, --captive
            Do test in captive mode (along with -t)

      -X, --abort
            Abort any non-captive test on device

    =================================================== SMARTCTL EXAMPLES =====

      smartctl --all /dev/sda                    (Prints all SMART information)

      smartctl --smart=on --offlineauto=on --saveauto=on /dev/sda
                                                  (Enables SMART on first disk)

      smartctl --test=long /dev/sda          (Executes extended disk self-test)

      smartctl --attributes --log=selftest --quietmode=errorsonly /dev/sda
                                          (Prints Self-Test & Attribute errors)
      smartctl --all --device=3ware,2 /dev/sda
      smartctl --all --device=3ware,2 /dev/twe0
      smartctl --all --device=3ware,2 /dev/twa0
      smartctl --all --device=3ware,2 /dev/twl0
              (Prints all SMART info for 3rd ATA disk on 3ware RAID controller)
      smartctl --all --device=hpt,1/1/3 /dev/sda
              (Prints all SMART info for the SATA disk attached to the 3rd PMPort
               of the 1st channel on the 1st HighPoint RAID controller)
      smartctl --all --device=areca,3/1 /dev/sg2
              (Prints all SMART info for 3rd ATA disk of the 1st enclosure
               on Areca RAID controller)

### [Examples]

[smartctl] is a utility that is used to control and monitor S.M.A.R.T. enabled drives.

#### [Information]

Print information of a drive, including S.M.A.R.T. support:

`root `[`#`]`smartctl -i /dev/sda`

#### [Identify the Drive]

Determine the identifier of the drive you want to enable S.M.A.R.T. for

`root `[`#`]`smartctl --scan`

#### [Activation]

Enable S.M.A.R.T. on a drive:

`root `[`#`]`smartctl -s on /dev/sda`

#### [Print health]

Print the S.M.A.R.T. health status of a drive:

`root `[`#`]`smartctl -H /dev/sda`

If the result is `PASSED`, the drive is in good health. If the result is `FAILED`, drive failure is imminent and the data should be backed up.

#### [Print capabilities]

Print the S.M.A.R.T. capabilities of a drive, including supported tests and the time required to run them:

`root `[`#`]`smartctl -c /dev/sda`

#### [Print vendor specific attributes]

Print the vendor specific S.M.A.R.T attributes of a drive:

`root `[`#`]`smartctl -A /dev/sda`

#### [Running Tests]

Discover the exceptional capabilities of smartmontools and unlock a wealth of technical insights by running comprehensive S.M.A.R.T. tests on the drive.

-   **Offline Test (offline)**:

Assess the fundamental functionality and immediate offline reliability of the drive with the Offline Test. This test offers a swift evaluation of the drive\'s basic operations, providing valuable diagnostic information. The command to embark on this diagnostic journey is as follows:

`root `[`#`]`smartctl -t offline /dev/sda`

-   **Short Self Test (short)**:

Scrutinize the critical components of the drive and conduct a focused scan of a specific disk portion with the Short Self Test. This test is designed to swiftly detect any immediate issues and provide valuable insights into the drive\'s overall health. To initiate this focused analysis, execute the following command:

`root `[`#`]`smartctl -t short /dev/sda`

-   **Extended Self Test (long)**:

Delve deep into the drive\'s surface and perform a meticulous scan of the entire disk with the Extended Self Test. This comprehensive examination provides a detailed analysis of the media\'s health and integrity, offering in-depth insights into the drive\'s overall condition. To initiate this meticulous assessment, execute the following command:

`root `[`#`]`smartctl -t long /dev/sda`

-   **Conveyance Self Test (conveyance)**:

Evaluate the drive\'s reliability under various conditions, including transportation and regular use, with the Conveyance Self Test. This test ensures the drive remains dependable and resilient in different scenarios. It is recommended to run this test after moving the drive or experiencing a power loss. To engage in this essential evaluation, execute the following command:

`root `[`#`]`smartctl -t conveyance /dev/sda`

After executing a test, carefully monitor its progress using the appropriate command to retrieve its status. It is important to note that these tests may require a significant amount of time to complete due to their thorough nature. Once the tests are finished, examine the results to determine the health status of the drive:

-   If the result indicates **PASSED**, it signifies that the drive is in good health and performing optimally, providing reassurance and peace of mind.

<!-- -->

-   If the result indicates **FAILED**, prompt action is necessary as it indicates imminent drive failure. In such cases, it is strongly advised to back up the data without delay, safeguarding against potential data loss.

By performing these tests on a regular basis, users can ensure the reliability and longevity of their drives by proactively detecting and addressing potential issues at their early stages.

-   **To cancel an ongoing test (abort-test)**:

Issue the cancellation command for the specific test in progress. The command will be similar to the one used to start the test, but with an additional parameter to cancel it.

`root `[`#`]`smartctl --abort-test=test /dev/sda`

Replace **test** with the appropriate test identifier and **/dev/sda** with the correct drive identifier.

Canceling an ongoing test is generally not dangerous to the drive or its data if done correctly. The smartmontools utility is designed to handle test cancellations gracefully, minimizing any potential adverse effects. However, keep in mind the following points:

-   Incomplete Results: Canceling a test will result in incomplete test results, which may limit the insights gained from the test. Interpret the available data with caution.

<!-- -->

-   Data Integrity: Canceling a test does not pose an immediate risk to the drive\'s data integrity. However, it is always prudent to maintain regular backups of important data to safeguard against unforeseen events.

** Note**\
It is important to exercise caution when canceling tests and consider the potential impact on the test results. If possible, it is generally recommended to allow tests to complete for accurate and comprehensive results. However, in specific situations where canceling becomes necessary or desirable, following the proper cancellation procedure should **not** pose significant dangers to the drive or its data

#### [Print logs]

Print a S.M.A.R.T. log of a drive:

`root `[`#`]`smartctl -l LOG /dev/sda`

The possible values for `LOG` include:

-   `error`: Print the S.M.A.R.T. error log. This log provides information about any errors encountered by the drive. If the result is `No Errors Logged`, it indicates that the drive is in good health. If there are some old errors, the drive is likely in good health. However, if there are numerous recent errors, it may indicate imminent drive failure, and it is recommended to back up the data.

<!-- -->

-   `selftest`: Print the S.M.A.R.T. self-test log. This log contains the results of the `short`, `long`, and `conveyance` tests. It provides insights into the drive\'s performance and health based on the outcomes of these tests.

<!-- -->

-   `selective`: Print the S.M.A.R.T. selective self-test log. This log displays the results of selective self-tests performed on the drive. It helps assess the health and reliability of specific areas or attributes of the drive.

<!-- -->

-   `background`: Print the S.M.A.R.T. background scan results log. This log shows the results of background scans performed on the drive. It helps detect and report any issues found during background scanning operations.

## [Configuration]

To send out notifications using custom scripts, place those scripts in the directory [/etc/smartd_warning.d]. To run all scripts, add `@ALL` to the `-m` directive in [/etc/smartd.conf]. If the `-m` directive also contains an email address, it should be in the following format:

[FILE] **`/etc/smartd.conf`**

    DEFAULT -m larry@example.org,@ALL
    ...

**Single Drive Monitoring:**

This configuration monitors the drive [/dev/sda], enabling automatic Attribute autosave, overall health status notifications, and per-drive S.M.A.R.T. Status notifications. Notifications will be sent to larry@example.org.

[FILE] **`/etc/smartd.conf`**

    /dev/sda -a -o on -S on -m larry@example.org

**Multiple Drives:**

This configuration monitors both [/dev/sda] and [/dev/sdb]. Each drive has the same options as in the previous example, but notifications will be sent to different email addresses.

[FILE] **`/etc/smartd.conf`**

    /dev/sda -a -o on -S on -m larry@example.org
    /dev/sdb -a -o on -S on -m perry@example.org

**Customized Schedule:**

This configuration includes a customized schedule using the `-s` option. The specified schedule runs tests on Saturday at 02:00 (`S`) and on the 3rd day of each month at 06:03 (`L`).

[FILE] **`/etc/smartd.conf`**

    /dev/sda -a -o on -S on -m larry@example.org -s (S/../.././02|L/../../6/03)

**Selective Drive Monitoring:**

This configuration selectively monitors different drives with specific options.

-   [/dev/sda] is monitored with automatic Attribute autosave, overall health status notifications, and per-drive S.M.A.R.T. Status notifications sent to larry@example.org.

<!-- -->

-   [/dev/sdb] is monitored with the same options as above, but with a customized schedule that runs tests on Saturday at 02:00 (`S`) and on the 3rd day of each month at 06:03 (`L`). Notifications will be sent to larry@example.org.

<!-- -->

-   [/dev/sdc] is monitored for overall health, with notifications sent for any error occurrences. Notifications will be sent to admin@example.com.

[FILE] **`/etc/smartd.conf`**

    /dev/sda -a -o on -S on -m larry@example.org
    /dev/sdb -a -o on -S on -m perry@example.org -s (S/../.././02|L/../../6/03)
    /dev/sdc -H -l error -m admin@example.com

### [S.M.A.R.T. daemon]

[smartd] is a daemon that continuously monitors the S.M.A.R.T. information of drives. It can be configured via [/etc/smartd.conf]. See [man smartd.conf] for more information. [smartd] will log any errors to [/var/log/messages].

In this example [smartd] monitors 4 drives and sends a test e-mail on startup. It also runs a scheduled test every week on Friday at 3:00 a.m.

[FILE] **`/etc/smartd.conf`**

    /dev/disk/by-id/ata-ST3000DM001-000000_00000000 -m alerts@example.com -M test -H -l error -l selftest -f -s L/../../5/03
    /dev/disk/by-id/ata-ST3000DM001-111111_11111111 -m alerts@example.com -M test -H -l error -l selftest -f -s L/../../5/03
    /dev/disk/by-id/ata-WDC_WD20EARS-00MVWB0_WD-000000000000 -m alerts@example.com -M test -H -l error -l selftest -f -s L/../../5/03
    /dev/disk/by-id/ata-WDC_WD20EARS-00MVWB0_WD-111111111111 -m alerts@example.com -M test -H -l error -l selftest -f -s L/../../5/03

### [OpenRC service]

[FILE] **`/etc/conf.d/smartd`**

    # Add a net dependency for the smartd service
    rc_need="net"

To start [smartd]:

`root `[`#`]`/etc/init.d/smartd start`

To start [smartd] at boot:

`root `[`#`]`rc-update add smartd default`

To debug [smartd] and check for possible configuration errors:

`root `[`#`]`smartd -d`

** Note**\
To stop the debugging instance of smartd, use [Ctrl]+[\\]

## [External resources]

-   [[[Gentoo bugtracker: known bugs]](https://bugs.gentoo.org/buglist.cgi?quicksearch=smartmontools&order=bug_id%20DESC)[]]
-   [smartmontools bugtracker: known bugs](https://www.smartmontools.org/report/1)