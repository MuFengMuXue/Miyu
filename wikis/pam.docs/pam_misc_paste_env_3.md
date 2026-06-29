# pam_misc_paste_env(3)

## Name
pam_misc_paste_env — transcribing an environment to that of PAM

## DESCRIPTION

This function takes the supplied list of environment pointers and *uploads* its contents to the PAM environment. Success is indicated by PAM_SUCCESS.

## SEE ALSO

`pam_putenv(3)`, `pam(8)`

## STANDARDS

The `pam_misc_paste_env` function is part of the `libpam_misc` Library and not defined in any standard.
