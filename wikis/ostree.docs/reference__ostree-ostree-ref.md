[TABLE]

## Functions

|  |  |
|----|----|
| OstreeCollectionRef \* | [ostree_collection_ref_new](reference__ostree-ostree-ref.md#ostree-collection-ref-new "ostree_collection_ref_new ()") () |
| OstreeCollectionRef \* | [ostree_collection_ref_dup](reference__ostree-ostree-ref.md#ostree-collection-ref-dup "ostree_collection_ref_dup ()") () |
| void | [ostree_collection_ref_free](reference__ostree-ostree-ref.md#ostree-collection-ref-free "ostree_collection_ref_free ()") () |
| guint | [ostree_collection_ref_hash](reference__ostree-ostree-ref.md#ostree-collection-ref-hash "ostree_collection_ref_hash ()") () |
| gboolean | [ostree_collection_ref_equal](reference__ostree-ostree-ref.md#ostree-collection-ref-equal "ostree_collection_ref_equal ()") () |
| OstreeCollectionRef \*\* | [ostree_collection_ref_dupv](reference__ostree-ostree-ref.md#ostree-collection-ref-dupv "ostree_collection_ref_dupv ()") () |
| void | [ostree_collection_ref_freev](reference__ostree-ostree-ref.md#ostree-collection-ref-freev "ostree_collection_ref_freev ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeCollectionRefv](reference__ostree-ostree-ref.md#OstreeCollectionRefv "OstreeCollectionRefv") |

## Description

## Functions

### ostree_collection_ref_new ()

``` programlisting
OstreeCollectionRef *
ostree_collection_ref_new (const gchar *collection_id,
                           const gchar *ref_name);
```

Create a new OstreeCollectionRef containing (*`collection_id`* , *`ref_name`* ). If *`collection_id`* is `NULL`, this is equivalent to a plain ref name string (not a refspec; no remote name is included), which can be used for non-P2P operations.

#### Parameters

|               |                                             |              |
|---------------|---------------------------------------------|--------------|
| collection_id | a collection ID, or `NULL` for a plain ref. | \[nullable\] |
| ref_name      | a ref name                                  |              |

#### Returns

a new OstreeCollectionRef.

\[transfer full\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_collection_ref_dup ()

``` programlisting
OstreeCollectionRef *
ostree_collection_ref_dup (const OstreeCollectionRef *ref);
```

Create a copy of the given *`ref`* .

#### Parameters

|     |                         |                  |
|-----|-------------------------|------------------|
| ref | an OstreeCollectionRef. | \[not nullable\] |

#### Returns

a newly allocated copy of *`ref`* .

\[transfer full\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_collection_ref_free ()

``` programlisting
void
ostree_collection_ref_free (OstreeCollectionRef *ref);
```

Free the given *`ref`* .

#### Parameters

|     |                         |                   |
|-----|-------------------------|-------------------|
| ref | an OstreeCollectionRef. | \[transfer full\] |

Since: 2018.6

------------------------------------------------------------------------

### ostree_collection_ref_hash ()

``` programlisting
guint
ostree_collection_ref_hash (gconstpointer ref);
```

Hash the given *`ref`* . This function is suitable for use with GHashTable. *`ref`* must be non-`NULL`.

#### Parameters

|     |                         |                                              |
|-----|-------------------------|----------------------------------------------|
| ref | an OstreeCollectionRef. | \[not nullable\]\[type OstreeCollectionRef\] |

#### Returns

hash value for *`ref`*

Since: 2018.6

------------------------------------------------------------------------

### ostree_collection_ref_equal ()

``` programlisting
gboolean
ostree_collection_ref_equal (gconstpointer ref1,
                             gconstpointer ref2);
```

Compare *`ref1`* and *`ref2`* and return `TRUE` if they have the same collection ID and ref name, and `FALSE` otherwise. Both *`ref1`* and *`ref2`* must be non-`NULL`.

#### Parameters

|  |  |  |
|----|----|----|
| ref1 | an OstreeCollectionRef. | \[not nullable\]\[type OstreeCollectionRef\] |
| ref2 | another OstreeCollectionRef. | \[not nullable\]\[type OstreeCollectionRef\] |

#### Returns

`TRUE` if *`ref1`* and *`ref2`* are equal, `FALSE` otherwise

Since: 2018.6

------------------------------------------------------------------------

### ostree_collection_ref_dupv ()

``` programlisting
OstreeCollectionRef **
ostree_collection_ref_dupv (const OstreeCollectionRef *const *refs);
```

Copy an array of OstreeCollectionRefs, including deep copies of all its elements. *`refs`* must be `NULL`-terminated; it may be empty, but must not be `NULL`.

#### Parameters

|  |  |  |
|----|----|----|
| refs | `NULL`-terminated array of OstreeCollectionRefs. | \[array zero-terminated=1\] |

#### Returns

a newly allocated copy of *`refs`* .

\[transfer full\]\[array zero-terminated=1\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_collection_ref_freev ()

``` programlisting
void
ostree_collection_ref_freev (OstreeCollectionRef **refs);
```

Free the given array of *`refs`* , including freeing all its elements. *`refs`* must be `NULL`-terminated; it may be empty, but must not be `NULL`.

#### Parameters

|  |  |  |
|----|----|----|
| refs | an array of OstreeCollectionRefs. | \[transfer full\]\[array zero-terminated=1\] |

Since: 2018.6

## Types and Values

### OstreeCollectionRefv

``` programlisting
typedef OstreeCollectionRef **OstreeCollectionRefv;
```

A `NULL`-terminated array of OstreeCollectionRef instances, designed to be used with `g_auto()`:

[TABLE]

Since: 2018.6

------------------------------------------------------------------------
