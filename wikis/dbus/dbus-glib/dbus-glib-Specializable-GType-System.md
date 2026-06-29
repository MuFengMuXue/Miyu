|                      |     |     |     |     |
|:---------------------|-----|-----|-----|-----|
| Top  \|  Description |     |     |     |     |

<table width="100%">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td data-valign="top"><h2 id="specializable-gtype-system">Specializable GType System</h2>
<p>Specializable GType System — Specialized GTypes</p></td>
<td class="gallery_image" style="text-align: right;" data-valign="top"></td>
</tr>
</tbody>
</table>

## Stability Level

Unstable, unless otherwise indicated

## Functions

|  |  |
|----|----|
| void | (\*DBusGTypeSpecializedCollectionIterator) () |
| void | (\*DBusGTypeSpecializedMapIterator) () |
| gpointer | (\*DBusGTypeSpecializedConstructor) () |
| void | (\*DBusGTypeSpecializedFreeFunc) () |
| gpointer | (\*DBusGTypeSpecializedCopyFunc) () |
| gboolean | (\*DBusGTypeSpecializedCollectionFixedAccessorFunc) () |
| void | (\*DBusGTypeSpecializedCollectionIteratorFunc) () |
| void | (\*DBusGTypeSpecializedCollectionAppendFunc) () |
| void | (\*DBusGTypeSpecializedCollectionEndAppendFunc) () |
| void | (\*DBusGTypeSpecializedMapIteratorFunc) () |
| void | (\*DBusGTypeSpecializedMapAppendFunc) () |
| gboolean | (\*DBusGTypeSpecializedStructGetMember) () |
| gboolean | (\*DBusGTypeSpecializedStructSetMember) () |
| GType | dbus_g_type_get_collection () |
| GType | dbus_g_type_get_map () |
| GType | dbus_g_type_get_structv () |
| GType | dbus_g_type_get_struct () |
| gboolean | dbus_g_type_is_collection () |
| gboolean | dbus_g_type_is_map () |
| gboolean | dbus_g_type_is_struct () |
| GType | dbus_g_type_get_collection_specialization () |
| GType | dbus_g_type_get_map_key_specialization () |
| GType | dbus_g_type_get_map_value_specialization () |
| GType | dbus_g_type_get_struct_member_type () |
| guint | dbus_g_type_get_struct_size () |
| gpointer | dbus_g_type_specialized_construct () |
| void | dbus_g_type_specialized_init_append () |
| void | dbus_g_type_specialized_collection_append () |
| void | dbus_g_type_specialized_collection_end_append () |
| void | dbus_g_type_specialized_map_append () |
| gboolean | dbus_g_type_collection_get_fixed () |
| void | dbus_g_type_collection_value_iterate () |
| void | dbus_g_type_map_value_iterate () |
| gboolean | dbus_g_type_struct_get_member () |
| gboolean | dbus_g_type_struct_set_member () |
| gboolean | dbus_g_type_struct_get () |
| gboolean | dbus_g_type_struct_set () |
| void | dbus_g_type_specialized_init () |
| void | dbus_g_type_register_collection () |
| void | dbus_g_type_register_map () |
| const DBusGTypeSpecializedMapVtable \* | dbus_g_type_map_peek_vtable () |
| const DBusGTypeSpecializedCollectionVtable \* | dbus_g_type_collection_peek_vtable () |
| const DBusGTypeSpecializedStructVtable \* | dbus_g_type_struct_peek_vtable () |
| void | dbus_g_type_register_struct () |
| GVariant \* | dbus_g_value_build_g_variant () |
| void | dbus_g_value_parse_g_variant () |
| \#define | DBUS_TYPE_G_BOOLEAN_ARRAY |
| \#define | DBUS_TYPE_G_UCHAR_ARRAY |
| \#define | DBUS_TYPE_G_UINT_ARRAY |
| \#define | DBUS_TYPE_G_INT_ARRAY |
| \#define | DBUS_TYPE_G_UINT64_ARRAY |
| \#define | DBUS_TYPE_G_INT64_ARRAY |
| \#define | DBUS_TYPE_G_OBJECT_ARRAY |
| \#define | DBUS_TYPE_G_STRING_STRING_HASHTABLE |
| \#define | DBUS_TYPE_G_SIGNATURE |
| \#define | DBUS_TYPE_G_OBJECT_PATH |

## Types and Values

|         |                                      |
|---------|--------------------------------------|
|         | DBusGTypeSpecializedAppendContext    |
|         | DBusGTypeSpecializedVtable           |
|         | DBusGTypeSpecializedCollectionVtable |
|         | DBusGTypeSpecializedMapVtable        |
|         | DBusGTypeSpecializedStructVtable     |
| typedef | DBusGSignature                       |
| typedef | DBusGObjectPath                      |

## Includes

``` synopsis
#include <dbus/dbus-glib.h>
```

## Description

Specialized gtypes are basically a way to allow the definition of recursive GTypes. It allows the definition of 'containers' which is basically a user defined structure capable of holding other data, and a set of functions defining how to access that structure. Containers come in 3 flavors: collections, maps and structs.

A collection is a container that holds an ordered set of items, all of which must be the same type. (This is an *array* in standard D-Bus terminology.) dbus-glib specialized collections can be GArray (for numeric elements), GPtrArray (for string, object or boxed elements), GSList (for boxed elements, not recommended), or a user-defined type.

