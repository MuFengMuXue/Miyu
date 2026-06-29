# org.freedesktop.PolicyKit1.Authority Interface

## Signals

Changed

()

## Properties

BackendName

readable String

BackendVersion

readable String

BackendFeatures

readable

AuthorityFeatures

## Description

This D-Bus interface is implemented by the `/org/freedesktop/PolicyKit1/Authority` object on the well-known name `org.freedesktop.PolicyKit1` on the system message bus.

## Enumerations

## The CheckAuthorizationFlags Flags

    {
      None                 = 0x00000000,
      AllowUserInteraction = 0x00000001,
      AlwaysCheck          = 0x00000002
    }
              

Flags used in the [CheckAuthorization()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.CheckAuthorization) method.

`None`  
No flags set.

`AllowUserInteraction`  
If the [Subject](#eggdbus-struct-Subject) can obtain the authorization through authentication, and an authentication agent is available, then attempt to do so. Note, this means that the [CheckAuthorization()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.CheckAuthorization) method will block while the user is being asked to authenticate.

`AlwaysCheck`  
Check access against policy even if the [Subject](#eggdbus-struct-Subject) is the root user.

## The ImplicitAuthorization Enumeration

    {
      NotAuthorized                               = 0,
      AuthenticationRequired                      = 1,
      AdministratorAuthenticationRequired         = 2,
      AuthenticationRequiredRetained              = 3,
      AdministratorAuthenticationRequiredRetained = 4,
      Authorized                                  = 5
    }
              

An enumeration for granting implicit authorizations.

`NotAuthorized`  
The [Subject](#eggdbus-struct-Subject) is not authorized.

`AuthenticationRequired`  
Authentication is required.

`AdministratorAuthenticationRequired`  
Authentication as an administrator is required.

`AuthenticationRequiredRetained`  
Authentication is required. If the authorization is obtained, it is retained.

`AdministratorAuthenticationRequiredRetained`  
Authentication as an administrator is required. If the authorization is obtained, it is retained.

`Authorized`  
The subject is authorized.

## The org.freedesktop.PolicyKit1.Error.\* Error Domain

    {
      org.freedesktop.PolicyKit1.Error.Failed,
      org.freedesktop.PolicyKit1.Error.Cancelled,
      org.freedesktop.PolicyKit1.Error.NotSupported,
      org.freedesktop.PolicyKit1.Error.NotAuthorized,
      org.freedesktop.PolicyKit1.Error.CancellationIdNotUnique
    }
              

Errors that can be returned by various method calls.

`org.freedesktop.PolicyKit1.Error.Failed`  
The operation failed.

`org.freedesktop.PolicyKit1.Error.Cancelled`  
The operation was cancelled.

`org.freedesktop.PolicyKit1.Error.NotSupported`  
The operation is not supported.

`org.freedesktop.PolicyKit1.Error.NotAuthorized`  
You are not authorized to perform the requested operation.

`org.freedesktop.PolicyKit1.Error.CancellationIdNotUnique`  
The passed `cancellation_id` is already in use.

## The AuthorityFeatures Flags

    {
      None                   = 0x00000000,
      TemporaryAuthorization = 0x00000001
    }
              

Flags describing features supported by the Authority implementation.

`None`  
No flags set.

`TemporaryAuthorization`  
The authority supports temporary authorizations that can be obtained through authentication.

## Structures

## The Subject Structure

    {
      String               subject_kind,
      Dict<String,Variant> subject_details
    }
              

This struct describes subjects such as UNIX processes. It is typically used to check if a given process is authorized for an action.

The following kinds of subjects are known:

**Unix Process**

`subject_kind` should be set to `unix-process` with keys `pidfd` (of type `int32`) and `uid` (of type `int32`) (if the operating system supports ProcessID File Descriptors), or alternatively with keys `pid` (of type `uint32`), `uid` (of type `int32`) and `start-time` (of type `uint64`).

**Unix Session**

`subject_kind` should be set to `unix-session` with the key `session-id` (of type `string`).

**System Bus Name**

`subject_kind` should be set to `system-bus-name` with the key `name` (of type `string`).

`String subject_kind`  
The type of the subject.

`Dict<String,Variant> subject_details`  
Details about the subject. Depending of the value of `subject_kind`, a set of well-defined key/value pairs are guaranteed to be available.

## The Identity Structure

    {
      String               identity_kind,
      Dict<String,Variant> identity_details
    }
              

This struct describes identities such as UNIX users and UNIX groups. It is typically used to check if a given process is authorized for an action.

The following kinds of identities are known:

**Unix User**

`identity_kind` should be set to `unix-user` with key `uid` (of type `uint32`).

**Unix Group**

`identity_kind` should be set to `unix-group` with key `gid` (of type `uint32`).

`String identity_kind`  
Type of identity.

`Dict<String,Variant> identity_details`  
Details about the identity. Depending of the value of `identity_kind`, a set of well-defined key/value pairs are guaranteed to be available.

## The ActionDescription Structure

    {
      String                action_id,
      String                description,
      String                message,
      String                vendor_name,
      String                vendor_url,
      String                icon_name,
      ImplicitAuthorization implicit_any,
      ImplicitAuthorization implicit_inactive,
      ImplicitAuthorization implicit_active,
      Dict<String,String>   annotations
    }
              

This struct describes actions registered with the PolicyKit daemon.

`String action_id`  
Action Identifier.

`String description`  
Localized description of the action.

`String message`  
Localized message to be displayed when making the user authenticate for an action.

`String vendor_name`  
Name of the provider of the action or the empty string.

`String vendor_url`  
A URL pointing to a place with more information about the action or the empty string.

`String icon_name`  
The themed icon describing the action or the empty string if no icon is set.

`ImplicitAuthorization implicit_any`  
A value from the [ImplicitAuthorization](#eggdbus-enum-ImplicitAuthorization). enumeration for implicit authorizations that apply to any [Subject](#eggdbus-struct-Subject).

`ImplicitAuthorization implicit_inactive`  
A value from the [ImplicitAuthorization](#eggdbus-enum-ImplicitAuthorization). enumeration for implicit authorizations that apply any [Subject](#eggdbus-struct-Subject) in an inactive user session on the local console.

`ImplicitAuthorization implicit_active`  
A value from the [ImplicitAuthorization](#eggdbus-enum-ImplicitAuthorization). enumeration for implicit authorizations that apply any [Subject](#eggdbus-struct-Subject) in an active user session on the local console.

`Dict<String,String> annotations`  
Annotations for the action.

## The AuthorizationResult Structure

    {
      Boolean             is_authorized,
      Boolean             is_challenge,
      Dict<String,String> details
    }
              

Describes the result of calling [CheckAuthorization()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.CheckAuthorization).

`Boolean is_authorized`  
TRUE if the given [Subject](#eggdbus-struct-Subject) is authorized for the given action.

`Boolean is_challenge`  
TRUE if the given [Subject](#eggdbus-struct-Subject) could be authorized if more information was provided, and [CheckAuthorizationFlags.AllowUserInteraction](#eggdbus-constant-CheckAuthorizationFlags.AllowUserInteraction) wasn't passed or no suitable authentication agent was available.

`Dict<String,String> details`  
Details for the result. Known key/value-pairs include `polkit.temporary_authorization_id` (if the authorization is temporary, this is set to the opaque temporary authorization id), `polkit.retains_authorization_after_challenge` (Set to a non-empty string if the authorization will be retained after authentication (if is_challenge is TRUE)), `polkit.dismissed` (Set to a non-empty string if the authentication dialog was dismissed by the user), `polkit.result` (Set to the string value of the polkit.Result enum, e.g.: `auth_admin`).

## The TemporaryAuthorization Structure

    {
      String  id,
      String  action_id,
      Subject subject,
      UInt64  time_obtained,
      UInt64  time_expires
    }
              

This struct describes a temporary authorization.

`String id`  
An opaque identifier for the temporary authorization.

`String action_id`  
The action the temporary authorization is for.

`Subject subject`  
The subject the temporary authorization is for.

`UInt64 time_obtained`  
When the temporary authorization was obtained, in seconds since the Epoch Jan 1, 1970 0:00 UTC. Note that the PolicyKit daemon is using monotonic time internally so the returned value may change if system time changes.

`UInt64 time_expires`  
When the temporary authorization is set to expire, in seconds since the Epoch Jan 1, 1970 0:00 UTC. Note that the PolicyKit daemon is using monotonic time internally so the returned value may change if system time changes.

## Method Details

## EnumerateActions ()

    EnumerateActions (IN  String                    locale,
                      OUT Array<ActionDescription>  action_descriptions)
        

Enumerates all registered PolicyKit actions.

`IN String locale`:  
The locale to get descriptions in or the blank string to use the system locale.

`OUT Array<ActionDescription> action_descriptions`:  
An array of [ActionDescription](#eggdbus-struct-ActionDescription) structs.

## CheckAuthorization ()

    CheckAuthorization (IN  Subject                  subject,
                        IN  String                   action_id,
                        IN  Dict<String,String>      details,
                        IN  CheckAuthorizationFlags  flags,
                        IN  String                   cancellation_id,
                        OUT AuthorizationResult      result)
        

Checks if `subject` is authorized to perform the action with identifier `action_id`

If `cancellation_id` is non-empty and already in use for the caller, the [org.freedesktop.PolicyKit1.Error.CancellationIdNotUnique](#eggdbus-constant-Error.org.freedesktop.PolicyKit1.Error.CancellationIdNotUnique) error is returned.

Note that [CheckAuthorizationFlags.AllowUserInteraction](#eggdbus-constant-CheckAuthorizationFlags.AllowUserInteraction) SHOULD be passed ONLY if the event that triggered the authorization check is stemming from an user action, e.g. the user pressing a button or attaching a device.

`IN Subject subject`:  
A [Subject](#eggdbus-struct-Subject) struct.

`IN String action_id`:  
Identifier for the action that `subject` is attempting to do.

`IN Dict<String,String> details`:  
Details describing the action. Keys starting with `polkit.` are can only be set if defined in this document.

Known keys include `polkit.message` and `polkit.gettext_domain` that can be used to override the message shown to the user. This latter is needed because the user could be running an authentication agent in another locale than the calling process.

The (translated version of) `polkit.message` may include references to other keys that are expanded with their respective values. For example if the key `device_file` has the value `/dev/sda` then the message "`Authenticate to format $(device_file)`" is expanded to "`Authenticate to format /dev/sda`".

The key `polkit.icon_name` is used to override the icon shown in the authentication dialog.

If non-empty, then the request will fail with [org.freedesktop.PolicyKit1.Error.Failed](#eggdbus-constant-Error.org.freedesktop.PolicyKit1.Error.Failed) unless the process doing the check itself is sufficiently authorized (e.g. running as uid 0).

`IN CheckAuthorizationFlags flags`:  
A set of [CheckAuthorizationFlags](#eggdbus-enum-CheckAuthorizationFlags).

`IN String cancellation_id`:  
A unique id used to cancel the the authentication check via [CancelCheckAuthorization()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.CancelCheckAuthorization) or the empty string if cancellation is not needed.

`OUT AuthorizationResult result`:  
An [AuthorizationResult](#eggdbus-struct-AuthorizationResult) structure.

## CancelCheckAuthorization ()

    CancelCheckAuthorization (IN  String  cancellation_id)
        

Cancels an authorization check.

`IN String cancellation_id`:  
The `cancellation_id` passed to [CheckAuthorization()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.CheckAuthorization).

## RegisterAuthenticationAgent ()

    RegisterAuthenticationAgent (IN  Subject  subject,
                                 IN  String   locale,
                                 IN  String   object_path)
        

Register an authentication agent.

Note that this should be called by same effective UID which will be passed to [AuthenticationAgentResponse2()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.AuthenticationAgentResponse2).

`IN Subject subject`:  
The subject to register the authentication agent for, typically a session subject.

`IN String locale`:  
The locale of the authentication agent.

`IN String object_path`:  
The object path of authentication agent object on the unique name of the caller.

## RegisterAuthenticationAgentWithOptions ()

    RegisterAuthenticationAgentWithOptions (IN  Subject  subject,
                                            IN  String                   locale,
                                            IN  String                   object_path,
                                            IN  Dict<String,Variant>     options)
        

Like [RegisterAuthenticationAgent](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.RegisterAuthenticationAgent) but takes additional options. If the option `fallback` (of type `Boolean`) is TRUE, then the authentcation agent will only be used as a fallback, e.g. if another agent (without the `fallback` option set TRUE) is available, it will be used instead.

## UnregisterAuthenticationAgent ()

    UnregisterAuthenticationAgent (IN  Subject  subject,
                                   IN  String   object_path)
        

Unregister an authentication agent.

`IN Subject subject`:  
The `subject` passed to [RegisterAuthenticationAgent()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.RegisterAuthenticationAgent).

`IN String object_path`:  
The `object_path` passed to [RegisterAuthenticationAgent()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.RegisterAuthenticationAgent).

## AuthenticationAgentResponse ()

    AuthenticationAgentResponse (IN  String    cookie,
                                 IN  Identity  identity)
        

Method for authentication agents to invoke on successful authentication, intended only for use by a privileged helper process internal to polkit. This method will fail unless a sufficiently privileged +caller invokes it. Deprecated in favor of [AuthenticationAgentResponse2()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.AuthenticationAgentResponse2).

`IN String cookie`:  
The cookie identifying the authentication request that was passed to the authentication agent.

`IN Identity identity`:  
A [Identity](#eggdbus-struct-Identity) struct describing what identity was authenticated.

## AuthenticationAgentResponse2 ()

    AuthenticationAgentResponse2 (IN  uint32 uid,
                                  IN  String cookie,
                                  IN  Identity  identity)
        

Method for authentication agents to invoke on successful authentication, intended only for use by a privileged helper process internal to polkit. This method will fail unless a sufficiently privileged caller invokes it. Note this method was introduced in 0.114 and should be preferred over [AuthenticationAgentResponse()](#eggdbus-method-org.freedesktop.PolicyKit1.Authority.AuthenticationAgentResponse) as it fixes a security issue.

`IN uint32 uid`:  
The user id of the agent; normally this is the owner of the parent pid of the process that invoked the internal setuid helper.

`IN String cookie`:  
The cookie identifying the authentication request that was passed to the authentication agent.

`IN Identity identity`:  
A [Identity](#eggdbus-struct-Identity) struct describing what identity was authenticated.

## AuthenticationAgentResponse3 ()

    AuthenticationAgentResponse3 (IN  String cookie,
                                  IN  Identity  identity,
                                  IN  Subject  subject)
        

Method for authentication agents to invoke on successful authentication, intended only for use by a privileged helper process running via socket activation. This method will fail unless a sufficiently privileged caller invokes it. In contract to other methods this takes a subject as input, which allows reliably tracking the requester via PID FD.

`IN String cookie`:  
The cookie identifying the authentication request that was passed to the authentication agent.

`IN Identity identity`:  
A [Identity](#eggdbus-struct-Identity) struct describing what identity was authenticated.

`IN Subject subject`:  
A [Subject](#eggdbus-struct-Subject) struct describing what entity requested the authentication.

## EnumerateTemporaryAuthorizations ()

    EnumerateTemporaryAuthorizations (IN  Subject                        subject,
                                      OUT Array<TemporaryAuthorization>  temporary_authorizations)
        

Retrieves all temporary authorizations that applies to `subject`.

`IN Subject subject`:  
The subject to get temporary authorizations for.

`OUT Array<TemporaryAuthorization> temporary_authorizations`:  
An array of [TemporaryAuthorization](#eggdbus-struct-TemporaryAuthorization) structs.

## RevokeTemporaryAuthorizations ()

    RevokeTemporaryAuthorizations (IN  Subject  subject)
        

Revokes all temporary authorizations that applies to `subject`.

`IN Subject subject`:  
The subject to revoke temporary authorizations from.

## RevokeTemporaryAuthorizationById ()

    RevokeTemporaryAuthorizationById (IN  String  id)
        

Revokes all temporary authorizations that applies to `subject`.

`IN String id`:  
The opaque identifier of the temporary authorization.

## Signal Details

## The "Changed" signal

    Changed ()
        

This signal is emitted when actions and/or authorizations change

## Property Details

## The "BackendName" property

    BackendName     readable     String
        

The name of the currently used Authority backend.

## The "BackendVersion" property

    BackendVersion     readable     String
        

The version of the currently used Authority backend.

## The "BackendFeatures" property

    BackendFeatures     readable     AuthorityFeatures
        

The features supported by the currently used Authority backend.
