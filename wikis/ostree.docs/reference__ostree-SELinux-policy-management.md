[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeSePolicy](reference__ostree-SELinux-policy-management.md#OstreeSePolicy "OstreeSePolicy") \* | [ostree_sepolicy_new](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-new "ostree_sepolicy_new ()") () |
| [OstreeSePolicy](reference__ostree-SELinux-policy-management.md#OstreeSePolicy "OstreeSePolicy") \* | [ostree_sepolicy_new_at](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-new-at "ostree_sepolicy_new_at ()") () |
| [OstreeSePolicy](reference__ostree-SELinux-policy-management.md#OstreeSePolicy "OstreeSePolicy") \* | [ostree_sepolicy_new_from_commit](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-new-from-commit "ostree_sepolicy_new_from_commit ()") () |
| GFile \* | [ostree_sepolicy_get_path](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-get-path "ostree_sepolicy_get_path ()") () |
| const char \* | [ostree_sepolicy_get_name](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-get-name "ostree_sepolicy_get_name ()") () |
| gboolean | [ostree_sepolicy_get_label](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-get-label "ostree_sepolicy_get_label ()") () |
| const char \* | [ostree_sepolicy_get_csum](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-get-csum "ostree_sepolicy_get_csum ()") () |
| gboolean | [ostree_sepolicy_restorecon](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-restorecon "ostree_sepolicy_restorecon ()") () |
| gboolean | [ostree_sepolicy_setfscreatecon](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-setfscreatecon "ostree_sepolicy_setfscreatecon ()") () |
| void | [ostree_sepolicy_fscreatecon_cleanup](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-fscreatecon-cleanup "ostree_sepolicy_fscreatecon_cleanup ()") () |
| void | [ostree_sepolicy_set_null_log](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-set-null-log "ostree_sepolicy_set_null_log ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeSePolicy](reference__ostree-SELinux-policy-management.md#OstreeSePolicy "OstreeSePolicy") |
| enum | [OstreeSePolicyRestoreconFlags](reference__ostree-SELinux-policy-management.md#OstreeSePolicyRestoreconFlags "enum OstreeSePolicyRestoreconFlags") |

## Description

A [OstreeSePolicy](reference__ostree-SELinux-policy-management.md#OstreeSePolicy "OstreeSePolicy") object can load the SELinux policy from a given root and perform labeling.

## Functions

### ostree_sepolicy_new ()

``` programlisting
OstreeSePolicy *
ostree_sepolicy_new (GFile *path,
                     GCancellable *cancellable,
                     GError **error);
```

#### Parameters

|             |                          |     |
|-------------|--------------------------|-----|
| path        | Path to a root directory |     |
| cancellable | Cancellable              |     |
| error       | Error                    |     |

#### Returns

An accessor object for SELinux policy in root located at *`path`* .

\[transfer full\]

------------------------------------------------------------------------

### ostree_sepolicy_new_at ()

``` programlisting
OstreeSePolicy *
ostree_sepolicy_new_at (int rootfs_dfd,
                        GCancellable *cancellable,
                        GError **error);
```

#### Parameters

|             |                                              |     |
|-------------|----------------------------------------------|-----|
| rootfs_dfd  | Directory fd for rootfs (will not be cloned) |     |
| cancellable | Cancellable                                  |     |
| error       | Error                                        |     |

#### Returns

An accessor object for SELinux policy in root located at *`rootfs_dfd`* .

\[transfer full\]

Since: 2017.4

------------------------------------------------------------------------

### ostree_sepolicy_new_from_commit ()

``` programlisting
OstreeSePolicy *
ostree_sepolicy_new_from_commit (OstreeRepo *repo,
                                 const char *rev,
                                 GCancellable *cancellable,
                                 GError **error);
```

Extract the SELinux policy from a commit object via a partial checkout. This is useful for labeling derived content as separate commits.

This function is the backend of [`ostree_repo_commit_modifier_set_sepolicy_from_commit()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-modifier-set-sepolicy-from-commit "ostree_repo_commit_modifier_set_sepolicy_from_commit ()").

#### Parameters

|             |                        |     |
|-------------|------------------------|-----|
| repo        | The repo               |     |
| rev         | ostree ref or checksum |     |
| cancellable | Cancellable            |     |
| error       | Error                  |     |

#### Returns

A new policy.

\[transfer full\]

------------------------------------------------------------------------

### ostree_sepolicy_get_path ()

``` programlisting
GFile *
ostree_sepolicy_get_path (OstreeSePolicy *self);
```

This API should be considered deprecated, because it's supported for policy objects to be created from file-descriptor relative paths, which may not be globally accessible.

#### Parameters

|      |                   |     |
|------|-------------------|-----|
| self | A SePolicy object |     |

#### Returns

Path to rootfs.

\[transfer none\]\[nullable\]

------------------------------------------------------------------------

### ostree_sepolicy_get_name ()

``` programlisting
const char *
ostree_sepolicy_get_name (OstreeSePolicy *self);
```

#### Returns

Type of current policy.

\[transfer none\]\[nullable\]

------------------------------------------------------------------------

### ostree_sepolicy_get_label ()

``` programlisting
gboolean
ostree_sepolicy_get_label (OstreeSePolicy *self,
                           const char *relpath,
                           guint32 unix_mode,
                           char **out_label,
                           GCancellable *cancellable,
                           GError **error);
```

Store in *`out_label`* the security context for the given *`relpath`* and mode *`unix_mode`* . If the policy does not specify a label, `NULL` will be returned.

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| relpath | Path |   |
| unix_mode | Unix mode |   |
| out_label | Return location for security context. | \[nullable\]\[out\]\[transfer full\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_sepolicy_get_csum ()

``` programlisting
const char *
ostree_sepolicy_get_csum (OstreeSePolicy *self);
```

#### Returns

Checksum of current policy.

\[transfer none\]\[nullable\]

Since: 2016.5

------------------------------------------------------------------------

### ostree_sepolicy_restorecon ()

``` programlisting
gboolean
ostree_sepolicy_restorecon (OstreeSePolicy *self,
                            const char *path,
                            GFileInfo *info,
                            GFile *target,
                            OstreeSePolicyRestoreconFlags flags,
                            char **out_new_label,
                            GCancellable *cancellable,
                            GError **error);
```

Reset the security context of *`target`* based on the SELinux policy.

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| path | Path string to use for policy lookup |   |
| info | File attributes. | \[nullable\] |
| target | Physical path to target file |   |
| flags | Flags controlling behavior |   |
| out_new_label | New label, or `NULL` if unchanged. | \[nullable\]\[optional\]\[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_sepolicy_setfscreatecon ()

``` programlisting
gboolean
ostree_sepolicy_setfscreatecon (OstreeSePolicy *self,
                                const char *path,
                                guint32 mode,
                                GError **error);
```

#### Parameters

|       |                                    |     |
|-------|------------------------------------|-----|
| self  | Policy                             |     |
| path  | Use this path to determine a label |     |
| mode  | Used along with *`path`*           |     |
| error | Error                              |     |

------------------------------------------------------------------------

### ostree_sepolicy_fscreatecon_cleanup ()

``` programlisting
void
ostree_sepolicy_fscreatecon_cleanup (void **unused);
```

Cleanup function for [`ostree_sepolicy_setfscreatecon()`](reference__ostree-SELinux-policy-management.md#ostree-sepolicy-setfscreatecon "ostree_sepolicy_setfscreatecon ()").

#### Parameters

|  |  |  |
|----|----|----|
| unused | Not used, just in case you didn't infer that from the parameter name |   |

------------------------------------------------------------------------

### ostree_sepolicy_set_null_log ()

``` programlisting
void
ostree_sepolicy_set_null_log (void);
```

Since: 2025.2

## Types and Values

### OstreeSePolicy

``` programlisting
typedef struct OstreeSePolicy OstreeSePolicy;
```

------------------------------------------------------------------------

### enum OstreeSePolicyRestoreconFlags

#### Members

|                                                |     |     |
|------------------------------------------------|-----|-----|
| OSTREE_SEPOLICY_RESTORECON_FLAGS_NONE          |     |     |
| OSTREE_SEPOLICY_RESTORECON_FLAGS_ALLOW_NOLABEL |     |     |
| OSTREE_SEPOLICY_RESTORECON_FLAGS_KEEP_EXISTING |     |     |

------------------------------------------------------------------------
