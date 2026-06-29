# pam_prompt(3)

## Name
pam_prompt — interface to conversation function

## DESCRIPTION

The `pam_prompt` function constructs a message from the specified format string and arguments and passes it to the conversation function as set by the service. Upon successful return, *response* is set to point to a string returned from the conversation function. This string is allocated on heap and should be freed.

## RETURN VALUES

PAM_BUF_ERR  
Memory buffer error.

PAM_CONV_ERR  
Conversation failure.

PAM_SUCCESS  
Conversation succeeded, response is set.

PAM_SYSTEM_ERR  
System error.

## SEE ALSO

`pam(8)`, `pam_conv(3)`

## STANDARDS

The `pam_prompt` and `pam_vprompt` functions are Linux-PAM extensions.
