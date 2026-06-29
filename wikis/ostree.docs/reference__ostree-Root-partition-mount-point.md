[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") \* | [ostree_sysroot_new](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-new "ostree_sysroot_new ()") () |
| [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") \* | [ostree_sysroot_new_default](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-new-default "ostree_sysroot_new_default ()") () |
| gboolean | [ostree_sysroot_initialize](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-initialize "ostree_sysroot_initialize ()") () |
| gboolean | [ostree_sysroot_initialize_with_mount_namespace](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-initialize-with-mount-namespace "ostree_sysroot_initialize_with_mount_namespace ()") () |
| GFile \* | [ostree_sysroot_get_path](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-path "ostree_sysroot_get_path ()") () |
| gboolean | [ostree_sysroot_load](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()") () |
| gboolean | [ostree_sysroot_load_if_changed](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load-if-changed "ostree_sysroot_load_if_changed ()") () |
| gboolean | [ostree_sysroot_lock](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-lock "ostree_sysroot_lock ()") () |
| gboolean | [ostree_sysroot_try_lock](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-try-lock "ostree_sysroot_try_lock ()") () |
| void | [ostree_sysroot_lock_async](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-lock-async "ostree_sysroot_lock_async ()") () |
| gboolean | [ostree_sysroot_lock_finish](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-lock-finish "ostree_sysroot_lock_finish ()") () |
| void | [ostree_sysroot_unlock](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-unlock "ostree_sysroot_unlock ()") () |
| void | [ostree_sysroot_unload](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-unload "ostree_sysroot_unload ()") () |
| gboolean | [ostree_sysroot_update_post_copy](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-update-post-copy "ostree_sysroot_update_post_copy ()") () |
| void | [ostree_sysroot_set_mount_namespace_in_use](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-set-mount-namespace-in-use "ostree_sysroot_set_mount_namespace_in_use ()") () |
| gboolean | [ostree_sysroot_is_booted](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-is-booted "ostree_sysroot_is_booted ()") () |
| int | [ostree_sysroot_get_fd](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-fd "ostree_sysroot_get_fd ()") () |
| gboolean | [ostree_sysroot_ensure_initialized](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-ensure-initialized "ostree_sysroot_ensure_initialized ()") () |
| int | [ostree_sysroot_get_bootversion](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-bootversion "ostree_sysroot_get_bootversion ()") () |
| int | [ostree_sysroot_get_subbootversion](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-subbootversion "ostree_sysroot_get_subbootversion ()") () |
| GPtrArray \* | [ostree_sysroot_get_deployments](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-deployments "ostree_sysroot_get_deployments ()") () |
| [OstreeDeployment](reference__ostree-ostree-deployment.md#OstreeDeployment "OstreeDeployment") \* | [ostree_sysroot_get_booted_deployment](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-booted-deployment "ostree_sysroot_get_booted_deployment ()") () |
| [OstreeDeployment](reference__ostree-ostree-deployment.md#OstreeDeployment "OstreeDeployment") \* | [ostree_sysroot_require_booted_deployment](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-require-booted-deployment "ostree_sysroot_require_booted_deployment ()") () |
| GFile \* | [ostree_sysroot_get_deployment_directory](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-deployment-directory "ostree_sysroot_get_deployment_directory ()") () |
| char \* | [ostree_sysroot_get_deployment_dirpath](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-deployment-dirpath "ostree_sysroot_get_deployment_dirpath ()") () |
| GFile \* | [ostree_sysroot_get_deployment_origin_path](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-deployment-origin-path "ostree_sysroot_get_deployment_origin_path ()") () |
| gboolean | [ostree_sysroot_cleanup](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-cleanup "ostree_sysroot_cleanup ()") () |
| gboolean | [ostree_sysroot_prepare_cleanup](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-prepare-cleanup "ostree_sysroot_prepare_cleanup ()") () |
| gboolean | [ostree_sysroot_cleanup_prune_repo](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-cleanup-prune-repo "ostree_sysroot_cleanup_prune_repo ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_sysroot_repo](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-repo "ostree_sysroot_repo ()") () |
| gboolean | [ostree_sysroot_get_repo](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-repo "ostree_sysroot_get_repo ()") () |
| [OstreeDeployment](reference__ostree-ostree-deployment.md#OstreeDeployment "OstreeDeployment") \* | [ostree_sysroot_get_staged_deployment](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-staged-deployment "ostree_sysroot_get_staged_deployment ()") () |
| gboolean | [ostree_sysroot_init_osname](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-init-osname "ostree_sysroot_init_osname ()") () |
| gboolean | [ostree_sysroot_deployment_kexec_load](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deployment-kexec-load "ostree_sysroot_deployment_kexec_load ()") () |
| gboolean | [ostree_sysroot_deployment_set_kargs](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deployment-set-kargs "ostree_sysroot_deployment_set_kargs ()") () |
| gboolean | [ostree_sysroot_deployment_set_kargs_in_place](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deployment-set-kargs-in-place "ostree_sysroot_deployment_set_kargs_in_place ()") () |
| gboolean | [ostree_sysroot_deployment_set_mutable](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deployment-set-mutable "ostree_sysroot_deployment_set_mutable ()") () |
| gboolean | [ostree_sysroot_deployment_unlock](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deployment-unlock "ostree_sysroot_deployment_unlock ()") () |
| gboolean | [ostree_sysroot_deployment_set_pinned](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deployment-set-pinned "ostree_sysroot_deployment_set_pinned ()") () |
| gboolean | [ostree_sysroot_write_deployments](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-write-deployments "ostree_sysroot_write_deployments ()") () |
| gboolean | [ostree_sysroot_write_deployments_with_options](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-write-deployments-with-options "ostree_sysroot_write_deployments_with_options ()") () |
| gboolean | [ostree_sysroot_write_origin_file](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-write-origin-file "ostree_sysroot_write_origin_file ()") () |
| gboolean | [ostree_sysroot_stage_tree](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-stage-tree "ostree_sysroot_stage_tree ()") () |
| gboolean | [ostree_sysroot_stage_tree_with_options](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-stage-tree-with-options "ostree_sysroot_stage_tree_with_options ()") () |
| gboolean | [ostree_sysroot_stage_overlay_initrd](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-stage-overlay-initrd "ostree_sysroot_stage_overlay_initrd ()") () |
| gboolean | [ostree_sysroot_change_finalization](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-change-finalization "ostree_sysroot_change_finalization ()") () |
| gboolean | [ostree_sysroot_deploy_tree](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deploy-tree "ostree_sysroot_deploy_tree ()") () |
| gboolean | [ostree_sysroot_deploy_tree_with_options](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deploy-tree-with-options "ostree_sysroot_deploy_tree_with_options ()") () |
| [OstreeDeployment](reference__ostree-ostree-deployment.md#OstreeDeployment "OstreeDeployment") \* | [ostree_sysroot_get_merge_deployment](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-merge-deployment "ostree_sysroot_get_merge_deployment ()") () |
| void | [ostree_sysroot_query_deployments_for](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-query-deployments-for "ostree_sysroot_query_deployments_for ()") () |
| GKeyFile \* | [ostree_sysroot_origin_new_from_refspec](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-origin-new-from-refspec "ostree_sysroot_origin_new_from_refspec ()") () |
| gboolean | [ostree_sysroot_simple_write_deployment](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-simple-write-deployment "ostree_sysroot_simple_write_deployment ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") |
| enum | [OstreeSysrootSimpleWriteDeploymentFlags](reference__ostree-Root-partition-mount-point.md#OstreeSysrootSimpleWriteDeploymentFlags "enum OstreeSysrootSimpleWriteDeploymentFlags") |

## Description

A [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") object represents a physical root filesystem, which in particular should contain a toplevel /ostree directory. Inside this directory is an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") in /ostree/repo, plus a set of deployments in /ostree/deploy.

This class is not by default safe against concurrent use by threads or external processes. You can use [`ostree_sysroot_lock()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-lock "ostree_sysroot_lock ()") to perform locking externally.

## Functions

### ostree_sysroot_new ()

``` programlisting
OstreeSysroot *
ostree_sysroot_new (GFile *path);
```

Create a new [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") object for the sysroot at *`path`* . If *`path`* is `NULL`, the current visible root file system is used, equivalent to [`ostree_sysroot_new_default()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-new-default "ostree_sysroot_new_default ()").

#### Parameters

|  |  |  |
|----|----|----|
| path | Path to a system root directory, or `NULL` to use the current visible root file system. | \[allow-none\] |

#### Returns

An accessor object for an system root located at *`path`* .

\[transfer full\]

------------------------------------------------------------------------

### ostree_sysroot_new_default ()

``` programlisting
OstreeSysroot *
ostree_sysroot_new_default (void);
```

#### Returns

An accessor for the current visible root / filesystem.

\[transfer full\]

------------------------------------------------------------------------

### ostree_sysroot_initialize ()

``` programlisting
gboolean
ostree_sysroot_initialize (OstreeSysroot *self,
                           GError **error);
```

Subset of [`ostree_sysroot_load()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()"); performs basic initialization. Notably, one can invoke [`ostree_sysroot_get_fd()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-fd "ostree_sysroot_get_fd ()") after calling this function.

It is not necessary to call this function if [`ostree_sysroot_load()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()") is invoked.

#### Parameters

|      |         |     |
|------|---------|-----|
| self | sysroot |     |

Since: 2020.1

------------------------------------------------------------------------

### ostree_sysroot_initialize_with_mount_namespace ()

``` programlisting
gboolean
ostree_sysroot_initialize_with_mount_namespace
                               (OstreeSysroot *self,
                                GCancellable *cancellable,
                                GError **error);
```

Prepare the current process for modifying a booted sysroot, if applicable. This function subsumes the functionality of `ostree_sysroot_initialize` and may be invoked wherever that function is.

If the sysroot does not appear to be booted, or where the current process is not uid 0, this function returns successfully.

Otherwise, if the process is in the same mount namespace as pid 1, create a new namespace.

If you invoke this function, it must be before [`ostree_sysroot_load()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()"); it may be invoked before or after [`ostree_sysroot_initialize()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-initialize "ostree_sysroot_initialize ()").

Since: 2022.7

------------------------------------------------------------------------

### ostree_sysroot_get_path ()

``` programlisting
GFile *
ostree_sysroot_get_path (OstreeSysroot *self);
```

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

Path to rootfs.

\[transfer none\]\[not nullable\]

------------------------------------------------------------------------

### ostree_sysroot_load ()

``` programlisting
gboolean
ostree_sysroot_load (OstreeSysroot *self,
                     GCancellable *cancellable,
                     GError **error);
```

Load deployment list, bootversion, and subbootversion from the rootfs *`self`* .

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Sysroot     |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

------------------------------------------------------------------------

### ostree_sysroot_load_if_changed ()

``` programlisting
gboolean
ostree_sysroot_load_if_changed (OstreeSysroot *self,
                                gboolean *out_changed,
                                GCancellable *cancellable,
                                GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| self | [OstreeSysroot](reference__ostree-Root-partition-mount-point.md#OstreeSysroot "OstreeSysroot") |   |
| out_changed | . | \[out caller-allocates\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2016.4

------------------------------------------------------------------------

### ostree_sysroot_lock ()

``` programlisting
gboolean
ostree_sysroot_lock (OstreeSysroot *self,
                     GError **error);
```

Acquire an exclusive multi-process write lock for *`self`* . This call blocks until the lock has been acquired. The lock is not reentrant.

Release the lock with [`ostree_sysroot_unlock()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-unlock "ostree_sysroot_unlock ()"). The lock will also be released if *`self`* is deallocated.

#### Parameters

|       |       |     |
|-------|-------|-----|
| self  | Self  |     |
| error | Error |     |

------------------------------------------------------------------------

### ostree_sysroot_try_lock ()

``` programlisting
gboolean
ostree_sysroot_try_lock (OstreeSysroot *self,
                         gboolean *out_acquired,
                         GError **error);
```

Try to acquire an exclusive multi-process write lock for *`self`* . If another process holds the lock, this function will return immediately, setting *`out_acquired`* to `FALSE`, and returning `TRUE` (and no error).

Release the lock with [`ostree_sysroot_unlock()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-unlock "ostree_sysroot_unlock ()"). The lock will also be released if *`self`* is deallocated.

#### Parameters

|              |                                            |         |
|--------------|--------------------------------------------|---------|
| self         | Self                                       |         |
| out_acquired | Whether or not the lock has been acquired. | \[out\] |
| error        | Error                                      |         |

------------------------------------------------------------------------

### ostree_sysroot_lock_async ()

``` programlisting
void
ostree_sysroot_lock_async (OstreeSysroot *self,
                           GCancellable *cancellable,
                           GAsyncReadyCallback callback,
                           gpointer user_data);
```

An asynchronous version of [`ostree_sysroot_lock()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-lock "ostree_sysroot_lock ()").

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Self        |     |
| cancellable | Cancellable |     |
| callback    | Callback    |     |
| user_data   | User data   |     |

------------------------------------------------------------------------

### ostree_sysroot_lock_finish ()

``` programlisting
gboolean
ostree_sysroot_lock_finish (OstreeSysroot *self,
                            GAsyncResult *result,
                            GError **error);
```

Call when [`ostree_sysroot_lock_async()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-lock-async "ostree_sysroot_lock_async ()") is ready.

#### Parameters

|        |        |     |
|--------|--------|-----|
| self   | Self   |     |
| result | Result |     |
| error  | Error  |     |

------------------------------------------------------------------------

### ostree_sysroot_unlock ()

``` programlisting
void
ostree_sysroot_unlock (OstreeSysroot *self);
```

Clear the lock previously acquired with [`ostree_sysroot_lock()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-lock "ostree_sysroot_lock ()"). It is safe to call this function if the lock has not been previously acquired.

#### Parameters

|      |      |     |
|------|------|-----|
| self | Self |     |

------------------------------------------------------------------------

### ostree_sysroot_unload ()

``` programlisting
void
ostree_sysroot_unload (OstreeSysroot *self);
```

Release any resources such as file descriptors referring to the root directory of this sysroot. Normally, those resources are cleared by finalization, but in garbage collected languages that may not be predictable.

This undoes the effect of [`ostree_sysroot_load()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()").

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

------------------------------------------------------------------------

### ostree_sysroot_update_post_copy ()

``` programlisting
gboolean
ostree_sysroot_update_post_copy (OstreeSysroot *self,
                                 GCancellable *cancellable,
                                 GError **error);
```

Update a sysroot as needed after having copied it into place using file-level operations. This enables options like fs-verity on the required files that may have been lost during the copy.

#### Parameters

|       |         |     |
|-------|---------|-----|
| self  | Sysroot |     |
| error | Error   |     |

Since: 2023.11

------------------------------------------------------------------------

### ostree_sysroot_set_mount_namespace_in_use ()

``` programlisting
void
ostree_sysroot_set_mount_namespace_in_use
                               (OstreeSysroot *self);
```

If this function is invoked, then libostree will assume that a private Linux mount namespace has been created by the process. The primary use case for this is to have e.g. /sysroot mounted read-only by default.

If this function has been called, then when a function which requires writable access is invoked, libostree will automatically remount as writable any mount points on which it operates. This currently is just `/sysroot` and `/boot`.

If you invoke this function, it must be before [`ostree_sysroot_load()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()"); it may be invoked before or after [`ostree_sysroot_initialize()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-initialize "ostree_sysroot_initialize ()").

Since: 2020.1

------------------------------------------------------------------------

### ostree_sysroot_is_booted ()

``` programlisting
gboolean
ostree_sysroot_is_booted (OstreeSysroot *self);
```

Can only be invoked after [`ostree_sysroot_initialize()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-initialize "ostree_sysroot_initialize ()").

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

`TRUE` iff the sysroot points to a booted deployment

Since: 2020.1

------------------------------------------------------------------------

### ostree_sysroot_get_fd ()

``` programlisting
int
ostree_sysroot_get_fd (OstreeSysroot *self);
```

Access a file descriptor that refers to the root directory of this sysroot. [`ostree_sysroot_initialize()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-initialize "ostree_sysroot_initialize ()") (or [`ostree_sysroot_load()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()")) must have been invoked prior to calling this function.

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

A file descriptor valid for the lifetime of *`self`*

------------------------------------------------------------------------

### ostree_sysroot_ensure_initialized ()

``` programlisting
gboolean
ostree_sysroot_ensure_initialized (OstreeSysroot *self,
                                   GCancellable *cancellable,
                                   GError **error);
```

Ensure that *`self`* is set up as a valid rootfs, by creating /ostree/repo, among other things.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Sysroot     |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

------------------------------------------------------------------------

### ostree_sysroot_get_bootversion ()

``` programlisting
int
ostree_sysroot_get_bootversion (OstreeSysroot *self);
```

------------------------------------------------------------------------

### ostree_sysroot_get_subbootversion ()

``` programlisting
int
ostree_sysroot_get_subbootversion (OstreeSysroot *self);
```

------------------------------------------------------------------------

### ostree_sysroot_get_deployments ()

``` programlisting
GPtrArray *
ostree_sysroot_get_deployments (OstreeSysroot *self);
```

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

Ordered list of deployments.

\[element-type OstreeDeployment\]\[transfer container\]

------------------------------------------------------------------------

### ostree_sysroot_get_booted_deployment ()

``` programlisting
OstreeDeployment *
ostree_sysroot_get_booted_deployment (OstreeSysroot *self);
```

This function may only be called if the sysroot is loaded.

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

The currently booted deployment, or `NULL` if none.

\[transfer none\]\[nullable\]

------------------------------------------------------------------------

### ostree_sysroot_require_booted_deployment ()

``` programlisting
OstreeDeployment *
ostree_sysroot_require_booted_deployment
                               (OstreeSysroot *self,
                                GError **error);
```

Find the booted deployment, or return an error if not booted via OSTree.

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

The currently booted deployment, or an error.

\[transfer none\]\[not nullable\]

Since: 2021.1

------------------------------------------------------------------------

### ostree_sysroot_get_deployment_directory ()

``` programlisting
GFile *
ostree_sysroot_get_deployment_directory
                               (OstreeSysroot *self,
                                OstreeDeployment *deployment);
```

#### Parameters

|            |              |     |
|------------|--------------|-----|
| self       | Sysroot      |     |
| deployment | A deployment |     |

#### Returns

Path to deployment root directory.

\[transfer full\]

------------------------------------------------------------------------

### ostree_sysroot_get_deployment_dirpath ()

``` programlisting
char *
ostree_sysroot_get_deployment_dirpath (OstreeSysroot *self,
                                       OstreeDeployment *deployment);
```

Note this function only returns a \*relative\* path - if you want to access, it, you must either use fd-relative api such as `openat()`, or concatenate it with the full [`ostree_sysroot_get_path()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-path "ostree_sysroot_get_path ()").

#### Parameters

|            |              |     |
|------------|--------------|-----|
| self       | Repo         |     |
| deployment | A deployment |     |

#### Returns

Path to deployment root directory, relative to sysroot.

\[transfer full\]\[not nullable\]

------------------------------------------------------------------------

### ostree_sysroot_get_deployment_origin_path ()

``` programlisting
GFile *
ostree_sysroot_get_deployment_origin_path
                               (GFile *deployment_path);
```

#### Parameters

|                 |                   |     |
|-----------------|-------------------|-----|
| deployment_path | A deployment path |     |

#### Returns

Path to deployment origin file.

\[transfer full\]

------------------------------------------------------------------------

### ostree_sysroot_cleanup ()

``` programlisting
gboolean
ostree_sysroot_cleanup (OstreeSysroot *self,
                        GCancellable *cancellable,
                        GError **error);
```

Delete any state that resulted from a partially completed transaction, such as incomplete deployments.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Sysroot     |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

------------------------------------------------------------------------

### ostree_sysroot_prepare_cleanup ()

``` programlisting
gboolean
ostree_sysroot_prepare_cleanup (OstreeSysroot *self,
                                GCancellable *cancellable,
                                GError **error);
```

Like [`ostree_sysroot_cleanup()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-cleanup "ostree_sysroot_cleanup ()") in that it cleans up incomplete deployments and old boot versions, but does NOT prune the repository.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Sysroot     |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

------------------------------------------------------------------------

### ostree_sysroot_cleanup_prune_repo ()

``` programlisting
gboolean
ostree_sysroot_cleanup_prune_repo (OstreeSysroot *sysroot,
                                   OstreeRepoPruneOptions *options,
                                   gint *out_objects_total,
                                   gint *out_objects_pruned,
                                   guint64 *out_pruned_object_size_total,
                                   GCancellable *cancellable,
                                   GError **error);
```

Prune the system repository. This is a thin wrapper around [`ostree_repo_prune_from_reachable()`](reference__ostree-OstreeRepo.md#ostree-repo-prune-from-reachable "ostree_repo_prune_from_reachable ()"); the primary addition is that this function automatically gathers all deployed commits into the reachable set.

You generally want to at least set the `OSTREE_REPO_PRUNE_FLAGS_REFS_ONLY` flag in *`options`* . A commit traversal depth of `0` is assumed.

Locking: exclusive

#### Parameters

|  |  |  |
|----|----|----|
| sysroot | Sysroot |   |
| options | Flags controlling pruning |   |
| out_objects_total | Number of objects found. | \[out\] |
| out_objects_pruned | Number of objects deleted. | \[out\] |
| out_pruned_object_size_total | Storage size in bytes of objects deleted. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2018.6

------------------------------------------------------------------------

### ostree_sysroot_repo ()

``` programlisting
OstreeRepo *
ostree_sysroot_repo (OstreeSysroot *self);
```

This function is a variant of [`ostree_sysroot_get_repo()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-repo "ostree_sysroot_get_repo ()") that cannot fail, and returns a cached repository. Can only be called after [`ostree_sysroot_initialize()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-initialize "ostree_sysroot_initialize ()") or [`ostree_sysroot_load()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-load "ostree_sysroot_load ()") has been invoked successfully.

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

The OSTree repository in sysroot *`self`* .

\[transfer none\]\[not nullable\]

Since: 2017.7

------------------------------------------------------------------------

### ostree_sysroot_get_repo ()

``` programlisting
gboolean
ostree_sysroot_get_repo (OstreeSysroot *self,
                         OstreeRepo **out_repo,
                         GCancellable *cancellable,
                         GError **error);
```

Retrieve the OSTree repository in sysroot *`self`* . The repo is guaranteed to be open (see [`ostree_repo_open()`](reference__ostree-OstreeRepo.md#ostree-repo-open "ostree_repo_open ()")).

#### Parameters

|  |  |  |
|----|----|----|
| self | Sysroot |   |
| out_repo | Repository in sysroot *`self`* . | \[out\]\[transfer full\]\[optional\] |
| cancellable | Cancellable |   |
| error | Error |   |

#### Returns

`TRUE` on success, `FALSE` otherwise

------------------------------------------------------------------------

### ostree_sysroot_get_staged_deployment ()

``` programlisting
OstreeDeployment *
ostree_sysroot_get_staged_deployment (OstreeSysroot *self);
```

#### Parameters

|      |         |     |
|------|---------|-----|
| self | Sysroot |     |

#### Returns

The currently staged deployment, or `NULL` if none.

\[transfer none\]\[nullable\]

Since: 2018.5

------------------------------------------------------------------------

### ostree_sysroot_init_osname ()

``` programlisting
gboolean
ostree_sysroot_init_osname (OstreeSysroot *self,
                            const char *osname,
                            GCancellable *cancellable,
                            GError **error);
```

Initialize the directory structure for an "osname", which is a group of operating system deployments, with a shared `/var`. One is required for generating a deployment.

#### Parameters

|             |                                          |     |
|-------------|------------------------------------------|-----|
| self        | Sysroot                                  |     |
| osname      | Name group of operating system checkouts |     |
| cancellable | Cancellable                              |     |
| error       | Error                                    |     |

Since: 2016.4

------------------------------------------------------------------------

### ostree_sysroot_deployment_kexec_load ()

``` programlisting
gboolean
ostree_sysroot_deployment_kexec_load (OstreeSysroot *self,
                                      OstreeDeployment *deployment,
                                      GCancellable *cancellable,
                                      GError **error);
```

Prepare the specified deployment for a kexec.

#### Parameters

|             |                                   |     |
|-------------|-----------------------------------|-----|
| self        | Sysroot                           |     |
| deployment  | Deployment to prepare a kexec for |     |
| cancellable | Cancellable                       |     |
| error       | Error                             |     |

Since: 2025.1

------------------------------------------------------------------------

### ostree_sysroot_deployment_set_kargs ()

``` programlisting
gboolean
ostree_sysroot_deployment_set_kargs (OstreeSysroot *self,
                                     OstreeDeployment *deployment,
                                     char **new_kargs,
                                     GCancellable *cancellable,
                                     GError **error);
```

Entirely replace the kernel arguments of *`deployment`* with the values in *`new_kargs`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Sysroot |   |
| deployment | A deployment |   |
| new_kargs | Replace deployment's kernel arguments. | \[array zero-terminated=1\]\[element-type utf8\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_sysroot_deployment_set_kargs_in_place ()

``` programlisting
gboolean
ostree_sysroot_deployment_set_kargs_in_place
                               (OstreeSysroot *self,
                                OstreeDeployment *deployment,
                                char *kargs_str,
                                GCancellable *cancellable,
                                GError **error);
```

Replace the kernel arguments of *`deployment`* with the values in *`kargs_str`* .

#### Parameters

|             |                                             |                |
|-------------|---------------------------------------------|----------------|
| self        | Sysroot                                     |                |
| deployment  | A deployment                                |                |
| kargs_str   | Replace *`deployment`* 's kernel arguments. | \[allow-none\] |
| cancellable | Cancellable                                 |                |
| error       | Error                                       |                |

------------------------------------------------------------------------

### ostree_sysroot_deployment_set_mutable ()

``` programlisting
gboolean
ostree_sysroot_deployment_set_mutable (OstreeSysroot *self,
                                       OstreeDeployment *deployment,
                                       gboolean is_mutable,
                                       GCancellable *cancellable,
                                       GError **error);
```

By default, deployment directories are not mutable. This function will allow making them temporarily mutable, for example to allow layering additional non-OSTree content.

#### Parameters

|             |                                                  |     |
|-------------|--------------------------------------------------|-----|
| self        | Sysroot                                          |     |
| deployment  | A deployment                                     |     |
| is_mutable  | Whether or not deployment's files can be changed |     |
| cancellable | Cancellable                                      |     |
| error       | Error                                            |     |

------------------------------------------------------------------------

### ostree_sysroot_deployment_unlock ()

``` programlisting
gboolean
ostree_sysroot_deployment_unlock (OstreeSysroot *self,
                                  OstreeDeployment *deployment,
                                  OstreeDeploymentUnlockedState unlocked_state,
                                  GCancellable *cancellable,
                                  GError **error);
```

Configure the target deployment *`deployment`* such that it is writable. There are multiple modes, essentially differing in whether or not any changes persist across reboot.

The `OSTREE_DEPLOYMENT_UNLOCKED_HOTFIX` state is persistent across reboots.

#### Parameters

|                |                                   |     |
|----------------|-----------------------------------|-----|
| self           | Sysroot                           |     |
| deployment     | Deployment                        |     |
| unlocked_state | Transition to this unlocked state |     |
| cancellable    | Cancellable                       |     |
| error          | Error                             |     |

Since: 2016.4

------------------------------------------------------------------------

### ostree_sysroot_deployment_set_pinned ()

``` programlisting
gboolean
ostree_sysroot_deployment_set_pinned (OstreeSysroot *self,
                                      OstreeDeployment *deployment,
                                      gboolean is_pinned,
                                      GError **error);
```

By default, deployments may be subject to garbage collection. Typical uses of libostree only retain at most 2 deployments. If *`is_pinned`* is `TRUE`, a metadata bit will be set causing libostree to avoid automatic GC of the deployment. However, this is really an "advisory" note; it's still possible for e.g. older versions of libostree unaware of pinning to GC the deployment.

This function does nothing and returns successfully if the deployment is already in the desired pinning state. It is an error to try to pin the staged deployment (as it's not in the bootloader entries).

#### Parameters

|            |                                                      |     |
|------------|------------------------------------------------------|-----|
| self       | Sysroot                                              |     |
| deployment | A deployment                                         |     |
| is_pinned  | Whether or not deployment will be automatically GC'd |     |
| error      | Error                                                |     |

Since: 2018.3

------------------------------------------------------------------------

### ostree_sysroot_write_deployments ()

``` programlisting
gboolean
ostree_sysroot_write_deployments (OstreeSysroot *self,
                                  GPtrArray *new_deployments,
                                  GCancellable *cancellable,
                                  GError **error);
```

Older version of [`ostree_sysroot_write_deployments_with_options()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-write-deployments-with-options "ostree_sysroot_write_deployments_with_options ()"). This version will perform post-deployment cleanup by default.

#### Parameters

|                 |                          |                                   |
|-----------------|--------------------------|-----------------------------------|
| self            | Sysroot                  |                                   |
| new_deployments | List of new deployments. | \[element-type OstreeDeployment\] |
| cancellable     | Cancellable              |                                   |
| error           | Error                    |                                   |

------------------------------------------------------------------------

### ostree_sysroot_write_deployments_with_options ()

``` programlisting
gboolean
ostree_sysroot_write_deployments_with_options
                               (OstreeSysroot *self,
                                GPtrArray *new_deployments,
                                OstreeSysrootWriteDeploymentsOpts *opts,
                                GCancellable *cancellable,
                                GError **error);
```

Assuming *`new_deployments`* have already been deployed in place on disk via [`ostree_sysroot_deploy_tree()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deploy-tree "ostree_sysroot_deploy_tree ()"), atomically update bootloader configuration. By default, no post-transaction cleanup will be performed. You should invoke [`ostree_sysroot_cleanup()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-cleanup "ostree_sysroot_cleanup ()") at some point after the transaction, or specify `do_postclean` in *`opts`* . Skipping the post-transaction cleanup is useful if for example you want to control pruning of the repository.

#### Parameters

|                 |                          |                                   |
|-----------------|--------------------------|-----------------------------------|
| self            | Sysroot                  |                                   |
| new_deployments | List of new deployments. | \[element-type OstreeDeployment\] |
| opts            | Options                  |                                   |
| cancellable     | Cancellable              |                                   |
| error           | Error                    |                                   |

Since: 2017.4

------------------------------------------------------------------------

### ostree_sysroot_write_origin_file ()

``` programlisting
gboolean
ostree_sysroot_write_origin_file (OstreeSysroot *sysroot,
                                  OstreeDeployment *deployment,
                                  GKeyFile *new_origin,
                                  GCancellable *cancellable,
                                  GError **error);
```

Immediately replace the origin file of the referenced *`deployment`* with the contents of *`new_origin`* . If *`new_origin`* is `NULL`, this function will write the current origin of *`deployment`* .

#### Parameters

|             |                 |                |
|-------------|-----------------|----------------|
| sysroot     | System root     |                |
| deployment  | Deployment      |                |
| new_origin  | Origin content. | \[allow-none\] |
| cancellable | Cancellable     |                |
| error       | Error           |                |

------------------------------------------------------------------------

### ostree_sysroot_stage_tree ()

``` programlisting
gboolean
ostree_sysroot_stage_tree (OstreeSysroot *self,
                           const char *osname,
                           const char *revision,
                           GKeyFile *origin,
                           OstreeDeployment *merge_deployment,
                           char **override_kernel_argv,
                           OstreeDeployment **out_new_deployment,
                           GCancellable *cancellable,
                           GError **error);
```

Older version of [`ostree_sysroot_stage_tree_with_options()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-stage-tree-with-options "ostree_sysroot_stage_tree_with_options ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | Sysroot |   |
| osname | osname to use for merge deployment. | \[allow-none\] |
| revision | Checksum to add |   |
| origin | Origin to use for upgrades. | \[allow-none\] |
| merge_deployment | Use this deployment for merge path. | \[allow-none\] |
| override_kernel_argv | Use these as kernel arguments; if `NULL`, inherit options from provided_merge_deployment. | \[allow-none\]\[array zero-terminated=1\]\[element-type utf8\] |
| out_new_deployment | The new deployment path. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2018.5

------------------------------------------------------------------------

### ostree_sysroot_stage_tree_with_options ()

``` programlisting
gboolean
ostree_sysroot_stage_tree_with_options
                               (OstreeSysroot *self,
                                const char *osname,
                                const char *revision,
                                GKeyFile *origin,
                                OstreeDeployment *merge_deployment,
                                OstreeSysrootDeployTreeOpts *opts,
                                OstreeDeployment **out_new_deployment,
                                GCancellable *cancellable,
                                GError **error);
```

Like [`ostree_sysroot_deploy_tree()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deploy-tree "ostree_sysroot_deploy_tree ()"), but "finalization" only occurs at OS shutdown time.

#### Parameters

|                    |                                     |                |
|--------------------|-------------------------------------|----------------|
| self               | Sysroot                             |                |
| osname             | osname to use for merge deployment. | \[allow-none\] |
| revision           | Checksum to add                     |                |
| origin             | Origin to use for upgrades.         | \[allow-none\] |
| merge_deployment   | Use this deployment for merge path. | \[allow-none\] |
| opts               | Options                             |                |
| out_new_deployment | The new deployment path.            | \[out\]        |
| cancellable        | Cancellable                         |                |
| error              | Error                               |                |

Since: 2020.7

------------------------------------------------------------------------

### ostree_sysroot_stage_overlay_initrd ()

``` programlisting
gboolean
ostree_sysroot_stage_overlay_initrd (OstreeSysroot *self,
                                     int fd,
                                     char **out_checksum,
                                     GCancellable *cancellable,
                                     GError **error);
```

Stage an overlay initrd to be used in an upcoming deployment. Returns a checksum which can be passed to [`ostree_sysroot_deploy_tree_with_options()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deploy-tree-with-options "ostree_sysroot_deploy_tree_with_options ()") or [`ostree_sysroot_stage_tree_with_options()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-stage-tree-with-options "ostree_sysroot_stage_tree_with_options ()") via the `overlay_initrds` array option.

#### Parameters

|              |                                   |                          |
|--------------|-----------------------------------|--------------------------|
| self         | Sysroot                           |                          |
| fd           | File descriptor to overlay initrd |                          |
| out_checksum | Overlay initrd checksum.          | \[out\]\[transfer full\] |
| cancellable  | Cancellable                       |                          |
| error        | Error                             |                          |

Since: 2020.7

------------------------------------------------------------------------

### ostree_sysroot_change_finalization ()

``` programlisting
gboolean
ostree_sysroot_change_finalization (OstreeSysroot *self,
                                    OstreeDeployment *deployment,
                                    GError **error);
```

Given the target deployment (which must be the staged deployment) this API will toggle its "finalization locking" state. If it is currently locked, it will be unlocked (and hence queued to apply on shutdown).

#### Parameters

|            |                                 |     |
|------------|---------------------------------|-----|
| self       | Sysroot                         |     |
| deployment | Deployment which must be staged |     |
| error      | Error                           |     |

Since: 2023.8

------------------------------------------------------------------------

### ostree_sysroot_deploy_tree ()

``` programlisting
gboolean
ostree_sysroot_deploy_tree (OstreeSysroot *self,
                            const char *osname,
                            const char *revision,
                            GKeyFile *origin,
                            OstreeDeployment *provided_merge_deployment,
                            char **override_kernel_argv,
                            OstreeDeployment **out_new_deployment,
                            GCancellable *cancellable,
                            GError **error);
```

Older version of [`ostree_sysroot_stage_tree_with_options()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-stage-tree-with-options "ostree_sysroot_stage_tree_with_options ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | Sysroot |   |
| osname | osname to use for merge deployment. | \[nullable\] |
| revision | Checksum to add |   |
| origin | Origin to use for upgrades. | \[nullable\] |
| provided_merge_deployment | Use this deployment for merge path. | \[nullable\] |
| override_kernel_argv | Use these as kernel arguments; if `NULL`, inherit options from provided_merge_deployment. | \[nullable\]\[array zero-terminated=1\]\[element-type utf8\] |
| out_new_deployment | The new deployment path. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2018.5

------------------------------------------------------------------------

### ostree_sysroot_deploy_tree_with_options ()

``` programlisting
gboolean
ostree_sysroot_deploy_tree_with_options
                               (OstreeSysroot *self,
                                const char *osname,
                                const char *revision,
                                GKeyFile *origin,
                                OstreeDeployment *provided_merge_deployment,
                                OstreeSysrootDeployTreeOpts *opts,
                                OstreeDeployment **out_new_deployment,
                                GCancellable *cancellable,
                                GError **error);
```

Check out deployment tree with revision *`revision`* , performing a 3 way merge with *`provided_merge_deployment`* for configuration.

When booted into the sysroot, you should use the [`ostree_sysroot_stage_tree()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-stage-tree "ostree_sysroot_stage_tree ()") API instead.

#### Parameters

|  |  |  |
|----|----|----|
| self | Sysroot |   |
| osname | osname to use for merge deployment. | \[nullable\] |
| revision | Checksum to add |   |
| origin | Origin to use for upgrades. | \[nullable\] |
| provided_merge_deployment | Use this deployment for merge path. | \[nullable\] |
| opts | Options. | \[nullable\] |
| out_new_deployment | The new deployment path. | \[out\]\[transfer full\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2020.7

------------------------------------------------------------------------

### ostree_sysroot_get_merge_deployment ()

``` programlisting
OstreeDeployment *
ostree_sysroot_get_merge_deployment (OstreeSysroot *self,
                                     const char *osname);
```

Find the deployment to use as a configuration merge source; this is the first one in the current deployment list which matches osname.

#### Parameters

|        |                         |                |
|--------|-------------------------|----------------|
| self   | Sysroot                 |                |
| osname | Operating system group. | \[allow-none\] |

#### Returns

Configuration merge deployment.

\[transfer full\]\[nullable\]

------------------------------------------------------------------------

### ostree_sysroot_query_deployments_for ()

``` programlisting
void
ostree_sysroot_query_deployments_for (OstreeSysroot *self,
                                      const char *osname,
                                      OstreeDeployment **out_pending,
                                      OstreeDeployment **out_rollback);
```

Find the pending and rollback deployments for *`osname`* . Pass `NULL` for *`osname`* to use the booted deployment's osname. By default, pending deployment is the first deployment in the order that matches *`osname`* , and *`rollback`* will be the next one after the booted deployment, or the deployment after the pending if we're not looking at the booted deployment.

#### Parameters

|  |  |  |
|----|----|----|
| self | Sysroot |   |
| osname | "stateroot" name. | \[allow-none\] |
| out_pending | The pending deployment. | \[out\]\[nullable\]\[optional\]\[transfer full\] |
| out_rollback | The rollback deployment. | \[out\]\[nullable\]\[optional\]\[transfer full\] |

Since: 2017.7

------------------------------------------------------------------------

### ostree_sysroot_origin_new_from_refspec ()

``` programlisting
GKeyFile *
ostree_sysroot_origin_new_from_refspec
                               (OstreeSysroot *self,
                                const char *refspec);
```

#### Parameters

|         |           |     |
|---------|-----------|-----|
| self    | Sysroot   |     |
| refspec | A refspec |     |

#### Returns

A new config file which sets *`refspec`* as an origin.

\[transfer full\]\[not nullable\]

------------------------------------------------------------------------

### ostree_sysroot_simple_write_deployment ()

``` programlisting
gboolean
ostree_sysroot_simple_write_deployment
                               (OstreeSysroot *sysroot,
                                const char *osname,
                                OstreeDeployment *new_deployment,
                                OstreeDeployment *merge_deployment,
                                OstreeSysrootSimpleWriteDeploymentFlags flags,
                                GCancellable *cancellable,
                                GError **error);
```

Prepend *`new_deployment`* to the list of deployments, commit, and cleanup. By default, all other deployments for the given *`osname`* except the merge deployment and the booted deployment will be garbage collected.

If [`OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_RETAIN`](reference__ostree-Root-partition-mount-point.md#OSTREE-SYSROOT-SIMPLE-WRITE-DEPLOYMENT-FLAGS-RETAIN:CAPS) is specified, then all current deployments will be kept.

If [`OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_RETAIN_PENDING`](reference__ostree-Root-partition-mount-point.md#OSTREE-SYSROOT-SIMPLE-WRITE-DEPLOYMENT-FLAGS-RETAIN-PENDING:CAPS) is specified, then pending deployments will be kept.

If [`OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_RETAIN_ROLLBACK`](reference__ostree-Root-partition-mount-point.md#OSTREE-SYSROOT-SIMPLE-WRITE-DEPLOYMENT-FLAGS-RETAIN-ROLLBACK:CAPS) is specified, then rollback deployments will be kept.

If [`OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_NOT_DEFAULT`](reference__ostree-Root-partition-mount-point.md#OSTREE-SYSROOT-SIMPLE-WRITE-DEPLOYMENT-FLAGS-NOT-DEFAULT:CAPS) is specified, then instead of prepending, the new deployment will be added right after the booted or merge deployment, instead of first.

If [`OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_NO_CLEAN`](reference__ostree-Root-partition-mount-point.md#OSTREE-SYSROOT-SIMPLE-WRITE-DEPLOYMENT-FLAGS-NO-CLEAN:CAPS) is specified, then no cleanup will be performed after adding the deployment. Make sure to call [`ostree_sysroot_cleanup()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-cleanup "ostree_sysroot_cleanup ()") sometime later, instead.

#### Parameters

|  |  |  |
|----|----|----|
| sysroot | Sysroot |   |
| osname | OS name. | \[allow-none\] |
| new_deployment | Prepend this deployment to the list |   |
| merge_deployment | Use this deployment for configuration merge. | \[allow-none\] |
| flags | Flags controlling behavior |   |
| cancellable | Cancellable |   |
| error | Error |   |

## Types and Values

### OstreeSysroot

``` programlisting
typedef struct OstreeSysroot OstreeSysroot;
```

------------------------------------------------------------------------

### enum OstreeSysrootSimpleWriteDeploymentFlags

#### Members

|                                                              |     |     |
|--------------------------------------------------------------|-----|-----|
| OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_NONE            |     |     |
| OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_RETAIN          |     |     |
| OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_NOT_DEFAULT     |     |     |
| OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_NO_CLEAN        |     |     |
| OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_RETAIN_PENDING  |     |     |
| OSTREE_SYSROOT_SIMPLE_WRITE_DEPLOYMENT_FLAGS_RETAIN_ROLLBACK |     |     |

------------------------------------------------------------------------
