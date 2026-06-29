## Name

sd_bus_message_dump, sd_bus_message_dump_json — Produce a string representation of a message for debugging purposes

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                            |                       |
|----------------------------|-----------------------|
| `int sd_bus_message_dump(` | sd_bus_message \*`m`, |
|                            | FILE \*`f`,           |
|                            | uint64_t `flags``)`;  |

 

|                                 |                               |
|---------------------------------|-------------------------------|
| `int sd_bus_message_dump_json(` | sd_bus_message \*`m`,         |
|                                 | uint64_t `flags`,             |
|                                 | sd_json_variant \*\*`ret``)`; |

 

## Description

The `sd_bus_message_dump()` function writes a textual representation of the message *`m`* to the stream *`f`*. If *`f`* is `NULL`, standard output (`stdio`) will be used. This function is intended to be used for debugging purposes, and the output is neither stable nor designed to be machine readable.

The `sd_bus_message_dump_json()` function converts the DBus message *`m`* to a JSON variant and stores it in *`ret`*. The caller should call `sd_json_variant_unref()` for the acquired JSON variant after use. Unlike `sd_bus_message_dump()`, the function itself does not print anything. To print the DBus message in the JSON format, please pass the returned JSON variant to `sd_json_variant_dump()`.

The *`flags`* parameter may be used to modify the output, and is a combination of zero or more of the following flags:

`SD_BUS_MESSAGE_DUMP_WITH_HEADER`  
The header of the message that specifies the message type, flags, and several more additional metadata will be printed or included in the resulting JSON object.

`SD_BUS_MESSAGE_DUMP_SUBTREE_ONLY`  
Only the current container will be printed or converted. When the flag is *not* specified, the contents of the whole message will be printed or converted.

Note that these functions move the read pointer of the message. It may be necessary to reset the position afterwards, for example with sd_bus_message_rewind(3).

## Examples

Output for a signal message (with `SD_BUS_MESSAGE_DUMP_WITH_HEADER`):

``` programlisting
‣ Type=signal  Endian=l  Flags=1  Version=1  Cookie=22
  Path=/value/a  Interface=org.freedesktop.DBus.Properties  Member=PropertiesChanged
  MESSAGE "sa{sv}as" {
          STRING "org.freedesktop.systemd.ValueTest";
          ARRAY "{sv}" {
                  DICT_ENTRY "sv" {
                          STRING "Value";
                          VARIANT "s" {
                                  STRING "object 0x1e, path /value/a";
                          };
                  };
          };
          ARRAY "s" {
                  STRING "Value2";
                  STRING "AnExplicitProperty";
          };
  };
```

## Return Value

On success, this function returns 0 or a positive integer. On failure, it returns a negative errno-style error code. No error codes are currently defined.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-bus(3), sd-json(3)
