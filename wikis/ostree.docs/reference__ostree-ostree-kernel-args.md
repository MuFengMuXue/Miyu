[TABLE]

## Functions

|  |  |
|----|----|
| void | [ostree_kernel_args_free](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-free "ostree_kernel_args_free ()") () |
| [OstreeKernelArgs](reference__ostree-ostree-kernel-args.md#OstreeKernelArgs "OstreeKernelArgs") \* | [ostree_kernel_args_new](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-new "ostree_kernel_args_new ()") () |
| void | [ostree_kernel_args_cleanup](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-cleanup "ostree_kernel_args_cleanup ()") () |
| void | [ostree_kernel_args_replace_take](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-replace-take "ostree_kernel_args_replace_take ()") () |
| void | [ostree_kernel_args_replace](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-replace "ostree_kernel_args_replace ()") () |
| void | [ostree_kernel_args_replace_argv](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-replace-argv "ostree_kernel_args_replace_argv ()") () |
| void | [ostree_kernel_args_append](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-append "ostree_kernel_args_append ()") () |
| void | [ostree_kernel_args_append_argv](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-append-argv "ostree_kernel_args_append_argv ()") () |
| void | [ostree_kernel_args_append_argv_filtered](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-append-argv-filtered "ostree_kernel_args_append_argv_filtered ()") () |
| void | [ostree_kernel_args_append_if_missing](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-append-if-missing "ostree_kernel_args_append_if_missing ()") () |
| gboolean | [ostree_kernel_args_new_replace](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-new-replace "ostree_kernel_args_new_replace ()") () |
| gboolean | [ostree_kernel_args_delete](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-delete "ostree_kernel_args_delete ()") () |
| gboolean | [ostree_kernel_args_delete_key_entry](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-delete-key-entry "ostree_kernel_args_delete_key_entry ()") () |
| gboolean | [ostree_kernel_args_append_proc_cmdline](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-append-proc-cmdline "ostree_kernel_args_append_proc_cmdline ()") () |
| void | [ostree_kernel_args_parse_append](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-parse-append "ostree_kernel_args_parse_append ()") () |
| const char \* | [ostree_kernel_args_get_last_value](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-get-last-value "ostree_kernel_args_get_last_value ()") () |
| [OstreeKernelArgs](reference__ostree-ostree-kernel-args.md#OstreeKernelArgs "OstreeKernelArgs") \* | [ostree_kernel_args_from_string](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-from-string "ostree_kernel_args_from_string ()") () |
| char \*\* | [ostree_kernel_args_to_strv](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-to-strv "ostree_kernel_args_to_strv ()") () |
| char \* | [ostree_kernel_args_to_string](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-to-string "ostree_kernel_args_to_string ()") () |
| gboolean | [ostree_kernel_args_contains](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-contains "ostree_kernel_args_contains ()") () |
| gboolean | [ostree_kernel_args_delete_if_present](reference__ostree-ostree-kernel-args.md#ostree-kernel-args-delete-if-present "ostree_kernel_args_delete_if_present ()") () |

## Types and Values

|  |  |
|----|----|
|   | [OstreeKernelArgs](reference__ostree-ostree-kernel-args.md#OstreeKernelArgs "OstreeKernelArgs") |

## Description

## Functions

### ostree_kernel_args_free ()

``` programlisting
void
ostree_kernel_args_free (OstreeKernelArgs *kargs);
```

Frees the kargs structure

#### Parameters

|       |                                                      |     |
|-------|------------------------------------------------------|-----|
| kargs | An OstreeKernelArgs that represents kernel arguments |     |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_new ()

``` programlisting
OstreeKernelArgs *
ostree_kernel_args_new (void);
```

Initializes a new OstreeKernelArgs structure and returns it

\[skip\]

#### Returns

A newly created [OstreeKernelArgs](reference__ostree-ostree-kernel-args.md#OstreeKernelArgs "OstreeKernelArgs") for kernel arguments.

\[transfer full\]

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_cleanup ()

``` programlisting
void
ostree_kernel_args_cleanup (void *loc);
```

Frees the OstreeKernelArgs structure pointed by \*loc

#### Parameters

|     |                                        |     |
|-----|----------------------------------------|-----|
| loc | Address of an OstreeKernelArgs pointer |     |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_replace_take ()

``` programlisting
void
ostree_kernel_args_replace_take (OstreeKernelArgs *kargs,
                                 char *arg);
```

Finds and replaces the old key if *`arg`* is already in the hash table, otherwise adds *`arg`* as new key and split_keyeq (arg) as value. Note that when replacing old key, the old values are freed.

#### Parameters

|       |                                        |                   |
|-------|----------------------------------------|-------------------|
| kargs | a OstreeKernelArgs instance            |                   |
| arg   | key or key/value pair for replacement. | \[transfer full\] |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_replace ()

``` programlisting
void
ostree_kernel_args_replace (OstreeKernelArgs *kargs,
                            const char *arg);
```

Finds and replaces the old key if *`arg`* is already in the hash table, otherwise adds *`arg`* as new key and split_keyeq (arg) as value. Note that when replacing old key value pair, the old values are freed.

#### Parameters

|       |                                       |     |
|-------|---------------------------------------|-----|
| kargs | a OstreeKernelArgs instance           |     |
| arg   | key or key/value pair for replacement |     |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_replace_argv ()

``` programlisting
void
ostree_kernel_args_replace_argv (OstreeKernelArgs *kargs,
                                 char **argv);
```

Finds and replaces each non-null arguments of *`argv`* in the hash table, otherwise adds individual arg as new key and split_keyeq (arg) as value. Note that when replacing old key value pair, the old values are freed.

#### Parameters

|       |                                    |     |
|-------|------------------------------------|-----|
| kargs | a OstreeKernelArgs instance        |     |
| argv  | an array of key or key/value pairs |     |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_append ()

``` programlisting
void
ostree_kernel_args_append (OstreeKernelArgs *kargs,
                           const char *arg);
```

Appends *`arg`* which is in the form of key=value pair to the hash table kargs-\>table (appends to the value list if key is already in the hash table) and appends key to kargs-\>order if it is not in the hash table already.

#### Parameters

|       |                                   |     |
|-------|-----------------------------------|-----|
| kargs | a OstreeKernelArgs instance       |     |
| arg   | key or key/value pair to be added |     |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_append_argv ()

``` programlisting
void
ostree_kernel_args_append_argv (OstreeKernelArgs *kargs,
                                char **argv);
```

Appends each value in *`argv`* to the corresponding value array and appends key to kargs-\>order if it is not in the hash table already.

#### Parameters

|       |                                       |                             |
|-------|---------------------------------------|-----------------------------|
| kargs | a OstreeKernelArgs instance           |                             |
| argv  | an array of key=value argument pairs. | \[array zero-terminated=1\] |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_append_argv_filtered ()

``` programlisting
void
ostree_kernel_args_append_argv_filtered
                               (OstreeKernelArgs *kargs,
                                char **argv,
                                char **prefixes);
```

Appends each argument that does not have one of the *`prefixes`* as prefix to the *`kargs`*

#### Parameters

|          |                                       |                             |
|----------|---------------------------------------|-----------------------------|
| kargs    | a OstreeKernelArgs instance           |                             |
| argv     | an array of key=value argument pairs. | \[array zero-terminated=1\] |
| prefixes | an array of prefix strings.           | \[array zero-terminated=1\] |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_append_if_missing ()

``` programlisting
void
ostree_kernel_args_append_if_missing (OstreeKernelArgs *kargs,
                                      const char *arg);
```

Appends *`arg`* which is in the form of key=value pair to the hash table kargs-\>table (appends to the value list if key is not in the hash table) and appends key to kargs-\>order if it is not in the hash table.

#### Parameters

|       |                                   |     |
|-------|-----------------------------------|-----|
| kargs | a OstreeKernelArgs instance       |     |
| arg   | key or key/value pair to be added |     |

Since: 2022.5

------------------------------------------------------------------------

### ostree_kernel_args_new_replace ()

``` programlisting
gboolean
ostree_kernel_args_new_replace (OstreeKernelArgs *kargs,
                                const char *arg,
                                GError **error);
```

This function implements the basic logic behind key/value pair replacement. Do note that the arg need to be properly formatted

When replacing key with exact one value, the arg can be in the form: key, key=new_val, or key=old_val=new_val The first one swaps the old_val with the key to an empty value The second and third replace the old_val into the new_val

When replacing key with multiple values, the arg can only be in the form of: key=old_val=new_val. Unless there is a special case where there is an empty value associated with the key, then key=new_val will work because old_val is empty. The empty val will be swapped with the new_val in that case

#### Parameters

|       |                           |     |
|-------|---------------------------|-----|
| kargs | OstreeKernelArgs instance |     |
| arg   | a string argument         |     |
| error | error instance            |     |

#### Returns

`TRUE` on success, `FALSE` on failure (and in some other instances such as:

1.  key not found in *`kargs`*

2.  old value not found when *`arg`* is in the form of key=old_val=new_val

3.  multiple old values found when *`arg`* is in the form of key=old_val)

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_delete ()

``` programlisting
gboolean
ostree_kernel_args_delete (OstreeKernelArgs *kargs,
                           const char *arg,
                           GError **error);
```

There are few scenarios being handled for deletion:

1: for input arg with a single key(i.e without = for split), the key/value pair will be deleted if there is only one value that is associated with the key

2: for input arg wth key/value pair, the specific key value pair will be deleted from the pointer array if those exist.

3: If the found key has only one value associated with it, the key entry in the table will also be removed, and the key will be removed from order table

#### Parameters

|       |                                    |     |
|-------|------------------------------------|-----|
| kargs | a OstreeKernelArgs instance        |     |
| arg   | key or key/value pair for deletion |     |
| error | an GError instance                 |     |

#### Returns

`TRUE` on success, `FALSE` on failure

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_delete_key_entry ()

``` programlisting
gboolean
ostree_kernel_args_delete_key_entry (OstreeKernelArgs *kargs,
                                     const char *key,
                                     GError **error);
```

This function removes the key entry from the hashtable as well from the order pointer array inside kargs

Note: since both table and order inside kernel args are with free function, no extra free functions are being called as they are done automatically by GLib

#### Parameters

|       |                              |     |
|-------|------------------------------|-----|
| kargs | an OstreeKernelArgs instance |     |
| key   | the key to remove            |     |
| error | an GError instance           |     |

#### Returns

`TRUE` on success, `FALSE` on failure

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_append_proc_cmdline ()

``` programlisting
gboolean
ostree_kernel_args_append_proc_cmdline
                               (OstreeKernelArgs *kargs,
                                GCancellable *cancellable,
                                GError **error);
```

Appends the command line arguments in the file "/proc/cmdline" that does not have "BOOT_IMAGE=" and "initrd=" as prefixes to the *`kargs`*

#### Parameters

|             |                                              |     |
|-------------|----------------------------------------------|-----|
| kargs       | a OstreeKernelArgs instance                  |     |
| cancellable | optional GCancellable object, NULL to ignore |     |
| error       | an GError instance                           |     |

#### Returns

`TRUE` on success, `FALSE` on failure

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_parse_append ()

``` programlisting
void
ostree_kernel_args_parse_append (OstreeKernelArgs *kargs,
                                 const char *options);
```

Parses *`options`* by separating it by whitespaces and appends each argument to *`kargs`*

#### Parameters

|         |                                              |     |
|---------|----------------------------------------------|-----|
| kargs   | a OstreeKernelArgs instance                  |     |
| options | a string representing command line arguments |     |

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_get_last_value ()

``` programlisting
const char *
ostree_kernel_args_get_last_value (OstreeKernelArgs *kargs,
                                   const char *key);
```

Finds and returns the last element of value array corresponding to the *`key`* in *`kargs`* hash table. Note that the application will be terminated if the *`key`* is found but the value array is empty

#### Parameters

|       |                                           |     |
|-------|-------------------------------------------|-----|
| kargs | a OstreeKernelArgs instance               |     |
| key   | a key to look for in *`kargs`* hash table |     |

#### Returns

`NULL` if *`key`* is not found in the *`kargs`* hash table, otherwise returns last element of value array corresponding to *`key`* .

\[nullable\]

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_from_string ()

``` programlisting
OstreeKernelArgs *
ostree_kernel_args_from_string (const char *options);
```

Initializes a new OstreeKernelArgs then parses and appends *`options`* to the empty OstreeKernelArgs

\[skip\]

#### Parameters

|         |                                              |     |
|---------|----------------------------------------------|-----|
| options | a string representing command line arguments |     |

#### Returns

newly allocated [OstreeKernelArgs](reference__ostree-ostree-kernel-args.md#OstreeKernelArgs "OstreeKernelArgs") with *`options`* appended.

\[transfer full\]

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_to_strv ()

``` programlisting
char **
ostree_kernel_args_to_strv (OstreeKernelArgs *kargs);
```

Extracts all key value pairs in *`kargs`* and appends to a temporary array in forms of "key=value" or "key" if value is NULL, and returns the temporary array with the GPtrArray wrapper freed

#### Parameters

|       |                             |     |
|-------|-----------------------------|-----|
| kargs | a OstreeKernelArgs instance |     |

#### Returns

an array of "key=value" pairs or "key" if value is NULL.

\[transfer full\]

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_to_string ()

``` programlisting
char *
ostree_kernel_args_to_string (OstreeKernelArgs *kargs);
```

Extracts all key value pairs in *`kargs`* and appends to a temporary GString in forms of "key=value" or "key" if value is NULL separated by a single whitespace, and returns the temporary string with the GString wrapper freed

Note: the application will be terminated if one of the values array in *`kargs`* is NULL

#### Parameters

|       |                             |     |
|-------|-----------------------------|-----|
| kargs | a OstreeKernelArgs instance |     |

#### Returns

a string of "key=value" pairs or "key" if value is NULL, separated by single whitespaces.

\[transfer full\]

Since: 2019.3

------------------------------------------------------------------------

### ostree_kernel_args_contains ()

``` programlisting
gboolean
ostree_kernel_args_contains (OstreeKernelArgs *kargs,
                             const char *arg);
```

Search for *`arg`* which is in the form of key=value pair at the hash table kargs-\>table and returns true if finds it.

#### Parameters

|       |                                |     |
|-------|--------------------------------|-----|
| kargs | a OstreeKernelArgs instance    |     |
| arg   | key or key/value pair to check |     |

#### Returns

`TRUE` if *`arg`* is contained in *`kargs`* , `FALSE` otherwise.

Since: 2022.7

------------------------------------------------------------------------

### ostree_kernel_args_delete_if_present ()

``` programlisting
gboolean
ostree_kernel_args_delete_if_present (OstreeKernelArgs *kargs,
                                      const char *arg,
                                      GError **error);
```

Deletes *`arg`* which is in the form of key=value pair from the hash table kargs-\>table.

#### Parameters

|       |                                     |     |
|-------|-------------------------------------|-----|
| kargs | a OstreeKernelArgs instance         |     |
| arg   | key or key/value pair to be deleted |     |
| error | an GError instance                  |     |

#### Returns

`TRUE` on success, `FALSE` on failure

Since: 2022.7

## Types and Values

### OstreeKernelArgs

``` programlisting
typedef struct _OstreeKernelArgs OstreeKernelArgs;
```

------------------------------------------------------------------------