A map is a container that holds a set of key/value pairs. The keys have one type, and the values another; the type of the keys must be a numeric or string-like type. (This is a *dict* (dictionary) or *array of dict entry* in standard D-Bus terminology.) dbus-glib specialized maps can be GHashTable or a user-defined type.

A struct is a container that holds a fixed number of members, each member having a predefined type. (This is a *struct* in standard D-Bus terminology.) It is analogous to the C *`struct`* keyword, but dbus-glib does not generally represent D-Bus structs in C structs. dbus-glib specialized structs can be GValueArray or a user-defined type.

A specialization is a GType detailing a particular container with particular types (a type specialization).

Functions are provided for constructing and manipulating specializations.

This documentation needs splitting into two pages, one for defining new containers and using existing containers. I expect most users to only do the latter. I also need to add some examples.

## Functions

### DBusGTypeSpecializedCollectionIterator ()

``` programlisting
void
(*DBusGTypeSpecializedCollectionIterator)
                               (const GValue *value,
                                gpointer user_data);
```

`DBusGTypeSpecializedCollectionIterator` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

A library-user-supplied function, called for each element in the collection when `dbus_g_type_collection_value_iterate()` is called.

#### Parameters

|  |  |  |
|----|----|----|
| value | an element of the collection |   |
| user_data | the data supplied when calling `dbus_g_type_collection_value_iterate()` |   |

### DBusGTypeSpecializedMapIterator ()

``` programlisting
void
(*DBusGTypeSpecializedMapIterator) (const GValue *key_val,
                                    const GValue *value_val,
                                    gpointer user_data);
```

`DBusGTypeSpecializedMapIterator` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

A library-user-supplied function, called for each key/value pair in the collection when `dbus_g_type_map_value_iterate()` is called.

#### Parameters

|  |  |  |
|----|----|----|
| key_val | a key from the map |   |
| value_val | a value from the map |   |
| user_data | the data supplied when calling `dbus_g_type_map_value_iterate()` |   |

### DBusGTypeSpecializedConstructor ()

``` programlisting
gpointer
(*DBusGTypeSpecializedConstructor) (GType type);
```

`DBusGTypeSpecializedConstructor` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

#### Parameters

|      |                          |     |
|------|--------------------------|-----|
| type | a specialized boxed type |     |

#### Returns

a new instance of *`type`*

### DBusGTypeSpecializedFreeFunc ()

``` programlisting
void
(*DBusGTypeSpecializedFreeFunc) (GType type,
                                 gpointer val);
```

`DBusGTypeSpecializedFreeFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Frees *`val`* according to *`type`* . This is analogous to GBoxedFreeFunc, but can use information from *`type`* (for instance to free the contents of a container before freeing the actual container).

#### Parameters

|      |                          |     |
|------|--------------------------|-----|
| type | a specialized boxed type |     |
| val  | an instance of *`type`*  |     |

### DBusGTypeSpecializedCopyFunc ()

``` programlisting
gpointer
(*DBusGTypeSpecializedCopyFunc) (GType type,
                                 gpointer src);
```

`DBusGTypeSpecializedCopyFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Copies *`src`* according to *`type`* . This is analogous to GBoxedCopyFunc, but can use information from *`type`* (for instance to copy each element of a collection).

#### Parameters

|      |                          |     |
|------|--------------------------|-----|
| type | a specialized boxed type |     |
| src  | an instance of *`type`*  |     |

#### Returns

a deep copy of *`src`*

### DBusGTypeSpecializedCollectionFixedAccessorFunc ()

``` programlisting
gboolean
(*DBusGTypeSpecializedCollectionFixedAccessorFunc)
                               (GType type,
                                gpointer instance,
                                gpointer *values,
                                guint *len);
```

`DBusGTypeSpecializedCollectionFixedAccessorFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_collection_get_fixed()` for a GValue with type *`type`* , containing *`instance`* .

#### Parameters

|          |                                                          |     |
|----------|----------------------------------------------------------|-----|
| type     | a specialized collection boxed type                      |     |
| instance | an instance of *`type`*                                  |     |
| values   | used to return a pointer to the contents of *`instance`* |     |
| len      | used to return the number of elements in *`instance`*    |     |

#### Returns

`TRUE` on success

### DBusGTypeSpecializedCollectionIteratorFunc ()

``` programlisting
void
(*DBusGTypeSpecializedCollectionIteratorFunc)
                               (GType type,
                                gpointer instance,
                                DBusGTypeSpecializedCollectionIterator iterator,
                                gpointer user_data);
```

`DBusGTypeSpecializedCollectionIteratorFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_collection_value_iterate()` for a GValue with type *`type`* , containing *`instance`* .

#### Parameters

|           |                                       |     |
|-----------|---------------------------------------|-----|
| type      | a specialized collection boxed type   |     |
| instance  | an instance of *`type`*               |     |
| iterator  | the function to call for each element |     |
| user_data | data to pass to *`iterator`*          |     |

### DBusGTypeSpecializedCollectionAppendFunc ()

``` programlisting
void
(*DBusGTypeSpecializedCollectionAppendFunc)
                               (DBusGTypeSpecializedAppendContext *ctx,
                                GValue *val);
```

`DBusGTypeSpecializedCollectionAppendFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_specialized_collection_append()`.

This function should use the *`val`* and *`specialization_type`* members of *`ctx`* .

#### Parameters

|  |  |  |
|----|----|----|
| ctx | an appending context returned by `dbus_g_type_specialized_init_append()` |   |
| val | a value to copy into the collection |   |

