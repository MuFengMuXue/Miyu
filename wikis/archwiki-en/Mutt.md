# Mutt

Mutt is a text-based mail client renowned for its powerful features. Though over two decades old, Mutt remains the mail client of choice for a great number of power users.

Mutt focuses primarily on being a Mail User Agent (MUA), and was originally written to view mail. Later implementations (added for retrieval, sending, and filtering mail) are simplistic compared to other mail applications and, as such, users may wish to use external applications to extend Mutt's capabilities.

Nevertheless, the Arch Linux  package is compiled with IMAP, POP3 and SMTP support, removing the necessity for external applications.

This article covers using both native IMAP sending and retrieval, and a setup depending on OfflineIMAP or getmail (POP3) to retrieve mail, procmail to filter it in the case of POP3, and msmtp to send it.

## Installation
Install the  package. A popular fork with more features is .

Optionally install external helper applications for an IMAP setup, such as isync or OfflineIMAP.

Or (if using POP3) , ,  or  and .

## Configuration
This section covers #IMAP, #POP3, #Maildir and #SMTP configuration.

Mutt will, by default, search six locations for its configuration file; , , and , first with  appended, then without. Any of these locations will work. In case you decide to put the initialization file somewhere else, use . You should also know some prerequisite for Mutt configuration. Its syntax is very close to the Bourne Shell. For example, you can get the content of another configuration file:

 source /path/to/other/config/file

You can use variables and assign the result of shell commands to them.

 set editor=`echo \$EDITOR`

Here the  gets escaped so that it does not get substituted by Mutt before being passed to the shell. Also note the use of the backquotes, as bash syntax  does not work. Mutt has a lot of predefined variables, but you can also set your own. User variables must begin with "my"!

 set my_name = "John Doe"

## IMAP
## Native IMAP support
The  package is compiled with IMAP support. At the very least you need to have four lines in your muttrc file to be able to access your mail.

## imap_user
 set imap_user=USERNAME

## imap_pass
If unset, the password will be prompted for.

 set imap_pass=SECRET

## folder
Instead of a local directory which contains all your mail (and directories), use your server (and the highest folder in the hierarchy, if needed).

 set folder=imapYou do not have to use a folder, but it might be convenient if you have all your other folders inside your INBOX, for example. Whatever you set here as your folder can be accessed later in Mutt with just an equal sign (=) or a plus sign (+). Example:

 set folder=imaps://imap.gmail.com/

It should be noted that for several accounts, it is best practice to use different folders -- e.g. for account-hook. If you have several Gmail accounts, use

 set folder=imaps://username@imap.gmail.com/

instead, where your account is username@gmail.com. This way it will be possible to distinguish the different folders. Otherwise it would lead to authentication errors.

## spoolfile
The spoolfile is the folder where your (unfiltered) e-mail arrives. Most e-mail services conventionally name it INBOX. You can now use '=' or '+' as a substitution for the full  path that was configured above. For example:

 set spoolfile=+INBOX

## mailboxes
Any IMAP folders that should be checked regularly for new mail should be listed here:

 mailboxes =INBOX =family
 mailboxes imaps://imap.gmail.com/INBOX imaps://imap.gmail.com/family

Alternatively, check for all subscribed IMAP folders (as if all were added with a  line):

 set imap_check_subscribed

These two versions are equivalent if you want to subscribe to all folders. So the second method is much more convenient, but the first one gives you more flexibility. Also, newer Mutt versions are configured by default to include a macro bound to the 'y' key which will allow you to change to any of the folders listed under mailboxes.

If you do not set this variable, the spoolfile will be used by default. This variable is also important for the #Sidebar.

## Summary
Using these options, you will be able to start Mutt, enter your IMAP password, and start reading your mail. Here is a muttrc snippet (for Gmail) with some other lines you might consider adding for better IMAP support.

## External IMAP support
While IMAP support is built into Mutt, it does not download mail for offline use. It is possible to use an external application such as OfflineIMAP or isync to download your emails to a local folder which can then be processed by Mutt.

