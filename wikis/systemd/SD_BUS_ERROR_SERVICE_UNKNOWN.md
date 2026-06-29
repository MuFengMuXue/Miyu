## Name

sd-bus-errors, SD_BUS_ERROR_FAILED, SD_BUS_ERROR_NO_MEMORY, SD_BUS_ERROR_SERVICE_UNKNOWN, SD_BUS_ERROR_NAME_HAS_NO_OWNER, SD_BUS_ERROR_NO_REPLY, SD_BUS_ERROR_IO_ERROR, SD_BUS_ERROR_BAD_ADDRESS, SD_BUS_ERROR_NOT_SUPPORTED, SD_BUS_ERROR_LIMITS_EXCEEDED, SD_BUS_ERROR_ACCESS_DENIED, SD_BUS_ERROR_AUTH_FAILED, SD_BUS_ERROR_NO_SERVER, SD_BUS_ERROR_TIMEOUT, SD_BUS_ERROR_NO_NETWORK, SD_BUS_ERROR_ADDRESS_IN_USE, SD_BUS_ERROR_DISCONNECTED, SD_BUS_ERROR_INVALID_ARGS, SD_BUS_ERROR_FILE_NOT_FOUND, SD_BUS_ERROR_FILE_EXISTS, SD_BUS_ERROR_UNKNOWN_METHOD, SD_BUS_ERROR_UNKNOWN_OBJECT, SD_BUS_ERROR_UNKNOWN_INTERFACE, SD_BUS_ERROR_UNKNOWN_PROPERTY, SD_BUS_ERROR_PROPERTY_READ_ONLY, SD_BUS_ERROR_UNIX_PROCESS_ID_UNKNOWN, SD_BUS_ERROR_INVALID_SIGNATURE, SD_BUS_ERROR_INCONSISTENT_MESSAGE, SD_BUS_ERROR_TIMED_OUT, SD_BUS_ERROR_MATCH_RULE_NOT_FOUND, SD_BUS_ERROR_MATCH_RULE_INVALID, SD_BUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED, SD_BUS_ERROR_INVALID_FILE_CONTENT, SD_BUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN, SD_BUS_ERROR_OBJECT_PATH_IN_USE — Standard D-Bus error names

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-bus.h>
```

``` funcsynopsisinfo
#define SD_BUS_ERROR_FAILED                  "org.freedesktop.DBus.Error.Failed"
#define SD_BUS_ERROR_NO_MEMORY               "org.freedesktop.DBus.Error.NoMemory"
#define SD_BUS_ERROR_SERVICE_UNKNOWN         "org.freedesktop.DBus.Error.ServiceUnknown"
#define SD_BUS_ERROR_NAME_HAS_NO_OWNER       "org.freedesktop.DBus.Error.NameHasNoOwner"
#define SD_BUS_ERROR_NO_REPLY                "org.freedesktop.DBus.Error.NoReply"
#define SD_BUS_ERROR_IO_ERROR                "org.freedesktop.DBus.Error.IOError"
#define SD_BUS_ERROR_BAD_ADDRESS             "org.freedesktop.DBus.Error.BadAddress"
#define SD_BUS_ERROR_NOT_SUPPORTED           "org.freedesktop.DBus.Error.NotSupported"
#define SD_BUS_ERROR_LIMITS_EXCEEDED         "org.freedesktop.DBus.Error.LimitsExceeded"
#define SD_BUS_ERROR_ACCESS_DENIED           "org.freedesktop.DBus.Error.AccessDenied"
#define SD_BUS_ERROR_AUTH_FAILED             "org.freedesktop.DBus.Error.AuthFailed"
#define SD_BUS_ERROR_NO_SERVER               "org.freedesktop.DBus.Error.NoServer"
#define SD_BUS_ERROR_TIMEOUT                 "org.freedesktop.DBus.Error.Timeout"
#define SD_BUS_ERROR_NO_NETWORK              "org.freedesktop.DBus.Error.NoNetwork"
#define SD_BUS_ERROR_ADDRESS_IN_USE          "org.freedesktop.DBus.Error.AddressInUse"
#define SD_BUS_ERROR_DISCONNECTED            "org.freedesktop.DBus.Error.Disconnected"
#define SD_BUS_ERROR_INVALID_ARGS            "org.freedesktop.DBus.Error.InvalidArgs"
#define SD_BUS_ERROR_FILE_NOT_FOUND          "org.freedesktop.DBus.Error.FileNotFound"
#define SD_BUS_ERROR_FILE_EXISTS             "org.freedesktop.DBus.Error.FileExists"
#define SD_BUS_ERROR_UNKNOWN_METHOD          "org.freedesktop.DBus.Error.UnknownMethod"
#define SD_BUS_ERROR_UNKNOWN_OBJECT          "org.freedesktop.DBus.Error.UnknownObject"
#define SD_BUS_ERROR_UNKNOWN_INTERFACE       "org.freedesktop.DBus.Error.UnknownInterface"
#define SD_BUS_ERROR_UNKNOWN_PROPERTY        "org.freedesktop.DBus.Error.UnknownProperty"
#define SD_BUS_ERROR_PROPERTY_READ_ONLY      "org.freedesktop.DBus.Error.PropertyReadOnly"
#define SD_BUS_ERROR_UNIX_PROCESS_ID_UNKNOWN "org.freedesktop.DBus.Error.UnixProcessIdUnknown"
#define SD_BUS_ERROR_INVALID_SIGNATURE       "org.freedesktop.DBus.Error.InvalidSignature"
#define SD_BUS_ERROR_INCONSISTENT_MESSAGE    "org.freedesktop.DBus.Error.InconsistentMessage"
#define SD_BUS_ERROR_TIMED_OUT               "org.freedesktop.DBus.Error.TimedOut"
#define SD_BUS_ERROR_MATCH_RULE_NOT_FOUND    "org.freedesktop.DBus.Error.MatchRuleNotFound"
#define SD_BUS_ERROR_MATCH_RULE_INVALID      "org.freedesktop.DBus.Error.MatchRuleInvalid"
#define SD_BUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED \
                                             "org.freedesktop.DBus.Error.InteractiveAuthorizationRequired"
