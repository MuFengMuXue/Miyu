# Fdm

fdm (fetch and deliver mail), is a simple program for delivering and filtering mail. Comparing it to other same-purposed applications shows that it has similarities with Mutt's very focused design principles.

## Installation
Install the  package.

## Configuration
fdm can be configured through a configuration file. Default is , or  if that does not exist.

For full details refer to the manual pages ,  and the .

## mbox
Alpine uses the mbox format, so we need to set up some files that we will be editing:

 $ cd
 $ mkdir mail
 $ touch mail/INBOX .fdm.conf
 $ chmod 600 .fdm.conf mail/INBOX

## maildir
Mutt prefers a capitalized mail directory, and is able to use the maildir format. If you plan on using Mutt do the following setup:

 $ cd
 $ touch .fdm.conf; chmod 600 .fdm.conf
 $ mkdir -p Mail/INBOX/{new,cur,tmp}

## An example configuration
Edit , and add your email accounts and basic filter rules. Use mbox or maildir, but not both.

This will collect the mail from the listed accounts and deliver it to the INBOX folder that we made. Refer to the  man page for specifics on how to connect to other types of mail servers (POP3 for example).

## Password Management
Passwords for email accounts can be stored as plain text in the config file or can be requested from a password manager or key-ring via a shell command, in the format of

## Using a password manager
Here is an example using pass:

 account "foo" imaps server "imap.example.com"
     user "foo@example.com" pass $(pass foo-email-entry | head -1)

## OAuth2 authentication, gmail
fdm can use OAuth2 access tokens that are required for GMail, but it lacks the ability to renew and/or authorize OAuth2 credentials. A comprehensive solution is using the oama utility which provides IMAP/SMTP clients with the capabilities of renewal and authorization of OAuth2 credentials. After the initial setup, access token renewal happens automatically in the background transparent to the user.

Install the  package and configure fdm:

 account "foo" imaps server "imap.gmail.com"
     user "foo@gmail.com"
     pass $(oama access foo@gmail.com)
     oauthbearer

## Running from cron
While the above examples work fine for interactive use, using them from a cron job is a bit more involved since some of the programs invoked might expect certain environments. One can work around that by using wrapper scripts and exporting the needed environment variables.

Here are a few tricks for such scripts:

 ...
 # for pass
 export PASSWORD_STORE_DIR=~/.local/var/password-store
 ...
 # when using gnome's keyring
 # secret-tool can't live without these two envvars
 # so we fake them for the case this script runs in a cron job
 export DISPLAY=${DISPLAY:-:0}
 export DBUS_SESSION_BUS_ADDRESS=${DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/$UID/bus}
 ...

## Testing
Once you have this setup to your satisfaction, attempt to collect your mail by manually running fdm.

 $ fdm -kv fetch

This will keep your mail untouched on the server in case there are errors. Look over the output to make sure everything worked as planned. Open your favorite mail reader (MUA) and make sure that you can read the mail that was just delivered.

## Extended usage
## Additional filtering
If you want to have mail from a certain account go to a specific mailbox, you could add the following lines to your  file. From the configuration file above, if you wanted to filter the mail from  into its own folder , you would add this below the existing "action" line:

 action bar-deliver mbox "%h/mail/bar-mail"

Change the  to  if needed, also make sure the path is correct.

To activate the new action, add this before the existing "match" line:

 match account bar action bar-deliver

Then all mail to  will be put into the  mail folder.

## Automation
Since fdm does not run as a daemon, timed mail fetching is left to job schedulers like cron or systemd timers. This section will show implementations for both.

## Cron
Fetch and sort mail from all accounts every 15 minutes, appending a log all matches to a local file:

## systemd timer
Setup the fdm service for the local user to fetch and sort mail from all accounts:

{{hc|${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user/fdm.service|
Description=Fetch mail using fdm
After=network.target network-online.target dbus.socket
Documentation=man:fdm(1)

[Service
Type=oneshot
ExecStart=/usr/bin/fdm fetch
}}

Then setup the timer to run the service every 15 minutes:

{{hc|${XDG_CONFIG_HOME:-$HOME/.config}/systemd/user/fdm.timer|
Description=Fetch mail using fdm

[Timer
# Uncomment to run the service two minutes after booting
# OnBootSec=2m
OnUnitActiveSec=15m
Persistent=true

Install
WantedBy=timers.target
}}

Finally start/enable the user unit .
