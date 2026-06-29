## Name

ostree-reset — Reset a ref to a previous commit

## Synopsis

`ostree reset ` {REF} {REF_TO_RESET_TO}

## Description

Given a commit, this command will reset the ref to a previous specified commit.

## Example

**\$ ostree log my-branch**

``` programlisting
        commit 67e382b11d213a402a5313e61cbc69dfd5ab93cb07
        Date:  2014-06-12 13:42:54 +0000
            This is the second commit

        commit ce19c41036cc45e49b0cecf6b157523c2105c4de1c
        Date:  2014-06-12 11:20:08 +0000
            Initial commit
```

**\$ ostree reset my-branch my-branch^**

**\$ ostree log my-branch**

``` programlisting
        commit ce19c41036cc45e49b0cecf6b157523c2105c4de1c
        Date:  2014-06-12 11:20:08 +0000
            Initial commit
```
