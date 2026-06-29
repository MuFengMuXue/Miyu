## Name

sd_path_lookup, sd_path_lookup_strv — Query well-known file system paths

## Synopsis

``` funcsynopsisinfo
#include <systemd/sd-path.h>
```

``` funcsynopsisinfo
enum {
        SD_PATH_TEMPORARY,
        SD_PATH_TEMPORARY_LARGE,

        SD_PATH_SYSTEM_BINARIES,
        SD_PATH_SYSTEM_INCLUDE,
        SD_PATH_SYSTEM_LIBRARY_PRIVATE,
        SD_PATH_SYSTEM_LIBRARY_ARCH,
        SD_PATH_SYSTEM_SHARED,
        SD_PATH_SYSTEM_CONFIGURATION_FACTORY,
        SD_PATH_SYSTEM_STATE_FACTORY,

        SD_PATH_SYSTEM_CONFIGURATION,
        SD_PATH_SYSTEM_SEARCH_CONFIGURATION,
        SD_PATH_SYSTEM_RUNTIME,
        SD_PATH_SYSTEM_RUNTIME_LOGS,
        SD_PATH_SYSTEM_STATE_PRIVATE,
        SD_PATH_SYSTEM_STATE_LOGS,
        SD_PATH_SYSTEM_STATE_CACHE,
        SD_PATH_SYSTEM_STATE_SPOOL,

        SD_PATH_USER_BINARIES,
        SD_PATH_USER_LIBRARY_PRIVATE,
        SD_PATH_USER_LIBRARY_ARCH,
        SD_PATH_USER_SHARED,

        SD_PATH_USER_CONFIGURATION,
        SD_PATH_USER_RUNTIME,
        SD_PATH_USER_STATE_PRIVATE,
        SD_PATH_USER_STATE_CACHE,

        SD_PATH_USER,
        SD_PATH_USER_DOCUMENTS,
        SD_PATH_USER_MUSIC,
        SD_PATH_USER_PICTURES,
        SD_PATH_USER_VIDEOS,
        SD_PATH_USER_DOWNLOAD,
        SD_PATH_USER_PUBLIC,
        SD_PATH_USER_TEMPLATES,
        SD_PATH_USER_DESKTOP,

        SD_PATH_SEARCH_BINARIES,
        SD_PATH_SEARCH_BINARIES_DEFAULT,
        SD_PATH_SEARCH_LIBRARY_PRIVATE,
        SD_PATH_SEARCH_LIBRARY_ARCH,
        SD_PATH_SEARCH_SHARED,
        SD_PATH_SEARCH_CONFIGURATION_FACTORY,
        SD_PATH_SEARCH_STATE_FACTORY,
        SD_PATH_SEARCH_CONFIGURATION,

        SD_PATH_SYSTEMD_UTIL,
        SD_PATH_SYSTEMD_SYSTEM_UNIT,
        SD_PATH_SYSTEMD_SYSTEM_PRESET,
        SD_PATH_SYSTEMD_USER_UNIT,
        SD_PATH_SYSTEMD_USER_PRESET,
        SD_PATH_SYSTEMD_SYSTEM_CONF,
        SD_PATH_SYSTEMD_USER_CONF,
        SD_PATH_SYSTEMD_SEARCH_SYSTEM_UNIT,
        SD_PATH_SYSTEMD_SEARCH_USER_UNIT,
        SD_PATH_SYSTEMD_SYSTEM_GENERATOR,
        SD_PATH_SYSTEMD_USER_GENERATOR,
        SD_PATH_SYSTEMD_SEARCH_SYSTEM_GENERATOR,
        SD_PATH_SYSTEMD_SEARCH_USER_GENERATOR,
        SD_PATH_SYSTEMD_SLEEP,
        SD_PATH_SYSTEMD_SHUTDOWN,

        SD_PATH_TMPFILES,
        SD_PATH_SYSUSERS,
        SD_PATH_SYSCTL,
        SD_PATH_BINFMT,
        SD_PATH_MODULES_LOAD,
        SD_PATH_CATALOG,

        SD_PATH_SYSTEMD_SEARCH_NETWORK,

        SD_PATH_SYSTEMD_SYSTEM_ENVIRONMENT_GENERATOR,
        SD_PATH_SYSTEMD_USER_ENVIRONMENT_GENERATOR,
        SD_PATH_SYSTEMD_SEARCH_SYSTEM_ENVIRONMENT_GENERATOR,
        SD_PATH_SYSTEMD_SEARCH_USER_ENVIRONMENT_GENERATOR,
};
```

