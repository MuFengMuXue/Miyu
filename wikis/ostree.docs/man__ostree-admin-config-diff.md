## Name

ostree-admin-config-diff — Diff current /etc configuration versus default

## Synopsis

`ostree admin config-diff` \[OPTIONS...\]

## Description

Prints the differences between the current /etc directory and the default configuration in /usr/etc. Newly added files (present in /etc but not in /usr/etc) will be prefixed with 'A'. Modified files will be prefixed with 'M', and deleted files with 'D'.

## Options

`--os`="STATEROOT"  
Use a different operating system stateroot than the current one.

## Example

**\$ ostree admin config-diff**

``` programlisting
        M   shadow
        A   example.txt
    
```