Consider using applications such as  or  to sort mail.

## POP3
The  package is compiled with POP3 support, which is configured via the  variables as described in .

Alternatively, it is possible to use external programs to fetch mail using POP3. One popular option is to use getmail for retrieving and procmail for filtering the mail.

## Maildir
Maildir is a generic and standardized format. Almost every MUA is able to handle Maildirs and Mutt's support is excellent. There are just a few simple things that you need to do to get Mutt to use them. Open your muttrc and add the following lines:

This is a minimal Configuration that enables you to access your Maildir and checks for new local Mails in INBOX. This configuration also caches the headers of the eMails to speed up directory-listings. It might not be enabled in your build (but it sure is in the Arch-Package). Note that this does not affect OfflineIMAP in any way. It always syncs all of the directories on a Server.  tells Mutt which local directories to poll for new Mail. You might want to add more Spoolfiles (for example the Directories of Mailing-Lists) and maybe other things. But this is subject to the Mutt manual and beyond the scope of this document.

## SMTP
Whether you use POP or IMAP to receive mail you will probably still send mail using SMTP.

## Folders
There is basically only one important folder here: the one where all your sent e-mails will be saved.

 set record = +Sent

Gmail automatically saves sent e-mail to , so we do not want duplicates.

 unset record

## Native SMTP support
The  package is compiled with SMTP support.

Here are the common SMTP settings:

If your SMTP server is STARTTLS-based, add the following:

If your SMTP server is SMTPS-based, add the following instead:

If your SMTP credentials are not the same as your IMAP credentials, then you must use the correct credentials instead of  and .

If you get an error like , then your server probably uses STARTTLS instead of SMTPS.

If your server uses the LOGIN authentication method you might need to specify this explicitly, despite the manual's claim that all methods are tried by default:

See  for more information.

## External SMTP support
An external SMTP agent such as msmtp, sSMTP or  can also be used.

The  variable in your  determines the program and arguments used to deliver mail in mutt. Any additional arguments must be interpreted by the program as recipient addresses.

For example, if using msmtp:

## Sending mails from Mutt
Now, startup :

You should see all the mail in . Press  to compose mail; it will use the editor defined by your  environment variable. If this variable is not set, you can fix it before starting Mutt:

 $ export EDITOR=your-favorite-editor
 $ mutt

You can also set the editor from Mutt's configuration file:

For testing purposes, address the letter to yourself. After you have written the letter, save and exit the editor. You will return to Mutt, which will now show information about your e-mail. Press  to send it.

## Multiple accounts
Now you should have a working configuration for one account at least. You might wonder how to use several accounts, since we put everything into a single file.

Well all you need is to write account-specific parameters to their respective files and source them. All the IMAP/POP3/SMTP configuration for each account should go to its respective folder.

Mutt can handle this thanks to one of its most powerful features: hooks. Basically a hook is a command that gets executed before a specific action. There are several hooks available. For multiple accounts, you must use account-hooks and folder-hooks.

* Folder-hooks will run a command before switching folders. This is mostly useful to set the appropriate SMTP parameters when you are in a specific folder. For instance when you are in your work mailbox and you send a e-mail, it will automatically use your work account as sender.
* Account-hooks will run a command every time Mutt calls a function related to an account, like IMAP syncing. It does not require you to switch to any folder.

