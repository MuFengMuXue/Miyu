# pam_strerror(3)

## Name
pam_strerror — return string describing PAM error code

## DESCRIPTION

The `pam_strerror` function returns a pointer to a string describing the error code passed in the argument *errnum*, possibly using the LC_MESSAGES part of the current locale to select the appropriate language. This string must not be modified by the application. No library function will modify this string.

## RETURN VALUES

This function returns always a pointer to a string.

## SEE ALSO

`pam(8)`
