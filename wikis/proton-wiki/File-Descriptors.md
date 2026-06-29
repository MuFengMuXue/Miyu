## File Descriptor Limit

Linux kernel has fairly low default limit of [file descriptors](https://en.wikipedia.org/wiki/File_descriptor) that a given process can open - only 4096. Games can use a lot of them for inter-process communication, synchronization primitives and reading assets.

Setting this limit higher is necessary to be able to run a lot of the games out there.

## Systemd-based Linux Distributions

Systemd 240 or newer by default sets the soft limit to 1024 and hard limit to 524288. No action is necessary.

If you want to further alter those values see `DefaultLimitNOFILE` in [`man systemd.conf.d`](https://www.freedesktop.org/software/systemd/man/systemd-system.conf#DefaultLimitCPU=).

## Non-Systemd Linux Distributions With PAM

If your distribution is using [PAM](https://github.com/linux-pam/linux-pam) and has `pam_limits.so` enabled you can configure the limits via [`limits.conf`](https://www.man7.org/linux/man-pages/man5/limits.conf.5.html), e.g `/etc/security/limits.conf`.

```
*               hard    nofile             524288
```

## Everything Else

Please consult documentation of your distributions.