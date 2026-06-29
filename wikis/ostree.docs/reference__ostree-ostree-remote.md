[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") \* | [ostree_remote_ref](reference__ostree-ostree-remote.md#ostree-remote-ref "ostree_remote_ref ()") () |
| void | [ostree_remote_unref](reference__ostree-ostree-remote.md#ostree-remote-unref "ostree_remote_unref ()") () |
| const gchar \* | [ostree_remote_get_name](reference__ostree-ostree-remote.md#ostree-remote-get-name "ostree_remote_get_name ()") () |
| gchar \* | [ostree_remote_get_url](reference__ostree-ostree-remote.md#ostree-remote-get-url "ostree_remote_get_url ()") () |

## Types and Values

|  |  |
|----|----|
| struct | [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") |

## Description

## Functions

### ostree_remote_ref ()

``` programlisting
OstreeRemote *
ostree_remote_ref (OstreeRemote *remote);
```

Increase the reference count on the given *`remote`* .

#### Parameters

|  |  |  |
|----|----|----|
| remote | an [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") |   |

#### Returns

a copy of *`remote`* , for convenience.

\[transfer full\]

Since: 2018.6

------------------------------------------------------------------------

### ostree_remote_unref ()

``` programlisting
void
ostree_remote_unref (OstreeRemote *remote);
```

Decrease the reference count on the given *`remote`* and free it if the reference count reaches 0.

#### Parameters

|  |  |  |
|----|----|----|
| remote | an [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote"). | \[transfer full\] |

Since: 2018.6

------------------------------------------------------------------------

### ostree_remote_get_name ()

``` programlisting
const gchar *
ostree_remote_get_name (OstreeRemote *remote);
```

Get the human-readable name of the remote. This is what the user configured, if the remote was explicitly configured; and will otherwise be a stable, arbitrary, string.

#### Parameters

|  |  |  |
|----|----|----|
| remote | an [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") |   |

#### Returns

remote’s name

Since: 2018.6

------------------------------------------------------------------------

### ostree_remote_get_url ()

``` programlisting
gchar *
ostree_remote_get_url (OstreeRemote *remote);
```

Get the URL from the remote.

#### Parameters

|  |  |  |
|----|----|----|
| remote | an [OstreeRemote](reference__ostree-ostree-remote.md#OstreeRemote "struct OstreeRemote") |   |

#### Returns

the remote's URL.

\[transfer full\]\[nullable\]

Since: 2018.6

## Types and Values

### struct OstreeRemote

``` programlisting
struct OstreeRemote {
  int ref_count;      /* atomic */
  char *name;         /* (not nullable) */
  char *refspec_name; /* (nullable) */
  char *group;        /* group name in options (not nullable) */
  char *keyring;      /* keyring name ($refspec_name.trustedkeys.gpg) (not nullable) */
  GFile *file;        /* NULL if remote defined in repo/config */
  GKeyFile *options;
};
```

This represents the configuration for a single remote repository. Currently, remotes can only be passed around as (reference counted) opaque handles. In future, more API may be added to create and interrogate them.

Since: 2018.6

------------------------------------------------------------------------
