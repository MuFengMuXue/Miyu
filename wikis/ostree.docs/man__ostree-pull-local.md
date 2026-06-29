## Name

ostree-pull-local — Copy data from a source repository

## Synopsis

`ostree pull-local` \[OPTIONS...\] {SOURCE_REPO} \[REFS...\]

## Description

Copies data from a given repository; optimized for copies only between repositories on the same system.

## Options

`--remote`="REMOTE"  
Add REMOTE to refspec.

`--disable-fsync`  
Do no invoke fsync().

`--untrusted`  
Do not trust source, verify checksums and don't hardlink into source.

`--disable-verify-bindings`  
Disable verification of commit metadata bindings.

## Example

**\$ ostree pull-local /ostree/repo**

``` programlisting
        Enumerating objects...
        pull: 25709/25709 scanned, 0 objects copied
        Writing 5 refs
```
