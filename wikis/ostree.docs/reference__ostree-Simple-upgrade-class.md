[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeSysrootUpgrader](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgrader "OstreeSysrootUpgrader") \* | [ostree_sysroot_upgrader_new](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-new "ostree_sysroot_upgrader_new ()") () |
| [OstreeSysrootUpgrader](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgrader "OstreeSysrootUpgrader") \* | [ostree_sysroot_upgrader_new_for_os](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-new-for-os "ostree_sysroot_upgrader_new_for_os ()") () |
| [OstreeSysrootUpgrader](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgrader "OstreeSysrootUpgrader") \* | [ostree_sysroot_upgrader_new_for_os_with_flags](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-new-for-os-with-flags "ostree_sysroot_upgrader_new_for_os_with_flags ()") () |
| GKeyFile \* | [ostree_sysroot_upgrader_get_origin](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-get-origin "ostree_sysroot_upgrader_get_origin ()") () |
| GKeyFile \* | [ostree_sysroot_upgrader_dup_origin](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-dup-origin "ostree_sysroot_upgrader_dup_origin ()") () |
| gboolean | [ostree_sysroot_upgrader_set_origin](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-set-origin "ostree_sysroot_upgrader_set_origin ()") () |
| char \* | [ostree_sysroot_upgrader_get_origin_description](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-get-origin-description "ostree_sysroot_upgrader_get_origin_description ()") () |
| gboolean | [ostree_sysroot_upgrader_check_timestamps](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-check-timestamps "ostree_sysroot_upgrader_check_timestamps ()") () |
| gboolean | [ostree_sysroot_upgrader_pull](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-pull "ostree_sysroot_upgrader_pull ()") () |
| gboolean | [ostree_sysroot_upgrader_pull_one_dir](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-pull-one-dir "ostree_sysroot_upgrader_pull_one_dir ()") () |
| gboolean | [ostree_sysroot_upgrader_deploy](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-deploy "ostree_sysroot_upgrader_deploy ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeSysrootUpgrader](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgrader "OstreeSysrootUpgrader") |
| enum | [OstreeSysrootUpgraderFlags](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgraderFlags "enum OstreeSysrootUpgraderFlags") |
| enum | [OstreeSysrootUpgraderPullFlags](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgraderPullFlags "enum OstreeSysrootUpgraderPullFlags") |

## Description

The [OstreeSysrootUpgrader](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgrader "OstreeSysrootUpgrader") class allows performing simple upgrade operations.

## Functions

### ostree_sysroot_upgrader_new ()

``` programlisting
OstreeSysrootUpgrader *
ostree_sysroot_upgrader_new (OstreeSysroot *sysroot,
                             GCancellable *cancellable,
                             GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| sysroot | An [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") |   |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

An upgrader.

\[transfer full\]

------------------------------------------------------------------------

### ostree_sysroot_upgrader_new_for_os ()

``` programlisting
OstreeSysrootUpgrader *
ostree_sysroot_upgrader_new_for_os (OstreeSysroot *sysroot,
                                    const char *osname,
                                    GCancellable *cancellable,
                                    GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| sysroot | An [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") |   |
| osname | Operating system name. | \[allow-none\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

An upgrader.

\[transfer full\]

------------------------------------------------------------------------

### ostree_sysroot_upgrader_new_for_os_with_flags ()

``` programlisting
OstreeSysrootUpgrader *
ostree_sysroot_upgrader_new_for_os_with_flags
                               (OstreeSysroot *sysroot,
                                const char *osname,
                                OstreeSysrootUpgraderFlags flags,
                                GCancellable *cancellable,
                                GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| sysroot | An [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") |   |
| osname | Operating system name. | \[allow-none\] |
| flags | Flags |   |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

An upgrader.

\[transfer full\]

------------------------------------------------------------------------

### ostree_sysroot_upgrader_get_origin ()

``` programlisting
GKeyFile *
ostree_sysroot_upgrader_get_origin (OstreeSysrootUpgrader *self);
```

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

The origin file, or `NULL` if unknown.

\[transfer none\]\[nullable\]

------------------------------------------------------------------------

### ostree_sysroot_upgrader_dup_origin ()

``` programlisting
GKeyFile *
ostree_sysroot_upgrader_dup_origin (OstreeSysrootUpgrader *self);
```

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

A copy of the origin file, or `NULL` if unknown.

\[transfer full\]\[nullable\]

------------------------------------------------------------------------

### ostree_sysroot_upgrader_set_origin ()

``` programlisting
gboolean
ostree_sysroot_upgrader_set_origin (OstreeSysrootUpgrader *self,
                                    GKeyFile *origin,
                                    GCancellable *cancellable,
                                    GError **error);
```

Replace the origin with *`origin`* .

#### Parameters

|             |                 |                |
|-------------|-----------------|----------------|
| self        | Sysroot         |                |
| origin      | The new origin. | \[allow-none\] |
| cancellable | Cancellable     |                |
| error       | Error           |                |

------------------------------------------------------------------------

### ostree_sysroot_upgrader_get_origin_description ()

``` programlisting
char *
ostree_sysroot_upgrader_get_origin_description
                               (OstreeSysrootUpgrader *self);
```

#### Parameters

|      |          |     |
|------|----------|-----|
| self | Upgrader |     |

#### Returns

A one-line descriptive summary of the origin, or `NULL` if unknown.

\[transfer full\]\[nullable\]

------------------------------------------------------------------------

### ostree_sysroot_upgrader_check_timestamps ()

``` programlisting
gboolean
ostree_sysroot_upgrader_check_timestamps
                               (OstreeRepo *repo,
                                const char *from_rev,
                                const char *to_rev,
                                GError **error);
```

Check that the timestamp on *`to_rev`* is equal to or newer than *`from_rev`* . This protects systems against man-in-the-middle attackers which provide a client with an older commit.

#### Parameters

|          |               |     |
|----------|---------------|-----|
| repo     | Repo          |     |
| from_rev | From revision |     |
| to_rev   | To revision   |     |
| error    | Error         |     |

------------------------------------------------------------------------

### ostree_sysroot_upgrader_pull ()

``` programlisting
gboolean
ostree_sysroot_upgrader_pull (OstreeSysrootUpgrader *self,
                              OstreeRepoPullFlags flags,
                              OstreeSysrootUpgraderPullFlags upgrader_flags,
                              OstreeAsyncProgress *progress,
                              gboolean *out_changed,
                              GCancellable *cancellable,
                              GError **error);
```

Perform a pull from the origin. First check if the ref has changed, if so download the linked objects, and store the updated ref locally. Then *`out_changed`* will be `TRUE`.

If the origin remote is unchanged, *`out_changed`* will be set to `FALSE`.

#### Parameters

|                |                                     |                |
|----------------|-------------------------------------|----------------|
| self           | Upgrader                            |                |
| flags          | Flags controlling pull behavior     |                |
| upgrader_flags | Flags controlling upgrader behavior |                |
| progress       | Progress.                           | \[allow-none\] |
| out_changed    | Whether or not the origin changed.  | \[out\]        |
| cancellable    | Cancellable                         |                |
| error          | Error                               |                |

------------------------------------------------------------------------

### ostree_sysroot_upgrader_pull_one_dir ()

``` programlisting
gboolean
ostree_sysroot_upgrader_pull_one_dir (OstreeSysrootUpgrader *self,
                                      const char *dir_to_pull,
                                      OstreeRepoPullFlags flags,
                                      OstreeSysrootUpgraderPullFlags upgrader_flags,
                                      OstreeAsyncProgress *progress,
                                      gboolean *out_changed,
                                      GCancellable *cancellable,
                                      GError **error);
```

Like [`ostree_sysroot_upgrader_pull()`](reference__ostree-Simple-upgrade-class.md#ostree-sysroot-upgrader-pull "ostree_sysroot_upgrader_pull ()"), but allows retrieving just a subpath of the tree. This can be used to download metadata files from inside the tree such as package databases.

#### Parameters

|  |  |  |
|----|----|----|
| self | Upgrader |   |
| dir_to_pull | Subdirectory path (should include a leading /) |   |
| flags | Flags controlling pull behavior |   |
| upgrader_flags | Flags controlling upgrader behavior |   |
| progress | Progress. | \[allow-none\] |
| out_changed | Whether or not the origin changed. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_sysroot_upgrader_deploy ()

``` programlisting
gboolean
ostree_sysroot_upgrader_deploy (OstreeSysrootUpgrader *self,
                                GCancellable *cancellable,
                                GError **error);
```

Write the new deployment to disk, perform a configuration merge with /etc, and update the bootloader configuration.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Self        |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

## Types and Values

### OstreeSysrootUpgrader

``` programlisting
typedef struct OstreeSysrootUpgrader OstreeSysrootUpgrader;
```

------------------------------------------------------------------------

### enum OstreeSysrootUpgraderFlags

Flags controlling operation of an [OstreeSysrootUpgrader](reference__ostree-Simple-upgrade-class.md#OstreeSysrootUpgrader "OstreeSysrootUpgrader").

#### Members

|  |  |  |
|----|----|----|
| OSTREE_SYSROOT_UPGRADER_FLAGS_NONE | No options |   |
| OSTREE_SYSROOT_UPGRADER_FLAGS_IGNORE_UNCONFIGURED | Do not error if the origin has an unconfigured-state key |   |
| OSTREE_SYSROOT_UPGRADER_FLAGS_STAGE | Enable "staging" (finalization at shutdown); recommended (Since: 2021.4) |   |
| OSTREE_SYSROOT_UPGRADER_FLAGS_KEXEC |   |   |

------------------------------------------------------------------------

### enum OstreeSysrootUpgraderPullFlags

#### Members

|                                                |     |     |
|------------------------------------------------|-----|-----|
| OSTREE_SYSROOT_UPGRADER_PULL_FLAGS_NONE        |     |     |
| OSTREE_SYSROOT_UPGRADER_PULL_FLAGS_ALLOW_OLDER |     |     |
| OSTREE_SYSROOT_UPGRADER_PULL_FLAGS_SYNTHETIC   |     |     |

------------------------------------------------------------------------
