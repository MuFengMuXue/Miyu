**Resources**

[[]][Home](https://www.clamav.net/)

[[]][Package information](https://packages.gentoo.org/packages/app-antivirus/clamav)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Clam_AntiVirus "wikipedia:Clam AntiVirus")

**ClamAV** is an open-source (GPL-2) anti-virus engine. The base package ([[[app-antivirus/clamav]](https://packages.gentoo.org/packages/app-antivirus/clamav)[]]) provides a number of utilities, including a daemon ([clamd]), a command line scanner ([clamscan]), an on-access file scanner ([clamonacc]), and a tool for fetching updates ([freshclam]).

ClamAV is a flexible tool, and can be used in many different ways including:

-   Providing email virus scanning as part of a mail gateway.
-   Web scanning.
-   Endpoint Security (desktop scanning).

This is often accomplished by an application or service calling ClamAV as part of its workflow, for example Postfix ([[[mail-mta/postfix]](https://packages.gentoo.org/packages/mail-mta/postfix)[]]) can be [configured to connect](https://wiki.gentoo.org/wiki/Complete_Virtual_Mail_Server/amavisd_spamassassin_clamav#Installation_2 "Complete Virtual Mail Server/amavisd spamassassin clamav") to a ClamAV daemon listening for connections on the system.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Update detection database]](#Update_detection_database)
    -   [[1.4] [Quick test of clamscan]](#Quick_test_of_clamscan)
    -   [[1.5] [Services]](#Services)
        -   [[1.5.1] [OpenRC]](#OpenRC)
        -   [[1.5.2] [Systemd]](#Systemd)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Integration with mail-filter/amavisd-new]](#Integration_with_mail-filter.2Famavisd-new)
    -   [[2.2] [On-access file scanning]](#On-access_file_scanning)
    -   [[2.3] [Additional clamonacc configuration]](#Additional_clamonacc_configuration)
    -   [[2.4] [ClamAV GUI]](#ClamAV_GUI)
-   [[3] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [app-antivirus/clamav](https://packages.gentoo.org/packages/app-antivirus/clamav) [[]] [Clam Anti-Virus Scanner]

  --------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+clamapp`](https://packages.gentoo.org/useflags/+clamapp)                             Build applications (clamscan, clamd, clamdscan, clamonacc (also has its own USE flag), sigtool, clambc, clamav-milter (also requires milter USE flag), clamdtop, clamsubmit, clamconf).
  [`+system-mspack`](https://packages.gentoo.org/useflags/+system-mspack)                 Use dev-libs/libmspack instead of the version bundled with ClamAV
  [`bzip2`](https://packages.gentoo.org/useflags/bzip2)                                   Enable bzip2 compression support
  [`clamdtop`](https://packages.gentoo.org/useflags/clamdtop)                             A Top like tool which shows what clamd is currently scanning amongst other things
  [`clamonacc`](https://packages.gentoo.org/useflags/clamonacc)                           Build the clamonacc on-access scanner
  [`clamsubmit`](https://packages.gentoo.org/useflags/clamsubmit)                         A tool to submit false positives / negatives
  [`debug`](https://packages.gentoo.org/useflags/debug)                                   Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`doc`](https://packages.gentoo.org/useflags/doc)                                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`experimental`](https://packages.gentoo.org/useflags/experimental)                     Enable experimental features
  [`iconv`](https://packages.gentoo.org/useflags/iconv)                                   Enable support for the iconv character set conversion library
  [`libclamav-only`](https://packages.gentoo.org/useflags/libclamav-only)                 Bypass building of libfreshclam and the ClamAV CLI applications.
  [`metadata-analysis-api`](https://packages.gentoo.org/useflags/metadata-analysis-api)   Enables collection of file property metadata using ClamAV API for analysis by ClamAV bytecode programs.
  [`milter`](https://packages.gentoo.org/useflags/milter)                                 Add sendmail mail filter (milter) support
  [`rar`](https://packages.gentoo.org/useflags/rar)                                       RAR support
  [`selinux`](https://packages.gentoo.org/useflags/selinux)                               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`systemd`](https://packages.gentoo.org/useflags/systemd)                               Enable use of systemd-specific libraries and features like socket activation or session tracking
  [`test`](https://packages.gentoo.org/useflags/test)                                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`xml`](https://packages.gentoo.org/useflags/xml)                                       DMG and XAR support
  --------------------------------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-10 14:57] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

First, install ClamAV:

`root `[`#`]`emerge --ask app-antivirus/clamav`

### [Update detection database]

Run [freshclam] to download the latest ClamAV detection database.

`root `[`#`]`freshclam`

### [Quick test of clamscan]

On-access scanning is discussed below. Scan a directory to validate the installation:

`user `[`$`]`clamscan ~`

    ...
    ----------- SCAN SUMMARY -----------
    Known viruses: 7162024
    Engine version: 0.102.3
    Scanned directories: 1
    Scanned files: 36
    Infected files: 0
    Data scanned: 44.62 MB
    Data read: 39.45 MB (ratio 1.13:1)
    Time: 12.278 sec (0 m 12 s)

### [Services]

#### [OpenRC]

Start the ClamAV and freshclam services, and add them to the default runlevel:

`root `[`#`]`rc-service freshclam start `

`root `[`#`]`rc-update add freshclam default `

`root `[`#`]`rc-service clamd start `

`root `[`#`]`rc-update add clamd default `

[clamav-milter] or [clamonacc] services may likewise require starting.

#### [Systemd]

Start the ClamAV and freshclam services, and make them start at boot time:

** Important**\
In a SystemD scenario, the clamav package currently provides **two** different service definitions: one for clamav as well as freshclam and contains two sets of services *clamav-daemon.service* & *clamav-freshclam.service*, versus *clamd.service* & *freshclamd.service*. **Use only the first ones** in the example below, as the alternatives start the daemons in the background (not systemd\'s philosophy).

`root `[`#`]`systemctl start clamav-daemon.service `

`root `[`#`]`systemctl start clamav-freshclam.service `

`root `[`#`]`systemctl enable clamav-daemon.service `

`root `[`#`]`systemctl enable clamav-freshclam.service `

## [Configuration]

The default Gentoo configuration of [clamd] is usable for both desktop systems and mail servers; changes can be made to [/etc/clamav/clamd.conf] if the defaults are not suitable. If the desired functionality is the ability to scan files for viruses on demand, no changes need to be made.

The ClamAV daemon on Gentoo (under both OpenRC and systemd) creates a world-writable socket at [/run/clamav/clamd.ctl]. Users who want to scan a file or directory should ask the [clamd] daemon to do it using the [clamdscan \--fdpass] command:

`user `[`$`]`clamdscan --fdpass /etc/clamd.conf `

    /etc/clamd.conf: OK

    ----------- SCAN SUMMARY -----------
    Infected files: 0
    Time: 0.313 sec (0 m 0 s)
    Start Date: 2020:10:23 09:16:19
    End Date:   2020:10:23 09:16:19

The `--fdpass` option sends a file descriptor to clamd rather than a path name, and avoids the need for the [clamav] user to be able to read everyone\'s files. As a result, the daemon should be able to run as the default [clamav] user in any scenario. The administrator should not have to mess with any users or groups.

** Warning**\
Do not change the user or group that clamd runs. In particular, doing so will invalidate the socket permissions expected by the service scripts.

### [][Integration with [[[mail-filter/amavisd-new]](https://packages.gentoo.org/packages/mail-filter/amavisd-new)[]]]

This works \"out of the box\" after configuring amavis to use [clamdscan \--fdpass] to invoke the virus scanner. For example,

[FILE] **`/etc/amavisd.conf`**

    # Use clamdscan with the --fdpass option so that the "clamav" user doesn't
    # need to be able to read amavis's private working directory.
    @av_scanners = (
      ['ClamAV-clamdscan', 'clamdscan', "--fdpass --stdout --no-summary ",
        [0], qr/:.*\sFOUND$/m, qr/^.*?: (?!Infected Archive)(.*) FOUND$/m ],
    );

Contrary to many how-to documents scattered about the internet, *it is not required to change any users or groups to make amavisd-new work with ClamAV.*

### [On-access file scanning]

** Important**\
The [clamonacc] service is separate from but relies upon the [clamd] service.

On Linux systems ClamAV is able to use the [fanotify](https://man7.org/linux/man-pages/man7/fanotify.7.html) API to perform on-access file scanning of nominated directories. [clamonacc] is the included utility that provides this functionality and it shares its configuration with [clamd] in [/etc/clamd.conf]

[KERNEL] **Enable fanotify**

    File Systems --->
        [*] Filesystem wide access notification
        [*] fanotify permissions checking

In the following example the [/home] directory will be recursively watched by [clamonacc]:

[FILE] **`/etc/clamd.conf`**

    OnAccessPrevention yes
    OnAccessIncludePath /home
    OnAccessExcludeUname clamav

** Warning**\
Like [clamscan], [clamonacc] accepts the `--fdpass` flag to allow [clamd] to scan files that the [clamav] user cannot access, such as user home directories. However, the [clamonacc] service does not provide `--fdpass` by default. This can lead to errors in [/var/log/clamav/clamd.log] like

[CODE]

    Sun Oct  5 00:02:42 2025 -> WARNING: File path check failure for: /home/larry/eicar.com.txt

By default, such scanning failures will not prevent access. To avoid this, users may edit the [services](#Services) files to add `--fdpass`. [The service does not currently provide a separate configuration file for this purpose.](https://bugs.gentoo.org/787233)

** Note**\
ClamAV [provides](https://docs.clamav.net/manual/Usage/Configuration.html) some documentation for configuring [clamonacc] that may be useful.

Download an eicar test file to a location within the include path.

`user `[`$`]`wget https://www.eicar.org/download/eicar.com`

Start [clamonacc] to test the configuration

`root `[`#`]`rc-service clamonacc start`

Attempt to access the eicar test file ([clamonacc] should prevent it):

`user `[`$`]`cat ~/eicar.com`

    cat: eicar.com: Operation not permitted

### [Additional clamonacc configuration]

If the default [clamonacc] performance is insufficient, and there are available system resources, the following configuration values can be adjusted (increased from the default) in [/etc/clamd.conf]:

-   MaxQueue
-   MaxThreads
-   OnAccessMaxThreads

### [ClamAV GUI]

[[[app-antivirus/clamtk]](https://packages.gentoo.org/packages/app-antivirus/clamtk)[]] can be installed to provide users with a GUI for that can (among other things): configure [clamd] scan settings, schedule scans of user home directories, and launch on-demand scans of individual files or folders.

`root `[`#`]`emerge --ask app-antivirus/clamtk`

## [External resources]

-   [ClamAV](https://wiki.archlinux.org/index.php/ClamAV) (Arch Wiki)