|                               |                        |
|-------------------------------|------------------------|
| `int `**`sd_path_lookup`**`(` | uint64_t `type`,       |
|                               | const char \*`suffix`, |
|                               | char \*\*`paths``)`;   |

 

|                                    |                        |
|------------------------------------|------------------------|
| `int `**`sd_path_lookup_strv`**`(` | uint64_t `type`,       |
|                                    | const char \*`suffix`, |
|                                    | char \*\*\*`paths``)`; |

 

## Description

`sd_path_lookup()` and `sd_bus_path_lookup_strv()` return a single path or set of file system paths specified by the argument *`type`*. In case of `sd_path_lookup()` a single `NUL`-terminated string is returned. When *`type`* specifies a set of paths, they are concatenated using "`:`" as a separator (as is traditionally done for e.g. `$PATH` or `$LD_LIBRARY_PATH`). In case of `sd_path_lookup_strv()` a `NULL`-terminated array of strings is returned (strv). If suffix *`suffix`* is given, it is concatenated to each of the paths after a slash ("`/`"). All returned paths are absolute.

For paths which refer to user directories, the relevant XDG standard is followed, with support for environment variables like `$XDG_DOCUMENTS_DIR`, `$XDG_DESKTOP_DIR`, ..., and explicit configuration in `/etc/xdg/user-dirs.conf` or `${XDG_CONFIG_HOME}/user-dirs.dirs`. See XDG Base Directory Specification for details.

systemd-path(1) is a wrapper around `sd_path_lookup()` and allows the same set of paths to be queried.

## Return Value

On success, `sd_path_lookup()` and `sd_path_lookup_strv()` return a non-negative integer. On failure, a negative errno-style error number is returned by either function.

The returned string or string array (strv) must be free(3)'d by the caller.

### Errors

Returned errors may indicate the following problems:

`-EOPNOTSUPP`  
Unknown identifier *`type`*.

Added in version 246.

`-EINVAL`  
Output argument is `NULL`.

Added in version 246.

`-ENXIO`  
Query failed because of an undefined environment variable (e.g. for `SD_PATH_USER_RUNTIME` when `$XDG_RUNTIME_DIR` is not defined).

Added in version 246.

`-ENOMEM`  
Memory allocation failed.

Added in version 246.

## Examples

### Look up the location of ~/Documents

``` programlisting
/* SPDX-License-Identifier: MIT-0 */

#include <stdio.h>
#include <stdlib.h>
#include <systemd/sd-path.h>

int main(void) {
  int r;
  char *t;

  r = sd_path_lookup(SD_PATH_USER_DOCUMENTS, NULL, &t);
  if (r < 0)
    return EXIT_FAILURE;

  printf("~/Documents: %s\n", t);
  free(t);

  return EXIT_SUCCESS;
}
```

Note that the default answer of `$HOME/Documents` may be overridden by `user-dirs.conf` or `$XDG_DOCUMENTS_DIR`.

## Notes

Functions described here are available as a shared library, which can be compiled against and linked to with the `libsystemd` pkg-config(1) file.

The code described here uses getenv(3), which is declared to be not multi-thread-safe. This means that the code calling the functions described here must not call setenv(3) from a parallel thread. It is recommended to only do calls to `setenv()` from an early phase of the program when no other threads have been started.

## History

`sd_path_lookup()` and `sd_path_lookup_strv()` were added in version 246.

## See Also

systemd(1), sd-path(3), systemd-path(1)
