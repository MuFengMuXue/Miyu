Miscellaneous

D-Bus low-level public API

Miscellaneous API that doesn't cleanly fit anywhere else. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="macros" class="groupheader"> Macros</h2></td>
</tr>
<tr id="r_gab0c43046c79ba743bb2a4ed39ca4a5cd" class="memitem:gab0c43046c79ba743bb2a4ed39ca4a5cd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MAJOR_VERSION   1</td>
</tr>
<tr class="memdesc:gab0c43046c79ba743bb2a4ed39ca4a5cd">
<td class="mdescLeft"> </td>
<td class="mdescRight">The COMPILE TIME major version of libdbus, that is, the "X" in "X.Y.Z", as an integer literal.<br />
</td>
</tr>
<tr class="separator:gab0c43046c79ba743bb2a4ed39ca4a5cd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga6dcc9731da9f0713d55faa14937b4e06" class="memitem:ga6dcc9731da9f0713d55faa14937b4e06">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MINOR_VERSION   16</td>
</tr>
<tr class="memdesc:ga6dcc9731da9f0713d55faa14937b4e06">
<td class="mdescLeft"> </td>
<td class="mdescRight">The COMPILE TIME minor version of libdbus, that is, the "Y" in "X.Y.Z", as an integer literal.<br />
</td>
</tr>
<tr class="separator:ga6dcc9731da9f0713d55faa14937b4e06">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga44289275b3259451d0ba4185c735f1a3" class="memitem:ga44289275b3259451d0ba4185c735f1a3">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_MICRO_VERSION   2</td>
</tr>
<tr class="memdesc:ga44289275b3259451d0ba4185c735f1a3">
<td class="mdescLeft"> </td>
<td class="mdescRight">The COMPILE TIME micro version of libdbus, that is, the "Z" in "X.Y.Z", as an integer literal.<br />
</td>
</tr>
<tr class="separator:ga44289275b3259451d0ba4185c735f1a3">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga75f948aee9cf34afea18081cb4a7395f" class="memitem:ga75f948aee9cf34afea18081cb4a7395f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_VERSION   ((1 &lt;&lt; 16) | (16 &lt;&lt; 8) | (2))</td>
</tr>
<tr class="memdesc:ga75f948aee9cf34afea18081cb4a7395f">
<td class="mdescLeft"> </td>
<td class="mdescRight">The COMPILE TIME version of libdbus, as a single integer that has 0 in the most significant byte, the major version in the next most significant byte, the minor version in the third most significant, and the micro version in the least significant byte.<br />
</td>
</tr>
<tr class="separator:ga75f948aee9cf34afea18081cb4a7395f">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga538fff8f5929a940d195f3d74c49b27f" class="memitem:ga538fff8f5929a940d195f3d74c49b27f">
<td class="memItemLeft" style="text-align: right;" data-valign="top">#define </td>
<td class="memItemRight" data-valign="bottom">DBUS_VERSION_STRING   "1.16.2"</td>
</tr>
<tr class="memdesc:ga538fff8f5929a940d195f3d74c49b27f">
<td class="mdescLeft"> </td>
<td class="mdescRight">The COMPILE TIME version of libdbus, as a string "X.Y.Z".<br />
</td>
</tr>
<tr class="separator:ga538fff8f5929a940d195f3d74c49b27f">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_ga699a239bc42fd16cca3a17090e49cad8" class="memitem:ga699a239bc42fd16cca3a17090e49cad8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_try_get_local_machine_id (DBusError *error)</td>
</tr>
<tr class="memdesc:ga699a239bc42fd16cca3a17090e49cad8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Obtains the machine UUID of the machine this process is running on.<br />
</td>
</tr>
<tr class="separator:ga699a239bc42fd16cca3a17090e49cad8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2b21c9a12fea5f92763441c65ccbfcf9" class="memitem:ga2b21c9a12fea5f92763441c65ccbfcf9">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_get_local_machine_id (void)</td>
</tr>
<tr class="memdesc:ga2b21c9a12fea5f92763441c65ccbfcf9">
<td class="mdescLeft"> </td>
<td class="mdescRight">Obtains the machine UUID of the machine this process is running on.<br />
</td>
</tr>
<tr class="separator:ga2b21c9a12fea5f92763441c65ccbfcf9">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gacf200f947f77da9857685b58dc453d8a" class="memitem:gacf200f947f77da9857685b58dc453d8a">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_get_version (int *major_version_p, int *minor_version_p, int *micro_version_p)</td>
</tr>
<tr class="memdesc:gacf200f947f77da9857685b58dc453d8a">
<td class="mdescLeft"> </td>
<td class="mdescRight">Gets the DYNAMICALLY LINKED version of libdbus.<br />
</td>
</tr>
<tr class="separator:gacf200f947f77da9857685b58dc453d8a">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac02f6b021decd9fa35697a36ea581f86" class="memitem:gac02f6b021decd9fa35697a36ea581f86">
<td class="memItemLeft" style="text-align: right;" data-valign="top">DBUS_EXPORT dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_setenv (const char *variable, const char *value)</td>
</tr>
<tr class="memdesc:gac02f6b021decd9fa35697a36ea581f86">
<td class="mdescLeft"> </td>
<td class="mdescRight">Wrapper for setenv().<br />
</td>
</tr>
<tr class="separator:gac02f6b021decd9fa35697a36ea581f86">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Miscellaneous API that doesn't cleanly fit anywhere else.