### DBusGTypeSpecializedCollectionEndAppendFunc ()

``` programlisting
void
(*DBusGTypeSpecializedCollectionEndAppendFunc)
                               (DBusGTypeSpecializedAppendContext *ctx);
```

`DBusGTypeSpecializedCollectionEndAppendFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_specialized_collection_end_append()`.

This function should use the *`val`* and *`specialization_type`* members of *`ctx`* .

#### Parameters

|  |  |  |
|----|----|----|
| ctx | an appending context returned by `dbus_g_type_specialized_init_append()` |   |

### DBusGTypeSpecializedMapIteratorFunc ()

``` programlisting
void
(*DBusGTypeSpecializedMapIteratorFunc)
                               (GType type,
                                gpointer instance,
                                DBusGTypeSpecializedMapIterator iterator,
                                gpointer user_data);
```

`DBusGTypeSpecializedMapIteratorFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_map_value_iterate()` for a GValue with type *`type`* , containing *`instance`* .

#### Parameters

|           |                                              |     |
|-----------|----------------------------------------------|-----|
| type      | a specialized map boxed type                 |     |
| instance  | an instance of *`type`*                      |     |
| iterator  | the function to call for each key/value pair |     |
| user_data | data to pass to *`iterator`*                 |     |

### DBusGTypeSpecializedMapAppendFunc ()

``` programlisting
void
(*DBusGTypeSpecializedMapAppendFunc) (DBusGTypeSpecializedAppendContext *ctx,
                                      GValue *key,
                                      GValue *val);
```

`DBusGTypeSpecializedMapAppendFunc` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_specialized_map_append()`.

This function should use the *`val`* and *`specialization_type`* members of *`ctx`* , and replace any existing value with key equal to *`key`* .

#### Parameters

|  |  |  |
|----|----|----|
| ctx | an appending context returned by `dbus_g_type_specialized_init_append()` |   |
| key | a key to add to the collection |   |
| val | a value to add to the collection |   |

### DBusGTypeSpecializedStructGetMember ()

``` programlisting
gboolean
(*DBusGTypeSpecializedStructGetMember)
                               (GType type,
                                gpointer instance,
                                guint member,
                                GValue *ret_value);
```

`DBusGTypeSpecializedStructGetMember` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_struct_get_member()` for a GValue with type *`type`* , containing *`instance`* .

#### Parameters

|  |  |  |
|----|----|----|
| type | a specialized struct boxed type |   |
| instance | an instance of *`type`* |   |
| member | the index of the member, starting from 0 |   |
| ret_value | an initialized GValue of the appropriate type for the given member of *`type`* |   |

#### Returns

`TRUE` on success

### DBusGTypeSpecializedStructSetMember ()

``` programlisting
gboolean
(*DBusGTypeSpecializedStructSetMember)
                               (GType type,
                                gpointer instance,
                                guint member,
                                const GValue *new_value);
```

`DBusGTypeSpecializedStructSetMember` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Implements `dbus_g_type_struct_set_member()` for a GValue with type *`type`* , containing *`instance`* .

#### Parameters

|  |  |  |
|----|----|----|
| type | a specialized struct boxed type |   |
| instance | an instance of *`type`* |   |
| member | the index of the member, starting from 0 |   |
| new_value | an initialized GValue of the appropriate type for the given member of *`type`* |   |

#### Returns

`TRUE` on success

### dbus_g_type_get_collection ()

``` programlisting
GType
dbus_g_type_get_collection (const char *container,
                            GType specialization);
```

`dbus_g_type_get_collection` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Gets a GType for a particular collection instance, creating the type if not already created.

#### Parameters

|                |                                                  |     |
|----------------|--------------------------------------------------|-----|
| container      | a string specifying a registered collection type |     |
| specialization | GType of collection elements                     |     |

#### Returns

the GType of that instance

### dbus_g_type_get_map ()

``` programlisting
GType
dbus_g_type_get_map (const char *container,
                     GType key_specialization,
                     GType value_specialization);
```

`dbus_g_type_get_map` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Gets a GType for a particular map instance, creating the type if not already created.

#### Parameters

|                      |                                           |     |
|----------------------|-------------------------------------------|-----|
| container            | a string specifying a registered map type |     |
| key_specialization   | GType of keys                             |     |
| value_specialization | GType of values                           |     |

#### Returns

the GType of that instance

### dbus_g_type_get_structv ()

``` programlisting
GType
dbus_g_type_get_structv (const char *container,
                         guint num_members,
                         GType *types);
```

`dbus_g_type_get_structv` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Gets a GType for a particular struct instance, creating the type if not already created.

#### Parameters

|             |                                                     |     |
|-------------|-----------------------------------------------------|-----|
| container   | a string specifying a registered struct type        |     |
| num_members | number of members in the struct                     |     |
| types       | an array specufying a GType for each struct element |     |

#### Returns

the GType of that instance

### dbus_g_type_get_struct ()

``` programlisting
GType
dbus_g_type_get_struct (const char *container,
                        GType first_type,
                        ...);
```

`dbus_g_type_get_struct` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Varags method to get a GType for a particular struct instance, creating the type if not already created.

#### Parameters

|  |  |  |
|----|----|----|
| container | a string specifying a registered struct type |   |
| first_type | GType for the struct's first member |   |
| ... | more GTypes for the struct's members, terminated by G_TYPE_INVALID |   |

#### Returns

the GType of that instance

### dbus_g_type_is_collection ()

``` programlisting
gboolean
dbus_g_type_is_collection (GType gtype);
```

