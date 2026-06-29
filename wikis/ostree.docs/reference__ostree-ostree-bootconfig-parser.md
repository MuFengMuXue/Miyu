[TABLE]

## Functions

|  |  |
|----|----|
| [OstreeBootconfigParser](reference__ostree-ostree-bootconfig-parser.md#OstreeBootconfigParser "OstreeBootconfigParser") \* | [ostree_bootconfig_parser_new](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-new "ostree_bootconfig_parser_new ()") () |
| [OstreeBootconfigParser](reference__ostree-ostree-bootconfig-parser.md#OstreeBootconfigParser "OstreeBootconfigParser") \* | [ostree_bootconfig_parser_clone](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-clone "ostree_bootconfig_parser_clone ()") () |
| gboolean | [ostree_bootconfig_parser_parse](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-parse "ostree_bootconfig_parser_parse ()") () |
| gboolean | [ostree_bootconfig_parser_parse_at](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-parse-at "ostree_bootconfig_parser_parse_at ()") () |
| gboolean | [ostree_bootconfig_parser_write](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-write "ostree_bootconfig_parser_write ()") () |
| gboolean | [ostree_bootconfig_parser_write_at](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-write-at "ostree_bootconfig_parser_write_at ()") () |
| void | [ostree_bootconfig_parser_set](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-set "ostree_bootconfig_parser_set ()") () |
| const char \* | [ostree_bootconfig_parser_get](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-get "ostree_bootconfig_parser_get ()") () |
| void | [ostree_bootconfig_parser_set_overlay_initrds](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-set-overlay-initrds "ostree_bootconfig_parser_set_overlay_initrds ()") () |
| char \*\* | [ostree_bootconfig_parser_get_overlay_initrds](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-get-overlay-initrds "ostree_bootconfig_parser_get_overlay_initrds ()") () |
| guint64 | [ostree_bootconfig_parser_get_tries_left](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-get-tries-left "ostree_bootconfig_parser_get_tries_left ()") () |
| guint64 | [ostree_bootconfig_parser_get_tries_done](reference__ostree-ostree-bootconfig-parser.md#ostree-bootconfig-parser-get-tries-done "ostree_bootconfig_parser_get_tries_done ()") () |

## Types and Values

|  |  |
|----|----|
|   | [OstreeBootconfigParser](reference__ostree-ostree-bootconfig-parser.md#OstreeBootconfigParser "OstreeBootconfigParser") |

## Description

## Functions

### ostree_bootconfig_parser_new ()

``` programlisting
OstreeBootconfigParser *
ostree_bootconfig_parser_new (void);
```

------------------------------------------------------------------------

### ostree_bootconfig_parser_clone ()

``` programlisting
OstreeBootconfigParser *
ostree_bootconfig_parser_clone (OstreeBootconfigParser *self);
```

#### Parameters

|      |                     |     |
|------|---------------------|-----|
| self | Bootconfig to clone |     |

#### Returns

Copy of *`self`* .

\[transfer full\]

------------------------------------------------------------------------

### ostree_bootconfig_parser_parse ()

``` programlisting
gboolean
ostree_bootconfig_parser_parse (OstreeBootconfigParser *self,
                                GFile *path,
                                GCancellable *cancellable,
                                GError **error);
```

------------------------------------------------------------------------

### ostree_bootconfig_parser_parse_at ()

``` programlisting
gboolean
ostree_bootconfig_parser_parse_at (OstreeBootconfigParser *self,
                                   int dfd,
                                   const char *path,
                                   GCancellable *cancellable,
                                   GError **error);
```

Initialize a bootconfig from the given file.

#### Parameters

|             |              |     |
|-------------|--------------|-----|
| self        | Parser       |     |
| dfd         | Directory fd |     |
| path        | File path    |     |
| cancellable | Cancellable  |     |
| error       | Error        |     |

------------------------------------------------------------------------

### ostree_bootconfig_parser_write ()

``` programlisting
gboolean
ostree_bootconfig_parser_write (OstreeBootconfigParser *self,
                                GFile *output,
                                GCancellable *cancellable,
                                GError **error);
```

------------------------------------------------------------------------

### ostree_bootconfig_parser_write_at ()

``` programlisting
gboolean
ostree_bootconfig_parser_write_at (OstreeBootconfigParser *self,
                                   int dfd,
                                   const char *path,
                                   GCancellable *cancellable,
                                   GError **error);
```

------------------------------------------------------------------------

### ostree_bootconfig_parser_set ()

``` programlisting
void
ostree_bootconfig_parser_set (OstreeBootconfigParser *self,
                              const char *key,
                              const char *value);
```

Set the *`key`* /*`value`* pair to the boot configuration dictionary.

#### Parameters

|       |         |     |
|-------|---------|-----|
| self  | Parser  |     |
| key   | the key |     |
| value | the key |     |

------------------------------------------------------------------------

### ostree_bootconfig_parser_get ()

``` programlisting
const char *
ostree_bootconfig_parser_get (OstreeBootconfigParser *self,
                              const char *key);
```

Get the value corresponding to *`key`* from the boot configuration dictionary.

#### Parameters

|      |                          |     |
|------|--------------------------|-----|
| self | Parser                   |     |
| key  | the key name to retrieve |     |

#### Returns

The corresponding value, or `NULL` if the key hasn't been found.

\[nullable\]

------------------------------------------------------------------------

### ostree_bootconfig_parser_set_overlay_initrds ()

``` programlisting
void
ostree_bootconfig_parser_set_overlay_initrds
                               (OstreeBootconfigParser *self,
                                char **initrds);
```

These are rendered as additional `initrd` keys in the final bootloader configs. The base initrd is part of the primary keys.

#### Parameters

|  |  |  |
|----|----|----|
| self | Parser |   |
| initrds | Array of overlay initrds or `NULL` to unset. | \[array zero-terminated=1\]\[transfer none\]\[allow-none\] |

Since: 2020.7

------------------------------------------------------------------------

### ostree_bootconfig_parser_get_overlay_initrds ()

``` programlisting
char **
ostree_bootconfig_parser_get_overlay_initrds
                               (OstreeBootconfigParser *self);
```

#### Parameters

|      |        |     |
|------|--------|-----|
| self | Parser |     |

#### Returns

Array of initrds or `NULL` if none are set.

\[array zero-terminated=1\]\[transfer none\]\[nullable\]

Since: 2020.7

------------------------------------------------------------------------

### ostree_bootconfig_parser_get_tries_left ()

``` programlisting
guint64
ostree_bootconfig_parser_get_tries_left
                               (OstreeBootconfigParser *self);
```

#### Parameters

|      |        |     |
|------|--------|-----|
| self | Parser |     |

#### Returns

Amount of boot tries left

Since: 2025.2

------------------------------------------------------------------------

### ostree_bootconfig_parser_get_tries_done ()

``` programlisting
guint64
ostree_bootconfig_parser_get_tries_done
                               (OstreeBootconfigParser *self);
```

#### Parameters

|      |        |     |
|------|--------|-----|
| self | Parser |     |

#### Returns

Amount of boot tries

## Types and Values

### OstreeBootconfigParser

``` programlisting
typedef struct _OstreeBootconfigParser OstreeBootconfigParser;
```

------------------------------------------------------------------------
