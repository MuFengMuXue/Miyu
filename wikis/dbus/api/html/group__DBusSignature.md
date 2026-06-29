Type signature parsing

D-Bus low-level public API

Parsing D-Bus type signatures. More...

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="data-structures" class="groupheader"> Data Structures</h2></td>
</tr>
<tr class="memitem:">
<td class="memItemLeft" style="text-align: right;" data-valign="top">struct  </td>
<td class="memItemRight" data-valign="bottom">DBusSignatureIter</td>
</tr>
<tr class="memdesc:">
<td class="mdescLeft"> </td>
<td class="mdescRight">DBusSignatureIter struct; contains no public fields. More...<br />
</td>
</tr>
<tr class="separator:">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

<table class="memberdecls">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="heading">
<td colspan="2"><h2 id="functions" class="groupheader"> Functions</h2></td>
</tr>
<tr id="r_gaba53b1756fe7f665d0657cc50253e3c8" class="memitem:gaba53b1756fe7f665d0657cc50253e3c8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_iter_init (DBusSignatureIter *iter, const char *signature)</td>
</tr>
<tr class="memdesc:gaba53b1756fe7f665d0657cc50253e3c8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initializes a DBusSignatureIter for reading a type signature.<br />
</td>
</tr>
<tr class="separator:gaba53b1756fe7f665d0657cc50253e3c8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac4761ce10d60d7581cfe98beb6a9c57c" class="memitem:gac4761ce10d60d7581cfe98beb6a9c57c">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_iter_get_current_type (const DBusSignatureIter *iter)</td>
</tr>
<tr class="memdesc:gac4761ce10d60d7581cfe98beb6a9c57c">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the current type pointed to by the iterator.<br />
</td>
</tr>
<tr class="separator:gac4761ce10d60d7581cfe98beb6a9c57c">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga898bbc14392cbedc087ce0be68d35c98" class="memitem:ga898bbc14392cbedc087ce0be68d35c98">
<td class="memItemLeft" style="text-align: right;" data-valign="top">char * </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_iter_get_signature (const DBusSignatureIter *iter)</td>
</tr>
<tr class="memdesc:ga898bbc14392cbedc087ce0be68d35c98">
<td class="mdescLeft"> </td>
<td class="mdescRight">Returns the signature of the single complete type starting at the given iterator.<br />
</td>
</tr>
<tr class="separator:ga898bbc14392cbedc087ce0be68d35c98">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaebb26dbc79dae5e11629f38b2c8277fd" class="memitem:gaebb26dbc79dae5e11629f38b2c8277fd">
<td class="memItemLeft" style="text-align: right;" data-valign="top">int </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_iter_get_element_type (const DBusSignatureIter *iter)</td>
</tr>
<tr class="memdesc:gaebb26dbc79dae5e11629f38b2c8277fd">
<td class="mdescLeft"> </td>
<td class="mdescRight">Convenience function for returning the element type of an array; This function allows you to avoid initializing a sub-iterator and getting its current type.<br />
</td>
</tr>
<tr class="separator:gaebb26dbc79dae5e11629f38b2c8277fd">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga90e48ef4b86180ba033727107b03bd29" class="memitem:ga90e48ef4b86180ba033727107b03bd29">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_iter_next (DBusSignatureIter *iter)</td>
</tr>
<tr class="memdesc:ga90e48ef4b86180ba033727107b03bd29">
<td class="mdescLeft"> </td>
<td class="mdescRight">Skip to the next value on this "level".<br />
</td>
</tr>
<tr class="separator:ga90e48ef4b86180ba033727107b03bd29">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0bd324faaf2dad5d075de3ff6c9b6796" class="memitem:ga0bd324faaf2dad5d075de3ff6c9b6796">
<td class="memItemLeft" style="text-align: right;" data-valign="top">void </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_iter_recurse (const DBusSignatureIter *iter, DBusSignatureIter *subiter)</td>
</tr>
<tr class="memdesc:ga0bd324faaf2dad5d075de3ff6c9b6796">
<td class="mdescLeft"> </td>
<td class="mdescRight">Initialize a new iterator pointing to the first type in the current container.<br />
</td>
</tr>
<tr class="separator:ga0bd324faaf2dad5d075de3ff6c9b6796">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga0f4b81be4f6193c7d8da0ee214772e02" class="memitem:ga0f4b81be4f6193c7d8da0ee214772e02">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_validate (const char *signature, DBusError *error)</td>
</tr>
<tr class="memdesc:ga0f4b81be4f6193c7d8da0ee214772e02">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check a type signature for validity.<br />
</td>
</tr>
<tr class="separator:ga0f4b81be4f6193c7d8da0ee214772e02">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gac375412dd15a7412967a927d17b6f3d8" class="memitem:gac375412dd15a7412967a927d17b6f3d8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_signature_validate_single (const char *signature, DBusError *error)</td>
</tr>
<tr class="memdesc:gac375412dd15a7412967a927d17b6f3d8">
<td class="mdescLeft"> </td>
<td class="mdescRight">Check that a type signature is both valid and contains exactly one complete type.<br />
</td>
</tr>
<tr class="separator:gac375412dd15a7412967a927d17b6f3d8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_gaa0c4c8aa34fa266daa55bd37bdad39b8" class="memitem:gaa0c4c8aa34fa266daa55bd37bdad39b8">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_type_is_container (int typecode)</td>
</tr>
<tr class="memdesc:gaa0c4c8aa34fa266daa55bd37bdad39b8">
<td class="mdescLeft"> </td>
<td class="mdescRight">A "container type" can contain basic types, or nested container types.<br />
</td>
</tr>
<tr class="separator:gaa0c4c8aa34fa266daa55bd37bdad39b8">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2d8afef7d754cf15d6b9733f00654c0e" class="memitem:ga2d8afef7d754cf15d6b9733f00654c0e">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_type_is_basic (int typecode)</td>
</tr>
<tr class="memdesc:ga2d8afef7d754cf15d6b9733f00654c0e">
<td class="mdescLeft"> </td>
<td class="mdescRight">A "basic type" is a somewhat arbitrary concept, but the intent is to include those types that are fully-specified by a single typecode, with no additional type information or nested values.<br />
</td>
</tr>
<tr class="separator:ga2d8afef7d754cf15d6b9733f00654c0e">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga2f89962cbd33e4ad843824157bae2093" class="memitem:ga2f89962cbd33e4ad843824157bae2093">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_type_is_fixed (int typecode)</td>
</tr>
<tr class="memdesc:ga2f89962cbd33e4ad843824157bae2093">
<td class="mdescLeft"> </td>
<td class="mdescRight">Tells you whether values of this type can change length if you set them to some other value.<br />
</td>
</tr>
<tr class="separator:ga2f89962cbd33e4ad843824157bae2093">
<td colspan="2" class="memSeparator"> </td>
</tr>
<tr id="r_ga7093ae3b35eb073dab939dae69b8c689" class="memitem:ga7093ae3b35eb073dab939dae69b8c689">
<td class="memItemLeft" style="text-align: right;" data-valign="top">dbus_bool_t </td>
<td class="memItemRight" data-valign="bottom">dbus_type_is_valid (int typecode)</td>
</tr>
<tr class="memdesc:ga7093ae3b35eb073dab939dae69b8c689">
<td class="mdescLeft"> </td>
<td class="mdescRight">Return TRUE if the argument is a valid typecode.<br />
</td>
</tr>
<tr class="separator:ga7093ae3b35eb073dab939dae69b8c689">
<td colspan="2" class="memSeparator"> </td>
</tr>
</tbody>
</table>