`dbus_g_type_is_collection` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Tests if a given GType is a collection.

#### Parameters

|       |                 |     |
|-------|-----------------|-----|
| gtype | a GType to test |     |

#### Returns

true if the given GType is a collection

### dbus_g_type_is_map ()

``` programlisting
gboolean
dbus_g_type_is_map (GType gtype);
```

`dbus_g_type_is_map` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Tests if a given GType is a map, i.e. it was created with `dbus_g_type_get_map()`.

#### Parameters

|       |                 |     |
|-------|-----------------|-----|
| gtype | a GType to test |     |

#### Returns

true if the given GType is a map

### dbus_g_type_is_struct ()

``` programlisting
gboolean
dbus_g_type_is_struct (GType gtype);
```

`dbus_g_type_is_struct` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Tests if a given GType is a struct, i.e. it was created with `dbus_g_type_get_struct()`

#### Parameters

|       |                 |     |
|-------|-----------------|-----|
| gtype | a GType to test |     |

#### Returns

true if the given GType is a struct

### dbus_g_type_get_collection_specialization ()

``` programlisting
GType
dbus_g_type_get_collection_specialization
                               (GType gtype);
```

`dbus_g_type_get_collection_specialization` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Return the type of each element in collections of type *`gtype`* . It is an error to call this function on a non-collection type.

#### Parameters

|       |                                                                  |     |
|-------|------------------------------------------------------------------|-----|
| gtype | a collection GType, as created by `dbus_g_type_get_collection()` |     |

#### Returns

the element type for a given collection GType.

### dbus_g_type_get_map_key_specialization ()

``` programlisting
GType
dbus_g_type_get_map_key_specialization
                               (GType gtype);
```

`dbus_g_type_get_map_key_specialization` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Return the type of the keys in maps of type *`gtype`* . It is an error to call this function on a non-map type.

#### Parameters

|       |                                                    |     |
|-------|----------------------------------------------------|-----|
| gtype | a map GType, as created by `dbus_g_type_get_map()` |     |

#### Returns

the key type for a given map GType.

### dbus_g_type_get_map_value_specialization ()

``` programlisting
GType
dbus_g_type_get_map_value_specialization
                               (GType gtype);
```

`dbus_g_type_get_map_value_specialization` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Return the type of the values in maps of type *`gtype`* . It is an error to call this function on a non-map type.

#### Parameters

|       |                                                     |     |
|-------|-----------------------------------------------------|-----|
| gtype | a map GType, as created by `dbus_g_type_get_map()`. |     |

#### Returns

the value type for a given map GType.

### dbus_g_type_get_struct_member_type ()

``` programlisting
GType
dbus_g_type_get_struct_member_type (GType gtype,
                                    guint member);
```

`dbus_g_type_get_struct_member_type` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Get the type of a member of a specialized struct. It is an error to call this function on a non-struct type.

#### Parameters

|        |                                                            |     |
|--------|------------------------------------------------------------|-----|
| gtype  | a struct GType, as created with `dbus_g_type_get_struct()` |     |
| member | the index of a struct member                               |     |

#### Returns

the type for a given member of a struct GType, or `G_TYPE_INVALID` if *`member`* \>= `dbus_g_type_get_struct_size()`

### dbus_g_type_get_struct_size ()

``` programlisting
guint
dbus_g_type_get_struct_size (GType gtype);
```

`dbus_g_type_get_struct_size` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Get the number of members in a specialized struct. It is an error to call this function on a non-struct type.

#### Parameters

|       |                                                             |     |
|-------|-------------------------------------------------------------|-----|
| gtype | a struct GType, as created with `dbus_g_type_get_struct()`. |     |

#### Returns

the number of members in a given struct GType.

### dbus_g_type_specialized_construct ()

``` programlisting
gpointer
dbus_g_type_specialized_construct (GType gtype);
```

`dbus_g_type_specialized_construct` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Create an instance of a given specialized type. The structure created and returned will depend on the container type of the GType. E.g. If the given type was created by dbus_g_type_get_collection("GArray", G_TYPE_INT), then this will return a GArray with element_size of sizeof(int)

#### Parameters

|  |  |  |
|----|----|----|
| gtype | a specialized GType, as created by `dbus_g_type_get_collection()`, `dbus_g_type_get_map()` or `dbus_g_type_get_struct()` |   |

#### Returns

a pointer to a newly constructed instance of the given type.

### dbus_g_type_specialized_init_append ()

``` programlisting
void
dbus_g_type_specialized_init_append (GValue *value,
                                     DBusGTypeSpecializedAppendContext *ctx);
```

`dbus_g_type_specialized_init_append` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Create a new context for adding elements to a collection or key/value pairs to a map. You generally don't need or want to use this..

#### Parameters

|  |  |  |
|----|----|----|
| value | a GValue containing an instance of specialized type |   |
| ctx | a DBusGTypeSpecializedAppendContext in which to return a new appending context. |   |

### dbus_g_type_specialized_collection_append ()

``` programlisting
void
dbus_g_type_specialized_collection_append
                               (DBusGTypeSpecializedAppendContext *ctx,
                                GValue *elt);
```

`dbus_g_type_specialized_collection_append` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Appends a given element to the end of a collection.

#### Parameters

|  |  |  |
|----|----|----|
| ctx | a context created by `dbus_g_type_specialized_init_append()` for a GValue containing a collection |   |
| elt | a GValue containing an element to append to the collection |   |

