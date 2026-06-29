# Thunderbird

Thunderbird is an open source email, news, and chat client previously developed by the Mozilla Foundation.

## Installation
Install the  package, with a language pack if required.

Other versions include:

*
*
*

A version overview, both past and future, can be read on MozillaWiki:Releases.

## Securing
* Thunderbird sends your system's internal IP address to the configured SMTP server as an argument to the HELO/ELHO SMTP command. This value can be overridden by setting  to, for example, . Setting this value may increase the spam score of messages you send. See and [https://kb.mozillazine.org/Mail_and_news_settings.
* To hide Thunderbird's User Agent, set  to  and create a new empty  string entry in the #Config editor.
* JavaScript is disabled for message content but not for RSS news feeds. To disable set  to  in the #Config editor.

## Extensions
*
*
*
*

## OpenPGP: signing and encryption
From Thunderbird 78.2.1 onwards, this functionality is integrated into Thunderbird. This was previously provided by the Enigmail add-on, which is not compatible with Thunderbird 78+. To migrate keys from Enigmail to Thunderbird, as well as learn what is currently supported, see Thunderbird OpenPGP FAQ. Before migration, make sure that a strong passphrase is used for the master password. Otherwise the private key will not be properly protected.

## Tips and tricks
## Config editor
Thunderbird can be extensively configured by clicking the Thunderbird Menu > Settings > General and looking for the Config Editor button at the bottom of the page.
Alternatively, if the menu bar is toggled the Config Editor button can be found by clicking Edit > Settings > General