## Macro Definition Documentation

## ◆ DBUS_MAJOR_VERSION

|                                 |
|---------------------------------|
| \#define DBUS_MAJOR_VERSION   1 |

The COMPILE TIME major version of libdbus, that is, the "X" in "X.Y.Z", as an integer literal.

Consider carefully whether to use this or the runtime version from dbus_get_version().

Definition at line 55 of file dbus-arch-deps.h.

## ◆ DBUS_MICRO_VERSION

|                                 |
|---------------------------------|
| \#define DBUS_MICRO_VERSION   2 |

The COMPILE TIME micro version of libdbus, that is, the "Z" in "X.Y.Z", as an integer literal.

Consider carefully whether to use this or the runtime version from dbus_get_version().

Definition at line 57 of file dbus-arch-deps.h.

## ◆ DBUS_MINOR_VERSION

|                                  |
|----------------------------------|
| \#define DBUS_MINOR_VERSION   16 |

The COMPILE TIME minor version of libdbus, that is, the "Y" in "X.Y.Z", as an integer literal.

Consider carefully whether to use this or the runtime version from dbus_get_version().

Definition at line 56 of file dbus-arch-deps.h.

## ◆ DBUS_VERSION

|                                                             |
|-------------------------------------------------------------|
| \#define DBUS_VERSION   ((1 \<\< 16) \| (16 \<\< 8) \| (2)) |

The COMPILE TIME version of libdbus, as a single integer that has 0 in the most significant byte, the major version in the next most significant byte, the minor version in the third most significant, and the micro version in the least significant byte.

This means two DBUS_VERSION can be compared to see which is higher.

Consider carefully whether to use this or the runtime version from dbus_get_version().

Definition at line 61 of file dbus-arch-deps.h.

## ◆ DBUS_VERSION_STRING

|                                         |
|-----------------------------------------|
| \#define DBUS_VERSION_STRING   "1.16.2" |

The COMPILE TIME version of libdbus, as a string "X.Y.Z".

Consider carefully whether to use this or the runtime version from dbus_get_version().

Definition at line 59 of file dbus-arch-deps.h.

## Function Documentation

## ◆ dbus_get_local_machine_id()

|                                               |     |       |     |     |     |
|-----------------------------------------------|-----|-------|-----|-----|-----|
| DBUS_EXPORT char \* dbus_get_local_machine_id | (   | void  |     | )   |     |

Obtains the machine UUID of the machine this process is running on.

The returned string must be freed with dbus_free().

This function returns NULL if there was not enough memory to read the UUID, or if the UUID could not be read because the D-Bus library was installed incorrectly. In the latter case, a warning is logged.

Other than its deficient error reporting, this function is the same as dbus_try_get_local_machine_id().

Returns  
a 32-byte-long hex-encoded UUID string, or NULL on failure

Definition at line 125 of file dbus-misc.c.

