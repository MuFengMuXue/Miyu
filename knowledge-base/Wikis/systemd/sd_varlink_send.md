## Name

sd_varlink_send, sd_varlink_sendb, sd_varlink_sendbo — Enqueues a Varlink method call, not expecting a reply

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

|                                |                                    |
|--------------------------------|------------------------------------|
| `int `**`sd_varlink_send`**`(` | sd_varlink \*`link`,               |
|                                | const char \*`method`,             |
|                                | sd_json_variant \*`parameters``)`; |

 

|                                 |                        |
|---------------------------------|------------------------|
| `int `**`sd_varlink_sendb`**`(` | sd_varlink \*`link`,   |
|                                 | const char \*`method`, |
|                                 | …`)`;                  |

 

|                                  |                        |
|----------------------------------|------------------------|
| `int `**`sd_varlink_sendbo`**`(` | sd_varlink \*`link`,   |
|                                  | const char \*`method`, |
|                                  | …`)`;                  |

 

## Description

`sd_varlink_send()` submits a method call via a Varlink connection. It takes the Varlink connection object, a method name as string parameter, and a JSON object containing the parameters to pass as function parameters. This call is asynchronous: the message will not be delivered immediately but only once sd_varlink_process(3) is invoked (which will happen automatically in one of the following event loop iterations if the Varlink connection is attached to an even loop).

`sd_varlink_sendb()` is similar to `sd_varlink_send()`, but instead of expecting a fully constructed sd_json_variant object carrying the parameters, this object is constructed on-the-fly directly from the parameter list, in a style identical to sd_json_build(3).

`sd_varlink_sendbo()` is identical to `sd_varlink_sendb()`, but an enclosing object is implicitly added, so that the parameter list is expected to consist of field pairs only. For details about the expected argument list, see sd_json_buildo(3).

Use `sd_varlink_send()`, `sd_varlink_sendb()` and `sd_varlink_sendbo()` only if no method call results are required, as they neither provide return parameters nor success/failure information. Use sd_varlink_call(3) (and related calls) to submit a method call synchronously, returning the server's response.

## Return Value

On success, `sd_varlink_send()`, `sd_varlink_sendb()` and `sd_varlink_sendbo()` return a non-negative integer. On failure, they return a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

`-ENOMEM`  
Memory allocation failed.

`-ENOTCONN`  
The Varlink connection object is not connected.

`-EBUSY`  
The Varlink connection object is already used for other purposes, i.e. executing a method call or similar.

`-ENOBUFS`  
The internal limit of queued messages for the Varlink connection has been reached. This limit is set very high, and hitting it typically indicates that the Varlink connection object is stalled — possibly because `sd_varlink_process()` has not been called regularly enough, or because the peer is not processing any queued messages. This limit is a safety precaution to ensure a stalled peer will not result in unbounded memory allocations on the client side.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_varlink_send()`, `sd_varlink_sendb()`, `sd_varlink_sendbo()` were added in version 257.

## See Also

systemd(1), sd-varlink(3), sd_varlink_call(3), sd_varlink_build(3)
