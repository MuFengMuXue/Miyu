## Name

ostree-admin-unlock — Prepare the current deployment for hotfix or development

## Synopsis

`ostree admin unlock` \[OPTIONS...\]

## Description

Remove the read-only bind mount on `/usr` and replace it with a writable overlay filesystem. This default invocation of "unlock" is intended for development/testing purposes. All changes in the overlay are lost on reboot. However, this command also supports "hotfixes", see below.

## Options

`--hotfix`  
If this option is provided, the current deployment will be cloned as a rollback target. This option is intended for things like emergency security updates to userspace components such as `sshd`. The semantics here differ from the default "development" unlock mode in that reboots will retain any changes (which is what you likely want for security hotfixes).

`--transient`  
If this option is provided, the overlay filesystem will be mounted read-only. It can still be affected by remounting it as read/write in a new mount namespace. For example:

``` programlisting
ostree admin unlock --transient
unshare -m -- sh -c 'mount --options-source=disable -o remount,rw /usr && touch /usr/myfile'
```