### dbus_g_type_specialized_collection_end_append ()

``` programlisting
void
dbus_g_type_specialized_collection_end_append
                               (DBusGTypeSpecializedAppendContext *ctx);
```

`dbus_g_type_specialized_collection_end_append` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Finish appending elements to a given collection

#### Parameters

|  |  |  |
|----|----|----|
| ctx | a context created by `dbus_g_type_specialized_init_append()` for a GValue containing a collection |   |

### dbus_g_type_specialized_map_append ()

``` programlisting
void
dbus_g_type_specialized_map_append (DBusGTypeSpecializedAppendContext *ctx,
                                    GValue *key,
                                    GValue *val);
```

`dbus_g_type_specialized_map_append` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Inserts the given key/value pair into the map instance.

#### Parameters

|  |  |  |
|----|----|----|
| ctx | a context created by `dbus_g_type_specialized_init_append()` for a GValue containing a map |   |
| key | a GValue containing a key, whose contents will be stolen by *`ctx`* |   |
| val | a GValue containing a value, whose contents will be stolen by *`ctx`* |   |

### dbus_g_type_collection_get_fixed ()

``` programlisting
gboolean
dbus_g_type_collection_get_fixed (GValue *value,
                                  gpointer *data_ret,
                                  guint *len_ret);
```

`dbus_g_type_collection_get_fixed` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Calling this function is likely to be a bad idea. Consider using `dbus_g_type_collection_value_iterate()` instead.

On success, *`data_ret`* is a pointer to the underlying data in a collection of fixed-length fundamental types. Knowledge of the underlying data model of the collection is needed in order to use *`data_ret`* correctly.

It is an error to call this function on a specialized type that is not a collection, or on a collection that does not have a *`fixed_accessor`* in its DBusGTypeSpecializedCollectionVtable.

Specialized GArrays are the only types provided by dbus-glib that can be used with this function; user-defined types might also work.

#### Parameters

|  |  |  |
|----|----|----|
| value | a GValue containing a boxed specialized collection that has a *`fixed_accessor`* in its vtable |   |
| data_ret | used to return a pointer to the fixed data, which must not be modified (for instance, for a GArray of gint, this would point to an array of gint) |   |
| len_ret | used to return the length (counting collection elements, not bytes: in a GArray containing one gint, this would be 1) |   |

#### Returns

`TRUE` on success

### dbus_g_type_collection_value_iterate ()

``` programlisting
void
dbus_g_type_collection_value_iterate (const GValue *value,
                                      DBusGTypeSpecializedCollectionIterator iterator,
                                      gpointer user_data);
```

`dbus_g_type_collection_value_iterate` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Calls the given function for each element of the collection. The function is passed a GValue containing the element and the given *`user_data`* parameter. The collection may not be modified while iterating over it.

#### Parameters

|           |                                       |     |
|-----------|---------------------------------------|-----|
| value     | a GValue holding a collection type.   |     |
| iterator  | a function to call for each element   |     |
| user_data | user data to pass to the *`iterator`* |     |

### dbus_g_type_map_value_iterate ()

``` programlisting
void
dbus_g_type_map_value_iterate (const GValue *value,
                               DBusGTypeSpecializedMapIterator iterator,
                               gpointer user_data);
```

`dbus_g_type_map_value_iterate` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Calls the given function for each key/value pair of the map. The function is passed two GValues containing the key/value pair and the given *`user_data`* parameter. The map may not be modified while iterating over it.

#### Parameters

|           |                                       |     |
|-----------|---------------------------------------|-----|
| value     | a GValue holding a specialized map    |     |
| iterator  | a function to call for each element   |     |
| user_data | user data to pass to the *`iterator`* |     |

### dbus_g_type_struct_get_member ()

``` programlisting
gboolean
dbus_g_type_struct_get_member (const GValue *value,
                               guint member,
                               GValue *dest);
```

`dbus_g_type_struct_get_member` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Fetches a given member of a given struct instance. *`dest`* must be initialised was the correct type for that member, e.g. as returned by *`dbus_g_type_get_struct_member_type`*

#### Parameters

|        |                                                            |     |
|--------|------------------------------------------------------------|-----|
| value  | a GValue containing a struct instance                      |     |
| member | the index of a given member                                |     |
| dest   | an initialised GValue in which to return the struct member |     |

#### Returns

`TRUE` if successful

### dbus_g_type_struct_set_member ()

``` programlisting
gboolean
dbus_g_type_struct_set_member (GValue *value,
                               guint member,
                               const GValue *src);
```

`dbus_g_type_struct_set_member` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Sets a given member of a struct to a new value. The type of *`src`* must match the existing type of *`member`* member of the struct.

#### Parameters

|        |                                                           |     |
|--------|-----------------------------------------------------------|-----|
| value  | a GValue containing a struct instance                     |     |
| member | the index of a given member                               |     |
| src    | an GValue containing the new value for that struct member |     |

#### Returns

`TRUE` if successful

### dbus_g_type_struct_get ()

``` programlisting
gboolean
dbus_g_type_struct_get (const GValue *value,
                        guint member,
                        ...);
```

`dbus_g_type_struct_get` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Collects the selected values of this struct into the return locations provided.

#### Parameters

|  |  |  |
|----|----|----|
| value | a GValue containing a struct instance |   |
| member | struct member to get |   |
| ... | location in which to return the value of this member, followed optionally by more member/return locations pairs, followed by `G_MAXUINT` |   |

#### Returns

`FALSE` on failure

