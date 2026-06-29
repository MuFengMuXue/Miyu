** Warning**\
Unrelated to glibc [#681586](https://bugs.gentoo.org/681586)

** Note**\
This is a single report; so far nobody else has observed it.

The usual [[[sys-libs/glibc]](https://packages.gentoo.org/packages/sys-libs/glibc)[]] upgrade procedure is to update [\@world], then use [[[app-admin/restart-services]](https://packages.gentoo.org/packages/app-admin/restart-services)[]] to restart daemons with changed libraries (most after a glibc update) and then a reboot (does not have to follow immediately). Since my distfiles are on glusterfs, an umount/mount is needed after the glibc update to reload libraries.

`root `[`#`]`emerge -uDNva1 @world `

`root `[`#`]`umount /usr/portage/distfiles `

`root `[`#`]`mount /usr/portage/distfiles `

`root `[`#`]`restart-services `

Prepare for the reboot, update kernel if necessary\...

`root `[`#`]`reboot`

With glibc 2.28 this caused sshd crashes on several machines. Even the [umount /usr/portage/distfiles] command terminated my ssh connection. It\'s probably a good idea to have [[[app-admin/monit]](https://packages.gentoo.org/packages/app-admin/monit)[]] installed to automatically restart sshd after a crash.

Because of that, this procedure seems to work better for glibc 2.28:

`root `[`#`]`emerge -uDNva1 @world --exclude sys-libs/glibc`

Prepare everything for the reboot, including kernel update if necessary

`root `[`#`]`emerge -av1 sys-libs/glibc`

`root `[`#`]`reboot`

## [It continues even after reboot]

This has worked fine for some time, but a week after this happened again on multiple machines. Rebuilding/upgrading to glusterfs 6.0 didn\'t help either. It\'s not reproducible on all machines.

It can be triggered by:

`root `[`#`]`mount /usr/portage/distfiles `

`root `[`#`]`emerge -ev1 sys-cluster/glusterfs `

`root `[`#`]`restart-services `

`root `[`#`]`umount /usr/portage/distfiles `