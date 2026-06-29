This page contains [[changes](//wiki.manjaro.org/index.php?title=ClamAV&oldid=24595&diff=55162)] which are not marked for translation.

Other languages:

[English] • ‎[Türkçe](//wiki.manjaro.org/index.php?title=ClamAV/tr "ClamAV (8% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=ClamAV/fr "ClamAV (12% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=ClamAV/ru "ClamAV (100% translated)")

## Contents

-   [[1] [About]](#About)
-   [[2] [Install ClamAV]](#Install_ClamAV)
-   [[3] [Set up ClamAV via CLI]](#Set_up_ClamAV_via_CLI)
    -   [[3.1] [Edit Config]](#Edit_Config)
    -   [[3.2] [Update Database]](#Update_Database)
    -   [[3.3] [Services]](#Services)
        -   [[3.3.1] [clamav / freshclam]](#clamav_.2F_freshclam)
        -   [[3.3.2] [cron]](#cron)
    -   [[3.4] [Schedule scans through \'cron\']](#Schedule_scans_through_.27cron.27)
        -   [[3.4.1] [Edit \'crontab\']](#Edit_.27crontab.27)
        -   [[3.4.2] [Create directories \'logs\' and \'quarantine\']](#Create_directories_.27logs.27_and_.27quarantine.27)
        -   [[3.4.3] [Set ExcludePath for \'quarantine\' folder]](#Set_ExcludePath_for_.27quarantine.27_folder)
    -   [[3.5] [Schedule updates through \'cron\']](#Schedule_updates_through_.27cron.27)
-   [[4] [Set up ClamAV via GUI (ClamTK)]](#Set_up_ClamAV_via_GUI_.28ClamTK.29)

# [About]

[![Clam.png](/images/e/ed/Clam.png)](//wiki.manjaro.org/index.php?title=File:Clam.png)

[ClamAV](https://www.clamav.net/) is an open-source antivirus engine for detecting trojans, viruses, malware & other malicious threats. One of its main uses is on mail servers as a server-side email virus scanner. The application was developed for Unix and has third party versions available for AIX, BSD, HP-UX, Linux, macOS, OpenVMS, OSF (Tru64) and Solaris. As of version `0.97.5`, ClamAV builds and runs on Microsoft Windows. Both ClamAV and its updates are made available free of charge.

Sourcefire, now acquired by Cisco, a maker of intrusion detection products and the owner of Snort, announced on 17 August 2007 that it had acquired the trademarks and copyrights to ClamAV from five key developers.

ClamAV includes a number of utilities: a command-line scanner, automatic database updater and a scalable multi-threaded daemon, running on an anti-virus engine from a shared library.

The application also features a Milter interface for sendmail and on-demand scanning. It has support for Zip, RAR, Tar, Gzip, Bzip2, OLE2, Cabinet, CHM, BinHex, SIS formats, most mail file formats, ELF executables and Portable Executable (PE) files compressed with UPX, FSG, Petite, NsPack, wwpack32, MEW, Upack and obfuscated with SUE, Y0da Cryptor. It also supports many document formats, including Microsoft Office, HTML, Rich Text Format (RTF) and Portable Document Format (PDF).

The ClamAV virus database is updated several times each day and as of 30 October 2011 contained 1,063,024 virus signatures with the daily update Virus DB number at 13867.

ClamAV is currently tested daily in comparative tests against other antivirus products on Shadowserver. In 2011, Shadowserver tested over 25 million samples against ClamAV and numerous other antivirus products. Out of the 25 million samples tested, ClamAV scored 76.60% ranking 12 out of 19, a higher rating than some much more established competitors.

ClamAV was included in comparative tests against other antivirus products. In the 2008 AV-Test it rated: on-demand: very poor, false positives: poor, on-access: poor, response time: very good, rootkits: very poor.

In a Shadowserver six-month test between June and December 2011, ClamAV detected over 75.45% of all viruses tested, putting it in fifth place behind AhnLab, Avira, BitDefender and Avast. AhnLab, the top antivirus, detected 80.28% [\[1\]](http://en.wikipedia.org/wiki/Clam_AntiVirus)

# [Install ClamAV]

ClamAV is available in the `extra` repository[\[2\]](https://archlinux.org/packages/extra/x86_64/clamav/). You can install it by command:

    sudo pacman -S clamav

# [Set up ClamAV via CLI]

## [Edit Config]

Edit the contents of the configuration files to suit your preferences:

-   `/etc/clamav/clamd.conf`
-   `/etc/clamav/freshclam.conf`

## [Update Database]

First update database:

    sudo freshclam

You may get a notification that `clamd` was not notified. This is normal because we haven\'t started the service yet.

Check database version:

    freshclam --version

## [Services]

### [][clamav / freshclam]

For automatic updates first create and set the required freshclam.log file:

    touch /var/log/clamav/freshclam.log
    chmod 600 /var/log/clamav/freshclam.log
    chown clamav /var/log/clamav/freshclam.log

Start and enable service:

    sudo systemctl enable --now clamav-daemon
    sudo systemctl enable --now clamav-freshclam

Check status daemons:

    sudo systemctl status clamav-daemon && sudo systemctl status clamav-freshclam

### [cron]

Make sure a cron daemon (for example \'cronie\') is installed, enabled and running, as cronjobs are used in this guide. See also: [Cron](https://wiki.archlinux.org/title/Cron)

Example with \'cronie\' (install, enable+start and check status):

    sudo pacman -S cronie
    sudo systemctl enable --now cronie.service
    sudo systemctl status cronie.service

Alternative: Use systemd Timers. See: [systemd/Timers](https://wiki.archlinux.org/title/Systemd/Timers)

## [][Schedule scans through \'cron\']

### [][Edit \'crontab\']

Run `crontab -e` to edit your `crontab` and add the following line, editing it to your needs:

    53 8 * * 5 /usr/bin/clamdscan --fdpass --multiscan --move="$HOME/.clam/quarantine" --log="$HOME/.clam/logs/$(date +\%Y\%m\%d)-weekly.log" "$HOME" 2>/dev/null 1>&2

This scans the entire `$HOME` directory every week on Saturday at 08:53. See `man 5 crontab` for more info on the formatting of this file and `man clamdscan` for an explanation of the options used.

### [][Create directories \'logs\' and \'quarantine\']

If not already present, the directories for `'logs'` and `'quarantine'` are to be created in the `$HOME` directory:

    mkdir -p "$/.clam/quarantine" && mkdir -p "$/.clam/logs"

Otherwise, for example, creating the logfile may fail due to missing authorization.

### [][Set ExcludePath for \'quarantine\' folder]

To exclude scanning the `'quarantine'` folder in the `$HOME` directory, add an `'ExcludePath'` to `'/etc/clamav/clamd.conf'` with your prefered editor, for example using \'vim\':

    sudo vim /etc/clamav/clamd.conf

Search for `ExcludePath` and add: `ExcludePath ^/home/.*/\.clam/quarantine`

Alternative: you can provide a separate config-file. For more Information see `man clamdscan` and `man clamd.conf`.

## [][Schedule updates through \'cron\']

A service should already be running for automatic updates, so that configuring updates via a cronjob are no longer necessary. To check the service run:

    systemctl status clamav-freshclam.service

For config see `man freshclam.conf`.

If the service is not available / can not be started and enabled on your system: Then run `sudo crontab -e -u clamav` to set up automatic updates. (These should be run as the `clamav` user.) Add the following line to update these at 13 past every hour:

    13 * * * * /usr/bin/freshclam --quiet

# [][Set up ClamAV via GUI (ClamTK)]

[ClamTK](https://archlinux.org/packages/community/any/clamtk/) is a graphical user interface to setup scheduled scans and updates as well as one-off scans. It\'s available in the `community` repository[\[3\]](https://archlinux.org/packages/community/any/clamtk/), you can install it with `pacman`:

    sudo pacman -S clamtk