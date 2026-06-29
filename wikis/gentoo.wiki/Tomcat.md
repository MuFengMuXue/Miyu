**Resources**

[[]][Home](https://tomcat.apache.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Apache_Tomcat "wikipedia:Apache Tomcat")

[[]][Package information](https://packages.gentoo.org/packages/www-servers/tomcat)

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Java/Tomcat_5_Guide "Project:Java/Tomcat 5 Guide")][Tomcat 5](https://wiki.gentoo.org/wiki/Project:Java/Tomcat_5_Guide "Project:Java/Tomcat 5 Guide")

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Java/Tomcat_6_Guide "Project:Java/Tomcat 6 Guide")][Tomcat 6](https://wiki.gentoo.org/wiki/Project:Java/Tomcat_6_Guide "Project:Java/Tomcat 6 Guide")

This article is about installing Apache Tomcat version 6.0.35-r1 and newer and 7.0.29-r1 and newer. Official Gentoo Project documentation for Tomcat can be found in the resource links to the right. There are significant changes in how Tomcat is configured so be sure to use the correct guide for the job.

## Contents

-   [[1] [Installation]](#Installation)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Service for systemd]](#Service_for_systemd)
    -   [[2.2] [Migrating old Tomcat instances]](#Migrating_old_Tomcat_instances)
    -   [[2.3] [Integrating Tomcat with Netbeans]](#Integrating_Tomcat_with_Netbeans)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Need dependent jars in classpath]](#Need_dependent_jars_in_classpath)
    -   [[3.2] [Tomcat fails to start after update]](#Tomcat_fails_to_start_after_update)

## [Installation]

To install Tomcat, `emerge` [[[www-servers/tomcat]](https://packages.gentoo.org/packages/www-servers/tomcat)[]]. By default, only manager and host-manager applications are installed. To install Tomcat documentation and example applications, enable the `extra-webapps` USE flag. The ebuild installs only what is known as Catalina home. Creation of Catalina base is described in next section.

## [Configuration]

Since version 6.0.35-r1 and 7-0-29-r1, Tomcat supports running of multiple instances. This largely affects the way Tomcat is configured. The preferred way to create and configure Tomcat instances is by using Tomcat instance manager located at [/usr/share/tomcat-7/gentoo/tomcat-instance-manager.bash] for Tomcat 7 and at [/usr/share/tomcat-6/gentoo/tomcat-instance-manager.bash] for Tomcat 6. Running the instance manager without any parameter displays following help text:

`user `[`$`]`/usr/share/tomcat-7/gentoo/tomcat-instance-manager.bash`

    No action specified!
    Usage: /usr/share/tomcat-7/gentoo/tomcat-instance-manager.bash <--create|--remove|--help> [--suffix s][--user u][--group g]

      Options:
        --help:
          show this text.
        --create:
          create a new instance
        --remove:
          remove an existing instance.
        --suffix SUFFIX:
          a suffix for this instance. the suffix may not collide with an already
          existing instance, defaults to empty.
        --user USER:
          the user for which to configure this instance for. The user needs to
          exist already. defaults to tomcat.
        --group GROUP:
          the group for which to configure this instance for. The group needs to
          exist already. defaults to tomcat.

      Examples:
        /usr/share/tomcat-7/gentoo/tomcat-instance-manager.bash --create --suffix testing --user tacmot --group tacmot
        /usr/share/tomcat-7/gentoo/tomcat-instance-manager.bash --remove --suffix testing

** Note**\
When using \"SLOT\" or \"suffix\" in the following text, use the SLOT number appropriate to the version of Tomcat in reference and the matching suffix for creating the Tomcat instance. If a suffix was not used while creating Tomcat instance then omit `--suffix` from the path.

Follow the information in the help to create new Tomcat instances. Tomcat instances use the following layout:

-   [/etc/conf.d/tomcat-SLOT-suffix]: configuration file for running Tomcat instance services
-   [/etc/init.d/tomcat-SLOT-suffix]: controlling script for the Tomcat instance
-   [/etc/tomcat-SLOT-suffix/]: directory containing standard Tomcat configuration files
-   [/var/lib/tomcat-SLOT-suffix/]: Catalina base directory
-   [/var/log/tomcat-SLOT-suffix/]: directory for instance log files

Start a Tomcat instance using following command:

`root `[`#`]`/etc/init.d/tomcat-SLOT-suffix start`

To start a Tomcat instance on boot, run following command:

`root `[`#`]`rc-update add tomcat-SLOT-suffix default`

** Note**\
When configuring multiple instances, be sure to adjust instance ports so that no instance uses the same port(s) as another instance.

### [Service for systemd]

To start tomcat in a systemd environment, create a service similar to:

[FILE] **`/lib/systemd/system/tomcat-SLOT-suffix.service`**

    [Unit]
    Description=Apache Tomcat Web Application Container
    After=syslog.target network.target

    [Service]

    WorkingDirectory=/var/tmp/tomcat-SLOT-suffix/
    Environment=JAVA_HOME=/opt/openjdk-bin-17/
    Environment=CATALINA_PID=/var/run/tomcat/tomcat-SLOT-suffix.pid
    Environment=CATALINA_HOME=/usr/share/tomcat-10/
    Environment=CATALINA_BASE=/var/lib/tomcat-SLOT-suffix/
    Environment="JAVA_OPTS=-Xdebug"

    ExecStart=/usr/share/tomcat-10/bin/catalina.sh run
    ExecStop=/bin/kill -15

    User=tomcat
    Group=tomcat

    [Install]
    WantedBy=multi-user.target

### [Migrating old Tomcat instances]

To migrate Tomcat instance from Tomcat installation that supported only single instance, follow these steps:

-   Stop old version of Tomcat
-   Upgrade Tomcat to new version
-   Create new Tomcat instance, for example:

`user `[`$`]`/usr/share/tomcat-7/gentoo/tomcat-instance-manager.bash --create --suffix main`

-   Configure Tomcat files of the new instance ([/etc/conf.d/tomcat-7-main] and [/etc/tomcat-7-main/\*]) and copy your applications from the old instance ([/var/lib/tomcat-7/webapps/\*]) to the new one ([/var/lib/tomcat-7-main/webapps/])
-   Make new Tomcat instance to start after boot if required:

`root `[`#`]`rc-update add tomcat-7-main default`

-   Start the new instance:

`root `[`#`]`/etc/init.d/tomcat-7-main start`

### [Integrating Tomcat with Netbeans]

Integration of Tomcat with Netbeans is easy. Run the instance manager with `--user` command line option and specify user name of the user being creating for the Catalina base. The newly created Catalina base files are then owned by the specified user and are fully accessible by Netbeans when being run under that user. Now configure Tomcat in Netbeans Servers configuration dialogue. When using Tomcat 7, use [/usr/share/tomcat-7] as Catalina home and [var/lib/tomcat-7-suffix] as Catalina base. When using Tomcat 6, use [/usr/share/tomcat-6] as Catalina home and [var/lib/tomcat-6-suffix/] as Catalina base. In both cases replace suffix with the appropriate suffix used when creating the instance.

## [Troubleshooting]

### [Need dependent jars in classpath]

java-config in the init script should include `-d` so that dependent JARs get added automagically to the classpath. See [[[bug #448990]](https://bugs.gentoo.org/show_bug.cgi?id=448990#c1)[]] for more information.

Edit catalina.sh

`root `[`#`]`nano /usr/share/tomcat-SLOT/bin/catalina.sh`

Add `-d` to CLASSPATH variable.

`` CLASSPATH=`java-config -d --classpath tomcat-8` ``

### [Tomcat fails to start after update]

You may need to update your init script and catalina properties:

`root `[`#`]`cp /usr/share/tomcat-SLOT/gentoo/tomcat.init /etc/init.d/tomcat-SLOT-suffix`

`root `[`#`]`cp /usr/share/tomcat-SLOT/conf/catalina.properties /etc/tomcat-SLOT-suffix/catalina.properties`

See [[[bug #559576]](https://bugs.gentoo.org/show_bug.cgi?id=559576)[]].