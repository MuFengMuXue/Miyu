# Notmuch

Notmuch is a mail indexer. Essentially, is a very thin front end on top of xapian.
Much like Sup, it focuses on one thing: indexing your email messages. Notmuch can be used as an email reader, or simply as an indexer and search tool for other MUAs, like mutt.

## Overview
Notmuch is written in C and an order of magnitude faster than sup-mail.
Notmuch can be terminated during the indexing process, on the next run it will continue where it left off.
Also like sup-mail, it does not provide a way to permanently delete unwanted email messages (however, see #Permanently delete emails).
It does not fetch or send mails, nor does it store your email addresses, you will need to use programs like OfflineIMAP, msmtp and abook for those tasks.

Install the  package. It provides python, vim, and emacs bindings.

## First time Usage
After installation, you enter an interactive setup by running:
 notmuch setup
The program prompts you for the location of your maildir and your primary and secondary email addresses. You can also edit the configuration file directly which is created by default at .

Subsequent re-indexing of the mail directories is done with:
 notmuch new

## Frontends
There are a range of ways to use notmuch, including CLI, or with one of the Unix :

## Emacs
The default frontend for notmuch is Emacs. It is developed by the same people that develop notmuch.

## Vim
There is a Vim interface available and included in the  package. To start it, type:
 vim -c NotMuch

## alot
alot is a standalone CLI interface for notmuch, written in Python. It is available as  and .

Alot uses mailcap for handling different kinds of files. This currently includes HTML mails, which means that you need to configure a  file in order to view HTML mails. As minimum, put this line into your :

 text/html; w3m -dump -o -document_charset=%{charset} %s; nametemplate=%s.html; copiousoutput

This uses , some other text based clients such as  or  can be used instead, although their arguments might differ.

More file handlers can be configured of course.

## bower
bower is another CLI interface, this one is written in Mercury. It is available as .

## Neomutt
Neomutt - Another mutt fork which includes many feature patches, among them the Notmuch integration patch. Install the  or the  package.

## aerc
aerc is a terminal-based full-featured (threading, MIME multipart emails, flags, tags, ...) MUA written in Go, supporting many backends including Notmuch. It is available as .

## astroid
Astroid is a graphical MUA and interface to notmuch written using C++ and GTK. It can be installed with  or . The GUI is designed to be very fast, preview HTML and attachments, be navigable by keyboard. It is extensively configurable and you use your favorite editor either embedded or launch it externally. Check out the Tour to see how astroid can be used and for a description of the complete setup, or check out the README for more information.

## Integrating with mutt
If you use mutt as your MUA, then notmuch is an excellent complementary tool to index and search your mail. The  package provides a script to integrate notmuch with mutt.

After installing the  package and configuring notmuch, the only thing left before using notmuch to search from mutt is adding keybindings to call the  perl script from mutt. Adding the following to your  is what is recommended in notmuch contrib source:

 macro index  \
 "set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key\
 notmuch-mutt -r --prompt search\
 `echo ${XDG_CACHE_HOME:-$HOME/.cache}/notmuch/mutt/results`\
 set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key" \
 "notmuch: search mail"

 macro index  \
 "set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key\
 notmuch-mutt -r thread\
 `echo ${XDG_CACHE_HOME:-$HOME/.cache}/notmuch/mutt/results`\
 set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key" \
 "notmuch: reconstruct thread"

 macro index  \
 "set my_old_pipe_decode=\$pipe_decode my_old_wait_key=\$wait_key nopipe_decode nowait_key\
 notmuch-mutt tag -- -inbox\
 set pipe_decode=\$my_old_pipe_decode wait_key=\$my_old_wait_key" \
 "notmuch: remove message from inbox"

The above uses  to search your inbox using notmuch,  to create threads from search results, and  to tag search results.

## Integrating with NeoMutt
If you use , the  package is not required. Instead, create a  with some basic (virtual) mailboxes. A virtual mailbox is not an actual folder, but the result of a notmuch query for a specific tag:

Next, make mutt aware of your virtual mailboxes by enabling virtual spoolfile and sourcing the latter:

At this point, mutt will still list your mailboxes as empty, because your mails are not yet tagged and thus, notmuch querys are empty. To fill your virtual mailboxes, you need to initially tag the messages in your maildir. A very simple approach is to create a shell script like the following:

Make the shell script executable and run it:
 ~/.scripts/notmuch-hook.sh
For the above example to work, make sure that notmuch tags new messages as 'new':

Finally, your hook script needs to rerun on new mail arrival. If you use  to sync IMAP to a local maildir, create a post sync hook:

Some useful key bindings:

## Permanently delete emails
One choice is to maintain a tag of emails you wish to remove from your disk, for example, "killed". Then, you can combine the search for the tags with  to delete them permanently:
 notmuch search --output=files --format=text0 tag:killed | xargs -r0 rm
 notmuch new
By placing this into the  hook for notmuch you can make sure you delete files before updating the database.
