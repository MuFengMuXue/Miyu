# dbus.types module

*class *dbus.types.Array(*\[iterable\]\[, signature\]\[, variant_level\]*)  
Bases: `list`

An array of similar items, implemented as a subtype of list.

As currently implemented, an Array behaves just like a list, but with the addition of a `signature` property set by the constructor; conversion of its items to D-Bus types is only done when it’s sent in a Message. This might change in future so validation is done earlier.

`variant_level` must be non-negative; the default is 0.

`signature` is the D-Bus signature string for a single element of the array, or None. If not None it must represent a single complete type, the type of a single array item; the signature of the whole Array may be obtained by prepending `a` to the given signature.

If None (the default), when the Array is sent over D-Bus, the item signature will be guessed from the first element.

append(*object*, */*)  
Append object to the end of the list.

clear()  
Remove all items from list.

copy()  
Return a shallow copy of the list.

count(*value*, */*)  
Return number of occurrences of value.

extend(*iterable*, */*)  
Extend list by appending elements from the iterable.

index(*value*, *start=0*, *stop=9223372036854775807*, */*)  
Return first index of value.

Raises ValueError if the value is not present.

insert(*index*, *object*, */*)  
Insert object before index.

pop(*index=- 1*, */*)  
Remove and return item at index (default last).

Raises IndexError if list is empty or index is out of range.

remove(*value*, */*)  
Remove first occurrence of value.

Raises ValueError if the value is not present.

reverse()  
Reverse *IN PLACE*.

signature  
The D-Bus signature of each element of this Array (a Signature instance)

sort(*\**, *key=None*, *reverse=False*)  
Sort the list in ascending order and return None.

The sort is in-place (i.e. the list itself is modified) and stable (i.e. the order of two equal elements is maintained).

If a key function is given, apply it once to each list item and sort them, ascending or descending, according to their function values.

The reverse flag can be set to sort in descending order.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an array, this is represented in Python by an Array with variant_level==2.

<!-- -->

*class *dbus.types.Boolean(*value: bool*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A boolean, represented as a subtype of `int` (not `bool`, because `bool` cannot be subclassed).

`value` is converted to 0 or 1 as if by `int(bool(value))`.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a boolean, this is represented in Python by a Boolean with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.Byte(*integer or bytes of length 1*\[, *variant_level*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned byte: a subtype of int, with range restricted to \[0, 255\].

A Byte b may be converted to a `str` of length 1 via `str(b)`` ``==`` ``chr(b)` (Python 2) or to a `bytes` of length 1 via `bytes([b])` (Python 3).

Most of the time you don’t want to use this class - it mainly exists for symmetry with the other D-Bus types. See dbus.ByteArray for a better way to handle arrays of Byte.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a byte, this is represented in Python by a Byte with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.ByteArray(*str*)  
Bases: `_dbus_bindings._BytesBase`

ByteArray is a subtype of `bytes` (an alias for `str` in Python 2 but a distinct type in Python 3) which can be used when you want an efficient immutable representation of a D-Bus byte array (signature `ay`).

By default, when byte arrays are converted from D-Bus to Python, they come out as a dbus.Array of dbus.Byte. This is just for symmetry with the other D-Bus types - in practice, what you usually want is the byte array represented as a string, using this class. To get this, pass the `byte_arrays=True` keyword argument to any of these methods:

- any D-Bus method proxy, or `connect_to_signal`, on the objects returned by Bus.get_object

- any D-Bus method on a dbus.Interface

- dbus.Interface.connect_to_signal

- Bus.add_signal_receiver

Import via:

    from dbus import ByteArray

Constructor:

    ByteArray(str)

capitalize() → copy of B  
Return a copy of B with only its first character capitalized (ASCII) and the rest lower-cased.

center(*width*, *fillchar=b' '*, */*)  
Return a centered string of length width.

Padding is done using the specified fill character.

count(*sub*\[, *start*\[, *end*\]\]) → int  
Return the number of non-overlapping occurrences of subsection sub in bytes B\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

decode(*encoding='utf-8'*, *errors='strict'*)  
Decode the bytes using the codec registered for encoding.

