# S-nail

Arch Linux uses S-nail as its POSIX  incarnation. S-nail is MIME capable and has extensions for line editing, S/MIME, SMTP, IMAP, POP3, and more. Mailx is the user side of the Unix mail system, whereas the system side was traditionally taken by sendmail. S-nail can also send directly to external SMTP servers, so no local MTA is required.

## Installation
Install the  package.

## Example usage
Because the systemwide configuration file () brings in some useful standards, sending mail over an installed local mail-transfer-agent (MTA), such as sendmail or postfix, can be as easy as follows:

 # echo 'Message body' | mailx --debug --subject='A subject' --attach=an_attachment.txt foo1@bar.example 'Foo2 '

Using the / flag results in a sandbox dry-run. You can adjust the program which is used as a MTA by setting the variable  (fine-tuning via , , ).

See the manual . In particular, see :

 # '
 # echo Message was passed successfully: $?

By default message delivery is asynchronous, and mailx will exit as soon as the prepared message has been passed over to the delivery mechanism, stating only whether message preparation was successful (or not). If the  option is set, however, the exit status of the started (builtin or not) MTA will be used as the message delivery "success" or "failure" status.

The / command line option will forcefully terminate option processing and turn on message send mode.

As shown in the previous example, commands can (and should) detach from environmental settings and configuration files via , /, and use explicit / and / command line flags to create their own reproducible setup.

Sending messages to files and pipes, without an MTA intervention, is possible with the  option:

 # echo bla | mailx --set=expandaddr --subject=test ./mbox.mbox
 # echo bla | mailx --set=expandaddr --subject=test '|cat >> ./mbox.mbox'
 # echo bla | mailx --set=expandaddr --subject=test -

 can be given a value and be used for address verification. The following example assumes somefile.pdf exists. As mentioned above, one should remove / to avoid a dry run. It sets the  option to the file used to record all outgoing mail, so that we then can look into the generated message:

 # echo Body | \
 >   LC_ALL=C.UTF-8 mailx --debug -:/ --set=v15-compat --set=sendwait --set=ttycharset=utf8 \
 >     --set=from='Me ' \
 >     --set=expandaddr=fail,-all,+addr \
 >     --set=nosave --set=record=/tmp/out.mbox \
 >     --set=mimetypes-load-control \
 >     --startup-cmd='mimetype application/pdf pdf' \
 >     --attach=somefile.pdf --subject=Subject \
 >      -. '(foo2bar) ' bob@hey.example
 # mailx --read-only --file /tmp/out.mbox

The manual sections , and  worth a glance when looking for more "quick shots".

In cases when in the following USER and PASS are specified as part of an URL (and only then), they must become URL-percent-encoded: mailx offers the  command which does this for you:

 # printf 'urlcodec encode USER PASS\nx\n' | mailx -#

 is for /. printf as well as mailx are subject to your locale settings:

 # # In UTF-8:
 # printf 'urlcodec encode SPAß\nx\n' | mailx -#
   SPA%C3%9F
 # # In ISO-8859-1:
 # printf 'urlc enc SPAß\nx\n' | mailx -#
   SPA%DF

