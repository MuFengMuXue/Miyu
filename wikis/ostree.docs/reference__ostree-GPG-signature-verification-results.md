[TABLE]

## Functions

|  |  |
|----|----|
| guint | [ostree_gpg_verify_result_count_all](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-count-all "ostree_gpg_verify_result_count_all ()") () |
| guint | [ostree_gpg_verify_result_count_valid](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-count-valid "ostree_gpg_verify_result_count_valid ()") () |
| gboolean | [ostree_gpg_verify_result_lookup](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-lookup "ostree_gpg_verify_result_lookup ()") () |
| GVariant \* | [ostree_gpg_verify_result_get](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-get "ostree_gpg_verify_result_get ()") () |
| GVariant \* | [ostree_gpg_verify_result_get_all](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-get-all "ostree_gpg_verify_result_get_all ()") () |
| void | [ostree_gpg_verify_result_describe](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-describe "ostree_gpg_verify_result_describe ()") () |
| void | [ostree_gpg_verify_result_describe_variant](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-describe-variant "ostree_gpg_verify_result_describe_variant ()") () |
| gboolean | [ostree_gpg_verify_result_require_valid_signature](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-require-valid-signature "ostree_gpg_verify_result_require_valid_signature ()") () |

## Types and Values

|  |  |
|----|----|
| enum | [OstreeGpgError](reference__ostree-GPG-signature-verification-results.md#OstreeGpgError "enum OstreeGpgError") |
| typedef | [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") |
| enum | [OstreeGpgSignatureAttr](reference__ostree-GPG-signature-verification-results.md#OstreeGpgSignatureAttr "enum OstreeGpgSignatureAttr") |
| enum | [OstreeGpgSignatureFormatFlags](reference__ostree-GPG-signature-verification-results.md#OstreeGpgSignatureFormatFlags "enum OstreeGpgSignatureFormatFlags") |

## Description

[OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") contains verification details for GPG signatures read from a detached [OstreeRepo](reference__ostree-OstreeRepo.md#OstreeRepo "OstreeRepo") metadata object.

Use [`ostree_gpg_verify_result_count_all()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-count-all "ostree_gpg_verify_result_count_all ()") and [`ostree_gpg_verify_result_count_valid()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-count-valid "ostree_gpg_verify_result_count_valid ()") to quickly check overall signature validity.

Use [`ostree_gpg_verify_result_lookup()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-lookup "ostree_gpg_verify_result_lookup ()") to find a signature by the key ID or fingerprint of the signing key.

For more in-depth inspection, such as presenting signature details to the user, pass an array of attribute values to [`ostree_gpg_verify_result_get()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-get "ostree_gpg_verify_result_get ()") or get all signature details with [`ostree_gpg_verify_result_get_all()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-get-all "ostree_gpg_verify_result_get_all ()").

## Functions

### ostree_gpg_verify_result_count_all ()

``` programlisting
guint
ostree_gpg_verify_result_count_all (OstreeGpgVerifyResult *result);
```

Counts all the signatures in *`result`* .

#### Parameters

|  |  |  |
|----|----|----|
| result | an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") |   |

#### Returns

signature count

------------------------------------------------------------------------

### ostree_gpg_verify_result_count_valid ()

``` programlisting
guint
ostree_gpg_verify_result_count_valid (OstreeGpgVerifyResult *result);
```

Counts only the valid signatures in *`result`* .

#### Parameters

|  |  |  |
|----|----|----|
| result | an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") |   |

#### Returns

valid signature count

------------------------------------------------------------------------

### ostree_gpg_verify_result_lookup ()

``` programlisting
gboolean
ostree_gpg_verify_result_lookup (OstreeGpgVerifyResult *result,
                                 const gchar *key_id,
                                 guint *out_signature_index);
```

Searches *`result`* for a signature signed by *`key_id`* . If a match is found, the function returns `TRUE` and sets *`out_signature_index`* so that further signature details can be obtained through [`ostree_gpg_verify_result_get()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-get "ostree_gpg_verify_result_get ()"). If no match is found, the function returns `FALSE` and leaves *`out_signature_index`* unchanged.

#### Parameters

|  |  |  |
|----|----|----|
| result | an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") |   |
| key_id | a GPG key ID or fingerprint |   |
| out_signature_index | return location for the index of the signature signed by *`key_id`* , or `NULL`. | \[out\] |

#### Returns

`TRUE` on success, `FALSE` on failure

------------------------------------------------------------------------

### ostree_gpg_verify_result_get ()

``` programlisting
GVariant *
ostree_gpg_verify_result_get (OstreeGpgVerifyResult *result,
                              guint signature_index,
                              OstreeGpgSignatureAttr *attrs,
                              guint n_attrs);
```

Builds a GVariant tuple of requested attributes for the GPG signature at *`signature_index`* in *`result`* . See the [OstreeGpgSignatureAttr](reference__ostree-GPG-signature-verification-results.md#OstreeGpgSignatureAttr "enum OstreeGpgSignatureAttr") description for the GVariantType of each available attribute.

It is a programmer error to request an invalid [OstreeGpgSignatureAttr](reference__ostree-GPG-signature-verification-results.md#OstreeGpgSignatureAttr "enum OstreeGpgSignatureAttr") or an invalid *`signature_index`* . Use [`ostree_gpg_verify_result_count_all()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-count-all "ostree_gpg_verify_result_count_all ()") to find the number of signatures in *`result`* .

#### Parameters

|  |  |  |
|----|----|----|
| result | an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") |   |
| signature_index | which signature to get attributes from |   |
| attrs | Array of requested attributes. | \[array length=n_attrs\] |
| n_attrs | Length of the *`attrs`* array |   |

#### Returns

a new, floating, GVariant tuple.

\[transfer floating\]

------------------------------------------------------------------------

### ostree_gpg_verify_result_get_all ()

``` programlisting
GVariant *
ostree_gpg_verify_result_get_all (OstreeGpgVerifyResult *result,
                                  guint signature_index);
```

Builds a GVariant tuple of all available attributes for the GPG signature at *`signature_index`* in *`result`* .

The child values in the returned GVariant tuple are ordered to match the [OstreeGpgSignatureAttr](reference__ostree-GPG-signature-verification-results.md#OstreeGpgSignatureAttr "enum OstreeGpgSignatureAttr") enumeration, which means the enum values can be used as index values in functions like `g_variant_get_child()`. See the [OstreeGpgSignatureAttr](reference__ostree-GPG-signature-verification-results.md#OstreeGpgSignatureAttr "enum OstreeGpgSignatureAttr") description for the GVariantType of each available attribute.

The [OstreeGpgSignatureAttr](reference__ostree-GPG-signature-verification-results.md#OstreeGpgSignatureAttr "enum OstreeGpgSignatureAttr") enumeration may be extended in the future with new attributes, which would affect the GVariant tuple returned by this function. While the position and type of current child values in the GVariant tuple will not change, to avoid backward-compatibility issues *please do not depend on the tuple's overall size or type signature*.

It is a programmer error to request an invalid *`signature_index`* . Use [`ostree_gpg_verify_result_count_all()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-count-all "ostree_gpg_verify_result_count_all ()") to find the number of signatures in *`result`* .

#### Parameters

|  |  |  |
|----|----|----|
| result | an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") |   |
| signature_index | which signature to get attributes from |   |

#### Returns

a new, floating, GVariant tuple.

\[transfer floating\]

------------------------------------------------------------------------

### ostree_gpg_verify_result_describe ()

``` programlisting
void
ostree_gpg_verify_result_describe (OstreeGpgVerifyResult *result,
                                   guint signature_index,
                                   GString *output_buffer,
                                   const gchar *line_prefix,
                                   OstreeGpgSignatureFormatFlags flags);
```

Appends a brief, human-readable description of the GPG signature at *`signature_index`* in *`result`* to the *`output_buffer`* . The description spans multiple lines. A *`line_prefix`* string, if given, will precede each line of the description.

The *`flags`* argument is reserved for future variations to the description format. Currently must be 0.

It is a programmer error to request an invalid *`signature_index`* . Use [`ostree_gpg_verify_result_count_all()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-count-all "ostree_gpg_verify_result_count_all ()") to find the number of signatures in *`result`* .

#### Parameters

|  |  |  |
|----|----|----|
| result | an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") |   |
| signature_index | which signature to describe |   |
| output_buffer | a GString to hold the description |   |
| line_prefix | optional line prefix string. | \[allow-none\] |
| flags | flags to adjust the description format |   |

------------------------------------------------------------------------

### ostree_gpg_verify_result_describe_variant ()

``` programlisting
void
ostree_gpg_verify_result_describe_variant
                               (GVariant *variant,
                                GString *output_buffer,
                                const gchar *line_prefix,
                                OstreeGpgSignatureFormatFlags flags);
```

Similar to [`ostree_gpg_verify_result_describe()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-describe "ostree_gpg_verify_result_describe ()") but takes a GVariant of all attributes for a GPG signature instead of an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult") and signature index.

The *`variant`* *MUST* have been created by [`ostree_gpg_verify_result_get_all()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-get-all "ostree_gpg_verify_result_get_all ()").

#### Parameters

|  |  |  |
|----|----|----|
| variant | a GVariant from [`ostree_gpg_verify_result_get_all()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-get-all "ostree_gpg_verify_result_get_all ()") |   |
| output_buffer | a GString to hold the description |   |
| line_prefix | optional line prefix string. | \[allow-none\] |
| flags | flags to adjust the description format |   |

------------------------------------------------------------------------

### ostree_gpg_verify_result_require_valid_signature ()

``` programlisting
gboolean
ostree_gpg_verify_result_require_valid_signature
                               (OstreeGpgVerifyResult *result,
                                GError **error);
```

Checks if the result contains at least one signature from the trusted keyring. You can call this function immediately after [`ostree_repo_verify_summary()`](reference__ostree-OstreeRepo.md#ostree-repo-verify-summary "ostree_repo_verify_summary ()") or [`ostree_repo_verify_commit_ext()`](reference__ostree-OstreeRepo.md#ostree-repo-verify-commit-ext "ostree_repo_verify_commit_ext ()") - it will handle the `NULL` *`result`* and filled *`error`* too.

#### Parameters

|  |  |  |
|----|----|----|
| result | an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult"). | \[nullable\] |
| error | A GError |   |

#### Returns

`TRUE` if *`result`* was not `NULL` and had at least one signature from trusted keyring, otherwise `FALSE`

Since: 2016.6

## Types and Values

### enum OstreeGpgError

Errors returned by signature creation and verification operations in OSTree. These may be returned by any API which creates or verifies signatures.

#### Members

|  |  |  |
|----|----|----|
| OSTREE_GPG_ERROR_NO_SIGNATURE | A signature was expected, but not found. |   |
| OSTREE_GPG_ERROR_INVALID_SIGNATURE | A signature was malformed. |   |
| OSTREE_GPG_ERROR_MISSING_KEY | A signature was found, but was created with a key not in the configured keyrings. |   |
| OSTREE_GPG_ERROR_EXPIRED_SIGNATURE | A signature was expired. Since: 2020.1. |   |
| OSTREE_GPG_ERROR_EXPIRED_KEY | A signature was found, but the key used to sign it has expired. Since: 2020.1. |   |
| OSTREE_GPG_ERROR_REVOKED_KEY | A signature was found, but the key used to sign it has been revoked. Since: 2020.1. |   |

Since: 2017.10

------------------------------------------------------------------------

### OstreeGpgVerifyResult

``` programlisting
typedef struct OstreeGpgVerifyResult OstreeGpgVerifyResult;
```

Private instance structure.

------------------------------------------------------------------------

### enum OstreeGpgSignatureAttr

Signature attributes available from an [OstreeGpgVerifyResult](reference__ostree-GPG-signature-verification-results.md#OstreeGpgVerifyResult "OstreeGpgVerifyResult"). The attribute's GVariantType is shown in brackets.

#### Members

|  |  |  |
|----|----|----|
| OSTREE_GPG_SIGNATURE_ATTR_VALID | \[G_VARIANT_TYPE_BOOLEAN\] Is the signature valid? |   |
| OSTREE_GPG_SIGNATURE_ATTR_SIG_EXPIRED | \[G_VARIANT_TYPE_BOOLEAN\] Has the signature expired? |   |
| OSTREE_GPG_SIGNATURE_ATTR_KEY_EXPIRED | \[G_VARIANT_TYPE_BOOLEAN\] Has the signing key expired? |   |
| OSTREE_GPG_SIGNATURE_ATTR_KEY_REVOKED | \[G_VARIANT_TYPE_BOOLEAN\] Has the signing key been revoked? |   |
| OSTREE_GPG_SIGNATURE_ATTR_KEY_MISSING | \[G_VARIANT_TYPE_BOOLEAN\] Is the signing key missing? |   |
| OSTREE_GPG_SIGNATURE_ATTR_FINGERPRINT | \[G_VARIANT_TYPE_STRING\] Fingerprint of the signing key |   |
| OSTREE_GPG_SIGNATURE_ATTR_TIMESTAMP | \[G_VARIANT_TYPE_INT64\] Signature creation Unix timestamp |   |
| OSTREE_GPG_SIGNATURE_ATTR_EXP_TIMESTAMP | \[G_VARIANT_TYPE_INT64\] Signature expiration Unix timestamp (0 if no expiration) |   |
| OSTREE_GPG_SIGNATURE_ATTR_PUBKEY_ALGO_NAME | \[G_VARIANT_TYPE_STRING\] Name of the public key algorithm used to create the signature |   |
| OSTREE_GPG_SIGNATURE_ATTR_HASH_ALGO_NAME | \[G_VARIANT_TYPE_STRING\] Name of the hash algorithm used to create the signature |   |
| OSTREE_GPG_SIGNATURE_ATTR_USER_NAME | \[G_VARIANT_TYPE_STRING\] The name of the signing key's primary user |   |
| OSTREE_GPG_SIGNATURE_ATTR_USER_EMAIL | \[G_VARIANT_TYPE_STRING\] The email address of the signing key's primary user |   |
| OSTREE_GPG_SIGNATURE_ATTR_FINGERPRINT_PRIMARY | \[G_VARIANT_TYPE_STRING\] Fingerprint of the signing key's primary key (will be the same as OSTREE_GPG_SIGNATURE_ATTR_FINGERPRINT if the the signature is already from the primary key rather than a subkey, and will be the empty string if the key is missing.) |   |
| OSTREE_GPG_SIGNATURE_ATTR_KEY_EXP_TIMESTAMP | \[G_VARIANT_TYPE_INT64\] Key expiration Unix timestamp (0 if no expiration or if the key is missing) |   |
| OSTREE_GPG_SIGNATURE_ATTR_KEY_EXP_TIMESTAMP_PRIMARY | \[G_VARIANT_TYPE_INT64\] Key expiration Unix timestamp of the signing key's primary key (will be the same as OSTREE_GPG_SIGNATURE_ATTR_KEY_EXP_TIMESTAMP if the signing key is the primary key and 0 if no expiration or if the key is missing) |   |

------------------------------------------------------------------------

### enum OstreeGpgSignatureFormatFlags

Formatting flags for [`ostree_gpg_verify_result_describe()`](reference__ostree-GPG-signature-verification-results.md#ostree-gpg-verify-result-describe "ostree_gpg_verify_result_describe ()"). Currently there's only one possible output format, but this enumeration allows for future variations.

#### Members

|                                     |                               |     |
|-------------------------------------|-------------------------------|-----|
| OSTREE_GPG_SIGNATURE_FORMAT_DEFAULT | Use the default output format |     |

------------------------------------------------------------------------
