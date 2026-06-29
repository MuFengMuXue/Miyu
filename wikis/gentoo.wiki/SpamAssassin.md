**Resources**

[[]][Home](https://spamassassin.apache.org)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Apache_SpamAssassin "wikipedia:Apache SpamAssassin")

[[]][Package information](https://packages.gentoo.org/packages/category/package)

[[]][Official documentation](https://spamassassin.apache.org/doc.html)

SpamAssassin is email spam filter software maintained by the Apache Foundation and written in Perl.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Files]](#Files)
    -   [[2.2] [Bayes SQL database]](#Bayes_SQL_database)
-   [[3] [Usage]](#Usage)
    -   [[3.1] [Spam detection rules]](#Spam_detection_rules)
    -   [[3.2] [Automated spam rule updates]](#Automated_spam_rule_updates)
-   [[4] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [mail-filter/spamassassin](https://packages.gentoo.org/packages/mail-filter/spamassassin) [[]] [An extensible mail filter which can identify and tag spam]

  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`berkdb`](https://packages.gentoo.org/useflags/berkdb)           Add support for sys-libs/db (Berkeley DB)
  [`cron`](https://packages.gentoo.org/useflags/cron)               Install a cron job to update SpamAssassin\'s rules daily.
  [`ipv6`](https://packages.gentoo.org/useflags/ipv6)               Add support for IP version 6
  [`ldap`](https://packages.gentoo.org/useflags/ldap)               Add LDAP support (Lightweight Directory Access Protocol)
  [`mysql`](https://packages.gentoo.org/useflags/mysql)             Add mySQL Database support
  [`postgres`](https://packages.gentoo.org/useflags/postgres)       Add support for the postgresql database
  [`qmail`](https://packages.gentoo.org/useflags/qmail)             Build qmail functionality and docs
  [`selinux`](https://packages.gentoo.org/useflags/selinux)         !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`sqlite`](https://packages.gentoo.org/useflags/sqlite)           Add support for sqlite - embedded sql database
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                 Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`test`](https://packages.gentoo.org/useflags/test)               Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`verify-sig`](https://packages.gentoo.org/useflags/verify-sig)   Verify upstream signatures on distfiles
  ----------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-26 02:33] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask mail-filter/spamassassin`

## [Configuration]

### [Files]

SpamAssassin comes with a number of modules (or plugins) that can be enabled or disabled via configuration files.

-   [/etc/mail/spamassassin] - Directory containing SpamAssassin modules.

When new plugins appear in a release of SpamAssassin, they are configured in a file named (for example) [v341.pre], which corresponds to SpamAssassin v3.4.1 and contains configuration for new plugins as of that version.

A user\'s local configuration belongs in [local.cf]; however, any file with a [.cf] suffix (in that same directory) will be loaded by SpamAssassin.

### [Bayes SQL database]

By default, SpamAssassin comes configured to use BerkeleyDB (`USE=berkdb`) for its bayes database. System administrator\'s who choose some other database backend (e.g. `USE=mysql`, `USE=postgres`, or `USE=sqlite`) will to configure SpamAssassin to use the alternative database backend before SpamAssassin will run.

Detailed instructions are provided with SpamAssassin and can be found in [README.bayes] within the SpamAssassin documentation directory (something like [/usr/share/doc/spamassassin\*/README.bayes]).

## [Usage]

### [Spam detection rules]

Gentoo\'s SpamAssassin ebuilds do not include spam detection rules, so these will need downloaded as part of the post-install process. The simplest way to do so is to run the [sa-update] command.

The SpamAssassin project\'s GPG key (so that the authenticity of the rules can be verified) must be downloaded and installed:

`root `[`#`]`wget -q https://spamassassin.apache.org/updates/GPG.KEY `

`root `[`#`]`sa-update --import GPG.KEY `

Next download the rules:

`root `[`#`]`sa-update`

To improve performance it is recommended to compile the spam detection rule set:

`root `[`#`]`sa-compile`

### [Automated spam rule updates]

The SpamAssassin project regularly releases new and updated rules. It is a good idea to schedule updates (at least) daily, so that the rules are never out of date. A cron job is ideal for this, and newer revisions of the SpamAssassin package supply a cron file. Enable the `cron` USE flag and re-emerge [[[mail-filter/spamassassin]](https://packages.gentoo.org/packages/mail-filter/spamassassin)[]].

## [See also]

[Thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird") --- Mozilla\'s solution to the e-mail client.