### dbus_g_type_struct_set ()

``` programlisting
gboolean
dbus_g_type_struct_set (GValue *value,
                        guint member,
                        ...);
```

`dbus_g_type_struct_set` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Sets the selected members of the struct in *`value`* .

#### Parameters

|  |  |  |
|----|----|----|
| value | a GValue containing a struct instance |   |
| member | struct member to set |   |
| ... | value for the first member, followed optionally by more member/value pairs, followed by `G_MAXUINT` |   |

#### Returns

`FALSE` on failure

### dbus_g_type_specialized_init ()

``` programlisting
void
dbus_g_type_specialized_init (void);
```

`dbus_g_type_specialized_init` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Initialize dbus-glib specialized GTypes.

In older versions of dbus-glib, it was necessary to do this before instantiating or registering any specialized type. It is now done automatically whenever necessary.

### dbus_g_type_register_collection ()

``` programlisting
void
dbus_g_type_register_collection (const char *name,
                                 const DBusGTypeSpecializedCollectionVtable *vtable,
                                 guint flags);
```

`dbus_g_type_register_collection` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Defines a new collection container.

#### Parameters

|        |                                        |     |
|--------|----------------------------------------|-----|
| name   | The name of a new collection container |     |
| vtable | the vtable defining the new container  |     |
| flags  | As yet unused.                         |     |

### dbus_g_type_register_map ()

``` programlisting
void
dbus_g_type_register_map (const char *name,
                          const DBusGTypeSpecializedMapVtable *vtable,
                          guint flags);
```

`dbus_g_type_register_map` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Defines a new map container.

#### Parameters

|        |                                       |     |
|--------|---------------------------------------|-----|
| name   | The name of a new map container       |     |
| vtable | the vtable defining the new container |     |
| flags  | As yet unused.                        |     |

### dbus_g_type_map_peek_vtable ()

``` programlisting
const DBusGTypeSpecializedMapVtable *
dbus_g_type_map_peek_vtable (GType map_type);
```

`dbus_g_type_map_peek_vtable` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Peek the vtable for a given map specialization

#### Parameters

|          |                                 |     |
|----------|---------------------------------|-----|
| map_type | a gtype of a map specialization |     |

#### Returns

the vtable

### dbus_g_type_collection_peek_vtable ()

``` programlisting
const DBusGTypeSpecializedCollectionVtable *
dbus_g_type_collection_peek_vtable (GType collection_type);
```

`dbus_g_type_collection_peek_vtable` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Peek the vtable for a given collection specialization

#### Parameters

|                 |                                        |     |
|-----------------|----------------------------------------|-----|
| collection_type | a gtype of a collection specialization |     |

#### Returns

the vtable

### dbus_g_type_struct_peek_vtable ()

``` programlisting
const DBusGTypeSpecializedStructVtable *
dbus_g_type_struct_peek_vtable (GType struct_type);
```

`dbus_g_type_struct_peek_vtable` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Peek the vtable for a given struct specialization

#### Parameters

|             |                                    |     |
|-------------|------------------------------------|-----|
| struct_type | a gtype of a struct specialization |     |

#### Returns

the vtable

### dbus_g_type_register_struct ()

``` programlisting
void
dbus_g_type_register_struct (const char *name,
                             const DBusGTypeSpecializedStructVtable *vtable,
                             guint flags);
```

`dbus_g_type_register_struct` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Defines a new struct container.

#### Parameters

|        |                                       |     |
|--------|---------------------------------------|-----|
| name   | The name of a new struct container    |     |
| vtable | the vtable defining the new container |     |
| flags  | As yet unused.                        |     |

### dbus_g_value_build_g_variant ()

``` programlisting
GVariant *
dbus_g_value_build_g_variant (const GValue *value);
```

`dbus_g_value_build_g_variant` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Recurses *`value`* and converts its contents to a GVariant.

The value must either be a simple value (integer, string, boolean, object path etc.) or a specialized container registered with `dbus_g_type_get_collection()`, `dbus_g_type_get_map()` or `dbus_g_type_get_struct()`. Providing any other type is a programming error (including as a child type).

#### Parameters

|       |                                                         |     |
|-------|---------------------------------------------------------|-----|
| value | a simple or specialized GValue to convert to a GVariant |     |

#### Returns

a new GVariant containing *`value`* with a floating reference

### dbus_g_value_parse_g_variant ()

``` programlisting
void
dbus_g_value_parse_g_variant (GVariant *variant,
                              GValue *value);
```

`dbus_g_value_parse_g_variant` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

Deserialize *`variant`* and put an equivalent dbus-glib data structure in *`value`* .

It is an error if *`variant`* contains any GVariant extensions not supported by dbus-glib, including handles (file descriptor passing) and 'maybe' types.

#### Parameters

|         |                      |     |
|---------|----------------------|-----|
| variant | a GVariant           |     |
| value   | a zero-filled GValue |     |

### DBUS_TYPE_G_BOOLEAN_ARRAY

``` programlisting
#define DBUS_TYPE_G_BOOLEAN_ARRAY  (dbus_g_type_get_collection ("GArray", G_TYPE_BOOLEAN))
```

`DBUS_TYPE_G_BOOLEAN_ARRAY` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE ("ab")`.

Expands to a function call returning the GType of a GArray of gboolean (corresponding to the D-Bus signature "ab").

### DBUS_TYPE_G_UCHAR_ARRAY

``` programlisting
#define DBUS_TYPE_G_UCHAR_ARRAY    (dbus_g_type_get_collection ("GArray", G_TYPE_UCHAR))
```

`DBUS_TYPE_G_UCHAR_ARRAY` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE_BYTESTRING`.

