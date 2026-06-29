# org.freedesktop.PolicyKit1.AuthenticationAgent Interface

## Description

This D-Bus interface is used for communication between the system-wide PolicyKit daemon and one or more authentication agents each running in a user session.

An authentication agent must implement this interface and register (passing the object path of the object implementing the interface) using the [RegisterAuthenticationAgent()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.RegisterAuthenticationAgent) and [UnregisterAuthenticationAgent()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.UnregisterAuthenticationAgent) methods on the [org.freedesktop.PolicyKit1.Authority](#eggdbus-interface-org.freedesktop.PolicyKit1.Authority) interface of the PolicyKit daemon.

## Method Details

## BeginAuthentication ()

    BeginAuthentication (IN  String               action_id,
                         IN  String               message,
                         IN  String               icon_name,
                         IN  Dict<String,String>  details,
                         IN  String               cookie,
                         IN  Array<Identity>      identities)
        

Called by the PolicyKit daemon when the authentication agent needs the user to authenticate as one of the identities in `identities` for the action with the identifier `action_id`.

Upon succesful authentication, the authentication agent must invoke the [AuthenticationAgentResponse2()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.AuthenticationAgentResponse2) method on the [org.freedesktop.PolicyKit1.Authority](#eggdbus-interface-org.freedesktop.PolicyKit1.Authority) interface of the PolicyKit daemon before returning. This is normally achieved via the [PolkitAgentSession](#PolkitAgentSession) API, which invokes a private setuid helper process to verify the authentication.

The authentication agent should not return until after authentication is complete. If the user dismisses the authentication dialog, the authentication agent should return the [org.freedesktop.PolicyKit1.Error.Cancelled](#eggdbus-constant-Error.org.freedesktop.PolicyKit1.Error.Cancelled) error.

`IN String action_id`:  
The identifier for the action that the user is authentication for.

`IN String message`:  
The message to display to the user. This is translated into the locale passed when registering the authentication agent using [RegisterAuthenticationAgent()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.RegisterAuthenticationAgent).

`IN String icon_name`:  
The themed icon describing the action or the empty string if no icon is set.

`IN Dict<String,String> details`:  
Details about the authentication request. This is a dictionary of key/value pairs where both key and value are strings. Known key/value-pairs include `polkit.caller-pid` (the process id of the mechanism making the authorization check) and `polkit.subject-pid` (the process id of the subject the check is for).

`IN String cookie`:  
A cookie identifying the authentication request.

`IN Array<Identity> identities`:  
An array of [Identity](#eggdbus-struct-Identity) structs that the user can use for authentication.

## CancelAuthentication ()

    CancelAuthentication (IN  String  cookie)
        

Called by the PolicyKit daemon if the authentication agent needs to cancel an authentication dialog.

`IN String cookie`:  
The cookie identifying the authentication request.
