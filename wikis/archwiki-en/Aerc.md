# Aerc

aerc is a terminal-based e-mail client with Vim-style keybindings and an ex-command system. It uses an embedded teminal which allows to use any terminal-editor as an embedded component to compose e-mails. aerc comes with inbuilt support for IMAP and SMTP, but also supports Maildir and Notmuch. While aerc provides a simple wizard to set up an e-mail account, the complete configuration is handled in text files within .

aerc is written in Go and uses the Tcell package for the terminal UI.

## Installation
Install the  package.

## Tips and tricks
## Khard as addressbook provider
 can be configured as an address book provider=== Send from an alias ===

In the section corresponding to the account having multiple email addresses (at least one alias) of the  file (refer to ), add the following line:

This will read the  address from the header to choose the alias to use.

## Display Notmuch tags
When using Notmuch as a backend in the  file (refer to ), one may display the Notmuch's tags inside the mail list by adding the following inside the  [https://lists.sr.ht/~rjarry/aerc-discuss/%3CD74TRLOLNC1E.98VZHB938D7@etriadi.com%3E#%3CD74U9GZ865N8.1GSR1W8LVIVMS@jasoncarloscox.com%3E:

## Save sent mails
If you want to save every sent mail in a specific directory in your mailbox, put the following line into .

To save every mail in a mail box named "SENT":

 copy-to = SENT

## Officials
* The official aerc website
* The aerc repository
* The aerc Wiki
* The aerc mailing lists

## Third-party posts
* Email client (aerc) - Will Webberley
