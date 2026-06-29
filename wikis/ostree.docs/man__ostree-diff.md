## Name

ostree-diff — Compare a directory against a revision

## Synopsis

`ostree diff` \[OPTIONS...\] {REV_OR_DIR} {REV_OR_DIR}

## Description

Compare a directory or revision against another directory or revision. If REV_OR_DIR starts with \`/\` or \`./\`, it is interpreted as a directory, otherwise a revision. Shows files and directories modified, added, and deleted. If there is a file in the second REV_OR_DIR not in the first, it will show with an "A" for "added". If a file in the first REV_OR_DIR is not in the second, it shows "D" for "deleted". "M" for "modified" will also show.

## Options

`--stats`  
Print various statistics.

`--fs-diff`  
Print filesystem diff.

`--owner-uid`  
Use file ownership user id for local files.

`--owner-gid`  
Use file ownership group id for local files.

## Example

**\$ ostree diff my-branch^ my-branch**

``` programlisting
        A   /testdirectory
        M   /helloworld.txt
```

**\$ ostree diff my-branch my-branch^**

``` programlisting
        D   /testdirectory
        M   /helloworld.txt
```