## Set the default browser
Thunderbird uses the default browser as defined by the XDG MIME Applications. This is commonly modified by desktop environments (for example GNOME's Control Center: Details > Default Applications > Web).

This can be overridden with  in the #Config editor

If the following is all set to  (default), set them to  and Thunderbird will ask you which application to use when you click on a link (remember to also check "Remember my choice for .. links").

 network.protocol-handler.warn-external.http
 network.protocol-handler.warn-external.https

## Plain text mode and font uniformity
Plain Text mode lets you view all your emails without HTML rendering and is available in View > Message Body As. This defaults to the Monospace font but the size is still inherited from original system fontconfig settings. The following example will overwrite this with Ubuntu Mono of 10 pixels (available in: ).

Remember to run  to update system font cache. See Font configuration for more information.

## Migrate profile to another system
At first close a running Thunderbird. Then locate the profile folder  and copy it recursively to a backup location.
Before starting Thunderbird on the new machine the first time, restore the profle from the backup location to .

For more details see https://support.mozilla.org/en-US/kb/moving-thunderbird-data-to-a-new-computer.

## Export and import
Before you start with Importing or Exporting tasks, backup your complete  profile:

 $ cp -R ~/.thunderbird /to/backup/folder/

If your accounts are broken or you want to join two different Thunderbird installations, you can install ImportExportTools NG add-on for both Thunderbird installations and following this just export and import all your data to the new installation.

## Change the default sorting order
Thunderbird (up to at least 31.4.0-1) sorts mail by date with the oldest on top without any threading. While this can be changed per folder, it is easier to set a sane default instead as described here.

Set these preferences in the #Config editor:

 mailnews.default_sort_order = 2 (descending)
 mailnews.default_view_flags = 1 (Threaded view)

## Maildir support
The default message store format is mbox. To enable the use of Maildir, see MozillaWiki:Thunderbird/Maildir. You basically have to set the following preference in the #Config editor:

 mail.serverDefaultStoreContractID = @mozilla.org/msgstore/maildirstore;1

Some limitations up to at least 31.4.0-1: only the "tmp" and "cur" directories are supported. The "new" directory is completely ignored. The read state of mails are stored in a separate ".msf" file, so initially all local mail using Maildir will be marked as unread even when located in the "cur" directory. It is also possible to change this setting in the regular user interface now: Go to Menu > Settings > General > Indexing > Message Store Type for new accounts and choose File per message (maildir).

## Spell checking
Install hunspell and a hunspell language dictionary and restart Thunderbird.

See the Firefox article for how to set the default spell checking language.

## Native notifications
Make sure that  in the #Config editor is set to "true" (default). This option means that extensions (such as Gnome Integration) are not needed for these newer versions of Thunderbird.

You might also need to install a notification server.

## Sound
Thunderbird can be configured to play sounds when new emails are received and when calendar reminders are dispatched. This requires .

## Theming tweaks
Thunderbird should conform to GTK#Themes as defined on your system.  However, two tweaks are desirable for full consistency.  These are most beneficial for dark themes.

# To view the body of emails with colors following your theme:
## Go to Menu > Settings > General
## Find the Language & Appearance section
## Click the Colors button
## Check Use system colors
## Set the option for Override the colors specified by the content with my selection above to Always or Only with High Contrast themes
# To view Lightning calendar with colors following your theme:
## Go to Menu > Preferences > Preferences
## Select the Calendar tab
## Check Optimize colors for accessibility

Further customization can be attained by creating and editing a .  See Firefox/Tweaks#General user interface CSS settings and Mozillazine's userchrome page.

## Keyboard bindings
Thunderbird unfortunately lacks an easy way to disable single-key bindings, such that pressing e.g. "a" on the keyboard will not archive a message. The tbkeys-lite extension provides a means of editing and deleting such bindings and is available for Thunderbird 68.0 onwards.

## Use OpenPGP with external GnuPG
Starting with v78.1, Thunderbird now ships with integrated OpenPGP support previously provided by Add-Ons like Enigmail. It will offer you to migrate your existing Enigmail keys into Thunderbird upon the first start after the update. If you do not want to store your private keys inside Thunderbird, it is possible to use Thunderbird with an external GnuPG installation in order to keep your keys safe or use a Smartcard.

To view any OpenPGP keys stored inside Thunderbird:
# Go to Menu > Tools > OpenPGP Key Manager
# Disable View > Display Keys From Other People for better visibility of your own keys. Private keys are displayed in bold.
# Review present keys and possibly delete them.
# Import public keys of any external private keys you want to use using File > Import public key(s) from file. See GnuPG#Export your public key.
To enable external GnuPG support in Thunderbird:
# Ensure you have relevant keys available or created.
# Open the #Config editor
# Search for  and set its value to
# Go to Menu > Account Settings and select the account you want to use.
# Click Manage Identities and select the Identity you want to edit.
# Click Edit > End-To-End Encryption > Add Key.
# Select Use your external key through GnuPG and paste your key ID from GnuPG.
Refer to MozillaWiki:Thunderbird:OpenPGP:Smartcards for further instructions and specialized configurations.

## Wayland
Starting with version 128, Thunderbird defaults to Wayland instead of XWayland and does not require any configuration. Older versions of Thunderbird support opting into Wayland mode via an environment variable.
 $ MOZ_ENABLE_WAYLAND=1 thunderbird

## Tor
To route the connection to the server through the Tor network the proxy settings must be set accordingly.

# Make sure you have  installed and that the process is running.
# In Thunderbird go to Menu > Settings > General. In the Network & Disk Space > Connection section, click on the Settings... button.
# Select Manual proxy configuration, enter localhost as SOCKS Host and 9050 as Port (9050 is the default; it may be configured differently in /etc/tor/torrc). Select Proxy DNS when using SOCKS v5.

## Troubleshooting
## LDAP Segfault
An LDAP clash (Bugzilla#292127) arises on systems configured to use it to fetch user information. A possible workaround consists of renaming the conflicting bundled LDAP library.

## Error: Incoming server already exists
If you want to reinstall a previously deleted account with the same account data, you might get a popup with "Incoming server already exists". See bug Bugzilla#1121151 for details. Unfortunately, if you get this error you can now only clean reinstall Thunderbird:

# Make a backup of your current profile:
# Export all your Accounts, Calendar and Feeds via an add-on like it is written in Export section of this Wiki.
# Close Thunderbird
# Remove all your data by deleting your current Thunderbird folder .
# Start Thunderbird
# Create your mail accounts, feeds and calendars (empty).
# Install the ImportExportTools NG add-on
# Import all your data.

## Thunderbird UI freezes when receiving a new message
If Thunderbird is configured to show an alert when a new message arrives, or at launch, the lack of a notification daemon may freeze the interface (white screen) for many seconds. You can solve this issue by disabling alerts or installing a notification server.

## LC_TIME environment variable not respected
Thunderbird should use the  environment variable for localization, but it might not do so in all contexts. Some problems can be mitigated by setting Menu > Preferences > Preferences > Advanced > Date and Time Formatting to Regional settings locale, a setting which was introduced in Thunderbird 56.

With version 60, Gecko started using the CLDR project for localization, including datetime formatting, which uses different settings than most other software based purely on . There is a bug report for this issue that includes workarounds with varying effects. To achieve ISO-8601-formatted dates in Thunderbird and a week beginning on Monday, use .

Starting in Thunderbird version 91, one can set a number of preferences to make Thunderbird compliant with ISO-8601. Most programs can be set to ISO-8601 by setting your region locale to , but by default Thunderbird ignores regional locale preferences. See for details.

## Authentication failure while connecting to server imap.gmail.com error when using OAuth2 with G Suite account
Sometimes Thunderbird fails to log in to G Suite with Authentication failure while connecting to server imap.gmail.com error. It can be fixed with setting  setting to  in #Config editor and then passing authentication stage again.

## Outlook 365 SMTP fails to authenticate with OAuth2 authentication
Apparently by default, SMTP authentication is disabled for Outlook 365 accounts. Use the Microsoft 365 admin center to enable it. Refer to: [https://docs.microsoft.com/en-us/exchange/clients-and-mobile-in-exchange-online/authenticated-client-smtp-submission Enable SMTP AUTH for specific mailboxes.

## Difficulties using Thunderbird to access Outlook 365 accounts
Version 102.7.0 of Thunderbird included changes to the OAUTH2 implementation that affected access to Outlook 365 accounts (see and [https://bugzilla.mozilla.org/show_bug.cgi?id=1810760). Affected users should directly upgrade to 102.7.1 or newer.

## Cannot login to access Outlook 365 accounts
If, after being redirected to your institution's login page, inserting credentials and pressing the login button, you are being redirected to the same login page, try to:

# Remove cookies and cache with Menu > Tools > Clear Recent History, on Time range to clear select Everything, on History select Browsing History, Cookies, Cache, click Ok.
# Enable cookies with Edit > Settings > Privacy & Security and under Web Content check Accept cookies from sites