## Detailed Description

Parsing D-Bus type signatures.

## Function Documentation

## ◆ dbus_signature_iter_get_current_type()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT int dbus_signature_iter_get_current_type | ( | const DBusSignatureIter \*  | *iter* | ) |  |

Returns the current type pointed to by the iterator.

If the iterator is pointing at a type code such as 's', then it will be returned directly.

However, when the parser encounters a container type start character such as '(' for a structure, the corresponding type for the container will be returned, e.g. DBUS_TYPE_STRUCT, not '('. In this case, you should initialize a sub-iterator with dbus_signature_iter_recurse() to parse the container type.

Parameters  
|      |                        |
|------|------------------------|
| iter | pointer to an iterator |

<!-- -->

Returns  
current type (e.g. DBUS_TYPE_STRING, DBUS_TYPE_ARRAY)

Definition at line 97 of file dbus-signature.c.

References \_dbus_first_type_in_signature_c_str(), and DBusSignatureRealIter::pos.

Referenced by dbus_signature_iter_get_element_type(), dbus_signature_iter_recurse(), and dbus_signature_validate_single().

## ◆ dbus_signature_iter_get_element_type()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT int dbus_signature_iter_get_element_type | ( | const DBusSignatureIter \*  | *iter* | ) |  |

Convenience function for returning the element type of an array; This function allows you to avoid initializing a sub-iterator and getting its current type.