Expands to a function call returning the GType of a GArray of guchar (corresponding to the D-Bus signature "ay").

Note that this is not the same thing as a GByteArray! dbus-glib does not know about the GByteArray type.

### DBUS_TYPE_G_UINT_ARRAY

``` programlisting
#define DBUS_TYPE_G_UINT_ARRAY     (dbus_g_type_get_collection ("GArray", G_TYPE_UINT))
```

`DBUS_TYPE_G_UINT_ARRAY` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE ("au")`.

Expands to a function call returning the GType of a GArray of guint (corresponding to the D-Bus signature "au").

### DBUS_TYPE_G_INT_ARRAY

``` programlisting
#define DBUS_TYPE_G_INT_ARRAY      (dbus_g_type_get_collection ("GArray", G_TYPE_INT))
```

`DBUS_TYPE_G_INT_ARRAY` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE ("ai")`.

Expands to a function call returning the GType of a GArray of gint (corresponding to the D-Bus signature "ai").

### DBUS_TYPE_G_UINT64_ARRAY

``` programlisting
#define DBUS_TYPE_G_UINT64_ARRAY   (dbus_g_type_get_collection ("GArray", G_TYPE_UINT64))
```

`DBUS_TYPE_G_UINT64_ARRAY` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE ("at")`.

Expands to a function call returning the GType of a GArray of guint64 (corresponding to the D-Bus signature "at").

### DBUS_TYPE_G_INT64_ARRAY

``` programlisting
#define DBUS_TYPE_G_INT64_ARRAY    (dbus_g_type_get_collection ("GArray", G_TYPE_INT64))
```

`DBUS_TYPE_G_INT64_ARRAY` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE ("ax")`.

Expands to a function call returning the GType of a GArray of gint64 (corresponding to the D-Bus signature "ax").

### DBUS_TYPE_G_OBJECT_ARRAY

``` programlisting
#define DBUS_TYPE_G_OBJECT_ARRAY   (dbus_g_type_get_collection ("GPtrArray", G_TYPE_OBJECT))
```

