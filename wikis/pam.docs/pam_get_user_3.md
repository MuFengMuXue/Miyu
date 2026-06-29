# pam_get_user(3)

## Name
pam_get_user — get user name

## DESCRIPTION

The `pam_get_user` function returns the name of the user specified by `pam_start(3)`. If no user was specified it returns what `pam_get_item (pamh, PAM_USER, ... );` would have returned. If this is NULL it obtains the username via the `pam_conv(3)` mechanism, it prompts the user with the first non-NULL string in the following list:

- The *prompt* argument passed to the function.

- What is returned by pam_get_item (pamh, PAM_USER_PROMPT, ... );

- The default prompt: "login: "

By whatever means the username is obtained, a pointer to it is returned as the contents of *\*user*. Note, this memory should *not* be *free()*'d or *modified* by the module.

This function sets the *PAM_USER* item associated with the `pam_set_item(3)` and `pam_get_item(3)` functions.

## RETURN VALUES

PAM_SUCCESS  
User name was successful retrieved.

PAM_SYSTEM_ERR  
A NULL pointer was submitted.

PAM_CONV_ERR  
The conversation method supplied by the application failed to obtain the username.

PAM_BUF_ERR  
Memory buffer error.

PAM_ABORT  
Error resuming an old conversation.

PAM_CONV_AGAIN  
The conversation method supplied by the application is waiting for an event.

## SEE ALSO

`pam_end(3)`, `pam_get_item(3)`, `pam_set_item(3)`, `pam_strerror(3)`
