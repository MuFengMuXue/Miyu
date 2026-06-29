## Name

sd_bus_reply_method_error, sd_bus_reply_method_errorf, sd_bus_reply_method_errorfv, sd_bus_reply_method_errno, sd_bus_reply_method_errnof, sd_bus_reply_method_errnofv — Reply with an error to a D-Bus method call

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

|                                  |                              |
|----------------------------------|------------------------------|
| `int sd_bus_reply_method_error(` | sd_bus_message \*`call`,     |
|                                  | const sd_bus_error \*`e``)`; |

 

|                                   |                          |
|-----------------------------------|--------------------------|
| `int sd_bus_reply_method_errorf(` | sd_bus_message \*`call`, |
|                                   | const char \*`name`,     |
|                                   | const char \*`format`,   |
|                                   | ...`)`;                  |

 

|                                    |                          |
|------------------------------------|--------------------------|
| `int sd_bus_reply_method_errorfv(` | sd_bus_message \*`call`, |
|                                    | const char \*`name`,     |
|                                    | const char \*`format`,   |
|                                    | va_list `ap``)`;         |

 

|                                  |                              |
|----------------------------------|------------------------------|
| `int sd_bus_reply_method_errno(` | sd_bus_message \*`call`,     |
|                                  | int `error`,                 |
|                                  | const sd_bus_error \*`p``)`; |

 

|                                   |                          |
|-----------------------------------|--------------------------|
| `int sd_bus_reply_method_errnof(` | sd_bus_message \*`call`, |
|                                   | int `error`,             |
|                                   | const char \*`format`,   |
|                                   | ...`)`;                  |

 

|                                    |                          |
|------------------------------------|--------------------------|
| `int sd_bus_reply_method_errnofv(` | sd_bus_message \*`call`, |
|                                    | int `error`,             |
|                                    | const char \*`format`,   |
|                                    | va_list `ap``)`;         |

 

## Description

The `sd_bus_reply_method_error()` function sends an error reply to the *`call`* message. The error structure *`e`* specifies the error to send, and is used as described in sd_bus_message_new_method_error(3). If no reply is expected to *`call`*, this function succeeds without sending a reply.

The `sd_bus_reply_method_errorf()` is to `sd_bus_reply_method_error()` what `sd_bus_message_new_method_errorf()` is to `sd_bus_message_new_method_error()`.

The `sd_bus_reply_method_errno()` is to `sd_bus_reply_method_error()` what `sd_bus_message_new_method_errno()` is to `sd_bus_message_new_method_error()`.

The `sd_bus_reply_method_errnof()` is to `sd_bus_reply_method_error()` what `sd_bus_message_new_method_errnof()` is to `sd_bus_message_new_method_error()`.

## Return Value

This function returns a non-negative integer if the error reply was successfully sent or if *`call`* does not expect a reply. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
The input parameter *`call`* is `NULL`.

Message *`call`* is not a method call message.

Message *`call`* is not attached to a bus.

The error parameter *`e`* to `sd_bus_reply_method_error()` is not set, see sd_bus_error_is_set(3).

`-EPERM`  
Message *`call`* has been sealed.

`-ENOTCONN`  
The bus to which message *`call`* is attached is not connected.

`-ENOMEM`  
Memory allocation failed.

In addition, any error returned by sd_bus_send(3) may be returned.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), sd-bus(3), sd_bus_message_new_method_error(3)
