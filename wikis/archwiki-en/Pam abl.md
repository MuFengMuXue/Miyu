# Pam abl

pam_abl provides another layer of security against brute-force SSH password guessing.  It allows you to set a maximum number of unsuccessful login attempts within a given time period, after which a host and/or user is blacklisted.  Once a host/user is blacklisted, all authentication attempts will fail even if the correct password is given.  Hosts/users which stop attempting to login for a specified period of time will be removed from the blacklist.

## Installation
Install the  package.

## Configuration
## Add pam_abl to the PAM auth stack
Open  as root in your editor of choice. Add the following line above all other lines:

Assuming you have not made any other modifications, your  should now look like this:

## Edit pam_abl.conf
Edit  to customize the rules and other settings.

See  for details.

## Managing the blacklist databases
## Check blacklisted hosts/users
As root, simply run:
 # pam_abl

## Manually remove a host or user from the blacklist
As root, simply run:
 # pam_abl -w -U
or
 # pam_abl -w -H
Using * as a wildcard to match multiple hosts/users is allowed in both of the above commands.

## Manually add a host or user to the blacklist
As root, simply run:
 # pam_abl -f -U
or
 # pam_abl -f -H

## Purging old users/hosts entries
As pam_abl does not run as a daemon, it performs "lazy purging" of the blacklist.  In other words, it does not remove old users/hosts entries from the blacklist until an authentication attempt occurs. This does not affect functionality, although it will frequently cause extra failures to show up when checking blacklisted hosts/users. To force a purge, run:
 # pam_abl -p

## Other pam_abl commands
Like virtually all linux utilities, a manpage is available to see all options:
 $ man pam_abl

## Known issues
As of current version (1.0), pam_abl has a problem that can affect its ability to blacklist under specific conditions.

Due to the way sshd operates and the way pam modules are passed information, failure of a given attempt is not logged until either a second attempt is made or the connection is closed. This means that long as the attacker only makes one attempt per connection, and never closes any connections, no failures are ever logged.

In practice, the sshd_config settings "MaxStartups" (default 10) and to a lesser degree "LoginGraceTime" (default 120s) limit the viability of this approach, but it still could be used to squeeze out more attempts then you specify.

In the meantime, the workaround is to set "MaxAuthTries" to 1 (or expect that an additional "MaxStartups" number of attempts could be made above and beyond what you specify in your pam_abl config).
