# Arch package guidelines/Security

This page describes security packaging guidelines for Arch Linux packages. For C/C++ projects the compiler and linker can apply security hardening options. Arch Linux applies PIE, FORTIFY_SOURCE, stack protector, nx and relro by default.

## Usage
Hardening protections can be reviewed by running .

 $ checksec --file=/usr/bin/cat

## RELRO
RELRO is a generic mitigation technique to harden the data sections of an ELF binary/process. When a program is loaded several ELF memory sections need to be written to by the linker but can be turned read-only before turning control over to the program. This prevents attackers of overriding some ELF sections. There are two different RELRO modes:

* Partial RELRO () some sections are marked as read-only after program load except the GOT () is still writeable.
* Full RELRO () during program load all dynamic symbols are resolved, allowing for the complete GOT to be marked read-only.

If an application reports partial relro, investigate if the build toolchain passes our LDFLAGS or allows overriding LDFLAGS. For Go packages investigate if the build method uses  as pure golang Makefile replacement which does not allow passing of LDFLAGS.

## Haskell
For Haskell it is not clear how to achieve Full RELRO at the moment.

## Go
See Go package guidelines#Flags and build options.

## Stack canary
A stack canary is added by the compiler between the buffer and control data on the stack. If this well known value is corrupted, a buffer overflow occurred and the running program segfaults to prevent possible arbitrary code execution.

The  package has it enabled stack protection by default with the --enable-default-ssp compile option.

## NX
## C/C++
Executable-space protection marks memory regions as non-executable, such that an attempt to execute machine code in these regions will cause an exception. It makes use of hardware features such as the NX bit (no-execute bit), or in some cases software emulation of those features.

## PIE
## C/C++
The  package has it enabled by default for C/C++ with --enable-default-pie.

## Golang
Pass the following flags to :

 export GOFLAGS='-buildmode=pie'
 export CGO_CPPFLAGS="-D_FORTIFY_SOURCE=3"
 export CGO_LDFLAGS="-Wl,-z,relro,-z,now"

## Haskell
Pass the following flag to :

 --ghc-option='-pie'

## RPATH/RUNPATH
RUNPATH/RPATH provides further search paths for the object it is listed in (it can be used both for executable and for shared objects).

 $ objdump -x /usr/bin/perl | grep -E 'RPATH|RUNPATH'

If the RPATH value contains a path within an attackers control it can possibly execute code by installing a malicious library in that directory for example CVE-2006-1566 CVE-2005-4280. See Debian:RpathIssue.

The RPATH entry is set by the linker by passing for example the following string to LDFLAGS . To make an RUNPATH entry append  to the linker flags.

## FORTIFY
Fortify source is a macro that adds buffer overflow protection in various functions that perform operations on memory and strings. It checks whether an attacker tries to copy more bytes to overflow a buffer and then stops the execution of the program. This protection is enabled with the default :

See makepkg#Configuration.

## systemd services
If a systemd service file is shipped with the package due to upstream not providing any, look into applying the following systemd service hardening features. Systemd provides a way to analyse security features which are enabled for a service.

 $ systemd-analyze security reflector.service

## File access
A service can be hardened by restricting file system access.

Set up a new file system namespace for the executed process and mounts private  and  directories inside it that is not shared by processes outside the namespace. Useful for programs which write data to .

 PrivateTmp=true

ProtectSystem has three different varieties of mounting directories as read-only for the executed process. The "full" option mounts ,  and  read only. ProtectHome makes ,  and  inaccessible to the executed process.

 ProtectSystem=strict
 ProtectHome=true

Sets up a new  namespace for the executed process and only adds API pseudo devices such as ,  or , but not for physical devices or system memory, system ports and others. This is useful to secure the execute process from writing directly to physical devices, systemd also adds a system call filter for calls within the  set.

 PrivateDevices=true

These options make the executed process unable to change kernel variables accessible through , , etc. ProtectControlGroups makes the  hierarchy read-only.

 ProtectKernelTunables=true
 ProtectControlGroups=true

Making file paths inaccessible can be done as following:

 InaccessiblePaths=/etc

More detailed information can be found in .

## User
Ensure that the executed process and its children can never gain new privileges through .

 NoNewPrivileges=true

## Memory
Prohibit attempts to create memory mappings that are both writable and executable, to change mappings to be executable or to create executable shared memory. This sandboxes a process against allowing an attacker to write in to memory which is also executed. Note that enabling this is not compatible with all applications which rely on a JIT.

 MemoryDenyWriteExecute=true

## System calls
Locks down the  system call so that the kernel execution domain can not be changed.

 LockPersonality=true

System calls can be restricted in a service as well, systemd can display syscalls to filter on:

 $ systemd-analyze syscall-filter

Predefined groups are available, e.g. to use the recommended starting point for whitelisting system calls for system services use:

 SystemCallFilter=@system-service

System calls can be restricted by their architecture such as to prevent 32-bit binaries from executing on 64-bit machines (no non-native binaries):

 SystemCallArchitectures=native

## Network
If the running process does not require any network access it can be fully disabled by setting up a new network namespace for the process and only configuration a loopback interface.

 PrivateNetwork=true

If network is required, the type of address families used can be restricted for the  system call by for example only allowing UNIX sockets.

 RestrictAddressFamilies=AF_UNIX

For when only network to localhost or specific IP ranges is required a process can be restricted by only allowing network access to localhost.

 IPAddressAllow=localhost
 IPAddressDeny=any

More information about network filtering can be found in .

## Various
Sets up a new UTS namespace for the execute process and disallows changing the hostname or domainname.

 ProtectHostname=true
