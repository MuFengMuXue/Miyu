**Resources**

[[]][Home](http://git.zx2c4.com/cgit/about/)

[[]][GitWeb](http://git.zx2c4.com/cgit/)

[[]][cgitrc(5)](https://git.zx2c4.com/cgit/tree/cgitrc.5.txt)

[[]][[#cgit](ircs://irc.libera.chat/#cgit)] ([[webchat](https://web.libera.chat/#cgit)])

**cgit** is a hyperfast web frontend for git repositories written in C. Cgit makes it possible for potential contributors to track and view project source code using a web interface.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Environment variables]](#Environment_variables)
    -   [[2.2] [Files]](#Files)
    -   [[2.3] [Cron (optional)]](#Cron_.28optional.29)
-   [[3] [Troubleshooting]](#Troubleshooting)
    -   [[3.1] [Issue 1]](#Issue_1)
-   [[4] [See also]](#See_also)
-   [[5] [External resources]](#External_resources)

## [Installation]

### [USE flags]

### [USE flags for] [www-apps/cgit](https://packages.gentoo.org/packages/www-apps/cgit) [[]] [A fast web-interface for Git repositories]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+highlight`](https://packages.gentoo.org/useflags/+highlight)   Enable source code highlighting
  [`+lua`](https://packages.gentoo.org/useflags/+lua)               Enable support for Lua scripting
  [`doc`](https://packages.gentoo.org/useflags/doc)                 Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)           Add support for installing web-based applications into a virtual-hosting environment
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 02:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

[cgit] can be managed using [webapp-config] if the `vhosts` USE flag is enabled. Without `vhosts` USE flag set, cgit will be installed in the default path of the used web server.

### [Emerge]

`root `[`#`]`emerge --ask www-apps/cgit`

After installation some post-install instructions should be visible in the output from the install command. Please read these instructions carefully before proceeding to use [cgit].

### [Additional software]

[cgit] depends upon a web server. Choose one of the listed web servers available in gentoo portage:

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache")
-   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx")
-   [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd")

After the installation and configuration of a web server is finished, continue with the [cgit] configuration process.

## [Configuration]

### [Environment variables]

-   CGIT_CONFIG

### [Files]

-   [/etc/cgitrc] - The global configuration file. This is used to modifying settings for all users.
-   [/etc/cgitrepos] - (optional) additional cgit generated repository list file

### [][Cron (optional)]

This method will generate a file [/etc/cgitrepos] using a local directory path.

Adjust the `--scan-tree=` path in the below command, to match the directory path to the git repositories:

`root `[`#`]`/usr/share/webapps/cgit/*/hostroot/cgi-bin/cgit.cgi --scan-tree=/PATH/TO/REPOSITORY > /etc/cgitrepos`

Append a include statement `include=/etc/cgitrepos` at the end of the [/etc/cgitrc] configuration file.

[FILE] **`/etc/cgitrc`**

    ...
    include /etc/cgitrepos

Add a cron job to schedule repository list generation every 24 hours:

[FILE] **`/etc/cron.daily/cgitrepos`**

    #!/bin/sh
    /usr/share/webapps/cgit/*/hostroot/cgi-bin/cgit.cgi --scan-tree=/PATH/TO/REPOSITORY > /etc/cgitrepos

Make the script executable, by setting `+x` bit:

`root `[`#`]`chmod +x /etc/cron.daily/cgitrepos`

## [Troubleshooting]

### [Issue 1]

cgit has been build using the `vhost` USE flag, and configured as Apache vhost (virtual named host). Following files are not displayed in the browser:

-   cgit.css
-   cgit.png
-   favicon.ico

The file robots.txt is ignored too. The application has wrong `paths` settings.

Add `Alias`\'es for the missing files in the virtual host configuration file:

[FILE] **`/etc/apache2/vhosts.d/cgit.*_vhost.include`**

    ...
    Alias /cgit.css     /var/www/cgit/htdocs/cgit/cgit.css
    Alias /cgit.png     /var/www/cgit/htdocs/cgit/cgit.png
    Alias /favicon.ico  /var/www/cgit/htdocs/cgit/favicon.ico
    Alias /robots.txt   /var/www/cgit/htdocs/cgit/robots.txt
    ScriptAlias / "/var/www/cgit/cgi-bin/cgit.cgi/"
    ...

## [See also]

-   [Git](https://wiki.gentoo.org/wiki/Git "Git") --- widely used, open source, distributed [version control system](https://wiki.gentoo.org/wiki/Version_control_systems "Version control systems")
-   [Webapp-config](https://wiki.gentoo.org/wiki/Webapp-config "Webapp-config") --- Gentoo\'s installer for web-based applications.

## [External resources]

-   [The official cgit FAQ](https://git.zx2c4.com/cgit/about/faq)