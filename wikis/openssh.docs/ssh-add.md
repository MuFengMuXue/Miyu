# Ssh Add

adds private key identities to the authentication agent,

When run without arguments, it adds the files

and

After loading a private key,

will try to load corresponding certificate information from the filename obtained by appending

to the name of the private key file. Alternative file names can be given on the command line.

If any file requires a passphrase,

asks for the passphrase from the user. The passphrase is read from the user's tty.

retries the last passphrase if multiple identity files are given.

The authentication agent must be running and the

environment variable must contain the name of its socket for

to work.

The options are as follows:

When loading keys into or deleting keys from the agent, process certificates only and skip plain keys.

Indicates that added identities should be subject to confirmation before being used for authentication. Confirmation is performed by

Successful confirmation is signaled by a zero exit status from

rather than text entered into the requester.

Deletes all identities from the agent.

Instead of adding identities, removes identities from the agent. If

has been run without arguments, the keys for the default identities and their corresponding certificates will be removed. Otherwise, the argument list will be interpreted as a list of paths to public key files to specify keys and certificates to be removed from the agent. If no public key is found at a given path,

will append

and retry. If the argument list consists of

then

will read public keys to be removed from standard input.

Specifies the hash algorithm used when displaying key fingerprints. Valid options are:

and

The default is

Remove keys provided by the PKCS#11 shared library

Specifies a known hosts file to look up hostkeys when using destination-constrained keys via the

flag. This option may be specified multiple times to allow multiple files to be searched. If no files are specified,

will use the default

known hosts files:

and

When adding keys, constrain them to be usable only through specific hosts or to specific destinations.

Destination constraints of the form

permit use of the key only from the origin host (the one running

to the listed destination host, with optional user name.

Constraints of the form

allow a key available on a forwarded

to be used through a particular host (as specified by

to authenticate to a further host, specified by

Multiple destination constraints may be added when loading keys. When attempting authentication with a key that has destination constraints, the whole connection path, including

forwarding, is tested against those constraints and each hop must be permitted for the attempt to succeed. For example, if key is forwarded to a remote host,

and is attempting authentication to another host,

then the operation will be successful only if

was permitted from the origin host and the subsequent

hop is also permitted by destination constraints.

Hosts are identified by their host keys, and are looked up from known hosts files by

Wildcards patterns may be used for hostnames and certificate host keys are supported. By default, keys added by

are not destination constrained.

Destination constraints were added in OpenSSH release 8.9. Support in both the remote SSH client and server is required when using destination-constrained keys over a forwarded

channel.

It is also important to note that destination constraints can only be enforced by

when a key is used, or when it is forwarded by a

Specifically, it does not prevent an attacker with access to a remote

from forwarding it again and using it on a different host (but only to a permitted destination).

Load resident keys from a FIDO authenticator.

When loading keys into or deleting keys from the agent, process plain private keys only and skip certificates.

Lists public key parameters of all identities currently represented by the agent.

Lists fingerprints of all identities currently represented by the agent.

When adding certificates, by default

will request that the agent automatically delete the certificate shortly after the certificate's expiry date. This flag suppresses this behaviour and does not specify a lifetime for certificates added to an agent.

Query the agent for the list of protocol extensions it supports. Note: not all agents support this query.

Be quiet after a successful operation.

Specifies a path to a library that will be used when adding FIDO authenticator-hosted keys, overriding the default of using the internal USB HID support.

Add keys provided by the PKCS#11 shared library

Certificate files may optionally be listed as command-line arguments. If these are present, then they will be loaded into the agent using any corresponding private keys loaded from the PKCS#11 token.

Tests whether the private keys that correspond to the specified

files are usable by performing sign and verify operations on each.

Set a maximum lifetime when adding identities to an agent. The lifetime may be specified in seconds or in a time format specified in

Verbose mode. Causes

to print debugging messages about its progress. This is helpful in debugging problems. Multiple

options increase the verbosity. The maximum is 3.

Unlock the agent.

Lock the agent with a password.

If

needs a passphrase, it will read the passphrase from the current terminal if it was run from a terminal. If

does not have a terminal associated with it but

and

are set, it will execute the program specified by

(by default

and open an X11 window to read the passphrase. This is particularly useful when calling

from a

or related script.

allows further control over the use of an askpass program. If this variable is set to

then

will never attempt to use one. If it is set to

then

will prefer to use the askpass program instead of the TTY when requesting passwords. Finally, if the variable is set to

then the askpass program will be used for all passphrase input regardless of whether

is set.

Identifies the path of a

socket used to communicate with the agent.

Specifies a path to a library that will be used when loading any FIDO authenticator-hosted keys, overriding the default of using the built-in USB HID support.

Contains the ECDSA, authenticator-hosted ECDSA, Ed25519, authenticator-hosted Ed25519 or RSA authentication identity of the user.

Identity files should not be readable by anyone but the user. Note that

ignores identity files if they are accessible by others.

Exit status is 0 on success, 1 if the specified command fails, and 2 if

is unable to contact the authentication agent.

OpenSSH is a derivative of the original and free ssh 1.2.12 release by Tatu Ylonen. Aaron Campbell, Bob Beck, Markus Friedl, Niels Provos, Theo de Raadt and Dug Song removed many bugs, re-added newer features and created OpenSSH. Markus Friedl contributed the support for SSH protocol versions 1.5 and 2.0.
