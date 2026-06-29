[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") \* | [ostree_mutable_tree_new](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-new "ostree_mutable_tree_new ()") () |
| [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") \* | [ostree_mutable_tree_new_from_commit](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-new-from-commit "ostree_mutable_tree_new_from_commit ()") () |
| [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") \* | [ostree_mutable_tree_new_from_checksum](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-new-from-checksum "ostree_mutable_tree_new_from_checksum ()") () |
| gboolean | [ostree_mutable_tree_check_error](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-check-error "ostree_mutable_tree_check_error ()") () |
| void | [ostree_mutable_tree_set_metadata_checksum](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-set-metadata-checksum "ostree_mutable_tree_set_metadata_checksum ()") () |
| const char \* | [ostree_mutable_tree_get_metadata_checksum](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-get-metadata-checksum "ostree_mutable_tree_get_metadata_checksum ()") () |
| void | [ostree_mutable_tree_set_contents_checksum](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-set-contents-checksum "ostree_mutable_tree_set_contents_checksum ()") () |
| const char \* | [ostree_mutable_tree_get_contents_checksum](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-get-contents-checksum "ostree_mutable_tree_get_contents_checksum ()") () |
| gboolean | [ostree_mutable_tree_replace_file](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-replace-file "ostree_mutable_tree_replace_file ()") () |
| gboolean | [ostree_mutable_tree_remove](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-remove "ostree_mutable_tree_remove ()") () |
| gboolean | [ostree_mutable_tree_ensure_dir](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-ensure-dir "ostree_mutable_tree_ensure_dir ()") () |
| gboolean | [ostree_mutable_tree_lookup](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-lookup "ostree_mutable_tree_lookup ()") () |
| gboolean | [ostree_mutable_tree_ensure_parent_dirs](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-ensure-parent-dirs "ostree_mutable_tree_ensure_parent_dirs ()") () |
| gboolean | [ostree_mutable_tree_walk](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-walk "ostree_mutable_tree_walk ()") () |
| GHashTable \* | [ostree_mutable_tree_get_subdirs](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-get-subdirs "ostree_mutable_tree_get_subdirs ()") () |
| GHashTable \* | [ostree_mutable_tree_get_files](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-get-files "ostree_mutable_tree_get_files ()") () |
| gboolean | [ostree_mutable_tree_fill_empty_from_dirtree](reference__ostree-In-memory-modifiable-filesystem-tree.md#ostree-mutable-tree-fill-empty-from-dirtree "ostree_mutable_tree_fill_empty_from_dirtree ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") |

## Description

In order to commit content into an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo"), it must first be imported into an [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree"). There are several high level APIs to create an initiable [OstreeMutableTree](reference__ostree-In-memory-modifiable-filesystem-tree.md#OstreeMutableTree "OstreeMutableTree") from a physical filesystem directory, but they may also be computed programmatically.

## Functions

### ostree_mutable_tree_new ()

``` programlisting
OstreeMutableTree *
ostree_mutable_tree_new (void);
```

#### Returns

A new tree.

\[transfer full\]

------------------------------------------------------------------------

### ostree_mutable_tree_new_from_commit ()

``` programlisting
OstreeMutableTree *
ostree_mutable_tree_new_from_commit (OstreeRepo *repo,
                                     const char *rev,
                                     GError **error);
```

Creates a new OstreeMutableTree with the contents taken from the given commit. The data will be loaded from the repo lazily as needed.

#### Parameters

|      |                                                               |     |
|------|---------------------------------------------------------------|-----|
| repo | The repo which contains the objects refered by the checksums. |     |
| rev  | ref or SHA-256 checksum                                       |     |

#### Returns

A new tree.

\[transfer full\]

Since: 2021.5

------------------------------------------------------------------------

### ostree_mutable_tree_new_from_checksum ()

``` programlisting
OstreeMutableTree *
ostree_mutable_tree_new_from_checksum (OstreeRepo *repo,
                                       const char *contents_checksum,
                                       const char *metadata_checksum);
```

Creates a new OstreeMutableTree with the contents taken from the given repo and checksums. The data will be loaded from the repo lazily as needed.

#### Parameters

|  |  |  |
|----|----|----|
| repo | The repo which contains the objects refered by the checksums. |   |
| contents_checksum | dirtree checksum |   |
| metadata_checksum | dirmeta checksum |   |

#### Returns

A new tree.

\[transfer full\]

Since: 2018.7

------------------------------------------------------------------------

### ostree_mutable_tree_check_error ()

``` programlisting
gboolean
ostree_mutable_tree_check_error (OstreeMutableTree *self,
                                 GError **error);
```

In some cases, a tree may be in a "lazy" state that loads data in the background; if an error occurred during a non-throwing API call, it will have been cached. This function checks for a cached error. The tree remains in error state.

#### Parameters

|      |      |     |
|------|------|-----|
| self | Tree |     |

#### Returns

`TRUE` on success

Since: 2018.7

------------------------------------------------------------------------

### ostree_mutable_tree_set_metadata_checksum ()

``` programlisting
void
ostree_mutable_tree_set_metadata_checksum
                               (OstreeMutableTree *self,
                                const char *checksum);
```

------------------------------------------------------------------------

### ostree_mutable_tree_get_metadata_checksum ()

``` programlisting
const char *
ostree_mutable_tree_get_metadata_checksum
                               (OstreeMutableTree *self);
```

------------------------------------------------------------------------

### ostree_mutable_tree_set_contents_checksum ()

``` programlisting
void
ostree_mutable_tree_set_contents_checksum
                               (OstreeMutableTree *self,
                                const char *checksum);
```

------------------------------------------------------------------------

### ostree_mutable_tree_get_contents_checksum ()

``` programlisting
const char *
ostree_mutable_tree_get_contents_checksum
                               (OstreeMutableTree *self);
```

------------------------------------------------------------------------

### ostree_mutable_tree_replace_file ()

``` programlisting
gboolean
ostree_mutable_tree_replace_file (OstreeMutableTree *self,
                                  const char *name,
                                  const char *checksum,
                                  GError **error);
```

------------------------------------------------------------------------

### ostree_mutable_tree_remove ()

``` programlisting
gboolean
ostree_mutable_tree_remove (OstreeMutableTree *self,
                            const char *name,
                            gboolean allow_noent,
                            GError **error);
```

Remove the file or subdirectory named *`name`* from the mutable tree *`self`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Tree |   |
| name | Name of file or subdirectory to remove |   |
| allow_noent | If *`FALSE`* , an error will be thrown if *`name`* does not exist in the tree |   |
| error | a GError |   |

Since: 2018.9

------------------------------------------------------------------------

### ostree_mutable_tree_ensure_dir ()

``` programlisting
gboolean
ostree_mutable_tree_ensure_dir (OstreeMutableTree *self,
                                const char *name,
                                OstreeMutableTree **out_subdir,
                                GError **error);
```

Returns the subdirectory of self with filename *`name`* , creating an empty one it if it doesn't exist.

#### Parameters

|  |  |  |
|----|----|----|
| self | Tree |   |
| name | Name of subdirectory of self to retrieve/creates |   |
| out_subdir | the subdirectory. | \[out\]\[transfer full\]\[optional\] |
| error | a GError |   |

------------------------------------------------------------------------

### ostree_mutable_tree_lookup ()

``` programlisting
gboolean
ostree_mutable_tree_lookup (OstreeMutableTree *self,
                            const char *name,
                            char **out_file_checksum,
                            OstreeMutableTree **out_subdir,
                            GError **error);
```

Lookup *`name`* and returns *`out_file_checksum`* or *`out_subdir`* depending on its file type.

#### Parameters

|  |  |  |
|----|----|----|
| self | Tree |   |
| name | name |   |
| out_file_checksum | checksum. | \[out\]\[transfer full\]\[nullable\]\[optional\] |
| out_subdir | subdirectory. | \[out\]\[transfer full\]\[nullable\]\[optional\] |
| error | a GError |   |

#### Returns

`TRUE` on success and either *`out_file_checksum`* or *`out_subdir`* are filled, `FALSE` otherwise.

------------------------------------------------------------------------

### ostree_mutable_tree_ensure_parent_dirs ()

``` programlisting
gboolean
ostree_mutable_tree_ensure_parent_dirs
                               (OstreeMutableTree *self,
                                GPtrArray *split_path,
                                const char *metadata_checksum,
                                OstreeMutableTree **out_parent,
                                GError **error);
```

Create all parent trees necessary for the given *`split_path`* to exist.

#### Parameters

|  |  |  |
|----|----|----|
| self | Tree |   |
| split_path | File path components. | \[element-type utf8\] |
| metadata_checksum | SHA256 checksum for metadata |   |
| out_parent | The parent tree. | \[out\]\[transfer full\]\[optional\] |
| error | a GError |   |

------------------------------------------------------------------------

### ostree_mutable_tree_walk ()

``` programlisting
gboolean
ostree_mutable_tree_walk (OstreeMutableTree *self,
                          GPtrArray *split_path,
                          guint start,
                          OstreeMutableTree **out_subdir,
                          GError **error);
```

Traverse *`start`* number of elements starting from *`split_path`* ; the child will be returned in *`out_subdir`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | Tree |   |
| split_path | Split pathname. | \[element-type utf8\] |
| start | Descend from this number of elements in *`split_path`* |   |
| out_subdir | Target parent. | \[out\]\[transfer full\] |
| error | Error |   |

------------------------------------------------------------------------

### ostree_mutable_tree_get_subdirs ()

``` programlisting
GHashTable *
ostree_mutable_tree_get_subdirs (OstreeMutableTree *self);
```

#### Returns

All children directories.

\[transfer none\]\[element-type utf8 OstreeMutableTree\]

------------------------------------------------------------------------

### ostree_mutable_tree_get_files ()

``` programlisting
GHashTable *
ostree_mutable_tree_get_files (OstreeMutableTree *self);
```

#### Returns

All children files (the value is a checksum).

\[transfer none\]\[element-type utf8 utf8\]

------------------------------------------------------------------------

### ostree_mutable_tree_fill_empty_from_dirtree ()

``` programlisting
gboolean
ostree_mutable_tree_fill_empty_from_dirtree
                               (OstreeMutableTree *self,
                                OstreeRepo *repo,
                                const char *contents_checksum,
                                const char *metadata_checksum);
```

Merges *`self`* with the tree given by *`contents_checksum`* and *`metadata_checksum`* , but only if it's possible without writing new objects to the *`repo`* . We can do this if either *`self`* is empty, the tree given by *`contents_checksum`* is empty or if both trees already have the same *`contents_checksum`* .

#### Returns

*`TRUE`* if merge was successful, *`FALSE`* if it was not possible.

This function enables optimisations when composing trees. The provided checksums are not loaded or checked when this function is called. Instead the contents will be loaded only when needed.

Since: 2018.7

## Types and Values

### OstreeMutableTree

``` programlisting
typedef struct OstreeMutableTree OstreeMutableTree;
```

Private instance structure.

------------------------------------------------------------------------
