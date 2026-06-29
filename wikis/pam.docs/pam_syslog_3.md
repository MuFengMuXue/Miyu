# pam_syslog(3)

## Name
pam_syslog — send messages to the system logger

## DESCRIPTION

The `pam_syslog` function logs messages using `syslog(3)` and is intended for internal use by Linux-PAM and PAM service modules. The *priority* argument is formed by ORing the facility and the level values as documented in the `syslog(3)` manual page.

The `pam_vsyslog` function performs the same task as `pam_syslog()` with the difference that it takes a set of arguments which have been obtained using the `stdarg(3)` variable argument list macros.

## SEE ALSO

`pam(8)`

## STANDARDS

The `pam_syslog` and `pam_vsyslog` functions are Linux-PAM extensions.
