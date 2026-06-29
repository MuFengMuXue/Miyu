[TABLE]

## Functions

|  |  |
|----|----|
| \#define | [OSTREE_OBJECT_TYPE_IS_META](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-IS-META:CAPS "OSTREE_OBJECT_TYPE_IS_META()")() |
| const GVariantType \* | [ostree_metadata_variant_type](reference__ostree-Core-repository-independent-functions.md#ostree-metadata-variant-type "ostree_metadata_variant_type ()") () |
| gboolean | [ostree_validate_checksum_string](reference__ostree-Core-repository-independent-functions.md#ostree-validate-checksum-string "ostree_validate_checksum_string ()") () |
| gboolean | [ostree_validate_collection_id](reference__ostree-Core-repository-independent-functions.md#ostree-validate-collection-id "ostree_validate_collection_id ()") () |
| guchar \* | [ostree_checksum_to_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-to-bytes "ostree_checksum_to_bytes ()") () |
| GVariant \* | [ostree_checksum_to_bytes_v](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-to-bytes-v "ostree_checksum_to_bytes_v ()") () |
| char \* | [ostree_checksum_from_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-from-bytes "ostree_checksum_from_bytes ()") () |
| char \* | [ostree_checksum_from_bytes_v](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-from-bytes-v "ostree_checksum_from_bytes_v ()") () |
| void | [ostree_checksum_inplace_from_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-inplace-from-bytes "ostree_checksum_inplace_from_bytes ()") () |
| void | [ostree_checksum_inplace_to_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-inplace-to-bytes "ostree_checksum_inplace_to_bytes ()") () |
| const guchar \* | [ostree_checksum_bytes_peek](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-bytes-peek "ostree_checksum_bytes_peek ()") () |
| const guchar \* | [ostree_checksum_bytes_peek_validate](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-bytes-peek-validate "ostree_checksum_bytes_peek_validate ()") () |
| char \* | [ostree_checksum_b64_from_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-b64-from-bytes "ostree_checksum_b64_from_bytes ()") () |
| guchar \* | [ostree_checksum_b64_to_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-b64-to-bytes "ostree_checksum_b64_to_bytes ()") () |
| void | [ostree_checksum_b64_inplace_from_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-b64-inplace-from-bytes "ostree_checksum_b64_inplace_from_bytes ()") () |
| void | [ostree_checksum_b64_inplace_to_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-b64-inplace-to-bytes "ostree_checksum_b64_inplace_to_bytes ()") () |
| int | [ostree_cmp_checksum_bytes](reference__ostree-Core-repository-independent-functions.md#ostree-cmp-checksum-bytes "ostree_cmp_checksum_bytes ()") () |
| gboolean | [ostree_validate_rev](reference__ostree-Core-repository-independent-functions.md#ostree-validate-rev "ostree_validate_rev ()") () |
| gboolean | [ostree_validate_remote_name](reference__ostree-Core-repository-independent-functions.md#ostree-validate-remote-name "ostree_validate_remote_name ()") () |
| gboolean | [ostree_parse_refspec](reference__ostree-Core-repository-independent-functions.md#ostree-parse-refspec "ostree_parse_refspec ()") () |
| const char \* | [ostree_object_type_to_string](reference__ostree-Core-repository-independent-functions.md#ostree-object-type-to-string "ostree_object_type_to_string ()") () |
| [OstreeObjectType](reference__ostree-Core-repository-independent-functions.md#OstreeObjectType "enum OstreeObjectType") | [ostree_object_type_from_string](reference__ostree-Core-repository-independent-functions.md#ostree-object-type-from-string "ostree_object_type_from_string ()") () |
| guint | [ostree_hash_object_name](reference__ostree-Core-repository-independent-functions.md#ostree-hash-object-name "ostree_hash_object_name ()") () |
| GVariant \* | [ostree_object_name_serialize](reference__ostree-Core-repository-independent-functions.md#ostree-object-name-serialize "ostree_object_name_serialize ()") () |
| void | [ostree_object_name_deserialize](reference__ostree-Core-repository-independent-functions.md#ostree-object-name-deserialize "ostree_object_name_deserialize ()") () |
| char \* | [ostree_object_to_string](reference__ostree-Core-repository-independent-functions.md#ostree-object-to-string "ostree_object_to_string ()") () |
| void | [ostree_object_from_string](reference__ostree-Core-repository-independent-functions.md#ostree-object-from-string "ostree_object_from_string ()") () |
| gboolean | [ostree_content_stream_parse](reference__ostree-Core-repository-independent-functions.md#ostree-content-stream-parse "ostree_content_stream_parse ()") () |
| gboolean | [ostree_content_file_parse](reference__ostree-Core-repository-independent-functions.md#ostree-content-file-parse "ostree_content_file_parse ()") () |
| gboolean | [ostree_content_file_parse_at](reference__ostree-Core-repository-independent-functions.md#ostree-content-file-parse-at "ostree_content_file_parse_at ()") () |
| gboolean | [ostree_raw_file_to_archive_z2_stream](reference__ostree-Core-repository-independent-functions.md#ostree-raw-file-to-archive-z2-stream "ostree_raw_file_to_archive_z2_stream ()") () |
| gboolean | [ostree_raw_file_to_archive_z2_stream_with_options](reference__ostree-Core-repository-independent-functions.md#ostree-raw-file-to-archive-z2-stream-with-options "ostree_raw_file_to_archive_z2_stream_with_options ()") () |
| gboolean | [ostree_raw_file_to_content_stream](reference__ostree-Core-repository-independent-functions.md#ostree-raw-file-to-content-stream "ostree_raw_file_to_content_stream ()") () |
| gboolean | [ostree_break_hardlink](reference__ostree-Core-repository-independent-functions.md#ostree-break-hardlink "ostree_break_hardlink ()") () |
| gboolean | [ostree_checksum_file_from_input](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file-from-input "ostree_checksum_file_from_input ()") () |
| gboolean | [ostree_checksum_file](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file "ostree_checksum_file ()") () |
| gboolean | [ostree_checksum_file_at](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file-at "ostree_checksum_file_at ()") () |
| void | [ostree_checksum_file_async](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file-async "ostree_checksum_file_async ()") () |
| gboolean | [ostree_checksum_file_async_finish](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file-async-finish "ostree_checksum_file_async_finish ()") () |
| GVariant \* | [ostree_fs_get_all_xattrs](reference__ostree-Core-repository-independent-functions.md#ostree-fs-get-all-xattrs "ostree_fs_get_all_xattrs ()") () |
| GVariant \* | [ostree_fs_get_all_xattrs_at](reference__ostree-Core-repository-independent-functions.md#ostree-fs-get-all-xattrs-at "ostree_fs_get_all_xattrs_at ()") () |
| GVariant \* | [ostree_create_directory_metadata](reference__ostree-Core-repository-independent-functions.md#ostree-create-directory-metadata "ostree_create_directory_metadata ()") () |
| gboolean | [ostree_validate_structureof_objtype](reference__ostree-Core-repository-independent-functions.md#ostree-validate-structureof-objtype "ostree_validate_structureof_objtype ()") () |
| gboolean | [ostree_validate_structureof_csum_v](reference__ostree-Core-repository-independent-functions.md#ostree-validate-structureof-csum-v "ostree_validate_structureof_csum_v ()") () |
| gboolean | [ostree_validate_structureof_checksum_string](reference__ostree-Core-repository-independent-functions.md#ostree-validate-structureof-checksum-string "ostree_validate_structureof_checksum_string ()") () |
| gboolean | [ostree_validate_structureof_file_mode](reference__ostree-Core-repository-independent-functions.md#ostree-validate-structureof-file-mode "ostree_validate_structureof_file_mode ()") () |
| gboolean | [ostree_validate_structureof_commit](reference__ostree-Core-repository-independent-functions.md#ostree-validate-structureof-commit "ostree_validate_structureof_commit ()") () |
| gboolean | [ostree_validate_structureof_dirtree](reference__ostree-Core-repository-independent-functions.md#ostree-validate-structureof-dirtree "ostree_validate_structureof_dirtree ()") () |
| gboolean | [ostree_validate_structureof_dirmeta](reference__ostree-Core-repository-independent-functions.md#ostree-validate-structureof-dirmeta "ostree_validate_structureof_dirmeta ()") () |
| gchar \* | [ostree_commit_get_parent](reference__ostree-Core-repository-independent-functions.md#ostree-commit-get-parent "ostree_commit_get_parent ()") () |
| guint64 | [ostree_commit_get_timestamp](reference__ostree-Core-repository-independent-functions.md#ostree-commit-get-timestamp "ostree_commit_get_timestamp ()") () |
| gboolean | [ostree_commit_metadata_for_bootable](reference__ostree-Core-repository-independent-functions.md#ostree-commit-metadata-for-bootable "ostree_commit_metadata_for_bootable ()") () |
| gchar \* | [ostree_commit_get_content_checksum](reference__ostree-Core-repository-independent-functions.md#ostree-commit-get-content-checksum "ostree_commit_get_content_checksum ()") () |
| gboolean | [ostree_commit_get_object_sizes](reference__ostree-Core-repository-independent-functions.md#ostree-commit-get-object-sizes "ostree_commit_get_object_sizes ()") () |
| OstreeCommitSizesEntry \* | [ostree_commit_sizes_entry_new](reference__ostree-Core-repository-independent-functions.md#ostree-commit-sizes-entry-new "ostree_commit_sizes_entry_new ()") () |
| OstreeCommitSizesEntry \* | [ostree_commit_sizes_entry_copy](reference__ostree-Core-repository-independent-functions.md#ostree-commit-sizes-entry-copy "ostree_commit_sizes_entry_copy ()") () |
| void | [ostree_commit_sizes_entry_free](reference__ostree-Core-repository-independent-functions.md#ostree-commit-sizes-entry-free "ostree_commit_sizes_entry_free ()") () |
| gboolean | [ostree_check_version](reference__ostree-Core-repository-independent-functions.md#ostree-check-version "ostree_check_version ()") () |

## Types and Values

|  |  |
|----|----|
| \#define | [OSTREE_MAX_METADATA_SIZE](reference__ostree-Core-repository-independent-functions.md#OSTREE-MAX-METADATA-SIZE:CAPS "OSTREE_MAX_METADATA_SIZE") |
| \#define | [OSTREE_MAX_METADATA_WARN_SIZE](reference__ostree-Core-repository-independent-functions.md#OSTREE-MAX-METADATA-WARN-SIZE:CAPS "OSTREE_MAX_METADATA_WARN_SIZE") |
| enum | [OstreeObjectType](reference__ostree-Core-repository-independent-functions.md#OstreeObjectType "enum OstreeObjectType") |
| \#define | [OSTREE_OBJECT_TYPE_LAST](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-LAST:CAPS "OSTREE_OBJECT_TYPE_LAST") |
| \#define | [OSTREE_DIRMETA_GVARIANT_STRING](reference__ostree-Core-repository-independent-functions.md#OSTREE-DIRMETA-GVARIANT-STRING:CAPS "OSTREE_DIRMETA_GVARIANT_STRING") |
| \#define | [OSTREE_DIRMETA_GVARIANT_FORMAT](reference__ostree-Core-repository-independent-functions.md#OSTREE-DIRMETA-GVARIANT-FORMAT:CAPS "OSTREE_DIRMETA_GVARIANT_FORMAT") |
| \#define | [OSTREE_FILEMETA_GVARIANT_STRING](reference__ostree-Core-repository-independent-functions.md#OSTREE-FILEMETA-GVARIANT-STRING:CAPS "OSTREE_FILEMETA_GVARIANT_STRING") |
| \#define | [OSTREE_FILEMETA_GVARIANT_FORMAT](reference__ostree-Core-repository-independent-functions.md#OSTREE-FILEMETA-GVARIANT-FORMAT:CAPS "OSTREE_FILEMETA_GVARIANT_FORMAT") |
| \#define | [OSTREE_TREE_GVARIANT_STRING](reference__ostree-Core-repository-independent-functions.md#OSTREE-TREE-GVARIANT-STRING:CAPS "OSTREE_TREE_GVARIANT_STRING") |
| \#define | [OSTREE_TREE_GVARIANT_FORMAT](reference__ostree-Core-repository-independent-functions.md#OSTREE-TREE-GVARIANT-FORMAT:CAPS "OSTREE_TREE_GVARIANT_FORMAT") |
| \#define | [OSTREE_COMMIT_GVARIANT_STRING](reference__ostree-Core-repository-independent-functions.md#OSTREE-COMMIT-GVARIANT-STRING:CAPS "OSTREE_COMMIT_GVARIANT_STRING") |
| \#define | [OSTREE_COMMIT_GVARIANT_FORMAT](reference__ostree-Core-repository-independent-functions.md#OSTREE-COMMIT-GVARIANT-FORMAT:CAPS "OSTREE_COMMIT_GVARIANT_FORMAT") |
| \#define | [OSTREE_SUMMARY_GVARIANT_STRING](reference__ostree-Core-repository-independent-functions.md#OSTREE-SUMMARY-GVARIANT-STRING:CAPS "OSTREE_SUMMARY_GVARIANT_STRING") |
| \#define | [OSTREE_SUMMARY_GVARIANT_FORMAT](reference__ostree-Core-repository-independent-functions.md#OSTREE-SUMMARY-GVARIANT-FORMAT:CAPS "OSTREE_SUMMARY_GVARIANT_FORMAT") |

## Description

These functions implement repository-independent algorithms for operating on the core OSTree data formats, such as converting GFileInfo into a GVariant.

There are 4 types of objects; file, dirmeta, tree, and commit. The last 3 are metadata, and the file object is the only content object type.

All metadata objects are stored as GVariant (big endian). The rationale for this is the same as that of the ext{2,3,4} family of filesystems; most developers will be using LE, and so it's better to continually test the BE-\>LE swap.

The file object is a custom format in order to support streaming.

## Functions

### OSTREE_OBJECT_TYPE_IS_META()

``` programlisting
#define OSTREE_OBJECT_TYPE_IS_META(t) (t >= 2 && t <= 6)
```

#### Parameters

|  |  |  |
|----|----|----|
| t | An [OstreeObjectType](reference__ostree-Core-repository-independent-functions.md#OstreeObjectType "enum OstreeObjectType") |   |

#### Returns

`TRUE` if object type is metadata

------------------------------------------------------------------------

### ostree_metadata_variant_type ()

``` programlisting
const GVariantType *
ostree_metadata_variant_type (OstreeObjectType objtype);
```

------------------------------------------------------------------------

### ostree_validate_checksum_string ()

``` programlisting
gboolean
ostree_validate_checksum_string (const char *sha256,
                                 GError **error);
```

Use this function to see if input strings are checksums.

#### Parameters

|        |                   |     |
|--------|-------------------|-----|
| sha256 | SHA256 hex string |     |
| error  | Error             |     |

#### Returns

`TRUE` if *`sha256`* is a valid checksum string, `FALSE` otherwise

------------------------------------------------------------------------

### ostree_validate_collection_id ()

``` programlisting
gboolean
ostree_validate_collection_id (const char *collection_id,
                               GError **error);
```

Check whether the given *`collection_id`* is valid. Return an error if it is invalid or `NULL`.

Valid collection IDs are reverse DNS names:

- They are composed of 1 or more elements separated by a period (`.`) character. All elements must contain at least one character.

- Each element must only contain the ASCII characters `[A-Z][a-z][0-9]_` and must not begin with a digit.

- They must contain at least one `.` (period) character (and thus at least two elements).

- They must not begin with a `.` (period) character.

- They must not exceed 255 characters in length.

(This makes their format identical to D-Bus interface names, for consistency.)

#### Parameters

|               |                  |              |
|---------------|------------------|--------------|
| collection_id | A collection ID. | \[nullable\] |
| error         | Error            |              |

#### Returns

`TRUE` if *`collection_id`* is a valid collection ID, `FALSE` if it is invalid or `NULL`

Since: 2018.6

------------------------------------------------------------------------

### ostree_checksum_to_bytes ()

``` programlisting
guchar *
ostree_checksum_to_bytes (const char *checksum);
```

#### Parameters

|          |                   |     |
|----------|-------------------|-----|
| checksum | An ASCII checksum |     |

#### Returns

Binary checksum from *`checksum`* of length 32; free with `g_free()`.

\[transfer full\]\[array fixed-size=32\]

------------------------------------------------------------------------

### ostree_checksum_to_bytes_v ()

``` programlisting
GVariant *
ostree_checksum_to_bytes_v (const char *checksum);
```

#### Parameters

|          |                   |     |
|----------|-------------------|-----|
| checksum | An ASCII checksum |     |

#### Returns

New GVariant of type ay with length 32.

\[transfer full\]

------------------------------------------------------------------------

### ostree_checksum_from_bytes ()

``` programlisting
char *
ostree_checksum_from_bytes (const guchar *csum);
```

#### Parameters

|      |                                  |                         |
|------|----------------------------------|-------------------------|
| csum | An binary checksum of length 32. | \[array fixed-size=32\] |

#### Returns

String form of *`csum`* .

\[transfer full\]

------------------------------------------------------------------------

### ostree_checksum_from_bytes_v ()

``` programlisting
char *
ostree_checksum_from_bytes_v (GVariant *csum_v);
```

#### Parameters

|        |                     |     |
|--------|---------------------|-----|
| csum_v | GVariant of type ay |     |

#### Returns

String form of *`csum_bytes`* .

\[transfer full\]

------------------------------------------------------------------------

### ostree_checksum_inplace_from_bytes ()

``` programlisting
void
ostree_checksum_inplace_from_bytes (const guchar *csum,
                                    char *buf);
```

Overwrite the contents of *`buf`* with stringified version of *`csum`* .

\[skip\]

#### Parameters

|  |  |  |
|----|----|----|
| csum | An binary checksum of length 32. | \[array fixed-size=32\] |
| buf | Output location, must be at least OSTREE_SHA256_STRING_LEN+1 bytes in length |   |

------------------------------------------------------------------------

### ostree_checksum_inplace_to_bytes ()

``` programlisting
void
ostree_checksum_inplace_to_bytes (const char *checksum,
                                  guchar *buf);
```

Convert *`checksum`* from a string to binary in-place, without allocating memory. Use this function in hot code paths.

#### Parameters

|          |                                               |     |
|----------|-----------------------------------------------|-----|
| checksum | a SHA256 string                               |     |
| buf      | Output buffer with at least 32 bytes of space |     |

------------------------------------------------------------------------

### ostree_checksum_bytes_peek ()

``` programlisting
const guchar *
ostree_checksum_bytes_peek (GVariant *bytes);
```

#### Parameters

|       |                     |     |
|-------|---------------------|-----|
| bytes | GVariant of type ay |     |

#### Returns

Binary checksum data in *`bytes`* ; do not free. If *`bytes`* does not have the correct length, return `NULL`.

\[transfer none\]\[array fixed-size=32\]\[element-type guint8\]

------------------------------------------------------------------------

### ostree_checksum_bytes_peek_validate ()

``` programlisting
const guchar *
ostree_checksum_bytes_peek_validate (GVariant *bytes,
                                     GError **error);
```

Like [`ostree_checksum_bytes_peek()`](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-bytes-peek "ostree_checksum_bytes_peek ()"), but also throws *`error`* .

#### Parameters

|       |                     |     |
|-------|---------------------|-----|
| bytes | GVariant of type ay |     |
| error | Errror              |     |

#### Returns

Binary checksum data.

\[transfer none\]\[array fixed-size=32\]\[element-type guint8\]

------------------------------------------------------------------------

### ostree_checksum_b64_from_bytes ()

``` programlisting
char *
ostree_checksum_b64_from_bytes (const guchar *csum);
```

#### Parameters

|      |                                  |                         |
|------|----------------------------------|-------------------------|
| csum | An binary checksum of length 32. | \[array fixed-size=32\] |

#### Returns

Modified base64 encoding of *`csum`*

The "modified" term refers to the fact that instead of '/', the '\_' character is used.

\[transfer full\]

Since: 2016.8

------------------------------------------------------------------------

### ostree_checksum_b64_to_bytes ()

``` programlisting
guchar *
ostree_checksum_b64_to_bytes (const char *checksum);
```

#### Parameters

|          |                   |     |
|----------|-------------------|-----|
| checksum | An ASCII checksum |     |

#### Returns

Binary version of *`checksum`* .

\[transfer full\]\[array fixed-size=32\]

Since: 2016.8

------------------------------------------------------------------------

### ostree_checksum_b64_inplace_from_bytes ()

``` programlisting
void
ostree_checksum_b64_inplace_from_bytes
                               (const guchar *csum,
                                char *buf);
```

Overwrite the contents of *`buf`* with modified base64 encoding of *`csum`* . The "modified" term refers to the fact that instead of '/', the '\_' character is used.

\[skip\]

#### Parameters

|  |  |  |
|----|----|----|
| csum | An binary checksum of length 32. | \[array fixed-size=32\] |
| buf | Output location, must be at least 44 bytes in length |   |

------------------------------------------------------------------------

### ostree_checksum_b64_inplace_to_bytes ()

``` programlisting
void
ostree_checksum_b64_inplace_to_bytes (const char *checksum,
                                      guint8 *buf);
```

Overwrite the contents of *`buf`* with stringified version of *`csum`* .

\[skip\]

#### Parameters

|  |  |  |
|----|----|----|
| checksum | An binary checksum of length 32. | \[array fixed-size=32\] |
| buf | Output location, must be at least 45 bytes in length |   |

------------------------------------------------------------------------

### ostree_cmp_checksum_bytes ()

``` programlisting
int
ostree_cmp_checksum_bytes (const guchar *a,
                           const guchar *b);
```

Compare two binary checksums, using `memcmp()`.

#### Parameters

|     |                   |     |
|-----|-------------------|-----|
| a   | A binary checksum |     |
| b   | A binary checksum |     |

------------------------------------------------------------------------

### ostree_validate_rev ()

``` programlisting
gboolean
ostree_validate_rev (const char *rev,
                     GError **error);
```

#### Parameters

|       |                   |     |
|-------|-------------------|-----|
| rev   | A revision string |     |
| error | Error             |     |

#### Returns

`TRUE` if *`rev`* is a valid ref string

------------------------------------------------------------------------

### ostree_validate_remote_name ()

``` programlisting
gboolean
ostree_validate_remote_name (const char *remote_name,
                             GError **error);
```

#### Parameters

|             |               |     |
|-------------|---------------|-----|
| remote_name | A remote name |     |
| error       | Error         |     |

#### Returns

`TRUE` if *`remote_name`* is a valid remote name

Since: 2017.8

------------------------------------------------------------------------

### ostree_parse_refspec ()

``` programlisting
gboolean
ostree_parse_refspec (const char *refspec,
                      char **out_remote,
                      char **out_ref,
                      GError **error);
```

Split a refspec like `gnome-ostree:gnome-ostree/buildmain` or just `gnome-ostree/buildmain` into two parts. In the first case, *`out_remote`* will be set to `gnome-ostree`, and *`out_ref`* to `gnome-ostree/buildmain`. In the second case (a local ref), *`out_remote`* will be `NULL`, and *`out_ref`* will be `gnome-ostree/buildmain`. In both cases, `TRUE` will be returned.

#### Parameters

|  |  |  |
|----|----|----|
| refspec | A "refspec" string |   |
| out_remote | Return location for the remote name, or `NULL` if the refspec refs to a local ref. | \[out\]\[nullable\]\[optional\] |
| out_ref | Return location for the ref name. | \[out\]\[not nullable\]\[optional\] |
| error | Error |   |

#### Returns

`TRUE` on successful parsing, `FALSE` otherwise

------------------------------------------------------------------------

### ostree_object_type_to_string ()

``` programlisting
const char *
ostree_object_type_to_string (OstreeObjectType objtype);
```

Serialize *`objtype`* to a string; this is used for file extensions.

#### Parameters

|  |  |  |
|----|----|----|
| objtype | an [OstreeObjectType](reference__ostree-Core-repository-independent-functions.md#OstreeObjectType "enum OstreeObjectType") |   |

------------------------------------------------------------------------

### ostree_object_type_from_string ()

``` programlisting
OstreeObjectType
ostree_object_type_from_string (const char *str);
```

The reverse of [`ostree_object_type_to_string()`](reference__ostree-Core-repository-independent-functions.md#ostree-object-type-to-string "ostree_object_type_to_string ()").

#### Parameters

|  |  |  |
|----|----|----|
| str | A stringified version of [OstreeObjectType](reference__ostree-Core-repository-independent-functions.md#OstreeObjectType "enum OstreeObjectType") |   |

------------------------------------------------------------------------

### ostree_hash_object_name ()

``` programlisting
guint
ostree_hash_object_name (gconstpointer a);
```

Use this function with GHashTable and [`ostree_object_name_serialize()`](reference__ostree-Core-repository-independent-functions.md#ostree-object-name-serialize "ostree_object_name_serialize ()").

#### Parameters

|     |                                           |     |
|-----|-------------------------------------------|-----|
| a   | A GVariant containing a serialized object |     |

------------------------------------------------------------------------

### ostree_object_name_serialize ()

``` programlisting
GVariant *
ostree_object_name_serialize (const char *checksum,
                              OstreeObjectType objtype);
```

#### Parameters

|          |                   |     |
|----------|-------------------|-----|
| checksum | An ASCII checksum |     |
| objtype  | An object type    |     |

#### Returns

A new floating GVariant containing checksum string and objtype.

\[transfer floating\]

------------------------------------------------------------------------

### ostree_object_name_deserialize ()

``` programlisting
void
ostree_object_name_deserialize (GVariant *variant,
                                const char **out_checksum,
                                OstreeObjectType *out_objtype);
```

Reverse [`ostree_object_name_serialize()`](reference__ostree-Core-repository-independent-functions.md#ostree-object-name-serialize "ostree_object_name_serialize ()"). Note that *`out_checksum`* is only valid for the lifetime of *`variant`* , and must not be freed.

#### Parameters

|  |  |  |
|----|----|----|
| variant | A GVariant of type (su) |   |
| out_checksum | Pointer into string memory of *`variant`* with checksum. | \[out\]\[transfer none\] |
| out_objtype | Return object type. | \[out\] |

------------------------------------------------------------------------

### ostree_object_to_string ()

``` programlisting
char *
ostree_object_to_string (const char *checksum,
                         OstreeObjectType objtype);
```

#### Parameters

|          |                   |     |
|----------|-------------------|-----|
| checksum | An ASCII checksum |     |
| objtype  | Object type       |     |

#### Returns

A string containing both *`checksum`* and a stringifed version of *`objtype`*

------------------------------------------------------------------------

### ostree_object_from_string ()

``` programlisting
void
ostree_object_from_string (const char *str,
                           gchar **out_checksum,
                           OstreeObjectType *out_objtype);
```

Reverse [`ostree_object_to_string()`](reference__ostree-Core-repository-independent-functions.md#ostree-object-to-string "ostree_object_to_string ()").

#### Parameters

|              |                     |                          |
|--------------|---------------------|--------------------------|
| str          | An ASCII checksum   |                          |
| out_checksum | Parsed checksum.    | \[out\]\[transfer full\] |
| out_objtype  | Parsed object type. | \[out\]                  |

------------------------------------------------------------------------

### ostree_content_stream_parse ()

``` programlisting
gboolean
ostree_content_stream_parse (gboolean compressed,
                             GInputStream *input,
                             guint64 input_length,
                             gboolean trusted,
                             GInputStream **out_input,
                             GFileInfo **out_file_info,
                             GVariant **out_xattrs,
                             GCancellable *cancellable,
                             GError **error);
```

The reverse of [`ostree_raw_file_to_content_stream()`](reference__ostree-Core-repository-independent-functions.md#ostree-raw-file-to-content-stream "ostree_raw_file_to_content_stream ()"); this function converts an object content stream back into components.

#### Parameters

|               |                                                  |         |
|---------------|--------------------------------------------------|---------|
| compressed    | Whether or not the stream is zlib-compressed     |         |
| input         | Object content stream                            |         |
| input_length  | Length of stream                                 |         |
| trusted       | If `TRUE`, assume the content has been validated |         |
| out_input     | The raw file content stream.                     | \[out\] |
| out_file_info | Normal metadata.                                 | \[out\] |
| out_xattrs    | Extended attributes.                             | \[out\] |
| cancellable   | Cancellable                                      |         |
| error         | Error                                            |         |

------------------------------------------------------------------------

### ostree_content_file_parse ()

``` programlisting
gboolean
ostree_content_file_parse (gboolean compressed,
                           GFile *content_path,
                           gboolean trusted,
                           GInputStream **out_input,
                           GFileInfo **out_file_info,
                           GVariant **out_xattrs,
                           GCancellable *cancellable,
                           GError **error);
```

A thin wrapper for [`ostree_content_stream_parse()`](reference__ostree-Core-repository-independent-functions.md#ostree-content-stream-parse "ostree_content_stream_parse ()"); this function converts an object content stream back into components.

#### Parameters

|               |                                                  |         |
|---------------|--------------------------------------------------|---------|
| compressed    | Whether or not the stream is zlib-compressed     |         |
| content_path  | Path to file containing content                  |         |
| trusted       | If `TRUE`, assume the content has been validated |         |
| out_input     | The raw file content stream.                     | \[out\] |
| out_file_info | Normal metadata.                                 | \[out\] |
| out_xattrs    | Extended attributes.                             | \[out\] |
| cancellable   | Cancellable                                      |         |
| error         | Error                                            |         |

------------------------------------------------------------------------

### ostree_content_file_parse_at ()

``` programlisting
gboolean
ostree_content_file_parse_at (gboolean compressed,
                              int parent_dfd,
                              const char *path,
                              gboolean trusted,
                              GInputStream **out_input,
                              GFileInfo **out_file_info,
                              GVariant **out_xattrs,
                              GCancellable *cancellable,
                              GError **error);
```

A thin wrapper for [`ostree_content_stream_parse()`](reference__ostree-Core-repository-independent-functions.md#ostree-content-stream-parse "ostree_content_stream_parse ()"); this function converts an object content stream back into components.

#### Parameters

|               |                                                  |         |
|---------------|--------------------------------------------------|---------|
| compressed    | Whether or not the stream is zlib-compressed     |         |
| parent_dfd    | Directory file descriptor                        |         |
| path          | Subpath                                          |         |
| trusted       | If `TRUE`, assume the content has been validated |         |
| out_input     | The raw file content stream.                     | \[out\] |
| out_file_info | Normal metadata.                                 | \[out\] |
| out_xattrs    | Extended attributes.                             | \[out\] |
| cancellable   | Cancellable                                      |         |
| error         | Error                                            |         |

------------------------------------------------------------------------

### ostree_raw_file_to_archive_z2_stream ()

``` programlisting
gboolean
ostree_raw_file_to_archive_z2_stream (GInputStream *input,
                                      GFileInfo *file_info,
                                      GVariant *xattrs,
                                      GInputStream **out_input,
                                      GCancellable *cancellable,
                                      GError **error);
```

Convert from a "bare" file representation into an OSTREE_OBJECT_TYPE_FILE stream suitable for ostree pull.

#### Parameters

|             |                               |                |
|-------------|-------------------------------|----------------|
| input       | File raw content stream       |                |
| file_info   | A file info                   |                |
| xattrs      | Optional extended attributes. | \[allow-none\] |
| out_input   | Serialized object stream.     | \[out\]        |
| cancellable | Cancellable                   |                |
| error       | Error                         |                |

Since: 2016.6

------------------------------------------------------------------------

### ostree_raw_file_to_archive_z2_stream_with_options ()

``` programlisting
gboolean
ostree_raw_file_to_archive_z2_stream_with_options
                               (GInputStream *input,
                                GFileInfo *file_info,
                                GVariant *xattrs,
                                GVariant *options,
                                GInputStream **out_input,
                                GCancellable *cancellable,
                                GError **error);
```

Like [`ostree_raw_file_to_archive_z2_stream()`](reference__ostree-Core-repository-independent-functions.md#ostree-raw-file-to-archive-z2-stream "ostree_raw_file_to_archive_z2_stream ()"), but supports an extensible set of flags. The following flags are currently defined:

- `compression-level` (`i`): Level of compression to use, 0–9, with 0 being the least compression, and \<0 giving the default level (currently 6).

#### Parameters

|  |  |  |
|----|----|----|
| input | File raw content stream |   |
| file_info | A file info |   |
| xattrs | Optional extended attributes. | \[allow-none\] |
| options | A GVariant `a{sv}` with an extensible set of flags. | \[nullable\] |
| out_input | Serialized object stream. | \[out\] |
| cancellable | Cancellable |   |
| error | Error |   |

Since: 2017.3

------------------------------------------------------------------------

### ostree_raw_file_to_content_stream ()

``` programlisting
gboolean
ostree_raw_file_to_content_stream (GInputStream *input,
                                   GFileInfo *file_info,
                                   GVariant *xattrs,
                                   GInputStream **out_input,
                                   guint64 *out_length,
                                   GCancellable *cancellable,
                                   GError **error);
```

Convert from a "bare" file representation into an OSTREE_OBJECT_TYPE_FILE stream. This is a fundamental operation for writing data to an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo").

#### Parameters

|             |                               |                |
|-------------|-------------------------------|----------------|
| input       | File raw content stream       |                |
| file_info   | A file info                   |                |
| xattrs      | Optional extended attributes. | \[allow-none\] |
| out_input   | Serialized object stream.     | \[out\]        |
| out_length  | Length of stream.             | \[out\]        |
| cancellable | Cancellable                   |                |
| error       | Error                         |                |

------------------------------------------------------------------------

### ostree_break_hardlink ()

``` programlisting
gboolean
ostree_break_hardlink (int dfd,
                       const char *path,
                       gboolean skip_xattrs,
                       GCancellable *cancellable,
                       GError **error);
```

In many cases using libostree, a program may need to "break" hardlinks by performing a copy. For example, in order to logically append to a file.

This function performs full copying, including e.g. extended attributes and permissions of both regular files and symbolic links.

If the file is not hardlinked, this function does nothing and returns successfully.

This function does not perform synchronization via `fsync()` or `fdatasync()`; the idea is this will commonly be done as part of an [`ostree_repo_commit_transaction()`](reference__ostree-OstreeRepo.md#ostree-repo-commit-transaction "ostree_repo_commit_transaction ()"), which itself takes care of synchronization.

#### Parameters

|             |                                 |     |
|-------------|---------------------------------|-----|
| dfd         | Directory fd                    |     |
| path        | Path relative to *`dfd`*        |     |
| skip_xattrs | Do not copy extended attributes |     |
| error       | error                           |     |

Since: 2017.15

------------------------------------------------------------------------

### ostree_checksum_file_from_input ()

``` programlisting
gboolean
ostree_checksum_file_from_input (GFileInfo *file_info,
                                 GVariant *xattrs,
                                 GInputStream *in,
                                 OstreeObjectType objtype,
                                 guchar **out_csum,
                                 GCancellable *cancellable,
                                 GError **error);
```

Compute the OSTree checksum for a given input.

#### Parameters

|  |  |  |
|----|----|----|
| file_info | File information |   |
| xattrs | Optional extended attributes. | \[allow-none\] |
| in | File content, should be `NULL` for symbolic links. | \[allow-none\] |
| objtype | Object type |   |
| out_csum | Return location for binary checksum. | \[out\]\[array fixed-size=32\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_checksum_file ()

``` programlisting
gboolean
ostree_checksum_file (GFile *f,
                      OstreeObjectType objtype,
                      guchar **out_csum,
                      GCancellable *cancellable,
                      GError **error);
```

Compute the OSTree checksum for a given file.

#### Parameters

|  |  |  |
|----|----|----|
| f | File path |   |
| objtype | Object type |   |
| out_csum | Return location for binary checksum. | \[out\]\[array fixed-size=32\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_checksum_file_at ()

``` programlisting
gboolean
ostree_checksum_file_at (int dfd,
                         const char *path,
                         struct stat *stbuf,
                         OstreeObjectType objtype,
                         OstreeChecksumFlags flags,
                         char **out_checksum,
                         GCancellable *cancellable,
                         GError **error);
```

Compute the OSTree checksum for a given file. This is an fd-relative version of [`ostree_checksum_file()`](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file "ostree_checksum_file ()") which also takes flags and fills in a caller allocated buffer.

#### Parameters

|                                    |                                  |     |
|------------------------------------|----------------------------------|-----|
| dfd                                | Directory file descriptor        |     |
| path                               | Subpath                          |     |
| stbuf (allow-none)                 | Optional stat buffer             |     |
| objtype                            | Object type                      |     |
| flags                              | Flags                            |     |
| out_checksum (out) (transfer full) | Return location for hex checksum |     |
| cancellable                        | Cancellable                      |     |
| error                              | Error                            |     |

Since: 2017.13

------------------------------------------------------------------------

### ostree_checksum_file_async ()

``` programlisting
void
ostree_checksum_file_async (GFile *f,
                            OstreeObjectType objtype,
                            int io_priority,
                            GCancellable *cancellable,
                            GAsyncReadyCallback callback,
                            gpointer user_data);
```

Asynchronously compute the OSTree checksum for a given file; complete with [`ostree_checksum_file_async_finish()`](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file-async-finish "ostree_checksum_file_async_finish ()").

#### Parameters

|             |                                                     |     |
|-------------|-----------------------------------------------------|-----|
| f           | File path                                           |     |
| objtype     | Object type                                         |     |
| io_priority | Priority for operation, see `G_IO_PRIORITY_DEFAULT` |     |
| cancellable | Cancellable                                         |     |
| callback    | Invoked when operation is complete                  |     |
| user_data   | Data for *`callback`*                               |     |

------------------------------------------------------------------------

### ostree_checksum_file_async_finish ()

``` programlisting
gboolean
ostree_checksum_file_async_finish (GFile *f,
                                   GAsyncResult *result,
                                   guchar **out_csum,
                                   GError **error);
```

Finish computing the OSTree checksum for a given file; see [`ostree_checksum_file_async()`](reference__ostree-Core-repository-independent-functions.md#ostree-checksum-file-async "ostree_checksum_file_async ()").

#### Parameters

|  |  |  |
|----|----|----|
| f | File path |   |
| result | Async result |   |
| out_csum | Return location for binary checksum. | \[out\]\[array fixed-size=32\] |
| error | Error |   |

------------------------------------------------------------------------

### ostree_fs_get_all_xattrs ()

``` programlisting
GVariant *
ostree_fs_get_all_xattrs (int fd,
                          GCancellable *cancellable,
                          GError **error);
```

Retrieve all extended attributes in a canonical (sorted) order from the given file descriptor.

#### Parameters

|             |                 |     |
|-------------|-----------------|-----|
| fd          | File descriptor |     |
| cancellable | Cancellable     |     |
| error       | Error           |     |

#### Returns

A GVariant of type `a(ayay)`.

\[transfer full\]

------------------------------------------------------------------------

### ostree_fs_get_all_xattrs_at ()

``` programlisting
GVariant *
ostree_fs_get_all_xattrs_at (int dfd,
                             const char *path,
                             GCancellable *cancellable,
                             GError **error);
```

Retrieve all extended attributes in a canonical (sorted) order from the given path, relative to the provided directory file descriptor. The target path will not be dereferenced. Currently on Linux, this API must be used currently to retrieve extended attributes for symbolic links because while `O_PATH` exists, it cannot be used with `fgetxattr()`.

#### Parameters

|             |                           |     |
|-------------|---------------------------|-----|
| dfd         | Directory file descriptor |     |
| path        | Filesystem path           |     |
| cancellable | Cancellable               |     |
| error       | Error                     |     |

#### Returns

A GVariant of type `a(ayay)`.

\[transfer full\]

------------------------------------------------------------------------

### ostree_create_directory_metadata ()

``` programlisting
GVariant *
ostree_create_directory_metadata (GFileInfo *dir_info,
                                  GVariant *xattrs);
```

#### Parameters

|          |                                              |                |
|----------|----------------------------------------------|----------------|
| dir_info | a GFileInfo containing directory information |                |
| xattrs   | Optional extended attributes.                | \[allow-none\] |

#### Returns

A new GVariant containing [`OSTREE_OBJECT_TYPE_DIR_META`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-DIR-META:CAPS).

\[transfer full\]\[not nullable\]

------------------------------------------------------------------------

### ostree_validate_structureof_objtype ()

``` programlisting
gboolean
ostree_validate_structureof_objtype (guchar objtype,
                                     GError **error);
```

#### Parameters

|       |       |     |
|-------|-------|-----|
| error | Error |     |

#### Returns

`TRUE` if *`objtype`* represents a valid object type

------------------------------------------------------------------------

### ostree_validate_structureof_csum_v ()

``` programlisting
gboolean
ostree_validate_structureof_csum_v (GVariant *checksum,
                                    GError **error);
```

#### Parameters

|          |                         |     |
|----------|-------------------------|-----|
| checksum | a GVariant of type "ay" |     |
| error    | Error                   |     |

#### Returns

`TRUE` if *`checksum`* is a valid binary SHA256 checksum

------------------------------------------------------------------------

### ostree_validate_structureof_checksum_string ()

``` programlisting
gboolean
ostree_validate_structureof_checksum_string
                               (const char *checksum,
                                GError **error);
```

#### Parameters

|          |                 |     |
|----------|-----------------|-----|
| checksum | an ASCII string |     |
| error    | Error           |     |

#### Returns

`TRUE` if *`checksum`* is a valid ASCII SHA256 checksum

------------------------------------------------------------------------

### ostree_validate_structureof_file_mode ()

``` programlisting
gboolean
ostree_validate_structureof_file_mode (guint32 mode,
                                       GError **error);
```

#### Parameters

|       |                        |     |
|-------|------------------------|-----|
| mode  | A Unix filesystem mode |     |
| error | Error                  |     |

#### Returns

`TRUE` if *`mode`* represents a valid file type and permissions

------------------------------------------------------------------------

### ostree_validate_structureof_commit ()

``` programlisting
gboolean
ostree_validate_structureof_commit (GVariant *commit,
                                    GError **error);
```

Use this to validate the basic structure of *`commit`* , independent of any other objects it references.

#### Parameters

|  |  |  |
|----|----|----|
| commit | A commit object, [`OSTREE_OBJECT_TYPE_COMMIT`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-COMMIT:CAPS) |   |
| error | Error |   |

#### Returns

`TRUE` if *`commit`* is structurally valid

------------------------------------------------------------------------

### ostree_validate_structureof_dirtree ()

``` programlisting
gboolean
ostree_validate_structureof_dirtree (GVariant *dirtree,
                                     GError **error);
```

Use this to validate the basic structure of *`dirtree`* , independent of any other objects it references.

#### Parameters

|  |  |  |
|----|----|----|
| dirtree | A dirtree object, [`OSTREE_OBJECT_TYPE_DIR_TREE`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-DIR-TREE:CAPS) |   |
| error | Error |   |

#### Returns

`TRUE` if *`dirtree`* is structurally valid

------------------------------------------------------------------------

### ostree_validate_structureof_dirmeta ()

``` programlisting
gboolean
ostree_validate_structureof_dirmeta (GVariant *dirmeta,
                                     GError **error);
```

Use this to validate the basic structure of *`dirmeta`* .

#### Parameters

|  |  |  |
|----|----|----|
| dirmeta | A dirmeta object, [`OSTREE_OBJECT_TYPE_DIR_META`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-DIR-META:CAPS) |   |
| error | Error |   |

#### Returns

`TRUE` if *`dirmeta`* is structurally valid

------------------------------------------------------------------------

### ostree_commit_get_parent ()

``` programlisting
gchar *
ostree_commit_get_parent (GVariant *commit_variant);
```

#### Parameters

|  |  |  |
|----|----|----|
| commit_variant | Variant of type [`OSTREE_OBJECT_TYPE_COMMIT`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-COMMIT:CAPS) |   |

#### Returns

Checksum of the parent commit of *`commit_variant`* , or `NULL` if none.

\[nullable\]

------------------------------------------------------------------------

### ostree_commit_get_timestamp ()

``` programlisting
guint64
ostree_commit_get_timestamp (GVariant *commit_variant);
```

#### Parameters

|                |               |     |
|----------------|---------------|-----|
| commit_variant | Commit object |     |

#### Returns

timestamp in seconds since the Unix epoch, UTC

Since: 2016.3

------------------------------------------------------------------------

### ostree_commit_metadata_for_bootable ()

``` programlisting
gboolean
ostree_commit_metadata_for_bootable (GFile *root,
                                     GVariantDict *dict,
                                     GCancellable *cancellable,
                                     GError **error);
```

Update provided *`dict`* with standard metadata for bootable OSTree commits.

#### Parameters

|      |                                 |     |
|------|---------------------------------|-----|
| root | Root filesystem to be committed |     |
| dict | Dictionary to update            |     |

Since: 2021.1

------------------------------------------------------------------------

### ostree_commit_get_content_checksum ()

``` programlisting
gchar *
ostree_commit_get_content_checksum (GVariant *commit_variant);
```

There are use cases where one wants a checksum just of the content of a commit. OSTree commits by default capture the current timestamp, and may have additional metadata, which means that re-committing identical content often results in a new checksum.

By comparing checksums of content, it's possible to easily distinguish cases where nothing actually changed.

The content checksums is simply defined as `SHA256(root dirtree_checksum || root_dirmeta_checksum)`, i.e. the SHA-256 of the root "dirtree" object's checksum concatenated with the root "dirmeta" checksum (both in binary form, not hexadecimal).

#### Parameters

|                |                 |     |
|----------------|-----------------|-----|
| commit_variant | A commit object |     |

#### Returns

A SHA-256 hex string, or `NULL` if *`commit_variant`* is not well-formed.

\[nullable\]

Since: 2018.2

------------------------------------------------------------------------

### ostree_commit_get_object_sizes ()

``` programlisting
gboolean
ostree_commit_get_object_sizes (GVariant *commit_variant,
                                GPtrArray **out_sizes_entries,
                                GError **error);
```

Reads a commit's "ostree.sizes" metadata and returns an array of OstreeCommitSizesEntry in *`out_sizes_entries`* . Each element represents an object in the commit. If the commit does not contain the "ostree.sizes" metadata, a `G_IO_ERROR_NOT_FOUND` error will be returned.

#### Parameters

|  |  |  |
|----|----|----|
| commit_variant | variant of type [`OSTREE_OBJECT_TYPE_COMMIT`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-COMMIT:CAPS). | \[not nullable\] |
| out_sizes_entries | return location for an array of object size entries. | \[out\]\[element-type OstreeCommitSizesEntry\]\[transfer container\]\[optional\] |
| error | Error |   |

Since: 2020.1

------------------------------------------------------------------------

### ostree_commit_sizes_entry_new ()

``` programlisting
OstreeCommitSizesEntry *
ostree_commit_sizes_entry_new (const gchar *checksum,
                               OstreeObjectType objtype,
                               guint64 unpacked,
                               guint64 archived);
```

Create a new OstreeCommitSizesEntry for representing an object in a commit's "ostree.sizes" metadata.

#### Parameters

|          |                        |                  |
|----------|------------------------|------------------|
| checksum | object checksum.       | \[not nullable\] |
| objtype  | object type            |                  |
| unpacked | unpacked object size   |                  |
| archived | compressed object size |                  |

#### Returns

a new OstreeCommitSizesEntry.

\[transfer full\]\[nullable\]

Since: 2020.1

------------------------------------------------------------------------

### ostree_commit_sizes_entry_copy ()

``` programlisting
OstreeCommitSizesEntry *
ostree_commit_sizes_entry_copy (const OstreeCommitSizesEntry *entry);
```

Create a copy of the given *`entry`* .

#### Parameters

|       |                            |                  |
|-------|----------------------------|------------------|
| entry | an OstreeCommitSizesEntry. | \[not nullable\] |

#### Returns

a new copy of *`entry`* .

\[transfer full\]\[nullable\]

Since: 2020.1

------------------------------------------------------------------------

### ostree_commit_sizes_entry_free ()

``` programlisting
void
ostree_commit_sizes_entry_free (OstreeCommitSizesEntry *entry);
```

Free given *`entry`* .

#### Parameters

|       |                            |                   |
|-------|----------------------------|-------------------|
| entry | an OstreeCommitSizesEntry. | \[transfer full\] |

Since: 2020.1

------------------------------------------------------------------------

### ostree_check_version ()

``` programlisting
gboolean
ostree_check_version (guint required_year,
                      guint required_release);
```

#### Parameters

|                  |                          |     |
|------------------|--------------------------|-----|
| required_year    | Major/year required      |     |
| required_release | Release version required |     |

#### Returns

`TRUE` if current libostree has at least the requested version, `FALSE` otherwise

Since: 2017.4

## Types and Values

### OSTREE_MAX_METADATA_SIZE

``` programlisting
#define OSTREE_MAX_METADATA_SIZE (128 * 1024 * 1024)
```

Default limit for maximum permitted size in bytes of metadata objects fetched over HTTP (including repo/config files, refs, and commit/dirtree/dirmeta objects). This is an arbitrary number intended to mitigate disk space exhaustion attacks.

------------------------------------------------------------------------

### OSTREE_MAX_METADATA_WARN_SIZE

``` programlisting
#define OSTREE_MAX_METADATA_WARN_SIZE (7 * 1024 * 1024)
```

This variable is no longer meaningful, it is kept only for compatibility.

------------------------------------------------------------------------

### enum OstreeObjectType

Enumeration for core object types; [`OSTREE_OBJECT_TYPE_FILE`](reference__ostree-Core-repository-independent-functions.md#OSTREE-OBJECT-TYPE-FILE:CAPS) is for content, the other types are metadata.

#### Members

|  |  |  |
|----|----|----|
| OSTREE_OBJECT_TYPE_FILE | Content; regular file, symbolic link |   |
| OSTREE_OBJECT_TYPE_DIR_TREE | List of children (trees or files), and metadata |   |
| OSTREE_OBJECT_TYPE_DIR_META | Directory metadata |   |
| OSTREE_OBJECT_TYPE_COMMIT | Toplevel object, refers to tree and dirmeta for root |   |
| OSTREE_OBJECT_TYPE_TOMBSTONE_COMMIT | Toplevel object, refers to a deleted commit |   |
| OSTREE_OBJECT_TYPE_COMMIT_META | Detached metadata for a commit |   |
| OSTREE_OBJECT_TYPE_PAYLOAD_LINK | Symlink to a .file given its checksum on the payload only. |   |
| OSTREE_OBJECT_TYPE_FILE_XATTRS | Detached xattrs content, for 'bare-split-xattrs' mode. |   |
| OSTREE_OBJECT_TYPE_FILE_XATTRS_LINK | Hardlink to a .file-xattrs given the checksum of its .file object. |   |

------------------------------------------------------------------------

### OSTREE_OBJECT_TYPE_LAST

``` programlisting
#define OSTREE_OBJECT_TYPE_LAST OSTREE_OBJECT_TYPE_FILE_XATTRS_LINK
```

Last valid object type; use this to validate ranges.

------------------------------------------------------------------------

### OSTREE_DIRMETA_GVARIANT_STRING

``` programlisting
#define OSTREE_DIRMETA_GVARIANT_STRING "(uuua(ayay))"
```

------------------------------------------------------------------------

### OSTREE_DIRMETA_GVARIANT_FORMAT

``` programlisting
#define OSTREE_DIRMETA_GVARIANT_FORMAT G_VARIANT_TYPE (OSTREE_DIRMETA_GVARIANT_STRING)
```

- u - uid (big-endian)

- u - gid (big-endian)

- u - mode (big-endian)

- a(ayay) - xattrs

------------------------------------------------------------------------

### OSTREE_FILEMETA_GVARIANT_STRING

``` programlisting
#define OSTREE_FILEMETA_GVARIANT_STRING "(uuua(ayay))"
```

------------------------------------------------------------------------

### OSTREE_FILEMETA_GVARIANT_FORMAT

``` programlisting
#define OSTREE_FILEMETA_GVARIANT_FORMAT G_VARIANT_TYPE (OSTREE_FILEMETA_GVARIANT_STRING)
```

This is not a regular object type, but used as an xattr on a .file object in bare-user repositories. This allows us to store metadata information that we can't store in the real filesystem but we can still use a regular .file object that we can hardlink to in the case of a user-mode checkout.

- u - uid (big-endian)

- u - gid (big-endian)

- u - mode (big-endian)

- a(ayay) - xattrs

------------------------------------------------------------------------

### OSTREE_TREE_GVARIANT_STRING

``` programlisting
#define OSTREE_TREE_GVARIANT_STRING "(a(say)a(sayay))"
```

------------------------------------------------------------------------

### OSTREE_TREE_GVARIANT_FORMAT

``` programlisting
#define OSTREE_TREE_GVARIANT_FORMAT G_VARIANT_TYPE (OSTREE_TREE_GVARIANT_STRING)
```

- a(say) - array of (filename, checksum) for files

- a(sayay) - array of (dirname, tree_checksum, meta_checksum) for directories

------------------------------------------------------------------------

### OSTREE_COMMIT_GVARIANT_STRING

``` programlisting
#define OSTREE_COMMIT_GVARIANT_STRING "(a{sv}aya(say)sstayay)"
```

------------------------------------------------------------------------

### OSTREE_COMMIT_GVARIANT_FORMAT

``` programlisting
#define OSTREE_COMMIT_GVARIANT_FORMAT G_VARIANT_TYPE (OSTREE_COMMIT_GVARIANT_STRING)
```

- a{sv} - Metadata

- ay - parent checksum (empty string for initial)

- a(say) - Related objects

- s - subject

- s - body

- t - Timestamp in seconds since the epoch (UTC, big-endian)

- ay - Root tree contents

- ay - Root tree metadata

------------------------------------------------------------------------

### OSTREE_SUMMARY_GVARIANT_STRING

``` programlisting
#define OSTREE_SUMMARY_GVARIANT_STRING "(a(s(taya{sv}))a{sv})"
```

------------------------------------------------------------------------

### OSTREE_SUMMARY_GVARIANT_FORMAT

``` programlisting
#define OSTREE_SUMMARY_GVARIANT_FORMAT G_VARIANT_TYPE (OSTREE_SUMMARY_GVARIANT_STRING)
```

- a(s(taya{sv})) - Map of ref name -\> (latest commit size, latest commit checksum, additional metadata), sorted by ref name

- a{sv} - Additional metadata, at the current time the following are defined:

  - key: "ostree.static-deltas", value: a{sv}, static delta name -\> 32 bytes of checksum

  - key: "ostree.summary.last-modified", value: t, timestamp (seconds since the Unix epoch in UTC, big-endian) when the summary was last regenerated (similar to the HTTP `Last-Modified` header)

  - key: "ostree.summary.expires", value: t, timestamp (seconds since the Unix epoch in UTC, big-endian) after which the summary is considered stale and should be re-downloaded if possible (similar to the HTTP `Expires` header)

The currently defined keys for the `a{sv}` of additional metadata for each commit are:

- key: `ostree.commit.timestamp`, value: `t`, timestamp (seconds since the Unix epoch in UTC, big-endian) when the commit was committed

- key: `ostree.commit.version`, value: `s`, the `version` value from the commit's metadata if it was defined. Since: 2022.2

------------------------------------------------------------------------
