## Name

ostree-rev-parse — Output the target of a rev

## Synopsis

`ostree rev-parse ` {REV} {PATH}

## Options

`--single`, `-S`  
If the repository has exactly one commit, then print it; any other case will result in an error.

## Description

Given a REV, outputs the checksum of the latest commit of that revision.

## Example

**\$ ostree rev-parse my-branch**

``` programlisting
        ce19c41036cc45e49b0cecf6b157523c2105c4de1ce30101def1f759daafcc3e
```
