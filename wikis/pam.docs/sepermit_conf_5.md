# sepermit.conf(5)

## Name
sepermit.conf — configuration file for the pam_sepermit module

## DESCRIPTION

The lines of the configuration file have the following syntax:

\<\<user\>\>\[:\<\<option\>\>:\<\<option\>\>...\]

The *user* can be specified in the following manner:

- a username

- a groupname, with *@group* syntax. This should not be confused with netgroups.

- a SELinux user name with *%seuser* syntax.

The recognized options are:

exclusive  
Only single login session will be allowed for the user and the user's processes will be killed on logout.

ignore  
The module will never return PAM_SUCCESS status for the user. It will return PAM_IGNORE if SELinux is in the enforcing mode, and PAM_AUTH_ERR otherwise. It is useful if you want to support passwordless guest users and other confined users with passwords simultaneously.

The lines which start with \# character are comments and are ignored.

## EXAMPLES

These are some example lines which might be specified in `/etc/security/sepermit.conf`.

    %guest_u:exclusive
    %staff_u:ignore
    %user_u:ignore
        

## SEE ALSO

`pam_sepermit(8)`, `pam.d(5)`, `pam(8)`, `selinux(8)`,