References \_dbus_warn_check_failed(), dbus_error_free(), dbus_error_has_name(), DBUS_ERROR_INIT, DBUS_ERROR_NO_MEMORY, dbus_try_get_local_machine_id(), DBusError::message, and NULL.

## ◆ dbus_get_version()

|                                   |     |         |                    |
|-----------------------------------|-----|---------|--------------------|
| DBUS_EXPORT void dbus_get_version | (   | int \*  | *major_version_p*, |
|                                   |     | int \*  | *minor_version_p*, |
|                                   |     | int \*  | *micro_version_p*  |
|                                   | )   |         |                    |

Gets the DYNAMICALLY LINKED version of libdbus.

Alternatively, there are macros DBUS_MAJOR_VERSION, DBUS_MINOR_VERSION, DBUS_MICRO_VERSION, and DBUS_VERSION which allow you to test the VERSION YOU ARE COMPILED AGAINST. In other words, you can get either the runtime or the compile-time version. Think carefully about which of these you want in a given case.

The libdbus full version number is "MAJOR.MINOR.MICRO" where the MINOR changes if API is added, and the MICRO changes with each release of a MAJOR.MINOR series. The MINOR is an odd number for development releases and an even number for stable releases.

Parameters  
|                 |                                              |
|-----------------|----------------------------------------------|
| major_version_p | pointer to return the major version, or NULL |
| minor_version_p | pointer to return the minor version, or NULL |
| micro_version_p | pointer to return the micro version, or NULL |

Definition at line 213 of file dbus-misc.c.

References DBUS_MAJOR_VERSION, DBUS_MICRO_VERSION, and DBUS_MINOR_VERSION.

## ◆ dbus_setenv()

|                                     |     |                |            |
|-------------------------------------|-----|----------------|------------|
| DBUS_EXPORT dbus_bool_t dbus_setenv | (   | const char \*  | *varname*, |
|                                     |     | const char \*  | *value*    |
|                                     | )   |                |            |

Wrapper for setenv().

If the value is NULL, unsets the environment variable.

There is an unfixable memleak in that it is unsafe to free memory malloced for use with setenv. This is because we can not rely on internal implementation details of the underlying libc library.

This function is not thread-safe, because altering the environment in Unix is not thread-safe in general.

Parameters  
|         |                                                 |
|---------|-------------------------------------------------|
| varname | name of environment variable                    |
| value   | value of environment variable, or NULL to unset |

<!-- -->

Returns  
TRUE on success, FALSE if not enough memory.

Definition at line 126 of file dbus-sysdeps.c.

References \_dbus_assert, FALSE, NULL, and TRUE.

Referenced by \_dbus_server_new_for_launchd().

## ◆ dbus_try_get_local_machine_id()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT char \* dbus_try_get_local_machine_id | ( | DBusError \*  | *error* | ) |  |

Obtains the machine UUID of the machine this process is running on.

The returned string must be freed with dbus_free().

This UUID is guaranteed to remain the same until the next reboot (unless the sysadmin foolishly changes it and screws themselves). It will usually remain the same across reboots also, but hardware configuration changes or rebuilding the machine could break that.

The idea is that two processes with the same machine ID should be able to use shared memory, UNIX domain sockets, process IDs, and other features of the OS that require both processes to be running on the same OS kernel instance.

The machine ID can also be used to create unique per-machine instances. For example, you could use it in bus names or X selection names.

The machine ID is preferred over the machine hostname, because the hostname is frequently set to "localhost.localdomain" and may also change at runtime.

You can get the machine ID of a remote application by invoking the method GetMachineId from interface org.freedesktop.DBus.Peer.

If the remote application has the same machine ID as the one returned by this function, then the remote application is on the same machine as your application.

The UUID is not a UUID in the sense of RFC4122; the details are explained in the D-Bus specification.

Returns  
a 32-byte-long hex-encoded UUID string, or NULL on failure

Definition at line 76 of file dbus-misc.c.

References \_dbus_get_local_machine_uuid_encoded(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_steal_data(), DBUS_ERROR_NO_MEMORY, dbus_set_error(), and NULL.

Referenced by dbus_get_local_machine_id().
