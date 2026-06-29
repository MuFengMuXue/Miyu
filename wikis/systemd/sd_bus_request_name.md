## Name

sd_bus_request_name, sd_bus_request_name_async, sd_bus_release_name, sd_bus_release_name_async — Request or release a well-known service name on a bus

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|  |  |
|----|----|
| `typedef int (*`**`sd_bus_message_handler_t`**`)(` | sd_bus_message \*`m`, |
|   | void \*`userdata`, |
|   | sd_bus_error \*`ret_error``)`; |

 

|                                    |                      |
|------------------------------------|----------------------|
| `int `**`sd_bus_request_name`**`(` | sd_bus \*`bus`,      |
|                                    | const char \*`name`, |
|                                    | uint64_t `flags``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_request_name_async`**`(` | sd_bus \*`bus`, |
|   | sd_bus_slot \*\*`slot`, |
|   | const char \*`name`, |
|   | uint64_t `flags`, |
|   | sd_bus_message_handler_t `callback`, |
|   | void \*`userdata``)`; |

 

|                                    |                         |
|------------------------------------|-------------------------|
| `int `**`sd_bus_release_name`**`(` | sd_bus \*`bus`,         |
|                                    | const char \*`name``)`; |

 

|  |  |
|----|----|
| `int `**`sd_bus_release_name_async`**`(` | sd_bus \*`bus`, |
|   | sd_bus_slot \*\*`slot`, |
|   | const char \*`name`, |
|   | sd_bus_message_handler_t `callback`, |
|   | void \*`userdata``)`; |

 

## Description

`sd_bus_request_name()` requests a well-known service name on a bus. It takes a bus connection, a valid bus name, and a flags parameter. The flags parameter is a combination of zero or more of the following flags:

`SD_BUS_NAME_ALLOW_REPLACEMENT`  
After acquiring the name successfully, permit other peers to take over the name when they try to acquire it with the `SD_BUS_NAME_REPLACE_EXISTING` flag set. If `SD_BUS_NAME_ALLOW_REPLACEMENT` is not set on the original request, such a request by other peers will be denied.

Added in version 209.

`SD_BUS_NAME_REPLACE_EXISTING`  
Take over the name if it was already acquired by another peer, and that other peer has permitted takeover by setting `SD_BUS_NAME_ALLOW_REPLACEMENT` while acquiring it.

Added in version 209.

`SD_BUS_NAME_QUEUE`  
Queue the acquisition of the name when the name is already taken.

Added in version 209.

`sd_bus_request_name()` operates in a synchronous fashion: a message requesting the name is sent to the bus broker, and the call waits until the broker responds.

`sd_bus_request_name_async()` is an asynchronous version of `sd_bus_request_name()`. Instead of waiting for the request to complete, the request message is enqueued. The specified *`callback`* will be called when the broker's response is received. If the parameter is specified as `NULL` a default implementation is used instead which will terminate the connection when the name cannot be acquired. The function returns a slot object in its *`slot`* parameter — if it is passed as non-`NULL` — which may be used as a reference to the name request operation. Use sd_bus_slot_unref(3) to destroy this reference. Note that destroying the reference will not unregister the name, but simply ensure the specified callback is no longer called.

`sd_bus_release_name()` releases an acquired well-known name. It takes a bus connection and a valid bus name as parameters. This function operates synchronously, sending a release request message to the bus broker and waiting for it to reply.

`sd_bus_release_name_async()` is an asynchronous version of `sd_bus_release_name()`. The specified *`callback`* function is called when the name has been released successfully. If specified as `NULL` a generic implementation is used that ignores the result of the operation. As above, the *`slot`* (if non-`NULL`) is set to an object that may be used to reference the operation.

These functions are supported only on bus connections, i.e. connections to a bus broker and not on direct connections.

## Return Value

On success, these calls return 0 or a positive integer. On failure, these calls return a negative errno-style error code.

If `SD_BUS_NAME_QUEUE` is specified, `sd_bus_request_name()` will return 0 when the name is already taken by another peer and the client has been added to the queue for the name. In that case, the caller can subscribe to "`NameOwnerChanged`" signals to be notified when the name is successfully acquired. `sd_bus_request_name()` returns \> 0 when the name has immediately been acquired successfully.

### Errors

Returned errors may indicate the following problems:

`-EALREADY`  
The caller already is the owner of the specified name.

`-EEXIST`  
The name has already been acquired by a different peer, and SD_BUS_NAME_REPLACE_EXISTING was not specified or the other peer did not specify SD_BUS_NAME_ALLOW_REPLACEMENT while acquiring the name.

`-ESRCH`  
It was attempted to release a name that is currently not registered on the bus.

`-EADDRINUSE`  
It was attempted to release a name that is owned by a different peer on the bus.

`-EINVAL`  
A specified parameter is invalid. This is also generated when the requested name is a special service name reserved by the D-Bus specification, or when the operation is requested on a connection that does not refer to a bus.

`-ENOTCONN`  
The bus connection has been disconnected.

`-ECHILD`  
The bus connection has been created in a different process than the current one.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_bus_request_name()` and `sd_bus_release_name()` were added in version 209.

`sd_bus_request_name_async()` and `sd_bus_release_name_async()` were added in version 237.

## See Also

systemd(1), sd-bus(3), sd_bus_new(3), sd_bus_slot_unref(3)