Undefined behavior results if you invoke this function when the current type of the iterator is not DBUS_TYPE_ARRAY.

Parameters  
|      |                        |
|------|------------------------|
| iter | pointer to an iterator |

<!-- -->

Returns  
current array element type

Definition at line 151 of file dbus-signature.c.

References \_dbus_first_type_in_signature_c_str(), dbus_signature_iter_get_current_type(), DBUS_TYPE_ARRAY, DBUS_TYPE_INVALID, and DBusSignatureRealIter::pos.

## ◆ dbus_signature_iter_get_signature()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT char \* dbus_signature_iter_get_signature | ( | const DBusSignatureIter \*  | *iter* | ) |  |

Returns the signature of the single complete type starting at the given iterator.

For example, if the iterator is pointing at the start of "(ii)ii" (which is "a struct of two ints, followed by an int, followed by an int"), then "(ii)" would be returned. If the iterator is pointing at one of the "i" then just that "i" would be returned.

Parameters  
|      |                        |
|------|------------------------|
| iter | pointer to an iterator |

<!-- -->

Returns  
current signature; or NULL if no memory. Should be freed with dbus_free()

Definition at line 117 of file dbus-signature.c.

References \_dbus_string_append_len(), \_dbus_string_free(), \_dbus_string_init(), \_dbus_string_steal_data(), \_dbus_type_signature_next(), NULL, and DBusSignatureRealIter::pos.

## ◆ dbus_signature_iter_init()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_signature_iter_init | ( | DBusSignatureIter \*  | *iter*, |
|  |  | const char \*  | *signature*  |
|  | ) |  |  |

Initializes a DBusSignatureIter for reading a type signature.

This function is not safe to use on invalid signatures; be sure to validate potentially invalid signatures with dbus_signature_validate before using this function.

Parameters  
|           |                                      |
|-----------|--------------------------------------|
| iter      | pointer to an iterator to initialize |
| signature | the type signature                   |

Definition at line 72 of file dbus-signature.c.

References FALSE, DBusSignatureRealIter::finished, DBusSignatureRealIter::in_array, and DBusSignatureRealIter::pos.

Referenced by dbus_signature_validate_single().

## ◆ dbus_signature_iter_next()

|  |  |  |  |  |  |
|----|----|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_signature_iter_next | ( | DBusSignatureIter \*  | *iter* | ) |  |

Skip to the next value on this "level".

e.g. the next field in a struct, the next value in an array. Returns FALSE at the end of the current container.

Parameters  
|      |              |
|------|--------------|
| iter | the iterator |

<!-- -->

Returns  
FALSE if nothing more to read at or below this level

Definition at line 169 of file dbus-signature.c.

References \_dbus_type_signature_next(), DBUS_DICT_ENTRY_END_CHAR, DBUS_STRUCT_END_CHAR, DBUS_TYPE_INVALID, FALSE, DBusSignatureRealIter::finished, DBusSignatureRealIter::in_array, DBusSignatureRealIter::pos, and TRUE.

Referenced by dbus_signature_validate_single().

## ◆ dbus_signature_iter_recurse()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT void dbus_signature_iter_recurse | ( | const DBusSignatureIter \*  | *iter*, |
|  |  | DBusSignatureIter \*  | *subiter*  |
|  | ) |  |  |

