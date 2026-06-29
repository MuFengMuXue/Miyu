# SSSD

SSSD is a system daemon. Its primary function is to provide access to identity and authentication remote resource through a common framework that can provide caching and offline support to the system. It provides PAM and NSS modules, and in the future will D-BUS based interfaces for extended user information. It provides also a better database to store local users as well as extended user data.

## Installation
Install the  package.

## Configuration
## LDAP
See LDAP authentication#SSSD configuration.

## PAM proxy
If you would like software running as a non-root user to be able to use  for authentication, you can run SSSD as a PAM proxy for this by creating the following files.

Now specify  as the PAM service name in your software's configuration.

## Run SSSD as root
SSSD 2.10 and above runs as a non-root user by default, but here it needs to run as root in order to access . Override the unit  exactly like this:

{{bc|1=Environment=DEBUG_LOGGER=--logger=files
EnvironmentFile=-/etc/sysconfig/sssd
ExecStartPre=+-/bin/chown -f root:sssd /etc/sssd
ExecStartPre=+-/bin/chown -f root:sssd /etc/sssd/sssd.conf
ExecStartPre=+-/bin/chown -f -R root:sssd /etc/sssd/conf.d
ExecStartPre=+-/bin/chown -f -R root:sssd /etc/sssd/pki
ExecStartPre=+-/bin/sh -c "/bin/chown -f root:sssd /var/lib/sss/db/*.ldb"
ExecStartPre=+-/bin/sh -c "/bin/chown -f root:sssd /var/lib/sss/gpo_cache/*"
ExecStartPre=+-/bin/sh -c "/bin/chown -f root:sssd /var/log/sssd/*.log"
ExecStart=/usr/bin/sssd -i ${DEBUG_LOGGER}
Type=notify
NotifyAccess=main
Restart=on-abnormal
CapabilityBoundingSet= CAP_CHOWN CAP_DAC_OVERRIDE CAP_SETGID CAP_SETUID CAP_DAC_READ_SEARCH
#SecureBits=noroot noroot-locked
User=root
Group=sssd
# If service configured to be run under "root", uncomment "SupplementaryGroups"
#SupplementaryGroups=sssd }}

Note that SSSD wants its files like  and  to have the same owner as the user running SSSD, so you have to  those files to be root-owned. Additionally, delete and add  to  in  to prevent systemd-tmpfiles from reverting the permissions of SSSD files.

Finally, enable/start .

## Tips and tricks
## Prevent logins with empty passwords
If using SSSD as a PAM proxy, by default it allows logging into accounts with empty passwords, which could be undesirable. To fix this, remove  from :

Then add that file to  in .
