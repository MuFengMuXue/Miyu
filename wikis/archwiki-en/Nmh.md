# Nmh

nmh (new message handler), is a powerful electronic mail handling system. Following the Unix Philosophy, nmh is made up by a collection of simple programs each of which has a single purpose. This architecture allows the user to intersperse nmh with other commands at the shell prompt and to write scripts tailored to their needs.

## Installing
Install  or .

Optionally install a utility to handle IMAP or POP, for example ,  or .

Also optionally install  or another utility for sending mail.

## Configuring
nmh is extensively configurable in a variety of ways. The primary of these is the  file.

The syntax for  is unusual. For example, nmh will refuse to run if there are blank lines in the file. Read the  page for more.

By default, nmh uses  as your mail folder. To change this, set :

  Path: path/to/mail/folder

Set inbox (relative to Path):

  Inbox: inbox

Also by default, nmh populates the mail folder with the  command, which incorporates mail from the user's mail drop ().

If you have a non-standard mail drop path, you can set an environment variable , or set MailDrop in :

  MailDrop: /path/to/mail-drop

or set inc:

  inc: -file /path/to/mail-drop

Nmh is also capable of retrieving mail via POP. A basic POP setup (see  for more):

  inc: -host example.com -user username -sasl

## Usage
To become familiar with basic nmh usage, learn and practice the following commands:

{| class="wikitable"
|-
!width="75" |Command
!Description
|-
|inc
|Incorporate new mail.
|-
|scan
|Scan the contents of the current folder.
|-
|folder/folders
|Change the current folder or list folders and their contents.
|-
|show
|Display messages.
|-
|comp
|Compose a new message.
|-
|repl
|Reply to a message.
|-
|refile
|Move a message to another folder.
|}

## Frontends
While nmh is fully usable from the command-line, several console-based and graphical user interfaces exist. Also, some common mail tools interact smoothly with the mh format.

## MH-specific Frontends
* MH-V, a console interface to mh/nmh with vi- keybindings.
* MH-E, a console interface to mh/nmh with Emacs keybindings.
* exmh, a TK-based mh GUI.

## MH-compatible Frontends
* Popular MUA mutt understands mh format. (Use  in your muttrc.)
* Full-text mail indexer and search utility mairix can read and write in mh format. (Use  and  in .mairixrc)