Initialize a new iterator pointing to the first type in the current container.

The results are undefined when calling this if the current type is a non-container (i.e. if dbus_type_is_container() returns FALSE for the result of dbus_signature_iter_get_current_type()).

Parameters  
|         |                                                       |
|---------|-------------------------------------------------------|
| iter    | the current interator                                 |
| subiter | an iterator to initialize pointing to the first child |

Definition at line 212 of file dbus-signature.c.

References dbus_signature_iter_get_current_type(), DBUS_TYPE_ARRAY, dbus_type_is_container(), FALSE, DBusSignatureRealIter::in_array, DBusSignatureRealIter::pos, and TRUE.

## ◆ dbus_signature_validate()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_signature_validate | ( | const char \*  | *signature*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Check a type signature for validity.

Remember that NULL can always be passed instead of a DBusError\*, if you don't care about having an error name and message.

Parameters  
|           |                                      |
|-----------|--------------------------------------|
| signature | a potentially invalid type signature |
| error     | error return                         |

<!-- -->

Returns  
TRUE if signature is valid or FALSE if an error is set

Definition at line 238 of file dbus-signature.c.

References \_dbus_string_get_length(), \_dbus_string_init_const(), \_dbus_validate_signature_with_reason(), DBUS_ERROR_INVALID_SIGNATURE, dbus_set_error(), DBUS_VALID, FALSE, and TRUE.

Referenced by dbus_signature_validate_single().

## ◆ dbus_signature_validate_single()

|  |  |  |  |
|----|----|----|----|
| DBUS_EXPORT dbus_bool_t dbus_signature_validate_single | ( | const char \*  | *signature*, |
|  |  | DBusError \*  | *error*  |
|  | ) |  |  |

Check that a type signature is both valid and contains exactly one complete type.

"One complete type" means a single basic type, array, struct, or dictionary, though the struct or array may be arbitrarily recursive and complex. More than one complete type would mean for example "ii" or two integers in sequence.

Parameters  
|           |                                      |
|-----------|--------------------------------------|
| signature | a potentially invalid type signature |
| error     | error return                         |

<!-- -->

Returns  
TRUE if signature is valid and has exactly one complete type

Definition at line 270 of file dbus-signature.c.

References DBUS_ERROR_INVALID_SIGNATURE, dbus_set_error(), dbus_signature_iter_get_current_type(), dbus_signature_iter_init(), dbus_signature_iter_next(), dbus_signature_validate(), DBUS_TYPE_INVALID, FALSE, and TRUE.

## ◆ dbus_type_is_basic()

|                                            |     |      |            |     |     |
|--------------------------------------------|-----|------|------------|-----|-----|
| DBUS_EXPORT dbus_bool_t dbus_type_is_basic | (   | int  | *typecode* | )   |     |

A "basic type" is a somewhat arbitrary concept, but the intent is to include those types that are fully-specified by a single typecode, with no additional type information or nested values.

So all numbers and strings are basic types and structs, arrays, and variants are not basic types. DBUS_TYPE_INVALID is not a basic type.

It is an error to pass an invalid type-code, other than DBUS_TYPE_INVALID, to this function. The valid type-codes are defined by dbus-protocol.h and can be checked with dbus_type_is_valid().

Parameters  
|          |                                               |
|----------|-----------------------------------------------|
| typecode | either a valid type-code or DBUS_TYPE_INVALID |

<!-- -->

Returns  
TRUE if type is basic

Definition at line 324 of file dbus-signature.c.

References DBUS_TYPE_INVALID, dbus_type_is_valid(), and FALSE.

Referenced by \_dbus_marshal_read_basic(), \_dbus_marshal_write_basic(), \_dbus_message_iter_get_args_valist(), \_dbus_type_reader_set_basic(), \_dbus_validate_signature_with_reason(), \_dbus_variant_read(), dbus_message_append_args_valist(), and dbus_message_iter_append_basic().

## ◆ dbus_type_is_container()

