dbus-address.h

1/\* -\*- mode: C; c-file-style: "gnu"; indent-tabs-mode: nil; -\*- \*/

2/\* dbus-address.h Server address parser.

3 \*

4 \* Copyright (C) 2003 CodeFactory AB

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

29\#ifndef DBUS_ADDRESS_H

30\#define DBUS_ADDRESS_H

31

32\#include \<dbus/dbus-types.h\>

33\#include \<dbus/dbus-errors.h\>

34

35DBUS_BEGIN_DECLS

36

43typedef struct DBusAddressEntry DBusAddressEntry;

44

45DBUS_EXPORT

46dbus_bool_t dbus_parse_address (const char \*address,

47 DBusAddressEntry \*\*\*entry_result,

48 int \*array_len,

49 DBusError \*error);

50DBUS_EXPORT

51const char \*dbus_address_entry_get_value (DBusAddressEntry \*entry,

52 const char \*key);

53DBUS_EXPORT

54const char \*dbus_address_entry_get_method (DBusAddressEntry \*entry);

55DBUS_EXPORT

56void dbus_address_entries_free (DBusAddressEntry \*\*entries);

57

58DBUS_EXPORT

59char\* dbus_address_escape_value (const char \*value);

60DBUS_EXPORT

61char\* dbus_address_unescape_value (const char \*value,

62 DBusError \*error);

63

76static inline void

77dbus_clear_address_entries (DBusAddressEntry \*\*\*pointer_to_entries)

78{

79 \_dbus_clear_pointer_impl (DBusAddressEntry \*, pointer_to_entries,

80 dbus_address_entries_free);

81}

82

85DBUS_END_DECLS

86

87\#endif /\* DBUS_ADDRESS_H \*/

dbus_address_entries_free

void dbus_address_entries_free(DBusAddressEntry \*\*entries)

Frees a NULL-terminated array of address entries.

**Definition** dbus-address.c:194

dbus_parse_address

dbus_bool_t dbus_parse_address(const char \*address, DBusAddressEntry \*\*\*entry_result, int \*array_len, DBusError \*error)

Parses an address string of the form:

**Definition** dbus-address.c:368

dbus_address_entry_get_method

const char \* dbus_address_entry_get_method(DBusAddressEntry \*entry)

Returns the method string of an address entry.

**Definition** dbus-address.c:232

dbus_address_unescape_value

char \* dbus_address_unescape_value(const char \*value, DBusError \*error)

Unescapes the given string as a value in a key=value pair for a D-Bus address.

**Definition** dbus-address.c:622

dbus_address_escape_value

char \* dbus_address_escape_value(const char \*value)

Escapes the given string as a value in a key=value pair for a D-Bus address.

**Definition** dbus-address.c:588

dbus_address_entry_get_value

const char \* dbus_address_entry_get_value(DBusAddressEntry \*entry, const char \*key)

Returns a value from a key of an entry.

**Definition** dbus-address.c:249

DBUS_BEGIN_DECLS

\#define DBUS_BEGIN_DECLS

Macro used prior to declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:36

DBUS_END_DECLS

\#define DBUS_END_DECLS

Macro used after declaring functions in the D-Bus header files.

**Definition** dbus-macros.h:37

DBusAddressEntry

Internals of DBusAddressEntry.

**Definition** dbus-address.c:49

DBusError

Object representing an exception.

**Definition** dbus-errors.h:51
