# pam_info(3)

## Name
pam_info — display messages to the user

## DESCRIPTION

The `pam_info` function prints messages through the conversation function to the user.

The `pam_vinfo` function performs the same task as `pam_info()` with the difference that it takes a set of arguments which have been obtained using the `stdarg(3)` variable argument list macros.

## RETURN VALUES

PAM_BUF_ERR  
Memory buffer error.

PAM_CONV_ERR  
Conversation failure.

PAM_SUCCESS  
Transaction was successful created.

PAM_SYSTEM_ERR  
System error.

## SEE ALSO

`pam(8)`

## STANDARDS

The `pam_info` and `pam_vinfo` functions are Linux-PAM extensions.
