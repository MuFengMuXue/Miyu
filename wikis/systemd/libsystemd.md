## Name

libsystemd — Functions for implementing services and interacting with systemd

## Synopsis

``` programlisting
#include <systemd/sd-bus.h>
#include <systemd/sd-daemon.h>
#include <systemd/sd-device.h>
#include <systemd/sd-event.h>
#include <systemd/sd-gpt.h>
#include <systemd/sd-hwdb.h>
#include <systemd/sd-id128.h>
#include <systemd/sd-journal.h>
#include <systemd/sd-json.h>
#include <systemd/sd-login.h>
#include <systemd/sd-messages.h>
#include <systemd/sd-path.h>
#include <systemd/sd-varlink.h>
```

`pkg-config --cflags --libs libsystemd`

## Description

The `libsystemd` library provides functions that allow interacting with various interfaces provided by the systemd(1) service manager, as well as various other functions and constants useful for implementing services in general.

See sd-bus(3), sd-bus-errors(3), sd-daemon(3), sd-device(3), sd-event(3), sd-hwdb(3), sd-id128(3), sd-journal(3), sd-json(3), sd-login(3), sd-path(3), and sd-varlink(3) for information about different parts of the library interface.

## Interface stability

Strict backwards-compatibility is maintained for the API (application programming interface) and ABI (application binary interface). Symbol versioning is used, with symbols only added and never removed.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), libudev(3), pkg-config(1), Interface Portability and Stability Promise