Hooks take two parameters:

 account-hook [!regex command
 folder-hook command

The regex is the folder to be matched (or not if preceded by the !). The command tells what to do.

Let us give a full example:

Finally  should be similar to .

Now all your accounts are set, start Mutt. To switch from one account to another, just change the folder ( key). Alternatively you can use the sidebar.

To change folder for different mailboxes you have to type the complete address -- for IMAP/POP3 folders, this may be quite inconvenient -- let us bind some key to it.

With the above shortcuts (or with the sidebar) you will find that changing folders (with  by default) is not contextual, i.e. it will not list the folders of the current mailbox, but of the one used the last time you changed folders. To make the behaviour more contextual, the trick is to press = or + for current mailbox. You can automate this with the following macro:

 macro index 'c' '?^K='

## Alternative way
Another method to use mutt with multiple accounts is to run multiple mutt instances. You can have common settings in .muttrc and account specific settings in their respective files. Now you can source .muttrc from account specific config file. Advantage of this method is folder switching is not required to access different accounts, which improves workflow and saves time. For example,

Finally  should be similar to . Now you can run mutt with

 mutt -F .mutt/work
 mutt -F .mutt/personal

or create alias mutt_work in your .bashrc

 alias mutt_work="mutt -F .mutt/work"
 alias mutt_personal="mutt -F .mutt/personal"

or write a script to start all mutt instances in one go,

 #!/bin/sh
 lxterminal -e mutt -F .mutt/work
 lxterminal -e mutt -F .mutt/personal

## Passwords management
Keep in mind that writing your password in  is a security risk. One solution is to always enter the password manually, but this becomes cumbersome.

## GPG
An alternative solution is to encrypt your password with GnuPG in an encrypted file. Setup your own keypair if you have not done so already. Create a file in a tmpfs with the following contents:

 set my_pass = "password"

Then encrypt this file, setting yourself as the recipient and move it into an accessible location. In this example the encrypted file resides at $HOME/.my-pwds.gpg.

In your mutt configuration file add the following before any account:

 source "gpg -dq $HOME/.my-pwds.gpg |"

This decrypts the file quietly and sets the variable  in this example. This can be used in any variable after it has been sourced. For example:

If you use external tools like OfflineIMAP and msmtp, you need to set up an agent (e.g. gpg-agent, see GnuPG#gpg-agent) to keep the passphrase into cache and thus avoiding those tools always prompting for it.

## Pass
You can also use pass to encrypt your passwords easily. Just add the passwords to the given passwords as follows:
 pass add user@domain.tld
After that, just add the command  in your , for instance:
 set imap_pass="`pass show user@domain.tld`"
Note the use of both backquotes and regular quotes to prevent the output of the backquotes from being parsed[https://neomutt.org/guide/configuration.html#ex-backtick-dblquotes.

## Security concern
If  is available from the UI, it is possible to see the password unencrypted, which may be undesired if anybody else than you has access to your session while Mutt is running. You may want to disable it for this reason. As a consequence, every command that the user intends to use must be bound to a key in advance, otherwise it will never be accessible.

## Tips and tricks
Guides to get you started with using and customizing Mutt:

* My first Mutt (maintained by Bruno Postle)
* The Woodnotes Guide to the Mutt Email Client (maintained by Randall Wood)
* The Homely Mutt (by Steve Losh)
* Everything You Need To Know To Start Using GnuPG with Mutt (by Justin R. Miller)
* A List of useful programs that often are used in combination with Neomutt

If you have any Mutt specific questions, feel free to ask in the Arch IRC channels.

## Key bindings
The default key bindings are quite far from the more common Emacs-like or Vi-like bindings. You can customize them to your preference. Mutt has a different set of bindings for the pager, the index, the attachment view, etc. Thus you need to specify which map you want to modify when you bind a key. You can review the list of commands and key bindings from Mutt's help page (default key: ). Example of Vi-like bindings:

## Composition
## Encrypt and sign mail (GnuPG)
To start encrypting mail in mutt using GnuPG copy  to your mutt configuration folder (e.g. to ). Then append the following to your mutt configuration file (e.g. ):

 source ~/.mutt/gpg.rc

Most encryption options are then available by pressing  in the compose view.

See the  and  options in .

## E-mail character encoding
When using Mutt there are two levels where the character sets that must be specified:

* The text editor used to write the e-mail must save it in the desired encoding.
* Mutt will then check the e-mail and determine which encoding is the more appropriate according to the priority you specified in the  variable. Default: "us-ascii:iso-8859-1:utf-8".

So if you write an e-mail with characters allowed in ISO-8859-1 (like 'résumé'), but without characters specific to Unicode, then Mutt will set the encoding to ISO-8859-1.

To avoid this behaviour, set the variable in your :

 set send_charset="us-ascii:utf-8"

or even

 set send_charset="utf-8"

The first compatible charset starting from the left will be used. Since UTF-8 is a superset of US-ASCII it does not harm to leave it in front of UTF-8, it may ensure old MUA will not get confused when seeing the charset in the e-mail header.

## Custom mail headers
One of the greatest thing in Mutt is that you can have full control over your mail header.

First, make your headers editable when you write e-mails:

 set edit_headers=yes

Mutt also features a special function  for customizing your header. Yes, it is named just like a variable, but in fact it is a function.

You can clear it completely, which you should do when switching accounts with different headers, otherwise they will overlap:

 unmy_hdr *

Other variables have also an impact on the headers, so it is wise to clear them before using :

 unset use_from
 unset use_domain
 unset user_agent

Now, you can add any field you want -- even non-standard one -- to your header using the following syntax:

 my_hdr :

Note that  can be the result of a command.

Example:

## Signature block
Create a .signature in your home directory.  Your signature will be appended at the end of your email. Alternatively you can specify a file in your Mutt configuration:

 set signature="path/to/sig/file"

## Random signature
You can use fortune (package ) to add a random signature to Mutt.

Create a fortune file and then add the following line to your .muttrc:

Note the pipe at the end. It tells Mutt that the specified string is not a file, but a command.

## Compose and send from command line
Man pages will show all available commands and how to use them, but here are a couple of examples. You could use Mutt to send alerts, logs or some other system information, triggered by login through , or as a regular cron job.

Send a message:

 mutt -s "Subject" somejoeorjane@someserver.com
This is bold text
}}

Now before sending the mail, use the  command (default shortcut ), and replace  by .

## Display another email while composing
A common complaint with Mutt is that when composing a new mail (or reply), you cannot open another mail (i.e. for checking with another correspondent) without closing the current mail (postponing). The following describes a solution:

First, fire up Mutt as usual. Then, launch another terminal window. Now start a new Mutt with

 mutt -R

This starts Mutt in read-only mode, and you can browse other emails at your convenience. It is strongly recommended to always launch a second Mutt in read-only mode, as conflicts will easily arise otherwise.

## Printing
You can install  for fancier printing quality. In your muttrc file, insert:

 set print_command="/usr/bin/muttprint %s -p {PrinterName}"

## Viewing content
## Viewing URLs in a web browser
This can be done using ,  or  . To use urlscan, install  and insert below in the mutt config file.

 macro index,pager \cb " urlscan" "call urlscan to extract URLs out of a message"
 macro attach,compose \cb " urlscan" "call urlscan to extract URLs out of a message"

Hitting ctrl+b will list all the urls from the email. The BROWSER environment variable can be used to select default web browser.

Default keybindings can be listed with F1 key. There is no need to create config file for urlscan unless additional keybindings or color-schemes are required. If desired default config file at  can be created using below command.

 urlscan -g

To use urlview inplace of urlscan, install the  package and add the following lines in mutt config file.

 macro index,pager \cb " urlview" "call urlview to extract URLs out of a message"
 macro attach,compose \cb " urlview" "call urlview to extract URLs out of a message"

Create a .urlview in $HOME and insert the following:

 REGEXP (((http|https|ftp|gopher)|mailto)>"\t*|www\..,;\t>">\):
 COMMAND  %s

Hitting ctrl+b while using mutt will list all the urls from the email. Navigate up or down with arrow keys and hit enter on the desired url. Your browser will start and go to the selected site.

Some browser will require additional arguments to work properly. For example, Luakit will close on Mutt exit. You need to fork it to background, using the  parameter:

 COMMAND luakit -n %s 2>/dev/null

The  is to make it quiet, i.e. to prevent useless message printing where you do not want them to.

## Viewing HTML
It is possible to pass the HTML body to an external HTML program and then dump it, keeping email viewing uniform and unobtrusive. Three programs are described here: ,  and  (make sure the selected package is installed).

If  does not exist you will need to create it and save the following to it.

 text/html; lynx -assume_charset=%{charset} -display_charset=utf-8 -collapse_br_tags -dump %s; nametemplate=%s.html; copiousoutput

or, in case of w3m,

 text/html; w3m -I %{charset} -T text/html; copiousoutput;

or, in case of elinks,

 text/html; elinks -dump; copiousoutput;

or, in case of elinks (with color support),

 text/html; elinks -dump -dump-color-mode 1; copiousoutput;

Edit  and add the following,

 set mailcap_path   = ~/.mutt/mailcap

To automatically open HTML messages in lynx, w3m or elinks add this additional line to the muttrc:

 auto_view text/html

The beauty of this is, instead of seeing an HTML body as source or being opened by a separate program, in this case lynx, you see the formatted content directly, and any URL links within the email can be displayed with , assuming you have  installed and configured as above.

If you receive many emails with multiple or alternate encodings, Mutt may default to treating every email as HTML. To avoid this, add the following variable to your ~/.muttrc to have Mutt default to text when available and use w3m/lynx only when no text version is available in the email:

 alternative_order text/plain text/html

Some HTML mails may not display correctly in a text-based web browser. As a fallback solution, you can bind a key to open a graphical browser in such cases.
The following macro will open the HTML mail selected from the attachment view in the web browser defined in the environment. (Feel free to adapt the  folder).

 macro attach 'V' "iconv -c --to-code=UTF8 > ~/.cache/mutt/mail.html$BROWSER ~/.cache/mutt/mail.html"

If  is , then set  to  in  as described in to ensure non-ASCII characters in the HTML page are displayed correctly.

To convert HTML emails to sanitised markdown and view the resulting output using mutt's internal pager, install  and use the following mailcap entry:

 text/html; html2text --images-to-alt --ignore-tables --decode-errors=ignore %s; copiousoutput

## Viewing pdf files
You also can view attached pdf files with similar configuration to the mailcap HTML view.

For example, to open with , add the following line to the mailcap file:
 application/pdf; zathura %s;

Then in the attachment section type  on the pdf file and a instance of zathura will open the file.

This could be done with other pdf viewers.

## Filtering the message view
You can restrict the view to e-mails matching a pattern and specific properties with the  command (default shortcut: ).

To view all e-mails containing "foo" in the header, simply write "foo" and you are done. To remove the filter, use the "all" keyword.

To view all flagged messages, use

 ~F

To view all unread messages that are either of size ≥1MB or from johndoe, use

 ~U (~z 1M- | ~f johndoe)

All possible patterns are listed in the [http://www.mutt.org/doc/manual/#patterns official manual.

## Conversation grouping
The default sort order is by date. Use the  command (default key: ) to change the sorting option. You can group e-mails by conversation/thread, in which case you can define how to sort threads and how to sort within a thread.

In the following example, threads are sorted according to the date of their last e-mail.

## Configuring editors to work with mutt
## vim
*To limit the width of text to 72 characters, edit your .vimrc file and add:

 au BufRead /tmp/mutt-* set tw=72

*Another choice is to use Vim's mail filetype plugin to enable other mail-centric options besides 72 character width. Edit , creating it if unpresent, and add:

*To set a different tmp directory, e.g. ~/.tmp, add a line to your muttrc as follows:

 set tmpdir="~/.tmp"

*To reformat a modified text see the Vim context help

 :h 10.7

## GNU nano
nano is another nice console editor to use with Mutt.

To limit the width of text to 72 characters, edit your .nanorc file and add:

  set fill 72
  set breaklonglines

If you do not want to limit the width of text globally, you can pass the column number as an argument to the hard-wrap option in your muttrc file, e.g.:

  set editor="nano -r 72 -b"

Also, in muttrc file, you can specify the line to start editing so that you will skip the mail header:

  set editor="nano +7"

## Emacs
Emacs has a mail and a message major mode. To switch to mail-mode automatically when Emacs is called from Mutt, you can add the following to your :

If you usually run Emacs daemon, you may want Mutt to connect to it. Add this to your :

## Display settings
## Colors
Append the contents of  to your .muttrc file, or copy and source it. Then adjust to your liking.

The actual color each of these settings will produce depends on the colors set in your ~/.Xresources file.

Alternatively, you can source any file you want containing colors (and thus act as a theme file). See for a theme example.

## Index Format
Here follows a quick example to put in your  to customize the Index Format, i.e. the columns displayed in the folder view.

See the [http://www.mutt.org/doc/manual/#index-format Mutt Reference,  and  for more details.

## Display recipient instead of sender in "Sent" folder view
By default Mutt uses the  format string in the  variable, which will display:

* "To ", if an address in the "To:" or "Cc:" header field matches an address defined by the user's  command.
* Otherwise it displays the author name, or recipient name if the message is from you.

If you use multiple email addresses in the same mailbox, make sure to configure the alternates variable, so that Mutt knows which messages were from you.

## Variable column width
If you resize the window, the subject might get truncated while there is still unused space left for some fields, like for the sender.
You can get the maximum number of columns supported by your terminal (i.e. the width) using a shell call to . With this value, you can set a percentage of the width to fields like Sender and Subject.

Example using the above folder-hook and a sidebar width of 24:

{{hc|muttrc|
## From field gets 30% of remaining space, Subject gets 70%.
## Remaining space is the total width minus the other fields (35), minus the sidebar (24)
set my_index_format_pre='set my_col_from = `echo $((30 * ($(tput cols)-35-24) / 100))`; set my_col_subject = `echo $((70 * ($(tput cols)-35-24) / 100))`; set index_format="%2C | %Z %-$my_col_from.${my_col_from}'
set my_index_format_post=' (%-4.4c) %?M? ?%-$my_col_subject.${my_col_subject}s"'

folder-hook .*[sSent.* "$my_index_format_pre"t"$my_index_format_post"
folder-hook ! .*"$my_index_format_pre"F"$my_index_format_post"
}}

We must set the variables  and  from within the hooks. Otherwise, the column values will not get re-computed.

We can add a binding to force re-computing the index format without changing folder:

## Sidebar
Example settings for a sidebar are in , including keybindings. Copy, edit, and source that file in your mutt configuration file. Be sure to change .

Append the following in order to toggle the sidebar visibility:

Note that with the  option, folders appear in the order they were set to   if you do not use the  option.

## Display the index above the pager view
Set the following variable in your :

 set pager_index_lines=10

## Contact management
## Address aliases
Aliases is the way Mutt manages contacts. An alias is nickname [longname .

* The nickname is what you will type in Mutt to get your contact address. One word only, and should be easy to remember.
* The longname is optional. It may be several words.
* An ' must be in a valid form (i.e. with an ).

It is quite simple indeed. Add this to :

Explanation:

*  is the file where the information is getting stored when you add an alias from within Mutt.
*  specifies which field to use to sort the alias list when displayed in Mutt. Possible values: alias, address.
*  if set to yes mutt will display the "personal" name from your aliases in the index menu if it finds an alias that matches the message's sender.
*  tells Mutt to read aliases on startup. Needed for auto-completion.

Now all you have to do when prompted  is writing the alias instead of the full address. The beauty of it is that you can auto-complete the alias using .
Autocompleting a wrong or an empty string will display the full list. You can select the alias as usual, or by typing its index number.

There are two ways to create aliases:

* From Mutt, press  when an e-mail of the targetted person if selected.
* Edit the alias_file manually. The syntax is really simple:

## Abook
 is a stand-alone program dedicated to contact management. It uses a very simple text-based interface and contacts are stored in a plain text, human-readable database. Besides the desired contact properties are extensible (birthday, address, fax, and so on).

Abook is specifically designed to be interfaced with Mutt, so that it can serve as a full, more featured replacement of Mutt internal aliases. If you want to use Abook instead of aliases, remove the aliases configuration in  and add this:

See  and  for more details and a full configuration sample.

## Goobook
Goobook allows you to search your Google contacts from the command line or from within Mutt and can be installed with the  or  packages.

Before using goobook you must configure .  To generate the default template:

 $ goobook config-template > ~/.goobookrc

See  for configuration options. At a minimum, you will need to enter your email and password.

In order to authenticate with Google, you must generate a Client ID and Client secret. See for details.

If you want to use Goobook instead of aliases, remove any alias configuration in  and add:

When composing an email message within mutt,  will now search your Google contacts.  While viewing messages  will add the sender to Google contacts.

## Khard
 is a command-line addressbook that uses locally-stored carddav address book entries. You can use  or its successor,  to sync those with CardDAV servers.

The integration in mutt is similar to abook, see [https://khard.readthedocs.io/en/latest/scripting.html#mutt khard documentation.

## Manage multiple sender accounts
If you use multiple sender accounts, you can automatically associate a specific sender account with a recipient.  scans sent emails for the most recent "From" details associated with specific recipients, saving these in a file for mutt to source. The next time you email this recipient, mutt will automatically invoke a send-hook with the same email address and real name that you used previously. See mutt-vid's homepage for more details.

## Request IMAP mail retrieval manually
If you do not want to wait for the next automatic IMAP fetching (or if you did not enable it), you might want to fetch mails manually. There is a mutt command  for that. Alternatively, you could bind it to a key:

 bind index "^" imap-fetch-mail

## Avoiding slow index on large (IMAP) folders due to coloring
Index highlighting by regex is nice, but can lead to slow folder viewing if your regex checks the body of the message.

Use folder-hook for only highlighting in, for example, the inbox (if you manage to empty your mailbox efficiently):

 folder-hook . 'uncolor index "~b \"Hi Joe\" ~R !~T !~F !~p !~P"'
 folder-hook ""!"" 'color index brightyellow black "~b \"Hi Joe\" ~N !~T !~F !~p !~P"'

## Speed up folders switch
Add this to your :

## Archive treated e-mails
When you read an e-mail, you have four choices: Answer it, Flag it, Archive it or Delete it. If you have this in mind, you can keep your inbox slim and fit with this macro (set up for Gmail):

 macro index \' "~R !~D !~F\
 +" \
 "Archive"

## Migrating mails from one computer to another
In case you are transfering your mails to a new machine (copy&paste), you probably need to delete the header cache (a file or folder like  if you followed the above configuration)  to make Mutt able to read your migrated E-Mails. Otherwise Mutt may freeze.

Note that if you had a folder created for you header cache, all mailboxes will have their own cache file, so you can delete caches individually without having to remove everything.

## Default folder for saving attachments
By default Mutt will save attachments to the folder it was started from. If you want to always set the default destination to , you can create the following alias, which launches Mutt in this folder:

 alias mutt='cd ~/attachments && mutt'

If you are using bash, you can use  and  to restore the directory state after mutt exits.

 alias mutt='pushd ~/attachments; mutt; popd'

## Pager behavior
Show context lines when going to next page:

 set pager_context=3

Stop at the end instead of displaying next mail:

 set pager_stop=yes

## Fast reply
By default Mutt will ask to confirm the recipient and the subject when you reply to an e-mail. It will also ask if you want to include the original mail in your answer. If you assume you will always stick to the default values, you can set up Mutt to skip these questions:

You can still edit the recipient and the subject before sending.

## Ignore own e-mail addresses from group-reply
Mutt will include your e-mail address(es) in the recipient list when you group-reply to a mail you were CC'ed. You can ask Mutt to ignore some addresses with:

 alternates mail1@server1|mail2@server2|...

## IMAP message cache
When using the built-in IMAP support, e-mails are fetched in memory by default. Retrieving a big e-mail several times will download it from your IMAP server that many times.

Alternatively, you can ask Mutt to store all fetched messages on disk:

(The folder must exist.) This will make any future retrieval instantaneous, even with big attachments.

If you want to purge the cache from its oldest e-mails exceeding a limit of, say, 50MB, you can use a script like the following:

{{hc|~/.mutt/purgecache.sh|
#!/bin/sh

## In KB.
CACHE_LIMIT=51200

cd "$1" 2>/dev/null
[ $? -ne 0  && exit

[ $(du -s . | cut -f1 -d'	') -lt $CACHE_LIMIT ] && exit
while IFS= read -r i; do
	rm "$i"
	[ $(du -s . | cut -f1 -d'	') -lt $CACHE_LIMIT ] && exit
done  /dev/null &; nametemplate=%s.html
 application/*; xdg-open %s &> /dev/null &;
 image/*; xdg-open %s &> /dev/null &;

 is used to prevent any error or message from cluttering the mutt terminal window. And  is used because chromium refuse to render local files without .html extension as HTML.

## Troubleshooting
## Backspace does not work in Mutt
This is a common problem with some xterm-like terminals. Two solutions:

* Either rebind the key in

 bind index,pager ^? previous-line

Note that  is one single character representing backspace in caret notation. To type in Emacs, use , in Vim .

* Or fix your terminal:

 $ infocmp > termbs.src

Edit  and change  to , then:

 $ tic -x termbs.src

## The change-folder function always prompt for the same mailbox
This is not a bug, this is actually an intended behaviour. See the multiple accounts section for a workaround.

## I cannot change folder when using Mutt read-only (Mutt -R)
This is certainly because you are using macros like this one:

 macro index,pager  'source ~/.mutt/personal!'

This macro tells Mutt to sync (which is a write operation) before switching.

Either use the sidebar or set another macro:

 macro index,pager  'source ~/.mutt/personal!'

## Error sending message, child exited 127 (Exec error.).
This is an SMTP error. It means that mutt does not know how to send the message. You can either try installing sendmail and see if that solves your issue, or you can set the  smtp_url variable. If you use gmail, you can add the following to your muttrc to tell mutt to use gmails smtp server.

 set smtp_url=smtps://$imap_user:$imap_pass@smtp.gmail.com

Take note of the smtps protocol, it is important. This should solve the problem.

## Character encoding problems
If you are having problems with character encoding, first read this section in the Mutt wiki.

If Chinese text is still garbled, it may help to decode with GBK even when GB2312 is specified in the header. You can do this with  by adding the following to your  file:

 text/plain; iconv -f gbk -t utf-8 %s; test=echo "%{charset}" | grep -ic "gb2312"; copiousoutput;

and enabling it by adding a line to your :

 auto_view text/plain

For HTML emails, you can edit the relevant line of your mailcap by replacing {{ic|%{charset}}} with {{ic|$(echo %{charset} | sed s/gb2312/gbk/I)}}, for example:

 text/html; w3m -dump -I $(echo %{charset} | sed s/gb2312/gbk/I) %s; nametemplate=%s.html; copiousoutput

## Unable to login with GMail
Gmail disables access from applications it considers less secure, including . You can enable access by following the instructions here

## Not possible to open too long URLs with urlview
Too long URLs are not parsed correctly, because urlview does not decode text (see You can let mutt decode the e-mails instead. Replace the line for opening urlview with the following code:

 macro index \cb "\
 :set my_tmp_pipe_decode=\$pipe_decode\n\
 :set pipe_decode\n\
 |urlview\n\
 :set pipe_decode=\$my_tmp_pipe_decode\n\
 :unset my_tmp_pipe_decode\n" \
 'call urlview to extract URLs out of a message'

Another option is to use [https://github.com/firecat53/urlscan urlscan instead, which gives a text user interface to select the URL and can deal with much stranger text formats.

## Documentation
Newcomers may find it quite hard to find help for Mutt. Actually most of the topics are covered in the official documentation. We urge you to read it.

* The official manual. The stock  package for Arch Linux also installs the HTML and plain text manual at .
* The  and  man pages.
