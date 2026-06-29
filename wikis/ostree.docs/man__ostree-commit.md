## Name

ostree-commit — Commit a new revision

## Synopsis

`ostree commit` \[OPTIONS...\] --branch= {BRANCH} \[PATH\]

## Description

This allows you to commit changes to a branch. The specification of the branch is required. The command will print the checksum of a successful commit.

## Options

`--subject`, `-s`="SUBJECT"  
One line subject. (optional)

`--body`, `-m`="BODY"  
Full description. (optional)

`--body-file`, `-F`="FILE"  
Full commit description from a file. (optional)

`--editor`, `-e`  
Open a text editor for the commit description. It will use OSTREE_EDITOR, VISUAL, EDITOR, or vi, in descending order of preference. The commit will be aborted if the message is left empty.

`--branch`, `-b`="BRANCH"  
Branch. Required, unless --orphan is given.

`--parent`="COMMIT"  
Parent checksum or "none" to explicitly use no parent. If not specified, `BRANCH` is used as parent (no parent in case `BRANCH` does not exist).

`--tree`="dir=PATH" or "tar=TARFILE" or "ref=COMMIT"  
Overlay the given argument as a tree. When committing an archive, the TARFILE can be specified as `-` to read the archive from standard input.

`--base`="REV"  
Start from the content in a commit. This differs from `--tree=ref=REV` in that no commit modifiers are applied. This is usually what you want when creating a derived commit. This is also used for `--selinux-policy-from-base`.

`--add-metadata-string`="KEY=VALUE"  
Add a key/value pair to metadata. Can be specified multiple times.

`--add-metadata`="KEY=VALUE"  
Add a key/value pair to metadata, where the KEY is a string, and VALUE is g_variant_parse() formatted. Can be specified multiple times.

`--keep-metadata`="KEY"  
Keep metadata KEY and its associated VALUE from parent. Can be specified multiple times.

`--add-detached-metadata-string`="KEY=VALUE"  
Add a key/value pair to detached metadata.

`--owner-uid`="UID"  
Set file ownership user id.

`--owner-gid`="GID"  
Set file ownership group id.

`--no-xattrs`  
Do not import extended attributes.

`--selinux-labeling-epoch`0 \| 1  
When SELinux labeling is enabled, epoch `1` ensures that `/usr/etc` is labeled as if it was `/etc`.

`--bootable`  
Inject standard metadata for a bootable Linux filesystem tree.

`--link-checkout-speedup`  
Optimize for commits of trees composed of hardlinks into the repository.

`--tar-autocreate-parents`  
When loading tar archives, automatically create parent directories as needed.

`--skip-if-unchanged`  
If the contents are unchanged from previous commit, do nothing.

`--consume`  
When committing from a local directory (i.e. not an archive or --tree=ref), assume ownership of the content. This may simply involve deleting it, but if possible, the content may simply be `rename()`ed into the repository rather than creating a new copy.

`--statoverride`="PATH"  
File containing list of modifications to make permissions (file mode in decimal, followed by space, followed by file path). The specified mode is ORed with the file's original mode unless preceded by "=".

`--skip-list`="PATH"  
File containing list of file paths to skip (one path per line).

`--table-output`  
Output more information in a KEY: VALUE format.

`--generate-sizes`  
Generate size information along with commit metadata.

`--gpg-sign`="KEY-ID"  
GPG Key ID with which to sign the commit (if have GPGME - GNU Privacy Guard Made Easy).

`--gpg-homedir`="HOMEDIR"  
GPG home directory to use when looking for keyrings (if have GPGME - GNU Privacy Guard Made Easy).

`--timestamp`="TIMESTAMP"  
Override the timestamp of the commit to TIMESTAMP.

`--orphan`  
Create a commit without writing to a ref (branch)

`--fsync`="POLICY"  
POLICY is a boolean which specifies whether fsync should be used or not. Default to true.

`-s, --sign-type`  
Use particular signature engine. Currently available ed25519 , spki , and dummy signature types. The default is ed25519 .

`--sign-from-file`="PATH"  
This will read a key (corresponding to the provided `--sign-type` from the provided path. The encoding of the key depends on signature engine. For ed25519 the key should be base64 encoded, for spki it should be in PEM format, and for dummy it should be an ASCII-string.

`--sign`="KEY-ID"  
In new code, avoid using this because passing private keys via command line arguments are prone to leakage in logs and process listings.

The `KEY-ID` is:

`for ed25519 and spki:`  
`base64`-encoded secret key for commit signing.

`for dummy:`  
ASCII-string used as secret key.

## Example

**\$ ostree commit --branch=my-branch --subject="Initial commit"**

``` programlisting
        67e382b11d213a402a5313e61cbc69dfd5ab93cb07fbb8b71c2e84f79fa5d7dc
```