## Configuration
Configuration files are the user-specific  and the systemwide , the latter of which is in the PKGBUILD's backup array, and hence will survive upgrades to s-nail. All the remaining examples in this article are based upon this configuration template, which simply sets some security and send mode basics:

 # All the examples require v15-compat!
 set v15-compat

 # Arch Linux-specific locations of certificates.
 # Since these are subject to the Arch Linux update mechanism,
 # use only those, do not try to load OpenSSL builtin ones.
 # And use the TLS specific set: see "man 8 update-ca-trust"
 #set tls-ca-dir=/etc/ssl/certs
 set tls-ca-file=/etc/ssl/certs/ca-certificates.crt
 set tls-ca-no-defaults
 #set tls-ca-flags=partial-chain

 # Do not use protocols older than TLS v1.2.
 # Change this only when the remote server does not support it:
 # CipherString: explicitly define the list of ciphers, which may
 #   improve security, especially with protocols older than TLS v1.2.
 #   See ciphers(1).  Possibly best to only use tls-config-pairs-HOST
 #   (or -USER@HOST), as necessary, again..
 #   Note that TLSv1.3 uses Ciphersuites= instead, which will join
 #   with CipherString (if protocols older than v1.3 are allowed)
 # Curves: especially with TLSv1.3 curves selection may be desired.
 # MinProtocol,MaxProtocol: do not use protocols older than TLS v1.2.
 #   Change this only when the remote server does not support it:
 #   maybe use chain support via tls-config-pairs-HOST / -USER@HOST
 #   to define such explicit exceptions, then, e.g.,
 #     MinProtocol=TLSv1.1
 set tls-config-pairs='\
      CipherString=TLSv1.2:!aNULL:!eNULL:@STRENGTH,\
      Curves=P-521:P-384:P-256,\
      Protocol=-ALL\, +TLSv1.2\, +TLSv1.3'

 # Request strict TLL transport layer security checks
 set tls-verify=strict

 # Essential setting: select allowed character sets
 # (Have a look at the "Character sets" manual section)
 set sendcharsets=utf-8,iso-8859-1

 # A very kind option: when replying to a message, first try to
 # use the same encoding that the original poster used herself!
 set reply-in-same-charset
 # When replying to or forwarding a message the comment and name
 # parts of email addresses are removed unless this variable is set
 set fullnames

 # When sending messages, wait until the Mail-Transfer-Agent finishs.
 set sendwait

 # Only use builtin MIME types, no mime.types(5) files.
 # That set is often sufficient, but look at the output of the
 # `mimetype' command to ensure this is true for you, too
 set mimetypes-load-control

 # Default directory where we act in (relative to $HOME if not absolute)
 set folder=mail
 # A leading "+" (often) means: under folder
 # record is used to save copies of sent messages, $DEAD is error storage
 # inbox: system mailbox, by default /var/mail/$USER: file %
 # $MBOX: secondary mailbox: file &
 set MBOX=+mbox.mbox record=+sent.mbox DEAD=+dead.mbox
 set inbox=+system.mbox

 # Define some shortcuts; now one may say, e.g., file mymbo
 shortcut mymbo %:+mbox.mbox \
          myrec +sent.mbox

 # This is optional, but you should get the big picture
 # by reading the manual before you leave that off
 set from="Your Name "

 # Mailing-list specifics (manual: "Mailing lists"):
 set followup-to followup-to-honour=ask-yes reply-to-honour=ask-yes
 # And teach some non-subscribed / some subscribed lists, too
 mlist @xyz-editor.xyz$ @xyzf.xyz$
 mlsubscribe ^xfans@xfans.xyz$