|                                                |     |      |            |     |     |
|------------------------------------------------|-----|------|------------|-----|-----|
| DBUS_EXPORT dbus_bool_t dbus_type_is_container | (   | int  | *typecode* | )   |     |

A "container type" can contain basic types, or nested container types.

DBUS_TYPE_INVALID is not a container type.

It is an error to pass an invalid type-code, other than DBUS_TYPE_INVALID, to this function. The valid type-codes are defined by dbus-protocol.h and can be checked with dbus_type_is_valid().

Parameters  
|          |                                               |
|----------|-----------------------------------------------|
| typecode | either a valid type-code or DBUS_TYPE_INVALID |

<!-- -->

Returns  
TRUE if type is a container

Definition at line 300 of file dbus-signature.c.

References DBUS_TYPE_INVALID, dbus_type_is_valid(), and FALSE.

Referenced by dbus_message_iter_open_container(), and dbus_signature_iter_recurse().

## ◆ dbus_type_is_fixed()

|                                            |     |      |            |     |     |
|--------------------------------------------|-----|------|------------|-----|-----|
| DBUS_EXPORT dbus_bool_t dbus_type_is_fixed | (   | int  | *typecode* | )   |     |

Tells you whether values of this type can change length if you set them to some other value.

For this purpose, you assume that the first byte of the old and new value would be in the same location, so alignment padding is not a factor.

This function is useful to determine whether dbus_message_iter_get_fixed_array() may be used.

Some structs are fixed-size (if they contain only fixed-size types) but struct is not considered a fixed type for purposes of this function.

It is an error to pass an invalid type-code, other than DBUS_TYPE_INVALID, to this function. The valid type-codes are defined by dbus-protocol.h and can be checked with dbus_type_is_valid().

Parameters  
|          |                                               |
|----------|-----------------------------------------------|
| typecode | either a valid type-code or DBUS_TYPE_INVALID |

<!-- -->

Returns  
FALSE if the type can occupy different lengths

Definition at line 355 of file dbus-signature.c.

References DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, DBUS_TYPE_INVALID, dbus_type_is_valid(), DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, FALSE, and TRUE.

Referenced by \_dbus_marshal_write_fixed_multi(), \_dbus_message_iter_get_args_valist(), \_dbus_type_reader_read_fixed_multi(), \_dbus_type_reader_set_basic(), \_dbus_type_writer_write_fixed_multi(), dbus_message_append_args_valist(), dbus_message_iter_append_fixed_array(), dbus_message_iter_get_element_count(), and dbus_message_iter_get_fixed_array().

## ◆ dbus_type_is_valid()

|                                            |     |      |            |     |     |
|--------------------------------------------|-----|------|------------|-----|-----|
| DBUS_EXPORT dbus_bool_t dbus_type_is_valid | (   | int  | *typecode* | )   |     |

Return TRUE if the argument is a valid typecode.

DBUS_TYPE_INVALID surprisingly enough is not considered valid, and random unknown bytes aren't either. This function is safe with untrusted data.

Parameters  
|          |                       |
|----------|-----------------------|
| typecode | a potential type-code |

<!-- -->

Returns  
TRUE if valid

Definition at line 389 of file dbus-signature.c.

References DBUS_TYPE_ARRAY, DBUS_TYPE_BOOLEAN, DBUS_TYPE_BYTE, DBUS_TYPE_DICT_ENTRY, DBUS_TYPE_DOUBLE, DBUS_TYPE_INT16, DBUS_TYPE_INT32, DBUS_TYPE_INT64, DBUS_TYPE_OBJECT_PATH, DBUS_TYPE_SIGNATURE, DBUS_TYPE_STRING, DBUS_TYPE_STRUCT, DBUS_TYPE_UINT16, DBUS_TYPE_UINT32, DBUS_TYPE_UINT64, DBUS_TYPE_UNIX_FD, DBUS_TYPE_VARIANT, FALSE, and TRUE.

Referenced by \_dbus_validate_signature_with_reason(), dbus_connection_can_send_type(), dbus_type_is_basic(), dbus_type_is_container(), and dbus_type_is_fixed().
