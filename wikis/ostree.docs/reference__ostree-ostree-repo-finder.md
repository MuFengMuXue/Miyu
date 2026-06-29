[TABLE]

## Functions

|  |  |
|----|----|
| void | [ostree_repo_finder_resolve_async](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-async "ostree_repo_finder_resolve_async ()") () |
| GPtrArray \* | [ostree_repo_finder_resolve_finish](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-finish "ostree_repo_finder_resolve_finish ()") () |
| void | [ostree_repo_finder_resolve_all_async](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-all-async "ostree_repo_finder_resolve_all_async ()") () |
| GPtrArray \* | [ostree_repo_finder_resolve_all_finish](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-all-finish "ostree_repo_finder_resolve_all_finish ()") () |
| OstreeRepoFinderResult \* | [ostree_repo_finder_result_new](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-result-new "ostree_repo_finder_result_new ()") () |
| OstreeRepoFinderResult \* | [ostree_repo_finder_result_dup](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-result-dup "ostree_repo_finder_result_dup ()") () |
| void | [ostree_repo_finder_result_free](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-result-free "ostree_repo_finder_result_free ()") () |
| gint | [ostree_repo_finder_result_compare](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-result-compare "ostree_repo_finder_result_compare ()") () |
| void | [ostree_repo_finder_result_freev](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-result-freev "ostree_repo_finder_result_freev ()") () |

## Types and Values

