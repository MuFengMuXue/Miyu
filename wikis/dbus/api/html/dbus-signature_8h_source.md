dbus-signature.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-signatures.h utility functions for D-Bus types

3 \*

4 \* Copyright (C) 2005 Red Hat Inc.

5 \*

6 \* SPDX-License-Identifier: AFL-2.1 OR GPL-2.0-or-later

7 \*

8 \* Licensed under the Academic Free License version 2.1

9 \*

10 \* This program is free software; you can redistribute it and/or modify

11 \* it under the terms of the GNU General Public License as published by

12 \* the Free Software Foundation; either version 2 of the License, or

13 \* (at your option) any later version.

14 \*

15 \* This program is distributed in the hope that it will be useful,

16 \* but WITHOUT ANY WARRANTY; without even the implied warranty of

17 \* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the

18 \* GNU General Public License for more details.

19 \*

20 \* You should have received a copy of the GNU General Public License

21 \* along with this program; if not, write to the Free Software

22 \* Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

23 \*

24 \*/

25\#if !defined (DBUS_INSIDE_DBUS_H) && !defined (DBUS_COMPILATION)

26\#error "Only \<dbus/dbus.h\> can be included directly, this file may disappear or change contents."

27\#endif

28

29\#ifndef DBUS_SIGNATURES_H

30\#define DBUS_SIGNATURES_H

31

32\#include \<dbus/dbus-macros.h\>

33\#include \<dbus/dbus-types.h\>

34\#include \<dbus/dbus-errors.h\>

35

36DBUS_BEGIN_DECLS

37

46typedef struct

47{

48 void \*dummy1;

49 void \*dummy2;

50 dbus_uint32_t dummy8;

51 int dummy12;

52 int dummy17;

53} DBusSignatureIter;

54

55DBUS_EXPORT

56void dbus_signature_iter_init (DBusSignatureIter \*iter,

57 const char \*signature);

58

59DBUS_EXPORT

60int dbus_signature_iter_get_current_type (const DBusSignatureIter \*iter);

61

62DBUS_EXPORT

63char \* dbus_signature_iter_get_signature (const DBusSignatureIter \*iter);

64

65DBUS_EXPORT

66int dbus_signature_iter_get_element_type (const DBusSignatureIter \*iter);

67

68DBUS_EXPORT

69dbus_bool_t dbus_signature_iter_next (DBusSignatureIter \*iter);

70

71DBUS_EXPORT

72void dbus_signature_iter_recurse (const DBusSignatureIter \*iter,

73 DBusSignatureIter \*subiter);

74

75DBUS_EXPORT

76dbus_bool_t dbus_signature_validate (const char \*signature,

77 DBusError \*error);

78

79DBUS_EXPORT

80dbus_bool_t dbus_signature_validate_single (const char \*signature,

81 DBusError \*error);

82

83DBUS_EXPORT

84dbus_bool_t dbus_type_is_valid (int typecode);

85

86DBUS_EXPORT

87dbus_bool_t dbus_type_is_basic (int typecode);

88DBUS_EXPORT

89dbus_bool_t dbus_type_is_container (int typecode);

90DBUS_EXPORT

91dbus_bool_t dbus_type_is_fixed (int typecode);

92

95DBUS_END_DECLS

96

97\#endif /\* DBUS_SIGNATURE_H \*/

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

dbus_signature_iter_recurse

void dbus_signature_iter_recurse(const DBusSignatureIter \*iter, DBusSignatureIter \*subiter)

Initialize a new iterator pointing to the first type in the current container.

**Definition** dbus-signature.c:212

dbus_signature_validate

dbus_bool_t dbus_signature_validate(const char \*signature, DBusError \*error)

Check a type signature for validity.

**Definition** dbus-signature.c:238

dbus_type_is_basic

dbus_bool_t dbus_type_is_basic(int typecode)

A "basic type" is a somewhat arbitrary concept, but the intent is to include those types that are ful...

**Definition** dbus-signature.c:324

dbus_type_is_fixed

dbus_bool_t dbus_type_is_fixed(int typecode)

Tells you whether values of this type can change length if you set them to some other value.

**Definition** dbus-signature.c:355

dbus_type_is_valid

dbus_bool_t dbus_type_is_valid(int typecode)

Return TRUE if the argument is a valid typecode.

**Definition** dbus-signature.c:389

dbus_signature_iter_get_signature

char \* dbus_signature_iter_get_signature(const DBusSignatureIter \*iter)

Returns the signature of the single complete type starting at the given iterator.

**Definition** dbus-signature.c:117

dbus_signature_iter_next

dbus_bool_t dbus_signature_iter_next(DBusSignatureIter \*iter)

Skip to the next value on this "level".

**Definition** dbus-signature.c:169

dbus_type_is_container

dbus_bool_t dbus_type_is_container(int typecode)

A "container type" can contain basic types, or nested container types.

**Definition** dbus-signature.c:300

dbus_signature_iter_init

void dbus_signature_iter_init(DBusSignatureIter \*iter, const char \*signature)

Initializes a DBusSignatureIter for reading a type signature.

**Definition** dbus-signature.c:72

dbus_signature_validate_single

dbus_bool_t dbus_signature_validate_single(const char \*signature, DBusError \*error)

Check that a type signature is both valid and contains exactly one complete type.

**Definition** dbus-signature.c:270

dbus_signature_iter_get_current_type

int dbus_signature_iter_get_current_type(const DBusSignatureIter \*iter)

Returns the current type pointed to by the iterator.

**Definition** dbus-signature.c:97

dbus_signature_iter_get_element_type

int dbus_signature_iter_get_element_type(const DBusSignatureIter \*iter)

Convenience function for returning the element type of an array; This function allows you to avoid in...

**Definition** dbus-signature.c:151

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51

DBusSignatureIter

DBusSignatureIter struct; contains no public fields.

**Definition** dbus-signature.h:47

DBusSignatureIter::dummy12

int dummy12

Don't use this.

**Definition** dbus-signature.h:51

DBusSignatureIter::dummy2

void \* dummy2

Don't use this.

**Definition** dbus-signature.h:49

DBusSignatureIter::dummy1

void \* dummy1

Don't use this.

**Definition** dbus-signature.h:48

DBusSignatureIter::dummy8

dbus_uint32_t dummy8

Don't use this.

**Definition** dbus-signature.h:50

DBusSignatureIter::dummy17

int dummy17

Don't use this.

**Definition** dbus-signature.h:52
