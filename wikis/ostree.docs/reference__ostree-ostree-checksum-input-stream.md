[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeChecksumInputStream](reference__ostree-ostree-checksum-input-stream.md#OstreeChecksumInputStream "struct OstreeChecksumInputStream") \* | [ostree_checksum_input_stream_new](reference__ostree-ostree-checksum-input-stream.md#ostree-checksum-input-stream-new "ostree_checksum_input_stream_new ()") () |

## Types and Values

|  |  |
|----|----|
| struct | [OstreeChecksumInputStream](reference__ostree-ostree-checksum-input-stream.md#OstreeChecksumInputStream "struct OstreeChecksumInputStream") |

## Description

## Functions

### ostree_checksum_input_stream_new ()

``` programlisting
OstreeChecksumInputStream *
ostree_checksum_input_stream_new (GInputStream *stream,
                                  GChecksum *checksum);
```

## Types and Values

### struct OstreeChecksumInputStream

``` programlisting
struct OstreeChecksumInputStream {
  GFilterInputStream parent_instance;
};
```

------------------------------------------------------------------------
