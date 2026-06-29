This page contains [[changes](https://wiki.gentoo.org/index.php?title=Owncloud&diff=921051)] which are not marked for translation.

\

**Resources**

[[]][Home](https://owncloud.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/OwnCloud "wikipedia:OwnCloud")

ownCloud is a free, open source, Dropbox-like file synchronization and cloud service. Since it can be setup and hosted on private servers it has no set limit on storage capacity or the number of connected users.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Features]](#Features)
    -   [[1.2] [Requirements]](#Requirements)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Emerge]](#Emerge)
        -   [[2.2.1] [Optional: Installing ownCloud server in the vhost directory via webapp-config]](#Optional:_Installing_ownCloud_server_in_the_vhost_directory_via_webapp-config)
    -   [[2.3] [Updates]](#Updates)
        -   [[2.3.1] [Optional: Updating ownCloud server in the vhost directory via webapp-config]](#Optional:_Updating_ownCloud_server_in_the_vhost_directory_via_webapp-config)
-   [[3] [Configuration]](#Configuration)
    -   [[3.1] [Performance tweaks]](#Performance_tweaks)
        -   [[3.1.1] [Enable APCu]](#Enable_APCu)
    -   [[3.2] [Misc tweaks]](#Misc_tweaks)
        -   [[3.2.1] [Disable integrity check]](#Disable_integrity_check)
-   [[4] [Usage]](#Usage)
    -   [[4.1] [ownCloud client]](#ownCloud_client)
-   [[5] [Removal]](#Removal)
    -   [[5.1] [Optional: Removing ownCloud server from the vhost directory via webapp-config]](#Optional:_Removing_ownCloud_server_from_the_vhost_directory_via_webapp-config)
    -   [[5.2] [gnome-keyring support]](#gnome-keyring_support)
-   [[6] [See also]](#See_also)
-   [[7] [References]](#References)

## [Introduction]

### [Features]

-   File storage in conventional directory structures or via WebDAV;
-   Encryption of user files;
-   Synchronization of ownCloud Client running Windows (Windows XP, Vista, 7 and 8), Mac OS X (10.6 or better), or Linux;
-   Calendar (also as CalDAV);
-   Task scheduler;
-   Address book (also as CardDAV);
-   Music streaming (through Ampache);
-   User and group administration (via OpenID or Lightweight Directory Access Protocol);
-   Sharing of content across groups or public URLs;
-   Online text editor with syntax highlighting and code folding;
-   Bookmarking;
-   URL shortening Suite;
-   Photo gallery;
-   Video viewer;
-   Portable Document Format viewer (using PDF.js);
-   Viewer for OpenDocument Files (.odt, .odp, .ods);
-   Firefox Sync/Mozilla Sync hosting --- Mozilla Firefox users can store all history, form data, bookmarks etc. in an ownCloud server;
-   External storage such as Dropbox, GoogleDrive, or Amazon S3 can be mounted to an ownCloud installation;
-   Customizable with one-click application install;
-   Logging Module: supports logging of file-related actions, logs, who accessed what, when and from where. Only available ownCloud Business, Enterprise and Education Editions.

### [Requirements]

The following will be needed in order for ownCloud to function properly:

-   A web server - ([Apache](https://wiki.gentoo.org/wiki/Apache "Apache"), [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd"), [Nginx](https://wiki.gentoo.org/wiki/Nginx "Nginx"), or likewise).
-   webapp-config - ([[[app-admin/webapp-config]](https://packages.gentoo.org/packages/app-admin/webapp-config)[]]) to easily install ownCloud Server to an vhost directory.
-   PHP 5.4.9 or greater - for owncloud-5.0.13-r1 and up.

## [Installation]

### [USE flags]

If `vhosts` USE will be enabled, so do before the install. The following is a list of possible USE flags.

Cannot load package information. Is the atom *www-apps/owncloud* correct?

### [Emerge]

Install ownCloud:

`root `[`#`]`emerge --ask www-apps/owncloud`

#### [Optional: Installing ownCloud server in the vhost directory via webapp-config]

### [Updates]

#### [Optional: Updating ownCloud server in the vhost directory via webapp-config]

This command will update the installed ownCloud server which is located in the directory [cloud] to the version 5.0.14

`root `[`#`]`webapp-config -h myDomain.com -d cloud -U owncloud 5.0.14`

Requires the [webapp-config] command (from [[[app-admin/webapp-config]](https://packages.gentoo.org/packages/app-admin/webapp-config)[]]):

If the `vhosts` USE flag is enabled, this command will install the ownCloud server version 5.0.13-r1 for the domain `myDomain.com` to the directory [cloud] which will (normally) be located in [/var/www/myDomain.com/htdocs/]

`root `[`#`]`webapp-config -h myDomain.com -d cloud -I owncloud 5.0.13-r1`

Make sure that this directory is added as a vhosts directory.

## [Configuration]

### [Performance tweaks]

Activate ownCloud Cronjobs ([for more information](https://doc.owncloud.com/server/admin_manual/configuration/server/background_jobs_configuration.html)):

`root `[`#`]`crontab -u apache -e`

     */15  *  *  *  * php -f /var/www/mydomain.com/htdocs/cloud/cron.php

#### [Enable APCu]

`root `[`#`]`PHP_TARGETS="php5-4" emerge -av dev-php/pecl-apcu`

Then restart the php-fpm service:

`root `[`#`]`/etc/init.d/php-fpm restart`

To verify if apc is working, copy [apc.php] in the [www] folder

`root `[`#`]`cp /usr/share/php/apc/apc.php /var/www/`

Open it with a preferred web browser.

### [Misc tweaks]

#### [Disable integrity check]

[Currently](https://github.com/owncloud/core/issues/24218), the integrity checker complains when there is a .webapp file in the root of the OwnCloud installation directory. This file is generated, and required, by the webapp-config tool used to install all web apps on Gentoo. One possible temporary solution to this is to disable integrity check. This can be accomplished by adding the following to [config.php]:

[FILE] **`config/config.php`**

    'integrity.check.disabled' => true

## [Usage]

### [ownCloud client]

Install the client by emerging the following package:

`root `[`#`]`emerge --ask net-misc/owncloud-client`

## [Removal]

### [Optional: Removing ownCloud server from the vhost directory via webapp-config]

This command will remove the installed ownCloud server version 5.0.14 which is located in the directory [cloud].

`root `[`#`]`webapp-config -h myDomain.com -d cloud -C owncloud 5.0.14`

### [gnome-keyring support]

You may have to install libgnome-keyring to enable owncloud-client support for gnome-keyring ^[\[1\]](#cite_note-1)^:

`root `[`#`]`emerge --ask gnome-base/libgnome-keyring`

Otherwise it may try to use kwallet.

## [See also]

-   [Dropbox](https://wiki.gentoo.org/wiki/Dropbox "Dropbox") --- a closed source file synchronization and cloud service utility built from open and closed source software.
-   [SparkleShare](https://wiki.gentoo.org/wiki/SparkleShare "SparkleShare") --- a cross platform, free, open source, Dropbox-like, git-based collaboration and file sharing tool.
-   [Webapp-config](https://wiki.gentoo.org/wiki/Webapp-config "Webapp-config") --- Gentoo\'s installer for web-based applications.

## [References]

1.  [[[↑](#cite_ref-1)] [[https://theterminallife.com/owncloud-client-gnome-keyring-issues/](https://theterminallife.com/owncloud-client-gnome-keyring-issues/)]]