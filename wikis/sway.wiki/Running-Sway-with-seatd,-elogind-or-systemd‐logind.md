Sway makes use of libseat to access seat devices through seatd or (e)logind, allowing sway to run without elevated privileges for input and output device access.

# systemd-logind

systemd-based distros should already have systemd-logind configured.

Running `sway` from an interactive, physical login session should detect and utilize the logind. Default PAM configurations will not allow you to start sway from SSH sessions or similar.

Note that seatd is checked for first, and sway output will contain a message about seatd failing and the next backend being attempted. This is expected and not an error, as indicated by the message.

# elogind

[`elogind`](https://github.com/elogind/elogind) is a project to take systemd's logind and separate it into an external program that can be run without the rest of systemd. The `elogind` service must be started and enabled before use, and the `pam_elogind.so` PAM module appropriately configured.

Running `sway` from an interactive, physical login session should detect and utilize elogind. Default PAM configurations will not allow you to start sway from SSH sessions or similar.

Note that seatd is checked for first, and sway output will contain a message about seatd failing and the next backend being attempted. This is expected and not an error, as indicated by the message.

# seatd

[`seatd`](https://github.com/kennylevinsen/seatd) is a novel and portable seat management service, depending only on libc and working with BSDs just as well as Linux. In order to use `seatd`, install `seatd`, and if your distribution has separate packages for init scripts, `seatd-<init-system>` or equivalent. After that, add the user that needs to launch sway to the `seat` group or equivalent for your distro (with `usermod -aG seat <user>`), and remember to logout in order for this to take effect. The seatd service should be enabled and started.

Running `sway` from anywhere as a user in the appropriate seat group should detect and utilize seatd.

# seatd-launch

If you don't want to enable the seatd service, it's possible to wrap the Sway command line inside `seatd-launch`:

```shell
seatd-launch -- sway
```

This will start a dedicated seatd instance for sway, and will stop seatd when sway exits.