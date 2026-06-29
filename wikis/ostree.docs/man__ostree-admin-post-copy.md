## Name

ostree-admin-post-copy — Fix up sysroot after a (file based) copy

## Synopsis

`ostree admin post-copy` \[OPTIONS...\]

## Description

Applies any fixes to a sysroot that are needed after having copyed it file by file. This includes enabling fs-verity to any files that lack it, which can happen if you copy a file.

## Options

`--sysroot`="PATH"  
Path to the system to use rather than the current one.
