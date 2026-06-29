[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") \* | [ostree_async_progress_new](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-new "ostree_async_progress_new ()") () |
| [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") \* | [ostree_async_progress_new_and_connect](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-new-and-connect "ostree_async_progress_new_and_connect ()") () |
| void | [ostree_async_progress_copy_state](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-copy-state "ostree_async_progress_copy_state ()") () |
| char \* | [ostree_async_progress_get_status](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-get-status "ostree_async_progress_get_status ()") () |
| void | [ostree_async_progress_get](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-get "ostree_async_progress_get ()") () |
| GVariant \* | [ostree_async_progress_get_variant](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-get-variant "ostree_async_progress_get_variant ()") () |
| guint | [ostree_async_progress_get_uint](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-get-uint "ostree_async_progress_get_uint ()") () |
| guint64 | [ostree_async_progress_get_uint64](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-get-uint64 "ostree_async_progress_get_uint64 ()") () |
| void | [ostree_async_progress_set_status](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-set-status "ostree_async_progress_set_status ()") () |
| void | [ostree_async_progress_set](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-set "ostree_async_progress_set ()") () |
| void | [ostree_async_progress_set_variant](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-set-variant "ostree_async_progress_set_variant ()") () |
| void | [ostree_async_progress_set_uint](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-set-uint "ostree_async_progress_set_uint ()") () |
| void | [ostree_async_progress_set_uint64](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-set-uint64 "ostree_async_progress_set_uint64 ()") () |
| void | [ostree_async_progress_finish](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-finish "ostree_async_progress_finish ()") () |

## Types and Values

|  |  |
|----|----|
| typedef | [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") |

## Description

For many asynchronous operations, it's desirable for callers to be able to watch their status as they progress. For example, an user interface calling an asynchronous download operation will want to be able to see the total number of bytes downloaded.

This class provides a mechanism for callees of asynchronous operations to communicate back with callers. It transparently handles thread safety, ensuring that the progress change notification occurs in the thread-default context of the calling operation.

The [`ostree_async_progress_get_status()`](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-get-status "ostree_async_progress_get_status ()") and [`ostree_async_progress_set_status()`](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#ostree-async-progress-set-status "ostree_async_progress_set_status ()") methods get and set a well-known `status` key of type `G_VARIANT_TYPE_STRING`. This key may be accessed using the other [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") methods, but it must always have the correct type.

## Functions

### ostree_async_progress_new ()

``` programlisting
OstreeAsyncProgress *
ostree_async_progress_new (void);
```

#### Returns

A new progress object.

\[transfer full\]

------------------------------------------------------------------------

### ostree_async_progress_new_and_connect ()

``` programlisting
OstreeAsyncProgress *
ostree_async_progress_new_and_connect (void (*changed) (OstreeAsyncProgress *self, gpointer user_data),
                                       gpointer user_data);
```

\[skip\]

#### Parameters

|           |                             |     |
|-----------|-----------------------------|-----|
| changed   | a notification callback     |     |
| user_data | data to pass to *`changed`* |     |

#### Returns

A new progress object.

\[transfer full\]

------------------------------------------------------------------------

### ostree_async_progress_copy_state ()

``` programlisting
void
ostree_async_progress_copy_state (OstreeAsyncProgress *self,
                                  OstreeAsyncProgress *dest);
```

Atomically copies all the state from *`self`* to *`dest`* , without invoking the callback. This is used for proxying progress objects across different GMainContexts.

#### Parameters

|  |  |  |
|----|----|----|
| self | An [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") to copy from |   |
| dest | An [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") to copy to |   |

Since: 2019.6

------------------------------------------------------------------------

### ostree_async_progress_get_status ()

``` programlisting
char *
ostree_async_progress_get_status (OstreeAsyncProgress *self);
```

Get the human-readable status string from the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress"). This operation is thread-safe. The retuned value may be `NULL` if no status is set.

This is a convenience function to get the well-known `status` key.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") |   |

#### Returns

the current status, or `NULL` if none is set.

\[transfer full\]\[nullable\]

Since: 2017.6

------------------------------------------------------------------------

### ostree_async_progress_get ()

``` programlisting
void
ostree_async_progress_get (OstreeAsyncProgress *self,
                           ...);
```

Get the values corresponding to zero or more keys from the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress"). Each key is specified in @... as the key name, followed by a GVariant format string, followed by the necessary arguments for that format string, just as for `g_variant_get()`. After those arguments is the next key name. The varargs list must be `NULL`-terminated.

Each format string must make deep copies of its value, as the values stored in the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") may be freed from another thread after this function returns.

This operation is thread-safe, and all the keys are queried atomically.

[TABLE]

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") |   |
| ... | key name, format string, GVariant return locations, …, followed by `NULL` |   |

Since: 2017.6

------------------------------------------------------------------------

### ostree_async_progress_get_variant ()

``` programlisting
GVariant *
ostree_async_progress_get_variant (OstreeAsyncProgress *self,
                                   const char *key);
```

Look up a key in the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") and return the GVariant associated with it. The lookup is thread-safe.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") |   |
| key | a key to look up |   |

#### Returns

value for the given *`key`* , or `NULL` if it was not set.

\[transfer full\]\[nullable\]

Since: 2017.6

------------------------------------------------------------------------

### ostree_async_progress_get_uint ()

``` programlisting
guint
ostree_async_progress_get_uint (OstreeAsyncProgress *self,
                                const char *key);
```

------------------------------------------------------------------------

### ostree_async_progress_get_uint64 ()

``` programlisting
guint64
ostree_async_progress_get_uint64 (OstreeAsyncProgress *self,
                                  const char *key);
```

------------------------------------------------------------------------

### ostree_async_progress_set_status ()

``` programlisting
void
ostree_async_progress_set_status (OstreeAsyncProgress *self,
                                  const char *status);
```

Set the human-readable status string for the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress"). This operation is thread-safe. `NULL` may be passed to clear the status.

This is a convenience function to set the well-known `status` key.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") |   |
| status | new status string, or `NULL` to clear the status. | \[nullable\] |

Since: 2017.6

------------------------------------------------------------------------

### ostree_async_progress_set ()

``` programlisting
void
ostree_async_progress_set (OstreeAsyncProgress *self,
                           ...);
```

Set the values for zero or more keys in the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress"). Each key is specified in @... as the key name, followed by a GVariant format string, followed by the necessary arguments for that format string, just as for `g_variant_new()`. After those arguments is the next key name. The varargs list must be `NULL`-terminated.

g_variant_ref_sink() will be called as appropriate on the GVariant parameters, so they may be floating.

This operation is thread-safe, and all the keys are set atomically.

[TABLE]

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") |   |
| ... | key name, format string, GVariant parameters, …, followed by `NULL` |   |

Since: 2017.6

------------------------------------------------------------------------

### ostree_async_progress_set_variant ()

``` programlisting
void
ostree_async_progress_set_variant (OstreeAsyncProgress *self,
                                   const char *key,
                                   GVariant *value);
```

Assign a new *`value`* to the given *`key`* , replacing any existing value. The operation is thread-safe. *`value`* may be a floating reference; `g_variant_ref_sink()` will be called on it.

Any watchers of the [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") will be notified of the change if *`value`* differs from the existing value for *`key`* .

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeAsyncProgress](reference__ostree-Progress-notification-system-for-asynchronous-operations.md#OstreeAsyncProgress "OstreeAsyncProgress") |   |
| key | a key to set |   |
| value | the value to assign to *`key`* |   |

Since: 2017.6

------------------------------------------------------------------------

### ostree_async_progress_set_uint ()

``` programlisting
void
ostree_async_progress_set_uint (OstreeAsyncProgress *self,
                                const char *key,
                                guint value);
```

------------------------------------------------------------------------

### ostree_async_progress_set_uint64 ()

``` programlisting
void
ostree_async_progress_set_uint64 (OstreeAsyncProgress *self,
                                  const char *key,
                                  guint64 value);
```

------------------------------------------------------------------------

### ostree_async_progress_finish ()

``` programlisting
void
ostree_async_progress_finish (OstreeAsyncProgress *self);
```

Process any pending signals, ensuring the main context is cleared of sources used by this object. Also ensures that no further events will be queued.

#### Parameters

|      |      |     |
|------|------|-----|
| self | Self |     |

## Types and Values

### OstreeAsyncProgress

``` programlisting
typedef struct OstreeAsyncProgress OstreeAsyncProgress;
```

------------------------------------------------------------------------
