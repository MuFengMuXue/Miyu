## Name

hostname — Local hostname configuration file

## Synopsis

`/etc/hostname`

## Description

The `/etc/hostname` file configures the name of the local system. Unless overridden as described in the next section, systemd(1) will set this hostname during boot using the sethostname(2) system call.

The file should contain a single newline-terminated hostname string. Comments (lines starting with a "`#`") are ignored. The hostname should be composed of up to 64 7-bit ASCII lower-case alphanumeric characters or hyphens forming a valid DNS domain name. It is strongly recommended that this name contains only a single DNS label, i.e does not contain any dots. This recommendation reflects both usual expectations of applications, and the fact that the Linux kernel limits the length of the system hostname to 64 (i.e. close to the maximum DNS label length of 63) rather than 255 (the maximum DNS domain name length). When applied, invalid characters will be filtered out in an attempt to make the name valid, but obviously it is recommended to use a valid name and not rely on this filtering.

If the question mark character "`?`" appears in the hostname, it is automatically substituted by a hexadecimal character derived from the machine-id(5) when applied, securely and deterministically by cryptographic hashing. Example: "`foobar-????-????`" will automatically expand to "`foobar-92a9-061c`" or similar, depending on the local machine ID.

You may use hostnamectl(1) to change the value of this file during runtime from the command line. Use systemd-firstboot(1) to initialize it on mounted (but not booted) system images.

## Hostname semantics

systemd(1) and the associated tools will obtain the hostname in the following ways:

- If the kernel command line parameter `systemd.hostname=` specifies a valid hostname, systemd(1) will use it to set the hostname during early boot, see kernel-command-line(7),

- Otherwise, the "static" hostname specified by `/etc/hostname` as described above will be used.

- Otherwise, a transient hostname may be set during runtime, for example based on information in a DHCP lease, see systemd-hostnamed.service(8). Both NetworkManager and systemd-networkd.service(8) allow this. Note that systemd-hostnamed.service(8) gives higher priority to the static hostname, so the transient hostname will only be used if the static hostname is not configured.

- Otherwise, a fallback hostname configured at compilation time will be used ("`localhost`").

Effectively, the static hostname has higher priority than a transient hostname, which has higher priority than the fallback hostname. Transient hostnames are equivalent, so setting a new transient hostname causes the previous transient hostname to be forgotten. The hostname specified on the kernel command line is like a transient hostname, with the exception that it has higher priority when the machine boots. Also note that those are the semantics implemented by systemd tools, but other programs may also set the hostname.

## History

The simple configuration file format of `/etc/hostname` originates from Debian GNU/Linux.

## See Also

systemd(1), sethostname(2), hostname(1), hostname(7), machine-id(5), machine-info(5), hostnamectl(1), systemd-hostnamed.service(8), systemd-firstboot(1)
