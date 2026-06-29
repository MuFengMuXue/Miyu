## Name

ostree-fsck — Check the repository for consistency

## Synopsis

`ostree fsck` \[OPTIONS...\]

## Description

Checks the repository to verify the content integrity of commit objects. Looks for missing and corrupted objects and metadata, and validates directory structure and metadata.

## Options

`--quiet`,`-q`  
Only print error messages.

`--delete`  
Remove corrupted objects.

`--add-tombstones`  
Add tombstone commit for referenced but missing commits.

`--verify-bindings`  
Verify that the commits pointed to by each ref have that ref in the binding set. You should usually add this option; it only defaults to off for backwards compatibility.

`--verify-back-refs`  
Verify that all the refs listed in a commit’s ref-bindings point to that commit. This cannot be used in repositories where the target of refs is changed over time as new commits are added, but can be used in repositories which are regenerated from scratch for each commit. Implies `--verify-bindings` as well.

## Example

**\$ ostree fsck**

``` programlisting
        Enumerating objects...
        Verifying content integrity of of 2 commit objects
        0/2572 objects
        2571/2572 objects
```
