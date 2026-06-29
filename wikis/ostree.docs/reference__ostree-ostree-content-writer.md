[TABLE]

## Functions

|  |  |
|----|----|
| char \* | [ostree_content_writer_finish](reference__ostree-ostree-content-writer.md#ostree-content-writer-finish "ostree_content_writer_finish ()") () |

## Description

## Functions

### ostree_content_writer_finish ()

``` programlisting
char *
ostree_content_writer_finish (OstreeContentWriter *self,
                              GCancellable *cancellable,
                              GError **error);
```

Complete the object write and return the checksum.

#### Parameters

|             |             |     |
|-------------|-------------|-----|
| self        | Writer      |     |
| cancellable | Cancellable |     |
| error       | Error       |     |

#### Returns

Checksum, or `NULL` on error.

\[transfer full\]

------------------------------------------------------------------------