#define SD_BUS_ERROR_INVALID_FILE_CONTENT    "org.freedesktop.DBus.Error.InvalidFileContent"
#define SD_BUS_ERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN \
                                             "org.freedesktop.DBus.Error.SELinuxSecurityContextUnknown"
#define SD_BUS_ERROR_OBJECT_PATH_IN_USE      "org.freedesktop.DBus.Error.ObjectPathInUse"
      
```

## Description

In addition to the error names user programs define, D-Bus knows a number of generic, standardized error names that are listed below.

In addition to this list, in sd-bus, the special error namespace "`System.Error.`" is used to map arbitrary Linux system errors (as defined by errno(3)) to D-Bus errors and back. For example, the error `EUCLEAN` is mapped to "`System.Error.EUCLEAN`" and back.

`SD_BUS_ERROR_FAILED`  
A generic error indication. See the error message for further details. This error name should be avoided, in favor of a more expressive error name.

Added in version 223.

`SD_BUS_ERROR_NO_MEMORY`  
A memory allocation failed, and the requested operation could not be completed.

Added in version 223.

`SD_BUS_ERROR_SERVICE_UNKNOWN`  
The contacted bus service is unknown and cannot be activated.

Added in version 223.

`SD_BUS_ERROR_NAME_HAS_NO_OWNER`  
The specified bus service name currently has no owner.

Added in version 223.

`SD_BUS_ERROR_NO_REPLY`  
A message did not receive a reply. This error is usually generated after a timeout.

Added in version 223.

`SD_BUS_ERROR_IO_ERROR`  
Generic input/output error, for example when accessing a socket or other I/O context.

Added in version 223.

`SD_BUS_ERROR_BAD_ADDRESS`  
The specified D-Bus bus address string is malformed.

Added in version 223.

`SD_BUS_ERROR_NOT_SUPPORTED`  
The requested operation is not supported on the local system.

Added in version 223.

`SD_BUS_ERROR_LIMITS_EXCEEDED`  
Some limited resource has been exhausted.

Added in version 223.

`SD_BUS_ERROR_ACCESS_DENIED`  
Access to a resource has been denied due to security restrictions.

Added in version 223.

`SD_BUS_ERROR_AUTH_FAILED`  
Authentication did not complete successfully.

Added in version 223.

`SD_BUS_ERROR_NO_SERVER`  
Unable to connect to the specified server.

Added in version 223.

`SD_BUS_ERROR_TIMEOUT`  
An operation timed out. Note that method calls which timeout generate a `SD_BUS_ERROR_NO_REPLY`.

Added in version 223.

`SD_BUS_ERROR_NO_NETWORK`  
No network available to execute requested network operation on.

Added in version 223.

`SD_BUS_ERROR_ADDRESS_IN_USE`  
The specified network address is already being listened on.

Added in version 223.

`SD_BUS_ERROR_DISCONNECTED`  
The connection has been terminated.

Added in version 223.

`SD_BUS_ERROR_INVALID_ARGS`  
One or more invalid arguments have been passed.

Added in version 223.

`SD_BUS_ERROR_FILE_NOT_FOUND`  
The requested file could not be found.

Added in version 223.

`SD_BUS_ERROR_FILE_EXISTS`  
The requested file already exists.

Added in version 223.

`SD_BUS_ERROR_UNKNOWN_METHOD`  
The requested method does not exist in the selected interface.

Added in version 223.

`SD_BUS_ERROR_UNKNOWN_OBJECT`  
The requested object does not exist in the selected service.

Added in version 223.

`SD_BUS_ERROR_UNKNOWN_INTERFACE`  
The requested interface does not exist on the selected object.

Added in version 223.

`SD_BUS_ERROR_UNKNOWN_PROPERTY`  
The requested property does not exist in the selected interface.

Added in version 223.

`SD_BUS_ERROR_PROPERTY_READ_ONLY`  
A write operation was requested on a read-only property.

Added in version 223.

`SD_BUS_ERROR_UNIX_PROCESS_ID_UNKNOWN`  
The requested PID is not known.

Added in version 223.

`SD_BUS_ERROR_INVALID_SIGNATURE`  
The specified message signature is not valid.

Added in version 223.

`SD_BUS_ERROR_INCONSISTENT_MESSAGE`  
The passed message does not validate correctly.

Added in version 223.

`SD_BUS_ERROR_MATCH_RULE_NOT_FOUND`  
The specified match rule does not exist.

Added in version 223.

`SD_BUS_ERROR_MATCH_RULE_INVALID`  
The specified match rule is invalid.

Added in version 223.

`SD_BUS_ERROR_INTERACTIVE_AUTHORIZATION_REQUIRED`  
Access to the requested operation is not permitted. However, it might be available after interactive authentication. This is usually returned by method calls supporting a framework for additional interactive authorization, when interactive authorization was not enabled with the sd_bus_message_set_allow_interactive_authorization(3) for the method call message.

Added in version 223.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## See Also

systemd(1), libsystemd(3), sd-bus(3), sd_bus_error(3), sd_bus_message_set_allow_interactive_authorization(3), errno(3), strerror_r(3)
