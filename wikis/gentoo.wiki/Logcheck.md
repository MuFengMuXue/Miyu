Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/Logcheck/de "Logcheck (39% translated)")
-   [English]
-   [español](https://wiki.gentoo.org/wiki/Logcheck/es "Logcheck (36% translated)")
-   [français](https://wiki.gentoo.org/wiki/Logcheck/fr "Logcheck (42% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Logcheck/hu "Logcheck (100% translated)")
-   [čeština](https://wiki.gentoo.org/wiki/Logcheck/cs "Logcheck/cs (6% translated)")
-   [русский](https://wiki.gentoo.org/wiki/Logcheck/ru "Logcheck (39% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Logcheck/zh-cn "Logcheck (39% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Logcheck/ja "logcheck (100% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/Logcheck/ko "Logcheck (36% translated)")

**logcheck** is a tool to analyze the system logs.

## Contents

-   [[1] [Getting Started With logcheck]](#Getting_Started_With_logcheck)
    -   [[1.1] [Background]](#Background)
    -   [[1.2] [Installing logcheck]](#Installing_logcheck)
    -   [[1.3] [Basic configuration]](#Basic_configuration)
    -   [[1.4] [Enable periodical log check]](#Enable_periodical_log_check)
        -   [[1.4.1] [Cron users]](#Cron_users)
        -   [[1.4.2] [Systemd users]](#Systemd_users)
-   [[2] [Troubleshooting]](#Troubleshooting)
    -   [[2.1] [General tips]](#General_tips)

## [Getting Started With logcheck]

### [Background]

[[[app-admin/logcheck]](https://packages.gentoo.org/packages/app-admin/logcheck)[]] is an updated version of [[[app-admin/logsentry]](https://packages.gentoo.org/packages/app-admin/logsentry)[]], which is a tool to analyze the system logs. Additionally, logcheck comes with a built-in database of common, not-interesting log messages to filter out the noise. The general idea of the tool is that all messages are interesting, except the ones explicitly marked as noise. logcheck periodically sends an email with a summary of interesting messages.

### [Installing logcheck]

** Important**\
It is strongly recommended to remove logsentry if it is installed on the system. Additionally, [/etc/logcheck] directory should be removed to avoid permission and file collision problem.

`root `[`#`]`emerge -c logsentry`

`root `[`#`]`rm -rf /etc/logcheck`

Next, the installation of logcheck can be proceeded.

`root `[`#`]`emerge --ask app-admin/logcheck`

### [Basic configuration]

[[[app-admin/logcheck]](https://packages.gentoo.org/packages/app-admin/logcheck)[]] creates a separate user \"logcheck\" to avoid running as root. Actually, it will refuse to run as root. To allow it to analyze the logs, it need to be sure they are readable by logcheck. Here is an example for [[[app-admin/syslog-ng]](https://packages.gentoo.org/packages/app-admin/syslog-ng)[]]:

[FILE] **`/etc/syslog-ng/syslog-ng.conf`syslog-ng configuration snippet**

    options ;

Next, reload the configuration and make sure the changes work as expected.

`root `[`#`]`/etc/init.d/syslog-ng reload `

`root `[`#`]`ls -l /var/log/messages`

    -rw-r----- 1 root logcheck 1694438 Feb 12 12:18 /var/log/messages

Some basic logcheck settings in [/etc/logcheck/logcheck.conf] need to be adjusted:

[FILE] **`/etc/logcheck/logcheck.conf`Basic /etc/logcheck/logcheck.conf setup**

    # Controls the level of filtering:
    # Can be set to "workstation", "server" or "paranoid" for different
    # levels of filtering. Defaults to server if not set.
    ## (The workstation level includes server, and server includes paranoid.
    The paranoid level filters almost no messages)
    REPORTLEVEL="server"

    # Controls the address mail goes to:
    # *NOTE* the script does not set a default value for this variable!
    # Should be set to an offsite "emailaddress@some.domain.tld"
    ## (Make sure you can receive the logcheck e-mails. Testing is strongly
    recommended)
    SENDMAILTO="root"

    # Controls if syslog-summary is run over each section.
    # Alternatively, set to "1" to enable extra summary.
    # HINT: syslog-summary needs to be installed.
    ## (If you get a lot of similar messages in the logs, you
    may want to install app-admin/syslog-summary and enable
    this setting)
    SYSLOGSUMMARY=0

It must be specified logcheck which log files to scan ([/etc/logcheck/logcheck.logfiles.d]). More files can be added into [/etc/logcheck/logcheck.logfiles.d] each of one containing a list of log files to be checked. The installation script will generate 2 files: journal.logfiles and syslog.logfiles.

[FILE] **`/etc/logcheck/logcheck.logfiles.d/syslog.logfiles`Basic setup**

    ## (This is an example for syslog-ng)
    ## Log entries in the logs listed below will be checked by logcheck

    # The default is to check standard syslog files
    # created by rsyslog or other syslog daemons

    # (If the system does not use a syslog daemon, these
    # lines can be commented out)
    #/var/log/syslog
    #/var/log/auth.log
    /var/log/messages

### [Enable periodical log check]

Finally, enable a periodical check of the log files.

#### [Cron users]

If logcheck is emerged with the [[[cron]](https://packages.gentoo.org/useflags/cron)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag enabled, it can read /etc/cron.hourly/logcheck.cron

[FILE] **`/etc/cron.hourly/logcheck.cron`Basic /etc/cron.hourly/logcheck.cron**

    #!/bin/sh
    #
    # To enable sync via cron, execute "sudo -u logcheck touch /etc/logcheck/cron-logcheck-enabled"
    if [[ ! -f /etc/logcheck/cron-logcheck-enabled ]]; then
        exit
    fi
    if [ ! -d /var/lock/logcheck ]; then
        mkdir -p /var/lock/logcheck
        chown logcheck:logcheck /var/lock/logcheck
    fi
    sudo -u logcheck nice -n10 /usr/sbin/logcheck

To enable an hourly cron job, run:

`root `[`#`]`sudo -u logcheck touch /etc/logcheck/cron-logcheck-enabled`

** Note**\
For more information about cron read the [Cron Guide](https://wiki.gentoo.org/wiki/Cron "Cron").

#### [Systemd users]

If logcheck is emerged with [[[systemd]](https://packages.gentoo.org/useflags/systemd)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE flag enabled, a logcheck.timer can be activated running:

`root `[`#`]`systemctl enable --now logcheck.timer`

Now the user will be regularly getting important log messages by email. An example message looks like this:

[CODE] **Example logcheck message**

    System Events
    =-=-=-=-=-=-=
    Feb 10 17:13:53 localhost kernel: [30233.238342] conftest[25838]: segfault at 40 ip 40061403 sp bfc443c4 error 4
    in libc-2.10.1.so[4003e000+142000]
    Feb 11 12:31:21 localhost postfix/pickup[18704]: fatal: could not find any active network interfaces
    Feb 11 12:31:22 localhost postfix/master[3776]: warning: process //usr/lib/postfix/pickup pid 18704 exit status 1
    Feb 11 12:31:22 localhost postfix/master[3776]: warning: //usr/lib/postfix/pickup: bad command startup -- throttling

## [Troubleshooting]

### [General tips]

To display more debugging information the logcheck\'s `-d` switch can be used. Example:

`root `[`#`]`su -s /bin/bash -c '/usr/sbin/logcheck -d' logcheck`

    D: [1281318818] Turning debug mode on
    D: [1281318818] Sourcing - /etc/logcheck/logcheck.conf
    D: [1281318818] Finished getopts c:dhH:l:L:m:opr:RsS:tTuvw
    D: [1281318818] Trying to get lockfile: /var/lock/logcheck/logcheck.lock
    D: [1281318818] Running lockfile-touch /var/lock/logcheck/logcheck.lock
    D: [1281318818] cleanrules: /etc/logcheck/cracking.d/kernel
    ...
    D: [1281318818] cleanrules: /etc/logcheck/violations.d/su
    D: [1281318818] cleanrules: /etc/logcheck/violations.d/sudo
    ...
    D: [1281318825] logoutput called with file: /var/log/messages
    D: [1281318825] Running /usr/sbin/logtail2 on /var/log/messages
    D: [1281318825] Sorting logs
    D: [1281318825] Setting the Intro
    D: [1281318825] Checking for security alerts
    D: [1281318825] greplogoutput: kernel
    ...
    D: [1281318825] greplogoutput: returning 1
    D: [1281318825] Checking for security events
    ...
    D: [1281318825] greplogoutput: su
    D: [1281318825] greplogoutput: Entries in checked
    D: [1281318825] cleanchecked - file: /tmp/logcheck.uIFLqU/violations-ignore/logcheck-su
    D: [1281318825] report: cat'ing - Security Events for su
    ...
    D: [1281318835] report: cat'ing - System Events
    D: [1281318835] Setting the footer text
    D: [1281318835] Sending report: 'localhost 2010-08-09 03:53 Security Events' to root
    D: [1281318835] cleanup: Killing lockfile-touch - 17979
    D: [1281318835] cleanup: Removing lockfile: /var/lock/logcheck/logcheck.lock
    D: [1281318835] cleanup: Removing - /tmp/logcheck.uIFLqU

\

Authorship information[]

This page is based on a document formerly found on [gentoo.org](https://www.gentoo.org/).\
The following people contributed to the original document: **phajdan.jr, nightmorph**\
\
*[Editors: please do **not** add yourself here. Contributions are recorded on each article\'s associated history page, this list is only present to preserve authorship information, as wiki history does not allow for any external attribution.]*