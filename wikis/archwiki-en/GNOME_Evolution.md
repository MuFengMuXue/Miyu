# GNOME/Evolution

Evolution is an application for managing email, calendars, contacts, tasks, notes, and RSS web feeds. It is the default mail client for GNOME and includes support for IMAP, Microsoft Exchange Server, Novell GroupWise, LDAP, WebDAV, CalDAV, and many other services and protocols.

## Installation
Install the  package. Non-GNOME users should also see #Using Evolution outside of GNOME.

Additional plugins:

*
*
*
*
*

## IMAP setup
See IMAP+ mail account settings in GNOME Help.

## Alternative IMAP setup
An alternative to letting Evolution connect directly to the IMAP server is to sync the IMAP server to your PC. This costs as much hard-disk space as you have mail, though it is possible to limit the folders synced in this manner (see #OfflineIMAP setup). An additional benefit (primary inspiration for this app) is that you have a full copy of your email, including attachments, on your PC for retrieval, even if on the move without an internet connection.

To set this up, you will need to install the  package. See https://www.offlineimap.org/ for more information.

## OfflineIMAP setup
OfflineIMAP takes its settings from the  file, which you will need to create. Most users will be able to use the template file below for a standard IMAP server. See OfflineIMAP for more information.

You will likely need to add additional translations if you are using Gmail.

For remote Mailserver repository:

For Local repository:

Other examples of nametrans configurations (including those for Courier IMAP servers) can be found at https://www.offlineimap.org/doc/nametrans.html.

You may also be interested in running offlineimap in the background.

## Evolution setup for offlineimap's maildir
See Maildir Format Mail Directories account settings in GNOME Help. Set the Mail Directory path in Edit > Preferences > Mail Accounts > Edit > Receiving Email to the "root" folder if you are using a variant of the  file from #OfflineIMAP setup. You can also choose to "check for new messages" more frequently in Receiving Options (like every minute instead of every 60 minutes) since this process will only check your local copy and not the server-side copy.

## Gmail setup
See Access a Gmail IMAP via Evolution or Access a Gmail POP Account via Evolution in GNOME Help. You may also be interested in reading Check Gmail through other email platforms (for IMAP) or Read Gmail messages on other email clients using POP in Gmail Help to manually fill in the following fields/checkboxes under Receiving Mail and/or Sending Mail in the Evolution Mail Configuration Assistant:

* Server Type
* Server and Port
** Server requires authentication
* Username
* Encryption method

OAuth2 (Google) should be selected from the drop-down menu under Authentication in Receiving Email.

## Gmail calendar
You can use your Gmail calendar in Evolution with one of two methods (barring GNOME Online Accounts as mentioned in #Gmail setup).

## Using a WebDAV calendar
Follow the steps under "Get your calendar (view only)" in Google's Calendar Help to obtain the "secret address in iCal format" for your desired calendar. Then follow the steps under Using a WebDev calendar in GNOME Help. Use the previously obtained secret address for the address in the URL field.

## Using a Google calendar
Follow the steps under Using a Google calendar in GNOME Help. You may need to grant GNOME Evolution access to your Google Account if prompted.

## Google contacts
Similarly with #Gmail calendar, you can also sync your Google contacts in Evolution. See Using a Google addressbook in GNOME Help for more information.

## Microsoft Exchange and Office 365
If your email is locally hosted on a Microsoft Exchange Server or cloud hosted on Office 365, you can use IMAP/POP and SMTP to access your email. However, some additional features such as access to Outlook Calendar and contact management are only available if you connect to the Microsoft Exchange Server or Office 365 server using Microsoft's proprietary Exchange ActiveSync (EAS) protocol.

There are two methods by which you can add/manage a Microsoft Exchange account in Evolution, but both will require Evolution EWS.

## Using GNOME Online Accounts
Install the  package if it is not already present. Then select Online Accounts in GNOME Settings and add a new Microsoft Exchange account with the following values:

{| class="wikitable"
! E-mail
| Your e-mail address (e.g. your.name@example.com)
|-
! Password
| Your e-mail account password or an app password from https://aka.ms/mfasetup
|-
! Username
| Your e-mail address once more
|-
! Server
| outlook.office365.com
|}

Your Exchange account should be listed alongside your other online accounts after clicking Connect. Choose what you want to synchronize (by default, all features are enabled).

## Without using GNOME Online Accounts
See https://wiki.gnome.org/Apps/Evolution/EWS/OAuth2; in particular, the introduction and "Configure the account in Evolution" for users of free accounts. In other words, users of free accounts do not need to concern themselves with application/tenant IDs since they cannot use OAuth2.

Access to the GNOME Evolution (EWS) application may not not allowed by your organization. One possible workaround (instead of requesting access from an administrator) is to select Basic instead of OAuth2 (Office365) from the drop-down menu under Authentication in the Receiving Email section of the Evolution Mail Configuration Assistant. Users of free accounts can also select Basic—this is an alternative to "creating an application specific password."

## Using Evolution outside of GNOME
Evolution relies on GNOME Keyring for storing account passwords, so to use Evolution outside of GNOME, see GNOME/Keyring#Using the keyring and make sure a password keyring with the name login exists.

## Spell checking
See Spell checking in GNOME Help. Evolution uses Enchant through , so you can use checkers other than Hunspell to facilitate spell checking.

## Tips and tricks
## Changing cipher settings
It is possible to change the advertised ciphers used to secure the connection to the server. Evolution does not provide a switch to change the settings for the used ciphers. However, since Evolution uses GnuTLS, it is possible to change the settings using environment variables.

One way to change these settings is to copy the  file to  and set the appropriate environment variable in the copied .desktop file. For example, make the following changes to avoid using ECC ciphers with NIST/NSA curves:

{{hc|~/.local/share/applications/org.gnome.Evolution.desktop|2=
...
Exec=env G_TLS_GNUTLS_PRIORITY=${G_TLS_GNUTLS_PRIORITY:-NORMAL:-ECDHE-ECDSA:-ECDHE-RSA} evolution %U
...
}}

A different way to achieve this would be with a wrapper script:

{{bc|1=
#!/bin/sh

export G_TLS_GNUTLS_PRIORITY=${G_TLS_GNUTLS_PRIORITY:-NORMAL:%COMPAT:\!VERS-SSL3.0}

exec /usr/bin/evolution
}}

The available cipher settings are documented in https://gnutls.org/manual/html_node/Priority-Strings.html.

## Use custom fonts
As default, Evolution offers only a few builtin fonts to be used for writing messages. However, you can set others fonts to be used as the "Default" option when writing HTML messages. That is done by creating a webkit editor plugin on . Check below an example using Microsoft's Calibri font:

{{bc|
'use strict';

var localhostBodyFontPlugin = {
   name : "localhostBodyFontPlugin",
   setup : function(doc) {
      if (doc.body) {
          doc.body.setAttribute("style", "font-family: Calibri,sans-serif; font-size: 11.0pt;")
      }
   }
};

EvoEditor.RegisterPlugin(localhostBodyFontPlugin);
}}
