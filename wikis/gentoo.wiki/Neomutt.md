[] This article is a [stub](https://wiki.gentoo.org/wiki/Category:Stub "Category:Stub"). Please help out by [expanding it](https://wiki.gentoo.org/index.php?title=Neomutt&action=edit) - [how to get started](https://wiki.gentoo.org/wiki/Gentoo_Wiki:Contributor%27s_guide "Gentoo Wiki:Contributor's guide").

**Resources**

[[]][Home](https://neomutt.org)

[[]][Official documentation](https://neomutt.org/guide/index)

[[]][Package information](https://packages.gentoo.org/packages/mail-client/neomutt)

[[]][GitHub](https://github.com/neomutt/neomutt)

[[]][Bugs (upstream)](https://github.com/neomutt/neomutt/issues)

[[]][[#neomutt](ircs://irc.libera.chat/#neomutt)] ([[webchat](https://web.libera.chat/#neomutt)])

[**neomutt**] is a command-line mail client forked from [[mutt](https://wiki.gentoo.org/wiki/Mutt "Mutt")].

## Contents

-   [[1] [Installation]](#Installation)
    -   [[1.1] [Emerge]](#Emerge)
    -   [[1.2] [USE Flags]](#USE_Flags)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Configuration Scripts]](#Configuration_Scripts)
        -   [[2.1.1] [Mutt Wizard]](#Mutt_Wizard)
-   [[3] [External URLs]](#External_URLs)

## [Installation]

### [Emerge]

`root `[`#`]`emerge --ask mail-client/neomutt`

### [USE Flags]

### [USE flags for] [mail-client/neomutt](https://packages.gentoo.org/packages/mail-client/neomutt) [[]] [A small but very powerful text-based mail client]

  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------
  [`autocrypt`](https://packages.gentoo.org/useflags/autocrypt)           Enable autocrypt.org support
  [`berkdb`](https://packages.gentoo.org/useflags/berkdb)                 Enable BDB (Berkley DB) backend for header caching
  [`doc`](https://packages.gentoo.org/useflags/doc)                       Add extra documentation (API, Javadoc, etc). It is recommended to enable per package instead of globally
  [`gdbm`](https://packages.gentoo.org/useflags/gdbm)                     Enable GDBM (GNU dbm) backend for header caching
  [`gnutls`](https://packages.gentoo.org/useflags/gnutls)                 Prefer net-libs/gnutls as SSL/TLS provider (ineffective with USE=-ssl)
  [`gpgme`](https://packages.gentoo.org/useflags/gpgme)                   Build gpgme backend to support S/MIME, PGP/MIME and traditional/inline PGP
  [`idn`](https://packages.gentoo.org/useflags/idn)                       Enable support for Internationalized Domain Names
  [`kerberos`](https://packages.gentoo.org/useflags/kerberos)             Add kerberos support
  [`kyotocabinet`](https://packages.gentoo.org/useflags/kyotocabinet)     Enable Kyoto Cabinet database backend for header caching
  [`lmdb`](https://packages.gentoo.org/useflags/lmdb)                     Enable LMDB (Lightning Memory-Mapped Database) backend for header caching
  [`lz4`](https://packages.gentoo.org/useflags/lz4)                       Add lz4 support for header cache compression
  [`nls`](https://packages.gentoo.org/useflags/nls)                       Add Native Language Support (using gettext - GNU locale utilities)
  [`notmuch`](https://packages.gentoo.org/useflags/notmuch)               Enable support for net-mail/notmuch
  [`pgp-classic`](https://packages.gentoo.org/useflags/pgp-classic)       Build classic-pgp backend to support PGP/MIME and traditional/inline PGP
  [`qdbm`](https://packages.gentoo.org/useflags/qdbm)                     Enable QDBM (Quicker Database Manager) database backend for header caching
  [`sasl`](https://packages.gentoo.org/useflags/sasl)                     Add support for the Simple Authentication and Security Layer
  [`selinux`](https://packages.gentoo.org/useflags/selinux)               !!internal use only!! Security Enhanced Linux support, this must be set by the selinux profile or breakage will occur
  [`smime-classic`](https://packages.gentoo.org/useflags/smime-classic)   Build classic-smime backend to support S/MIME
  [`ssl`](https://packages.gentoo.org/useflags/ssl)                       Add support for SSL/TLS connections (Secure Socket Layer / Transport Layer Security)
  [`test`](https://packages.gentoo.org/useflags/test)                     Enable dependencies and/or preparations necessary to run tests (usually controlled by FEATURES=test but can be toggled independently)
  [`tokyocabinet`](https://packages.gentoo.org/useflags/tokyocabinet)     Enable Tokyo Cabinet database backend for header caching
  [`zlib`](https://packages.gentoo.org/useflags/zlib)                     Add zlib support for header cache compression
  [`zstd`](https://packages.gentoo.org/useflags/zstd)                     Add zstd support for header cache compression
  ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------------------

[Data provided by the [Gentoo Package Database](https://packages.gentoo.org) · Last update: 2026-05-04 10:54] [[More information about USE flags](/wiki/Handbook:AMD64/Working/USE)]

## [Configuration]

Configure Neomutt in the configuration file located in [\~/.config/neomutt/neomuttrc].

Here is an example from the official github:

[FILE] **`~/.config/neomutt/neomuttrc`**

    ##########################################################################
    #   00 - Neomutt configuration
    ##########################################################################
    # -------------------------------------------------------------------------
    # Name: tmpdir
    # -------------------------------------------------------------------------
    # This variable allows you to specify where NeoMutt will place its
    # temporary files needed for displaying and composing messages.  If this
    # variable is not set, the environment variable $TMPDIR is used.   Failing
    # that, then “/tmp” is used.
    # -------------------------------------------------------------------------

    # set tmpdir=/tmp
    # -------------------------------------------------------------------------
    # Name: alias_file
    # -------------------------------------------------------------------------
    # The  default  file  in  which  to  save aliases created by the
    # <create-alias> function.  Entries added to this file  are  encoded  in
    # the  character  set  specified  by  $con‐ fig_charset if it is set or the
    # current character set otherwise.
    # -------------------------------------------------------------------------

    # set alias_file="~/.neomuttrc"
    # set alias_file="~/.neomutt/alias"

    # -------------------------------------------------------------------------
    # Note: NeoMutt will not automatically source this file; you must
    # explicitly use the “source” command for it to be executed in case this
    # option points to a dedicated alias file.
    # -------------------------------------------------------------------------

    # source "~/.neomutt/alias"
    # -------------------------------------------------------------------------
    # Name: query_command
    # -------------------------------------------------------------------------
    # This  specifies  the  command  NeoMutt  will use to make external address
    # queries.  The string may contain a “%s”, which will be substituted with
    # the  query  string  the  user types.   NeoMutt  will  add quotes around
    # the string substituted for “%s” automatically according to shell quoting
    # rules, so you should avoid adding your own.  If no  “%s”  is found  in
    # the  string,  NeoMutt will append the user's query to the end of the
    # string.  See “query” for more information.
    # -------------------------------------------------------------------------

    # set query_command = "/usr/bin/lbdbq '%s'"
    ##########################################################################
    #   01 - Basic personal setup
    ##########################################################################
    # -------------------------------------------------------------------------
    # Name: alternates
    # -------------------------------------------------------------------------
    # alternates  is used to inform NeoMutt about alternate addresses where you
    # receive mail; you can use regular expressions (regex) to specify
    # alternate  addresses.  This  affects NeoMutt's idea about messages from
    # you, and messages addressed to you.  unalternates  can be used to write
    # exceptions to alternates patterns. To remove a regu‐ lar expression from
    # the alternates list, use the unalternates command with exactly  the same
    # regex or use “*” to remove all entries.  The  optional  -group flag
    # causes all of the subsequent regular expressions to be added to or
    # removed from the named group.

    # alternates mymailbox@domain.tld
    # alternates mymailbox@work.tld
    # -------------------------------------------------------------------------
    # Name: realname
    # -------------------------------------------------------------------------
    # This variable specifies what “real” or “personal” name should be used
    # when sending mes‐ sages.  If not specified, then the user's “real name”
    # will  be  read  from  /etc/passwd.   This option will not be used, if
    # “$from” is set.
    # -------------------------------------------------------------------------

    # set realname = "Firstname Lastname"

    # -------------------------------------------------------------------------
    # Name: from
    # -------------------------------------------------------------------------
    # When set, this variable contains a default “from” address.  It can be
    # overridden  using “my_hdr” (including from a “send-hook”) and
    # $reverse_name.  This variable is ignored if $use_from is unset.  If not
    # specified, then it may be read from the environment variable $EMAIL.
    # -------------------------------------------------------------------------

    # set from="mailbox@domain.tld"
    # -------------------------------------------------------------------------
    # Name: alias / unalias
    # -------------------------------------------------------------------------
    # alias  defines a surrogate key for the given address(es). Each address
    # will be resolved into either an email address  (user@example.com) or a
    # named  email  address  (User  Name <user@example.com>).   The  address
    # may be specified in either format, or in the format “user@example.com
    # (User Name)”.  Note: If you want to create an alias for more than one
    # address, you must  separate the addresses with a comma (“,”).  unalias
    # removes  the  alias corresponding to the given key or all aliases when
    # “*” is used as an argument.  The optional -group flag causes the
    # address(es) to be added  to or  removed from  the named group.
    # -------------------------------------------------------------------------

    # unalias *
    # alias Lastname.Firstname Full Name <mailbox@domain.tld>
    # alias -group Groupname Lastname.Firstname Full Name <mailbox@domain.tld>
    ##########################################################################
    #   02 - Mailbox and folders
    ##########################################################################
    # -------------------------------------------------------------------------
    # Name: mbox_type
    # -------------------------------------------------------------------------
    # The default mailbox type used when creating new folders. May be any of
    # “mbox”, “MMDF”, “MH” or “Maildir”.
    # -------------------------------------------------------------------------

    # set mbox_type=mbox
    # set mbox_type=Maildir
    # -------------------------------------------------------------------------
    # Name: folder
    # -------------------------------------------------------------------------
    # Specifies the default location of your mailboxes.  A “+” or “=” at the
    # beginning  of  a pathname  will be expanded to the value of this
    # variable.  Note that if you change this variable (from the default) value
    # you need to make  sure  that  the  assignment  occurs before you use “+”
    # or “=” for any other variables since expansion takes place when han‐
    # dling the “mailboxes” command.
    # -------------------------------------------------------------------------

    # set folder=~/Mail
    # -------------------------------------------------------------------------
    # Name: spoolfile
    # -------------------------------------------------------------------------
    # If your spool mailbox is in a non-default place where NeoMutt cannot find
    # it,  you  can specify its location with this variable.  If not specified,
    # then the environment variables $MAIL and $MAILDIR will be checked.
    # -------------------------------------------------------------------------

    # set spoolfile = ""
    # -------------------------------------------------------------------------
    # Name: postponed
    # -------------------------------------------------------------------------
    # NeoMutt  allows you to indefinitely “postpone sending a message” which
    # you are editing.  When you choose to postpone a message, NeoMutt saves it
    # in  the  mailbox  specified  by this variable.  Also see the $postpone
    # variable.
    # -------------------------------------------------------------------------

    # set postponed = "~/postponed"
    # set postponed = "+Drafts"
    # -------------------------------------------------------------------------
    # Name: record
    # -------------------------------------------------------------------------
    # This specifies the file into which your outgoing messages should be
    # appended.  (This is meant as the primary method for saving a copy of your
    # messages, but another way  to  do this  is using the “my_hdr” command to
    # create a “Bcc:” field with your email address in it.) The value of
    # $record is overridden by the $force_name and $save_name variables, and
    # the “fcc-hook” command.  Also see $copy.
    # -------------------------------------------------------------------------

    # set record = "~/sent"
    # set record = "+Sent"
    # -------------------------------------------------------------------------
    # Name: trash
    # -------------------------------------------------------------------------
    # If set, this variable specifies the path of the trash folder where the
    # mails marked for deletion will be moved, instead of being irremediably
    # purged.  NOTE:  When you delete a message in the trash folder, it is
    # really deleted, so that you have a way to clean the trash.
    # -------------------------------------------------------------------------

    # set trash = ""
    # set trash = "+Trash"

    # -------------------------------------------------------------------------
    # Name: mailboxes
    # -------------------------------------------------------------------------
    # The mailboxes  specifies  folders which can receive mail and which will
    # be checked for new messages. When changing folders, pressing space will
    # cycle through folders with new mail.  The named-mailboxes is an
    # alternative to mailboxes that allows adding a description for a mailbox.
    # NeoMutt can be configured to display the description instead of the
    # mailbox path.  The unmailboxes  command  is used to remove a file name
    # from the list of folders which can receive mail.  If “*” is specified as
    # the file name, the list is emptied.
    # -------------------------------------------------------------------------

    # unmailboxes *
    # mailboxes +Drafts +Sent +Spam
    ##########################################################################
    #   03 - Compose email
    ##########################################################################
    # -------------------------------------------------------------------------
    # Name: my_hdr / unmy_hdr
    # -------------------------------------------------------------------------
    # Using my_hdr, you can define headers which will be added to the messages
    # you  compose.  unmy_hdr will remove the given user-defined headers.
    # -------------------------------------------------------------------------

    # unmy_hdr *
    # my_hdr X-Location: Europe, Germany
    # -------------------------------------------------------------------------
    # Name: user_agent
    # -------------------------------------------------------------------------
    # When set, NeoMutt will add a “User-Agent:”  header  to  outgoing
    # messages,  indicating which version of NeoMutt was used for composing
    # them.
    # -------------------------------------------------------------------------

    # set user_agent

    # -------------------------------------------------------------------------
    # Name: editor
    # -------------------------------------------------------------------------
    # This variable specifies which editor is used by NeoMutt.  It defaults to
    # the  value  of the  $VISUAL,  or  $EDITOR,  environment  variable, or to
    # the string “vi” if neither of those are set.  The $editor string may
    # contain a %s escape, which will be replaced by the name  of  the file  to
    # be edited.  If the %s escape does not appear in $editor, a space and the
    # name to be edited are appended.  The resulting string is then executed by
    # running sh -c 'string' where string is the expansion of $editor described
    # above.
    # -------------------------------------------------------------------------

    # set editor = "vi"
    # set editor="vim -c 'set spell spelllang=de,en' -c 'set colorcolumn=72' -c 'startinsert' -c 'set tw=7    2 et' -c 'set wrap' '+/^$'"
    # -------------------------------------------------------------------------
    # Name: edit_headers
    # -------------------------------------------------------------------------
    # This option allows you to edit the header of your outgoing messages along
    # with the body of your message.  Although  the  compose menu may have
    # localized header labels, the labels passed to your editor will be
    # standard RFC2822 headers, (e.g. To:, Cc:, Subject:).  Headers  added  in
    # your editor must also be RFC2822 headers, or one of the pseudo headers
    # listed in “edit- header”.  NeoMutt will not understand localized header
    # labels, just  as  it  would  not when parsing an actual email.  Note
    # that changes made to the References: and Date: headers are ignored for
    # interoper‐ ability reasons.
    # -------------------------------------------------------------------------

    # set edit_headers
    # -------------------------------------------------------------------------
    # Name: ispell
    # -------------------------------------------------------------------------
    # How to invoke ispell (GNU's spell-checking software).
    # -------------------------------------------------------------------------

    # set ispell="ispell"
    # set ispell="aspell -e -c"
    # -------------------------------------------------------------------------
    # Name: attribution
    # -------------------------------------------------------------------------
    # This is the string that will precede a message which has been included in
    # a reply.  For a full listing of defined printf(3)-like sequences see the
    # section on $index_format.

    # set attribution = "On %d, %n wrote:"
    # set attribution = "Am %, den % um % % schrieb %F:"
    # -------------------------------------------------------------------------
    # Name: forward_format
    # -------------------------------------------------------------------------
    # This variable controls the default subject when forwarding a message.  It
    # uses the same format sequences as the $index_format variable.
    # -------------------------------------------------------------------------

    # set forward_format = "[%a: %s]"
    # -------------------------------------------------------------------------
    # Name: signature
    # -------------------------------------------------------------------------
    # Specifies the filename of your signature, which is appended to all
    # outgoing  messages.  If  the filename ends with a pipe (“

### [Configuration Scripts]

#### [Mutt Wizard]

Initial setup of Neomutt can be intimidating to those who have not done it before. To make the process easier, [[[mail-client/mutt-wizard]](https://packages.gentoo.org/packages/mail-client/mutt-wizard)[]] was created. As the name suggests, it walks the user step-by-step through the process of setting up a proper [muttrc] file.

There might be a few errors which can be solved with the USE Flag sasl.

Set the use flag in [/etc/portage/package.use], then re-emerge [neomutt]:

`root `[`#`]`emerge --ask neomutt`

## [External URLs]

-   [neomutt.org](https://neomutt.org)
-   [neomutt/samples](https://github.com/neomutt/samples)