## Name

ostree-admin-cleanup — Delete untagged deployments and repository objects

## Synopsis

`ostree admin cleanup `

## Description

OSTree sysroot cleans up other bootversions and old deployments. If/when a pull or deployment is interrupted, a partially written state may remain on disk. This command cleans up any such partial states.

## Example

**\$ ostree admin cleanup**
