## Name

ostree-export — Generate a tar archive from an OSTree commit

## Synopsis

`ostree export` \[OPTIONS...\] {BRANCH}

## Description

This command generates a GNU tar formatted archive from an OSTree commit. This is useful for cases like backups, converting OSTree commits into Docker images, and the like.

## Example

**\$ ostree export exampleos/x86_64/standard \| gzip \> exampleos-standard.tar.gz**
