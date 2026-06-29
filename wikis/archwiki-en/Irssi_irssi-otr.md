# Irssi/irssi-otr

The irssi-otr module adds
Off-the-Record Messaging support to irssi.

## Installing
irssi-otr is now part of .

## Usage
See the
README.

## Loading the module on startup
If you are tired of typing  you can put the following
in your :

 LOAD otr

## Stripping HTML
If you are using irssi-otr with BitlBee you will notice
that some clients send you HTML formatted messages.  Normally BitlBee
automatically strips the HTML formatting, but since the messages are
encrypted this does not work anymore.  Nevertheless you can achieve
the same by stripping the HTML with regular expressions using the
Trigger script.  Just make
sure you load the script before the otr module.  You can either do this
manually or again make your  look like this:

 SCRIPT LOAD trigger.pl
 LOAD otr

Also make sure that  is not in
 since the files from this directory
are loaded after .

Since it is not possible to perfectly match HTML code with regular
expressions we will take a somewhat conservative approach.  We will only
strip HTML tags we explicitly specified from PRIVMSGS from the BitlBee
network, where we assume you added you server.

You can  the following lines or copy them to
.

You can even make HTML line breaks look like multiple messages:

 -privmsgs -nocase -tags 'BitlBee' -regexp '(\s*&lt;br&gt;\s*)+' -replace '\n�8/�g �e'

Where  is the non-printable character .  In vi(m)
you can get it by pressing  in insert mode.
If your are using a theme different than the default one you probably
have to adapt the replacing string to match color and indentation.

And finally we convert some escaped HTML characters:

 -privmsgs -nocase -tags 'BitlBee' -regexp '&amp;amp;' -replace '&'
 -privmsgs -nocase -tags 'BitlBee' -regexp '&amp;gt;' -replace '>'
 -privmsgs -nocase -tags 'BitlBee' -regexp '&amp;lt;' -replace '<'
 -privmsgs -nocase -tags 'BitlBee' -regexp '&amp;quot;' -replace '"'

These are just some basic replaces, just extend them if you need more.
