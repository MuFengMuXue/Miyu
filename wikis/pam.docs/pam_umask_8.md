# pam_umask(8)

## Name
pam_umask — PAM module to set the file mode creation mask

## Synopsis
```
pam_umask.so debug silent usergroups nousergroups umask= mask
```

## DESCRIPTION

pam_umask is a PAM module to set the file mode creation mask of the current environment. The umask affects the default permissions assigned to newly created files.

The PAM module tries to get the umask value from the following places in the following order:

- umask= entry in the user's GECOS field (see below for details)

- umask= argument

- UMASK entry from /etc/login.defs

- UMASK= entry from /etc/default/login

The GECOS field is split on comma ',' characters. Entries must be set in its 'other' (sub-)field (the 5th field within the GECOS field), which could be done, for example, using `chfn --other`. In addition to the umask= entry, the module also recognizes the pri= entry, which sets the nice priority value for the session, and the ulimit= entry, which sets the maximum size of files the processes in the session can create.

## OPTIONS

debug  
Print debug information.

silent  
Don't print informative messages.

usergroups  
If the user is not root and the username is the same as primary group name, the umask group bits are set to be the same as owner bits (examples: 022 -\> 002, 077 -\> 007).

nousergroups  
This is the direct opposite of the usergroups option described above, which can be useful in case pam_umask has been compiled with usergroups enabled by default and you want to disable it at runtime.

umask=mask  
Sets the calling process's file mode creation mask (umask) to `mask` & 0777. The value is interpreted as Octal.

## MODULE TYPES PROVIDED

Only the `session` type is provided.

## RETURN VALUES

PAM_SUCCESS  
The new umask was set successfully.

PAM_BUF_ERR  
Memory buffer error.

PAM_CONV_ERR  
The conversation method supplied by the application failed to obtain the username.

PAM_INCOMPLETE  
The conversation method supplied by the application returned PAM_CONV_AGAIN.

PAM_SERVICE_ERR  
No username was given.

PAM_USER_UNKNOWN  
User not known.

## EXAMPLES

Add the following line to `/etc/pam.d/login` to set the user specific umask at login:

            session optional pam_umask.so umask=0022
          

## SEE ALSO

`pam.conf(5)`, `pam.d(5)`, `pam(8)`
