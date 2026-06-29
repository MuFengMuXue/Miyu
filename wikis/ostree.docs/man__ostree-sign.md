## Name

ostree-sign — Sign a commit

## Synopsis

`ostree sign` \[OPTIONS...\] {COMMIT} {KEY-ID...}

## Description

Add a new signature to a commit. Note that currently, this will append a new signature even if the commit is already signed with a given key.

For \`ed25519\` and \`spki\`, there are several "well-known" system places for trusted and revoked public keys as listed below.

Files:

- `/etc/ostree/trusted.`*`SIGN-TYPE`*

- `/etc/ostree/revoked.`*`SIGN-TYPE`*

- `/usr/share/ostree/trusted.`*`SIGN-TYPE`*

- `/usr/share/ostree/revoked.`*`SIGN-TYPE`*

Directories containing files with keys:

- `/etc/ostree/trusted.`*`SIGN-TYPE`*`.d`

- `/etc/ostree/revoked.`*`SIGN-TYPE`*`.d`

- `/usr/share/ostree/trusted.`*`SIGN-TYPE`*`.d`

- `/usr/share/ostree/revoked.`*`SIGN-TYPE`*`.d`

The format of those files depends on the signature mechanism; for \`ed25519\`, keys are stored in the `base64` encoding per line, while for \`spki\` they are stored in the PEM "PUBLIC KEY" encoding.

## Options

`KEY-ID`  
`for ed25519 and spki:`  
`base64`-encoded secret (for signing) or public key (for verifying).

`for dummy:`  
ASCII-string used as secret key and public key.

`--verify`  
Verify signatures

`-s, --sign-type`  
Use particular signature mechanism. Currently available ed25519 , spki , and dummy signature types. The default is ed25519 .

`--keys-file`  
Read key(s) from file `filename`.

Valid for `ed25519` and `spki` signature types. This file must contain `base64`-encoded secret key(s) (for signing) or public key(s) (for verifying) per line.

`--keys-dir`  
Redefine the system path, where to search files and subdirectories with well-known and revoked keys.
