|                      |     |     |     |     |
|:---------------------|-----|-----|-----|-----|
| Top  \|  Description |     |     |     |     |

<table width="100%">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-valign="top"><h2 id="dbusgerror">DBusGError</h2>
<p>DBusGError — DBus GError</p></td>
<td class="gallery_image" style="text-align: right;" data-valign="top"></td>
</tr>
</tbody>
</table>

## Stability Level

Stable, unless otherwise indicated

## Functions

|               |                                 |
|---------------|---------------------------------|
| gboolean      | dbus_g_error_has_name ()        |
| const char \* | dbus_g_error_get_name ()        |
| void          | dbus_g_error_domain_register () |

## Types and Values

|          |             |
|----------|-------------|
| enum     | DBusGError  |
| \#define | DBUS_GERROR |

## Includes

``` synopsis
#include <dbus/dbus-glib.h>
```

## Description

DBusGError is the GError used by DBus.

## Functions

### dbus_g_error_has_name ()

``` programlisting
gboolean
dbus_g_error_has_name (GError *error,
                       const char *name);
```

`dbus_g_error_has_name` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_error_get_remote_error()`.

Determine whether D-BUS error name for a remote exception matches the given name. This function is intended to be invoked on a GError returned from an invocation of a remote method, e.g. via `dbus_g_proxy_end_call()`. It will silently return `FALSE` for errors which are not remote D-BUS exceptions (i.e. with a domain other than `DBUS_GERROR` or a code other than `DBUS_GERROR_REMOTE_EXCEPTION`).

#### Parameters

|       |                                         |     |
|-------|-----------------------------------------|-----|
| error | the GError given from the remote method |     |
| name  | the D-BUS error name                    |     |

#### Returns

`TRUE` if and only if the remote error has the given name

### dbus_g_error_get_name ()

``` programlisting
const char *
dbus_g_error_get_name (GError *error);
```

`dbus_g_error_get_name` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_error_get_remote_error()`.

This function may only be invoked on a GError returned from an invocation of a remote method, e.g. via `dbus_g_proxy_end_call()`. Moreover, you must ensure that the error's domain is `DBUS_GERROR`, and the code is `DBUS_GERROR_REMOTE_EXCEPTION`.

#### Parameters

|       |                                         |     |
|-------|-----------------------------------------|-----|
| error | the GError given from the remote method |     |

#### Returns

the D-BUS name for a remote exception.

### dbus_g_error_domain_register ()

``` programlisting
void
dbus_g_error_domain_register (GQuark domain,
                              const char *default_iface,
                              GType code_enum);
```

`dbus_g_error_domain_register` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `g_dbus_error_register_error_domain()`.

Register a GError domain and set of codes with D-Bus. When an object raises a GError in the domain *`domain`* from one of its D-Bus methods, the D-Bus error name used will be *`default_iface`* , followed by a dot, followed by the GEnumValue.value_nick corresponding to the GError.code. For D-Bus, it's conventional to use an error name (value_nick) that is in CamelCase.

(For instance, if a D-Bus method `com.example.MyObject.GetThings` can raise a GError with domain `MY_ERROR` and code

`MY_ERROR_NOT_HAPPY`, you could call `dbus_g_error_domain_register (MY_ERROR, "com.example.MyError", MY_TYPE_ERROR)`, and set up the value_nick for `MY_ERROR_NOT_HAPPY` to be `NotHappy`,

resulting in the D-Bus error string

`com.example.MyError.NotHappy`.)

If *`default_iface`* is `NULL`, the D-Bus interface of the method that failed will be used.

(For instance, if the above example had called

`dbus_g_error_domain_register (MY_ERROR, NULL, MY_TYPE_ERROR)`

instead, then the D-Bus error string would be

`com.example.MyObject.NotHappy`.)

#### Parameters

|               |                                             |     |
|---------------|---------------------------------------------|-----|
| domain        | the GError domain                           |     |
| default_iface | the prefix used for error values, or `NULL` |     |
| code_enum     | a GType for a GEnum of the error codes      |     |

## Types and Values

### enum DBusGError

`DBusGError` is deprecated and should not be used in newly-written code.

New code should use GDBus and its GDBusError enum instead.

A GError enumeration for the domain `DBUS_GERROR`. The values' meanings can be found by looking at the comments for the corresponding constants in dbus-protocol.h.

#### Members

|                                              |     |     |
|----------------------------------------------|-----|-----|
| DBUS_GERROR_FAILED                           |     |     |
| DBUS_GERROR_NO_MEMORY                        |     |     |
| DBUS_GERROR_SERVICE_UNKNOWN                  |     |     |
| DBUS_GERROR_NAME_HAS_NO_OWNER                |     |     |
| DBUS_GERROR_NO_REPLY                         |     |     |
| DBUS_GERROR_IO_ERROR                         |     |     |
| DBUS_GERROR_BAD_ADDRESS                      |     |     |
| DBUS_GERROR_NOT_SUPPORTED                    |     |     |
| DBUS_GERROR_LIMITS_EXCEEDED                  |     |     |
| DBUS_GERROR_ACCESS_DENIED                    |     |     |
| DBUS_GERROR_AUTH_FAILED                      |     |     |
| DBUS_GERROR_NO_SERVER                        |     |     |
| DBUS_GERROR_TIMEOUT                          |     |     |
| DBUS_GERROR_NO_NETWORK                       |     |     |
| DBUS_GERROR_ADDRESS_IN_USE                   |     |     |
| DBUS_GERROR_DISCONNECTED                     |     |     |
| DBUS_GERROR_INVALID_ARGS                     |     |     |
| DBUS_GERROR_FILE_NOT_FOUND                   |     |     |
| DBUS_GERROR_FILE_EXISTS                      |     |     |
| DBUS_GERROR_UNKNOWN_METHOD                   |     |     |
| DBUS_GERROR_TIMED_OUT                        |     |     |
| DBUS_GERROR_MATCH_RULE_NOT_FOUND             |     |     |
| DBUS_GERROR_MATCH_RULE_INVALID               |     |     |
| DBUS_GERROR_SPAWN_EXEC_FAILED                |     |     |
| DBUS_GERROR_SPAWN_FORK_FAILED                |     |     |
| DBUS_GERROR_SPAWN_CHILD_EXITED               |     |     |
| DBUS_GERROR_SPAWN_CHILD_SIGNALED             |     |     |
| DBUS_GERROR_SPAWN_FAILED                     |     |     |
| DBUS_GERROR_UNIX_PROCESS_ID_UNKNOWN          |     |     |
| DBUS_GERROR_INVALID_SIGNATURE                |     |     |
| DBUS_GERROR_INVALID_FILE_CONTENT             |     |     |
| DBUS_GERROR_SELINUX_SECURITY_CONTEXT_UNKNOWN |     |     |
| DBUS_GERROR_REMOTE_EXCEPTION                 |     |     |

### DBUS_GERROR

``` programlisting
#define DBUS_GERROR dbus_g_error_quark ()
```

`DBUS_GERROR` is deprecated and should not be used in newly-written code.

New code should use GDBus and its GDBusError enum instead.

Expands to a function call returning the error domain quark for DBusGError, for use with GError.

## See Also

GError
