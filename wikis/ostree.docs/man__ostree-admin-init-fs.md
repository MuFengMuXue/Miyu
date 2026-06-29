## Name

ostree-admin-init-fs — Initialize a new root filesystem

## Synopsis

`ostree admin init-fs` \[OPTIONS...\] {PATH}

## Description

Initialize an empty physical root filesystem in the designated PATH, with normal toplevels and correct permissions for each directory. Primarily useful for operating system installers.

## Options

`--modern`  
Equivalent to `--epoch=1`.

`--epoch`  
This accepts an integer value in the range \[0-1\], inclusive. The default is zero for compatibility.

When set to 1, the command will skip adding a number of toplevel "API filesystems" such as `/proc` to the toplevel of the physical root. These should be unnecessary, as they should only be mounted in the final deployment root. The main exception is `/boot`, which may need to be mounted in some setups before the target root.

Epoch 2 is the same as 1, except that the toplevel `ostree` directory is mode 0700, denying access from unprivileged code. This is a new recommended best practice as it avoids access to old configuration files in `/etc` in previous deployments, as well as potentially old setuid binaries in `/ostree/repo`.

## Example

**\$ mkdir /example**

**\$ ostree admin init-fs --epoch=1 /example**

**\$ ls /example**

*boot*��
