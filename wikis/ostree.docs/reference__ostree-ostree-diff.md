[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeDiffItem](reference__ostree-ostree-diff.md#OstreeDiffItem "struct OstreeDiffItem") \* | [ostree_diff_item_ref](reference__ostree-ostree-diff.md#ostree-diff-item-ref "ostree_diff_item_ref ()") () |
| void | [ostree_diff_item_unref](reference__ostree-ostree-diff.md#ostree-diff-item-unref "ostree_diff_item_unref ()") () |
| gboolean | [ostree_diff_dirs](reference__ostree-ostree-diff.md#ostree-diff-dirs "ostree_diff_dirs ()") () |
| gboolean | [ostree_diff_dirs_with_options](reference__ostree-ostree-diff.md#ostree-diff-dirs-with-options "ostree_diff_dirs_with_options ()") () |
| void | [ostree_diff_print](reference__ostree-ostree-diff.md#ostree-diff-print "ostree_diff_print ()") () |

## Types and Values

|  |  |
|----|----|
| enum | [OstreeDiffFlags](reference__ostree-ostree-diff.md#OstreeDiffFlags "enum OstreeDiffFlags") |
| struct | [OstreeDiffItem](reference__ostree-ostree-diff.md#OstreeDiffItem "struct OstreeDiffItem") |

## Description

## Functions

### ostree_diff_item_ref ()

``` programlisting
OstreeDiffItem *
ostree_diff_item_ref (OstreeDiffItem *diffitem);
```

------------------------------------------------------------------------

### ostree_diff_item_unref ()

``` programlisting
void
ostree_diff_item_unref (OstreeDiffItem *diffitem);
```

------------------------------------------------------------------------

### ostree_diff_dirs ()

``` programlisting
gboolean
ostree_diff_dirs (OstreeDiffFlags flags,
                  GFile *a,
                  GFile *b,
                  GPtrArray *modified,
                  GPtrArray *removed,
                  GPtrArray *added,
                  GCancellable *cancellable,
                  GError **error);
```

Compute the difference between directory *`a`* and *`b`* as 3 separate sets of [OstreeDiffItem](reference__ostree-ostree-diff.md#OstreeDiffItem "struct OstreeDiffItem") in *`modified`* , *`removed`* , and *`added`* .

#### Parameters

|  |  |  |
|----|----|----|
| flags | Flags |   |
| a | First directory path, or `NULL` |   |
| b | First directory path |   |
| modified | Modified files. | \[element-type OstreeDiffItem\] |
| removed | Removed files. | \[element-type Gio.File\] |
| added | Added files. | \[element-type Gio.File\] |
| cancellable | Cancellable |   |
| error | Error |   |

------------------------------------------------------------------------

### ostree_diff_dirs_with_options ()

``` programlisting
gboolean
ostree_diff_dirs_with_options (OstreeDiffFlags flags,
                               GFile *a,
                               GFile *b,
                               GPtrArray *modified,
                               GPtrArray *removed,
                               GPtrArray *added,
                               OstreeDiffDirsOptions *options,
                               GCancellable *cancellable,
                               GError **error);
```

Compute the difference between directory *`a`* and *`b`* as 3 separate sets of [OstreeDiffItem](reference__ostree-ostree-diff.md#OstreeDiffItem "struct OstreeDiffItem") in *`modified`* , *`removed`* , and *`added`* .

#### Parameters

|  |  |  |
|----|----|----|
| flags | Flags |   |
| a | First directory path, or `NULL` |   |
| b | First directory path |   |
| modified | Modified files. | \[element-type OstreeDiffItem\] |
| removed | Removed files. | \[element-type Gio.File\] |
| added | Added files. | \[element-type Gio.File\] |
| cancellable | Cancellable |   |
| options | Options. | \[allow-none\] |
| error | Error |   |

Since: 2017.4

------------------------------------------------------------------------

### ostree_diff_print ()

``` programlisting
void
ostree_diff_print (GFile *a,
                   GFile *b,
                   GPtrArray *modified,
                   GPtrArray *removed,
                   GPtrArray *added);
```

Print the contents of a diff to stdout.

#### Parameters

|          |                      |                                 |
|----------|----------------------|---------------------------------|
| a        | First directory path |                                 |
| b        | First directory path |                                 |
| modified | Modified files.      | \[element-type OstreeDiffItem\] |
| removed  | Removed files.       | \[element-type Gio.File\]       |
| added    | Added files.         | \[element-type Gio.File\]       |

## Types and Values

### enum OstreeDiffFlags

#### Members

|                                 |     |     |
|---------------------------------|-----|-----|
| OSTREE_DIFF_FLAGS_NONE          |     |     |
| OSTREE_DIFF_FLAGS_IGNORE_XATTRS |     |     |

------------------------------------------------------------------------

### struct OstreeDiffItem

``` programlisting
struct OstreeDiffItem {
  gint refcount; /* atomic */

  GFile *src;
  GFile *target;

  GFileInfo *src_info;
  GFileInfo *target_info;

  char *src_checksum;
  char *target_checksum;
};
```

------------------------------------------------------------------------
