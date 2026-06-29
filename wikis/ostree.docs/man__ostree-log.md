## Name

ostree-log — Show log starting at a commit or ref

## Synopsis

`ostree log` \[OPTIONS...\] {REF}

## Description

Shows a log of commits to a given ref or branch. Includes commit checksum, timestamp, and commit message.

## Options

`--raw`  
Show raw variant data.

## Example

**\$ ostree log my-branch**

``` programlisting
        commit 67e382b11d213a402a5313e61cbc69dfd5ab93cb07fbb8b71c2e84f79fa5d7dc
        Date:  2014-06-12 13:42:54 +0000
            This is the second commit

        commit ce19c41036cc45e49b0cecf6b157523c2105c4de1ce30101def1f759daafcc3e
        Date:  2014-06-12 11:20:08 +0000
            Initial commit
```
