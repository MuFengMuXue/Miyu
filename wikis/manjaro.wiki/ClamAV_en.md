[Translate this page](//wiki.manjaro.org/index.php?title=Special:Translate&group=page-ClamAV&language=en&action=page&filter= "Special:Translate")

Other languages:

[English](//wiki.manjaro.org/index.php?title=ClamAV "ClamAV (100% translated)") • ‎[Türkçe](//wiki.manjaro.org/index.php?title=ClamAV/tr "ClamAV (8% translated)") • ‎[français](//wiki.manjaro.org/index.php?title=ClamAV/fr "ClamAV (12% translated)") • ‎[русский](//wiki.manjaro.org/index.php?title=ClamAV/ru "ClamAV (100% translated)")

## Contents

-   [[1] [About]](#About)
-   [[2] [Installing ClamAV]](#Installing_ClamAV)
-   [[3] [Setup ClamAV]](#Setup_ClamAV)
-   [[4] [ClamTK - graphical interface of ClamAV]](#ClamTK_-_graphical_interface_of_ClamAV)
-   [[5] [See Also]](#See_Also)

# [About]

[![Clam.png](/images/e/ed/Clam.png)](//wiki.manjaro.org/index.php?title=File:Clam.png)

Clam AntiVirus (ClamAV) is a free, cross-platform antivirus software tool-kit able to detect many types of malicious software, including viruses. One of its main uses is on mail servers as a server-side email virus scanner. The application was developed for Unix and has third party versions available for AIX, BSD, HP-UX, Linux, OS X, OpenVMS, OSF (Tru64) and Solaris. As of version 0.97.5, ClamAV builds and runs on Microsoft Windows. Both ClamAV and its updates are made available free of charge.

Sourcefire, now acquired by Cisco, a maker of intrusion detection products and the owner of Snort, announced on 17 August 2007 that it had acquired the trademarks and copyrights to ClamAV from five key developers.

ClamAV includes a number of utilities: a command-line scanner, automatic database updater and a scalable multi-threaded daemon, running on an anti-virus engine from a shared library. The application also features a Milter interface for sendmail and on-demand scanning. It has support for Zip, RAR, Tar, Gzip, Bzip2, OLE2, Cabinet, CHM, BinHex, SIS formats, most mail file formats, ELF executables and Portable Executable (PE) files compressed with UPX, FSG, Petite, NsPack, wwpack32, MEW, Upack and obfuscated with SUE, Y0da Cryptor. It also supports many document formats, including Microsoft Office, HTML, Rich Text Format (RTF) and Portable Document Format (PDF). The ClamAV virus database is updated several times each day and as of 30 October 2011 contained 1,063,024 virus signatures with the daily update Virus DB number at 13867.

ClamAV is currently tested daily in comparative tests against other antivirus products on Shadowserver. In 2011, Shadowserver tested over 25 million samples against ClamAV and numerous other antivirus products. Out of the 25 million samples tested, ClamAV scored 76.60% ranking 12 out of 19, a higher rating than some much more established competitors. ClamAV was included in comparative tests against other antivirus products. In the 2008 AV-Test it rated: on-demand: very poor, false positives: poor, on-access: poor, response time: very good, rootkits: very poor. In a Shadowserver six-month test between June and December 2011, ClamAV detected over 75.45% of all viruses tested, putting it in fifth place behind AhnLab, Avira, BitDefender and Avast. AhnLab, the top antivirus, detected 80.28% [\[1\]](http://en.wikipedia.org/wiki/Clam_AntiVirus)

# [Installing ClamAV]

ClamAV is available in official repository. You can install it by command:

    sudo pacman -S clamav

# [Setup ClamAV]

Edit the contents of the configuration files to suit your preferences:

-   */etc/clamav/clamd.conf*
-   */etc/clamav/freshclam.conf*

First update database:

    sudo freshclam

You may get a notification that clamd was not notified. This is normal because we haven\'t started the service yet.

Start and enable service:

    sudo systemctl enable --now clamav-daemon

    sudo systemctl enable --now clamav-freshclam

Check status daemons:

    sudo systemctl status clamav-daemon && sudo systemctl status clamav-freshclam

Check database version:

    freshclam -V

# [ClamTK - graphical interface of ClamAV]

ClamTK is available in the repos, you can install it with pacman:

    sudo pacman -S clamtk

# [See Also]

[ClamAV Homepage](http://www.clamav.net/lang/en/)

[ClamTK Homepage](https://github.com/dave-theunsub/clamtk/)