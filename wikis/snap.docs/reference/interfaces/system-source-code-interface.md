#  system-source-code interface

`system-source-code`  allows read-only access to  `/usr/src`  on the host system, a directory that typically contains either the headers or the full source code and configuration of the host's Linux kernel

The interface it is not connected automatically because  the interface reveals kernel configuration and patches for the running system, which may or may not correspond to those found in public distro packages.

**Auto-connect** : no

Requires snapd version  *2.46+* .
