[[]]This article has some todo items:\

-   Update Apache FastCGI instructions
-   Update Lighttpd instructions
-   Add instructions about fetching emails/generating tickets

[Request Tracker (RT)](https://www.bestpractical.com/rt/) is a battle-tested issue tracking system which thousands of organizations use for bug tracking, help desk ticketing, customer service, workflow processes, change management, network operations, youth counselling and even more. [Organizations around the world](https://www.bestpractical.com/rt/who.html) have been running smoothly thanks to RT for over 10 years.

## Contents

-   [[1] [About this guide]](#About_this_guide)
-   [[2] [Installation]](#Installation)
    -   [[2.1] [USE flags]](#USE_flags)
    -   [[2.2] [Requirements]](#Requirements)
    -   [[2.3] [Emerge]](#Emerge)
-   [[3] [Setup and configuration]](#Setup_and_configuration)
    -   [[3.1] [Database]](#Database)
    -   [[3.2] [Configuring RT]](#Configuring_RT)
        -   [[3.2.1] [Sendmail alternatives]](#Sendmail_alternatives)
    -   [[3.3] [Configuring the web server]](#Configuring_the_web_server)
        -   [[3.3.1] [Apache]](#Apache)
            -   [[3.3.1.1] [mod_perl]](#mod_perl)
            -   [[3.3.1.2] [mod_fastcgi]](#mod_fastcgi)
        -   [[3.3.2] [lighttpd (untested)]](#lighttpd_.28untested.29)
-   [[4] [Feeding emails into RT]](#Feeding_emails_into_RT)
    -   [[4.1] [MTA on same server]](#MTA_on_same_server)
    -   [[4.2] [Without a MTA]](#Without_a_MTA)
-   [[5] [Log in]](#Log_in)
-   [[6] [Special thanks]](#Special_thanks)
-   [[7] [See also]](#See_also)

## [About this guide]

This guide was written using the latest version of RT available, which at the time of this writing is 4.2.9.

This guide assumes familiarity with [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") or [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") and will not delve into the details of either.

Whether or not virtual hosting is used holds no bearing on the bulk of this guide. It will be noted if there\'s something significantly different that must be done in a virtual hosting environment.

## [Installation]

### [USE flags]

### [USE flags for] [www-apps/rt](https://packages.gentoo.org/packages/www-apps/rt) [[]] [RT is an enterprise-grade ticketing system]

  --------------------------------------------------------------- --------------------------------------------------------------------------------------
  [`+apache`](https://packages.gentoo.org/useflags/+apache)       Add www-servers/apache support
  [`+postgres`](https://packages.gentoo.org/useflags/+postgres)   Add support for the postgresql database
  [`fastcgi`](https://packages.gentoo.org/useflags/fastcgi)       Add support for the FastCGI interface
  [`lighttpd`](https://packages.gentoo.org/useflags/lighttpd)     Add www-servers/lighttpd support
  [`mysql`](https://packages.gentoo.org/useflags/mysql)           Add mySQL Database support
  [`nginx`](https://packages.gentoo.org/useflags/nginx)           Add www-servers/nginx support
  [`vhosts`](https://packages.gentoo.org/useflags/vhosts)         Add support for installing web-based applications into a virtual-hosting environment
  --------------------------------------------------------------- --------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-07-04 22:18] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Requirements]

RT requires a database backend and works equally well with either [MySQL](https://wiki.gentoo.org/wiki/MySQL "MySQL") or [PostgreSQL](https://wiki.gentoo.org/wiki/PostgreSQL "PostgreSQL"). Enable at most one of their USE flags:

`root `[`#`]`echo "www-apps/rt mysql" >> /etc/portage/package.use`

`root `[`#`]`echo "www-apps/rt postgres" >> /etc/portage/package.use`

RT also requires a Web server. The default is to run on [Apache](https://wiki.gentoo.org/wiki/Apache "Apache"), but [lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") is also documented. To use lighttpd, you must enable its USE flag:

`root `[`#`]`echo "www-apps/rt lighttpd" >> /etc/portage/package.use`

### [Emerge]

Many of the packages RT depends on, including RT\'s own package, are keyword masked. Use the following command to have a patch automatically generated.

`root `[`#`]`emerge -av --autounmask-write =www-apps/rt-4.2.9`

Once the previous command has finished, use [dispatch-conf] to apply the patch:

`root `[`#`]`dispatch-conf`

Run emerge again:

`root `[`#`]`emerge -av www-apps/rt`

When the `vhosts` USE flag is enabled, run [webapp-config] to finish the installation:

`root `[`#`]`webapp-config -I -h localhost -d rt rt 4.2.9`

## [Setup and configuration]

### [Database]

RT provides a script called [rt-setup-database] which creates the initial database and a database user.

`root `[`#`]`/var/www/localhost/rt-4.2.9/sbin/rt-setup-database --action init --dba dbasuperuser --prompt-for-dba-password`

    In order to create or update your RT database, this script needs to connect to your
    Pg instance on localhost (port '') as postgres
    Please specify that user's database password below. If the user has no database
    password, just press return.

    Password:
    Working with:
    Type:   Pg
    Host:   localhost
    Port:
    Name:   rt4
    User:   rt_user
    DBA:    postgres
    Now creating a Pg database rt4 for RT.
    Done.
    Now populating database schema.
    Done.
    Now inserting database ACLs.
    Done.
    Now inserting RT core system objects.
    Done.
    Now inserting data.
    Done inserting data.
    Done.

### [Configuring RT]

RT uses an overlay system for configuration. This means that the default configuration is declared in [/var/www/localhost/rt-4.2.9/etc/RT_Config.pm], and that custom configurations are declared in [/var/www/localhost/rt-4.2.9/etc/RT_SiteConfig.pm]. [RT_SiteConfig.pm] will not exist until manually created. Any custom configuration in [RT_SiteConfig.pm] will be preserved in upgrades, while the default configurations, [RT_Config.pm], will be overwritten.

Either copy certain sections from [RT_Config.pm] to [RT_SiteConfig.pm], or create a full config from scratch.

`root `[`#`]`cd /var/www/localhost/rt-4.2.9/etc `

`root `[`#`]`cp RT_Config.pm RT_SiteConfig.pm `

`root `[`#`]`chmod u+w RT_SiteConfig.pm `

`root `[`#`]`$EDITOR RT_SiteConfig.pm`

The configuration file is well documented, but the [official documentation](https://www.bestpractical.com/docs/) can also be consulted.

#### [Sendmail alternatives]

When not using a full-blown SMTP server locally, use a lightweight client to send the emails instead as long as it provides a sendmail-compatible executable. Mail options are specified in RT_SiteConfig.pm.

### [Configuring the web server]

Request Tracker can be run on any [PSGI compliant server](http://plackperl.org/). However, [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") and [Lighttpd](https://wiki.gentoo.org/wiki/Lighttpd "Lighttpd") are proven platforms.

#### [Apache]

Only information pertinent to RT will be covered. Additional information about [Apache](https://wiki.gentoo.org/wiki/Apache "Apache") is covered elsewhere.

There\'s little information about which method works better for RT on Apache, and benchmarks have shown mod_perl and FastCGI to be nearly equal.

##### [mod_perl]

Save the following snippet within the individual `VirtualHost` tags RT is installed to or [/etc/apache2/vhosts.d/default_vhost.include]:

[CODE]

    # Replace /rt with the proper URL path after the domain name
    <Location /rt>
        SetHandler modperl
        PerlResponseHandler Plack::Handler::Apache2
        # Correct this path
        PerlSetVar psgi_app /var/www/localhost/rt-4.2.9/sbin/rt-server
    </Location>

    <Perl>
        use Plack::Handler::Apache2;
        # Correct this one, too
        Plack::Handler::Apache2->preload("/var/www/localhost/rt-4.2.9/sbin/rt-server");
    </Perl>

Instruct Apache to start with mod_perl enabled:

[FILE] **`/etc/conf.d/apache2`**

    APACHE2_OPTS="... -D PERL"

It may be necessary to change the owner and group of RT\'s Mason data directory:

`root `[`#`]`chown -R apache:apache /var/www/localhost/rt-4.2.9/var/mason_data`

##### [mod_fastcgi]

NOTE: When using `mod_fastcgi`, instruct [webapp-config] to install `rt` with appropriate permissions. Edit [/etc/vhosts/webapp-config]:

[FILE] **`/etc/vhosts/webapp-config`**

    VHOST_DEFAULT_UID="rt"
    VHOST_DEFAULT_GID="rt"

Save the following snippet within the individual `VirtualHost` tags RT is installed to or [/etc/apache2/vhosts.d/default_vhost.include].

[CODE]

    # Tell FastCGI to put its temporary files somewhere sane
    #FastCgiIpcDir /tmp

    # Match the path to the file system location
    FastCgiServer /var/www/localhost/rt-4.2.9-r1/sbin/rt-server.fcgi -processes 5 -idle-timeout 300

    # Match the first path to the URL where RT is actually available
    # Match the second path to the file system location
    ScriptAlias /rt /var/www/localhost/rt-4.2.9-r1/sbin/rt-server.fcgi/

    # Match the path to the URL where RT is actually available
    <Location /rt>
        <IfVersion >= 2.4> # For Apache 2.4
            Require all granted
        </IfVersion>
        <IfVersion < 2.4>  # For Apache 2.2
            Order allow,deny
            Allow from all
        </IfVersion>

        Options +ExecCGI
        SetHandler fastcgi-script
    </Location>

Edit [/etc/conf.d/apache2] to instruct `apache2` to start with `FASTCGI` and enabled:

[FILE] **`/etc/conf.d/apache2`**

    APACHE2_OPTS="-D FASTCGI"

To have apache start on boot:

`root `[`#`]`rc-update add apache2 default`

Restart apache so that all changes made so far will take effect:

`root `[`#`]`/etc/init.d/apache2 restart`

#### [][lighttpd (untested)]

RT is able to run on `lighttpd` + `fastcgi`. The ebuild will install an init script [/etc/init.d/rt] and a config file [/etc/conf.d/rt].

NOTE: To use `mod_fastcgi`, instruct [webapp-config] to install `rt` with appropriate permissions. Edit [/etc/vhosts/webapp-config]:

[FILE] **`/etc/vhosts/webapp-config`**

    VHOST_DEFAULT_UID="rt"
    VHOST_DEFAULT_GID="rt"

Edit [/etc/conf.d/rt] to set `RTPATH` to the root of the installation. Everything else in that file can be left at there defaults normally.

Also note that, under the default configuration, the socket in `$FCGI_SOCKET_PATH` is owned by rt:lighttpd, and is chmod-ded to g+rwx. This means that user `lighttpd` needs to be in the `rt` group. One way to do that is to use `vigr`. To change that behaviour, edit [/etc/init.d/rt] to suit.

Edit [/etc/lighttpd.conf] to enable `mod_fastcgi`:

-   Uncomment `mod_fastcgi` under `server.modules`
-   set `server.document-root`
-   set `fastcgi.server` to something like this:

[FILE] **`/etc/lighttpd.conf`**

    fastcgi.server = ( "/rt" =&gt;
     ( "rt" =&gt;
     (
     "socket" =&gt; "/var/www/localhost/rt-3.6.1/var/appSocket",
     "check-local" =&gt; "disable"
     )
     )
     )

Be sure to set the correct path to socket (same as `$FCGI_SOCKET_PATH` in [/etc/conf.d/rt]).

Now, start `rt` and `lighttpd`:

`root `[`#`]`/etc/init.d/rt start `

`root `[`#`]`/etc/init.d/lighttpd start`

If things don\'t seem to be working, check the `lighttpd` logs in [/var/log/lighttpd] and edit [/etc/init.d/rt] as per the comments in the file to make the `rt` daemon more verbose.

Note: this initscript should work with any `fastcgi`-enabled webserver.

## [Feeding emails into RT]

There are a variety of methods to feed email into RT. Use an MTA, such as Postfix, Exim, or the real Sendmail, whenever possible. Follow the [MTA On Same Server](#MTA_On_Same_Server) portion of this section.

However, if the system is only fetching email from a remote server, an MTA is optional, just 2 or 3 smaller utilities are required. Follow the [Without An MTA](#Without_An_MTA) portion of this section.

### [MTA on same server]

TODO

### [Without a MTA]

There are 2 utilities needed: [[[net-mail/fetchmail]](https://packages.gentoo.org/packages/net-mail/fetchmail)[]] and [[[mail-mta/msmtp]](https://packages.gentoo.org/packages/mail-mta/msmtp)[]]. When using aliases delivered to the same email box, [[[mail-filter/procmail]](https://packages.gentoo.org/packages/mail-filter/procmail)[]] becomes necessary.

[FILE] **`/etc/fetchmailrc`Configuration file for fetchmail**

    set logfile "/var/log/fetchmail.log"
    set no bouncemail

    poll imap.example.com protocol IMAP;

    user "rt@example.com" there with password "password"
    ssl
    sslproto SSL3
    nofetchall
    keep
    no rewrite
    mda "/usr/bin/procmail -f %F /var/www/localhost/rt-4.2.9/etc/procmailrc";

[FILE] **`/var/www/localhost/etc/rt-4.2.9/etc/procmailrc`Configuration for procmail**

    LOGFILE=/var/log/procmail.log

    :0
    * ^To:.*help@example.com
    | /var/www/localhost/rt-4.2.9/bin/rt-mailgate --url http://localhost/rt --queue Help --action correspond

    :0
    * ^To:.*help-comment@example.com
    | /var/www/localhost/rt-4.2.9/bin/rt-mailgate --url http://localhost/rt --queue Help --action comment

## [Log in]

Use a browser to log into RT. Username is `root`, and password is `password`. Change the password.

## [Special thanks]

Thank you to all those who worked on the [original version](https://rt-wiki.bestpractical.com/wiki/GentooInstallGuide) of this guide.

## [See also]

-   [Password reset](https://wiki.gentoo.org/wiki/Request_Tracker/Password_reset "Request Tracker/Password reset")