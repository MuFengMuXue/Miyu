# Sshd Config

reads configuration data from

(or the file specified with

on the command line). The file contains keyword-argument pairs, one per line. Unless noted otherwise, for each keyword, the first obtained value will be used. Lines starting with

and empty lines are interpreted as comments. Arguments may optionally be enclosed in double quotes

in order to represent arguments containing spaces.

The possible keywords and their meanings are as follows (note that keywords are case-insensitive and arguments are case-sensitive):

Specifies what environment variables sent by the client will be copied into the session's

See

and

in

for how to configure the client. The

environment variable is always accepted whenever the client requests a pseudo-terminal as it is required by the protocol. Variables are specified by name, which may contain the wildcard characters

and

Multiple environment variables may be separated by whitespace or spread across multiple

directives. Be warned that some environment variables could be used to bypass restricted user environments. For this reason, care should be taken in the use of this directive. The default is not to accept any environment variables.

Specifies which address family should be used by

Valid arguments are

(the default),

(use IPv4 only), or

(use IPv6 only).

Specifies whether

forwarding is permitted. The default is

Note that disabling agent forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.

This keyword can be followed by a list of group name patterns, separated by spaces. If specified, login is allowed only for users whose primary group or supplementary group list matches one of the patterns. Only group names are valid; a numerical group ID is not recognized. By default, login is allowed for all groups.

is not consulted for groups matched by

See PATTERNS in

for more information on patterns. This keyword may appear multiple times in

with each instance appending to the list.

Specifies whether StreamLocal (Unix-domain socket) forwarding is permitted. The available options are

(the default) or

to allow StreamLocal forwarding,

to prevent all StreamLocal forwarding,

