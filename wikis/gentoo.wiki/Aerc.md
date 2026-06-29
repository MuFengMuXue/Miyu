**Resources**

[[]][Home](https://aerc-mail.org/)

[[]][Package information](https://packages.gentoo.org/packages/mail-client/aerc)

[[]][Official documentation](https://man.sr.ht/~rjarry/aerc/)

[[]][GitWeb](https://git.sr.ht/~rjarry/aerc)

[[]][GitHub](https://github.com/rjarry/aerc)

[[]][Bugs (upstream)](https://todo.sr.ht/~rjarry/aerc)

[[]][[#aerc](ircs://irc.libera.chat/#aerc)] ([[webchat](https://web.libera.chat/#aerc)])

[aerc] is a lightweight, command-line [mail user agent](https://en.wikipedia.org/wiki/mail_user_agent "wikipedia:mail user agent") (MUA) written in the [Go](https://wiki.gentoo.org/wiki/Go "Go") programming language. Setup includes a simple startup wizard to assist users in connecting their first mail server.

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [USE flags]](#USE_flags)
    -   [[1.2] [Emerge]](#Emerge)
    -   [[1.3] [Additional software]](#Additional_software)
        -   [[1.3.1] [text/html MIME type support]](#text.2Fhtml_MIME_type_support)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Setup wizard]](#Setup_wizard)
    -   [[2.2] [Files]](#Files)
-   [[3] [See also]](#See_also)

## [Installation]

### [USE flags]

### [USE flags for] [mail-client/aerc](https://packages.gentoo.org/packages/mail-client/aerc) [[]] [Email client for your terminal]

  ----------------------------------------------------------- -------------------------------------
  [`notmuch`](https://packages.gentoo.org/useflags/notmuch)   Enable support for net-mail/notmuch
  ----------------------------------------------------------- -------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2025-11-04 16:01] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

### [Emerge]

`root `[`#`]`emerge --ask mail-client/aerc`

### [Additional software]

#### [][text/html MIME type support]

To view email with embedded text/html MIME type content, the [[[www-client/w3m]](https://packages.gentoo.org/packages/www-client/w3m)[]] and [[[net-proxy/dante]](https://packages.gentoo.org/packages/net-proxy/dante)[]] packages should be installed (according to [man aerc-tutorial]), and the text/html filter uncommented in the [\~/.config/aerc/aerc.conf] configuration file.

## [Configuration]

### [Setup wizard]

In general, to setup, run [aerc] and enter the values as appropriate, substituting the following information as necessary. It should take all of about 2 minutes to get connected to a mail server presuming the connection information is readily available.

For example, for a Gentoo developer to connect their email account to the mail server provided by Gentoo\'s [Infrastructure project](https://wiki.gentoo.org/wiki/Project:Infrastructure "Project:Infrastructure"):

**Basic account information:**

  --------------- ------------------
  Field           Value
  Name            Gentoo
  Full name       Larry the Cow
  Email address   larry@gentoo.org
  --------------- ------------------

  : First page of startup wizard

**Incoming mail (IMAP):**

  ----------------- --------------------
  Field             Value
  username          larry
  password          \
  Server address    dev.gentoo.org:143
  Connection mode   IMAP with STARTTLS
  ----------------- --------------------

  : Second page of startup wizard (IMAP)

**Outgoing mail (SMTP):**

  ----------------- ---------------------
  Field             Value
  username          larry
  password          \
  Server address    smtp.gentoo.org:587
  Connection mode   SMTP with STARTTLS
  ----------------- ---------------------

  : Third page of startup wizard (SMTP)

Once the program is connected to a mail account, it is helpful to perform some configuration changes to make it more friendly for reading Gentoo related mail.

### [Files]

If conversation threads/threading is desired, then (for at least v0.7.1 and prior) a filter will need to be applied to enable threading:

[FILE] **`~/.config/aerc/aerc.conf`Helpful aerc customization for Gentoo**

    #
    # aerc main configuration

    # Added to thread discussions in Gentoo
    [ui:account=Gentoo]
    threading-enabled=true

## [See also]

-   [Mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt") --- a text-based, command-line mail user agent (MUA).
-   [Neomutt](https://wiki.gentoo.org/wiki/Neomutt "Neomutt") --- command-line mail client forked from [[mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")].
-   [Thunderbird](https://wiki.gentoo.org/wiki/Thunderbird "Thunderbird") --- Mozilla\'s solution to the e-mail client.