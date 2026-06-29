## Name

pam_systemd_home — Authenticate users and mount home directories via `systemd-homed.service`

## Synopsis

`pam_systemd_home.so`

## Description

**pam_systemd_home** ensures that home directories managed by systemd-homed.service(8) are automatically activated (mounted) on user login, and are deactivated (unmounted) when the last session of the user ends. For such users, it also provides authentication (when per-user disk encryption is used, the disk encryption key is derived from the authentication credential supplied at login time), account management (the JSON user record embedded in the home store contains account details), and implements the updating of the encryption password (which is also used for user authentication).

## Options

The following options are understood:

`suspend=`  
Takes a boolean argument. If true, the home directory of the user will be suspended automatically during system suspend; if false it will remain active. Automatic suspending of the home directory improves security substantially as secret key material is automatically removed from memory before the system is put to sleep and must be re-acquired (through user re-authentication) when coming back from suspend. It is recommended to set this parameter for all PAM applications that have support for automatically re-authenticating via PAM on system resume. If multiple sessions of the same user are open in parallel the user's home directory will be left unsuspended on system suspend as long as at least one of the sessions does not set this parameter to on. Defaults to off.

Note that TTY logins generally do not support re-authentication on system resume. Re-authentication on system resume is primarily a concept implementable in graphical environments, in the form of lock screens brought up automatically when the system goes to sleep. This means that if a user concurrently uses graphical login sessions that implement the required re-authentication mechanism and console logins that do not, the home directory is not locked during suspend, due to the logic explained above. That said, it is possible to set this field for TTY logins too, ignoring the fact that TTY logins actually do not support the re-authentication mechanism. In that case the TTY sessions will appear hung until the user logs in on another virtual terminal (regardless of whether via another TTY session or graphically) which will resume the home directory and unblock the original TTY session. (Do note that lack of screen locking on TTY sessions means even though the TTY session appears hung, keypresses can still be queued into it, and the existing screen contents be read without re-authentication; this limitation is unrelated to the home directory management **pam_systemd_home** and `systemd-homed.service` implement.)

Turning this option on by default is highly recommended for all sessions, but only if the service managing these sessions correctly implements the aforementioned re-authentication. Note that the re-authentication must take place from a component running outside of the user's context, so that it does not require access to the user's home directory for operation. Traditionally, most desktop environments do not implement screen locking this way, and need to be updated accordingly.

This setting may also be controlled via the `$SYSTEMD_HOME_SUSPEND` environment variable (see below), which **pam_systemd_home** reads during initialization and sets for sessions. If both the environment variable is set and the module parameter specified the latter takes precedence.

Added in version 245.

`debug`\[=\]  
Takes an optional boolean argument. If yes or without the argument, the module will log debugging information as it operates.

Added in version 245.

## Home Area Support

Home directories managed by systemd-homed.service(8) support multiple home "areas", which are additional secondary home directories of the user within the primary home directory. An example: at login time if a user "`lennart`" with a home directory of `/home/lennart` specifies "`lennart%versuch1`" as account name during login, then **pam_systemd_home** will execute a login into "`lennart`" but ensure that the `$HOME` variable is set to `/home/lennart/Areas/versuch1` instead of the usual `/home/lennart`.

This is particularly useful when sharing the same home directory between multiple systems (for example between a host and a VM), with the desire to share the home directory to a large degree, but still have separate session configuration in place.

Note that the default area to log into can also be encoded in the user record, and it can be specified among pam_systemd(8) configuration parameters. However, an explicit area specified at login time (via the "`%`" described above) overrides any such default. Also note that simply suffixing an account with "`%`" at login time (i.e. specifying an empty area name) has the effect of ensuring a login into the primary home directory, overriding any default area configuration via the user record or PAM.

Note that not all login mechanisms are compatible with the "`%`" syntax at login time. Most notably ssh(8) is not.

Note that the area directory to log into must exist for the area specification to be respected. If an area is specified during login via the "`%`" logic (or the other mentioned mechanisms) and it does not actually exist the request will be ignored, and the user will log into the primary home directory instead.

Typically, in order to make use of the mechanism set up an area first, like this:

``` programlisting
lennart@zeta$ mkdir -p ~/Areas
lennart@zeta$ cp -av /etc/skel ~/Areas/versuch1
```

This should be enough to log into the newly created area, either via a regular terminal (using "`lennart%versuch1`" when prompted for a user name), or via run0(1):

``` programlisting
lennart@zeta$ run0 --area=versuch1
```

## Module Types Provided

The module implements all four PAM operations: `auth` (to allow authentication using the encrypted data), `account` (because users with `systemd-homed.service` user accounts are described in a JSON user record and may be configured in more detail than in the traditional Linux user database), `session` (because user sessions must be tracked in order to implement automatic release when the last session of the user is gone), `password` (to change the encryption password — also used for user authentication — through PAM).

## Environment

The following environment variables are initialized by the module and available to the processes of the user's session:

`$SYSTEMD_HOME=1`  
Indicates that the user's home directory is managed by `systemd-homed.service`.

Added in version 245.

`$SYSTEMD_HOME_SUSPEND=`  
Indicates whether the session has been registered with the suspend mechanism enabled or disabled (see above). The variable's value is either "`0`" or "`1`". Note that the module both reads the variable when initializing, and sets it for sessions.

Added in version 246.

## Example

Here's an example PAM configuration fragment that permits users managed by `systemd-homed.service` to log in:

``` programlisting
#%PAM-1.0
    -auth     [success=done authtok_err=bad perm_denied=bad maxtries=bad default=ignore] pam_systemd_home.so
auth      sufficient pam_unix.so
auth      required   pam_deny.so

account   required   pam_nologin.so
-account  [success=done authtok_expired=bad new_authtok_reqd=bad maxtries=bad acct_expired=bad default=ignore] pam_systemd_home.so
account   required   pam_unix.so

-password sufficient pam_systemd_home.so
password  sufficient pam_unix.so sha512 shadow try_first_pass
password  required   pam_deny.so

-session  optional   pam_keyinit.so revoke
-session  optional   pam_loginuid.so
-session  optional   pam_systemd_home.so
-session  optional   pam_systemd.so
session   required   pam_unix.so
```

## See Also

systemd(1), systemd-homed.service(8), homed.conf(5), homectl(1), pam_systemd(8), pam.conf(5), pam.d(5), pam(8)
