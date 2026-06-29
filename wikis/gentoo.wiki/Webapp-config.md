This page contains [[changes](https://wiki.gentoo.org/index.php?title=Webapp-config&oldid=799040&diff=1417887)] which are not marked for translation.

Other languages:

-   [English]
-   [français](https://wiki.gentoo.org/wiki/Webapp-config/fr "Webapp-config (100% translated)")
-   [magyar](https://wiki.gentoo.org/wiki/Webapp-config/hu "Webapp-config (100% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/Webapp-config/zh-cn "Webapp-config (47% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/Webapp-config/ja "webapp-config (93% translated)")

**Resources**

[[![Gentoo peach graphic](/images/thumb/a/ad/Gentoo-logo-peach.svg/25px-Gentoo-logo-peach.svg.png)](https://wiki.gentoo.org/wiki/Project:Webapps "Project:Webapps")][Project](https://wiki.gentoo.org/wiki/Project:Webapps "Project:Webapps")

[[]][Package information](https://packages.gentoo.org/packages/app-admin/webapp-config)

[[]][GitWeb](https://gitweb.gentoo.org/proj/webapp-config.git)

[[]][GitHub](https://github.com/gentoo/webapp-config)

[webapp-config] is Gentoo\'s installer for web-based applications. It is used for automatic setup of web applications in [virtual hosting environments](https://en.wikipedia.org/wiki/Virtual_hosting "wikipedia:Virtual hosting") (associated packages typically include a [`vhosts`](https://packages.gentoo.org/useflags/vhosts) USE flag). Originally written as a bash script, [webapp-config] is now Python-based and available in the Gentoo ebuild repository.

## Contents

-   [[1] [Concepts]](#Concepts)
    -   [[1.1] [Two-stage install]](#Two-stage_install)
    -   [[1.2] [Multiple installations of the same package]](#Multiple_installations_of_the_same_package)
    -   [[1.3] [File ownership and permissions]](#File_ownership_and_permissions)
    -   [[1.4] [Protected configuration files]](#Protected_configuration_files)
    -   [[1.5] [File copying options]](#File_copying_options)
        -   [[1.5.1] [Maintaining hard-links via a symlink]](#Maintaining_hard-links_via_a_symlink)
        -   [[1.5.2] [Symlinking across filesystems]](#Symlinking_across_filesystems)
        -   [[1.5.3] [Duplicating files by copying]](#Duplicating_files_by_copying)
    -   [[1.6] [Virtual file voodoo]](#Virtual_file_voodoo)
    -   [[1.7] [\$]](#.24.7BROOT.7D)
-   [[2] [Features]](#Features)
-   [[3] [Installation]](#Installation)
    -   [[3.1] [USE flags]](#USE_flags)
    -   [[3.2] [Emerge]](#Emerge)
-   [[4] [Configuration]](#Configuration)
    -   [[4.1] [Web server setup]](#Web_server_setup)
-   [[5] [Usage]](#Usage)
    -   [[5.1] [Listing and installing webapps]](#Listing_and_installing_webapps)
    -   [[5.2] [Upgrading an installed webapp]](#Upgrading_an_installed_webapp)
    -   [[5.3] [Removing an installation]](#Removing_an_installation)
-   [[6] [See also]](#See_also)

## [Concepts]

[webapp-config] is aimed at providing the package management functionality that web server administrators need when running multiple domains names off of the same IP address ([virtual hosting](https://en.wikipedia.org/wiki/Virtual_hosting "wikipedia:Virtual hosting")).

### [Two-stage install]

Package managers such as RPM and Portage are designed to install one copy of a package, and to install it onto a fixed location. This conflicts with the needs of a virtual hosting environment, where administrators need to be able to install one package in multiple places so that it can be part of more than one website. With that being said, package managers are essential for maintaining an operating system over time - how is it possible to have the best of both worlds?

The answer is a two-stage install. The traditional package manager installs a master copy into [/usr/share/webapps/]. This master copy is not fit to run - but it is ready to be used by the [webapp-config] utility to install a single package multiple times in multiple places.

### [Multiple installations of the same package]

[webapp-config] allows the administrator to install multiple copies of the same package on the same system at the same time. The administrator decides which directories to install each copy into.

In the web application world, these multiple installations are called \"virtual copies\".

Different *versions* of the same package can be installed on the same system at the same time. This allows web administrators to gradually roll out a new version of a package across sites; they are not forced to upgrade every site at once.

[webapp-config] minimizes the number of duplicated files to conserve disk space usage. The majority of files are hard linked to the master copy; only configuration files, and any files that the package needs to write to are *copied* into the virtual copy.

### [File ownership and permissions]

Administrators who are used to installing web-based applications by hand will know that it can be a pain to get every file owned by the correct user, and with the correct permissions. Some files need to be owned by the user that the web server runs as. Others need to be owned by specific shell accounts, so that those users can login and edit the configuration files. If the Linux distribution offers a choice of web servers - each running under a different user - even the installers can struggle to get it right.

With [webapp-config], the administrator tells the installer which web server to use and which shell account needs to be able to edit the configuration files. [webapp-config] then installs the files with the correct ownership and permissions.

### [Protected configuration files]

[webapp-config] automatically ensures that configuration files are *never* overwritten during an upgrade - even if the files have not been edited since the original installation. Additionally, [webapp-config] will never overwrite any file that it did not install, or that has been changed since it was installed by [webapp-config]. [webapp-config] uses MD5 checksums to determine whether a file has been changed. In the case of symbolic links, [webapp-config] will not replace a symlink that points to a different file.

When an upgrade does attempt to overwrite a protected file, [webapp-config] creates a [.\_cfg] file with the new file inside. [dispatch-conf] can be used to complete the changed configuration file install, just as any other configuration file updates.

### [File copying options]

A virtual copy is built mostly by creating hard links to files under [/usr/share/webapps]. If a hard link cannot be created, the file is copied from [/usr/share/webapps] instead.

Hard links can only be created to files on the same file system. If [/usr/share/webapps] and [/var/www] on kept on different file systems, [webapp-config] cannot use hard links, and will be forced to copy the files instead.

There are three ways to get around the hard link problem.

#### [Maintaining hard-links via a symlink]

The easiest way is to maintain hard-links to make [/usr/share/webapps] a symlink to a directory under [/var/www]. For most administrators, this will ensure that everything is on the same file system as long as one file system is used for the [/var/www] directory.

For example, presuming the [/usr/share/webapps] directory exists, and there is already a web application installed therein:

`root `[`#`]`mv /usr/share/webapps /var/www # Moves the default webapp directory `

`root `[`#`]`ln --symbolic /var/www/webapps /usr/share/webapps # Creates the symbolic link `

However, if for some reason hosted websites under [/var/www] or another directory must be kept on separate file systems, then [webapp-config] will not be able to hard-link files.

#### [Symlinking across filesystems]

As an alternative the `--soft` command-line option can be used. This tells [webapp-config] to create symbolic links *instead* of hard links. Symbolic links work across file systems.

The problem with using symbolic links is that some packages do not work when the virtual copy is made from symbolic links. Many users, and system administrators alike, have also complained that they find directories full of symbolic links confusing. For these reasons, symbolic links are not used by default in [webapp-config] any more.

#### [Duplicating files by copying]

The `--copy` command-line option can also be chosen. This particular switch tells [webapp-config] to directly *copy* the files from [/usr/share/webapps/] instead of hard links. Copying directly works across file systems with the drawback of consuming more space. This may be desired instead of relying on symbolic links in order to separate the virtualhost files, which admins can then modify, and files in [/usr/share/webapps/].

### [Virtual file voodoo]

By default, the master copy contains the metadata that decides which files get linked into a virtual copy and which files do not. Files are either owned by the web server (server-owned), are configuration files (config-owned), or are linked in (virtual). Directories can be server-owned or config-owned, but most of the time they need to be just plain directories (default-owned) created inside the installation directory (set with the `-d` option). [webapp-config] provides a number of switches which allows for overriding the master copy\'s metadata - in the case the overriding is ever needed.

The `--default-dirs` and `--virtual-files` switches allow the administrator to decide what [webapp-config] will do if (respectively) a directory or a file is marked as being default or virtual. [webapp-config] can be instructed to make the directory or file any of the other choices - server-owned or config-owned - instead.

### []}[\$]

[webapp-config] is intended to fully support `$`. For administrators unsure what that means see the emerge man page ([man emerge]).

## [Features]

** Note**\
See packages.gentoo.org for an [up-to-date listing of packages using the vhosts USE flag](https://packages.gentoo.org/useflags/vhosts).

Using the `vhosts` USE flag [webapp-config] is capable of managing the following applications:

  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------
  Application                                                       Package                                                                                                                                                                                                                                                                                                                                                                                 Homepage                                                                                                                       Description
  [Bugzilla](https://wiki.gentoo.org/wiki/Bugzilla "Bugzilla")      [[[www-apps/bugzilla]](https://packages.gentoo.org/packages/www-apps/bugzilla)[]]               [https://www.bugzilla.org](https://www.bugzilla.org)                                           Bugzilla is the Bug-Tracking System from the Mozilla project.
  [cgit](https://wiki.gentoo.org/wiki/Cgit "Cgit")                  [[[www-apps/cgit]](https://packages.gentoo.org/packages/www-apps/cgit)[]]                           [https://git.zx2c4.com/cgit/about](https://git.zx2c4.com/cgit/about)                           A fast web-interface for git repositories.
  cvsweb                                                            [[[www-apps/cvsweb]](https://packages.gentoo.org/packages/www-apps/cvsweb)[]]                     [https://www.freebsd.org/projects/cvsweb.html](https://www.freebsd.org/projects/cvsweb.html)   WWW interface to a CVS tree
  dokuwiki                                                          [[[www-apps/dokuwiki]](https://packages.gentoo.org/packages/www-apps/dokuwiki)[]]               [https://www.splitbrain.org/projects/dokuwiki](https://www.splitbrain.org/projects/dokuwiki)   DokuWiki is a simple to use Wiki aimed at a small company\'s documentation needs.
  [Drupal](https://wiki.gentoo.org/wiki/Drupal "Drupal")            [[[www-apps/drupal]](https://packages.gentoo.org/packages/www-apps/drupal)[]]                     [https://drupal.org/](https://drupal.org/)                                                     PHP-based open-source platform and content management system.
  [MediaWiki](https://wiki.gentoo.org/wiki/MediaWiki "MediaWiki")   [[[www-apps/mediawiki]](https://packages.gentoo.org/packages/www-apps/mediawiki)[]]            [https://www.mediawiki.org](https://www.mediawiki.org)                                                        The MediaWiki wiki web application (as used on wikipedia.org).
  mirmon                                                            [[[www-apps/mirmon]](https://packages.gentoo.org/packages/www-apps/mirmon)[]]                     [http://people.cs.uu.nl/henkp/mirmon/](http://people.cs.uu.nl/henkp/mirmon/)                   Simple webapp to monitor the status of mirrors.
  [Moodle](https://wiki.gentoo.org/wiki/Moodle "Moodle")            [[[www-apps/moodle]](https://packages.gentoo.org/packages/www-apps/moodle)[]]                     [https://moodle.org](https://moodle.org)                                                       The Moodle Course Management System.
  mythweb                                                           [[[www-apps/mythweb]](https://packages.gentoo.org/packages/www-apps/mythweb)[]]                  [https://www.mythtv.org](https://www.mythtv.org)                                               PHP scripts intended to manage MythTV from a web browser.
  [Nextcloud](https://wiki.gentoo.org/wiki/Nextcloud "Nextcloud")   [[[www-apps/nextcloud]](https://packages.gentoo.org/packages/www-apps/nextcloud)[]]            [https://nextcloud.com/](https://nextcloud.com/)                                               Web-based personal cloud that runs on your own server.
  [phpBB](https://wiki.gentoo.org/wiki/PhpBB "PhpBB")               [[[www-apps/phpBB]](https://packages.gentoo.org/packages/www-apps/phpBB)[]]                        [https://www.phpbb.com/](https://www.phpbb.com/)                                               phpBB is an open-source bulletin board package.
  phpsysinfo                                                        [[[www-apps/phpsysinfo]](https://packages.gentoo.org/packages/www-apps/phpsysinfo)[]]         [https://github.com/phpsysinfo/phpsysinfo/](https://github.com/phpsysinfo/phpsysinfo/)         phpSysInfo is a nice package that will display your system stats via PHP.
  postfixadmin                                                      [[[www-apps/postfixadmin]](https://packages.gentoo.org/packages/www-apps/postfixadmin)[]]   [http://postfixadmin.sourceforge.net](http://postfixadmin.sourceforge.net)                     Web Based Management tool for Postfix style virtual domains and users.
  rutorrent                                                         [[[www-apps/rutorrent]](https://packages.gentoo.org/packages/www-apps/rutorrent)[]]            [https://github.com/Novik/ruTorrent](https://github.com/Novik/ruTorrent)                       ruTorrent is a front-end for the popular Bittorrent client rTorrent.
  tt-rss                                                            [[[www-apps/tt-rss]](https://packages.gentoo.org/packages/www-apps/tt-rss)[]]                     [https://tt-rss.org/](https://tt-rss.org/)                                                     Tiny Tiny RSS - A web-based news feed (RSS/Atom) aggregator using AJAX.
  wiliki                                                            [[[www-apps/wiliki]](https://packages.gentoo.org/packages/www-apps/wiliki)[]]                     [http://practical-scheme.net/wiliki/](http://practical-scheme.net/wiliki/)                     WiLiKi is a lightweight Wiki engine written in and running on Gauche Scheme.
  [WordPress](https://wiki.gentoo.org/wiki/WordPress "WordPress")   [[[www-apps/wordpress]](https://packages.gentoo.org/packages/www-apps/wordpress)[]]            [https://wordpress.org/](https://wordpress.org/)                                               Wordpress php and mysql based content management system (CMS).
  ----------------------------------------------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------------------------------------------------ -----------------------------------------------------------------------------------

## [Installation]

### [USE flags]

### [USE flags for] [app-admin/webapp-config](https://packages.gentoo.org/packages/app-admin/webapp-config) [[]] [Gentoo\'s installer for web-based applications]

  ------------------------------------------------------------- -----------------------------------------------------------
  [`+portage`](https://packages.gentoo.org/useflags/+portage)   Propagate python_targets dependencies to sys-apps/portage
  ------------------------------------------------------------- -----------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-07 08:35] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install [webapp-config]:

`root `[`#`]`emerge --ask app-admin/webapp-config`

## [Configuration]

### [Web server setup]

[webapp-config] needs to know which web server to host the installed applications with. Popular choices include:

-   [Apache](https://wiki.gentoo.org/wiki/Apache "Apache")
-   [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx")
-   [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd")

\

** Note**\
If a web server has not been set up previous to this step in the [webapp-config] process, do so *before* continuing to proceed through this article. Visit the links referenced above to install and configure the web server. Once the web server has been set up return to this article

Edit the following line in the [/etc/vhosts/webapp-config] file to set a web server. This example would be the correct modification to make if [apache] ([[[www-servers/apache]](https://packages.gentoo.org/packages/www-servers/apache)[]]) was the web server of choice:

[FILE] **`/etc/vhosts/webapp-config`Setting webapp-config\'s web server preference**

    vhost_server="apache"

## [Usage]

### [Listing and installing webapps]

First, determine which [webapp-config] compatible web application(s) and their associated version(s) are *available* for installation, but yet uninstalled:

`root `[`#`]`webapp-config --list-unused-installs`

To list the webapps that are installed, with their version and full install location:

`root `[`#`]`webapp-config --list-installs --verbose`

webapp-config does not list the host or directory arguments used to install the webapp, if any were used\...

To install a webapp, use the `-I`/`--install` option and provide two arguments, the application name (which will be short, such as `nextcloud`), and the version of the application to install:

`root `[`#`]`webapp-config --install <app> <version> --pretend # Dry run to see what will occur upon installation`

`root `[`#`]`webapp-config --install <app> <version>`

To install a webapp under a specific vhost or subdirectory, use the `--host <hostname>` and/or `--dir <directory>` options to override the defaults set in the [/etc/vhosts/webapp-config] file:

`root `[`#`]`webapp-config --install <app> <version> --host <host> --dir <dir>`

The webapp will be accessible at `http://<host>/<dir>/`.

To show information about an installed webapp:

`root `[`#`]`webapp-config --show-installed [--host <host>] [--dir <dir>]`

This will print the webapp name and installed version of the webapp at the given directory location.

### [Upgrading an installed webapp]

First, determine which versions are available but unused:

`root `[`#`]`webapp-config --list-unused-installs`

This will list applications in a format like `<app>-<new-version>`

Then determine what you are using:

`root `[`#`]`webapp-config --list-installs --verbose`

You might see listings like `/var/www/example.com/htdocs/dir`, figure out how this maps to the `--host` and `--dir` options, if at all. Run the upgrade with:

`root `[`#`]`webapp-config --upgrade <app> <new-version-number> [--host <host>] [--dir <dir>]`

### [Removing an installation]

To remove an installed webapp:

`root `[`#`]`webapp-config --clean <app> <version>`

If you\'ve removed a webapp by hand and need to update the database for webapp-config, first check using pretend:

`root `[`#`]`webapp-config --prune-database=pretend`

If this looks correct, follow up with:

`root `[`#`]`webapp-config --prune-database=clean`

`--prune-database=clean` will only remove the registry entries, it will never remove files it doesn\'t recognize.

## [See also]

[Project:Webapps](https://wiki.gentoo.org/wiki/Project:Webapps "Project:Webapps") --- The Gentoo web-app team maintains most web applications available via Portage.