## Sending mail with an external SMTP server
To send messages via the built-in SMTP (Simple Mail Transfer Protocol) client to an external SMTP server, several options have to be set or adjusted. Add the following as appropriate to the configuration as above, changing bold strings. Reading the manual section  is worthwhile.

 # It can be as easy as
 # (Remember USER and PASS must be URL percent encoded)
 set mta=smtp://USER:PASS@HOST \
     smtp-use-starttls

 # It may be necessary to set hostname and/or smtp-hostname
 # if the "SERVER" of smtp and "domain" of from do not match.
 # Reading the "ON URL SYNTAX.." and smtp manual entries may be worthwhile
 set mta='''(smtp\
     smtp-auth=login[/plain... \
     smtp-use-starttls

 # E.g. here is a real life example of a very huge free mail provider
 # (Activate this account via mailx -AXooglX from the command line,
 # or use the ? accXooglX command in interactive mode)
 account XooglX {
    # Localize options, forget them when changing the account
    localopts yes
    # (The plain smtp:// proto is optional)
    set mta=smtp://USER:PASS@smtp.gmXil.com smtp-use-starttls
    set from="Your Name "
 }

 # And here is a pretty large one which does not allow sending mails
 # if there is a domain name mismatch on the SMTP protocol level,
 # which would bite us if the value of from does not match, e.g.,
 # for people who have a sXXXXeforge project and want to speak
 # with the mailing list under their project account (in from),
 # still sending the message through their normal mail provider
 account XandeX {
    localopts yes
    set mta=smtps://USER:PASS@smtp.yaXXex.ru:465 \
        hostname=yaXXex.com smtp-hostname=
    set from="Your Name "
 }

Note that, when storing passwords in , you should set appropriate permissions with . You can also set the netrc-lookup option and store user credentials in  (or $NETRC) instead; e.g., here is a real life example that sets up SMTP, POP3 as well as IMAP, storing all user credentials in there:

 account XandeX {
    localopts yes
    set from="Your Name "
    wysh set netrc-lookup # netrc-pipe='gpg -qd ~/.netrc.gpg'
    set mta=smtps://smtp.yXXXXx.ru:465 \
        smtp-hostname= hostname=yXXXXx.com
    set pop3-keepalive=240
    shortcut pop pop3s://pop.yXXXXx.ru
    # Type xp to login to the POP3 account
    commandalias xp 'fi pop'
    set imap-keepalive=240
    shortcut imap imaps://imap.yXXXXx.ru
    # Type xi to login to the IMAP account
    commandalias xi 'fi imap'
  }

and, in :

 machine *.yXXXXx.ru login USER password PASS

In this case USER and PASS are clear text, not URL encoded. You can further diversify things and use encrypted password storage. To adjust the example accordingly, simply encrypt your  file with OpenPGP and uncomment the  statement above.
The encrypted storage  can be created like this:

 # gpg -e .netrc
 # eval `gpg-agent --daemon --pinentry-program=/usr/bin/pinentry-curses --max-cache-ttl 99999 --default-cache-ttl 99999`

Test the configuration (use the / command line option for a dry-run):

 # echo test-body | mailx --verbose --verbose --account=XandeX --subject=test-subject some@where

## Interactive usage
Interactive usage is referred to throughout the manual as "compose mode". .

Mailx has a wide-glyph aware command line editor with history capabilities and coloured message display support. Because it strives for POSIX standard compliance some settings have to be adjusted before using it interactively does not baffle all descriptions, however. Reading  is unavoidable, but add, at a minimum, the following on top of the example configuration:

 # (The global configuration /etc/mail.rc provides some commented basics;
 # in particular it shows all options that POSIX mandates as defaults.)

 # Start into interactive mode even if the system mailbox is empty or
 # does not exist.  mailx will exit immediately without that one
 set emptystart

 # When composing a message, start directly into $EDITOR
 set editalong

 # Start $PAGER when a message is longer than VALUE lines;
 # without VALUE: screen $LINES
 set crt=

 # A nicer prompt for a modern terminal
 wysh set prompt='?\${?}!\${!}[\${account}#\${mailbox-display}? '

 # Add more entries to the history, and make that persistent
 set history-gabby history-file=+.s-nailhist
 # When printing messages, show only these headers
 # (Easier to retain what you want than to ignore
 # what you do not; use Print to see all headers and Show
 # to see the raw message content)
 retain date from to cc subject

 # Try to get around weird MIME attachment specifications
 # (This option can take a value, see the manual for more)
 set mime-counter-evidence=0xE

 # Display HTML parts inline, nicer than what the builtin viewer can achieve
 #set pipe-text/html='@* lynx -stdin -dump -force_html'
 # Learn another mimetype
 mimetype model/vrml wrl vrml

 # Create some new commands so that, e.g., `ls /tmp' will..
 commandalias ls !ls -latro
 commandalias ps !ps axu

Once you are in it use list to print all available builtin commands. Typing `?X' tries to expand "X" and print a help string; since mailx allows abbreviations of all commands this is sometimes handy, try, e.g., ?h, ?he and ?hel ... The command help will print a short summary of the most frequent used commands, more so if the variable  is set.

## Usage
When starting into interactive mode a summary of the content of the initially opened mailbox is printed, as via the  command.
In the header display messages are given numbers (starting at 1) which uniquely identify messages. Messages can be printed with the  command, or short: . Whereas  honours ed (or d) list of headers to be displayed, the rint command will not and display all headers; the ow command will print raw message content.

By default the current message (dot) is printed, but just like with many other commands it is possible to specify lists of messages, as is documented in the manual section ; e.g.,  will display all unread messages,  will print the current message (dot),  will print the messages 1 and 5 and  and  will print the previous and the next message, respectively. Note that simply typing RETURN in an empty line acts like  () and thus prints the next message.

The command  is nice for an overview, e.g., {{ic|f '@ ~/pair.pem

and setup S-nail via

 set smime-sign-cert=~/pair.pem \
     smime-sign-message-digest=SHA256 \
     smime-sign

From now any message that is sent will be signed. The default message digest would be SHA1, as mandated by RFC:5751. Note that S/MIME always works relative to the setting of the variable from, so it seems best to instead place the above settings in an . The  command verifies S/MIME messages, but note that S/MIME decryption and verification is solely based upon OpenSSL for now, which only supports messages with a simplistic MIME structure.

## Workaround missing OpenPGP support
S-nail does not yet support OpenPGP. However, using a macro it is possible to at least automatically verify inline ed messages, and using command ghosts their usage becomes handy: e.g., use the following in resource file and you will be able to verify a clearsigned message by just typing :

{{bc|
define V {
   \localopts yes; \wysh set pipe-text/plain=$'@*#++=@\
      &1");\
            print "--- GPG --verify ---";\
            print "";\
            next;\
         }\
         /^-----BEGIN PGP SIGNATURE-----/,/^-----END PGP SIGNATURE-----/ {\
            next;\
         }\
         {print}\
         \'';\
      print
}
define RK {
  !printf 'Key IDs to gpg --recv-keys: ';\
    read keyids;\
    gpg --recv-keys ${keyids};
}
commandalias V '\'call V
commandalias RK '\call RK'
}}

## Using an IMAP mailbox
The following are only quick hints. It is also possible to define folder and inbox to point to IMAP server folders, for example. Internationalized names are supported.

 set v15-compat
 # or many servers will expire the session
 set imap-keepalive=240
 set imap-cache=~/.imap_cache

 # You may want to define shortcuts to folders, for example:
 shortcut myimap "imaps://USER:PASS@server:port"
 set inbox=myimap
