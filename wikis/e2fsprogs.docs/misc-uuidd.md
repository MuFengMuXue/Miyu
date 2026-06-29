# NAME

uuidd - UUID generation daemon

# SYNOPSIS

**uuidd** \[ **-d** \] \[ **-p** *pidfile* \] \[ **-s** *socketpath* \] \[ **-T** *timeout* \]

**uuidd** \[ **-r** \| **-t** \] \[ **-n** *number* \] \[ **-s** *socketpath* \]

**uuidd -k**

# DESCRIPTION

The **uuidd** daemon is used by the UUID library to generate universally unique identifiers (UUIDs), especially time-based UUID's in a secure and guaranteed-unique fashion, even in the face of large numbers of threads trying to grab UUID's running on different CPU's.

# OPTIONS

**-d**
Run **uuidd** in debugging mode. This prevents uuidd from running as a daemon.

**-k**
If a currently uuidd daemon is running, kill it.

**-n*** number*
When issuing a test request to a running uuidd, request a bulk response of *number* UUID's.

**-p*** pidfile*
Specify the pathname where the pid file should be written. By default, the pid file is written to /var/lib/libuuid/uuidd.pid.

**-s*** socketpath*
Specify the pathname used for the unix-domain socket used by uuidd. By default, the pathname used is /var/lib/libuuid/request. This is primarily for debugging purposes, since the pathname is hard-coded in the libuuid library.

**-r**
Test uuidd by trying to connect to a running uuidd daemon and request it to return a random-based UUID.

**-t**
Test uuidd by trying to connect to a running uuidd daemon and request it to return a time-based UUID.

**-T*** timeout*
Specify a timeout for uuidd. If specified, then uuidd will exit after *timeout* seconds of inactivity.

# AUTHOR

The **uuidd** daemon was written by Theodore Ts'o \<tytso@mit.edu\>.

# AVAILABILITY

**uuidd** is part of libuuid from the e2fsprogs package and is available from http://e2fsprogs.sourceforge.net.

# SEE ALSO

**libuuid**(3), **uuidgen**(1)
