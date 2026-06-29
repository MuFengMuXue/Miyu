[TABLE]

## Functions

|  |  |
|----|----|
| gboolean | [ostree_repo_file_ensure_resolved](reference__ostree-ostree-repo-file.md#ostree-repo-file-ensure-resolved "ostree_repo_file_ensure_resolved ()") () |
| gboolean | [ostree_repo_file_get_xattrs](reference__ostree-ostree-repo-file.md#ostree-repo-file-get-xattrs "ostree_repo_file_get_xattrs ()") () |
| [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") \* | [ostree_repo_file_get_repo](reference__ostree-ostree-repo-file.md#ostree-repo-file-get-repo "ostree_repo_file_get_repo ()") () |
| [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") \* | [ostree_repo_file_get_root](reference__ostree-ostree-repo-file.md#ostree-repo-file-get-root "ostree_repo_file_get_root ()") () |
| void | [ostree_repo_file_tree_set_metadata](reference__ostree-ostree-repo-file.md#ostree-repo-file-tree-set-metadata "ostree_repo_file_tree_set_metadata ()") () |
| const char \* | [ostree_repo_file_tree_get_contents_checksum](reference__ostree-ostree-repo-file.md#ostree-repo-file-tree-get-contents-checksum "ostree_repo_file_tree_get_contents_checksum ()") () |
| const char \* | [ostree_repo_file_tree_get_metadata_checksum](reference__ostree-ostree-repo-file.md#ostree-repo-file-tree-get-metadata-checksum "ostree_repo_file_tree_get_metadata_checksum ()") () |
| GVariant \* | [ostree_repo_file_tree_get_contents](reference__ostree-ostree-repo-file.md#ostree-repo-file-tree-get-contents "ostree_repo_file_tree_get_contents ()") () |
| GVariant \* | [ostree_repo_file_tree_get_metadata](reference__ostree-ostree-repo-file.md#ostree-repo-file-tree-get-metadata "ostree_repo_file_tree_get_metadata ()") () |
| const char \* | [ostree_repo_file_get_checksum](reference__ostree-ostree-repo-file.md#ostree-repo-file-get-checksum "ostree_repo_file_get_checksum ()") () |
| int | [ostree_repo_file_tree_find_child](reference__ostree-ostree-repo-file.md#ostree-repo-file-tree-find-child "ostree_repo_file_tree_find_child ()") () |
| gboolean | [ostree_repo_file_tree_query_child](reference__ostree-ostree-repo-file.md#ostree-repo-file-tree-query-child "ostree_repo_file_tree_query_child ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") |

## Description

## Functions

### ostree_repo_file_ensure_resolved ()

``` programlisting
gboolean
ostree_repo_file_ensure_resolved (OstreeRepoFile *self,
                                  GError **error);
```

Ensure that the backing metadata is loaded.

#### Parameters

|       |             |     |
|-------|-------------|-----|
| self  | A repo file |     |
| error | Error       |     |

#### Returns

`FALSE` if the operation failed, `TRUE` otherwise

------------------------------------------------------------------------

### ostree_repo_file_get_xattrs ()

``` programlisting
gboolean
ostree_repo_file_get_xattrs (OstreeRepoFile *self,
                             GVariant **out_xattrs,
                             GCancellable *cancellable,
                             GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| self | [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") |   |
| out_xattrs | the extended attributes. | \[out\]\[optional\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_repo_file_get_repo ()

``` programlisting
OstreeRepo *
ostree_repo_file_get_repo (OstreeRepoFile *self);
```

#### Returns

Repository.

\[transfer none\]

------------------------------------------------------------------------

### ostree_repo_file_get_root ()

``` programlisting
OstreeRepoFile *
ostree_repo_file_get_root (OstreeRepoFile *self);
```

#### Returns

The root directory for the commit referenced by this file.

\[transfer none\]

------------------------------------------------------------------------

### ostree_repo_file_tree_set_metadata ()

``` programlisting
void
ostree_repo_file_tree_set_metadata (OstreeRepoFile *self,
                                    const char *checksum,
                                    GVariant *metadata);
```

Replace the metadata checksum and metadata object.

#### Parameters

|      |             |     |
|------|-------------|-----|
| self | A repo file |     |

------------------------------------------------------------------------

### ostree_repo_file_tree_get_contents_checksum ()

``` programlisting
const char *
ostree_repo_file_tree_get_contents_checksum
                               (OstreeRepoFile *self);
```

#### Parameters

|      |             |     |
|------|-------------|-----|
| self | A repo file |     |

#### Returns

The SHA256 digest of the content object, or `NULL` if this is not a directory.

\[nullable\]

------------------------------------------------------------------------

### ostree_repo_file_tree_get_metadata_checksum ()

``` programlisting
const char *
ostree_repo_file_tree_get_metadata_checksum
                               (OstreeRepoFile *self);
```

#### Parameters

|      |             |     |
|------|-------------|-----|
| self | A repo file |     |

#### Returns

The SHA256 digest of the metadata object, or `NULL` if this is not a directory.

\[nullable\]

------------------------------------------------------------------------

### ostree_repo_file_tree_get_contents ()

``` programlisting
GVariant *
ostree_repo_file_tree_get_contents (OstreeRepoFile *self);
```

This API will return `NULL` if the file is not "resolved" i.e. in a loaded state. It will also return `NULL` if this path is not a directory tree.

#### Parameters

|      |             |     |
|------|-------------|-----|
| self | A repo file |     |

#### Returns

The GVariant representing the children of this directory.

\[nullable\]

------------------------------------------------------------------------

### ostree_repo_file_tree_get_metadata ()

``` programlisting
GVariant *
ostree_repo_file_tree_get_metadata (OstreeRepoFile *self);
```

This API will return `NULL` if the file is not "resolved" i.e. in a loaded state. It will also return `NULL` if this path is not a directory tree.

#### Parameters

|      |             |     |
|------|-------------|-----|
| self | A repo file |     |

#### Returns

The GVariant representing the metadata for this directory.

\[nullable\]

------------------------------------------------------------------------

### ostree_repo_file_get_checksum ()

``` programlisting
const char *
ostree_repo_file_get_checksum (OstreeRepoFile *self);
```

------------------------------------------------------------------------

### ostree_repo_file_tree_find_child ()

``` programlisting
int
ostree_repo_file_tree_find_child (OstreeRepoFile *self,
                                  const char *name,
                                  gboolean *is_dir,
                                  GVariant **out_container);
```

#### Parameters

|  |  |  |
|----|----|----|
| self | [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") |   |
| name | name of the child |   |
| is_dir | . | \[out caller-allocates\] |
| out_container | . | \[out\] |

------------------------------------------------------------------------

### ostree_repo_file_tree_query_child ()

``` programlisting
gboolean
ostree_repo_file_tree_query_child (OstreeRepoFile *self,
                                   int n,
                                   const char *attributes,
                                   GFileQueryInfoFlags flags,
                                   GFileInfo **out_info,
                                   GCancellable *cancellable,
                                   GError **error);
```

#### Parameters

|  |  |  |
|----|----|----|
| self | [OstreeRepoFile](reference__ostree-ostree-repo-file.md#OstreeRepoFile "OstreeRepoFile") |   |
| n | the child number |   |
| attributes | an attribute string to match, see `g_file_attribute_matcher_new()` |   |
| flags | a GFileQueryInfoFlags |   |
| out_info | the GFileInfo of the child. | \[out\]\[transfer full\]\[optional\] |
| cancellable | a GCancellable or `NULL` |   |
| error | a GError or `NULL` |   |

#### Returns

`TRUE` on success and the *`out_info`* is set, `FALSE` otherwise.

## Types and Values

### OstreeRepoFile

``` programlisting
typedef struct OstreeRepoFile OstreeRepoFile;
```

------------------------------------------------------------------------
