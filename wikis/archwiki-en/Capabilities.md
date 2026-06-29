# Capabilities

Capabilities (POSIX 1003.1e, ) provide fine-grained control over superuser permissions, allowing use of the root user to be avoided. Software developers are encouraged to replace uses of the powerful setuid attribute in a system binary with a more minimal set of capabilities. Many packages make use of capabilities, such as  being used for . This enables  to be run by a normal user (as with the setuid method), while at the same time limiting the security consequences of a potential vulnerability in .

## Implementation
Capabilities are implemented on Linux using extended attributes () in the security namespace. Extended attributes are supported by all major Linux file systems, including Ext2, Ext3, Ext4, Btrfs, JFS, XFS, and Reiserfs. The following example prints the capabilities of fping with , and then prints the same data in its encoded form using :

Some programs copy extended attributes automatically, while others require a special flag. Examples for both classes are at extended attributes#Preserving extended attributes.

Capabilities are set by package install scripts on Arch, e.g. fping.install.

## Administration and maintenance
It is considered a bug if a package has overly permissive capabilities, so these cases should be reported rather than listed here. A capability essentially equivalent to root access () or trivially allowing root access () does not count as a bug since Arch does not support any MAC/RBAC systems.

## Other programs that benefit from capabilities
The following packages do not have files with the setuid attribute but require root privileges to work. By enabling some capabilities, regular users can use the program without privilege elevation.

The  behind the capabilities indicate the capability sets effective and permitted, more information can be found at .

{| class=wikitable
! program || Command (run as root)
|-
| Beep ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|-
|  ||
|}

Some packaged binaries, like , are already configured with needed capabilities via  files. There is no need to add capabilities manually as described above.

## Useful commands
Find setuid-root files:

 $ find /usr/bin /usr/lib -perm /4000 -user root

Find setgid-root files:

 $ find /usr/bin /usr/lib -perm /2000 -group root

## Running a program with temporary capabilities
Using  it is possible to run a program with some specific capabilities without modifying the extended attributes of the binary. The following example shows how to attach to a process using GDB using the  capability:

 $ sudo -E capsh --caps="cap_setpcap,cap_setuid,cap_setgid+ep cap_sys_ptrace+eip" --keep=1 --user="$USER" --addamb="cap_sys_ptrace" --shell=/usr/bin/gdb -- -p

The  is supplied to  above to pass the current user's login environment, e.g., the  variable and so on, to the child process(es).

An example of binding to a low port using netcat, in this case 123:

 $ sudo -E capsh --caps="cap_setpcap,cap_setuid,cap_setgid+ep cap_net_bind_service+eip" --keep=1 --user="$USER" --addamb="cap_net_bind_service" --shell=/usr/bin/nc -- -lvtn 123
 Listening on 0.0.0.0 123

Both of the above examples are really just for illustrative purposes, as (on most systems) you would be able to attach debugger to a process owned by any user, or open a port < 1024 as the root user, regardless. The use of  may provide some security benefits, though, as  runs as the named user, with all the normal kernel capabilities (i.e., restrictions) in place.

## systemd
Using  and , it is possible to assign capabilities to systemd units, which is much more safe than setting capabilities on binaries. See .
