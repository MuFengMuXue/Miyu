[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeChainInputStream](reference__ostree-ostree-chain-input-stream.md#OstreeChainInputStream "struct OstreeChainInputStream") \* | [ostree_chain_input_stream_new](reference__ostree-ostree-chain-input-stream.md#ostree-chain-input-stream-new "ostree_chain_input_stream_new ()") () |

## Types and Values

|  |  |
|----|----|
| struct | [OstreeChainInputStream](reference__ostree-ostree-chain-input-stream.md#OstreeChainInputStream "struct OstreeChainInputStream") |

## Description

## Functions

### ostree_chain_input_stream_new ()

``` programlisting
OstreeChainInputStream *
ostree_chain_input_stream_new (GPtrArray *streams);
```

## Types and Values

### struct OstreeChainInputStream

``` programlisting
struct OstreeChainInputStream {
  GInputStream parent_instance;
};
```

------------------------------------------------------------------------
