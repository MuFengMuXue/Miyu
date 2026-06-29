Other languages:

-   [Deutsch](https://wiki.gentoo.org/wiki/PAM/de "PAM (79% translated)")
-   [English]
-   [magyar](https://wiki.gentoo.org/wiki/PAM/hu "PAM (100% translated)")
-   [русский](https://wiki.gentoo.org/wiki/PAM/ru "PAM (77% translated)")
-   [中文（中国大陆）‎](https://wiki.gentoo.org/wiki/PAM/zh-cn "PAM (2% translated)")
-   [日本語](https://wiki.gentoo.org/wiki/PAM/ja "PAM (96% translated)")
-   [한국어](https://wiki.gentoo.org/wiki/PAM/ko "PAM/ko (40% translated)")

**Resources**

[[]][Home](http://www.linux-pam.org/)

[[]][Wikipedia](https://en.wikipedia.org/wiki/Linux_PAM "wikipedia:Linux PAM")

[[]][Package information](https://packages.gentoo.org/packages/sys-libs/pam)

PAM, or **P**luggable **A**uthentication **M**odules, is a modular approach to authentication. It allows (third party) services to provide an authentication module for their service which can then be used on PAM enabled systems. Services that use PAM for authentication can immediately use these modules without the need for a rebuild.

## Contents

-   [[1] [Introduction]](#Introduction)
    -   [[1.1] [Principles behind PAM]](#Principles_behind_PAM)
    -   [[1.2] [How PAM works]](#How_PAM_works)
-   [[2] [Configuration]](#Configuration)
    -   [[2.1] [Control directives]](#Control_directives)
    -   [[2.2] [Managing PAM configuration files]](#Managing_PAM_configuration_files)
-   [[3] [PAM and Gentoo]](#PAM_and_Gentoo)
-   [[4] [Example of how to parse system configuration]](#Example_of_how_to_parse_system_configuration)
-   [[5] [See also]](#See_also)
-   [[6] [External resources]](#External_resources)

## [[] Introduction]

Authentication management (part of access management) on a Linux server can be handled by PAM (Pluggable Authentication Modules). With PAM, services do not need to provide authentication services themselves. Instead, they rely on the PAM modules available on the system. Each service can use a different PAM configuration if it wants, although most of the time authentication is handled similarly across services. By calling PAM modules, services can support two-factor authentication out-of-the-box, immediately use centralized authentication repositories and more.

PAM provides a flexible, modular architecture for the following services:

-   Authentication management - verify if a user trying to authenticate a user account is actually the user.
-   Account management - check if that users\' password has expired or if the user is allowed to access this particular service.
-   Session management - execute certain tasks on logon or logoff of a user (auditing, mounting of file systems, \...).
-   Password management - offer an interface for password resets and the like.

** Note**\
PAM does *not* provide any services for authorizations. Generally, authorizations are done within an application. Some applications support group-based authorizations (so being a member of a group allows for being granted proper authorizations). A common (but not as common as PAM) approach for this is to support NSS (Name Service Switch). NSS is similar to PAM in its design principles. In fact, authorizations on Linux systems are handled through the NSS libraries.

### [[] Principles behind PAM]

When working with PAM, system administrators quickly discover the principles with which PAM works.

The first one is *back-end independence*. Applications that are PAM-aware do not need to incorporate any logic to deal with back-ends such as databases, LDAP service, password files, WS-Security enabled web services or other back-ends that have not been invented yet. By using PAM, applications segregate the back-end integration logic from their own. All they need to do is call PAM functions.

Another principle is *configuration independence*. Administrators do not need to learn how to configure dozens of different applications on how to interact with an LDAP server for authentication. Instead, they use the same configuration structure provided by PAM.

The final principle, which is part of the PAM name, is its *pluggable architecture*. When new back-ends need to be integrated, all the administrator has to do is to install the library for this back-end (by placing it in the right directory on the system) and configure this module (most of the modules use a single configuration file). From that point onward, the module is usable for applications. Administrators can configure the authentication to use this back-end and usually just need to restart the application.

### [[] How PAM works]

Applications that want to use PAM link with the PAM library (libpam) and call the necessary functions that reflect the above services. Other than that, the application does not need to implement any specific features for these services, as it is all handled by PAM. So when a user wants to authenticate itself against, say, a web application, then this web application calls PAM (passing on the user id and perhaps password or challenge) and checks the PAM return to see if the user is authenticated and allowed access to the application. It is PAM\'s task underlyingly to see where to authenticate against (such as a central database or LDAP server).

The strength of PAM is that everyone can build PAM modules to integrate with any PAM-enabled service or application. If a company releases a new service for authentication, all it needs to do is provide a PAM module that interacts with its service, and then all software that uses PAM can work with this service immediately: no need to rebuild or enhance those software titles.

## [[] Configuration]

Another important aspect of PAM is that it supports chaining of multiple modules. Let\'s look at a PAM configuration file for an unnamed service:

[FILE] **`/etc/pam.d/someservice`Example PAM configuration file for a service called \"someservice\"**

    # Authentication
    auth         required        pam_env.so
    auth         required        pam_ldap.so
    # Account management
    account      required        pam_ldap.so
    # Password management
    password     required        pam_ldap.so
    # Session management
    session      optional        pam_loginuid.so
    session      required        pam_selinux.so close
    session      required        pam_env.so
    session      required        pam_log.so level=audit
    session      required        pam_selinux.so open multiple
    session      optional        pam_mail.so

We see that the configuration file is structured in the four service domains that PAM supports: authentication, account management, password management, and session management.

Each of the sections in the configuration file calls one or more PAM modules. For instance, [pam_env.so] sets the environment variable which can be used by subsequent modules. The return code provided by the PAM module, together with the control directive (required or optional in the above example), allow PAM to decide how to proceed.

### [[] Control directives]

PAM supports the following control directives.

  -------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Control        Description
  `required`     The provided PAM module must succeed in order for the entire service (such as authentication) to succeed. If a PAM module fails, other PAM modules are still called upon (even though it is already certain that the service itself will be denied).
  `requisite`    The provided PAM module must succeed in order for the entire service to succeed. Unlike *required*, if the PAM module fails, control is immediately handed back and the service itself is denied.
  `sufficient`   If the provided PAM module succeeds, then the entire service is granted. The remainder of the PAM modules is not checked. If however the PAM module fails, then the remainder of the PAM modules is handled and the failure of this particular PAM module is ignored.
  `optional`     The success or failure of this particular PAM module is only important if it is the only module in the stack.
  `include`      Includes the contents of another PAM module\'s configuration file which matches the given type.
  -------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Chaining of modules allows for multiple authentications to be done, multiple tasks to be performed upon creating a session and more.

### [[] Managing PAM configuration files]

As the PAM configuration files control the authentication steps in an application, it is very important to safely manage the configuration files. These are generally stored in [/etc/pam.d/].

In larger enterprises, or security-sensitive systems, any modification of PAM configuration files should be properly audited.

The same goes for the location where the PAM modules themselves are stored ([/lib/security] or [/lib64/security]).

## [[] PAM and Gentoo]

Applications that can support PAM conditionally will use the [[[pam]](https://packages.gentoo.org/useflags/pam)[[]](https://wiki.gentoo.org/wiki/USE_flag "USE flag")] USE-flag. It is possible to run Gentoo systems without PAM (by setting `USE="-pam"`), but the default is to run with PAM support enabled.

When upgrading remote systems it is possible to leave the system inaccessible. To avoid this after an upgrade while being still logged in to the machine:

1.  check that logging is up and running
2.  check necessary configuration updates in [/etc/ssh] and [/etc/pam.d]
3.  check news items whether breaking changes were introduced, e.g. [PAM related news Item](https://www.gentoo.org/support/news-items/2020-06-23-upgrade-to-sys-libs_pam-1_4_0.html)
4.  check that changing passwords works flawlessly, e.g. [passwd] for root/ any user and cancel before actually changing the password
5.  restart [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") server in case it got updated
6.  check that a new login to the remote machine works

What could happen:

-   without logging errors during the checks cannot be analyzed
-   [passwd] errors out because of PAM module errors
-   SSH prohibits login because of PAM misconfiguration/ module errors, e.g. plain connection closed
-   password policies changed, e.g. prohibiting root without password

## [[] Example of how to parse system configuration]

In [this forum post](https://forums.gentoo.org/viewtopic-p-8623308.html) in 2021 given by [GDH-gentoo](https://forums.gentoo.org/profile.php?mode=viewprofile&u=393756), the configuration of a system is tracked down step-by-step, in order to find which service creates the directory [/run/user/\<uid\>] on a user login.

## [[] See also]

-   [PAM (Security Handbook)](https://wiki.gentoo.org/wiki/Security_Handbook/PAM "Security Handbook/PAM") --- Although the default PAM settings in Gentoo are reasonable, there is always room for improvement.
-   [PAM/U2F](https://wiki.gentoo.org/wiki/PAM/U2F "PAM/U2F") --- provides two-factor authentication through a FIDO U2F USB device, allowing users to authenticate at a press of a button against their system.
-   [PAM securetty](https://wiki.gentoo.org/wiki/PAM_securetty "PAM securetty") --- restricting [root] authentication with [PAM].
-   [pam_ssh_agent_auth](https://wiki.gentoo.org/wiki/Pam_ssh_agent_auth "Pam ssh agent auth") --- is the [PAM] module that allows a locally installed [SSH](https://wiki.gentoo.org/wiki/SSH "SSH") key to authenticate for [sudo](https://wiki.gentoo.org/wiki/Sudo "Sudo")
-   [Google Authenticator](https://wiki.gentoo.org/wiki/Google_Authenticator "Google Authenticator") --- describes an easy way to setup two-factor authentication on Gentoo.
-   [OATH-Toolkit](https://wiki.gentoo.org/wiki/OATH-Toolkit "OATH-Toolkit") --- toolkit for (OTP) One-Time Password authentication using HOTP/TOTP algorithms.
-   [YubiKey](https://wiki.gentoo.org/wiki/YubiKey "YubiKey") --- a hardware security device that can be used to safely store cryptographic keys, OTP tokens, and challenge response seeds

## [[] External resources]

-   [Working with PAM](https://devmanual.gentoo.org/tasks-reference/pam/index.html), a section inside the Gentoo developer manual