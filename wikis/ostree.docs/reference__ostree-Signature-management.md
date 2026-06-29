[TABLE]

## Functions

|  |  |
|----|----|
| GPtrArray \* | [ostree_sign_get_all](reference__ostree-Signature-management.md#ostree-sign-get-all "ostree_sign_get_all ()") () |
| gboolean | [ostree_sign_commit](reference__ostree-Signature-management.md#ostree-sign-commit "ostree_sign_commit ()") () |
| gboolean | [ostree_sign_commit_verify](reference__ostree-Signature-management.md#ostree-sign-commit-verify "ostree_sign_commit_verify ()") () |
| gboolean | [ostree_sign_data](reference__ostree-Signature-management.md#ostree-sign-data "ostree_sign_data ()") () |
| gboolean | [ostree_sign_data_verify](reference__ostree-Signature-management.md#ostree-sign-data-verify "ostree_sign_data_verify ()") () |
| [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") \* | [ostree_sign_get_by_name](reference__ostree-Signature-management.md#ostree-sign-get-by-name "ostree_sign_get_by_name ()") () |
| const gchar \* | [ostree_sign_get_name](reference__ostree-Signature-management.md#ostree-sign-get-name "ostree_sign_get_name ()") () |
| gboolean | [ostree_sign_add_pk](reference__ostree-Signature-management.md#ostree-sign-add-pk "ostree_sign_add_pk ()") () |
| gboolean | [ostree_sign_clear_keys](reference__ostree-Signature-management.md#ostree-sign-clear-keys "ostree_sign_clear_keys ()") () |
| gboolean | [ostree_sign_load_pk](reference__ostree-Signature-management.md#ostree-sign-load-pk "ostree_sign_load_pk ()") () |
| const gchar \* | [ostree_sign_metadata_format](reference__ostree-Signature-management.md#ostree-sign-metadata-format "ostree_sign_metadata_format ()") () |
| const gchar \* | [ostree_sign_metadata_key](reference__ostree-Signature-management.md#ostree-sign-metadata-key "ostree_sign_metadata_key ()") () |
| gboolean | [ostree_sign_set_pk](reference__ostree-Signature-management.md#ostree-sign-set-pk "ostree_sign_set_pk ()") () |
| gboolean | [ostree_sign_set_sk](reference__ostree-Signature-management.md#ostree-sign-set-sk "ostree_sign_set_sk ()") () |
| gboolean | [ostree_sign_summary](reference__ostree-Signature-management.md#ostree-sign-summary "ostree_sign_summary ()") () |
| OstreeBlobReader \* | [ostree_sign_read_pk](reference__ostree-Signature-management.md#ostree-sign-read-pk "ostree_sign_read_pk ()") () |
| OstreeBlobReader \* | [ostree_sign_read_sk](reference__ostree-Signature-management.md#ostree-sign-read-sk "ostree_sign_read_sk ()") () |

## Types and Values

|  |  |
|----|----|
|   | [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") |

## Description

An [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") interface allows to select and use any available engine for signing or verifying the commit object or summary file.

## Functions

### ostree_sign_get_all ()

``` programlisting
GPtrArray *
ostree_sign_get_all (void);
```

Return an array with newly allocated instances of all available signing engines; they will not be initialized.

#### Returns

an array of signing engines.

\[transfer full\]\[element-type OstreeSign\]

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_commit ()

``` programlisting
gboolean
ostree_sign_commit (OstreeSign *self,
                    OstreeRepo *repo,
                    const gchar *commit_checksum,
                    GCancellable *cancellable,
                    GError **error);
```

Add a signature to a commit.

Depending of the signing engine used you will need to load the secret key with [ostree_sign_set_sk](reference__ostree-Signature-management.md#ostree-sign-set-sk "ostree_sign_set_sk ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| repo | an OsreeRepo object |   |
| commit_checksum | SHA256 of given commit to sign |   |
| cancellable | A GCancellable |   |
| error | a GError |   |

#### Returns

*`TRUE`* if commit has been signed successfully, *`FALSE`* in case of error (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_commit_verify ()

``` programlisting
gboolean
ostree_sign_commit_verify (OstreeSign *self,
                           OstreeRepo *repo,
                           const gchar *commit_checksum,
                           char **out_success_message,
                           GCancellable *cancellable,
                           GError **error);
```

Verify if commit is signed with known key.

Depending of the signing engine used you will need to load the public key(s) for verification with [ostree_sign_set_pk](reference__ostree-Signature-management.md#ostree-sign-set-pk "ostree_sign_set_pk ()"), [ostree_sign_add_pk](reference__ostree-Signature-management.md#ostree-sign-add-pk "ostree_sign_add_pk ()") and/or [ostree_sign_load_pk](reference__ostree-Signature-management.md#ostree-sign-load-pk "ostree_sign_load_pk ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| repo | an OsreeRepo object |   |
| commit_checksum | SHA256 of given commit to verify |   |
| out_success_message | success message returned by the signing engine. | \[out\]\[nullable\]\[optional\] |
| cancellable | A GCancellable |   |
| error | a GError |   |

#### Returns

*`TRUE`* if commit has been verified successfully, *`FALSE`* in case of error or no valid keys are available (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_data ()

``` programlisting
gboolean
ostree_sign_data (OstreeSign *self,
                  GBytes *data,
                  GBytes **signature,
                  GCancellable *cancellable,
                  GError **error);
```

Sign the given *`data`* with pre-loaded secret key.

Depending of the signing engine used you will need to load the secret key with [ostree_sign_set_sk](reference__ostree-Signature-management.md#ostree-sign-set-sk "ostree_sign_set_sk ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| data | the raw data to be signed with pre-loaded secret key |   |
| signature | in case of success will contain signature. | \[out\] |
| cancellable | A GCancellable |   |
| error | a GError |   |

#### Returns

*`TRUE`* if *`data`* has been signed successfully, *`FALSE`* in case of error (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_data_verify ()

``` programlisting
gboolean
ostree_sign_data_verify (OstreeSign *self,
                         GBytes *data,
                         GVariant *signatures,
                         char **out_success_message,
                         GError **error);
```

Verify given data against signatures with pre-loaded public keys.

Depending of the signing engine used you will need to load the public key(s) with [ostree_sign_set_pk](reference__ostree-Signature-management.md#ostree-sign-set-pk "ostree_sign_set_pk ()"), [ostree_sign_add_pk](reference__ostree-Signature-management.md#ostree-sign-add-pk "ostree_sign_add_pk ()") or [ostree_sign_load_pk](reference__ostree-Signature-management.md#ostree-sign-load-pk "ostree_sign_load_pk ()").

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| data | the raw data to check |   |
| signatures | the signatures to be checked |   |
| out_success_message | success message returned by the signing engine. | \[out\]\[nullable\]\[optional\] |
| error | a GError |   |

#### Returns

*`TRUE`* if *`data`* has been signed at least with any single valid key, *`FALSE`* in case of error or no valid keys are available (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_get_by_name ()

``` programlisting
OstreeSign *
ostree_sign_get_by_name (const gchar *name,
                         GError **error);
```

Create a new instance of a signing engine.

#### Parameters

|       |                                      |     |
|-------|--------------------------------------|-----|
| name  | the name of desired signature engine |     |
| error | return location for a GError         |     |

#### Returns

New signing engine, or `NULL` if the engine is not known.

\[transfer full\]

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_get_name ()

``` programlisting
const gchar *
ostree_sign_get_name (OstreeSign *self);
```

Return the pointer to the name of currently used/selected signing engine.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |

#### Returns

pointer to the name *`NULL`* in case of error (unlikely).

\[transfer none\]

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_add_pk ()

``` programlisting
gboolean
ostree_sign_add_pk (OstreeSign *self,
                    GVariant *public_key,
                    GError **error);
```

Add the public key for verification. Could be called multiple times for adding all needed keys to be used for verification.

The *`public_key`* argument depends of the particular engine implementation.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| public_key | single public key to be added |   |
| error | a GError |   |

#### Returns

*`TRUE`* in case if the key could be added successfully, *`FALSE`* in case of error (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_clear_keys ()

``` programlisting
gboolean
ostree_sign_clear_keys (OstreeSign *self,
                        GError **error);
```

Clear all previously preloaded secret and public keys.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| error | a GError |   |

#### Returns

*`TRUE`* in case if no errors, *`FALSE`* in case of error

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_load_pk ()

``` programlisting
gboolean
ostree_sign_load_pk (OstreeSign *self,
                     GVariant *options,
                     GError **error);
```

Load public keys for verification from anywhere. It is expected that all keys would be added to already pre-loaded keys.

The *`options`* argument depends of the particular engine implementation.

For example, *`ed25515`* engine could use following string-formatted options:

- *`filename`* -- single file to use to load keys from

- *`basedir`* -- directory containing subdirectories 'trusted.ed25519.d' and 'revoked.ed25519.d' with appropriate public keys. Used for testing and re-definition of system-wide directories if defaults are not suitable for any reason.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| options | any options |   |
| error | a GError |   |

#### Returns

*`TRUE`* in case if at least one key could be load successfully, *`FALSE`* in case of error (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_metadata_format ()

``` programlisting
const gchar *
ostree_sign_metadata_format (OstreeSign *self);
```

Return the pointer to the string with format used in (detached) metadata for current signing engine.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |

#### Returns

pointer to the metadata format, *`NULL`* in case of error (unlikely).

\[transfer none\]

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_metadata_key ()

``` programlisting
const gchar *
ostree_sign_metadata_key (OstreeSign *self);
```

Return the pointer to the name of the key used in (detached) metadata for current signing engine.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |

#### Returns

pointer to the metadata key name, *`NULL`* in case of error (unlikely).

\[transfer none\]

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_set_pk ()

``` programlisting
gboolean
ostree_sign_set_pk (OstreeSign *self,
                    GVariant *public_key,
                    GError **error);
```

Set the public key for verification. It is expected what all previously pre-loaded public keys will be dropped.

The *`public_key`* argument depends of the particular engine implementation.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| public_key | single public key to be added |   |
| error | a GError |   |

#### Returns

*`TRUE`* in case if the key could be set successfully, *`FALSE`* in case of error (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_set_sk ()

``` programlisting
gboolean
ostree_sign_set_sk (OstreeSign *self,
                    GVariant *secret_key,
                    GError **error);
```

Set the secret key to be used for signing data, commits and summary.

The *`secret_key`* argument depends of the particular engine implementation.

#### Parameters

|  |  |  |
|----|----|----|
| self | an [OstreeSign](reference__ostree-Signature-management.md#OstreeSign "OstreeSign") object |   |
| secret_key | secret key to be added |   |
| error | a GError |   |

#### Returns

*`TRUE`* in case if the key could be set successfully, *`FALSE`* in case of error (*`error`* will contain the reason).

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_summary ()

``` programlisting
gboolean
ostree_sign_summary (OstreeSign *self,
                     OstreeRepo *repo,
                     GVariant *keys,
                     GCancellable *cancellable,
                     GError **error);
```

Add a signature to a summary file. Based on ostree_repo_add_gpg_signature_summary implementation.

#### Parameters

|  |  |  |
|----|----|----|
| self | Self |   |
| repo | ostree repository |   |
| keys | keys -- GVariant containing keys as GVarints specific to signature type. |   |
| cancellable | A GCancellable |   |
| error | a GError |   |

#### Returns

*`TRUE`* if summary file has been signed with all provided keys

Since: 2020.2

------------------------------------------------------------------------

### ostree_sign_read_pk ()

``` programlisting
OstreeBlobReader *
ostree_sign_read_pk (OstreeSign *self,
                     GInputStream *stream);
```

Start reading public keys from a stream.

#### Parameters

|        |                |     |
|--------|----------------|-----|
| self   | Self           |     |
| stream | a GInputStream |     |

#### Returns

a OstreamBlobReader or `NULL` on error.

\[transfer full\]

Since: 2025.2

------------------------------------------------------------------------

### ostree_sign_read_sk ()

``` programlisting
OstreeBlobReader *
ostree_sign_read_sk (OstreeSign *self,
                     GInputStream *stream);
```

Start reading secret keys from a stream.

#### Parameters

|        |                |     |
|--------|----------------|-----|
| self   | Self           |     |
| stream | a GInputStream |     |

#### Returns

a OstreamBlobReader or `NULL` on error.

\[transfer full\]

Since: 2025.2

## Types and Values

### OstreeSign

``` programlisting
typedef struct _OstreeSign OstreeSign;
```

------------------------------------------------------------------------
