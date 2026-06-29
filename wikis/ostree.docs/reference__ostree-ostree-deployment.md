[TABLE]

## Functions

|  |  |
|----|----|
| guint | [ostree_deployment_hash](reference__ostree-ostree-deployment.md#ostree-deployment-hash "ostree_deployment_hash ()") () |
| gboolean | [ostree_deployment_equal](reference__ostree-ostree-deployment.md#ostree-deployment-equal "ostree_deployment_equal ()") () |
| [OstreeDeployment](reference__ostree-ostree-deployment.md#OstreeDeployment "OstreeDeployment") \* | [ostree_deployment_new](reference__ostree-ostree-deployment.md#ostree-deployment-new "ostree_deployment_new ()") () |
| int | [ostree_deployment_get_index](reference__ostree-ostree-deployment.md#ostree-deployment-get-index "ostree_deployment_get_index ()") () |
| const char \* | [ostree_deployment_get_osname](reference__ostree-ostree-deployment.md#ostree-deployment-get-osname "ostree_deployment_get_osname ()") () |
| int | [ostree_deployment_get_deployserial](reference__ostree-ostree-deployment.md#ostree-deployment-get-deployserial "ostree_deployment_get_deployserial ()") () |
| const char \* | [ostree_deployment_get_csum](reference__ostree-ostree-deployment.md#ostree-deployment-get-csum "ostree_deployment_get_csum ()") () |
| const char \* | [ostree_deployment_get_bootcsum](reference__ostree-ostree-deployment.md#ostree-deployment-get-bootcsum "ostree_deployment_get_bootcsum ()") () |
| int | [ostree_deployment_get_bootserial](reference__ostree-ostree-deployment.md#ostree-deployment-get-bootserial "ostree_deployment_get_bootserial ()") () |
| [OstreeBootconfigParser](reference__ostree-ostree-bootconfig-parser.md#OstreeBootconfigParser "OstreeBootconfigParser") \* | [ostree_deployment_get_bootconfig](reference__ostree-ostree-deployment.md#ostree-deployment-get-bootconfig "ostree_deployment_get_bootconfig ()") () |
| GKeyFile \* | [ostree_deployment_get_origin](reference__ostree-ostree-deployment.md#ostree-deployment-get-origin "ostree_deployment_get_origin ()") () |
| char \* | [ostree_deployment_get_origin_relpath](reference__ostree-ostree-deployment.md#ostree-deployment-get-origin-relpath "ostree_deployment_get_origin_relpath ()") () |
| OstreeDeploymentUnlockedState | [ostree_deployment_get_unlocked](reference__ostree-ostree-deployment.md#ostree-deployment-get-unlocked "ostree_deployment_get_unlocked ()") () |
| gboolean | [ostree_deployment_is_pinned](reference__ostree-ostree-deployment.md#ostree-deployment-is-pinned "ostree_deployment_is_pinned ()") () |
| gboolean | [ostree_deployment_is_staged](reference__ostree-ostree-deployment.md#ostree-deployment-is-staged "ostree_deployment_is_staged ()") () |
| gboolean | [ostree_deployment_is_finalization_locked](reference__ostree-ostree-deployment.md#ostree-deployment-is-finalization-locked "ostree_deployment_is_finalization_locked ()") () |
| gboolean | [ostree_deployment_is_soft_reboot_target](reference__ostree-ostree-deployment.md#ostree-deployment-is-soft-reboot-target "ostree_deployment_is_soft_reboot_target ()") () |
| void | [ostree_deployment_set_index](reference__ostree-ostree-deployment.md#ostree-deployment-set-index "ostree_deployment_set_index ()") () |
| void | [ostree_deployment_set_bootserial](reference__ostree-ostree-deployment.md#ostree-deployment-set-bootserial "ostree_deployment_set_bootserial ()") () |
| void | [ostree_deployment_set_bootconfig](reference__ostree-ostree-deployment.md#ostree-deployment-set-bootconfig "ostree_deployment_set_bootconfig ()") () |
| void | [ostree_deployment_set_origin](reference__ostree-ostree-deployment.md#ostree-deployment-set-origin "ostree_deployment_set_origin ()") () |
| void | [ostree_deployment_origin_remove_transient_state](reference__ostree-ostree-deployment.md#ostree-deployment-origin-remove-transient-state "ostree_deployment_origin_remove_transient_state ()") () |
| [OstreeDeployment](reference__ostree-ostree-deployment.md#OstreeDeployment "OstreeDeployment") \* | [ostree_deployment_clone](reference__ostree-ostree-deployment.md#ostree-deployment-clone "ostree_deployment_clone ()") () |
| const char \* | [ostree_deployment_unlocked_state_to_string](reference__ostree-ostree-deployment.md#ostree-deployment-unlocked-state-to-string "ostree_deployment_unlocked_state_to_string ()") () |

## Types and Values

|  |  |
|----|----|
|   | [OstreeDeployment](reference__ostree-ostree-deployment.md#OstreeDeployment "OstreeDeployment") |

## Description

## Functions

### ostree_deployment_hash ()

``` programlisting
guint
ostree_deployment_hash (gconstpointer v);
```

#### Parameters

|     |             |                           |
|-----|-------------|---------------------------|
| v   | Deployment. | \[type OstreeDeployment\] |

#### Returns

An integer suitable for use in a `GHashTable`

------------------------------------------------------------------------

### ostree_deployment_equal ()

``` programlisting
gboolean
ostree_deployment_equal (gconstpointer ap,
                         gconstpointer bp);
```

#### Parameters

|     |               |                           |
|-----|---------------|---------------------------|
| ap  | A deployment. | \[type OstreeDeployment\] |
| bp  | A deployment. | \[type OstreeDeployment\] |

#### Returns

`TRUE` if deployments have the same osname, csum, and deployserial

------------------------------------------------------------------------

### ostree_deployment_new ()

``` programlisting
OstreeDeployment *
ostree_deployment_new (int index,
                       const char *osname,
                       const char *csum,
                       int deployserial,
                       const char *bootcsum,
                       int bootserial);
```

#### Parameters

|              |                                          |              |
|--------------|------------------------------------------|--------------|
| index        | Global index into the bootloader entries |              |
| osname       | "stateroot" for this deployment          |              |
| csum         | OSTree commit that will be deployed      |              |
| deployserial | Unique counter                           |              |
| bootcsum     | Kernel/initrd checksum.                  | \[nullable\] |
| bootserial   | Unique index                             |              |

#### Returns

New deployment.

\[transfer full\]\[not nullable\]

------------------------------------------------------------------------

### ostree_deployment_get_index ()

``` programlisting
int
ostree_deployment_get_index (OstreeDeployment *self);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

The global index into the bootloader ordering

------------------------------------------------------------------------

### ostree_deployment_get_osname ()

``` programlisting
const char *
ostree_deployment_get_osname (OstreeDeployment *self);
```

------------------------------------------------------------------------

### ostree_deployment_get_deployserial ()

``` programlisting
int
ostree_deployment_get_deployserial (OstreeDeployment *self);
```

------------------------------------------------------------------------

### ostree_deployment_get_csum ()

``` programlisting
const char *
ostree_deployment_get_csum (OstreeDeployment *self);
```

------------------------------------------------------------------------

### ostree_deployment_get_bootcsum ()

``` programlisting
const char *
ostree_deployment_get_bootcsum (OstreeDeployment *self);
```

------------------------------------------------------------------------

### ostree_deployment_get_bootserial ()

``` programlisting
int
ostree_deployment_get_bootserial (OstreeDeployment *self);
```

------------------------------------------------------------------------

### ostree_deployment_get_bootconfig ()

``` programlisting
OstreeBootconfigParser *
ostree_deployment_get_bootconfig (OstreeDeployment *self);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

Boot configuration.

\[transfer none\]\[nullable\]

------------------------------------------------------------------------

### ostree_deployment_get_origin ()

``` programlisting
GKeyFile *
ostree_deployment_get_origin (OstreeDeployment *self);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

Origin.

\[transfer none\]\[nullable\]

------------------------------------------------------------------------

### ostree_deployment_get_origin_relpath ()

``` programlisting
char *
ostree_deployment_get_origin_relpath (OstreeDeployment *self);
```

Note this function only returns a \*relative\* path - if you want to access, it, you must either use fd-relative api such as `openat()`, or concatenate it with the full [`ostree_sysroot_get_path()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-get-path "ostree_sysroot_get_path ()").

#### Parameters

|      |              |     |
|------|--------------|-----|
| self | A deployment |     |

#### Returns

Path to deployment root directory, relative to sysroot.

\[not nullable\]\[transfer full\]

------------------------------------------------------------------------

### ostree_deployment_get_unlocked ()

``` programlisting
OstreeDeploymentUnlockedState
ostree_deployment_get_unlocked (OstreeDeployment *self);
```

Since: 2016.4

------------------------------------------------------------------------

### ostree_deployment_is_pinned ()

``` programlisting
gboolean
ostree_deployment_is_pinned (OstreeDeployment *self);
```

See [`ostree_sysroot_deployment_set_pinned()`](reference__ostree-Root-partition-mount-point.md#ostree-sysroot-deployment-set-pinned "ostree_sysroot_deployment_set_pinned ()").

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

`TRUE` if deployment will not be subject to GC

Since: 2018.3

------------------------------------------------------------------------

### ostree_deployment_is_staged ()

``` programlisting
gboolean
ostree_deployment_is_staged (OstreeDeployment *self);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

`TRUE` if deployment should be "finalized" at shutdown time

Since: 2018.3

------------------------------------------------------------------------

### ostree_deployment_is_finalization_locked ()

``` programlisting
gboolean
ostree_deployment_is_finalization_locked
                               (OstreeDeployment *self);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

`TRUE` if deployment is queued to be "finalized" at shutdown time, but requires additional action.

Since: 2023.8

------------------------------------------------------------------------

### ostree_deployment_is_soft_reboot_target ()

``` programlisting
gboolean
ostree_deployment_is_soft_reboot_target
                               (OstreeDeployment *self);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

`TRUE` if deployment is set for a soft reboot.

Since: 2025.3

------------------------------------------------------------------------

### ostree_deployment_set_index ()

``` programlisting
void
ostree_deployment_set_index (OstreeDeployment *self,
                             int index);
```

Sets the global index into the bootloader ordering.

#### Parameters

|       |                                |     |
|-------|--------------------------------|-----|
| self  | Deployment                     |     |
| index | Index into bootloader ordering |     |

------------------------------------------------------------------------

### ostree_deployment_set_bootserial ()

``` programlisting
void
ostree_deployment_set_bootserial (OstreeDeployment *self,
                                  int index);
```

Should never have been made public API; don't use this.

#### Parameters

|       |                |     |
|-------|----------------|-----|
| self  | Deployment     |     |
| index | Don't use this |     |

------------------------------------------------------------------------

### ostree_deployment_set_bootconfig ()

``` programlisting
void
ostree_deployment_set_bootconfig (OstreeDeployment *self,
                                  OstreeBootconfigParser *bootconfig);
```

Set or clear the bootloader configuration.

#### Parameters

|            |                                  |              |
|------------|----------------------------------|--------------|
| self       | Deployment                       |              |
| bootconfig | Bootloader configuration object. | \[nullable\] |

------------------------------------------------------------------------

### ostree_deployment_set_origin ()

``` programlisting
void
ostree_deployment_set_origin (OstreeDeployment *self,
                              GKeyFile *origin);
```

Replace the "origin", which is a description of the source of the deployment and how to update to the next version.

#### Parameters

|        |                                     |              |
|--------|-------------------------------------|--------------|
| self   | Deployment                          |              |
| origin | Set the origin for this deployment. | \[nullable\] |

------------------------------------------------------------------------

### ostree_deployment_origin_remove_transient_state ()

``` programlisting
void
ostree_deployment_origin_remove_transient_state
                               (GKeyFile *origin);
```

The intention of an origin file is primarily describe the "inputs" that resulted in a deployment, and it's commonly used to derive the new state. For example, a key value (in pure libostree mode) is the "refspec". However, libostree (or other applications) may want to store "transient" state that should not be carried across upgrades.

This function just removes all members of the `libostree-transient` group. The name of that group is available to all libostree users; best practice would be to prefix values underneath there with a short identifier for your software.

Additionally, this function will remove the `origin/unlocked` and `origin/override-commit` members; these should be considered transient state that should have been under an explicit group.

#### Parameters

|        |           |     |
|--------|-----------|-----|
| origin | An origin |     |

Since: 2018.3

------------------------------------------------------------------------

### ostree_deployment_clone ()

``` programlisting
OstreeDeployment *
ostree_deployment_clone (OstreeDeployment *self);
```

#### Parameters

|      |            |     |
|------|------------|-----|
| self | Deployment |     |

#### Returns

New deep copy of *`self`* .

\[not nullable\]\[transfer full\]

------------------------------------------------------------------------

### ostree_deployment_unlocked_state_to_string ()

``` programlisting
const char *
ostree_deployment_unlocked_state_to_string
                               (OstreeDeploymentUnlockedState state);
```

#### Returns

Description of state.

\[not nullable\]

Since: 2016.4

## Types and Values

### OstreeDeployment

``` programlisting
typedef struct {
  GObject parent_instance;

  int index;
  char *osname;
  char *csum;
  int deployserial;
  char *bootcsum;
  int bootserial;
  OstreeBootconfigParser *bootconfig;
  GKeyFile *origin;
  OstreeDeploymentUnlockedState unlocked;
  gboolean staged;
  gboolean finalization_locked;
  gboolean soft_reboot_target;
  char **overlay_initrds;
  char *overlay_initrds_id;

  // Private cache of expected backing device/inode
  gboolean devino_initialized;
  dev_t device;
  ino_t inode;
} OstreeDeployment;
```

#### Members

|  |  |  |
|----|----|----|
| int *`index`*; | Global offset |   |
| char \**`osname`*; |   |   |
| char \**`csum`*; | OSTree checksum of tree |   |
| int *`deployserial`*; | How many times this particular csum appears in deployment list |   |
| char \**`bootcsum`*; | Checksum of kernel+initramfs |   |
| int *`bootserial`*; | An integer assigned to this tree per its \${bootcsum} |   |
| [OstreeBootconfigParser](reference__ostree-ostree-bootconfig-parser.md#OstreeBootconfigParser "OstreeBootconfigParser") \**`bootconfig`*; | Bootloader configuration |   |
| GKeyFile \**`origin`*; | How to construct an upgraded version of this tree |   |
| OstreeDeploymentUnlockedState *`unlocked`*; | The unlocked state |   |
| gboolean *`staged`*; | TRUE iff this deployment is staged |   |
| gboolean *`finalization_locked`*; |   |   |
| gboolean *`soft_reboot_target`*; |   |   |
| char \*\**`overlay_initrds`*; | Checksums of staged additional initrds for this deployment |   |
| char \**`overlay_initrds_id`*; | Unique ID generated from initrd checksums; used to compare deployments |   |
| gboolean *`devino_initialized`*; |   |   |
| dev_t *`device`*; |   |   |
| ino_t *`inode`*; |   |   |

------------------------------------------------------------------------
