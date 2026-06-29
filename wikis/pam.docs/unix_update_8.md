# unix_update(8)

## Name
unix_update — Helper binary that updates the password of a given user

## Synopsis
```
unix_update ...
```

## DESCRIPTION

*unix_update* is a helper program for the *pam_unix* module that updates the password of a given user. It is not intended to be run directly from the command line and logs a security violation if done so.

The purpose of the helper is to enable tighter confinement of login and password changing services. The helper is thus called only when SELinux is enabled on the system.

The interface of the helper - command line options, and input/output data format are internal to the *pam_unix* module and it should not be called directly from applications.

## SEE ALSO

`pam_unix(8)`