to allow local (from the perspective of

forwarding only or

to allow remote forwarding only. Note that disabling StreamLocal forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.

Specifies whether TCP forwarding is permitted. The available options are

(the default) or

to allow TCP forwarding,

to prevent all TCP forwarding,

to allow local (from the perspective of

forwarding only or

to allow remote forwarding only. Note that disabling TCP forwarding does not improve security unless users are also denied shell access, as they can always install their own forwarders.

This keyword can be followed by a list of user name patterns, separated by spaces. If specified, login is allowed only for user names that match one of the patterns. Only user names are valid; a numerical user ID is not recognized. By default, login is allowed for all users. If the pattern takes the form USER@HOST then USER and HOST are separately checked, restricting logins to particular users from particular hosts. HOST criteria may additionally contain addresses to match in CIDR address/masklen format.

is not consulted for users matched by

See PATTERNS in

for more information on patterns. This keyword may appear multiple times in

with each instance appending to the list.

Specifies the authentication methods that must be successfully completed for a user to be granted access. This option must be followed by one or more lists of comma-separated authentication method names, or by the single string

to indicate the default behaviour of accepting any single authentication method. If the default is overridden, then successful authentication requires completion of every method in at least one of these lists.

For example,

would require the user to complete public key authentication, followed by either password or keyboard interactive authentication. Only methods that are next in one or more lists are offered at each stage, so for this example it would not be possible to attempt password or keyboard-interactive authentication before public key.

For keyboard interactive authentication it is also possible to restrict authentication to a specific device by appending a colon followed by the device identifier

or

depending on the server configuration. For example,

would restrict keyboard interactive authentication to the

device.

If the publickey method is listed more than once,

verifies that keys that have been used successfully are not reused for subsequent authentications. For example,

requires successful authentication using two different public keys.

Note that each authentication method listed should also be explicitly enabled in the configuration.

The available authentication methods are:

(used for access to password-less accounts when

is enabled),

and

Specifies a program to be used to look up the user's public keys. The program must be owned by root, not writable by group or others and specified by an absolute path. Arguments to

accept the tokens described in the

section. If no arguments are specified then the username of the target user is used.

The program should produce on standard output zero or more lines of authorized_keys output (see

in

is tried after the usual

files and will not be executed if a matching key is found there. By default, no

is run. This command is only executed for valid users.

Specifies the user under whose account the

is run. It is recommended to use a dedicated user that has no other role on the host than running authorized keys commands. If

is specified but

is not, then

will refuse to start.

Specifies the file that contains the public keys used for user authentication. The format is described in the AUTHORIZED_KEYS FILE FORMAT section of

Arguments to

may include wildcards and accept the tokens described in the

section. After expansion,

is taken to be an absolute path or one relative to the user's home directory. Multiple files may be listed, separated by whitespace. Alternately this option may be set to

to skip checking for user keys in files. The default is

These files are only checked for valid users.

Specifies a program to be used to generate the list of allowed certificate principals as per

The program must be owned by root, not writable by group or others and specified by an absolute path. Arguments to

accept the tokens described in the

section. If no arguments are specified then the username of the target user is used.

The program should produce on standard output zero or more lines of

output. If either

or

is specified, then certificates offered by the client for authentication must contain a principal that is listed. By default, no

is run. This command is only executed for valid users.

Specifies the user under whose account the

is run. It is recommended to use a dedicated user that has no other role on the host than running authorized principals commands. If

is specified but

is not, then

will refuse to start.

Specifies a file that lists principal names that are accepted for certificate authentication. When using certificates signed by a key listed in

this file lists names, one of which must appear in the certificate for it to be accepted for authentication. Names are listed one per line preceded by key options (as described in

in

Empty lines and comments starting with

are ignored.

Arguments to

may include wildcards and accept the tokens described in the

section. After expansion,

is taken to be an absolute path or one relative to the user's home directory. The default is

i.e. not to use a principals file – in this case, the username of the user must appear in a certificate's principals list for it to be accepted. This file is only checked for valid users.

Note that

is only used when authentication proceeds using a CA listed in

and is not consulted for certification authorities trusted via

though the

key option offers a similar facility (see

for details).

The contents of the specified file are sent to the remote user before authentication is allowed. If the argument is

then no banner is displayed. By default, no banner is displayed.

Specifies which algorithms are allowed for signing of certificates by certificate authorities (CAs). The default is:

ssh-ed25519,ecdsa-sha2-nistp256, ecdsa-sha2-nistp384,ecdsa-sha2-nistp521, sk-ssh-ed25519@openssh.com, sk-ecdsa-sha2-nistp256@openssh.com, rsa-sha2-512,rsa-sha2-256

If the specified list begins with a

character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a

character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them.

Certificates signed using other algorithms will not be accepted for public key or host-based authentication.

Specifies whether and how quickly

should close inactive channels. Timeouts are specified as one or more

pairs separated by whitespace, where the

must be the special keyword

or a channel type name from the list below, optionally containing wildcard characters.

The timeout value

is specified in seconds or may use any of the units documented in the

section. For example,

would cause interactive sessions to terminate after five minutes of inactivity. Specifying a zero value disables the inactivity timeout.

The special timeout

applies to all active channels, taken together. Traffic on any active channel will reset the timeout, but when the timeout expires then all open channels will be closed. Note that this global timeout is not matched by wildcards and must be specified explicitly.

The available channel type names include:

Open connections to

Open TCP or Unix socket (respectively) connections that have been established from an

local forwarding, i.e.

or

Open TCP or Unix socket (respectively) connections that have been established to an

listening on behalf of an

remote forwarding, i.e.

The interactive main session, including shell session, command execution,

etc.

Open

connections.

Open X11 forwarding sessions.

Note that in all the above cases, terminating an inactive session does not guarantee to remove all resources associated with the session, e.g. shell processes or X11 clients relating to the session may continue to execute.

Moreover, terminating an inactive channel or session does not necessarily close the SSH connection, nor does it prevent a client from requesting another channel of the same type. In particular, expiring an inactive forwarding session does not prevent another identical forwarding from being subsequently created.

The default is not to expire channels of any type for inactivity.

Specifies the pathname of a directory to

to after authentication. At session startup

checks that all components of the pathname are root-owned directories which are not writable by group or others. After the chroot,

changes the working directory to the user's home directory. Arguments to

accept the tokens described in the

section.

The

must contain the necessary files and directories to support the user's session. For an interactive session this requires at least a shell, typically

and basic

nodes such as

and

devices. For file transfer sessions using SFTP no additional configuration of the environment is necessary if the in-process sftp-server is used, though sessions which use logging may require

inside the chroot directory on some operating systems (see

for details).

For safety, it is very important that the directory hierarchy be prevented from modification by other processes on the system (especially those outside the jail). Misconfiguration can lead to unsafe environments which

cannot detect.

The default is

indicating not to

Specifies the ciphers allowed. Multiple ciphers must be comma-separated. If the specified list begins with a

character, then the specified ciphers will be appended to the default set instead of replacing them. If the specified list begins with a

character, then the specified ciphers (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a

character, then the specified ciphers will be placed at the head of the default set.

The supported ciphers are:

3des-cbc

aes128-cbc

aes192-cbc

aes256-cbc

aes128-ctr

aes192-ctr

aes256-ctr

aes128-gcm@openssh.com

aes256-gcm@openssh.com

chacha20-poly1305@openssh.com

The default is:

chacha20-poly1305@openssh.com, aes128-gcm@openssh.com,aes256-gcm@openssh.com, aes128-ctr,aes192-ctr,aes256-ctr

The list of available ciphers may also be obtained using

Sets the number of client alive messages which may be sent without

receiving any messages back from the client. If this threshold is reached while client alive messages are being sent, sshd will disconnect the client, terminating the session. It is important to note that the use of client alive messages is very different from

The client alive messages are sent through the encrypted channel and therefore will not be spoofable. The TCP keepalive option enabled by

is spoofable. The client alive mechanism is valuable when the client or server depend on knowing when a connection has become unresponsive.

The default value is 3. If

is set to 15, and

is left at the default, unresponsive SSH clients will be disconnected after approximately 45 seconds. Setting a zero

disables connection termination.

Sets a timeout interval in seconds after which if no data has been received from the client,

will send a message through the encrypted channel to request a response from the client. The default is 0, indicating that these messages will not be sent to the client.

Specifies whether compression is enabled after the user has authenticated successfully. The argument must be

(a legacy synonym for

or

The default is

Compression applies to all traffic that flows over the SSH connection. If untrusted traffic (such as an open port-forward) is permitted over the connection alongside trusted traffic, then compression may leak information about session contents. For this reason, it is not recommended to enable compression for connections that share trusted and untrusted traffic.

This keyword can be followed by a list of group name patterns, separated by spaces. Login is disallowed for users whose primary group or supplementary group list matches one of the patterns. Only group names are valid; a numerical group ID is not recognized. By default, login is allowed for all groups.

is not consulted for groups matched by

See PATTERNS in

for more information on patterns. This keyword may appear multiple times in

with each instance appending to the list.

This keyword can be followed by a list of user name patterns, separated by spaces. Login is disallowed for user names that match one of the patterns. Only user names are valid; a numerical user ID is not recognized. By default, login is allowed for all users. If the pattern takes the form USER@HOST then USER and HOST are separately checked, restricting logins to particular users from particular hosts. HOST criteria may additionally contain addresses to match in CIDR address/masklen format.

is not consulted for users matched by

See PATTERNS in

for more information on patterns. This keyword may appear multiple times in

with each instance appending to the list.

Disables all forwarding features, including X11,

TCP and StreamLocal. This option overrides all other forwarding-related options and may simplify restricted configurations.

Writes a temporary file containing a list of authentication methods and public credentials (e.g. keys) used to authenticate the user. The location of the file is exposed to the user session through the

environment variable. The default is

Specifies the hash algorithm used when logging key fingerprints. Valid options are:

and

The default is

Forces the execution of the command specified by

ignoring any command supplied by the client and

if present. The command is invoked by using the user's login shell with the -c option. This applies to shell, command, or subsystem execution. It is most useful inside a

block. The command originally supplied by the client is available in the

environment variable. Specifying a command of

will force the use of an in-process SFTP server that requires no support files when used with

The default is

This directive does not limit other kinds of access that a client may request via their connection, such as TCP, agent, socket or X11 forwarding. If these are not desired, then they must be explicitly disabled, either individually via their respective options or all together using the

option.

Specifies whether remote hosts are allowed to connect to ports forwarded for the client. By default,

binds remote port forwardings to the loopback address. This prevents other remote hosts from connecting to forwarded ports.

can be used to specify that sshd should allow remote port forwardings to bind to non-loopback addresses, thus allowing other hosts to connect. The argument may be

to force remote port forwardings to be available to the local host only,

to force remote port forwardings to bind to the wildcard address, or

to allow the client to select the address to which the forwarding is bound. The default is

Specifies whether user authentication based on GSSAPI is allowed. The default is

Specifies whether to automatically destroy the user's credentials cache on logout. The default is

Accept delegated credentials on the server side. The default is

Determines whether to be strict about the identity of the GSSAPI acceptor a client authenticates against. If set to

then the client must authenticate against the host service on the current hostname. If set to

then the client may authenticate against any service key stored in the machine's default store. This facility is provided to assist with operation on multi homed machines. The default is

Specifies the signature algorithms that will be accepted for hostbased authentication as a list of comma-separated patterns. Alternately if the specified list begins with a

character, then the specified signature algorithms will be appended to the default set instead of replacing them. If the specified list begins with a

character, then the specified signature algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a

character, then the specified signature algorithms will be placed at the head of the default set. The default for this option is:

ssh-ed25519-cert-v01@openssh.com, ecdsa-sha2-nistp256-cert-v01@openssh.com, ecdsa-sha2-nistp384-cert-v01@openssh.com, ecdsa-sha2-nistp521-cert-v01@openssh.com, sk-ssh-ed25519-cert-v01@openssh.com, sk-ecdsa-sha2-nistp256-cert-v01@openssh.com, webauthn-sk-ecdsa-sha2-nistp256-cert-v01@openssh.com, rsa-sha2-512-cert-v01@openssh.com, rsa-sha2-256-cert-v01@openssh.com, ssh-ed25519, ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521, sk-ssh-ed25519@openssh.com, sk-ecdsa-sha2-nistp256@openssh.com, webauthn-sk-ecdsa-sha2-nistp256@openssh.com, rsa-sha2-512,rsa-sha2-256

The list of available signature algorithms may also be obtained using

This was formerly named HostbasedAcceptedKeyTypes.

Specifies whether rhosts or /etc/hosts.equiv authentication together with successful public key client host authentication is allowed (host-based authentication). The default is

Specifies whether or not the server will attempt to perform a reverse name lookup when matching the name in the

and

files during

A setting of

means that

uses the name supplied by the client rather than attempting to resolve the name from the TCP connection itself. The default is

Specifies a file containing a public host certificate. The certificate's public key must match a private host key already specified by

The default behaviour of

is not to load any certificates.

Specifies a file containing a private host key used by SSH. The defaults are

and

Note that

will refuse to use a file if it is group/world-accessible and that the

option restricts which of the keys are actually used by

It is possible to have multiple host key files. It is also possible to specify public host key files instead. In this case operations on the private key will be delegated to an

Identifies the UNIX-domain socket used to communicate with an agent that has access to the private host keys. If the string

is specified, the location of the socket will be read from the

environment variable.

Specifies the host key signature algorithms that the server offers. The default for this option is:

ssh-ed25519-cert-v01@openssh.com, ecdsa-sha2-nistp256-cert-v01@openssh.com, ecdsa-sha2-nistp384-cert-v01@openssh.com, ecdsa-sha2-nistp521-cert-v01@openssh.com, sk-ssh-ed25519-cert-v01@openssh.com, sk-ecdsa-sha2-nistp256-cert-v01@openssh.com, webauthn-sk-ecdsa-sha2-nistp256-cert-v01@openssh.com, rsa-sha2-512-cert-v01@openssh.com, rsa-sha2-256-cert-v01@openssh.com, ssh-ed25519, ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521, sk-ssh-ed25519@openssh.com, sk-ecdsa-sha2-nistp256@openssh.com, webauthn-sk-ecdsa-sha2-nistp256@openssh.com, rsa-sha2-512,rsa-sha2-256

The list of available signature algorithms may also be obtained using

Specifies whether to ignore per-user

and

files during

The system-wide

and

are still used regardless of this setting.

Accepted values are

(the default) to ignore all per-user files,

to allow the use of

but to ignore

or

to allow both

and

Specifies whether

should ignore the user's

during

and use only the system-wide known hosts file

The default is

Include the specified configuration file(s). Multiple pathnames may be specified and each pathname may contain

wildcards that will be expanded and processed in lexical order. Files without absolute paths are assumed to be in

An

directive may appear inside a

block to perform conditional inclusion.

Specifies the

value for the connection. Accepted values are

a numeric value, or

to use the operating system default. This option may take one or two arguments, separated by whitespace. If one argument is specified, it is used as the packet class unconditionally. If two values are specified, the first is automatically selected for interactive sessions and the second for non-interactive sessions. The default is

(Expedited Forwarding) for interactive sessions and

(the operating system default) for non-interactive sessions.

Specifies whether to allow keyboard-interactive authentication. All authentication styles from

are supported. The default is

The argument to this keyword must be

or

is a deprecated alias for this.

Specifies whether the password provided by the user for

will be validated through the Kerberos KDC. To use this option, the server needs a Kerberos servtab which allows the verification of the KDC's identity. The default is

If AFS is active and the user has a Kerberos 5 TGT, attempt to acquire an AFS token before accessing the user's home directory. The default is

If password authentication through Kerberos fails then the password will be validated via any additional local mechanism such as

The default is

Specifies whether to automatically destroy the user's ticket cache file on logout. The default is

Specifies the permitted KEX (Key Exchange) algorithms that the server will offer to clients. The ordering of this list is not important, as the client specifies the preference order. Multiple algorithms must be comma-separated.

If the specified list begins with a

character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a

character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a

character, then the specified algorithms will be placed at the head of the default set.

The supported algorithms are:

curve25519-sha256

curve25519-sha256@libssh.org

diffie-hellman-group1-sha1

diffie-hellman-group14-sha1

diffie-hellman-group14-sha256

diffie-hellman-group16-sha512

diffie-hellman-group18-sha512

diffie-hellman-group-exchange-sha1

diffie-hellman-group-exchange-sha256

ecdh-sha2-nistp256

ecdh-sha2-nistp384

ecdh-sha2-nistp521

mlkem768x25519-sha256

sntrup761x25519-sha512

sntrup761x25519-sha512@openssh.com

The default is:

mlkem768x25519-sha256, sntrup761x25519-sha512,sntrup761x25519-sha512@openssh.com, curve25519-sha256,curve25519-sha256@libssh.org, ecdh-sha2-nistp256,ecdh-sha2-nistp384,ecdh-sha2-nistp521

The list of supported key exchange algorithms may also be obtained using

Specifies the local addresses

should listen on. The following forms may be used:

The optional

qualifier requests

listen in an explicit routing domain. If

is not specified, sshd will listen on the address and all

options specified. The default is to listen on all local addresses on the current default routing domain. Multiple

options are permitted. For more information on routing domains, see

The server disconnects after this time if the user has not successfully logged in. If the value is 0, there is no time limit. The default is 120 seconds.

Gives the verbosity level that is used when logging messages from

The possible values are: QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG, DEBUG1, DEBUG2, and DEBUG3. The default is INFO. DEBUG and DEBUG1 are equivalent. DEBUG2 and DEBUG3 each specify higher levels of debugging output. Logging with a DEBUG level violates the privacy of users and is not recommended.

Specify one or more overrides to

An override consists of one or more pattern lists that matches the source file, function and line number to force detailed logging for. For example, an override pattern of:

kex.c:\*:1000,\*:kex_exchange_identification():\*,packet.c:\*

would enable detailed logging for line 1000 of

everything in the

function, and all code in the

file. This option is intended for debugging and no overrides are enabled by default.

Specifies the available MAC (message authentication code) algorithms. The MAC algorithm is used for data integrity protection. Multiple algorithms must be comma-separated. If the specified list begins with a

character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a

character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a

character, then the specified algorithms will be placed at the head of the default set.

The algorithms that contain

calculate the MAC after encryption (encrypt-then-mac). These are considered safer and their use recommended. The supported MACs are:

hmac-md5

hmac-md5-96

hmac-sha1

hmac-sha1-96

hmac-sha2-256

hmac-sha2-512

umac-64@openssh.com

umac-128@openssh.com

hmac-md5-etm@openssh.com

hmac-md5-96-etm@openssh.com

hmac-sha1-etm@openssh.com

hmac-sha1-96-etm@openssh.com

hmac-sha2-256-etm@openssh.com

hmac-sha2-512-etm@openssh.com

umac-64-etm@openssh.com

umac-128-etm@openssh.com

The default is:

umac-64-etm@openssh.com,umac-128-etm@openssh.com, hmac-sha2-256-etm@openssh.com,hmac-sha2-512-etm@openssh.com, hmac-sha1-etm@openssh.com, umac-64@openssh.com,umac-128@openssh.com, hmac-sha2-256,hmac-sha2-512,hmac-sha1

The list of available MAC algorithms may also be obtained using

Introduces a conditional block. If all of the criteria on the

line are satisfied, the keywords on the following lines override those set in the global section of the config file, until either another

line or the end of the file. If a keyword appears in multiple

blocks that are satisfied, only the first instance of the keyword is applied.

The arguments to

are one or more criteria-pattern pairs or one of the single token criteria:

which matches all criteria, or

which matches when the requested user-name does not match any known account. The available criteria are

and

(with

representing the

on which the connection was received).

The match patterns may consist of single entries or comma-separated lists and may use the wildcard and negation operators described in the

section of

The patterns in an

criteria may additionally contain addresses to match in CIDR address/masklen format, such as 192.0.2.0/24 or 2001:db8::/32. Note that the mask length provided must be consistent with the address - it is an error to specify a mask length that is too long for the address or one with bits set in this host portion of the address. For example, 192.0.2.0/33 and 192.0.2.0/8, respectively.

The

keyword matches against the version string of

for example

Only a subset of keywords may be used on the lines following a

keyword. Available keywords are

and

Specifies the maximum number of authentication attempts permitted per connection. Once the number of failures reaches half this value, additional failures are logged. The default is 6.

Specifies the maximum number of open shell, login or subsystem (e.g. sftp) sessions permitted per network connection. Multiple sessions may be established by clients that support connection multiplexing. Setting

to 1 will effectively disable session multiplexing, whereas setting it to 0 will prevent all shell, login and subsystem sessions while still permitting forwarding. The default is 10.

Specifies the maximum number of concurrent unauthenticated connections to the SSH daemon. Additional connections will be dropped until authentication succeeds or the

expires for a connection.

Alternatively, random early drop can be enabled by specifying the three colon separated values start:rate:full (e.g. "10:30:60"). The default is 10:30:100.

will refuse connection attempts with a probability of rate/100 (30%) if there are currently start (10) unauthenticated connections. The probability increases linearly and all connection attempts are refused if the number of unauthenticated connections reaches full (60).

Specifies the

file that contains the Diffie-Hellman groups used for the

and

key exchange methods. The default is

Specifies the service name used for Pluggable Authentication Modules (PAM) authentication, authorisation and session controls when

is enabled. The default is

Specifies whether password authentication is allowed. The default is

When password authentication is allowed, it specifies whether the server allows login to accounts with empty password strings. The default is

Specifies the addresses/ports on which a remote TCP port forwarding may listen. The listen specification must be one of the following forms:

Multiple permissions may be specified by separating them with whitespace. An argument of

can be used to remove all restrictions and permit any listen requests. An argument of

can be used to prohibit all listen requests. The host name may contain wildcards as described in the PATTERNS section in

The wildcard

can also be used in place of a port number to allow all ports. By default all port forwarding listen requests are permitted. Note that the

option may further restrict which addresses may be listened on. Note also that

will request a listen host of

if no listen host was specifically requested, and this name is treated differently to explicit localhost addresses of

and

Specifies the destinations to which TCP port forwarding is permitted. The forwarding specification must be one of the following forms:

Multiple forwards may be specified by separating them with whitespace. An argument of

can be used to remove all restrictions and permit any forwarding requests. An argument of

can be used to prohibit all forwarding requests. The wildcard

can be used for host or port to allow all hosts or ports respectively. Otherwise, no pattern matching or address lookups are performed on supplied names. By default all port forwarding requests are permitted.

Specifies whether root can log in using

The argument must be

or

The default is

If this option is set to

(or its deprecated alias,

password and keyboard-interactive authentication are disabled for root.

If this option is set to

root login with public key authentication will be allowed, but only if the

option has been specified (which may be useful for taking remote backups even if root login is normally not allowed). All other authentication methods are disabled for root.

If this option is set to

root is not allowed to log in.

Specifies whether

allocation is permitted. The default is

Specifies whether

device forwarding is allowed. The argument must be

(layer 3),

(layer 2), or

Specifying

permits both

and

The default is

Independent of this setting, the permissions of the selected

device must allow access to the user.

Specifies whether

and

options in

are processed by

Valid options are

or a pattern-list specifying which environment variable names to accept (for example

The default is

Enabling environment processing may enable users to bypass access restrictions in some configurations using mechanisms such as

Specifies whether any

file is executed. The default is

Specifies the number of unauthenticated connections allowed from a given source address, or

if there is no limit. This limit is applied in addition to

whichever is lower. The default is

Specifies the number of bits of source address that are grouped together for the purposes of applying PerSourceMaxStartups limits. Values for IPv4 and optionally IPv6 may be specified, separated by a colon. The default is

which means each address is considered individually.

Controls penalties for various conditions that may represent attacks on

If a penalty is enforced against a client then its source address and any others in the same network, as defined by

will be refused connection for a period.

A penalty doesn't affect concurrent connections in progress, but multiple penalties from the same source from concurrent connections will accumulate up to a maximum. Conversely, penalties are not applied until a minimum threshold time has been accumulated.

Penalties are enabled by default with the default settings listed below but may disabled using the

keyword. The defaults may be overridden by specifying one or more of the keywords below, separated by whitespace. All keywords accept arguments, e.g.

Specifies how long to refuse clients that cause a crash of

Specifies how long to refuse clients that disconnect after making one or more unsuccessful authentication attempts (default: 5s).

Specifies how long to refuse clients that attempt to log in with an invalid user (default: 5s).

Specifies how long to refuse clients that were administratively prohibited connection via the

option (default: 10s).

Specifies how long to refuse clients that disconnect without attempting authentication (default: 1s). This timeout should be used cautiously otherwise it may penalise legitimate scanning tools such as

Specifies how long to refuse clients that fail to authenticate after

(default: 10s).

Specifies the maximum time a particular source address range will be refused access for (default: 10m). Repeated penalties will accumulate up to this maximum.

Specifies the minimum penalty that must accrue before enforcement begins (default: 15s).

Specifies the maximum number of client IPv4 and IPv6 address ranges to track for penalties (default: 65536 for both).

Controls how the server behaves when

or

is exceeded. There are two operating modes:

which denies all incoming connections other than those exempted via

until a penalty expires, and

which allows new connections by removing existing penalties early (default: permissive). Note that client penalties below the

threshold count against the total number of tracked penalties. IPv4 and IPv6 addresses are tracked separately, so an overflow in one will not affect the other.

Allows specifying a different overflow mode for IPv6 addresses. The default it to use the same overflow mode as was specified for IPv4.

Specifies a comma-separated list of addresses to exempt from penalties. This list may contain wildcards and CIDR address/masklen ranges. Note that the mask length provided must be consistent with the address - it is an error to specify a mask length that is too long for the address or one with bits set in this host portion of the address. For example, 192.0.2.0/33 and 192.0.2.0/8, respectively. The default is not to exempt any addresses.

Specifies the file that contains the process ID of the SSH daemon, or

to not write one. The default is

Specifies the port number that

listens on. The default is 22. Multiple options of this type are permitted. See also

Specifies whether

should print the date and time of the last user login when a user logs in interactively. The default is

Specifies whether

should print

when a user logs in interactively. (On some systems it is also printed by the shell,

or equivalent.) The default is

Specifies the signature algorithms that will be accepted for public key authentication as a list of comma-separated patterns. Alternately if the specified list begins with a

character, then the specified algorithms will be appended to the default set instead of replacing them. If the specified list begins with a

character, then the specified algorithms (including wildcards) will be removed from the default set instead of replacing them. If the specified list begins with a

character, then the specified algorithms will be placed at the head of the default set. The default for this option is:

ssh-ed25519-cert-v01@openssh.com, ecdsa-sha2-nistp256-cert-v01@openssh.com, ecdsa-sha2-nistp384-cert-v01@openssh.com, ecdsa-sha2-nistp521-cert-v01@openssh.com, sk-ssh-ed25519-cert-v01@openssh.com, sk-ecdsa-sha2-nistp256-cert-v01@openssh.com, webauthn-sk-ecdsa-sha2-nistp256-cert-v01@openssh.com, rsa-sha2-512-cert-v01@openssh.com, rsa-sha2-256-cert-v01@openssh.com, ssh-ed25519, ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521, sk-ssh-ed25519@openssh.com, sk-ecdsa-sha2-nistp256@openssh.com, webauthn-sk-ecdsa-sha2-nistp256@openssh.com, rsa-sha2-512,rsa-sha2-256

The list of available signature algorithms may also be obtained using

Sets one or more public key authentication options. The supported keywords are:

(the default; indicating no additional options are enabled),

and

The

option causes public key authentication using a FIDO authenticator algorithm (i.e.

or

to always require the signature to attest that a physically present user explicitly confirmed the authentication (usually by touching the authenticator). By default,

requires user presence unless overridden with an authorized_keys option. The

flag disables this override.

The

option requires a FIDO key signature attest that the user was verified, e.g. via a PIN.

Neither the

or

options have any effect for other, non-FIDO, public key types.

Specifies whether public key authentication is allowed. The default is

Indicates that

should unconditionally terminate the connection. Additionally, a

penalty may be recorded against the source of the connection if

are enabled. This option is only really useful in a

block.

Specifies the maximum amount of data that may be transmitted or received before the session key is renegotiated, optionally followed by a maximum amount of time that may pass before the session key is renegotiated. The first argument is specified in bytes and may have a suffix of

or

to indicate Kilobytes, Megabytes, or Gigabytes, respectively. The default is between

and

depending on the cipher. The optional second value is specified in seconds and may use any of the units documented in the

section. The default value for

is

which means that rekeying is performed after the cipher's default amount of data has been sent or received and no time based rekeying is done.

Specifies the minimum RSA key size (in bits) that

will accept. User and host-based authentication keys smaller than this limit will be refused. The default is

bits. Note that this limit may only be raised from the default.

Specifies revoked public keys file, or

to not use one. Keys listed in this file will be refused for public key authentication. Note that if this file is not readable, then public key authentication will be refused for all users. Keys may be specified as a text file, listing one public key per line, or as an OpenSSH Key Revocation List (KRL) as generated by

This file may be consulted for each public key authentication attempt received by

and its contents must be consistent at all times, therefore it should only be atomically replaced and never modified in place while the server is running. For more information on KRLs, see the KEY REVOCATION LISTS section in

Specifies an explicit routing domain that is applied after authentication has completed. The user session, as well as any forwarded or listening IP sockets, will be bound to this

If the routing domain is set to

then the domain in which the incoming connection was received will be applied.

Specifies a path to a library that will be used when loading FIDO authenticator-hosted keys, overriding the default of using the built-in USB HID support.

Specifies one or more environment variables to set in child sessions started by

as

The environment value may be quoted (e.g. if it contains whitespace characters). Environment variables set by

override the default environment and any variables specified by the user via

or

Overrides the default path to the

binary that is invoked to complete user authentication. The default is

This option is intended for use by tests.

Overrides the default path to the

binary that is invoked to handle each connection. The default is

This option is intended for use by tests.

Sets the octal file creation mode mask

used when creating a Unix-domain socket file for local or remote port forwarding. This option is only used for port forwarding to a Unix-domain socket file.

The default value is 0177, which creates a Unix-domain socket file that is readable and writable only by the owner. Note that not all operating systems honor the file mode on Unix-domain socket files.

Specifies whether to remove an existing Unix-domain socket file for local or remote port forwarding before creating a new one. If the socket file already exists and

is not enabled,

will be unable to forward the port to the Unix-domain socket file. This option is only used for port forwarding to a Unix-domain socket file.

The argument must be

or

The default is

Specifies whether

should check file modes and ownership of the user's files and home directory before accepting login. This is normally desirable because novices sometimes accidentally leave their directory or files world-writable. The default is

Note that this does not apply to

whose permissions and ownership are checked unconditionally.

Configures an external subsystem (e.g. file transfer daemon). Arguments should be a subsystem name and a command (with optional arguments) to execute upon subsystem request.

The command

implements the SFTP file transfer subsystem.

Alternately the name

implements an in-process SFTP server. This may simplify configurations using

to force a different filesystem root on clients. It accepts the same command line arguments as

and even though it is in-process, settings such as

or

do not apply to it and must be set explicitly via command line arguments.

By default no subsystems are defined.

Gives the facility code that is used when logging messages from

The possible values are: DAEMON, USER, AUTH, LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7. The default is AUTH.

Specifies whether the system should send TCP keepalive messages to the other side. If they are sent, death of the connection or crash of one of the machines will be properly noticed. However, this means that connections will die if the route is down temporarily, and some people find it annoying. On the other hand, if TCP keepalives are not sent, sessions may hang indefinitely on the server, leaving

users and consuming server resources.

The default is

(to send TCP keepalive messages), and the server will notice if the network goes down or the client host crashes. This avoids infinitely hanging sessions.

To disable TCP keepalive messages, the value should be set to

Specifies a file containing public keys of certificate authorities that are trusted to sign user certificates for authentication, or

to not use one. Keys are listed one per line; empty lines and comments starting with

are allowed. If a certificate is presented for authentication and has its signing CA key listed in this file, then it may be used for authentication for any user listed in the certificate's principals list. Note that certificates that lack a list of principals will not be permitted for authentication using

For more details on certificates, see the CERTIFICATES section in

Specifies whether and how quickly

should close client connections with no open channels. Open channels include active shell, command execution or subsystem sessions, connected network, socket, agent or X11 forwardings. Forwarding listeners, such as those from the

flag, are not considered as open channels and do not prevent the timeout. The timeout value is specified in seconds or may use any of the units documented in the

section.

Note that this timeout starts when the client connection completes user authentication but before the client has an opportunity to open any channels. Caution should be used when using short timeout values, as they may not provide sufficient time for the client to request and open its channels before terminating the connection.

The default

is to never expire connections for having no open channels. This option may be useful in conjunction with

Specifies whether

should look up the remote host name, and to check that the resolved host name for the remote IP address maps back to the very same IP address.

If this option is set to

(the default) then only addresses and not host names may be used in

and

directives.

Enables the Pluggable Authentication Module interface. If set to

this will enable PAM authentication using

and

in addition to PAM account and session module processing for all authentication types.

Because PAM keyboard-interactive authentication usually serves an equivalent role to password authentication, you should disable either

or

If

is enabled, you will not be able to run

as a non-root user. The default is

Optionally specifies additional text to append to the SSH protocol banner sent by the server upon connection. The default is

Specifies the first display number available for

X11 forwarding. This prevents sshd from interfering with real X11 servers. The default is 10.

Specifies whether X11 forwarding is permitted. The argument must be

or

The default is

When X11 forwarding is enabled, there may be additional exposure to the server and to client displays if the

proxy display is configured to listen on the wildcard address (see

though this is not the default. Additionally, the authentication spoofing and authentication data verification and substitution occur on the client side. The security risk of using X11 forwarding is that the client's X11 display server may be exposed to attack when the SSH client requests forwarding (see the warnings for

in

A system administrator may have a stance in which they want to protect clients that may expose themselves to attack by unwittingly requesting X11 forwarding, which can warrant a

setting.

Note that disabling X11 forwarding does not prevent users from forwarding X11 traffic, as users can always install their own forwarders.

Specifies whether

should bind the X11 forwarding server to the loopback address or to the wildcard address. By default, sshd binds the forwarding server to the loopback address and sets the hostname part of the

environment variable to

This prevents remote hosts from connecting to the proxy display. However, some older X11 clients may not function with this configuration.

may be set to

to specify that the forwarding server should be bound to the wildcard address. The argument must be

or

The default is

Specifies the full pathname of the

program, or

to not use one. The default is

command-line arguments and configuration file options that specify time may be expressed using a sequence of the form:

where

is a positive integer value and

is one of the following:

seconds

seconds

minutes

hours

days

weeks

Each member of the sequence is added together to calculate the total time value.

Time format examples:

600 seconds (10 minutes)

10 minutes

1 hour 30 minutes (90 minutes)

Arguments to some keywords can make use of tokens, which are expanded at runtime. Tokens are expanded without quoting or escaping of shell characters. It is the administrator's responsibility to ensure they are safe in the context of their use.

The supported tokens in

are:

A literal

Identifies the connection endpoints, containing four space-separated values: client address, client port number, server address, and server port number.

The routing domain in which the incoming connection was received.

The fingerprint of the CA key.

The fingerprint of the key or certificate.

The home directory of the user.

The key ID in the certificate.

The base64-encoded CA key.

The base64-encoded key or certificate for authentication.

The serial number of the certificate.

The type of the CA key.

The key or certificate type.

The numeric user ID of the target user.

The username.

accepts the tokens %%, %C, %D, %f, %h, %k, %t, %U, and %u.

accepts the tokens %%, %h, %U, and %u.

accepts the tokens %%, %C, %D, %F, %f, %h, %i, %K, %k, %s, %T, %t, %U, and %u.

accepts the tokens %%, %h, %U, and %u.

accepts the tokens %%, %h, %U, and %u.

accepts the token %D.

Contains configuration data for

This file should be writable by root only, but it is recommended (though not necessary) that it be world-readable.

OpenSSH is a derivative of the original and free ssh 1.2.12 release by

and

removed many bugs, re-added newer features and created OpenSSH.

contributed the support for SSH protocol versions 1.5 and 2.0.

and

contributed support for privilege separation.
