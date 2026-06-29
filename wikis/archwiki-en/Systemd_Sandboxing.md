# Systemd/Sandboxing

systemd enables users to harden and sandbox system service units. Because of technical limitations, and ironically security reasons, user units can not be hardened or sandboxed properly since this would make privilege escalation issues possible. This does not affect system units which use the  directive.

Because of the nature of other unit types, only service units can be hardened/sandboxed in the traditional sense. See  and  for more information.

## General
Since hardening/sandboxing effectively restricts an application, it is not possible to use all the sandboxing directives. A web server for example should not use  since it usually needs network access.

 generates a score for the unit showing all the used directives, which can be helpful to determine what settings to try next.

Unfortunately, systemd's error messages on misconfiguration relating to sandboxing are sometimes vague and/or misleading. Setting the log level temporarily to  may help getting actually relevant information.

 # systemctl log-level debug

## Capabilities
 are used to grant a process certain elevated privileges. For example,  can be used so that an otherwise unprivileged process can bind ports below 1024, eliminating the need for it to start with root privileges at all. Another notable example is  to grant a backup program unrestricted read access to all locations.

In service units, you can accomplish this by using  to grant it capabilities and  to ensure nothing beyond the intended scope is granted:

## Common directives
Most of these directives can be applied to most applications without causing too many problems.

## Without special configuration
Simple boolean settings which can either be enabled or not. They can not be configured.

{| class="wikitable"
! Directive !! Impact1 !! Breakage2 !! Notes
|-
|  ||  ||  ||
|-
|  ||  ||  || Incompatible with dynamically generated code at runtime, including JIT, executable stacks, C compiler code "trampoline". Can be enhanced with .
|-
|  ||  ||  ||
|-
|  ||  ||  ||  and similar will still be there.
|-
|  ||  ||  || Disallows any network access.
|-
|  ||  ||  ||
|-
|  ||  ||  ||
|-
|  ||  ||  || May prevent denial-of-service situations.
|-
|  ||  ||  || Best used with .
|}

# How effective the directive is
# How likely the directive is to break something

## Configurable directives
Most of these directives are quite powerful and will affect a lot. It is recommended to consider using at least some of them.

{| class="wikitable"
! Directive !! Value !! Impact1 !! Breakage2 !! Notes
|-
| rowspan="3"|  ||  ||  ||  || Usually used with
|-
|  ||  ||  || May break e.g web servers using ACME to renew their own keys which may be in
|-
|  ||  ||  || There are in theory few applications which write to  and
|-
| rowspan="3"|  ||  ||  ||  || Some applications may need persistent data stored in 3
|-
|  ||  ||  || Home directories contain a lot of sensitive data and using either  or  may prevent leaks.4
|-
|  ||  ||  || Ideal for backup services
|-
| rowspan="2"| 5 ||  ||  ||  ||
|-
|  ||  ||  ||
|-
|  || e.g  ||  ||  || Takes a space-separated list of address families, .
|}

# How effective the directive is
# How likely the directive is to break something
#  can be used to mitigate some of the negative consequences
# This also makes  inaccessible, preventing leakage using IPC sockets. In theory, there may also be sockets elsewhere, e.g .
# Defaults to the hidepid value of the  mount when directive is omitted, which is usually  (unrestricted)

## Advanced directives
These directives are not useful for most units and are thus used more rarely.

{| class="wikitable"
! Directive !! Value !! Impact !! Breakage !! Notes
|-
|  || Boolean, e.g  ||  ||  || Needs to be combined with , , ,  and .|-
| 1,2 || Boolean ||  ||  || Some users reported  can not run when this is set, but this should be relatively safe.
|-
| 1 || Boolean ||  ||  ||
|-
| 1,2 || Boolean ||  ||  ||
|-
| 1 || Boolean ||  ||  || All official kernels have  set to , but this is still defense in depth.
|-
| 1 || Boolean ||  ||  ||
|-
| 1 || Boolean ||  ||  ||
|-
|  || e.g  ||  ||  || Takes a space-separated list of file systems or a set, e.g . See  for a full list.
|-
|  || e.g  ||  ||  || See also #Disabling non-native syscalls - prefer using this to opt out a unit from the system default instead.
|-
|  || e.g  ||  ||  || See  - forgetting just a single syscall will lead to your application segfaulting at possibly inopportune times.
|-
|  || e.g   ||  ||  || Best combined with  to ensure the privileged context can only bind to desired ports.
|}

# Redundant and unnecessary to specify if the service unit does not run with elevated privileges resulting from use of e.g  or running as root. If a service unit is running as another normal and unprivileged , these settings are entirely superfluous and can be safely omitted.
# Restricts issuing corresponding syscalls only, but not access to IPC services shipped by systemd (namely systemd-timedated and systemd-hostnamed).[https://github.com/systemd/systemd/pull/35447#issuecomment-2512361567 Care must be taken to block the D-Bus/Varlink methods involved if absolute security is demanded.

## chroot jail
It is possible to severely restrict what a process can see by specifying  and mounting required paths into this chroot-like jail.
 requires a directory to be present, whereas  does not and will override  seamlessly. Both, and especially the latter, appear to be secure chroot-like directives, which can not be broken out easily, as they do not use the  syscall.

All required paths must be mounted into this jail via  and :

This is a minimal example and most application will need more paths whitelisted. Some common paths include:

* ,
*
*
* Any sockets you need, e.g

It will be likely that debugging is at some point necessary when trying to sandbox a unit for the first time. If a unit can not be started at all and fails with , either the executable itself or required libraries are not accessible. Starting with broad paths at first (e.g allowing the entirety of ) and narrowing it down later can help, too.

## system.conf
Changes to  are global, so they will affect every unit. See

## Disabling non-native syscalls
Non-native binaries, in almost all cases 32-bit binaries, may partially compromise the security of the system because they do not have access to more hardening. There have been some relatively minor vulnerabilities, like CVE-2009-0835, which affected non-native syscalls.

This works well on most systems, but it needs to be at least partially disabled if e.g multilib is in use. Especially gaming with Wine may be impacted. Using  or modifying the session slice to override  can be used to disable restrictions partially.

## Enabling more unit statistics
systemd does not track all resource usage of a unit by default. Enable  to get more statistics in the  output and the journal. This is not strictly a security setting, but it will certainly make debugging easier and can provide useful insights into resource usage.
