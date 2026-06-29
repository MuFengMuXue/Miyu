# pam_canonicalize_user(8)

## Name
pam_canonicalize_user — Get user name and canonicalize it

## Synopsis
```
pam_canonicalize_user.so
```

## DESCRIPTION

This PAM module uses the name of the user obtained via `pam_get_user(3)` as a key to query the password database, and replaces *PAM_USER* with the *pw_name* value that has been returned.

## OPTIONS

This module does not recognise any options.

## MODULE TYPES PROVIDED

Only the `auth` module type is provided.

## RETURN VALUES

PAM_IGNORE  
The user name was set successfully.

PAM_USER_UNKNOWN  
The user was not found.

PAM_SYSTEM_ERR  
The application did not supply neither a user name nor a conversation method.

PAM_INCOMPLETE  
The conversation method supplied by the application is waiting for an event.

PAM_CONV_ERR  
The conversation method supplied by the application failed to obtain the user name.

PAM_ABORT  
Error resuming an old conversation.

PAM_BUF_ERR  
Memory buffer error.

## EXAMPLES

Prepend the PAM auth stack with the following line to canonicalize the user name before the authentication:

            auth required pam_canonicalize_user.so
          

## SEE ALSO

`pam_get_user(3)`, `pam_get_item(3)`, `pam_set_item(3)`, `getpwnam(3)`, `pam.conf(5)`, `pam.d(5)`, `pam(8)`
