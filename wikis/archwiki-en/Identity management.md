# Identity management

Identity management (IDM), sometimes also identity and access management (IAM), deals with how users gain a digital identity, the roles, and sometimes the permission granted to this identity.

## Software
There is a number of software which helps doing identity management. Amongst, in alphabetical order, tools and related:

* Google Authenticator, two-step authentication, using one time passwords.
* Initiative for Open Authentication, standardization on how to get an access token for a web API call. Includes passwords, but will in future use WebAuthn.
* kanidm, some info here. Successor of LDAP, Kerberos. Server side of WebAuthn.
* Kerberos, with Active Directory integration, FreeIPA
* LDAP authentication, passwords in a central server.
* PAM, Linux pluggable authentication modules. Kerberos, LDAP, kanidm, etc. can be plugged into Linux.
* Universal 2nd Factor, replaced by WebAuthn.
* Users and groups. can be stored on a system or centrally via LDAP, kanidm.
* WebAuthn, browser web authentication API, replacement for password authentication, backwards compatible with Universal 2nd Factor.
