## Name

systemd-hibernate-resume.service, systemd-hibernate-clear.service, systemd-hibernate-resume — Resume from hibernation

## Synopsis

`systemd-hibernate-resume.service`

`systemd-hibernate-clear.service`

`/usr/lib/systemd/systemd-hibernate-resume`

## Description

`systemd-hibernate-resume.service` initiates the resume from hibernation.

**systemd-hibernate-resume** only supports the in-kernel hibernation implementation, see Swap suspend. Internally, it works by writing the major:minor of selected device node to `/sys/power/resume`, along with the offset in memory pages (`/sys/power/resume_offset`) if supported.

The resume device node is either passed directly through arguments, or automatically acquired from kernel command line options and/or `HibernateLocation` EFI variable. The latter will normally be cleared by `systemd-hibernate-resume.service` on resumption. If a stale variable is detected, it would be cleared by `systemd-hibernate-clear.service`.

Failing to initiate a resume is not an error condition. It may mean that there was no resume image (e. g. if the system has been simply powered off and not hibernated). In such cases, the boot is ordinarily continued.

## See Also

systemd(1), systemd-hibernate-resume-generator(8)
