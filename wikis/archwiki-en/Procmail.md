# Procmail

Procmail is a program for filtering, sorting and storing email. It can be used both on mail clients and mail servers.
It can be used to filter out spam, checking for viruses, to send automatic replies, etc.

The goal of this article is to teach the configuration of procmail. This article assumes you already have either a email client (Mutt, nmh, etc) or a mail server (Sendmail, Postfix, etc) working, that can use (or requires) procmail. It also assumes you have at least basic knowledge on regular expressions. This article will give only a minimal explanation, for a complete manual, check the .

## Installation
Install the package .

## Configuration
The configuration is going to be saved on  if this is the configuration for an email client, or on  if is going to be used by an email server.

The configuration is composed of two sections; assignments and recipes.

## Assignments
The assignments section provides variables for procmail

## Recipes
Recipes are the main section, they are the actual filters that do the actions.
Recipes have the following format:

The conditions are extended regular expressions, with some few extra options. Conditions always start with an asterisk.

The action can be only a mailbox name, or an external program.

## Flags and lockfile
For basic recipes, you do not need any flags. But they can be necessary if your script calls an external command.
Here is a list of some of the most used flags:
* f Consider the pipe as a filter.
* w Wait for the filter or program to finish and check its exitcode (normally ignored); if the filter is unsuccessful, then the text will not have been filtered.
Using a  after the  is to use a lockfile. A lockfile is necessary to prevent problems if 2 or more instances of procmail are working at the same time (that may happen if 2 or more email arrive almost at the same moment).

You can set the name of the lockfile after the

## Conditions
A condition starts with an asterisk, following an extended regexp, like this one:

## Action
An action can be something as simple as

in that case, the mail that complies with the condition will be saved in the  inbox.

An action can also start with a pipe, which means the message is going to be passed to the standard input of the command following the pipe. For example:
 | /usr/bin/vendor_perl/spamc
By default, once a recipe's action is done, the processing is over.

If the f flag was used, the command can alter the message and keep reading recipes. In this example, the SpamAssassin command will add headers to the mail, with its spam status level, which later can be used by another recipe to block it, or store it on a different mailbox.

## Tips and tricks
## SpamAssassin
Here is an example using SpamAssassin to block spam. You should already have SpamAssassin installed and working.

## ClamAV
An example using the ClamAV antivirus.

{{bc|
# We make sure its going to use the sh shell. Mostly needed for mail-only account that have /usr/bin/nologin as shell
SHELL=/bin/sh

# We will scan the mail with clam using the standard input, and saving the result on the AV_REPORT variable
AV_REPORT=`clamdscan --stdout --no-summary - |sed 's/^stream: //'`

# We check if the word FOUND was in the result and save "Yes" or "No" according to that
VIRUS=`echo $AV_REPORT|sed '/FOUND/ { s/.*/Yes/; q  };  /FOUND/  !s/.*/No/'`

# formail is a filter that can alter a mail message, while keeping the correct format. We use it here to add/alter a header called
# X-Virus with either value Yes or No
:0fw
| formail -i "X-Virus: $VIRUS"

# And if we just added "X-Virus: Yes", we will also add another header with the scan result, and alter the subject, again, with the scan result.
# Since we are using the f flag, the mail is going to be delivered anyway.
:0fw
* ^X-Virus: Yes
| formail -i "X-Virus-Report: $AV_REPORT" -i "Subject: $AV_REPORT"
}}

## Filtering mail to a different mailbox
If a coworker keeps using forward to send you jokes and other non serious stuff, but at the same time, writes you work related mails, you could save the forwarded mails (most likely not-work-related mails) on a different mailbox.

## Postfix Piping
To pipe from postfix open  then add

After reloading , email will be send to procmail for filtering and delivery.

## Exim
To use with Exim, invoke  in the  file, or edit  to use it directly as a local delivery agent:

This was tested on Arch's standard Exim 4.94-2 package.

## Sending to Dovecot
To forward to dovecot change the following assignments

The deliver will be the first attempt then Default will be the back up.

The advantage is the dovecot will have its databases up to date at all times.

Then to spam mail and deliver for example

Further information can be found here https://wiki2.dovecot.org/procmail
