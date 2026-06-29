## Name

sd_varlink_server_new — Allocate Varlink server object

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-varlink.h>
```

|  |  |
|----|----|
| `int `**`sd_varlink_server_new`**`(` | sd_varlink_server\*\* `ret`, |
|   | sd_varlink_server_flags_t `flags``)`; |

 

## Description

`sd_varlink_server_new()` allocates a new Varlink server object. Initially the server does not listen on any socket or file descriptor. The newly allocated server object is returned in the *`ret`* parameter. Use `sd_varlink_server_unref()` to release the server object again after use.

The following flags may be passed in the *`flags`* parameter:

- `SD_VARLINK_SERVER_ROOT_ONLY`: only allow connections from UID 0 (i.e. the root user). This has two effects: any incoming connections is authenticated via `SO_PEERCRED` ensuring the UID reported by the kernel is zero. If this check fails the connection is immediately terminated. Moreover, when binding a socket inode in the file system, the access mode is set to 0600 (rather than 0666). If this option is used connections on non-`AF_UNIX` sockets or via pipes are never permitted.

- `SD_VARLINK_SERVER_MYSELF_ONLY`: this is very similar to `SD_VARLINK_SERVER_ROOT_ONLY` but enforces that the connecting client's UID must match the server's UID (i.e. the UID this function is invoked as). For servers that run as UID 0 the flags are equivalent. If both flags are specified in combination, connections are allowed by both UID 0 and the server's own UID.

- `SD_VARLINK_SERVER_ACCOUNT_UID`: if set connection accounting per client UID is enabled, and a limit on concurrent connections from the same UID is enforced. The limit can be set via `sd_varlink_server_set_connections_per_uid_max()`, and defaults to 3/4th of the total concurrent connection limit, as settable via `sd_varlink_server_set_connections_max()`.

- `SD_VARLINK_SERVER_INHERIT_USERDATA`: if set the user data field for incoming connection (i.e. sd_varlink) objects (as settable via `sd_varlink_set_userdata()`) is automatically set to the userdata field of the server (i.e. sd_varlink_server) object (as settable via `sd_varlink_server_set_userdata()`). If this flag is not specified the connection's user data field will default to `NULL`.

- `SD_VARLINK_SERVER_INPUT_SENSITIVE`: mark all incoming method call parameters as security sensitive (equivalent to calling `sd_json_variant_sensitive()`). This is useful for services that deal with secrets and similar, as it ensures that the parameters are kept out of debug logging, and memory used by the parameters is erased after use.

- `SD_VARLINK_SERVER_ALLOW_FD_PASSING_INPUT`: if set, allow receiving UNIX file descriptors via the connections, equivalent to calling `sd_varlink_set_allow_fd_passing_input()` immediately for each incoming connection. Note that this only has an effect if `AF_UNIX` sockets are used for communication.

- `SD_VARLINK_SERVER_ALLOW_FD_PASSING_OUTPUT`: similar, but controls sending of UNIX file descriptors.

- `SD_VARLINK_SERVER_FD_PASSING_INPUT_STRICT`: this flag can be used in conjunction with `SD_VARLINK_SERVER_ALLOW_FD_PASSING_INPUT`. If so, file descriptor passing is turned off on the listening sockets already, ensuring that the connection sockets derived from it at no time have file descriptor passing enabled. If `SD_VARLINK_SERVER_ALLOW_FD_PASSING_INPUT` is used without `SD_VARLINK_SERVER_FD_PASSING_INPUT_STRICT` then a choice when to prohibit or allow file descriptor passing can still be made after the connection came in, however permitting a time window where file descriptors might already be enqueued, that then need to be dropped again.

- `SD_VARLINK_SERVER_HANDLE_SIGINT`: if set, and `sd_varlink_server_loop_auto()` is used, incoming `SIGINT` process signals will be caught gracefully and cause the event loop to exit cleanly.

- `SD_VARLINK_SERVER_HANDLE_SIGTERM`: similar, but does the same for `SIGTERM`.

## Return Value

On success, `sd_varlink_server_new()` returns a non-negative integer. On failure, it returns a negative errno-style error code.

### Errors

Returned errors may indicate the following problems:

`-EINVAL`  
An argument is invalid.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_varlink_server_new()` was added in version 257.

## See Also

systemd(1), sd-varlink(3)
