** Note**\
This article refers to the Bugzilla web application. [Go here for the Gentoo Bugzilla guide](https://wiki.gentoo.org/wiki/Bugzilla/Guide "Bugzilla/Guide").

[] Some of the information in this article may have drifted out of sync with current practices. Please help out by [checking over the content](https://wiki.gentoo.org/index.php?title=Bugzilla&action=edit) ([how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide")).

**Resources**

[[]][Home](https://www.bugzilla.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Bugzilla "wikipedia:Bugzilla")

[[]][Guide](https://wiki.gentoo.org/wiki/Bugzilla/Guide "Bugzilla/Guide")

**Bugzilla** is a web application for tracking bugs.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Database]](#Database)
        -   [[1.3.1] [MySQL]](#MySQL)
        -   [[1.3.2] [PostgreSQL]](#PostgreSQL)
    -   [[1.4] [Checksetup]](#Checksetup)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Apache]](#Apache)
-   [[3] [Web end]](#Web_end)
-   [[4] [Upgrading]](#Upgrading)
-   [[5] [Troubleshooting]](#Troubleshooting)
-   [[6] [More documentation]](#More_documentation)
-   [[7] [References]](#References)

## [Installation]

### [USE flags]

### [USE flags for] [www-apps/bugzilla](https://packages.gentoo.org/packages/www-apps/bugzilla) [[]] [Bugzilla is the Bug-Tracking System from the Mozilla project]

  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`+sqlite`](https://packages.gentoo.org/useflags/+sqlite)     Add support for sqlite - embedded sql database
  [`apache2`](https://packages.gentoo.org/useflags/apache2)     Add Apache2 support
  [`doc`](https://packages.gentoo.org/useflags/doc)             Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`mysql`](https://packages.gentoo.org/useflags/mysql)         Add mySQL Database support
  [`postgres`](https://packages.gentoo.org/useflags/postgres)   Add support for the postgresql database
  [`selinux`](https://packages.gentoo.org/useflags/selinux)     !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`test`](https://packages.gentoo.org/useflags/test)           Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)       Add support for installing web-based applications into a virtual-hosting environment
  ------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-25 01:30] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

** Note**\
Users might prefer to emerge [[[app-admin/webapp-config]](https://packages.gentoo.org/packages/app-admin/webapp-config)[]] and configure it before proceeding to emerge [[[www-apps/bugzilla]](https://packages.gentoo.org/packages/www-apps/bugzilla)[]].

Install [[[www-apps/bugzilla]](https://packages.gentoo.org/packages/www-apps/bugzilla)[]]:

`root `[`#`]`emerge --ask www-apps/bugzilla`

### [Database]

#### [MySQL]

Install [[[dev-db/mysql]](https://packages.gentoo.org/packages/dev-db/mysql)[]] but prefer a 5.x version ^[\[1\]](#cite_note-1)^, then create a user for the bugzilla database:

`root `[`#`]`mysql -u root -p`

    mysql> CREATE USER 'bugs'@'localhost' IDENTIFIED BY '$db_pass';
    mysql> GRANT SELECT, INSERT,
    UPDATE, DELETE, INDEX, ALTER, CREATE, LOCK TABLES,
    CREATE TEMPORARY TABLES, DROP, REFERENCES ON bugs.*
    TO bugs@localhost IDENTIFIED BY '$db_pass';
    mysql> FLUSH PRIVILEGES;
    mysql> \q

#### [PostgreSQL]

Once [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL") is installed and set up on the system, install bugzilla with the [[[postgres]](https://packages.gentoo.org/useflags/postgres)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] [USE flag](https://wiki.gentoo.org/wiki/USE_flag "USE flag"), then create a user and a database for bugzilla to use:

`root `[`#`]`su - postgres`

`postgres``createuser -U postgres -dRSP bugs`

Edit the following configuration file and add the following line (adjust according to PostgeSQL version):

[FILE] **`/etc/postgresql-15/pg_hba.conf`**

    host   all    bugs   127.0.0.1    255.255.255.255  md5

Then restart the database server:

`root `[`#`]`/etc/init.d/postgresql restart`

Or:

`root `[`#`]`rc-service postgresql-15 restart`

### [Checksetup]

Change directory to [/var/www/localhost/htdocs/bugzilla], then execute [checksetup.pl]:

`root `[`#`]`cd /var/www/localhost/htdocs/bugzilla`

`root `[`#`]`./checksetup.pl`

The first execution produces a [localconfig] file, in which the information about the database used must be put. The comments in that files are self-explanatory. Next, re-run [checksetup.pl], which will create the database, configure bugzilla and create the admin user.

## [Configuration]

### [Apache]

Add bugzilla to the default vhost:

[FILE] **`/etc/apache2/vhosts.d/default_vhost.include`**

    <Directory "/var/www/localhost/htdocs/bugzilla">
      AddHandler cgi-script .cgi
      Options +ExecCGI +FollowSymLinks
      DirectoryIndex index.cgi index.html
      AllowOverride All
    </Directory>

Or alternatively define another vhost, which will make bugzilla directly available at [https://127.0.0.1](https://127.0.0.1):

[FILE] **`/etc/apache2/vhosts.d/bugzilla_vhost.conf`**

    <VirtualHost *:80>
        ServerName localhost
        DocumentRoot "/var/www/localhost/htdocs/bugzilla"
        <Directory "/var/www/localhost/htdocs/bugzilla">
            AddHandler cgi-script .cgi
            Options +ExecCGI +FollowSymLinks
            DirectoryIndex index.cgi index.html
            AllowOverride All
            Require all granted
        </Directory>
        <IfModule mpm_peruser_module>
            ServerEnvironment apache apache
        </IfModule>
        CustomLog /var/log/apache2/bugzilla_access.log combined
        ErrorLog /var/log/bugzilla_error.log
    </VirtualHost>

Then restart the web server:

`root `[`#`]`/etc/init.d/apache2 restart`

## [Web end]

Finally, point a web browser to [https://127.0.0.1/bugzilla/](https://127.0.0.1/bugzilla/) or [https://127.0.0.1](https://127.0.0.1) depending on the configuration. Log in with the admin account and bugzilla will invite to proceed to the essential post-installation configuration ^[\[2\]](#cite_note-2)^.

## [Upgrading]

** Warning**\
Bugzilla cannot be downgraded.

** Note**\
Before upgrading, it is recommended to backup the application and its database.

To upgrade bugzilla [[[app-admin/webapp-config]](https://packages.gentoo.org/packages/app-admin/webapp-config)[]] ^[\[3\]](#cite_note-3)^ can be used. Upgrade is done automatically if the package is emerged without the `vhosts` flag. Finally, after upgrading, `checksetup.pl` should always be run to apply database changes and set file permissions ^[\[4\]](#cite_note-4)^.

Upgrades can also be done manually as follows, which applies if you installed your bugzilla application to [/var/www/localhost/htdocs/bugzilla], you may replace this location accordingly. Before emerging bugzilla, move your bugzilla directory:

`root `[`#`]`mv /var/www/localhost/htdocs/bugzilla /var/www/localhost/htdocs/bugzilla-old`

Then emerge bugzilla:

`root `[`#`]`emerge -av www-apps/bugzilla`

Next, copy the directories [data], [lib] (may be empty) and [template/en/custom] (may not exist) from your previous installation to your new installation, together with the previous [localconfig] file. Then run [checksetup.pl]:

`root `[`#`]`cp /var/www/localhost/htdocs/bugzilla-old/data /var/www/localhost/htdocs/bugzilla/ `

`root `[`#`]`cp -r /var/www/localhost/htdocs/bugzilla-old/lib /var/www/localhost/htdocs/bugzilla/ `

`root `[`#`]`cp -r /var/www/localhost/htdocs/bugzilla-old/template/en/custom var/www/localhost/htdocs/bugzilla/ `

`root `[`#`]`cp /var/www/localhost/htdocs/bugzilla-old/localconfig var/www/localhost/htdocs/bugzilla/ `

`root `[`#`]`cd /var/www/localhost/htdocs/bugzilla/ `

`root `[`#`]`./checksetup.pl `

After having ascertained that the new installation works as expected, the old bugzilla directory may be deleted.

## [Troubleshooting]

If after executing checksetup.pl an output similar to the following is received:

`root `[`#`]`/var/www/localhost/htdocs/bugzilla/checksetup.pl`

    Undefined subroutine utf8::SWASHNEW called at Bugzilla/Util.pm line 104.
    Compilation failed in require at Bugzilla/Mailer.pm line 21,  line 755.
    BEGIN failed--compilation aborted at Bugzilla/Mailer.pm line 21,  line 755.
    Compilation failed in require at Bugzilla/Auth.pm line 22,  line 755.
    BEGIN failed--compilation aborted at Bugzilla/Auth.pm line 22,  line 755.
    Compilation failed in require at Bugzilla.pm line 23,  line 755.
    BEGIN failed--compilation aborted at Bugzilla.pm line 23,  line 755.
    Compilation failed in require at ./checksetup.pl line 75,  line 755.

Then comment this line ^[\[5\]](#cite_note-5)^ ^[\[6\]](#cite_note-6)^.

[FILE] **`/var/www/localhost/htdocs/bugzilla/Bugzilla/Util.pm`**

    $var =~ tr/\x-\x//d;

Then re-execute [checksetup.pl].

## [More documentation]

Find more documentation on the official bugzilla documentation page ^[\[7\]](#cite_note-7)^.

## [References]

1.  [[[↑](#cite_ref-1)] [ [https://bugzilla.mozilla.org/show_bug.cgi?id=1604051](https://bugzilla.mozilla.org/show_bug.cgi?id=1604051) \[MySQL 8 Compatibility\] ]]
2.  [[[↑](#cite_ref-2)] [ [https://bugzilla.readthedocs.io/en/5.0/installing/essential-post-install-config.html](https://bugzilla.readthedocs.io/en/5.0/installing/essential-post-install-config.html) \[Essential Post-Installation Configuration\] ]]
3.  [[[↑](#cite_ref-3)] [ [Webapp-config](https://wiki.gentoo.org/wiki/Webapp-config "Webapp-config") ]]
4.  [[[↑](#cite_ref-4)] [ [https://bugs.gentoo.org/124282](https://bugs.gentoo.org/124282) \[Update causes internal error\] ]]
5.  [[[↑](#cite_ref-5)] [[Mozilla bug 1588175](https://bugzilla.mozilla.org/show_bug.cgi?id=1588175) - Undefined subroutine utf8::SWASHNEW called at Bugzilla/Util.pm line 109.]]
6.  [[[↑](#cite_ref-6)] [[Perl issue 17271](https://github.com/Perl/perl5/issues/17271) - Safe.pm]]
7.  [[[↑](#cite_ref-7)] [ [https://bugzilla.readthedocs.io/en/5.0/index.html](https://bugzilla.readthedocs.io/en/5.0/index.html) \[Bugzilla Documentation\] ]]