`DBUS_TYPE_G_OBJECT_ARRAY` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE_OBJECT_PATH_ARRAY`.

Expands to a function call returning the GType of a GPtrArray of GObject.

Use this type with caution: it can sometimes be used as a representation of arrays whose D-Bus signature is "ao" (transferred as an array of object paths), but the conventional type for such arrays is `(dbus_g_type_get_collection ("GPtrArray", DBUS_TYPE_G_OBJECT_PATH))`.

### DBUS_TYPE_G_STRING_STRING_HASHTABLE

``` programlisting
#define DBUS_TYPE_G_STRING_STRING_HASHTABLE (dbus_g_type_get_map ("GHashTable", G_TYPE_STRING, G_TYPE_STRING))
```

`DBUS_TYPE_G_STRING_STRING_HASHTABLE` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is `G_VARIANT_TYPE ("a{ss}")`.

Expands to a function call returning the GType of a GHashTable where the keys are strings and the values are also strings (corresponding to the D-Bus signature "a{ss}").

### DBUS_TYPE_G_SIGNATURE

``` programlisting
#define DBUS_TYPE_G_SIGNATURE (dbus_g_signature_get_g_type ())
```

`DBUS_TYPE_G_SIGNATURE` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is a GVariant (`G_TYPE_VARIANT`) of type `G_VARIANT_TYPE_SIGNATURE`.

The GType of a DBusGSignature, which is a boxed type containing a D-Bus signature as a zero-terminated string. Signatures can be copied with `g_strdup()` and freed with `g_free()`, just like `G_TYPE_STRING`, but have a distinct boxed type to allow them to be distinguished when stored in a GValue.

#### Returns

a type derived from `G_TYPE_BOXED`

### DBUS_TYPE_G_OBJECT_PATH

``` programlisting
#define DBUS_TYPE_G_OBJECT_PATH (dbus_g_object_path_get_g_type ())
```

`DBUS_TYPE_G_OBJECT_PATH` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is a GVariant (`G_TYPE_VARIANT`) of type `G_VARIANT_TYPE_OBJECT_PATH`.

The GType of a DBusGObjectPath, which is a boxed type containing a D-Bus object path as a zero-terminated string. Object paths can be copied with `g_strdup()` and freed with `g_free()`, just like `G_TYPE_STRING`, but have a distinct boxed type to allow them to be distinguished when stored in a GValue.

#### Returns

a type derived from `G_TYPE_BOXED`

## Types and Values

### DBusGTypeSpecializedAppendContext

``` programlisting
typedef struct {
  /* public */
  GValue *val;
  GType specialization_type;
} DBusGTypeSpecializedAppendContext;
```

`DBusGTypeSpecializedAppendContext` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

A context for appending. There are more fields, which are private.

#### Members

|  |  |  |
|----|----|----|
| GValue \**`val`*; | the GValue containing the array to which you're appending |   |
| GType *`specialization_type`*; | the GType of the array's elements |   |

### DBusGTypeSpecializedVtable

``` programlisting
typedef struct {
  DBusGTypeSpecializedConstructor    constructor;
  DBusGTypeSpecializedFreeFunc       free_func;
  DBusGTypeSpecializedCopyFunc       copy_func;
  GDestroyNotify                     simple_free_func; /* for type-independent freeing if possible */
} DBusGTypeSpecializedVtable;
```

`DBusGTypeSpecializedVtable` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

A table of methods used to implement specialized container behaviour on user-defined collections, maps and structs. Exactly one of *`free_func`* and *`simple_free_func`* must be implemented; the other must be `NULL`. *`constructor`* and *`copy_func`* must always be implemented.

There are additional members, which are reserved for future expansion and must be `NULL`.

#### Members

|  |  |  |
|----|----|----|
| DBusGTypeSpecializedConstructor *`constructor`*; | returns a new, blank instance of the *`type`* |   |
| DBusGTypeSpecializedFreeFunc *`free_func`*; | if not `NULL`, frees the *`type`* instance *`val`* |   |
| DBusGTypeSpecializedCopyFunc *`copy_func`*; | returns a "deep copy" of the *`type`* instance *`val`* |   |
| GDestroyNotify *`simple_free_func`*; | if not `NULL`, frees its argument |   |

### DBusGTypeSpecializedCollectionVtable

``` programlisting
typedef struct {
  DBusGTypeSpecializedVtable                        base_vtable;
  DBusGTypeSpecializedCollectionFixedAccessorFunc   fixed_accessor;
  DBusGTypeSpecializedCollectionIteratorFunc        iterator;
  DBusGTypeSpecializedCollectionAppendFunc          append_func;
  DBusGTypeSpecializedCollectionEndAppendFunc       end_append_func;
} DBusGTypeSpecializedCollectionVtable;
```

`DBusGTypeSpecializedCollectionVtable` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

A table of methods used to implement specialized collection behaviour on user-defined types. At least *`iterator`* and *`append_func`* must be implemented.

#### Members

|  |  |  |
|----|----|----|
| DBusGTypeSpecializedVtable *`base_vtable`*; | base methods shared between collections and other types |   |
| DBusGTypeSpecializedCollectionFixedAccessorFunc *`fixed_accessor`*; | if not `NULL`, provides access to the contents of this collection, as documented for `dbus_g_type_collection_get_fixed()` |   |
| DBusGTypeSpecializedCollectionIteratorFunc *`iterator`*; | iterates through the members of *`instance`* |   |
| DBusGTypeSpecializedCollectionAppendFunc *`append_func`*; | appends a new member to *`instance`* |   |
| DBusGTypeSpecializedCollectionEndAppendFunc *`end_append_func`*; | if not `NULL`, called after each group of calls to the *`append_func`* |   |

### DBusGTypeSpecializedMapVtable

``` programlisting
typedef struct {
  DBusGTypeSpecializedVtable                        base_vtable;
  DBusGTypeSpecializedMapIteratorFunc               iterator;
  DBusGTypeSpecializedMapAppendFunc                 append_func;
} DBusGTypeSpecializedMapVtable;
```

`DBusGTypeSpecializedMapVtable` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

A table of methods used to implement specialized collection behaviour on user-defined types. Both methods must be implemented.

#### Members

|  |  |  |
|----|----|----|
| DBusGTypeSpecializedVtable *`base_vtable`*; | base methods shared between maps and other types |   |
| DBusGTypeSpecializedMapIteratorFunc *`iterator`*; | iterates through the members of *`instance`* |   |
| DBusGTypeSpecializedMapAppendFunc *`append_func`*; | adds a new key/value pair to *`instance`* |   |

### DBusGTypeSpecializedStructVtable

``` programlisting
typedef struct {
  DBusGTypeSpecializedVtable                        base_vtable;
  DBusGTypeSpecializedStructGetMember               get_member;
  DBusGTypeSpecializedStructSetMember               set_member;
} DBusGTypeSpecializedStructVtable;
```

`DBusGTypeSpecializedStructVtable` is deprecated and should not be used in newly-written code.

New code should use GDBus instead.

A table of methods used to implement specialized collection behaviour on user-defined types. Both methods must be implemented.

#### Members

|  |  |  |
|----|----|----|
| DBusGTypeSpecializedVtable *`base_vtable`*; | base methods shared between maps and other types |   |
| DBusGTypeSpecializedStructGetMember *`get_member`*; | returns a member by its index |   |
| DBusGTypeSpecializedStructSetMember *`set_member`*; | sets a member by its index |   |

### DBusGSignature

``` programlisting
typedef gchar DBusGSignature;
```

`DBusGSignature` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is a GVariant (`G_TYPE_VARIANT`) of type `G_VARIANT_TYPE_SIGNATURE`.

A typedef for a string used to represent D-Bus signatures. Its GType is `DBUS_TYPE_G_SIGNATURE`, derived from `G_TYPE_BOXED`.

Prior to version 0.FIXME this was used as the type name of `DBUS_TYPE_G_SIGNATURE`, but did not actually exist as a typedef.

Since 0.FIXME

### DBusGObjectPath

``` programlisting
typedef gchar DBusGObjectPath;
```

`DBusGObjectPath` is deprecated and should not be used in newly-written code.

New code should use GDBus instead. The closest equivalent is a GVariant (`G_TYPE_VARIANT`) of type `G_VARIANT_TYPE_OBJECT_PATH`.

A typedef for a string used to represent D-Bus object paths. Its GType is `DBUS_TYPE_G_OBJECT_PATH`, derived from `G_TYPE_BOXED`.

Prior to version 0.FIXME this was used as the type name of `DBUS_TYPE_G_OBJECT_PATH`, but did not actually exist as a typedef.

Since 0.FIXME