encoding  
The encoding with which to decode the bytes.

errors  
The error handling scheme to use for the handling of decoding errors. The default is ‘strict’ meaning that decoding errors raise a UnicodeDecodeError. Other possible values are ‘ignore’ and ‘replace’ as well as any other name registered with codecs.register_error that can handle UnicodeDecodeErrors.

endswith(*suffix*\[, *start*\[, *end*\]\]) → bool  
Return True if B ends with the specified suffix, False otherwise. With optional start, test B beginning at that position. With optional end, stop comparing B at that position. suffix can also be a tuple of bytes to try.

expandtabs(*tabsize=8*)  
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in B where subsection sub is found, such that sub is contained within B\[start,end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

fromhex()  
Create a bytes object from a string of hexadecimal numbers.

Spaces between two numbers are accepted. Example: bytes.fromhex(‘B9 01EF’) -\> b’\xb9\x01\xef’.

hex()  
Create a string of hexadecimal numbers from a bytes object.

> sep  
> An optional single character or byte to separate hex bytes.
>
> bytes_per_sep  
> How many bytes between separators. Positive values count from the right, negative values count from the left.

Example: \>\>\> value = b’xb9x01xef’ \>\>\> value.hex() ‘b901ef’ \>\>\> value.hex(‘:’) ‘b9:01:ef’ \>\>\> value.hex(‘:’, 2) ‘b9:01ef’ \>\>\> value.hex(‘:’, -2) ‘b901:ef’

index(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in B where subsection sub is found, such that sub is contained within B\[start,end\]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the subsection is not found.

isalnum() → bool  
Return True if all characters in B are alphanumeric and there is at least one character in B, False otherwise.

isalpha() → bool  
Return True if all characters in B are alphabetic and there is at least one character in B, False otherwise.

isascii() → bool  
Return True if B is empty or all characters in B are ASCII, False otherwise.

isdigit() → bool  
Return True if all characters in B are digits and there is at least one character in B, False otherwise.

islower() → bool  
Return True if all cased characters in B are lowercase and there is at least one cased character in B, False otherwise.

isspace() → bool  
Return True if all characters in B are whitespace and there is at least one character in B, False otherwise.

istitle() → bool  
Return True if B is a titlecased string and there is at least one character in B, i.e. uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.

isupper() → bool  
Return True if all cased characters in B are uppercase and there is at least one cased character in B, False otherwise.

join(*iterable_of_bytes*, */*)  
Concatenate any number of bytes objects.

The bytes whose method is called is inserted in between each pair.

The result is returned as a new bytes object.

Example: b’.’.join(\[b’ab’, b’pq’, b’rs’\]) -\> b’ab.pq.rs’.

ljust(*width*, *fillchar=b' '*, */*)  
Return a left-justified string of length width.

Padding is done using the specified fill character.

lower() → copy of B  
Return a copy of B with all ASCII characters converted to lowercase.

lstrip(*bytes=None*, */*)  
Strip leading bytes contained in the argument.

If the argument is omitted or None, strip leading ASCII whitespace.

*static *maketrans(*frm*, *to*, */*)  
Return a translation table useable for the bytes or bytearray translate method.

The returned table will be one where each byte in frm is mapped to the byte at the same position in to.

The bytes objects frm and to must be of the same length.

partition(*sep*, */*)  
Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original bytes object and two empty bytes objects.

removeprefix(*prefix*, */*)  
Return a bytes object with the given prefix string removed if present.

If the bytes starts with the prefix string, return bytes\[len(prefix):\]. Otherwise, return a copy of the original bytes.

removesuffix(*suffix*, */*)  
Return a bytes object with the given suffix string removed if present.

If the bytes ends with the suffix string and that suffix is not empty, return bytes\[:-len(prefix)\]. Otherwise, return a copy of the original bytes.

replace(*old*, *new*, *count=- 1*, */*)  
Return a copy with all occurrences of substring old replaced by new.

> count  
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

rfind(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in B where subsection sub is found, such that sub is contained within B\[start,end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in B where subsection sub is found, such that sub is contained within B\[start,end\]. Optional arguments start and end are interpreted as in slice notation.

Raise ValueError when the subsection is not found.

rjust(*width*, *fillchar=b' '*, */*)  
Return a right-justified string of length width.

Padding is done using the specified fill character.

rpartition(*sep*, */*)  
Partition the bytes into three parts using the given separator.

This will search for the separator sep in the bytes, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty bytes objects and the original bytes object.

rsplit(*sep=None*, *maxsplit=- 1*)  
Return a list of the sections in the bytes, using sep as the delimiter.

> sep  
> The delimiter according which to split the bytes. None (the default value) means split on ASCII whitespace characters (space, tab, return, newline, formfeed, vertical tab).
>
> maxsplit  
> Maximum number of splits to do. -1 (the default value) means no limit.

Splitting is done starting at the end of the bytes and working to the front.

rstrip(*bytes=None*, */*)  
Strip trailing bytes contained in the argument.

If the argument is omitted or None, strip trailing ASCII whitespace.

split(*sep=None*, *maxsplit=- 1*)  
Return a list of the sections in the bytes, using sep as the delimiter.

sep  
The delimiter according which to split the bytes. None (the default value) means split on ASCII whitespace characters (space, tab, return, newline, formfeed, vertical tab).

maxsplit  
Maximum number of splits to do. -1 (the default value) means no limit.

splitlines(*keepends=False*)  
Return a list of the lines in the bytes, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

startswith(*prefix*\[, *start*\[, *end*\]\]) → bool  
Return True if B starts with the specified prefix, False otherwise. With optional start, test B beginning at that position. With optional end, stop comparing B at that position. prefix can also be a tuple of bytes to try.

strip(*bytes=None*, */*)  
Strip leading and trailing bytes contained in the argument.

If the argument is omitted or None, strip leading and trailing ASCII whitespace.

swapcase() → copy of B  
Return a copy of B with uppercase ASCII characters converted to lowercase ASCII and vice versa.

title() → copy of B  
Return a titlecased version of B, i.e. ASCII words start with uppercase characters, all remaining cased characters have lowercase.

translate(*table*, */*, *delete=b''*)  
Return a copy with each character mapped by the given translation table.

> table  
> Translation table, which must be a bytes object of length 256.

All characters occurring in the optional argument delete are removed. The remaining characters are mapped through the given translation table.

upper() → copy of B  
Return a copy of B with all ASCII characters converted to uppercase.

zfill(*width*, */*)  
Pad a numeric string with zeros on the left, to fill a field of the given width.

The original string is never truncated.

<!-- -->

*class *dbus.types.Dictionary(*mapping_or_iterable=()*, *signature=None*, *variant_level=0*)  
Bases: `dict`

An mapping whose keys are similar and whose values are similar, implemented as a subtype of dict.

As currently implemented, a Dictionary behaves just like a dict, but with the addition of a `signature` property set by the constructor; conversion of its items to D-Bus types is only done when it’s sent in a Message. This may change in future so validation is done earlier.

`variant_level` must be non-negative; the default is 0.

`signature` is either a string or None. If a string, it must consist of exactly two complete type signatures, representing the ‘key’ type (which must be a primitive type, i.e. one of “bdginoqstuxy”) and the ‘value’ type. The signature of the whole Dictionary will be `a{xx}` where `xx` is replaced by the given signature.

If it is None (the default), when the Dictionary is sent over D-Bus, the key and value signatures will be guessed from an arbitrary element of the Dictionary.

clear() → None.  Remove all items from D.  

copy() → a shallow copy of D  

fromkeys(*value=None*, */*)  
Create a new dictionary with keys from iterable and values set to value.

get(*key*, *default=None*, */*)  
Return the value for key if key is in the dictionary, else default.

items() → a set-like object providing a view on D's items  

keys() → a set-like object providing a view on D's keys  

pop(*k*\[, *d*\]) → v, remove specified key and return the corresponding value.  
If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem()  
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault(*key*, *default=None*, */*)  
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

signature  
The D-Bus signature of each key in this Dictionary, followed by that of each value in this Dictionary, as a Signature instance.

update(\[*E*, \]*\*\*F*) → None.  Update D from dict/iterable E and F.  
If E is present and has a .keys() method, then does: for k in E: D\[k\] = E\[k\] If E is present and lacks a .keys() method, then does: for k, v in E: D\[k\] = v In either case, this is followed by: for k in F: D\[k\] = F\[k\]

values() → an object providing a view on D's values  

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a dictionary, this is represented in Python by a Dictionary with variant_level==2.

<!-- -->

*class *dbus.types.Double(*x=0*, */*)  
Bases: `_dbus_bindings._FloatBase`

A double-precision floating point number (a subtype of float).

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original float and with a positive denominator.

Raise OverflowError on infinities and a ValueError on NaNs.

    >>> (10.0).as_integer_ratio()
    (10, 1)
    >>> (0.0).as_integer_ratio()
    (0, 1)
    >>> (-.25).as_integer_ratio()
    (-1, 4)

conjugate()  
Return self, the complex conjugate of any float.

fromhex()  
Create a floating-point number from a hexadecimal string.

    >>> float.fromhex('0x1.ffffp10')
    2047.984375
    >>> float.fromhex('-0x1p-1074')
    -5e-324

hex()  
Return a hexadecimal representation of a floating-point number.

    >>> (-0.1).hex()
    '-0x1.999999999999ap-4'
    >>> 3.14159.hex()
    '0x1.921f9f01b866ep+1'

imag  
the imaginary part of a complex number

is_integer()  
Return True if the float is an integer.

real  
the real part of a complex number

variant_level  
The number of nested variants wrapping the real data. 0 if not in a variant.

<!-- -->

*class *dbus.types.Int16(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A signed 16-bit integer between -0x8000 and +0x7FFF, represented as a subtype of int.

value must be within the allowed range, or OverflowError will be raised.

> variant_level must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an int16, this is represented in Python by an Int16 with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.Int32(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A signed 32-bit integer between -0x8000 0000 and +0x7FFF FFFF, represented as a subtype of `int`.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an int32, this is represented in Python by an Int32 with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.Int64(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

A signed 64-bit integer between -0x8000 0000 0000 0000 and +0x7FFF FFFF FFFF FFFF, represented as a subtype of `long` in Python 2 or `int` in Python 3.

Note that this may be changed in future to be a subtype of int on 64-bit platforms; applications should not rely on either behaviour.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an int64, this is represented in Python by an Int64 with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.ObjectPath(*path: str*\[, *variant_level: int=0*\])  
Bases: `_dbus_bindings._StrBase`

A D-Bus object path, such as `/com/example/MyApp/Documents/abc`.

ObjectPath is a subtype of `str`, and object-paths behave like strings.

path must be an ASCII string following the syntax of object paths. variant_level must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an object path, this is represented in Python by an ObjectPath with variant_level==2.

capitalize()  
Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

casefold()  
Return a version of the string suitable for caseless comparisons.

center(*width*, *fillchar=' '*, */*)  
Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(*sub*\[, *start*\[, *end*\]\]) → int  
Return the number of non-overlapping occurrences of substring sub in string S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

encode(*encoding='utf-8'*, *errors='strict'*)  
Encode the string using the codec registered for encoding.

encoding  
The encoding in which to encode the string.

errors  
The error handling scheme to use for encoding errors. The default is ‘strict’ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and ‘xmlcharrefreplace’ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

endswith(*suffix*\[, *start*\[, *end*\]\]) → bool  
Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

expandtabs(*tabsize=8*)  
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format(*\*args*, *\*\*kwargs*) → str  
Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (‘{’ and ‘}’).

format_map(*mapping*) → str  
Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (‘{’ and ‘}’).

index(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()  
Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

isalpha()  
Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

isascii()  
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

isdecimal()  
Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

isdigit()  
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

isidentifier()  
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as “def” or “class”.

islower()  
Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

isnumeric()  
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

isprintable()  
Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

isspace()  
Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

istitle()  
Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

isupper()  
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

join(*iterable*, */*)  
Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: ‘.’.join(\[‘ab’, ‘pq’, ‘rs’\]) -\> ‘ab.pq.rs’

ljust(*width*, *fillchar=' '*, */*)  
Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()  
Return a copy of the string converted to lowercase.

lstrip(*chars=None*, */*)  
Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

*static *maketrans()  
Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

partition(*sep*, */*)  
Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

removeprefix(*prefix*, */*)  
Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string\[len(prefix):\]. Otherwise, return a copy of the original string.

removesuffix(*suffix*, */*)  
Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string\[:-len(suffix)\]. Otherwise, return a copy of the original string.

replace(*old*, *new*, *count=- 1*, */*)  
Return a copy with all occurrences of substring old replaced by new.

> count  
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

rfind(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(*width*, *fillchar=' '*, */*)  
Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition(*sep*, */*)  
Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

rsplit(*sep=None*, *maxsplit=- 1*)  
Return a list of the substrings in the string, using sep as the separator string.

> sep  
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.
>
> maxsplit  
> Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip(*chars=None*, */*)  
Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split(*sep=None*, *maxsplit=- 1*)  
Return a list of the substrings in the string, using sep as the separator string.

> sep  
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.
>
> maxsplit  
> Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

splitlines(*keepends=False*)  
Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

startswith(*prefix*\[, *start*\[, *end*\]\]) → bool  
Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

strip(*chars=None*, */*)  
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()  
Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()  
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

translate(*table*, */*)  
Replace each character in the string using the given translation table.

> table  
> Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via \_\_getitem\_\_, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

upper()  
Return a copy of the string converted to uppercase.

zfill(*width*, */*)  
Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

<!-- -->

*class *dbus.types.Signature(*value: str or unicode*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._StrBase`

A string subclass whose values are restricted to valid D-Bus signatures. When iterated over, instead of individual characters it produces Signature instances representing single complete types.

`value` must be a valid D-Bus signature (zero or more single complete types).

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a signature, this is represented in Python by a Signature with variant_level==2.

capitalize()  
Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

casefold()  
Return a version of the string suitable for caseless comparisons.

center(*width*, *fillchar=' '*, */*)  
Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(*sub*\[, *start*\[, *end*\]\]) → int  
Return the number of non-overlapping occurrences of substring sub in string S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

encode(*encoding='utf-8'*, *errors='strict'*)  
Encode the string using the codec registered for encoding.

encoding  
The encoding in which to encode the string.

errors  
The error handling scheme to use for encoding errors. The default is ‘strict’ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and ‘xmlcharrefreplace’ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

endswith(*suffix*\[, *start*\[, *end*\]\]) → bool  
Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

expandtabs(*tabsize=8*)  
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format(*\*args*, *\*\*kwargs*) → str  
Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (‘{’ and ‘}’).

format_map(*mapping*) → str  
Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (‘{’ and ‘}’).

index(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()  
Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

isalpha()  
Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

isascii()  
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

isdecimal()  
Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

isdigit()  
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

isidentifier()  
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as “def” or “class”.

islower()  
Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

isnumeric()  
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

isprintable()  
Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

isspace()  
Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

istitle()  
Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

isupper()  
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

join(*iterable*, */*)  
Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: ‘.’.join(\[‘ab’, ‘pq’, ‘rs’\]) -\> ‘ab.pq.rs’

ljust(*width*, *fillchar=' '*, */*)  
Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()  
Return a copy of the string converted to lowercase.

lstrip(*chars=None*, */*)  
Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

*static *maketrans()  
Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

partition(*sep*, */*)  
Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

removeprefix(*prefix*, */*)  
Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string\[len(prefix):\]. Otherwise, return a copy of the original string.

removesuffix(*suffix*, */*)  
Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string\[:-len(suffix)\]. Otherwise, return a copy of the original string.

replace(*old*, *new*, *count=- 1*, */*)  
Return a copy with all occurrences of substring old replaced by new.

> count  
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

rfind(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(*width*, *fillchar=' '*, */*)  
Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition(*sep*, */*)  
Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

rsplit(*sep=None*, *maxsplit=- 1*)  
Return a list of the substrings in the string, using sep as the separator string.

> sep  
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.
>
> maxsplit  
> Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip(*chars=None*, */*)  
Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split(*sep=None*, *maxsplit=- 1*)  
Return a list of the substrings in the string, using sep as the separator string.

> sep  
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.
>
> maxsplit  
> Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

splitlines(*keepends=False*)  
Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

startswith(*prefix*\[, *start*\[, *end*\]\]) → bool  
Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

strip(*chars=None*, */*)  
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()  
Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()  
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

translate(*table*, */*)  
Replace each character in the string using the given translation table.

> table  
> Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via \_\_getitem\_\_, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

upper()  
Return a copy of the string converted to uppercase.

zfill(*width*, */*)  
Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

<!-- -->

*class *dbus.types.String(*value: str or unicode*\[, *variant_level: int*\])  
Bases: `str`

A string represented using Unicode - a subtype of `unicode` (Python 2) or `str` (Python 3).

All strings on D-Bus are required to be valid Unicode; in the “wire protocol” they’re transported as UTF-8.

By default, when strings are converted from D-Bus to Python, they come out as this class. In Python 2, if you prefer to get UTF-8 strings (as instances of a subtype of str) or you want to avoid the conversion overhead of going from UTF-8 to Python’s internal Unicode representation, see the documentation for dbus.UTF8String.

variant_level must be non-negative; the default is 0.

capitalize()  
Return a capitalized version of the string.

More specifically, make the first character have upper case and the rest lower case.

casefold()  
Return a version of the string suitable for caseless comparisons.

center(*width*, *fillchar=' '*, */*)  
Return a centered string of length width.

Padding is done using the specified fill character (default is a space).

count(*sub*\[, *start*\[, *end*\]\]) → int  
Return the number of non-overlapping occurrences of substring sub in string S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

encode(*encoding='utf-8'*, *errors='strict'*)  
Encode the string using the codec registered for encoding.

encoding  
The encoding in which to encode the string.

errors  
The error handling scheme to use for encoding errors. The default is ‘strict’ meaning that encoding errors raise a UnicodeEncodeError. Other possible values are ‘ignore’, ‘replace’ and ‘xmlcharrefreplace’ as well as any other name registered with codecs.register_error that can handle UnicodeEncodeErrors.

endswith(*suffix*\[, *start*\[, *end*\]\]) → bool  
Return True if S ends with the specified suffix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. suffix can also be a tuple of strings to try.

expandtabs(*tabsize=8*)  
Return a copy where all tab characters are expanded using spaces.

If tabsize is not given, a tab size of 8 characters is assumed.

find(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

format(*\*args*, *\*\*kwargs*) → str  
Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces (‘{’ and ‘}’).

format_map(*mapping*) → str  
Return a formatted version of S, using substitutions from mapping. The substitutions are identified by braces (‘{’ and ‘}’).

index(*sub*\[, *start*\[, *end*\]\]) → int  
Return the lowest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

isalnum()  
Return True if the string is an alpha-numeric string, False otherwise.

A string is alpha-numeric if all characters in the string are alpha-numeric and there is at least one character in the string.

isalpha()  
Return True if the string is an alphabetic string, False otherwise.

A string is alphabetic if all characters in the string are alphabetic and there is at least one character in the string.

isascii()  
Return True if all characters in the string are ASCII, False otherwise.

ASCII characters have code points in the range U+0000-U+007F. Empty string is ASCII too.

isdecimal()  
Return True if the string is a decimal string, False otherwise.

A string is a decimal string if all characters in the string are decimal and there is at least one character in the string.

isdigit()  
Return True if the string is a digit string, False otherwise.

A string is a digit string if all characters in the string are digits and there is at least one character in the string.

isidentifier()  
Return True if the string is a valid Python identifier, False otherwise.

Call keyword.iskeyword(s) to test whether string s is a reserved identifier, such as “def” or “class”.

islower()  
Return True if the string is a lowercase string, False otherwise.

A string is lowercase if all cased characters in the string are lowercase and there is at least one cased character in the string.

isnumeric()  
Return True if the string is a numeric string, False otherwise.

A string is numeric if all characters in the string are numeric and there is at least one character in the string.

isprintable()  
Return True if the string is printable, False otherwise.

A string is printable if all of its characters are considered printable in repr() or if it is empty.

isspace()  
Return True if the string is a whitespace string, False otherwise.

A string is whitespace if all characters in the string are whitespace and there is at least one character in the string.

istitle()  
Return True if the string is a title-cased string, False otherwise.

In a title-cased string, upper- and title-case characters may only follow uncased characters and lowercase characters only cased ones.

isupper()  
Return True if the string is an uppercase string, False otherwise.

A string is uppercase if all cased characters in the string are uppercase and there is at least one cased character in the string.

join(*iterable*, */*)  
Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

Example: ‘.’.join(\[‘ab’, ‘pq’, ‘rs’\]) -\> ‘ab.pq.rs’

ljust(*width*, *fillchar=' '*, */*)  
Return a left-justified string of length width.

Padding is done using the specified fill character (default is a space).

lower()  
Return a copy of the string converted to lowercase.

lstrip(*chars=None*, */*)  
Return a copy of the string with leading whitespace removed.

If chars is given and not None, remove characters in chars instead.

*static *maketrans()  
Return a translation table usable for str.translate().

If there is only one argument, it must be a dictionary mapping Unicode ordinals (integers) or characters to Unicode ordinals, strings or None. Character keys will be then converted to ordinals. If there are two arguments, they must be strings of equal length, and in the resulting dictionary, each character in x will be mapped to the character at the same position in y. If there is a third argument, it must be a string, whose characters will be mapped to None in the result.

partition(*sep*, */*)  
Partition the string into three parts using the given separator.

This will search for the separator in the string. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing the original string and two empty strings.

removeprefix(*prefix*, */*)  
Return a str with the given prefix string removed if present.

If the string starts with the prefix string, return string\[len(prefix):\]. Otherwise, return a copy of the original string.

removesuffix(*suffix*, */*)  
Return a str with the given suffix string removed if present.

If the string ends with the suffix string and that suffix is not empty, return string\[:-len(suffix)\]. Otherwise, return a copy of the original string.

replace(*old*, *new*, *count=- 1*, */*)  
Return a copy with all occurrences of substring old replaced by new.

> count  
> Maximum number of occurrences to replace. -1 (the default value) means replace all occurrences.

If the optional argument count is given, only the first count occurrences are replaced.

rfind(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Return -1 on failure.

rindex(*sub*\[, *start*\[, *end*\]\]) → int  
Return the highest index in S where substring sub is found, such that sub is contained within S\[start:end\]. Optional arguments start and end are interpreted as in slice notation.

Raises ValueError when the substring is not found.

rjust(*width*, *fillchar=' '*, */*)  
Return a right-justified string of length width.

Padding is done using the specified fill character (default is a space).

rpartition(*sep*, */*)  
Partition the string into three parts using the given separator.

This will search for the separator in the string, starting at the end. If the separator is found, returns a 3-tuple containing the part before the separator, the separator itself, and the part after it.

If the separator is not found, returns a 3-tuple containing two empty strings and the original string.

rsplit(*sep=None*, *maxsplit=- 1*)  
Return a list of the substrings in the string, using sep as the separator string.

> sep  
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.
>
> maxsplit  
> Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Splitting starts at the end of the string and works to the front.

rstrip(*chars=None*, */*)  
Return a copy of the string with trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

split(*sep=None*, *maxsplit=- 1*)  
Return a list of the substrings in the string, using sep as the separator string.

> sep  
> The separator used to split the string.
>
> When set to None (the default value), will split on any whitespace character (including \n \r \t \f and spaces) and will discard empty strings from the result.
>
> maxsplit  
> Maximum number of splits (starting from the left). -1 (the default value) means no limit.

Note, str.split() is mainly useful for data that has been intentionally delimited. With natural text that includes punctuation, consider using the regular expression module.

splitlines(*keepends=False*)  
Return a list of the lines in the string, breaking at line boundaries.

Line breaks are not included in the resulting list unless keepends is given and true.

startswith(*prefix*\[, *start*\[, *end*\]\]) → bool  
Return True if S starts with the specified prefix, False otherwise. With optional start, test S beginning at that position. With optional end, stop comparing S at that position. prefix can also be a tuple of strings to try.

strip(*chars=None*, */*)  
Return a copy of the string with leading and trailing whitespace removed.

If chars is given and not None, remove characters in chars instead.

swapcase()  
Convert uppercase characters to lowercase and lowercase characters to uppercase.

title()  
Return a version of the string where each word is titlecased.

More specifically, words start with uppercased characters and all remaining cased characters have lower case.

translate(*table*, */*)  
Replace each character in the string using the given translation table.

> table  
> Translation table, which must be a mapping of Unicode ordinals to Unicode ordinals, strings, or None.

The table must implement lookup/indexing via \_\_getitem\_\_, for instance a dictionary or list. If this operation raises LookupError, the character is left untouched. Characters mapped to None are deleted.

upper()  
Return a copy of the string converted to uppercase.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an array, this is represented in Python by a String or UTF8String with variant_level==2.

zfill(*width*, */*)  
Pad a numeric string with zeros on the left, to fill a field of the given width.

The string is never truncated.

<!-- -->

*class *dbus.types.Struct(*iterable*, *signature=None*, *variant_level=0*)  
Bases: `tuple`

An structure containing items of possibly distinct types.

D-Bus structs may not be empty, so the iterable argument is required and may not be an empty iterable.

`signature` is either None, or a string representing the contents of the struct as one or more complete type signatures. The overall signature of the struct will be the given signature enclosed in parentheses, `()`.

If the signature is None (default) it will be guessed from the types of the items during construction.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a struct, this is represented in Python by a Struct with variant_level==2.

count(*value*, */*)  
Return number of occurrences of value.

index(*value*, *start=0*, *stop=9223372036854775807*, */*)  
Return first index of value.

Raises ValueError if the value is not present.

<!-- -->

*class *dbus.types.UInt16(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned 16-bit integer between 0 and 0xFFFF, represented as a subtype of `int`.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a uint16, this is represented in Python by a UInt16 with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.UInt32(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned 32-bit integer between 0 and 0xFFFF FFFF, represented as a subtype of `long` in Python 2 or `int` in Python 3.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a uint32, this is represented in Python by a UInt32 with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.UInt64(*value: int*\[, *variant_level: int*\])  
Bases: `_dbus_bindings._LongBase`

An unsigned 64-bit integer between 0 and 0xFFFF FFFF FFFF FFFF, subtype of `long` in Python 2 or `int` in Python 3.

`value` must be within the allowed range, or OverflowError will be raised.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a uint64, this is represented in Python by a UInt64 with variant_level==2.

as_integer_ratio()  
Return integer ratio.

Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.

    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)

bit_count()  
Number of ones in the binary representation of the absolute value of self.

Also known as the population count.

    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3

bit_length()  
Number of bits necessary to represent self in binary.

    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6

conjugate()  
Returns self, the complex conjugate of any int.

denominator  
the denominator of a rational number in lowest terms

from_bytes(*byteorder*, *\**, *signed=False*)  
Return the integer represented by the given array of bytes.

bytes  
Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Indicates whether two’s complement is used to represent the integer.

imag  
the imaginary part of a complex number

numerator  
the numerator of a rational number in lowest terms

real  
the real part of a complex number

to_bytes(*length*, *byteorder*, *\**, *signed=False*)  
Return an array of bytes representing an integer.

length  
Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes.

byteorder  
The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use \`sys.byteorder’ as the byte order value.

signed  
Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.

<!-- -->

*class *dbus.types.UnixFd(*value: int or file object*\[, *variant_level: int*\])  
Bases: `object`

A Unix Fd.

`value` must be the integer value of a file descriptor, or an object that implements the fileno() method. Otherwise, ValueError will be raised.

UnixFd keeps a dup() (duplicate) of the supplied file descriptor. The caller remains responsible for closing the original fd.

`variant_level` must be non-negative; the default is 0.

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing an Unix Fd, this is represented in Python by an Unix Fd with variant_level==2.

take() → int  
This method returns the file descriptor owned by UnixFd object. Note that, once this method is called, closing the file descriptor is the caller’s responsibility.

This method may be called at most once; UnixFd ‘forgets’ the file descriptor after it is taken.

Raises ValueError  
if this method has already been called

variant_level  
Indicates how many nested Variant containers this object is contained in: if a message’s wire format has a variant containing a variant containing a file descriptor, this is represented in Python by a UnixFd with variant_level==2.
