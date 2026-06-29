## Name

systemd-quotacheck@.service, systemd-quotacheck-root.service, systemd-quotacheck — File system quota checker logic

## Synopsis

`systemd-quotacheck@.service`

`systemd-quotacheck-root.service`

`/usr/lib/systemd/systemd-quotacheck`

## Description

`systemd-quotacheck@.service` and `systemd-quotacheck-root.service` are services responsible for file system quota checks. They run once at boot after all necessary file systems are mounted. They are pulled in only if at least one file system has quotas enabled.

## Kernel Command Line

`systemd-quotacheck` understands one kernel command line parameter:

`quotacheck.mode=`  
One of "`auto`", "`force`", "`skip`". Controls the mode of operation. The default is "`auto`", and ensures that file system quota checks are done when the file system quota checker deems them necessary. "`force`" unconditionally results in full file system quota checks. "`skip`" skips any file system quota checks.

Added in version 186.

## Credentials

**systemd-quotacheck** supports the service credentials logic as implemented by `ImportCredential=`/`LoadCredential=`/`SetCredential=` (see systemd.exec(5) for details). The following credentials are used when passed in:

`quotacheck.mode`  
The contents of the credential is parsed as same as the kernel command line option with the same name. See above for more details.

Added in version 258.

Note that by default the `systemd-quotacheck@.service` and `systemd-quotacheck-root.service` unit files are set up to inherit `quotacheck.mode` credential from the service manager.

## See Also

systemd(1), quotacheck(8), systemd-fsck@.service(8)
