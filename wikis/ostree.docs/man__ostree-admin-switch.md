## Name

ostree-admin-switch — Construct new tree from current origin and deploy it, if it changed

## Synopsis

`ostree admin switch` {REF}

## Description

Choose a different REF from the current remote to track. This is the ref that will be "tracked" and upgraded with **ostree admin upgrade**. Like an upgrade, the operating system state will be preserved.

## Options

`--reboot`,`-r`  
Reboot after a successful switch.

`--kexec`,`-k`  
Load new deployment into kexec after a successful switch.

`--os`="STATEROOT"  
Use a different operating system root than the current one.

## Example

**\$ ostree admin switch fedostree/20/workstation/gnome/core**
