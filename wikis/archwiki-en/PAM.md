# PAM

The Linux Pluggable Authentication Modules (PAM) provides a framework for system-wide user authentication. To quote the project:

:PAM provides a way to develop programs that are independent of authentication scheme. These programs need "authentication modules" to be attached to them at run-time in order to work. Which authentication module is to be attached is dependent upon the local system setup and is at the discretion of the local system administrator.

This article explains the Arch Linux base set-up defaults for PAM to authenticate local and remote users. Applying changes to the defaults is subject of crosslinked specialized per topic articles.

## Installation
The  package is a dependency of the  meta package and, thereby, normally installed on an Arch system. The PAM modules are installed into  exclusively.

The repositories contain a number of optional PAM packages, the #Configuration How-Tos show examples.

## Configuration
A number of  paths are relevant for PAM; execute  to see the default configuration files created. They relate to either #Security parameters for the modules, or the #PAM base-stack configuration.

## Security parameters
The path  contains system-specific configuration for variables the authentication methods offer. The base install populates it with default upstream configuration files.

Note Arch Linux does not provide distribution-specific configuration for these files. For example, the  file can be used to define system-wide defaults for password quality. Yet, to enable it, the  module has to be added to the #PAM base-stack of modules, which is not the case per default.

See #Security parameter configuration for some of the possibilities.

## PAM base-stack
The  path is exclusive for the PAM configuration to link the applications to the individual systems' authentication schemes. During installation of the system base, it is populated by:

* the  package, which contains the base-stack of Arch Linux specific PAM configuration to be used by applications, and
* other base packages. For example,  adds configuration for the central login and other programs, the  package adds the Arch Linux defaults to secure and modify the user database (see Users and groups).

The different configuration files of the base installation link together and are stacked during runtime. For example, on a local user logon, the login application sources the  policy, which in turn sources others:

For a different application, a different path may apply. For example,  installs its  PAM policy:

Consequently, the choice of the configuration file in the stack matters. For the above example, a special authentication method could be required for  only, or all remote logins by changing ; both changes would not affect local logins. Applying the change to  or  instead would affect local and remote logins.

Like the example of , any pam-aware application is required to install its policy to  in order to integrate and rely on the PAM stack appropriately. If an application fails to do it, the  default policy to deny and log a warning is applied.

The PAM package manual pages  and  describe the standardized content of the configuration files. In particular, they explain the four PAM groups: account, authentication, password, and session management, as well as the control values that may be used to configure stacking and behavior of the modules.

Additionally, extensive documentation is installed to  which, among various guides, contains browsable man pages for each of the standard modules.

## Examples
Two short examples to illustrate the above warning.

First, we take the following two lines from a historic Arch default:

From :
:The authentication component  performs the task of checking the users credentials (password). The default action of this module is to not permit the user access to a service if their official password is blank.
- the latter being what  is used for. Simply swapping the control values  and  for both lines is enough to disable password authentication, i.e. any user may logon without providing a password.

Second, as the contrary example, per default configuration of  in , creating the following file:

 # touch /etc/nologin

results in that no user other than root may login (if root logins are allowed, see Security#Restricting root login). To allow logins again, remove the file again before your logout from the console you created it with.

With that as background, see #PAM stack and module configuration for particular use-case configuration.

## Configuration How-Tos
This section provides an overview of content detailing how to apply changes to the PAM configuration and how to integrate special new PAM modules into the PAM stack. Note the man pages for the modules can generally be reached dropping the  extension.

## Security parameter configuration
The following sections describe examples to change the default PAM parameter configuration:

* Security#Enforcing strong passwords with pam_pwquality
:shows how to enforce strong passwords with .
* Security#Lock out user after three failed login attempts
:shows how to configure the limits on login attempts with .
* Security#Allow only certain users
:limits user logons with .
* Realtime process management#Configuring PAM and Security#Limit amount of processes
:detail how to configure system process limits with .
* Environment variables#Using pam_env
:shows examples to set environment variables via .

## PAM stack and module configuration
The following articles detail how to change the #PAM base-stack for special use-cases.

; pam_mount: detail examples for using  to automount encrypted directory paths on user login.
; ECryptfs#Auto-mounting: uses  to automount an encrypted directory.
; Dm-crypt/Mounting at login : shows how to use  to execute a custom script on a user login.
; Active Directory integration#Configuring PAM: uses  and  to let users authenticate via Active Directory (LDAP, Kerberos) services.
; LDAP authentication: is an article about integrating LDAP client or server-side authentication with .
; YubiKey#Linux user authentication with PAM: describes how to use U2F () and the proprietary Yubico OTP implementation () provided by the YubiKey with PAM
; pam_oath : shows an example to implement software based two-factor authentication with .
; fprint: employs  to setup fingerprint authentication.
; pam_autologin : saves username and password to log in automatically.
; pam_usb : shows how to configure  to use an usb-device for, optionally two-factor, authentication.
; SSH keys#pam_ssh: uses  to authenticate as a remote user.
; pam_abl: explains how  can be used to limit brute-forcing attacks via ssh.
; EncFS : may get automounted via .
; Google Authenticator: shows how to set up two-factor authentication with .
; Very Secure FTP Daemon#PAM with virtual users: explains how to configure a FTP chroot with  to authenticate users without a local system account.

## Further PAM packages
Other than those packages mentioned so far, the Arch User Repository contains a number of additional PAM modules and tools:

*

*

Note the AUR features a keyword tag for PAM, but not all available packages are updated to include it. Hence, searching the package description may be necessary.

## Tips and tricks
## Locked out
If PAM has locked you out, perhaps by typing the wrong password too many times, see Security#Lock out user after three failed login attempts.
