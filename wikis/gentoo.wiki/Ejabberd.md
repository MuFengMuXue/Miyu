[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Ejabberd&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://www.process-one.net/en/ejabberd/)

[[]][Community](https://www.ejabberd.im/)

[[]][Package information](https://packages.gentoo.org/packages/net-im/ejabberd)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Ejabberd "wikipedia:Ejabberd")

[[]][Official documentation](http://docs.ejabberd.im/)

[[]][GitHub](https://github.com/processone/ejabberd)

**ejabberd** is an open source, multi-platform, XMPP application server and MQTT broker, written mainly in Erlang.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Service]](#Service)
        -   [[2.2.1] [OpenRC]](#OpenRC)
    -   [[2.3] [Set up a jabber server using ejabberd]](#Set_up_a_jabber_server_using_ejabberd)

## [Installation]

### [USE flags]

### [USE flags for] [net-im/ejabberd](https://packages.gentoo.org/packages/net-im/ejabberd) [[]] [Robust, scalable and extensible XMPP server]

  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [`+stun`](https://packages.gentoo.org/useflags/+stun)           Enable STUN/TURN support
  [`captcha`](https://packages.gentoo.org/useflags/captcha)       Support for CAPTCHA Forms (XEP-158) on registration
  [`debug`](https://packages.gentoo.org/useflags/debug)           Enable extra debug codepaths, like asserts and extra output. If you want to get meaningful backtraces see https://wiki.gentoo.org/wiki/Project:Quality_Assurance/Backtraces
  [`full-xml`](https://packages.gentoo.org/useflags/full-xml)     Use XML features in XMPP stream (ex: CDATA), requires XML compliant clients
  [`ldap`](https://packages.gentoo.org/useflags/ldap)             Add LDAP support (Lightweight Directory Access Protocol)
  [`mssql`](https://packages.gentoo.org/useflags/mssql)           Enable Microsoft SQL Server support (via ODBC) for data storage
  [`mysql`](https://packages.gentoo.org/useflags/mysql)           Enable MySQL support for data storage
  [`odbc`](https://packages.gentoo.org/useflags/odbc)             Enable ODBC support to access data storage
  [`pam`](https://packages.gentoo.org/useflags/pam)               Add support for PAM (Pluggable Authentication Modules) - DANGEROUS to arbitrarily flip
  [`postgres`](https://packages.gentoo.org/useflags/postgres)     Enable PostgreSQL support for data storage
  [`redis`](https://packages.gentoo.org/useflags/redis)           Enable Redis support for transient data
  [`roster-gw`](https://packages.gentoo.org/useflags/roster-gw)   Turn on workaround for processing gateway subscriptions
  [`selinux`](https://packages.gentoo.org/useflags/selinux)       !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sip`](https://packages.gentoo.org/useflags/sip)               Enable SIP support
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)         Enable SQLite database support
  [`zlib`](https://packages.gentoo.org/useflags/zlib)             Enable Stream Compression (XEP-0138) using zlib
  --------------------------------------------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-03-30 09:28] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

Install ejabberd:

`root `[`#`]`emerge --ask net-im/ejabberd`

Adding various modules through USE flags will trigger things like: [[[dev-lang/erlang]](https://packages.gentoo.org/packages/dev-lang/erlang)[]], [[[net-im/ejabberd]](https://packages.gentoo.org/packages/net-im/ejabberd)[]], etc. to be installed with ejabberd.

## [Configuration]

### [Files]

[] The information in this section is probably **outdated**. You can help the Gentoo community by verifying and [updating this section](https://wiki.gentoo.org/index.php?title=Ejabberd&action=edit).

** Important**\
ejabberd.cfg has been superseded by ejabberd.yml, which is formatted in a completely different way. For old .cfg config files, \"man ejabberdctl\" for an automatic conversion script, see *convert_to_yaml*.

In [/etc/jabber/ejabberd.cfg] put:

[FILE] **`/etc/jabber/ejabberd.cfg`**

    :}.

And:

[FILE] **`/etc/jabber/ejabberd.cfg`**

    :.

Where foo.bar is what is required for the accounts, like bob@foo.bar (so the server should be available at foo.bar. If not, clientside configuration needs extra server parameter).

In [/etc/jabber/ejabberctl.cfg] put:

[FILE] **`/etc/jabber/ejabberctl.cfg`**

    :ERLANG_NODE=ejabberd

So the node will be called ejabberd@süpercomputer while süpercomputer is the one configured in [/etc/conf.d/hostname] If this is changed, remember to issue:

`root `[`#`]`rc-service hostname restart`

### [Service]

#### [OpenRC]

Then start:

`root `[`#`]`rc-service ejabberd start`

Then create users:

`user `[`$`]`ejabberdctl register   `

For example:

`user `[`$`]`ejabberdctl register bob foo.bar süpersecret`

### [Set up a jabber server using ejabberd]

This often fails at first try, because the whole ejabberd-erlang-mnesia thing can be really picky sometimes. So, one hint may be to not initialize/start/test anything until the final hostname selections are in every config file. Changing hostname afterwards can cause problems, at least before becoming familiar with the above mentioned tools.

Second hint: If errors are encountered when restarting here, Erlang nodes might have to be stopped, which unfortunately are not called \'erlang\' or something, but \'beam\', so this might be found useful:

`user `[`$`]`killall beam -9`