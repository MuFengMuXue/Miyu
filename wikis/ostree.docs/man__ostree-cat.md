## Name

ostree-cat — Display or concatenate contents of files

## Synopsis

`ostree cat` {COMMIT} {PATH...}

## Description

This command functions much like the typical Unix "cat" command, in that it displays the contents of a file, or concatenates them given two or more files. However, this command requires the user to specify a commit - a checksum or refspec corresponding to a given build. If you use a refspec, OSTree will refer to the most recent commit, unless you specify a parent build using the carat (^) at the end of the refspec. It will then operate the command in that given commit.

## Example

**\$ ostree cat my-branch helloworld.txt**

``` programlisting
        Hello, world!
```
