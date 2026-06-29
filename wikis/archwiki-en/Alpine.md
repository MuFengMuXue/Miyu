# Alpine

Alpine is based on pine, a text-based E-mail and newsclient that was originally released by the University of Washington in 1991. It is an easier to use alternative to mutt, a more lightweight approach to the mail reader concept.

## Installation
Install  or . Optionally a spellchecker may be installed. Alpine supports both  and .

 is a glue program that links GnuPG and Alpine.

## IMAP
Launch alpine:

 $ alpine

Navigate to the configuration page by pressing  then . Fill in your name, the name of your mailserver in "User Domain", and your SMTP server for sending mail. The format for the SMTP server is as follows:

 mailserver.org:portnumber/user=username/ssl (or tls)

Also note the format for where Alpine is configured to keep saved and postponed messages. This keeps the messages on the mailserver, instead of saving them locally.

 {mailserver.org}path/to/folder

The following example assumes a mailserver located at mailserver.org that uses STARTTLS, a user named Jim Bob, and common locations for mail folders on the server.

 Personal Name                     = Jim Bob
 User Domain                       = mailserver.org
 SMTP Server (for sending)         = mailserver.org:587/user=jimbob123/tls
 NNTP Server (for news)            =
 Inbox Path                        = {mailserver.org}Inbox
 Incoming Archive Folders          =
 Pruned Folders                    =
 Default Fcc (File carbon copy)    = {mailserver.org}Sent
 Default Saved Message Folder      = {mailserver.org}Archives
 Postponed Folder                  = {mailserver.org}Drafts
 Read Message Folder               =
 Form Letter Folder                =
 Trash Folder                      = {mailserver.org}Trash
 Literal Signature                 =
 Signature File                    =
 Feature List                      =

Press  to exit config. From the main menu, navigate the collectionLists page by pressing ( then ) to configure folders. Press enter to edit the folders on mailserver.org, and optionally set a nickname. The Server line uses the same format as the SMTP Server line above, except that this is for retrieving rather than sending mail. The following example is for an IMAP server:

 mailserver.org:143/user=jimbob123/tls

The Path and View fields can often be left blank.

## Setting the return address
To set a return address, enter the configuration page and navigate to the "Customized Headers" field (either use the "Whereis" command to search, or page down a few pages to find this) and change the value to:

 From:  Jim Bob

Of course, replace Jim Bob with your name and put your proper e-mail address in the <>.

## What else can you configure?
Almost anything, in particular you can specify which colors to use, (from the main menu press  for set up, then  for colors), a browser to open external links (this is in the "Config" setup that we have previously been modifying"), an alternate text editor to use, different folder views, etc.

Pressing  allows you to quickly search for options. Messages can be listed in localtime by enabling the option "Convert Dates to Localtime". Toggling options can be done using the enter key.

## Printing from alpine
Printing from Alpine directly to  does not work with special characters like Germanic umlauts in the Mail to be printed. The  program does help.
You can then edit :
 # Your default printer selection
 printer=YOURPRINTER a2ps -q --center-title --footer -PYOURPRINTER

 # List of special print commands
 personal-print-command=YOURPRINTER [ a2ps -q --center-title --footer -PYOURPRINTER

 # Which category default print command is in
 personal-print-category=3
Replace YOURPRINTER with the name of your printer. Note that these settings can also be applied in the setup UI of Alpine. See the manpage of  for more configuration options.

## Remote configuration
From the setup page, press  to enter RemoteConfigSetup. You will be prompted to upload your addressbook, signature, and configuration. In order to use the remote configuration on any computer, on the command line, enter:

 $ alpine -p "{mailserver.org:143/user=jimbob123/tls}remote_pinerc"

It may be desirable to make this command an alias in your shell configuration file.

## Tips and tricks
There is no direct, or immediately apparent command for arbitrarily invoking an update of the inbox, however, as indirectly referenced in the manual;
 New mail checking and notification occurs automatically every 2.5 minutes and after certain commands, e.g. refresh-screen (Ctrl-L).
