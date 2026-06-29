[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Jira&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://confluence.atlassian.com/adminjiraserver/installing-jira-applications-on-linux-938846841.html)

[[]][Wikipedia](https://en.wikipedia.org/wiki/https://en.wikipedia.org/wiki/Jira_(software) "wikipedia:https://en.wikipedia.org/wiki/Jira (software)")

Atlassian Jira is a ticket based tracking application. This document links to the relevant information at the software suppliers webpage and explains the integration into OpenRC.

## Contents

-   [[1] [Dependencies]](#Dependencies)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [Files]](#Files)
-   [[3] [OpenRC]](#OpenRC)

## [Dependencies]

[Apache2](https://wiki.gentoo.org/wiki/Apache2 "Apache2")

a supported database (see [https://confluence.atlassian.com/adminjiraserver/supported-platforms-938846830.html](https://confluence.atlassian.com/adminjiraserver/supported-platforms-938846830.html))

Hint: [MariaDB](https://wiki.gentoo.org/wiki/MariaDB "MariaDB") works fine, though it is not officially supported. Use mysql-connector-java-5.1.47.jar and mysql-connector-java-5.1.47-bin.jar for the connectors.

## [Installation]

** Warning**\
This software may cause unwanted damage to the system as it is not contained in an ebuild

Download the official tarball from atlassian and configure accordingly. [https://confluence.atlassian.com/adminjiraserver/installing-jira-applications-on-linux-938846841.html](https://confluence.atlassian.com/adminjiraserver/installing-jira-applications-on-linux-938846841.html)

### [Files]

-   [/opt/atlassian/jira] - Application
-   [/var/atlassian/application-data/jira/] - Configuration

## [OpenRC]

The automatically installed script will fail to start at boot, at it does not wait for the database or apache to start. Therefore change it accordingly:

Replace the content of the file to match the following

[FILE] **`/etc/init.d/jira`Modify startup script**

    #!/sbin/openrc-run
    # According to https://wiki.gentoo.org/index.php?title=Jira

    depend()

    start()

    stop()