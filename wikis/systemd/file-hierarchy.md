## Name

file-hierarchy — systemd file system hierarchy requirements

## Description

Operating systems using the systemd(1) system and service manager are organized based on a file system hierarchy inspired by UNIX, as described in UAPI.9 Linux File System Hierarchy. Additional requirements on *when* given parts of the hierarchy must be available during boot are listed in Mount Requirements.

Many of the paths described here can be queried with the systemd-path(1) tool.

## See Also

|                                  |
|----------------------------------|
| hier(7)                          |
| File System Hierarchy            |
| XDG Base Directory Specification |
| XDG User Directories             |
