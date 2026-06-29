# pam_shells(8)

## Name
pam_shells — PAM module to check for valid login shell

## Synopsis
```
pam_shells.so
```

## DESCRIPTION

pam_shells is a PAM module that only allows access to the system if the user's shell is listed in `/etc/shells`.

If this file does not exist, entries are taken from files `%vendordir%/shells`, `%vendordir%/shells.d/*` and `/etc/shells.d/*` in that order.

It also checks if needed files (e.g. `/etc/shells`) are plain files and not world writable.

## OPTIONS

This module does not recognise any options.

## MODULE TYPES PROVIDED

The `auth` and `account` module types are provided.

## RETURN VALUES

PAM_AUTH_ERR  
Access to the system was denied.

PAM_SUCCESS  
The user's login shell was listed as valid shell in `/etc/shells`.

PAM_USER_UNKNOWN  
The user does not exist or the user's login shell could not be determined.

PAM_SERVICE_ERR  
The module was not able to get the name of the user.

## EXAMPLES

    auth  required  pam_shells.so
          

## SEE ALSO

`shells(5)`, `pam.conf(5)`, `pam.d(5)`, `pam(8)`