|  |  |
|----|----|
|   | [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") |
| typedef | [OstreeRepoFinderResultv](reference__ostree-ostree-repo-finder.md#OstreeRepoFinderResultv "OstreeRepoFinderResultv") |

## Description

## Functions

### ostree_repo_finder_resolve_async ()

``` programlisting
void
ostree_repo_finder_resolve_async (OstreeRepoFinder *self,
                                  const OstreeCollectionRef *const *refs,
                                  OstreeRepo *parent_repo,
                                  GCancellable *cancellable,
                                  GAsyncReadyCallback callback,
                                  gpointer user_data);
```

Find reachable remote URIs which claim to provide any of the given *`refs`* . The specific method for finding the remotes depends on the [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") implementation.

Any remote which is found and which claims to support any of the given *`refs`* will be returned in the results. It is possible that a remote claims to support a given ref, but turns out not to — it is not possible to verify this until [`ostree_repo_pull_from_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-async "ostree_repo_pull_from_remotes_async ()") is called.

The returned results will be sorted with the most useful first — this is typically the remote which claims to provide the most *`refs`* , at the lowest latency.

Each result contains a mapping of *`refs`* to the checksums of the commits which the result provides. If the result provides the latest commit for a ref across all of the results, the checksum will be set. Otherwise, if the result provides an outdated commit, or doesn’t provide a given ref at all, the checksum will not be set. Results which provide none of the requested *`refs`* may be listed with an empty refs map.

Pass the results to [`ostree_repo_pull_from_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-async "ostree_repo_pull_from_remotes_async ()") to pull the given *`refs`* from those remotes.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") |   |
| refs | non-empty array of collection–ref pairs to find remotes for. | \[array zero-terminated=1\] |
| parent_repo | the local repository which the refs are being resolved for, which provides configuration information and GPG keys. | \[transfer none\] |
| cancellable | a GCancellable, or `NULL`. | \[nullable\] |
| callback | asynchronous completion callback |   |
| user_data | data to pass to *`callback`* |   |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_resolve_finish ()

``` programlisting
GPtrArray *
ostree_repo_finder_resolve_finish (OstreeRepoFinder *self,
                                   GAsyncResult *result,
                                   GError **error);
```

Get the results from a [`ostree_repo_finder_resolve_async()`](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-async "ostree_repo_finder_resolve_async ()") operation.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") |   |
| result | GAsyncResult from the callback |   |
| error | return location for a GError |   |

#### Returns

array of zero or more results.

\[transfer full\]\[element-type OstreeRepoFinderResult\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_resolve_all_async ()

``` programlisting
void
ostree_repo_finder_resolve_all_async (OstreeRepoFinder *const *finders,
                                      const OstreeCollectionRef *const *refs,
                                      OstreeRepo *parent_repo,
                                      GCancellable *cancellable,
                                      GAsyncReadyCallback callback,
                                      gpointer user_data);
```

A version of [`ostree_repo_finder_resolve_async()`](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-async "ostree_repo_finder_resolve_async ()") which queries one or more *`finders`* in parallel and combines the results.

#### Parameters

|  |  |  |
|----|----|----|
| finders | non-empty array of [OstreeRepoFinders](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder). | \[array zero-terminated=1\] |
| refs | non-empty array of collection–ref pairs to find remotes for. | \[array zero-terminated=1\] |
| parent_repo | the local repository which the refs are being resolved for, which provides configuration information and GPG keys. | \[transfer none\] |
| cancellable | a GCancellable, or `NULL`. | \[nullable\] |
| callback | asynchronous completion callback |   |
| user_data | data to pass to *`callback`* |   |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_resolve_all_finish ()

``` programlisting
GPtrArray *
ostree_repo_finder_resolve_all_finish (GAsyncResult *result,
                                       GError **error);
```

Get the results from a [`ostree_repo_finder_resolve_all_async()`](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-all-async "ostree_repo_finder_resolve_all_async ()") operation.

#### Parameters

|        |                                |     |
|--------|--------------------------------|-----|
| result | GAsyncResult from the callback |     |
| error  | return location for a GError   |     |

#### Returns

array of zero or more results.

\[transfer full\]\[element-type OstreeRepoFinderResult\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_result_new ()

``` programlisting
OstreeRepoFinderResult *
ostree_repo_finder_result_new (OstreeRemote *remote,
                               OstreeRepoFinder *finder,
                               gint priority,
                               GHashTable *ref_to_checksum,
                               GHashTable *ref_to_timestamp,
                               guint64 summary_last_modified);
```

Create a new OstreeRepoFinderResult instance. The semantics for the arguments are as described in the OstreeRepoFinderResult documentation.

#### Parameters

|  |  |  |
|----|----|----|
| remote | an [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") containing the transport details for the result. | \[transfer none\] |
| finder | the [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") instance which produced the result. | \[transfer none\] |
| priority | static priority of the result, where higher numbers indicate lower priority |   |
| ref_to_checksum | map of collection–ref pairs to checksums provided by this result. | \[element-type OstreeCollectionRef utf8\]\[transfer none\] |
| ref_to_timestamp | (element-type OstreeCollectionRef guint64) (nullable) (transfer none): map of collection–ref pairs to timestamps provided by this result |   |
| summary_last_modified | Unix timestamp (seconds since the epoch, UTC) when the summary file for the result was last modified, or `0` if this is unknown |   |

#### Returns

a new OstreeRepoFinderResult.

\[transfer full\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_result_dup ()

``` programlisting
OstreeRepoFinderResult *
ostree_repo_finder_result_dup (OstreeRepoFinderResult *result);
```

Copy an OstreeRepoFinderResult.

#### Parameters

|        |                                    |                   |
|--------|------------------------------------|-------------------|
| result | an OstreeRepoFinderResult to copy. | \[transfer none\] |

#### Returns

a newly allocated copy of *`result`* .

\[transfer full\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_result_free ()

``` programlisting
void
ostree_repo_finder_result_free (OstreeRepoFinderResult *result);
```

Free the given *`result`* .

#### Parameters

|        |                            |                   |
|--------|----------------------------|-------------------|
| result | an OstreeRepoFinderResult. | \[transfer full\] |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_result_compare ()

``` programlisting
gint
ostree_repo_finder_result_compare (const OstreeRepoFinderResult *a,
                                   const OstreeRepoFinderResult *b);
```

Compare two OstreeRepoFinderResult instances to work out which one is better to pull from, and hence needs to be ordered before the other.

#### Parameters

|     |                           |     |
|-----|---------------------------|-----|
| a   | an OstreeRepoFinderResult |     |
| b   | an OstreeRepoFinderResult |     |

#### Returns

\<0 if *`a`* is ordered before *`b`* , 0 if they are ordered equally, \>0 if *`b`* is ordered before *`a`*

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_finder_result_freev ()

``` programlisting
void
ostree_repo_finder_result_freev (OstreeRepoFinderResult **results);
```

Free the given *`results`* array, freeing each element and the container.

#### Parameters

|  |  |  |
|----|----|----|
| results | an OstreeRepoFinderResult. | \[array zero-terminated=1\]\[transfer full\] |

Since: 2018.6

## Types and Values

### OstreeRepoFinder

``` programlisting
typedef struct _OstreeRepoFinder OstreeRepoFinder;
```

------------------------------------------------------------------------

### OstreeRepoFinderResultv

``` programlisting
typedef OstreeRepoFinderResult **OstreeRepoFinderResultv;
```

A `NULL`-terminated array of OstreeRepoFinderResult instances, designed to be used with `g_auto()`:

[TABLE]

Since: 2018.6

------------------------------------------------------------------------
