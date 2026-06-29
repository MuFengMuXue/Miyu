[TABLE]

## Functions

|  |  |
|----|----|
| void | [ostree_repo_find_remotes_async](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-find-remotes-async "ostree_repo_find_remotes_async ()") () |
| OstreeRepoFinderResult \*\* | [ostree_repo_find_remotes_finish](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-find-remotes-finish "ostree_repo_find_remotes_finish ()") () |
| void | [ostree_repo_pull_from_remotes_async](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-async "ostree_repo_pull_from_remotes_async ()") () |
| gboolean | [ostree_repo_pull_from_remotes_finish](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-finish "ostree_repo_pull_from_remotes_finish ()") () |
| [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") \* | [ostree_repo_resolve_keyring_for_collection](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-resolve-keyring-for-collection "ostree_repo_resolve_keyring_for_collection ()") () |

## Types and Values

|  |  |
|----|----|
| \#define | [OSTREE_REPO_METADATA_REF](reference__ostree-ostree-repo-remote-finder.md#OSTREE-REPO-METADATA-REF:CAPS "OSTREE_REPO_METADATA_REF") |
| \#define | [OSTREE_META_KEY_DEPLOY_COLLECTION_ID](reference__ostree-ostree-repo-remote-finder.md#OSTREE-META-KEY-DEPLOY-COLLECTION-ID:CAPS "OSTREE_META_KEY_DEPLOY_COLLECTION_ID") |

## Description

## Functions

### ostree_repo_find_remotes_async ()

``` programlisting
void
ostree_repo_find_remotes_async (OstreeRepo *self,
                                const OstreeCollectionRef *const *refs,
                                GVariant *options,
                                OstreeRepoFinder **finders,
                                OstreeAsyncProgress *progress,
                                GCancellable *cancellable,
                                GAsyncReadyCallback callback,
                                gpointer user_data);
```

Find reachable remote URIs which claim to provide any of the given named *`refs`* . This will search for configured remotes (OstreeRepoFinderConfig), mounted volumes (OstreeRepoFinderMount) and (if enabled at compile time) local network peers (OstreeRepoFinderAvahi). In order to use a custom configuration of [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") instances, call [`ostree_repo_finder_resolve_all_async()`](reference__ostree-ostree-repo-finder.md#ostree-repo-finder-resolve-all-async "ostree_repo_finder_resolve_all_async ()") on them individually.

Any remote which is found and which claims to support any of the given *`refs`* will be returned in the results. It is possible that a remote claims to support a given ref, but turns out not to — it is not possible to verify this until [`ostree_repo_pull_from_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-async "ostree_repo_pull_from_remotes_async ()") is called.

The returned results will be sorted with the most useful first — this is typically the remote which claims to provide the most of *`refs`* , at the lowest latency.

Each result contains a list of the subset of *`refs`* it claims to provide. It is possible for a non-empty list of results to be returned, but for some of *`refs`* to not be listed in any of the results. Callers must check for this.

Pass the results to [`ostree_repo_pull_from_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-async "ostree_repo_pull_from_remotes_async ()") to pull the given *`refs`* from those remotes.

The following *`options`* are currently defined:

- `override-commit-ids` (`as`): Array of specific commit IDs to fetch. The nth commit ID applies to the nth ref, so this must be the same length as *`refs`* , if provided.

- `n-network-retries` (`u`): Number of times to retry each download on receiving a transient network error, such as a socket timeout; default is 5, 0 means return errors without retrying. Since: 2018.6

*`finders`* must be a non-empty `NULL`-terminated array of the [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") instances to use, or `NULL` to use the system default set of finders, which will typically be all available finders using their default options (but this is not guaranteed).

GPG verification of commits will be used unconditionally.

This will use the thread-default GMainContext, but will not iterate it.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| refs | non-empty array of collection–ref pairs to find remotes for. | \[array zero-terminated=1\] |
| options | a GVariant `a{sv}` with an extensible set of flags. | \[nullable\] |
| finders | non-empty array of [OstreeRepoFinder](reference__ostree-ostree-repo-finder.md#OstreeRepoFinder "OstreeRepoFinder") instances to use, or `NULL` to use the system defaults. | \[array zero-terminated=1\]\[transfer none\] |
| progress | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") to update with the operation’s progress, or `NULL`. | \[nullable\] |
| cancellable | a GCancellable, or `NULL`. | \[nullable\] |
| callback | asynchronous completion callback |   |
| user_data | data to pass to *`callback`* |   |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_find_remotes_finish ()

``` programlisting
OstreeRepoFinderResult **
ostree_repo_find_remotes_finish (OstreeRepo *self,
                                 GAsyncResult *result,
                                 GError **error);
```

Finish an asynchronous pull operation started with [`ostree_repo_find_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-find-remotes-async "ostree_repo_find_remotes_async ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| result | the asynchronous result |   |
| error | return location for a GError, or `NULL` |   |

#### Returns

a potentially empty array of OstreeRepoFinderResults, followed by a `NULL` terminator element; or `NULL` on error.

\[transfer full\]\[array zero-terminated=1\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_pull_from_remotes_async ()

``` programlisting
void
ostree_repo_pull_from_remotes_async (OstreeRepo *self,
                                     const OstreeRepoFinderResult *const *results,
                                     GVariant *options,
                                     OstreeAsyncProgress *progress,
                                     GCancellable *cancellable,
                                     GAsyncReadyCallback callback,
                                     gpointer user_data);
```

Pull refs from multiple remotes which have been found using [`ostree_repo_find_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-find-remotes-async "ostree_repo_find_remotes_async ()").

*`results`* are expected to be in priority order, with the best remotes to pull from listed first. [`ostree_repo_pull_from_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-async "ostree_repo_pull_from_remotes_async ()") will generally pull from the remotes in order, but may parallelise its downloads.

If an error is encountered when pulling from a given remote, that remote will be ignored and another will be tried instead. If any refs have not been downloaded successfully after all remotes have been tried, `G_IO_ERROR_FAILED` will be returned. The results of any successful downloads will remain cached in the local repository.

If *`cancellable`* is cancelled, `G_IO_ERROR_CANCELLED` will be returned immediately. The results of any successfully completed downloads at that point will remain cached in the local repository.

GPG verification of commits will be used unconditionally.

The following *`options`* are currently defined:

- `flags` (`i`): [OstreeRepoPullFlags](reference__ostree-OstreeRepo.md#OstreeRepoPullFlags "enum OstreeRepoPullFlags") to apply to the pull operation

- `inherit-transaction` (`b`): `TRUE` to inherit an ongoing transaction on the [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo"), rather than encapsulating the pull in a new one

- `depth` (`i`): How far in the history to traverse; default is 0, -1 means infinite

- `disable-static-deltas` (`b`): Do not use static deltas

- `http-headers` (`a(ss)`): Additional headers to add to all HTTP requests

- `subdirs` (`as`): Pull just these subdirectories

- `update-frequency` (`u`): Frequency to call the async progress callback in milliseconds, if any; only values higher than 0 are valid

- `append-user-agent` (`s`): Additional string to append to the user agent

- `n-network-retries` (`u`): Number of times to retry each download on receiving a transient network error, such as a socket timeout; default is 5, 0 means return errors without retrying. Since: 2018.6

- `ref-keyring-map` (`a(sss)`): Array of (collection ID, ref name, keyring remote name) tuples specifying which remote's keyring should be used when doing GPG verification of each collection-ref. This is useful to prevent a remote from serving malicious updates to refs which did not originate from it. This can be a subset or superset of the refs being pulled; any ref not being pulled will be ignored and any ref without a keyring remote will be verified with the keyring of the remote being pulled from.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| results | `NULL`-terminated array of remotes to pull from, including the refs to pull from each. | \[array zero-terminated=1\] |
| options | A GVariant `a{sv}` with an extensible set of flags. | \[nullable\] |
| progress | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") to update with the operation’s progress, or `NULL`. | \[nullable\] |
| cancellable | a GCancellable, or `NULL`. | \[nullable\] |
| callback | asynchronous completion callback |   |
| user_data | data to pass to *`callback`* |   |

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_pull_from_remotes_finish ()

``` programlisting
gboolean
ostree_repo_pull_from_remotes_finish (OstreeRepo *self,
                                      GAsyncResult *result,
                                      GError **error);
```

Finish an asynchronous pull operation started with [`ostree_repo_pull_from_remotes_async()`](reference__ostree-ostree-repo-remote-finder.md#ostree-repo-pull-from-remotes-async "ostree_repo_pull_from_remotes_async ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| result | the asynchronous result |   |
| error | return location for a GError, or `NULL` |   |

#### Returns

`TRUE` on success, `FALSE` otherwise

Since: 2018.6

------------------------------------------------------------------------

### ostree_repo_resolve_keyring_for_collection ()

``` programlisting
OstreeRemote *
ostree_repo_resolve_keyring_for_collection
                               (OstreeRepo *self,
                                const gchar *collection_id,
                                GCancellable *cancellable,
                                GError **error);
```

Find the GPG keyring for the given *`collection_id`* , using the local configuration from the given [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo"). This will search the configured remotes for ones whose `collection-id` key matches *`collection_id`* , and will return the first matching remote.

If multiple remotes match and have different keyrings, a debug message will be emitted, and the first result will be returned. It is expected that the keyrings should match.

If no match can be found, a `G_IO_ERROR_NOT_FOUND` error will be returned.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") |   |
| collection_id | the collection ID to look up a keyring for |   |
| cancellable | a GCancellable, or `NULL`. | \[nullable\] |
| error | return location for a GError, or `NULL` |   |

#### Returns

[OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") containing the GPG keyring for *`collection_id`* .

\[transfer full\]

Since: 2018.6

## Types and Values

### OSTREE_REPO_METADATA_REF

``` programlisting
#define OSTREE_REPO_METADATA_REF "ostree-metadata"
```

The name of a ref which is used to store metadata for the entire repository, such as its expected update time (`ostree.summary.expires`), name, or new GPG keys. Metadata is stored on contentless commits in the ref, and hence is signed with the commits.

This supersedes the additional metadata dictionary in the `summary` file (see [`ostree_repo_regenerate_summary()`](reference__ostree-OstreeRepo.md#ostree-repo-regenerate-summary "ostree_repo_regenerate_summary ()")), as the use of a ref means that the metadata for multiple upstream repositories can be included in a single mirror repository, disambiguating the refs using collection IDs. In order to support peer to peer redistribution of repository metadata, repositories must set a collection ID ([`ostree_repo_set_collection_id()`](reference__ostree-OstreeRepo.md#ostree-repo-set-collection-id "ostree_repo_set_collection_id ()")).

Users of OSTree may place arbitrary metadata in commits on this ref, but the keys must be namespaced by product or developer. For example, `exampleos.end-of-life`. The `ostree.` prefix is reserved.

Since: 2018.6

------------------------------------------------------------------------

### OSTREE_META_KEY_DEPLOY_COLLECTION_ID

``` programlisting
#define OSTREE_META_KEY_DEPLOY_COLLECTION_ID "ostree.deploy-collection-id"
```

GVariant type `s`. This key can be used in the repo metadata which is stored in OSTREE_REPO_METADATA_REF as well as in the summary. The semantics of this are that the remote repository wants clients to update their remote config to add this collection ID (clients can't do P2P operations involving a remote without a collection ID configured on it, even if one is configured on the server side). Clients must never change or remove a collection ID already set in their remote config.

Currently, OSTree does not implement changing a remote config based on this key, but it may do so in a later release, and until then clients such as Flatpak may implement it.

This is a replacement for the similar metadata key implemented by flatpak, `xa.collection-id`, which is now deprecated as clients which supported it had bugs with their P2P implementations.

Since: 2018.9

------------------------------------------------------------------------
