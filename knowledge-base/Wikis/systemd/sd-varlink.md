## Name

sd-varlink — APIs for Varlink IPC

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

`sd-varlink.h` is part of libsystemd(3) and provides APIs for implementing Varlink IPC clients and services. See https://varlink.org/ for more information about Varlink IPC.

Varlink IPC uses JSON as marshalling format. The sd-varlink API relies on the sd-json(3) API for JSON serialization, deserialization and manipulation.

Canonical encoding rules: sd-varlink omits the "`"parameters"`" member on the wire in replies, errors, and notifications when there are no parameters to transmit. This reduces message size and avoids ambiguity. Receivers must be tolerant and accept any of the following encodings for the absence of parameters: an omitted "`"parameters"`" key (preferred), a JSON "`null`" value, or an empty object "`{}`". When decoding, sd-varlink treats JSON "`null`" as if the member was omitted.

The varlinkctl(1) tool makes the functionality implemented by sd-varlink available from the command line.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## Directories

`/usr/lib/systemd/varlink-bridges/`  
When `sd_varlink_connect_url()` encounters a URL with a scheme that is not natively supported, it looks for a bridge helper binary named after the URL scheme in this directory. The binary is invoked the same way as "`exec:`" binaries but with the full URL passed as the first command line argument.

For example, if **varlinkctl introspect https://example.com/ws/sockets/io.systemd.Hostname** is called, **varlinkctl** will look for an executable `/usr/lib/systemd/varlink-bridges/https` and invoke it with "`https://example.com/ws/sockets/io.systemd.Hostname`" as its only argument.

## See Also

systemd(1), sd-event(3), sd-json(3), varlinkctl(1), sd-bus(3), pkg-config(1)
