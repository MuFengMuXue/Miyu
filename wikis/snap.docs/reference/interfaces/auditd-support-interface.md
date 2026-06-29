#  auditd-support interface

The `auditd-support` interface permits snaps to operate as the [`auditd`](https://www.man7.org/linux/man-pages/man8/auditd.8.html) service on the system.

## Developer details

**[Auto-connect](https://snapcraft.io/docs/explanation/interfaces/interface-auto-connection/)**: no

**[Super-privileged](https://snapcraft.io/docs/explanation/interfaces/super-privileged-interfaces/)**: yes

Unlike other `*-support` interfaces, there is no single official `auditd` snap for which this interface was intended to be used. Instead, snap packagers who wish to ship their own snap containing `auditd` or serving the role of `auditd` may request installation and connection of this interface.

The `auditd-support` interface grants access to the [`CAP_AUDIT_CONTROL` capability](https://www.man7.org/linux/man-pages/man7/capabilities.7.html), along with access to files commonly required by `auditd`.

### Code examples

The test code can be found in the snapd repository:
https://github.com/canonical/snapd/blob/master/interfaces/builtin/auditd_support_test.go

The source code for the interface is in the snapd repository:

https://github.com/canonical/snapd/blob/master/interfaces/builtin/auditd_support.go
